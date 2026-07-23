# F4 — Fundamento económico + falsabilidad popperiana — **Ciclo C-001**

> **Vista generada DESDE `F4_economia.jsonl`** (regla 9 del ORQUESTADOR: el JSONL es la fuente de verdad; este Markdown es la vista). Ejecutor de fase (Opus por política ADR-0008). Fecha de ejecución: 2026-07-23.
>
> **Alcance y límites (F0 / prompt F4).** F4 audita y razona el **fundamento económico** y la **falsabilidad** de cada mecanismo. **NO calcula, NO rankea, NO selecciona el "mejor" (eso es F7).** El análisis económico se hace a nivel de **MECANISMO** (compartido por sus variantes), no por paper. F4 **SÍ puede degradar o descartar** un edge que solo se sostenga en backtests, que no viaje, o que no pueda especificar sus condiciones de muerte. Esto **no** es priorización ni scoring. Los `tipo_F2 = teoria/meta` (pricing/fundamento) y `metodo` (régimen = filtro) **no reciben análisis de edge**.
>
> **Reglas 1-2 aplicadas:** no se inventan cifras; lo no verificable queda como `[memoria del modelo — verificar]`; se razona el fundamento, no se calcula. Referencia de calidad para las condiciones de muerte: `research/H-001-canal-donchian/HIPOTESIS_ECONOMICA.md` §5.

## Resumen de veredictos (desde el JSONL)

| Veredicto | N | Entradas |
|---|---|---|
| `fundamento_solido` | 10 | F1-001, F1-002, F1-003, F1-004, F1-006, F1-007 (Persistencia); F1-008, F1-009, F1-013 (Carry); F1-014 (Sobre-reacción LT) |
| `degradado` | 9 | F1-015, F1-016, F1-017, F1-018 (Sobre-reacción); F1-020, F1-021, F1-022, F1-023, F1-024 (Microestructura) |
| `descartado` | 1 | F1-025 (Microestructura: no es edge de retorno) |
| `no_procede_teoria_metodo` | 10 | F1-005 (meta); F1-010, F1-011, F1-012 (teoría carry); F1-019 (teoría Kyle); F1-026 a F1-030 (método régimen) |

Mecanismos con análisis de edge en alcance: **Persistencia (M1)**, **Prima de riesgo/Carry (M2)**, **Sobre-reacción/Mean reversion (M3)**, **Microestructura (M4)**. Mecanismo fuera de alcance como edge: **Régimen (M5)** — método/filtro.

> **Nota de proceso.** F4 no ordena entre los `fundamento_solido`. Que Persistencia coincida con H-001 ya en pipeline es una observación de redundancia para F7, no un descarte. Las reservas de transferibilidad concretas (p. ej. "¿la reversión sobrevive en líquidos?", "¿hay order book L2?") las **formaliza F5**; F4 solo las usa para degradar cuando la propia evidencia ya contradice el fundamento operable.

---

## M1 — Persistencia · `fundamento_solido`

**Entradas:** F1-001 (TSM, Moskowitz-Ooi-Pedersen), F1-002 (siglo AQR), F1-003 (dos siglos CFM), F1-004 (CTAs), F1-006 (SMA-10m Faber), F1-007 (Donchian/Turtle). Meta: F1-005 (ver no-procede).

