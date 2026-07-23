# F3 — Evidencia + Auditoría de Robustez Reportada — Ciclo C-001

> **Fecha:** 2026-07-20 · **Ejecutor:** Opus (Claude, vía búsqueda web) · **Fase:** F3 (ejecutor puro conforme F0: audita, no calcula; no evalúa rentabilidad, no rankea, no prioriza).
>
> **Esta es una VISTA generada DESDE `F3_evidencia.jsonl`** (fuente de verdad, regla dura 9 del ORQUESTADOR), **no al revés.** Si hay discrepancia, manda el JSONL. Los 30 objetos heredan verbatim todos los campos de `F2_arbol.jsonl` y añaden los campos F3 (`nivel_evidencia_final`, `estudios_independientes`, `riesgos`, `contradicciones`, `reproducibilidad_detalle`, `robustez_reportada[]`, `verificacion_web`).

## Notas de alcance (obligatorias)

1. **La asignación de mecanismo sigue siendo PROVISIONAL.** F4 la confirma o corrige con el análisis económico (`mecanismo_provisional: true` en todos los objetos). Nada aquí reasigna mecanismos.
2. **Esto NO es priorización ni validación.** No hay puntuación, ranking ni veredicto de "aprobado". La rúbrica y el scoring son de F7; el diseño experimental, de F6; el motor PIC valida, no el Banco.
3. **"No reportado" es un DATO, no un juicio de calidad.** Que una fuente no reporte bootstrap/walk-forward/Monte Carlo no la degrada por sí mismo: registra qué evidencia de robustez existe y cuál falta, para que F4-F6 lo incorporen como prueba o limitación.
4. **Niveles I-VII (F0 §4) y regla de no-promediado.** Cada entrada lleva el nivel MÁXIMO que alcanza como fuente individual; la acumulación de evidencia ocurre en el NODO de mecanismo (herencia de F2), no se promedia ni se suma dentro de una entrada. Las entradas de la familia Régimen son MÉTODO (filtro/condicionador, F0 §2): no se les asigna alfa de retorno.
5. **Verificación (reglas duras 1 y 2).** Lo verificado por búsqueda web en esta sesión se marca `verificacion_web: true`; lo apoyado solo en el conocimiento del modelo lleva `[memoria del modelo — verificar]` en el campo correspondiente. Ninguna métrica se inventa: las cifras citadas provienen de la fuente y están verificadas (p.ej. t-stat ~5 desde 1960 / ~10 desde 1800 en F1-003; carry cripto >40%/año en F1-009; Sharpe sobre ventana de 6 meses en F1-013).

## Matriz de calidad de la evidencia

Riesgos: **O**=overfitting · **DS**=data-snooping · **PB**=publication-bias · **S**=survivorship. `(r)`=reportado por la fuente · `(i)`=inferible por el auditor. Nivel: preliminar (F1) → final (F3).

