# F6 — Diseño Experimental — **Sesión 6a (DISEÑADOR)** — Ciclo C-001

> **Fecha:** 2026-07-23. Sesión 6a del diseñador (Opus). Insumo: `F5_transferencia.jsonl` (30 objetos F1–F5).
>
> **Estado: PASADA DEL DISEÑADOR — INCOMPLETA.** Este documento es solo la primera de las dos sesiones de F6 (ORQUESTADOR, prompt F6). Los protocolos aquí NO están completos hasta que la **sesión 6b (adversarial, sesión separada sin este contexto)** liste las amenazas a la validez y cada una entre al protocolo como prueba o limitación declarada. Sin 6b incorporada, ningún protocolo pasa a F7 (F0 §3 regla c: la resiliencia adversarial es COMPUERTA, no criterio ponderado).
>
> **Lo que esta sesión NO hace (reglas duras 1–2, 6, 10):** no calcula resultados, no estima Sharpe ni retornos, no decide si "funciona", no rankea, no descarta fuera de criterio. Los umbrales numéricos de §5 son **PROPUESTAS del banco**; los ratifica (o ajusta con justificación fechada) el Investigador Principal en el pre-registro formal (regla dura 6). Toda cifra bibliográfica lleva fuente verificable; lo no verificable va etiquetado `[memoria del modelo — verificar]`. **No se declara conformidad de fase** (la fija A-04 + IP).

---

## 0. Alcance de esta sesión y clasificación de las candidatas que viajan

De `F5_transferencia.jsonl`, las candidatas con `transferibilidad.veredicto ∈ {viaja, viaja_con_condiciones}` son (verificado por lectura del artefacto):

| IDs F1 | Mecanismo | Veredicto F5 | Tratamiento en 6a |
|---|---|---|---|
| F1-001, 002, 003, 004, 006, 007 | Persistencia (M1) | `viaja` | **NO se diseña protocolo nuevo** → §1 (nota H-001) |
| F1-005 | Persistencia (meta) | `na` | Fuera de F5 (unificador de especificación, no edge) — no procede |
| **F1-008, F1-009** | **Prima de riesgo / Carry (M2)** | `viaja` | **PROTOCOLO PRINCIPAL, completo** → §2 |
| F1-013 | Carry / arb funding CEX-DEX (M2) | `viaja_con_condiciones` | **Boceto + prerrequisito de infra** → §3 |
| F1-020 | Prima de iliquidez / ILLIQ (M2/M4, frontera) | `viaja_con_condiciones` | **Boceto + prerrequisito de datos** → §4 |

El resto (F1-010/011/012 pricing de funding = `na`; F1-014..018, 021..024 microestructura/otros = `no_viaja`; F1-025..030 = `na`) queda fuera del alcance de F6 por veredicto de F5.

---

## 1. Persistencia (F1-001..004, 006, 007) — NO se re-investiga

**El mecanismo de persistencia (M1) ya es H-001 (Donchian) en el pipeline (Fase B).** F0 §2 lo fija como REFERENCIA del ciclo, no como objeto de re-investigación; la transferibilidad de F5 lo confirma citando a H-001 como implementación directa en perpetuos cripto. **No se diseña un protocolo nuevo aquí.** F7 lo tratará como redundante/complementario en el mapa conceptual (F4 dejó constancia de la redundancia para F7). Fin de la nota.

---

## 2. PROTOCOLO CANDIDATO — CARRY / FUNDING (M2) — F1-008 + F1-009

### Encabezado (formato F0 §6)

- **Mecanismo → familia → variante (árbol F2):** Prima de riesgo (M2) → Carry / funding → Cosecha de la prima de funding de perpetuos cripto (cash-and-carry delta-neutral: spot largo / perp corto cuando el funding es rico; simétrico en funding negativo).
- **Nivel de evidencia (de F3, no recalculado):** nodo M2 a nivel **II–III**. Anclas: Koijen–Moskowitz–Pedersen–Vrugt 2018 (JFE 127(2):197-225, **verificada**) = carry multi-activo, nivel III; Schmeling–Schrimpf–Todorov 2023 (BIS WP 1087 / Management Science forthcoming, **verificada**) = carry cripto-nativo con límite al arbitraje explícito, nivel III; Werapun et al. 2025 (Blockchain: Research and Applications, DOI 10.1016/j.bcra.2025.100354, **verificada**) = evidencia empírica adyacente del perfil riesgo-retorno, nivel III con salvedad de venue.
- **Distinción respecto de H-001:** captura distinta (carry/prima de riesgo) frente a tendencia (persistencia). Es el mecanismo que F0 §2 nombra como **candidata natural a H-002** por dato ya disponible. NO es una implementación de persistencia.
- **Puntuación y sensibilidad:** las asigna F7, no 6a.