1. **Mecanismo causal.** Infra-reacción inicial a la información/flujo, seguida de sobre-reacción tardía (herding); en perpetuos cripto se amplifica por apalancamiento alto y cascadas de liquidación que convierten tendencias moderadas en grandes. **CONFIRMO** la asignación provisional de F2 a Persistencia (M1).
2. **Contraparte.** Quien hace fade de rupturas/tendencias tempranas (mean-reverters en el timeframe equivocado) financia el tramo grande cuando la tendencia es real; quien capitula tarde en cascada es el combustible del tramo final.
3. **Por qué no está arbitrada.** Límite **conductual / de dolor**: perfil de pago intolerable (win rate bajo, sangrado prolongado, dependencia de pocos trades grandes). No lo protege el secreto sino el dolor psicológico e institucional (career risk de CTAs). Capacidad: la señal **satura** (F1-003 lo documenta) y el crowding la erosiona parcialmente.
4. **Regímenes (a priori, falsables).** GANA en tendencias direccionales sostenidas (expansión de volatilidad, entrada de flujo/OI nuevo, crisis con drift persistente). PIERDE en mercados laterales/choppy, whipsaw, reversiones rápidas; el funding extremo comprime el neto en longs.
5. **Condiciones de muerte (falsabilidad).**
   - Colapso sostenido de la frecuencia de tendencias multi-día (% de ventanas de N días con rango > k·ATR en mínimos históricos por 6-12 meses).
   - Institucionalización/arbitraje del universo (compresión estructural de spreads/funding, flujo profesional) → decaimiento estilo BTC.
   - Reducción estructural del apalancamiento en perpetuos (regulación / deleverage duradero) apaga el amplificador de cascadas.
   - Información instantánea y generalizada elimina la infra-reacción que la ruptura detecta.
   - Competencia/capacidad: la prima se agota (t-stats históricos elevados colapsan post-publicación de forma sostenida en OOS multi-mercado).
   - Cambio de naturaleza del pago (win rate sube a 40-50% y el payoff se desconcentra de forma sostenida) → sospechar régimen nuevo/overfit, no celebrar.
6. **Veredicto.** `fundamento_solido`. Nodo de evidencia I-II (replicación independiente multi-siglo/multi-mercado). F1-007 (Donchian/Turtle, nivel V con survivorship alto) es débil como fuente individual, pero el fundamento vive en el **nodo**, no en esa entrada. **Nota de alcance:** coincide con H-001 (persistencia/Donchian) ya en pipeline; F4 no rankea, deja la redundancia para F7.

---

## M2 — Prima de riesgo / Carry · `fundamento_solido`

**Entradas edge:** F1-008 (carry multi-activo, Koijen et al.), F1-009 (crypto carry, Schmeling-Schrimpf-Todorov), F1-013 (funding arb CEX/DEX). Teoría: F1-010, F1-011, F1-012 (ver no-procede).

1. **Mecanismo causal.** El carry (funding en perpetuos) es la compensación por proveer exposición/seguro al lado estructuralmente desequilibrado. En cripto, la demanda apalancada minorista de exposición larga presiona base/funding al alza mientras el capital de arbitraje está limitado → prima de funding alta y volátil, cobrable manteniendo exposición neutral (corto perp / largo spot). **CONFIRMO** la asignación de F2 a Prima de riesgo (M2).
2. **Contraparte.** El largo apalancado minorista que paga funding por mantener exposición direccional (y, en funding negativo, el corto apalancado); el especulador que sobre-demanda exposición/convexidad al alza.
3. **Por qué no está arbitrada.** Capital de arbitraje limitado, **documentado explícitamente en fuente cripto-nativa** (F1-009, Management Science): fricciones regulatorias, límites de margen/apalancamiento, riesgo de contraparte/exchange (de-peg, liquidación, hack), coste de custodia del spot. El arbitraje perfecto consume balance y asume riesgo de cola.
4. **Regímenes (a priori, falsables).** GANA con funding persistentemente alto y estable (mercado alcista con apalancamiento largo dominante). PIERDE en "carry crashes" (F1-008): reversiones bruscas donde la prima cobrada se pierde en el desarme; skewness negativa; riesgo de cola de de-peg/liquidación.
5. **Condiciones de muerte (falsabilidad).**
   - Institucionalización del arbitraje de funding (basis-trade institucional, prime brokerage cripto, ETFs) comprime el funding medio por debajo de costes → prima agotada.
   - Regulación que elimine el apalancamiento minorista o iguale el acceso al arbitraje → desaparece el desequilibrio de flujo.
   - Funding estructuralmente cercano a cero/neutral de forma sostenida → no hay prima cobrable.
   - Costes reales (taker + slippage de la cesta + custodia del spot) que superen el funding neto.
   - Que los carry crashes dominen la distribución (Sharpe neto negativo tras el riesgo de cola de de-peg/liquidación).