| ID | Mecanismo (provisional) | Nivel F1→F3 | Estudios indep. | O / DS / PB / S | Reproducibilidad | Verif. web |
|----|----|----|----|----|----|----|
| F1-001 | Persistencia | III → **III** | 1 (nodo acumula F1-002..007) | Bajo(i) / Bajo-med(r) / Campo(i) / Bajo(i) | Media | sí |
| F1-002 | Persistencia | III → **III** | 0 indep. (mismo linaje AQR) | Bajo(i) / Bajo(i) / Med(i) / Med(i) | Baja-media | sí |
| F1-003 | Persistencia | IV → **IV** | 1 indep. (CFM ≠ AQR) | Bajo(i) / Bajo(i) / Med(i) / Med(i) | Baja | sí |
| F1-004 | Persistencia | IV → **IV** | 1 indep. (CTAs) | Bajo-med(r) / Bajo(i) / Med(i) / Med-alto(i) | Media | sí |
| F1-005 | Persistencia | III → **III** | 1 (meta/equivalencia) | Bajo(i) / Bajo(i) / Bajo-med(i) / n/a | Media | parcial |
| F1-006 | Persistencia | III → **IV ↓** | 1 | Bajo(i) / Bajo(i) / Med(i) / Bajo(i) | **Alta** | sí |
| F1-007 | Persistencia | V → **V** | 0 formales; 1 track real | Med(i) / Med(i) / Alto(i) / **Alto(i)** | Alta (reglas) | parcial |
| F1-008 | Prima de riesgo | III → **III** | 1 (unifica carry por clase) | Bajo(r) / Bajo-med(i) / Med(i) / Bajo-med(i) | Media | sí |
| F1-009 | Prima de riesgo | III → **III** (+MgmtSci) | 1 (carry cripto directo) | Bajo(i) / Bajo(i) / Bajo(i) / Med(i) | Media | sí |
| F1-010 | Prima de riesgo | IV → **IV** (teoría) | teórico | n/a / n/a / Bajo(i) / n/a | Alta (analítica) | parcial |
| F1-011 | Prima de riesgo | III → **III** (teoría) | teórico, indep. de F1-010 | n/a / n/a / Bajo(i) / n/a | Alta (analítica) | parcial |
| F1-012 | Prima de riesgo | IV → **IV** (teoría) | 1, muy reciente | Med(i) / n/v / Bajo(i) / n/a | Media | parcial |
| F1-013 | Prima de riesgo | III → **III** (salvedad venue) | 1 empírico (arb. funding) | Med(i) / Med(i) / Med(i) / Med-alto(i) | Media | sí |
| F1-014 | Sobre-reacción | III → **III** | 1 (nodo → II con 015/016) | Bajo(i) / Bajo/Alto(i) / Alto(i) / Med(i) | Alta | parcial |
| F1-015 | Sobre-reacción | III → **III** | 1 indep. de 014 | Bajo(i) / Bajo(i) / Med(i) / Med(i) | Alta | parcial |
| F1-016 | Sobre-reacción | III → **III** | 1 (evidencia matizadora) | Bajo(i) / Bajo(i) / Bajo(i) / Med(i) | Alta | parcial |
| F1-017 | Sobre-reacción | III → **III** | 1 crypto-nativo | Bajo-med(i) / Med(r) / Med(i) / **Alto(i)** | Media | sí |
| F1-018 | Sobre-reacción (frontera) | III → **III** (contradicción viva) | 1 vs ≥2 opuestos | Med(i) / **Alto(r)** / Alto(i) / **Alto(i)** | Media (momentos en disputa) | sí |
| F1-019 | Microestructura | III → **III** (teoría) | teórico fundacional | n/a / n/a / Bajo(i) / n/a | Alta (analítica) | parcial |
| F1-020 | Microestructura (frontera) | III → **III** | 1 (ILLIQ, >120 cites) | Bajo(i) / Bajo-med(i) / Med(i) / Med(i) | Alta | parcial |
| F1-021 | Microestructura | III → **III** | 1 (OFI canónico) | Bajo(i) / Bajo-med(i) / Bajo(i) / Bajo(i) | Media (req. L2) | parcial |
| F1-022 | Microestructura (frontera) | III → **III** (contradicción) | 1 vs crítica indep. | Med(i) / Med(i) / Med(i) / Bajo(i) | Media | parcial |
| F1-023 | Microestructura | IV → **IV** | 1 crypto-nativo (WP) | Bajo(i) / Bajo(i) / Bajo(i) / Bajo(i) | Baja (req. L2/L3) | sí |
| F1-024 | Microestructura | III → **III** | 1 crypto-nativo reciente | Med(i) / Med(i) / Med(i) / Med-alto(i) | Baja-media | parcial |
| F1-025 | Microestructura | III → **III** (salvedad venue) | 1 crypto-nativo (BTC/Kraken) | Bajo(i) / Bajo(i) / Med(i) / Bajo(i) | Media | parcial |
| F1-026 | Régimen | III → **III** (método) | método fundacional | n/a-método / n/a / Bajo(i) / n/a | Alta | parcial |
| F1-027 | Régimen | III → **III** (método) | 1 (aplic. tipos interés) | Bajo-med(i) / Bajo(i) / Bajo(i) / n/a | Alta | parcial |
| F1-028 | Régimen | III → **III** (método) | 1 línea (mismo grupo) | Med(i) / Med(i) / Med(i) / Bajo-med(i) | Media | parcial |
| F1-029 | Régimen | III → **III** (método) | 1 crypto-nativo reciente | Med(i) / Med(i) / Med(i) / Bajo(i) | Media | parcial |
| F1-030 | Régimen | III → **III** (método) | 1 crypto-nativo (indep. 029) | Med(i) / Med(i) / Med(i) / Bajo(i) | Media | parcial |