### 2.1 — Hipótesis principal falsable + secundarias

> **Honestidad sobre qué es este carry (obligatoria).** El carry de un perpetuo es **cobrar o pagar funding**. La estrategia principal aquí es **market-neutral (delta-hedged): spot largo + perp corto** cuando el funding es positivo (los largos apalancados pagan; el corto perp cobra), y su simétrico (perp largo + spot corto/sin exposición) cuando el funding es negativo. **Beta objetivo ≈ 0 por construcción** (posición neta en el subyacente ≈ 0). No es una apuesta direccional al precio: es **larga de la prima de funding y corta de la volatilidad del carry** (el arbitrajista cobra la prima y asume el riesgo de cola de *carry crash* / de-peg / liquidación de exchange, F4). Cualquier versión direccional (p. ej. "ir largo del activo cuando el funding es negativo") se declara explícitamente FUERA de este protocolo principal y, de considerarse, sería una hipótesis separada con beta declarada.

**Hipótesis principal (forma si–entonces, falsable):**

> **SI** en los perpetuos cripto existe un desequilibrio estructural de flujo (demanda apalancada minorista de exposición larga) que el capital de arbitraje no cierra por límites documentados (fricciones de margen/regulación, riesgo de contraparte/de-peg, coste de custodia del spot) — condición documentada por Schmeling–Schrimpf–Todorov (F1-009) —, **ENTONCES** una señal basada en el **signo y la magnitud del funding realizado** debería generar, en una cartera **delta-neutral spot/perp** sobre el universo cripto disponible, un **retorno positivo neto de costes reales (taker + slippage) por cosecha de funding, con beta ≈ 0 respecto del subyacente**, concentrado en los regímenes de funding persistentemente alto y penalizado en los *carry crashes*.

**Hipótesis secundarias (falsables):**

- **H2a (fuente del retorno):** el PnL neto proviene predominantemente del **funding acumulado**, no de la deriva de la base spot-perp ni de exposición direccional residual. Verificable descomponiendo PnL en {funding, base convergence, delta residual, costes}.
- **H2b (condicionalidad del funding):** el funding es **adverso al promedio incondicional** — la cosecha real, condicionada por símbolo y fecha, difiere del funding medio (lección exp-008 / TEORIA v0.2, citada en H-002.v2 §4). La señal condicional debe superar a una regla de "cobrar siempre".
- **H2c (asimetría de régimen):** la prima se concentra en funding alto/estable y se invierte o desaparece en *carry crashes* (skewness negativa documentada en F1-008). La distribución de retornos debe mostrar cola izquierda pesada.
- **H2d (corte transversal — CONDICIONAL a datos):** si hubiera universo amplio, ordenar por magnitud de funding (cobrar el decil más rico / evitar el más pobre) debería dominar a la cesta equiponderada. **No testeable hoy** con 5 símbolos (ver §2.3 prerrequisito); se declara como hipótesis en espera de Data Lake.

### 2.2 — Variables independientes y dependientes

**Independientes (señal / diseño):**
- Funding realizado por símbolo y período de funding (cada 8h en Binance) — señal primaria.
- Transformación de la señal: signo del funding, magnitud, y suavizado (media móvil de funding sobre ventana corta).
- Umbral de entrada/salida en términos de funding anualizado neto de costes.
- Frecuencia de rebalanceo / roll de la cobertura delta.
- Universo (los símbolos con funding+spot disponibles).

**Dependientes (medibles, no calculadas aquí):**
- Retorno neto de la cartera delta-neutral (neto de taker + slippage + el propio funding pagado/cobrado).
- Beta realizada vs. el subyacente (debe ≈ 0) y delta residual medio.
- Sharpe y MAR/Calmar (con la salvedad de §5: la asimetría negativa hace que el Sharpe sobredeclare; por eso se exige también un criterio de cola).
- Skewness y peor caída (proxy de exposición a *carry crash*).
- Descomposición de PnL {funding | base | delta residual | costes}.
- Nº de períodos de funding cobrados / pagados; concentración del PnL.