6. **Veredicto.** `fundamento_solido`. Mecanismo + contraparte + límite al arbitraje documentado en fuente cripto-nativa + evidencia empírica del perfil riesgo-retorno (F1-013). Candidata natural H-002 (dato ya disponible, F0 §2). Reserva trasladada a F6 (no degrada): ventana de datos corta de F1-013 y riesgo de cola de-peg no plenamente capturado.

---

## M3 — Sobre-reacción / Mean reversion · `degradado` (mecanismo LT `fundamento_solido`)

**Entradas edge:** F1-014 (De Bondt-Thaler, LT), F1-015 (Jegadeesh, reversión mensual), F1-016 (Lo-MacKinlay, matizador), F1-017 (Zaremba et al., reversión 1d cripto), F1-018 (Dobrynskaya, momentum/reversión cripto).

1. **Mecanismo causal.** Sobre-reacción conductual a noticias extremas (violación de Bayes; De Bondt-Thaler) que luego se revierte. **CONFIRMO parcialmente y CORRIJO/matizo** la asignación de F2: la propia evidencia de la familia muestra que buena parte del beneficio contrarian **no** es sobre-reacción idiosincrática sino **autocorrelación cruzada / lead-lag** y trading no sincrónico (F1-016), y que parte de la reversión de corto plazo es **rebote bid-ask** de microestructura (F1-015), no sobre-reacción. El mecanismo "puro" explica menos de lo que su narrativa sugiere.
2. **Contraparte.** Quien sobre-reacciona a la noticia extrema (comprador de euforia / vendedor de pánico) empuja el precio más allá del valor; en cripto, flujo minorista narrativo. El contrarian cobra por proveer liquidez a ese flujo.
3. **Por qué no está arbitrada.** Horizonte largo (F1-014): holding de años intolerable y riesgo de value trap. Horizonte corto (F1-015/017): costes de transacción y rebote bid-ask se comen la señal; en cripto la reversión de 1 día se concentra en ilíquidos, donde los costes anulan el retorno.
4. **Regímenes (a priori, falsables).** GANA en mercados fragmentados, con flujo minorista, tras choques de sentimiento extremos, en activos **ilíquidos**. PIERDE en activos líquidos/institucionalizados, donde (F1-017) el signo se **invierte a momentum**; y en horizonte corto con volatilidad/costes altos.
5. **Condiciones de muerte (falsabilidad) — varias YA OBSERVADAS en la evidencia F3.**
   - En el universo **líquido** (perpetuos = líquido) la reversión de corto plazo se invierte a momentum (F1-017, verificado): la forma operable en alcance está **falsada por su propia evidencia**.
   - Si la ganancia contrarian es atribuible a autocorrelación cruzada/lead-lag (F1-016), el mecanismo causal declarado no es el operante.
   - Si la reversión de corto plazo es rebote bid-ask (F1-015), desaparece neta de costes.
   - **Contradicción viva** (F1-018, Grobys-Shahzad): si la varianza del momentum/reversión cripto sigue una power-law de varianza infinita, Sharpe/t-stat "no existen" y la prima puede no ser realizable.
   - Institucionalización / reducción del flujo minorista narrativo elimina al sobre-reactor de contraparte.
6. **Veredicto por entrada.**
   - **F1-014 → `fundamento_solido`.** El mecanismo conductual de sobre-reacción de largo plazo (De Bondt-Thaler) tiene contraparte, límite al arbitraje y condiciones de muerte explícitas. Se marca sólido a nivel de mecanismo; que el horizonte 3-5 años (y base equity) VIAJE a perpetuos cripto lo juzga F5.
   - **F1-015 → `degradado`.** Confound de rebote bid-ask; neto de costes el edge causal se debilita.
   - **F1-016 → `degradado`.** Es el matizador: revela que el mecanismo "sobre-reacción pura" no opera solo (lead-lag + trading no sincrónico explican parte).
   - **F1-017 → `degradado` (reserva decisiva).** La reversión vive en ilíquidos; en líquidos hay momentum. Death condition **ya observada** para el alcance; F5 probablemente dictamine no-viaja para la forma reversión en líquidos.
   - **F1-018 → `degradado` (borderline descartado).** F6 DEBE incluir un test de colas/momentos como kill-switch; si la crítica de varianza infinita se confirma, pasa a `descartado`.