**Resumen de cambios de nivel vs F1:** 1 bajó (F1-006 III→IV, por venue de práctica + naturaleza de backtest público reproducible, F0 §4/§5), 0 subieron, 29 se mantuvieron. Ningún ascenso: la regla de no-promediado impide subir una entrada individual por la acumulación de evidencia del nodo.

## Resumen de robustez reportada, por familia / mecanismo

Conteo global (163 pruebas auditadas sobre las 30 entradas, 5-6 tipos por entrada): **36 "reportado" · 127 "no reportado".** Desglose por tipo de prueba: **walk-forward = 0 reportado** (30/30 no reportado); **bootstrap = 0 reportado** (30/30 no reportado); **Monte Carlo = 1** (y es método de inferencia bayesiana en F1-030, no validación de estrategia); **OOS = reportado en 6 entradas** (F1-002, F1-006, F1-024, F1-027, F1-028, y F1-003 como extensión secular); **cross-market = el tipo más reportado**; el resto de "reportado" son pruebas "otras" (subsample por década, robustez a costes, controles de factores, condicionamiento por liquidez, descomposición de fuentes).

### Persistencia (Trend following / TS momentum) — F1-001 a F1-007
- **Qué REPORTA la literatura:** cross-market amplísimo (58-71 contratos, 4 clases de activo, F1-001/004); subsample por décadas y por régimen macro (F1-002, 1880-2016; positivo cada década — verificado); extensión secular con t-stats altos (F1-003, ~5 desde 1960 / ~10 desde 1800 — verificado); robustez a costes de transacción vía modelo roll-over+rebalanceo (derivado de F1-004 — verificado); OOS internacional y actualización en tiempo real (F1-006, +20 mercados, 2009/2013 — verificado); equivalencia de especificaciones (F1-005, robustez a la forma del filtro).
- **Qué CALLA:** walk-forward formal, bootstrap y Monte Carlo: **no reportados en ninguna** entrada de la familia. OOS temporal ciego pre-registrado: ausente (la robustez se apoya en universalidad cross-activo y subperiodos, no en un hold-out ciego). Sin evidencia en cripto (0/7).
- **Reservas del auditor:** survivorship de mercados/instrumentos y de CTAs (F1-004/007) mayormente inferible; F1-002 no es replicación independiente (mismo linaje AQR); contradicción documentada sobre la significancia del TSM (Huang et al., JFE 2020) marcada `[memoria del modelo — verificar]`.