### 2.3 — Datos mínimos vs. lo que el laboratorio TIENE (declaración de prerrequisitos)

| Campo | Necesita el protocolo | Tiene el laboratorio | Estado |
|---|---|---|---|
| Funding realizado | Sí, por símbolo y timestamp (8h) | Funding real 2021–26 recolectado **solo para los 5 símbolos de H-001** (exp-008; A-02 APTO; hashes de fábrica congelados) | **Disponible para 5 símbolos** |
| OHLCV perp | Sí | Sí | Disponible |
| Precio spot (para la pata delta-neutral) | Sí — la cobertura long-spot/short-perp lo exige | El laboratorio ya usa "espejo spot sin funding" como diagnóstico (H-002.v2 §4) → serie spot disponible para esos símbolos | **Disponible (verificar cobertura por símbolo)** `[memoria del modelo — verificar: que exista serie spot alineada para los 5 símbolos]` |
| Open Interest (OI) | Deseable (H2c / lectura de régimen de flujo) | **NO recolectado** | **Prerrequisito de datos (P3 del Data Lake)** |
| Order book / profundidad | Para modelar slippage fino de la cesta | **NO disponible** | Se sustituye por supuesto de slippage conservador declarado (ver §5) |

**Universo:** los **5 símbolos de H-001** (perpetuos USDT) para los que existe funding real congelado. Los tickers exactos deben leerse del manifiesto de exp-008 / dictamen A-02, no asumirse `[memoria del modelo — verificar: la ficha de H-001 menciona BTC, ETH, SOL, DOGE entre ellos]`.
**Período:** 2021–2026 (extensión del funding recolectado). El funding perp solo existe desde el lanzamiento de cada perp (post-2017); restricción ya declarada en H-002.v2 §4.
**Frecuencia:** nativa del funding (8h); evaluación de cartera diaria.
**Fuente:** Binance (setup solo-Binance del laboratorio), con el dataset de funding bajo dictamen **A-02 previo (APTO) con hashes congelados** antes de correr, igual que exp-008 y H-002.v2 §4.

> **PRERREQUISITO DE DATOS EXPLÍCITO (para la versión de corte transversal / H2c y H2d):** un carry **de sección cruzada** (ordenar el universo por riqueza de funding) requiere un **universo cripto amplio** con funding recolectado, no 5 majors. Con 5 símbolos, la versión testeable hoy es la **serie de tiempo / signo-y-magnitud del funding por símbolo** (H2a–H2c), no el ranking transversal (H2d). Ampliar el universo de funding es trabajo del **Data Lake** y queda como prerrequisito bloqueante de H2d. OI (P3) es prerrequisito deseable, no bloqueante del núcleo.

### 2.3bis — Riesgos de cola declarados (de F4, obligatorio)

F4 (F1-008/009) señala explícitamente los riesgos de cola de este mecanismo; entran al protocolo como **objeto de medición y como compuerta de cola**, no como nota al pie:

1. **Carry crashes** (Koijen et al. 2018, verificado F3): reversiones bruscas donde la prima cobrada se pierde en el desarme; **skewness negativa** de la familia carry. La estrategia puede exhibir "muchos meses cobrando poco, un evento devolviéndolo todo".
2. **De-peg / riesgo de contraparte-exchange:** el arbitraje spot/perp asume riesgo de que el spot (o una stablecoin de margen) se de-pegue, o de liquidación/hack del exchange. No es diversificable dentro de un solo venue (solo-Binance).
3. **Riesgo de liquidación de la pata perp** en un movimiento adverso rápido si el margen es insuficiente (aunque la posición sea delta-neutral en teoría, el margen de la pata corta puede agotarse antes de que la pata spot se monetice).

Estos tres **deben** aparecer como métricas (peor caída, skewness, escenario de de-peg) y como criterio de rechazo por cola (§5, R3). La ventana corta de la evidencia empírica (F1-013, Sharpe sobre 6 meses) implica que el riesgo de cola está **sub-muestreado** en la literatura: se traslada como amenaza para 6b.

### 2.4 — Espacio de parámetros ACOTADO (justificación económica por rango)

Espacio deliberadamente pequeño (anti-sobreajuste; N total se declara para el Deflated Sharpe, PROTOCOLO §3). Cada rango tiene justificación económica, no "de 10 a 1000":