---

## M4 — Microestructura / Order flow / liquidez · `degradado` (1 `descartado`)

**Entradas edge:** F1-020 (ILLIQ), F1-021 (OFI, Cont et al.), F1-022 (VPIN), F1-023 (OFI cripto), F1-024 (order flow internacional), F1-025 (informatividad BTC). Teoría: F1-019 (Kyle, ver no-procede).

1. **Mecanismo causal.** El flujo de órdenes desequilibrado mueve el precio porque el market maker no distingue flujo informado de ruido y se protege (adverse selection; Kyle 1985 = fundamento). **CONFIRMO** la asignación de F2 a Microestructura (M4) con **dos correcciones de frontera:** (a) **F1-020 ILLIQ** es en rigor una **prima de riesgo de iliquidez** → reasigno su componente de retorno esperado a M2 (el de impacto/timing queda en M4); (b) **F1-022 VPIN** opera mejor como **filtro de régimen** de liquidez adversa (frontera M4/M5) que como alfa direccional.
2. **Contraparte.** El liquidity taker / uninformed trader que opera contra flujo informado; el market maker que se retira deja expuesto a quien queda dentro.
3. **Por qué no está arbitrada.** Velocidad (carrera de latencia), acceso a datos de libro (L2/L3), capacidad muy limitada (satura con poco capital), coste de infraestructura HFT.
4. **Regímenes (a priori, falsables).** GANA en episodios de desequilibrio de flujo con baja profundidad. PIERDE cuando la relación es contemporánea (no predictiva) o cuando los MM son rápidos y el spread ya incorpora el flujo.
5. **Condiciones de muerte (falsabilidad).**
   - Si la relación OFI→precio es **contemporánea y no predictiva** (F1-021 lo advierte), no hay edge tradeable — condición ya señalada por la evidencia.
   - Si VPIN no tiene poder predictivo genuino (contradicción Andersen-Bondarenko, F1-022), el filtro es artefacto de construcción.
   - Comoditización del acceso a datos de libro y de la velocidad → el edge se arbitra a coste de latencia cero.
   - Costes/latencia reales que superen el impacto capturable.
   - **Operabilidad:** ausencia de order book L2/L3 en el laboratorio hoy → no testeable (F0 §2 anticipa NO-VIAJA por datos; F5 lo formaliza).
6. **Veredicto por entrada.**
   - **F1-020 ILLIQ → `degradado`.** Corrección de frontera: prima de iliquidez (M2) más que timing de microestructura; en perpetuos líquidos la prima es fina y confundida con tamaño.
   - **F1-021 OFI → `degradado`.** Relación contemporánea (no probada como predictiva) + requiere L2. Fundamento (Kyle) sólido → degradado, no descartado; **prioridad del Data Lake**.
   - **F1-022 VPIN → `degradado`.** Poder predictivo disputado; encaja mejor como filtro de régimen.
   - **F1-023 OFI cripto → `degradado`.** Descriptivo (price discovery) y working paper; requiere L2/L3.
   - **F1-024 order flow internacional → `degradado`.** No requiere order book y reporta OOS (fortaleza), pero las afirmaciones de OOS/efecto permanente **no re-verificadas** `[memoria del modelo — verificar]` y datos especializados no confirmados públicos.
   - **F1-025 informatividad BTC → `descartado`.** No es un edge de retorno: estudia determinantes de liquidez/informatividad (un exchange, un activo), sin fuente de alfa direccional. Se descarta como EDGE por ausencia de retorno explotable, no por datos.