### Prima de riesgo (Carry / funding) — F1-008 a F1-013
- **Qué REPORTA:** cross-market multi-activo (F1-008: equities, bonos, commodities, treasuries, crédito, opciones — verificado); "carry crashes"/análisis de drawdown y controles de factores (F1-008); en cripto, documentación directa del carry/funding y del límite al arbitraje (F1-009, carry >40%/año — verificado); backtest de arbitraje de funding CEX vs DEX en 4 exchanges / 5 monedas (F1-013 — verificado). Fundamento teórico de pricing (F1-010/011/012): derivaciones de no-arbitraje y de anclaje estocástico del funding.
- **Qué CALLA:** OOS held-out, walk-forward, bootstrap, Monte Carlo: **no reportados** en toda la familia. Los tres papers teóricos (F1-010/011/012) no aportan evidencia empírica de retorno (por diseño). F1-013 computa Sharpe solo sobre ventanas de 6 meses (dato de funding semestral) — limitación declarada.
- **Reservas:** historia cripto corta; survivorship de exchanges/tokens; F1-012 muy reciente y sin revisión por pares (`[memoria del modelo — verificar]`).

### Sobre-reacción (Mean reversion) — F1-014 a F1-018
- **Qué REPORTA:** cross-sectional y subsample en acciones (F1-014/015/016); en cripto, battery de tests transversales y condicionamiento por liquidez (F1-017 — verificado: reversión de 1 día en ilíquidos, MOMENTUM en líquidos); controles por factores de riesgo cripto (F1-018 — verificado).
- **Qué CALLA:** walk-forward, bootstrap, Monte Carlo, OOS ciego: **no reportados** en toda la familia.
- **Reservas críticas:** (a) **F1-017**: el efecto de reversión NO sobrevive en las monedas más líquidas — decisivo para F5, ya que los perpetuos son el universo líquido. (b) **F1-018**: contradicción VIVA verificada — Grobys & Shahzad ("Cryptocurrency Momentum: Is It an Illusion?", Int. J. Finance & Economics) sostienen que la varianza sigue una ley de potencias con posible varianza infinita → t-stat/Sharpe podrían "no existir" y la prima no ser realizable; además data-snooping alto por barrido de horizontes. (c) F1-016 es la evidencia matizadora interna (parte de la ganancia contrarian es autocorrelación cruzada, no sobre-reacción pura). (d) Confounds de microestructura (rebote bid-ask) en F1-015 y efecto enero/tamaño en F1-014, `[memoria del modelo — verificar]`.

### Microestructura (Order flow / liquidez) — F1-019 a F1-025
- **Qué REPORTA:** fundamento teórico del impacto informado (F1-019, Kyle); ILLIQ en cross-section + time-series (F1-020); relación lineal OFI-precio (F1-021); toxicidad de flujo en torno al Flash Crash (F1-022); en cripto, contribución de órdenes límite/cancelaciones al price discovery en Coinbase/Binance (F1-023 — verificado), predicción OOS del corte transversal con order flow FX (F1-024, `[memoria del modelo — verificar]`), informatividad/liquidez en BTC/Kraken (F1-025).
- **Qué CALLA:** walk-forward, bootstrap, Monte Carlo: **no reportados**. Salvo F1-024, **no hay OOS de un edge de retorno explotable**: la mayoría documenta relaciones contemporáneas de formación de precio/liquidez, no señales predictivas tradeables (matiz clave para F4/F5).
- **Reservas:** familia dependiente de **order book L2/L3, NO disponible hoy en el laboratorio** (F0 §2: "probable NO-VIAJA por datos"); F1-023 sigue como working paper (verificado); contradicción sobre el poder predictivo de VPIN (Andersen-Bondarenko, `[memoria del modelo — verificar]`).

### Régimen (Detección de regímenes — FILTRO/condicionador, NO estrategia) — F1-026 a F1-030
- **Naturaleza:** todas son **método**, no edges con alfa (F0 §2). No se les asigna nivel de evidencia de retorno; se evalúa la calidad del método y su valor condicionante.
- **Qué REPORTA:** valor de pronóstico OOS del régimen vs modelo único en tipos de interés (F1-027, `[memoria del modelo — verificar]`); valor OOS de la asignación condicionada a régimen (F1-028, `[memoria del modelo — verificar]`); en cripto, modelización de regímenes de volatilidad de BTC (F1-029) y de precio de BTC (F1-030). El MCMC de F1-030 es método de inferencia, no prueba de robustez de estrategia.
- **Qué CALLA:** bootstrap, walk-forward, Monte Carlo (como validación de estrategia): **no reportados**. Las aplicaciones cripto (F1-029/030) son descriptivas (identificación de regímenes in-sample), sin backtest de un condicionador operativo.
- **Reservas:** F1-028 es un CORPUS del mismo grupo de autores → cuenta como UNA línea de evidencia, no como replicaciones independientes (no doble-conteo). Estabilidad/identificabilidad de los estados fuera de muestra es la reserva metodológica general.