| Parámetro | Rango propuesto | Justificación económica |
|---|---|---|
| Ventana de suavizado del funding | {1, 3, 8} períodos de 8h (= actual, 1 día, ~2.7 días) | El funding revierte a media y tiene ruido de 8h; suavizar > pocos días destruiría la señal (el funding no es persistente a semanas). Se acota por debajo de la escala del ciclo alcista. |
| Umbral de entrada (funding anualizado neto) | {0 (cobrar siempre que cubra coste), coste×1.5, coste×2} | El umbral 0-tras-costes es la frontera económica natural (cobrar solo si el funding esperado supera el taker round-trip). Múltiplos 1.5–2× prueban si exigir margen mejora la robustez sin ser arbitrarios. Nada por encima de 2× (dejaría de cobrar la mayor parte de la prima). |
| Histéresis de salida | {salir en signo cruzado, salir bajo umbral×0.5} | Evita whipsaw de rebalanceo cuando el funding oscila cerca de cero; el 0.5× es la mitad del umbral de entrada, no un parámetro libre. |
| Frecuencia de rebalanceo de la cobertura delta | {cada período de funding (8h), diario} | La cobertura se degrada con el movimiento del subyacente; rebalancear más fino que 8h multiplica costes taker sin fuente de retorno adicional (no hay funding intra-período). |
| Ponderación de la cesta | {equiponderada} fija | Con 5 símbolos, ponderar por señal (H2d) es sección cruzada → bloqueado por universo (§2.3). Se fija equiponderada para no introducir grados de libertad no soportados por datos. |

**N de configuraciones = producto de los rangos activos; se reporta obligatoriamente** (PROTOCOLO §3) como insumo del Deflated Sharpe (§5, R2). Ningún parámetro se elige "porque la curva se ve mejor" (PROTOCOLO regla anti-autoengaño 1).

### 2.5 — Criterios de éxito y de rechazo PROPUESTOS (numéricos, con lógica; ratifica el IP)

> Todos son **propuestas** (regla dura 6). Se separan en compuertas tipo **MATA** (rechaza la hipótesis) y **CAP** (limita confianza/sizing, no mata), siguiendo el patrón ya usado en H-002.v2 §3. **Los números los ratifica o ajusta el IP; el banco no impone.**

**Compuerta neto de costes reales (OBLIGATORIA, MATA) — G1:**
- Todo el análisis decisivo corre **neto de**: taker **~0.06%/lado** en cada pata y cada rebalanceo (round-trip por par de patas ≈ 0.12–0.24% según se abran/cierren ambas), **+ slippage conservador declarado** (a falta de order book, proponer p. ej. 0.02–0.05%/lado y justificarlo), **+ el funding realmente pagado/cobrado condicional por símbolo y fecha** (nunca un promedio incondicional — H2b).
- **RECHAZA (MATA) si el funding neto cosechado a lo largo de la muestra no supera el coste de transacción acumulado** (es decir, si la estrategia no "cubre su propio peaje"). Lógica: sin superar costes reales no hay edge cobrable, por definición del mecanismo (F4 lista "costes reales que superen el funding neto" como condición de muerte).

**Criterios de éxito propuestos (para promover a la siguiente etapa; conjunción):**
- **E1 (retorno ajustado por riesgo, neto):** Sharpe anualizado neto **≥ 1.0** — PROPUESTA, con la salvedad explícita de que el Sharpe **sobredeclara** en distribuciones de skewness negativa; por eso E1 **no basta solo** y se acompaña de E2.
- **E2 (robustez de cola):** MAR/Calmar neto **≥ 0.5** Y **skewness ≥ un piso a fijar por el IP** (proponer no peor que un umbral que descarte "cobrar céntimos y devolver el capital en un crash"). Lógica: el mecanismo tiene *carry crashes*; un Sharpe alto con cola izquierda catastrófica no es éxito.
- **E3 (neutralidad):** **|beta realizada| ≤ 0.1** y delta residual medio acotado. Lógica: si la estrategia gana por exposición direccional encubierta, no es carry — es beta disfrazada (H2a/H2b lo detectan).