> **Coherencia con F0 §2.** La microestructura se incluyó "a propósito" esperando NO-VIAJA por datos, para testear la maquinaria de F5 y alimentar prioridades del Data Lake. F4 no la descarta prematuramente por datos (eso es F5): degrada por (i) forma predictiva no disponible sin L2/L3 y (ii) entradas contemporáneas o disputadas; la retiene como prioridad del Data Lake.

---

## No procede como edge (teoría / meta / método)

Estas entradas **no reciben análisis de edge** (prompt F4): son fundamento/pricing o método (filtro), no fuentes de retorno.

- **F1-005 (meta, Persistencia).** Equivalencia TSM ≡ cruce de medias móviles: robustez a la especificación que unifica variantes bajo M1 (insumo del árbol F2), no un edge de retorno. → `no_procede_teoria_metodo`.
- **F1-010, F1-011, F1-012 (teoría, Carry).** Marcos de pricing del perpetuo (no-arbitraje / anclaje estocástico / regla de feedback del funding). Dan el **fundamento** de por qué el funding ancla precio y por qué la base es media-reversiva — insumo directo del análisis de M2 —, pero no son edges. → `no_procede_teoria_metodo`.
- **F1-019 (teoría, Microestructura).** Modelo de Kyle (lambda): fundamento teórico de por qué el order flow imbalance mueve el precio. → `no_procede_teoria_metodo`.
- **F1-026 a F1-030 (método, Régimen).** Régimen = **filtro/condicionador** (F0 §2; coherente con ROADMAP: régimen solo descriptivo a 12 meses), no fuente de alfa direccional. Como condicionador puede modular otros edges (M1/M2), pero eso se diseña en F6 sobre la estrategia condicionada, no como edge autónomo. → `no_procede_teoria_metodo` (×5).

---

## Campos con `[memoria del modelo — verificar]` heredados o añadidos en F4

- **F1-024:** afirmaciones de predicción OOS y "efecto permanente" del order flow internacional no re-verificadas en F3/F4 (heredado y reiterado como reserva del veredicto `degradado`).
- Reservas heredadas de F3 (verbatim en el JSONL) que pesan en F4: F1-018 (contradicción viva Grobys-Shahzad, verificada), F1-017 (inversión reversión→momentum en líquidos, verificada), F1-022 (Andersen-Bondarenko), F1-016/F1-015 (confounds de microestructura), F1-020 (robustez de la prima de iliquidez discutida).

## Fricciones registradas para C-002 (F0 §8)

- **Frontera edge/prima/método sin campo propio.** F1-020 (M4↔M2) y F1-022 (M4↔M5) exigieron resolución de frontera dentro de `f4_razon`; convendría un campo estructurado `frontera_resuelta_F4` en el esquema.
- **Método vs edge en Régimen.** Los `metodo` no admiten análisis de edge pero sí serían condicionadores; el esquema no distingue "no procede como edge / sí procede como condicionador en F6". Candidato a ADR.
- **`degradado` agrupa causas heterogéneas** (confound causal, contemporaneidad, datos ausentes, contradicción viva, corrección de frontera). Un subcampo `causa_degradacion` (taxonomía) mejoraría el filtrado en F5/F7.
- **F4 roza F5.** Varias degradaciones se apoyan en transferibilidad/datos (order book, líquidos vs ilíquidos). La separación F4/F5 funcionó, pero conviene fijar en F0 del C-002 la regla: F4 degrada solo cuando la propia evidencia contradice el fundamento operable; el veredicto no-viaja es de F5.

---

> **F4 CERRADA 2026-07-21** — A-04 CONFORME (`F4_DICTAMEN_A04.md`). La contradicción C-001 (dos frases comparativas) la resolvió el IP retirándolas: la contraparte de M1 queda sin la coletilla del "holder pasivo", y el veredicto sin el superlativo "más fuerte del ciclo" — sin cambiar veredictos ni estructura, sin re-arbitraje. **F5 (transferibilidad) desbloqueada.**
