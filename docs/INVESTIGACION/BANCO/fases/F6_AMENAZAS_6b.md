# F6 — Amenazas a la Validez — **Sesión 6b (REVISOR ADVERSARIAL)** — Ciclo C-001

> **Fecha:** 2026-07-23. Sesión 6b (adversarial). Ejecutor: revisor hostil de comité científico, **sin el contexto del diseñador de 6a**. Insumo: `F6_PROTOCOLOS_6a.md` (protocolos de la sesión de diseño) + `F0_PROTOCOLO.md` (§3c: la resiliencia adversarial es COMPUERTA) + `F5_transferencia.jsonl` (F1–F5) + `DATA.md` + `PROTOCOLO.md`.
>
> **Función de este documento (F0 §3c):** listar las amenazas a la validez de cada protocolo de 6a y, por cada amenaza, la **prueba o limitación que debe incorporarse** al protocolo para detectarla. Si una amenaza **no es cubrible con los datos de hoy**, la limitación queda **DECLARADA** como tal. Cada amenaza debe entrar al protocolo (como prueba o como limitación declarada) o el protocolo **no pasa a F7**.
>
> **Lo que este documento NO hace:** no reescribe el protocolo (eso es la fusión posterior 6a+6b), no calcula métricas, no rankea, **no declara conformidad de fase** (la fija A-04 + IP). No estima si "funciona": ataca la validez del diseño.
>
> **Nomenclatura:** `AC-n` = amenaza al protocolo de Carry (§2 de 6a); `AX-n` = boceto CEX-DEX (§3); `AI-n` = boceto ILLIQ (§4). Etiqueta `[NO CUBRIBLE HOY → LIMITACIÓN DECLARADA]` cuando los datos actuales no permiten una prueba y solo cabe declarar el límite.

---

## PROTOCOLO PRINCIPAL — CARRY / FUNDING (§2 de 6a, F1-008 + F1-009)

### Bloque A — Régimen que lo mata o lo invierte

**AC-1 — El período 2021–2026 ES un régimen de funding estructuralmente positivo; el resultado puede ser el régimen, no la señal.**
La hipótesis principal cosecha funding positivo (long-spot / short-perp). Casi toda la prima documentada (Schmeling–Schrimpf–Todorov: carry >40%/año) proviene del régimen alcista con demanda larga apalancada dominante. Un backtest sobre 2021–26 puede exhibir Sharpe alto **simplemente porque la ventana está dominada por funding positivo**, sin que la señal condicional (H2b) aporte nada sobre "cobrar siempre que sea positivo". El protocolo mide skewness y peor caída, pero **no exige partición por régimen de funding** ni prueba que el edge sobreviva fuera del régimen que lo genera. El período fija el resultado.
- **Prueba a incorporar:** partición del PnL neto por **régimen de funding** (p. ej. signo y nivel del funding medio del universo por mes/trimestre: positivo-alto / positivo-bajo / neutro / negativo). Reportar PnL, Sharpe y cola **por régimen**. Criterio: el edge no puede depender de un único sub-período de funding alto. Comparar explícitamente la señal condicional contra el benchmark ingenuo "cobrar siempre el funding positivo" (si no lo bate, H2b se refuta y el edge es el régimen).

**AC-2 — La "simetría" de la pata negativa (long-perp / short-spot) asume que shortear spot es factible y gratis; en setup solo-Binance puede no serlo.**
6a declara la versión simétrica para funding negativo, pero shortear spot cripto exige borrow (coste + disponibilidad) que el laboratorio solo-Binance no ha modelado. Contabilizar el lado negativo como cosechable **infla el retorno teórico** con un trade que quizá no se puede ejecutar.
- **Prueba/limitación a incorporar:** modelar el **coste y la disponibilidad de borrow del spot** para la pata negativa; **o**, si no es ejecutable hoy, restringir el protocolo a la pata cobrable (long-spot / short-perp) y **DECLARAR** que la mitad de funding negativo no es cosechable en el setup actual (limitación de alcance que reduce la muestra de eventos válidos, con impacto en AC-15).

### Bloque B — Crowding / saturación / capacidad