## Trazabilidad de verificación

- **Verificadas por búsqueda web en esta sesión (`verificacion_web: true` en el JSONL):** F1-001, F1-002, F1-003, F1-004, F1-006, F1-008, F1-009, F1-013, F1-017, F1-018, F1-023 (**11 entradas**; núcleo trend/carry/reversión cripto-nativa + la contradicción Grobys-Shahzad). Que una entrada verificada lleve además un `[memoria del modelo — verificar]` en algún sub-detalle NO la excluye de esta lista: la marca `verificacion_web: true` es sobre la fuente, no sobre cada dato secundario. (Lista y conteo derivados directamente del campo `verificacion_web` del JSONL, fuente de verdad.)
- **Verificación parcial (`verificacion_web: parcial`):** el resto — venue/bibliografía ya verificados en F1 (`verificada: true`); el detalle de robustez se apoya en conocimiento del modelo y se marca `[memoria del modelo — verificar]`.
- **Total de menciones `[memoria del modelo — verificar]`:** 41, distribuidas en 21 de las 30 entradas.

## Fricciones de proceso registradas para C-002 (instrumentación, F0 §8)

1. **El esquema pide `nivel_evidencia_final` por entrada, pero la evidencia se hereda por NODO (F2).** Coexisten dos granularidades (entrada individual vs mecanismo consolidado). Se resolvió etiquetando la entrada por su nivel individual y describiendo la consolidación en `estudios_independientes` y en el resumen por familia — pero convendría un campo explícito `nivel_nodo_final` en el F0 del C-002 para no forzar la interpretación.
2. **La jerarquía I-VII no encaja con las entradas de tipo `metodo`/`teoria`.** Régimen (5 entradas) y los papers teóricos de pricing (F1-010/011/019/026) no tienen "alfa de retorno" que clasificar. Se usó el sufijo "(método)"/"(teoría)"; el C-002 debería formalizar una escala paralela o una marca de exención para no-edges.
3. **`robustez_reportada` con tipos fijos (OOS/WF/bootstrap/MC/cross-market) genera muchas filas "no reportado".** Es correcto (regla F3), pero infla el artefacto; un campo compacto `pruebas_no_reportadas: [...]` + solo las reportadas en detalle reduciría ruido en C-002.
4. **Verificación web exhaustiva de 30 fuentes excede el presupuesto de una sesión.** Se priorizó verificar el núcleo cripto-nativo y las cifras load-bearing; el resto quedó `parcial` con etiqueta de memoria. Para C-002: o se acota el nº de fuentes por sesión, o se separa la verificación en una sub-fase dedicada.
5. **Contradicciones vivas (F1-018 momentum-ilusión; F1-022 VPIN; F1-014/015 confounds) no tienen un campo de "estado de la disputa".** Se registraron en `contradicciones`, pero su peso para F4 (falsabilidad) sugiere un campo estructurado `contradiccion_estado: {abierta|resuelta|matiz}` en C-002.

---
*Vista generada desde `F3_evidencia.jsonl` (30 objetos). **F3 CERRADA 2026-07-21** — A-04 CONFORME (v2, `F3_DICTAMEN_A04.md`) tras una remediación (conteo de verificadas alineado al JSONL) + aprobación del IP. Contradicción C-001 (niveles I-VII vs. entradas método/teoría) → pendiente para el F0 del C-002. F4 desbloqueada.*