**Criterios de rechazo propuestos (MATA / CAP):**
- **R1 (MATA):** falla G1 (no cubre costes) **o** el PnL neto se explica mayoritariamente por delta residual / deriva de base y no por funding (falla H2a). Lógica: sería otra cosa, no cosecha de funding.
- **R2 (CAP de confianza, no mata):** **Deflated Sharpe < 0** con el N de configuraciones declarado (PROTOCOLO §3), **o** n < 30 eventos de funding efectivos independientes en el tramo evaluado, **o** concentración top-k del PnL por encima de un umbral a fijar (patrón "top-5 > 50%" de H-002.v2 §3, T4). Lógica: limita sizing sin negar el edge; afirma sobre la *fuerza* de la evidencia.
- **R3 (MATA por cola):** los *carry crashes* dominan la distribución neta (Sharpe/E-criterios negativos una vez incluido un escenario de de-peg/liquidación de la stablecoin de margen o del venue). Lógica: F4 lo lista como condición de muerte ("que los carry crashes dominen la distribución").

### 2.6 — Secuencia de pruebas del pipeline PIC (PROTOCOLO.md)

Sigue el ciclo de vida `IDEA → PRE-REGISTRO → BACKTEST → OOS → LOCKBOX → (DRY RUN → TESTNET → PRODUCCIÓN)` y las Fases A/B/C:

1. **PRE-REGISTRO (antes de tocar datos):** sellar hipótesis (§2.1), universo/período (§2.3), espacio de parámetros (§2.4), particiones IS/OOS/lockbox y umbrales (§2.5) **con números ratificados por el IP**. Dictamen **A-02 previo (APTO)** sobre el dataset de funding con hashes congelados. Sellado estilo H-002.v2 §9.
2. **BACKTEST (motor determinista, con funding/comisiones/sizing reales):** correr sobre **IS** (partición temporal definida en el pre-registro, p. ej. tramo temprano) todas las configuraciones de §2.4; **registrar N total** (incluidas las fallidas) y todos los experimentos (PROTOCOLO §2).
3. **CORRECCIÓN POR PRUEBAS MÚLTIPLES:** Deflated Sharpe (o equivalente) con el N declarado (PROTOCOLO §3) → alimenta R2.
4. **OOS / walk-forward:** evaluar contra los umbrales pre-registrados (§2.5), **no contra la impresión visual de la curva** (PROTOCOLO §4). La partición se fija en el pre-registro. Dado que es baja frecuencia (funding cada 8h pero eventos-régimen escasos), incluir una **cláusula de "evidencia insuficiente"** análoga a H-002.v2 §5 (no declarar confirmada ni refutada por ausencia de datos hasta un mínimo de eventos y de tiempo, a fijar por el IP).
5. **LOCKBOX:** segmento definido en el pre-registro y **nunca consultado** durante la investigación; se abre **una sola vez**, registrando fecha/hipótesis/resultado (PROTOCOLO §5). Si la hipótesis se modifica tras abrirlo, ese lockbox queda quemado para esta familia (cuidado explícito, dada la experiencia de H-002.v1).
6. **Dictamen A-01** sobre el resultado (métricas por tramo, N, Deflated Sharpe, descomposición de PnL, métricas de cola) **antes de cualquier veredicto** (patrón H-002.v2 §6).
7. **Validación operativa Fases A/B/C** (`VALIDACION/CRITERIOS_FASES.md`) con criterios escritos antes de iniciar cada fase; el funding real y el riesgo de de-peg se vigilan en vivo (auditoría continua PnL live vs. modelo).

### 2.7 — Condiciones de retiro conceptual (derivadas de las condiciones de muerte de F4)

Qué vigilar ANTES de que el drawdown lo diga (F4 falsación de F1-008/009):

1. **Institucionalización del arbitraje de funding:** basis-trade institucional, prime brokerage cripto, ETFs con creación/redención que compriman el **funding medio por debajo de los costes** → prima agotada. Vigilar el funding medio realizado del universo.
2. **Regulación que elimine o iguale el apalancamiento minorista:** desaparece el desequilibrio de flujo que genera la prima.
3. **Funding estructuralmente ≈ 0 / neutral sostenido:** la base ancla en ~0 → no hay prima cobrable.
4. **Costes reales que superen el funding neto cobrable** (taker + slippage de la cesta + custodia del spot): la implementación muere aunque el fenómeno exista.
5. **Dominancia de carry crashes / materialización de de-peg:** si la cola izquierda pasa a dominar la distribución neta de forma sostenida, la prima no compensa el riesgo asumido → retirar.

### 2.8 — Esfuerzo de implementación estimado