**AC-3 — Crowding realizado dentro de la propia muestra: el basis-trade se institucionalizó entre 2021 y 2026; el edge puede estar ya muerto al final de la ventana.**
El cash-and-carry es el trade institucional de cripto 2023–2025 (ETF de BTC spot, prime brokerage, compresión de base). La ventana mezcla el régimen pre-institucionalización (2021, funding altísimo) con el post (2024–26, comprimido). Un Sharpe agregado **sobredeclara el edge forward-looking**. El §2.7 vigila el funding medio como "retiro conceptual" a futuro, pero el protocolo **no tiene un test de decaimiento del edge dentro de la muestra**.
- **Prueba a incorporar:** PnL acumulado y funding medio realizado **por año/sub-período**, con test explícito de **tendencia decreciente monótona** hacia el final de la muestra (proxy de crowding ya materializado). Si el edge se concentra en los primeros años y se anula después, declararlo: la prima puede haber muerto antes del pre-registro.

**AC-4 — Capacidad no estimable sin order book. [NO CUBRIBLE HOY → LIMITACIÓN DECLARADA]**
Sin datos de profundidad, **cuánto capital absorbe la cesta antes de mover funding/precio es incuantificable**. Cualquier Sharpe es a capacidad → 0. El protocolo trata la falta de order book solo como problema de slippage (AC-5), no como límite de capacidad.
- **Limitación a declarar:** sin order book ni datos de profundidad/OI recolectados, **la capacidad del edge no es estimable**; el resultado vale como señal de existencia a tamaño infinitesimal, no como estrategia dimensionable. Prerrequisito Data Lake: profundidad/OI (P3) para levantar la limitación.

### Bloque C — Sensibilidad a costes

**AC-5 — El slippage propuesto (0.02–0.05%/lado) es un número inventado sin order book, y la estrategia es intensiva en turnover (2 patas × rebalanceo 8h/diario). El edge puede morir con costes realistas.** *(una de las 2–3 más letales)*
La cobertura delta-neutral toca **dos patas** (spot + perp) y **rebalancea cada 8h o diario**. Un round-trip de dos patas cada 8h implica turnover anualizado potencialmente >100%, y a taker 0.06%/lado + slippage el peaje anual puede superar el funding neto **comprimido** de los años recientes (AC-3). El G1 exige "cubrir costes" pero **no exige análisis de sensibilidad al slippage** ni prueba de que la conclusión no dependa del rebalanceo más fino.
- **Prueba a incorporar:** (a) **curva de sensibilidad** del PnL neto al slippage {0, conservador declarado, pesimista 2–3×}, reportando el **breakeven de slippage** que anula el edge; (b) **descomposición del coste por fuente** (taker apertura/cierre vs. rebalanceo delta) y **turnover anualizado** reportado; (c) test de que el edge **no dependa del rebalanceo 8h** (si solo sobrevive con rehedge fino, es artefacto de coste subestimado). Enlazar con la variante de fills pesimistas ya usada en H-001 (DATA.md).

**AC-6 — El coste de re-hedge de la pata delta escala con la volatilidad del subyacente y no está modelado; se penaliza justo cuando más importa.**
Cuando el subyacente se mueve, la pata spot y la perp se descuadran y hay que retradear —a mal precio— para restaurar la neutralidad. Un coste de rebalanceo **fijo** subestima el gasto en los episodios de alta volatilidad, que son precisamente los que preceden a los carry-crashes.
- **Prueba a incorporar:** modelar el coste de re-hedge **condicional a la volatilidad realizada** del subyacente (no fijo), y reportar el coste de cobertura en el decil de mayor volatilidad por separado.

### Bloque D — Fugas de diseño (lookahead / survivorship / contaminación)

**AC-7 — LOOKAHEAD en el funding realizado. La señal "basada en el funding realizado" usa información no conocida en t.** *(la más letal)*
6a §2.1/§2.2 define la señal sobre el **funding realizado** por período de 8h. El funding rate se **fija y se liquida al final** del período de settlement: en el instante de decidir la posición del período t solo se conoce el rate corriente/predicho, **no el que se liquidará**. Usar el funding realizado de t para posicionarse en t es lookahead directo — exactamente el sesgo que DATA.md marca como "Alto si existiera" y que H-001 neutraliza con `shift(1)` sobre velas cerradas.
- **Prueba a incorporar:** exigir que la señal use **funding conocido en t** (rate publicado/estimado al inicio del período, o `shift` explícito del funding), **nunca** el funding que se liquida en t+1. Auditar en código (replay offline, como Fase A de H-001) que la señal en t no toca información de t. Sin esta corrección, cualquier resultado positivo es sospechoso de fuga.

