# H-001 — Canal de Donchian 512 sobre perpetuos USDT

| Campo | Valor |
|---|---|
| ID | H-001 |
| Familia | Trend following (corto plazo: canal ~5.3 días) |
| Mercado | Futuros perpetuos USDT. Costes modelados: Zoomex (taker 0.06%/lado + slippage por símbolo). Datos/dry run: Binance (testnet) |
| Universo | Backtest: BTC, ETH, SOL, BCH, DOGE, HYPE · Bot (cesta operativa): BTC, ETH, SOL, BCH, DOGE |
| Estado | ⏳ EN VALIDACIÓN — **Fase A iniciada 2026-07-02 03:53:46 UTC** (acta en PREREG) |
| Pre-registro | ✅ Original del 2026-06-24, ANTES de correr el backtest — migrado a [`research/H-001-canal-donchian/prereg/`](../../../research/H-001-canal-donchian/prereg/) |
| Gobernanza de fases | [`PREREG_FASE_AB.md`](../../../research/H-001-canal-donchian/prereg/PREREG_FASE_AB.md) (ver enmienda en `CRITERIOS_FASES.md`) |
| Última actualización de ficha | 2026-07-02 (tras inventario del lab original) |

## Hipótesis económica

**Operativa (pre-registro original, 2026-06-24, antes de correr):** un canal de 512 velas de 15m (~5.3 días) captura tendencias grandes y, al operar poco, sobrevive al coste real por lado. Incluyó una predicción del investigador que resultó falsada y así se documentó.

**Económica (A-03, 2026-07-02 — formulada ex-post, con declaración de honestidad):** subreacción/rebaño en mercado dominado por flujo minorista + amplificación por cascadas de liquidación en perpetuos + límites al arbitraje conductuales (el edge lo protege el dolor del perfil de pago, no el secreto). Al otro lado pierden los que hacen fade de rupturas, los que capitulan tarde y, en términos relativos, el holder pasivo durante los colapsos. Documento completo con 5 predicciones falsables (P1 ya consistente: alfa en alts, no en BTC) y 4 señales de retiro conceptual: [`research/H-001-canal-donchian/HIPOTESIS_ECONOMICA.md`](../../../research/H-001-canal-donchian/HIPOTESIS_ECONOMICA.md).

## Definición de la señal (congelada; especificación completa en `prereg/ESPECIFICACION_OPERATIVA.md`)

Entrada: ruptura del máx/mín de 512 velas (shift 1, sin lookahead), largo y corto, con reversa. Salida: canal opuesto de 256 velas con piso catastrófico 3×ATR(14), stop recalculado por vela cerrada. Sizing live: riesgo 0.10%/trade, apalancamiento ≤3x, máx 5 posiciones, cap agregado 0.60%, kill switch diario -5%. Solo velas cerradas.

## Las 5 preguntas epistemológicas — RESPONDIDAS con evidencia

1. **¿Cómo se eligió la ventana 512?** A priori, congelada el 2026-06-24 antes del primer backtest; los parámetros de señal **no se tunearon sobre el retorno**. Pendiente declarado en el veredicto: test de sensibilidad 384/512/640 (fragilidad, no optimización) — verificar si se ejecutó.
2. **¿Cuántas configuraciones se probaron?** De señal: una (la pre-registrada). De **geometría de riesgo**: una frontera (risk/trade × vol-target × topes) explorada *después* de ver resultados, con la señal congelada (`frontier_resultados.csv`). El sizing live (0.10%) salió de esa frontera sobre la misma muestra → es una elección post-hoc declarada; mitiga que el Sharpe es invariante al sizing (~0.42 en toda la frontera).
3. **¿Lockbox íntegro?** Definido en el pre-registro (último 20%), juzgado por separado como confirmación, resultados por activo en `VEREDICTO.md`. Además: ventana no vista 2021-2023 usada como segundo OOS de régimen.
4. **¿Survivorship?** Riesgo real y parcialmente reconocido: el universo son 6 majors elegidos en 2026 (supervivientes conocidos). No hay pares delistados en la muestra. Mitigante: la tesis final es la cesta completa sin selección (selección descartada por datos, Spearman -0.90). Queda declarado como limitación.
5. **¿Datos?** Velas 15m de cache propio (origen Binance); funding modelado 0.01%/8h — **el funding real es la mayor incógnita de magnitud declarada** (con funding alto, 2024-26 queda ≈ 0).