**Bajo-medio** (heredado de F5): el funding ya está recolectado y bajo A-02; el motor de backtest existe (reutilizado en H-001/H-002). Falta construir la **señal de carry** y la **mecánica delta-neutral spot/perp** (nueva respecto de H-001/H-002, que son direccionales) y el modelado del riesgo de de-peg. Justificación: la novedad de ingeniería es la pata de cobertura y la descomposición de PnL, no el dato.

---

## 3. BOCETO — Arbitraje de funding CEX vs. DEX (F1-013) — `viaja_con_condiciones`

**Idea (boceto, NO desarrollar como ejecutable hoy):** explotar la **divergencia de funding entre venues** (CEX vs. DEX) cobrando el diferencial con exposición neutral. Evidencia: Werapun et al. 2025 (verificada, nivel III con salvedad de venue) reporta menor volatilidad y baja correlación con HODL, con la reserva de **ventana de datos corta (Sharpe sobre 6 meses)** y **riesgo de cola de-peg/liquidación no plenamente capturado**.

> **PRERREQUISITO BLOQUEANTE (infra):** requiere **infraestructura multi-venue con DEX** (gestión de gas, latencia on-chain, custodia, operación simultánea CEX+DEX) que el laboratorio **NO tiene** (setup solo-Binance). Costes adicionales sobre el taker: **gas + slippage on-chain**, con ventana de arbitraje estrecha. **BLOQUEADO hasta que exista esa infra.** No se especifica protocolo completo porque no es ejecutable hoy; el diseño detallado se difiere a un ciclo en que la infra DEX exista. Comparte mecanismo M2 y hereda los riesgos de cola de §2.3bis, agravados por el riesgo de contrato inteligente / puente del lado DEX.

---

## 4. BOCETO — Prima de iliquidez ILLIQ (F1-020) — `viaja_con_condiciones`

**Idea (boceto, NO desarrollar como ejecutable hoy):** la medida de Amihud `ILLIQ = |retorno| / volumen$` (Amihud 2002, JFM 5:31-56, verificada; nivel III) es **computable con OHLCV+volumen** que el laboratorio ya tiene, SIN order book. F4 la **degradó** y la reasignó de M4 a **prima de riesgo de iliquidez (M2)**: en perpetuos líquidos la prima es fina y confundida con tamaño; su robustez fuera de microcaps es discutida `[memoria del modelo — verificar]`.

> **PRERREQUISITO BLOQUEANTE (datos):** es una prima de **corte transversal** → requiere un **universo cripto amplio con activos de liquidez heterogénea (incluidos delistados, para evitar survivorship)** para poder ordenar por iliquidez. En una cesta de ~5-6 majors (todos líquidos) la señal es débil por construcción. Este universo amplio con delistados es **trabajo del Data Lake**, y conecta directamente con la candidata **`ILLIQ-MR-001` en cola** (mean-reversion sobre iliquidez). **BLOQUEADO hasta que el Data Lake provea universo amplio + histórico de delistados.** No se especifica protocolo completo hoy. Nota de survivorship: sin los delistados, cualquier backtest de prima de iliquidez estaría sesgado al alza — amenaza a trasladar a 6b si alguna vez se activa.

---

## 5. Qué falta para cerrar F6 (handoff a 6b)

- **Sesión 6b (adversarial, contexto nuevo)** debe someter el protocolo de carry (§2) a revisión hostil: qué régimen lo mata, crowding/saturación de la prima de funding, sensibilidad a costes (taker + slippage sin order book), fugas probables (lookahead en el funding realizado vs. el funding conocido en t; survivorship del universo de 5 símbolos; contaminación del "espejo spot"), y formas en que podría "parecer que funciona" sin funcionar (p. ej. Sharpe alto ocultando cola de carry-crash; PnL por delta residual disfrazado de carry). **Cada amenaza debe entrar al protocolo como prueba o limitación declarada** (F0 §3c) o el protocolo no pasa a F7.
- Los **umbrales numéricos de §2.5 son propuestas**; el IP los ratifica/ajusta en el pre-registro formal.
- **Verificaciones pendientes** marcadas `[memoria del modelo — verificar]`: tickers exactos de los 5 símbolos de H-001; cobertura de serie spot alineada por símbolo; magnitud de la prima de iliquidez en cripto; robustez de ILLIQ fuera de microcaps.

---

*Fin de la pasada del diseñador (6a). Documento incompleto hasta incorporar 6b. No se declara conformidad de fase (corresponde a A-04 + IP).*