**AC-8 — SURVIVORSHIP letal: el universo de 5 símbolos elegido en 2026 censura los blow-ups, que son exactamente los carry-crashes que la tesis debe pagar. [NO CUBRIBLE HOY → LIMITACIÓN DECLARADA]** *(una de las 2–3 más letales)*
DATA.md declara el survivorship del universo (BTC/ETH/SOL/BCH/DOGE, majors vivos elegidos en 2026, sin delistados). Para carry esto es **más grave que para persistencia**: la estrategia cobra prima **a cambio de asumir el riesgo de cola de de-peg/blow-up**, y los símbolos que reventaron (LUNA/UST 2022, tokens de-peg) fueron eliminados del universo por no sobrevivir. Cobrar funding en LUNA justo antes de su colapso habría sido el carry-crash arquetípico — y ese símbolo **no está en la muestra**. El backtest **omite sistemáticamente los peores eventos de cola**: el Sharpe sobredeclara y la cola izquierda está censurada. Con solo 5 símbolos con funding recolectado, esto **no se puede corregir hoy**.
- **Limitación a declarar (obligatoria):** el universo censura los blow-ups; la **cola izquierda del carry está sub-muestrada por survivorship**. Todo resultado de Sharpe es un **límite superior**, y toda métrica de cola (skewness, peor caída) un **límite inferior del riesgo real**. Prerrequisito Data Lake bloqueante para levantarla: universo amplio **con delistados y su funding** (conecta con AC-11 y con el prerrequisito de H2d ya en 6a).

**AC-9 — Contaminación del "espejo spot": si la pata spot es sintética (perp − funding), la descomposición funding/base es tautológica y la pata larga no es validable.**
6a §2.3 usa la "serie espejo spot sin funding" que H-002.v2 construyó como **diagnóstico**, y marca `[verificar]` que exista serie spot alineada. El revisor ataca el supuesto de fondo: si ese "spot" se derivó del perp restándole el funding acumulado, entonces (i) la pata larga spot es **circular**, y (ii) la descomposición H2a {funding | base convergence | delta | costes} es **no-identificable** — el término de base sería mecánicamente cero o artefactual. El PnL "por funding" sería una tautología del constructo.
- **Prueba/limitación a incorporar:** exigir **precio spot independiente** (mercado spot real de Binance, no derivado del perp), verificado por símbolo. Si solo existe el espejo sintético, **DECLARAR** que la pata spot no es validable y que la descomposición base/funding (H2a) es **no-identificable** con los datos actuales → limitación **bloqueante** para H2a (dictamen A-02 debe pronunciarse sobre la procedencia de la serie spot antes de correr).

**AC-10 — Lockbox posiblemente ya contaminado: el funding de estos 5 símbolos/período ya fue inspeccionado por exp-008 y H-002.**
DATA.md: exp-008 recolectó y **evaluó** el funding real 2021–26 de los 5 símbolos (R0 ACEPTABLE), y H-002.v2 §4 usó el espejo spot. El lockbox de carry **no puede ser genuinamente ciego** sobre un dataset que ya fue tocado por experimentos previos. El protocolo advierte sobre "quemar" el lockbox (§2.6) pero **no reconoce que el dataset ya fue visto**.
- **Prueba/limitación a incorporar:** declarar explícitamente **qué sub-períodos/símbolos ya fueron inspeccionados** por exp-008/H-002 y reservar un lockbox temporal **no consultado**. Si todo el período 2021–26 ya fue inspeccionado, **DECLARAR contaminación del lockbox** (limitación) y exigir un período nuevo (mercado futuro / esperar datos) para la validación ciega — coherente con PROTOCOLO.md §5 (lockbox se abre una vez; si se tocó, está quemado).

### Bloque E — "Parece que funciona" sin funcionar

**AC-11 — Sharpe alto que oculta el carry-crash de cola, agravado porque la peor cola está fuera de muestra (AC-8). [parcialmente NO CUBRIBLE HOY]**
6a reconoce el carry-crash (E2, R3, skewness). Pero R3 depende de "incluir un escenario de de-peg/liquidación", y **el peor evento real fue censurado por survivorship** (AC-8): un Sharpe alto sobre 5 supervivientes **no puede ver el crash**. Los criterios E2/R3 son inaplicables con la cola histórica in-sample sola.
- **Prueba a incorporar:** evaluar R3 con un **escenario de estrés impuesto / sintético** (de-peg de −X% de la stablecoin de margen o de un símbolo; liquidación forzada de la pata perp; salto de funding adverso), **no solo** con la peor caída histórica. **DECLARAR** que la cola histórica está censurada y que R3 se apoya en estrés hipotético, no en frecuencia observada.

