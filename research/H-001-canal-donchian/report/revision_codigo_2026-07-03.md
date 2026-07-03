# Revisión adversarial de código — live_bot.py vs ESPECIFICACION vs backtest_donchian512.py

> Fecha: 2026-07-03. Revisor: sesión Fable 5 (rol A-01 sobre código). Alcance: lógica de señales, sizing, stops, costes, funding, observabilidad y bucle. Modo: solo lectura; nada del sistema vivo se toca.

## DICTAMEN GLOBAL

**La lógica de señal del bot es idéntica a la del backtester** — mismas fórmulas de canal (rolling 512/256 con shift(1)), mismo ATR (SMA 14 del TR), mismo congelado del ATR de entrada, misma precedencia stop→reversa→entrada, misma posibilidad de reversa en la misma vela. **No hay divergencias bloqueantes para la Fase A.** Hay 3 hallazgos de severidad media que afectan al diseño del replay y a la preparación de Fase B, y varios menores.

## Hallazgos

### M1 — 🟠 Omisión de BTC por min_notional en Fase B es casi CIERTA con el capital actual (cuantificado)

Con equity $750 y riesgo 0.10%, el tamaño de BTC sale ≈ `750×0.001/(3×ATR₁₆₉) ≈ 0.0015 BTC ≈ $86-90` de notional. El mínimo de Binance futures para BTCUSDT es **$100**. Consecuencia: **toda señal de BTC será omitida (o rechazada) en testnet/real.** El PREREG ya contempla esto (criterio B3: la decisión se toma documentada antes de C) — este hallazgo lo convierte de "posible" a "seguro", así que **la decisión puede tomarse YA**: subir capital de la fase B (~$1 200 da margen), aceptar cesta de 4, o reducir a BTC su riesgo mínimo viable. Nota adicional: el guard usa `limits.cost.min` de ccxt con default 5.0 si falta — verificar en testnet que ccxt puebla el mínimo real de BTC; si no, el bot enviaría la orden y sería rechazada **sin evento propio** (gap ya conocido y pospuesto en la especificación).

### M2 — 🟠 Vela saltada = señal/stop potencialmente invisible para el bot (diseño del replay)

El bot evalúa **solo la última vela cerrada** por ciclo. Si la API atrasa una vela (evento `vela_atrasada`, ya visto con BCH) y luego publica dos, la vela intermedia **nunca se evalúa**: una ruptura o un toque de stop ocurrido en ella se pierde en silencio (el stop se re-evalúa en la siguiente con datos nuevos; la entrada perdida ni se registra como omitida — el bot no la vio). El replay offline (criterio 1 de Fase A) evalúa TODAS las velas, así que **detectará estas divergencias: deben cruzarse contra los eventos `vela_atrasada` para clasificarlas como "explicadas"** en vez de como fallo de instrumentación. Frecuencia esperada: baja (feed testnet la infla; no extrapolable). No es bug a corregir en fase: es limitación conocida a documentar en el informe de cierre.

### M3 — 🟠 La curva de equity del backtester por activo subestima el drawdown intra-trade

`eqc[i] = eq + units*(c[i]-c[i-1])*pos` marca a mercado solo el incremento de UNA vela, no el PnL abierto acumulado desde la entrada. El PnL realizado es correcto (eq se actualiza bien al cerrar), pero la CURVA con la que se calculan **maxDD y Sharpe por activo en VEREDICTO.md** no acumula pérdidas latentes → maxDD por activo probablemente subestimado. Mitigante importante: los análisis de cesta/robustez posteriores corrigieron el MtM explícitamente ("bug de solo-cerradas corregido") y las decisiones finales (sizing, frontera) salieron de esos, no de este. Implicación: **no re-abrir el backtest congelado**; anotar que los maxDD por activo del veredicto inicial son optimistas y que las cifras de referencia son las de la cesta corregida.

### Menores (m4–m9)

- **m4.** Redondeo de qty: `round(units, step)` cuando la precisión es entera usa redondeo bancario de Python → puede redondear hacia ARRIBA (riesgo marginalmente > 0.10%). El caso `step` float usa floor (conservador). Impacto: bps del riesgo objetivo.
- **m5.** `eventos.csv` campo `precio` tiene semántica dual: en `ejecutada` es el fill; en `omitida` es el close de la vela. Documentado aquí para el replay; añadir al contrato 5a en la próxima edición de CONTRATOS.md.
- **m6.** Kill switch **inerte en DRY** por diseño (equity fijo + reset por ciclo, comentado en código): la Fase A no ejercita eventos `kill_switch`/`cap_riesgo_agregado`; la B sí. Además, con parámetros actuales el cap agregado (0.6%) nunca actúa antes que el máximo de 5 concurrentes (5×0.1%=0.5%≤0.6%) — rama efectivamente muerta salvo cambio de parámetros; conforme a especificación.
- **m7.** Funding en DRY se estima con `rate × units × entry_px` (precio de entrada, no mark price del momento del funding) — aproximación razonable, declararla en el informe de fase.
- **m8.** Reconciliación adopta posiciones del exchange con el ATR **actual** (no el de entrada) → stop aproximado tras recuperación (el propio log lo declara). Aceptable; anotar si ocurre durante la fase.
- **m9.** Sizing en DRY no compone (equity fija 750) mientras el modelo compone — despreciable a 10 días; relevante solo si la fase se extendiera mucho.

## Divergencias CONOCIDAS confirmadas (ya declaradas en docs, sin sorpresa)

Sizing backtest 0.5% vs live 0.10% (frontera) · backtest por activo sin funding (funding_apply/cesta lo añadieron) · fills de stop optimistas en backtest vs market real (la Fase B mide el exceso) · TE con sesgo positivo en DRY (fees=0).

## Consecuencias operativas (qué hacer con esto)

1. **Ahora:** tomar la decisión de capital para BTC (M1) y documentarla — desbloquea el criterio B3 antes de que muerda.
2. **Replay offline:** debe (a) usar parámetros LIVE (0.10%, caps de cartera), no los del backtest; (b) evaluar toda vela y clasificar divergencias contra eventos `vela_atrasada` (M2); (c) conocer la semántica dual de `precio` (m5).
3. **Informe de cierre de Fase A:** citar m6-m9 como limitaciones de cobertura del DRY (lo que la fase NO pudo ejercitar).
4. **Nada del sistema vivo se toca.** Ningún hallazgo alcanza el umbral de "corrección crítica" del PREREG.