## Resultados consolidados (fuente: `report/legacy/`)

| Métrica | Valor |
|---|---|
| Ventanas | 2024-07→2026-06 (in-sample + lockbox 20%) · 2021-2023 (no vista) · FULL 2021-26 |
| Sharpe (cesta, FULL) | ~0.42–0.43 (igual a B&H cesta) |
| Max DD @0.1%/trade | -18% vs **-88% del B&H** — la mejora real es drawdown, no Sharpe |
| Alfa anual (regresión vs cesta) | +11.6%, **t = 0.94 → NO significativa** |
| Beta / correlación | 0.006 / 0.01 → descorrelacionada (propiedad valiosa real) |
| Trades (FULL, cesta) | 1 884 · win rate 20.3% |
| Concentración | top-5 trades = 115% del neto → sin ellos, negativo (~5 trades efectivos) |
| Bootstrap (N=10 000) | Sharpe>0 en 83% · maxDD<-50% en 24% |

**Qué es (veredicto vigente del investigador):** trend-following market-neutral, descorrelacionado, con alfa positiva no significativa y extremadamente concentrada. Diversificador plausible / seguro de convexidad. **NO es edge probado.** La validación operativa valida instrumentación y ejecución, no edge (con Sharpe ~0.42 harían falta años).

## Limitaciones vigentes (declaradas)

Funding real no medido (mayor incógnita) · universo 100% cripto correlacionado ("5 activos no son 5 apuestas") · ~5 trades efectivos → robustez estadística baja por diseño del estilo · survivorship en la selección del universo · stop evaluado por vela cerrada, sin protección intrabar (limitación conocida del bot) · sizing elegido post-hoc sobre la misma muestra.

## Validación operativa (en curso)

- **Fase A (dry run):** iniciada 2026-07-02, mínimo 10 días, 6 criterios + replay offline + criterios de aborto — gobernada por `prereg/PREREG_FASE_AB.md`. Monitoreo 3 niveles (vigia.py 15 min, auditoria.py diaria 9:05, checklist semanal). Diario de incidencias activo.
- **Fase B (testnet, 1 mes):** TE ±5%, slippage mediana ≤5 bps sobre lo modelado, cero omisiones por min_notional en BTC sin decisión documentada.
- **Fase C (real ~$750):** solo si A y B aprueban todo; completar antes `RISK_POLICY.md` y criterio de retiro.

## Registro de eventos

| Fecha | Evento |
|---|---|
| 2026-06-24 | Pre-registro original: parámetros congelados + predicción del investigador (luego falsada y documentada). |
| 2026-06-24→25 | Backtest 6 activos, funding pesimista, jackknife, bootstrap, régimen 2021-23, frontera de riesgo, alfa/beta. Veredicto: diversificador no probado; cesta sin selección; sizing 0.10%. |
| 2026-07-01 | Observabilidad añadida (eventos.csv) y congelada. PREREG de Fases A/B escrito antes de acumular datos. |
| 2026-07-02 03:53 UTC | **Acta de inicio de Fase A** (trade #7 LONG BCH cruza el corte: entrada pre-corte, salida cuenta como evidencia de instrumentación). |
| 2026-07-02 | Ficha reescrita tras inventario del lab: las 5 preguntas respondidas con evidencia; docs originales migrados al repo. |
| 2026-07-02 | Hipótesis económica formulada por A-03 (ex-post, declarado): mecanismo, contraparte, 5 predicciones falsables, 4 señales de retiro conceptual. |