**AC-12 — PnL que es delta residual / exposición factorial disfrazado de funding. beta≈0 al símbolo no descarta beta a un factor de mercado agregado.**
H2a/E3/R1 miden beta≈0 vs. el subyacente de cada par. Pero una cesta long-spot/short-perp puede tener beta≈0 a cada símbolo y aún así **exposición neta al factor cripto agregado** (todo se mueve con BTC) o al **nivel de base/funding agregado** del mercado. El PnL parecería "carry neutral" y sería exposición factorial encubierta.
- **Prueba a incorporar:** medir beta **también contra un factor de mercado cripto agregado** (p. ej. BTC o índice de la cesta) **y contra el nivel de funding agregado**, no solo contra el subyacente par-a-par. Exigir descomposición identificable (ligada a AC-9: sin spot real, no es identificable).

**AC-13 — Sizing que explota en el pico: la pata perp corta puede liquidarse antes de que la pata spot se monetice; el backtest delta-neutral asume margen infinito.**
6a §2.3bis punto 3 reconoce el riesgo, pero el protocolo **no impone simular el margen** de la pata perp. Un backtest "delta-neutral en teoría" trata la posición como inmune a margin-call, cuando en un pinch de volatilidad la pata corta puede liquidarse a pérdida mientras la spot aún no se realiza.
- **Prueba a incorporar:** **simular explícitamente el margen de la pata perp** (liquidación forzada si el margen se agota en un movimiento adverso rápido), y **reportar cuántos períodos habrían gatillado margin-call**. No asumir la neutralidad como protección de solvencia intra-período.

### Bloque F — Falsabilidad real (¿los criterios pueden matar la hipótesis?)

**AC-14 — G1/R1 ("cubrir su propio peaje") es una compuerta puesta demasiado baja: cubrir costes no es tener edge.**
Un edge que apenas supera costes está económicamente muerto una vez que se descuenta el riesgo de cola documentado. R1 mata solo si **no** cubre costes, dejando pasar el edge marginal — que podría reportarse como "pasa G1" de forma engañosa. La compuerta no es falsadora en su tramo relevante.
- **Prueba/ajuste a incorporar:** el umbral de cobertura debe exigir **margen suficiente sobre costes para compensar el riesgo de cola** (p. ej. funding neto ≥ múltiplo del coste, no ≥ coste), o dejar la promoción condicionada únicamente a E1/E2 (Sharpe/MAR + cola) y no a G1. Documentar que G1 por sí solo no es criterio de éxito.

**AC-15 — n de eventos independientes demasiado bajo: R2 lo trata como CAP (limita confianza) cuando debería ser MATA (evidencia insuficiente para afirmar el edge).**
Con 5 símbolos, eventos de régimen de funding escasos, y la pérdida potencial de la mitad negativa (AC-2), el número de **eventos de funding efectivamente independientes** puede ser insuficiente para cualquier inferencia. Clasificarlo como CAP diluye la falsabilidad: permite "promover con baja confianza" algo estadísticamente vacío.
- **Prueba/ajuste a incorporar:** convertir el mínimo de eventos independientes en **compuerta de "evidencia insuficiente"** (ni confirma ni refuta) — elevar §2.6 punto 4 de nota a criterio, con umbral de n ratificado por el IP. Reportar el n efectivo (no nominal: descontar autocorrelación del funding, que es persistente intra-régimen).

**AC-16 — La única versión testeable hoy (serie de tiempo sobre 5 símbolos) es la forma más débil de la hipótesis; el protocolo valida lo débil y hereda la fuerza de lo no testeable.**
H2d (corte transversal) se declara no testeable con 5 símbolos — correcto. Pero lo que queda testeable (signo-y-magnitud en serie de tiempo) es **justo lo más expuesto** a confundir el régimen bull de funding con un edge (AC-1). El riesgo es que un resultado positivo de la forma débil se lea como validación del mecanismo completo.
- **Limitación a declarar:** el protocolo, con datos de hoy, **solo puede validar la forma serie-de-tiempo (la más débil)** de la hipótesis; el ranking transversal (H2d, la forma con más poder discriminante) queda **fuera de alcance** hasta el Data Lake. Ningún resultado positivo de la forma débil debe presentarse como confirmación del mecanismo de carry en general.

---

## BOCETO — ARBITRAJE FUNDING CEX vs. DEX (§3 de 6a, F1-013)

*(Ya bloqueado por prerrequisito de infra multi-venue/DEX. Amenazas a trasladar a su ficha para cuando se active.)*

**AX-1 — Evidencia base con ventana de 6 meses y survivorship de venues: no muestrea de-peg/exploit de puente.**
Werapun et al. 2025 calcula Sharpe sobre **ventanas de 6 meses** y sobre exchanges/DEX supervivientes (BitMEX, ApolloX, Drift). Ese horizonte no captura el riesgo de cola que domina el edge (liquidación, de-peg, exploit de contrato/puente del lado DEX). Un "bajo riesgo, baja correlación con HODL" a 6 meses es engañoso.
- **Limitación/prueba a incorporar (a la ficha del boceto):** cuando se active, exigir **ventana multi-año** y **riesgo de smart-contract/puente modelado**; **DECLARAR** que la evidencia actual es insuficiente en horizonte y **censurada por survivorship de venues**. Costes adicionales (gas + slippage on-chain, ventana de arbitraje estrecha) deben entrar al modelo de costes, no como nota.

**AX-2 — Comparte el mecanismo M2: hereda AC-1, AC-3, AC-5, AC-7, AC-8, AC-11 agravadas.**
El diferencial de funding entre venues es la misma prima M2 con una capa extra de riesgo. Todas las amenazas del carry principal aplican, más el riesgo de puente.
- **A incorporar:** cuando se diseñe el protocolo completo, arrastrar explícitamente las pruebas AC-1/3/5/7/8/11 y sumar el riesgo on-chain.

---

## BOCETO — PRIMA DE ILIQUIDEZ ILLIQ (§4 de 6a, F1-020)

*(Ya bloqueado por prerrequisito de datos: universo amplio con delistados. Amenazas a trasladar.)*

**AI-1 — Survivorship al alza: sin delistados, cualquier backtest de prima de iliquidez está sesgado al alza. [NO CUBRIBLE HOY → LIMITACIÓN DECLARADA]**
6a §4 ya lo anota; se refrenda como amenaza dura. Ordenar por iliquidez sin los activos que murieron (los más ilíquidos y de mayor prima aparente) sobreestima sistemáticamente el retorno del decil ilíquido.
- **Limitación a declarar:** sin histórico de **delistados**, la prima de iliquidez está **sesgada al alza por construcción**; no testeable sin universo amplio con bajas. Prerrequisito Data Lake (conecta con `ILLIQ-MR-001` en cola).

**AI-2 — Confound tamaño/liquidez en majors: F4 ya degradó el edge; en 6 majors líquidos la señal es débil y confundida con tamaño.**
La prima de iliquidez en cripto está confundida con tamaño/volumen, y su robustez fuera de microcaps es discutida `[memoria del modelo — verificar]`. En una cesta de majors todos líquidos, cualquier "señal" es probablemente proxy de tamaño.
- **Prueba/limitación a incorporar:** cuando se active, **control por tamaño obligatorio** y verificación de la magnitud de la prima en cripto (`[verificar]` pendiente de 6a); declarar que sin microcaps/universo heterogéneo la señal es débil por construcción.

---

## Cierre (handoff a la fusión 6a+6b y a A-04)

- Total de amenazas: **16 al carry (AC-1..16)**, **2 al boceto CEX-DEX (AX-1..2)**, **2 al boceto ILLIQ (AI-1..2)**.
- **No cubribles con los datos de hoy → LIMITACIÓN DECLARADA:** AC-4 (capacidad sin order book), AC-8 (survivorship que censura la cola del carry), AC-9 (si el spot es sintético, descomposición no-identificable — bloqueante, sujeto a verificación de A-02), AC-11 (cola histórica censurada; R3 solo por estrés sintético), AC-10 (lockbox posiblemente contaminado por exp-008), AC-16 (solo la forma débil es testeable), AX-1 y AI-1.
- Cada amenaza cubrible trae su **prueba a incorporar**; cada no-cubrible, su **limitación a declarar**. Ninguna se resuelve aquí: la **fusión 6a+6b** las incorpora al protocolo y **A-04 + IP** verifican que ninguna quedó fuera (F0 §3c). Sin esa incorporación, el protocolo de carry **no pasa a F7**.
- **No se declara conformidad de fase.**

---

*Fin de la pasada adversarial (6b). Revisor sin el contexto del diseñador de 6a. Documento de amenazas, no de rediseño.*
