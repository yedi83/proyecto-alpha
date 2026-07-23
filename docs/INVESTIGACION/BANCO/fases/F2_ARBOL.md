# F2 — Árbol genealógico por mecanismos — Ciclo C-001

> **Fecha: 2026-07-20 · Ejecutor: Opus (Claude) · Fase: F2 — Árbol genealógico (ORQUESTADOR §F2)**
> Insumo: `F1_catalogo.jsonl` (30 entradas, F1 CERRADA con A-04 CONFORME). Este documento reorganiza el catálogo plano de F1 en un árbol enraizado en MECANISMOS. **De aquí en adelante, el árbol ES el catálogo del Banco:** una estrategia deja de ser "Donchian 512" y pasa a ser "implementación N de la hipótesis de persistencia".
>
> **Fuente de verdad: `F2_arbol.jsonl`** (30 objetos, un objeto por entrada = la entrada de F1 heredada **verbatim** + los campos F2: `tipo_F2` {edge/teoria/metodo/meta}, `nivel_consolidado_mecanismo`, `frontera:{es_frontera, ancla, ubicaciones}`, `mecanismo_provisional`). Este documento es una **VISTA** de ese JSONL — no al revés (regla dura 9). El JSONL se generó heredando F1 sin alterar ningún campo (**0 alteraciones verificadas**) y añadiendo únicamente lo que F2 ya consolidó en este documento; ninguna información nueva.

## Notas obligatorias de alcance

1. **La asignación de `mecanismo` es PROVISIONAL.** F4 (fundamento económico) la confirma o corrige. Los casos frontera se declaran con sus dos ubicaciones posibles, sin forzar (regla 3 del prompt F2).
2. **Esto NO es priorización ni validación.** No hay pesos, ranking ni selección de candidatas (eso es F7). No hay veredictos empíricos (eso es el pipeline PIC). F2 solo agrupa por ineficiencia y consolida evidencia.
3. **Regla de agrupamiento:** la pregunta es *¿explotan la misma ineficiencia?*, no *¿se parecen los indicadores?* (Donchian, cruce de medias y TSM son el mismo filtro lineal → un solo edge; F1-005 lo demuestra formalmente).
4. **Herencia de evidencia:** los papers de las variantes se acumulan al nodo de familia/mecanismo. El "nivel consolidado" que se anota aquí es una lectura preliminar de F2; **F3 audita la robustez reportada** y fija el nivel final. Se distingue explícitamente entre papers de **edge** (documentan el patrón/retorno) y papers de **teoría/fundamento** (explican por qué existe) — estos últimos NO cuentan como réplicas independientes del edge.

---

## El árbol (MECANISMO → FAMILIA → VARIANTE)

### M1 · PERSISTENCIA (subreacción / continuación de tendencia)
*Ineficiencia: la información se incorpora con retraso; las tendencias persisten.* **Referencia del laboratorio: H-001 (Canal de Donchian 512) es la implementación N de este mecanismo** (F0 §2: familia de referencia, no se re-investiga en C-001).

- **Familia: Trend following / TS momentum**
  - F1-001 · Time Series Momentum 1-12m multi-activo · Moskowitz, Ooi & Pedersen (2012), JFE · III
  - F1-002 · Replicación multi-siglo 1880-2016 · Hurst, Ooi & Pedersen (2017), JPM · III
  - F1-003 · Replicación dos siglos 1800-2013 · Lempérière et al. (2014), CFM/arXiv · IV
  - F1-004 · Replicación vía CTAs (71 futuros, 1978-2012) · Baltas & Kosowski (2013), SSRN · IV
  - F1-005 · **Equivalencia TSM ≡ cruce de medias (filtro lineal)** · Levine & Pedersen (2016), FAJ · III — *pieza de deduplicación: prueba que Donchian/MA-cross/TSM son el mismo edge.*
  - F1-006 · SMA 10 meses (TAA binaria) · Faber (2007), J. Wealth Mgmt · III
  - F1-007 · **Ruptura de canal Donchian 20/55 (Turtle)** · Faith (2007), libro de practicante · V — *= la señal de H-001; por herencia (vía F1-005) hereda el cuerpo de evidencia III de la familia.*

### M2 · PRIMA DE RIESGO / CARRY
*Ineficiencia: el carry (retorno esperado si el precio no cambia) compensa un riesgo; en perpetuos cripto se materializa vía funding.*

- **Familia: Carry multi-activo (general)**
  - F1-008 · Composite de carry (equities, bonos, commodities, crédito, FX, opciones) · Koijen, Moskowitz, Pedersen & Vrugt (2018), JFE · III
- **Familia: Carry / funding de perpetuos cripto** (sub-familia específica del instrumento del laboratorio)
  - *Edge (patrón/retorno documentado):*
    - F1-009 · Carry de base perp cripto (corto futuro / largo spot) · Schmeling, Schrimpf & Todorov (2023), BIS WP · III
    - F1-013 · Arbitraje de funding CEX vs. DEX · Werapun et al. (2025), Blockchain: R&A · III
  - *Teoría / fundamento (por qué existe el funding — NO son réplicas del edge):*
    - F1-010 · Marco sin arbitraje de perpetuos · He, Manela, Ross & von Wachter (2022), SSRN · IV
    - F1-011 · Precio de anclaje estocástico · Ackerer, Hugonnier & Jermann (2025), Math. Finance · III
    - F1-012 · Funding como regla de retroalimentación · Zhang (2026), SSRN · IV

### M3 · SOBRE-REACCIÓN (reversión)
*Ineficiencia: los precios sobre-reaccionan y revierten. Estructura por horizonte: reversión a muy corto plazo → momentum a horizonte medio (M1) → reversión a largo plazo.*

- **Familia: Mean reversion**
  - F1-014 · Reversión de largo plazo (3-5 años) · De Bondt & Thaler (1985), JF · III — *paper fundacional de la sobre-reacción conductual.*
  - F1-015 · Reversión de corto plazo (mensual) · Jegadeesh (1990), JF · III
  - F1-016 · Reversión vía autocorrelación cruzada (lead-lag) · Lo & MacKinlay (1990), RFS · III
  - F1-017 · Reversión 1 día en cripto, condicionada por liquidez · Zaremba et al. (2021), IRFA · III
  - F1-018 · **[CASO FRONTERA]** Momentum corto (2-4 sem) + reversión >1 mes en cripto · Dobrynskaya (2023), J. Alt. Inv. · III — *ver §Casos frontera.*

### M4 · MICROESTRUCTURA / LIQUIDEZ
*Ineficiencia: el flujo de órdenes informado y la (i)liquidez mueven el precio y/o exigen prima. Tres sub-nodos distinguibles.*

- **Familia: Impacto de order flow / formación de precio** (order flow → precio)
  - F1-019 · Modelo insider/noise/market-maker · Kyle (1985), Econometrica · III — *teoría fundacional del impacto.*
  - F1-021 · Order Flow Imbalance (OFI), impacto lineal · Cont, Kukanov & Stoikov (2014), JFEc · III
  - F1-023 · OFI en exchanges centralizados cripto · Alexander et al. (2024), SSRN · IV
  - F1-024 · Order flow internacional → corte transversal cripto · Anastasopoulos et al. (2026), J. Fin. Markets · III
  - F1-025 · Informatividad del trade flow, LOB de Bitcoin · Westland (2021), PLOS ONE · III
- **Familia: Iliquidez como prima / toxicidad de flujo**
  - F1-020 · **[CASO FRONTERA]** ILLIQ (prima de iliquidez) · Amihud (2002), J. Fin. Markets · III — *ver §Casos frontera (frontera con M2).*
  - F1-022 · **[CASO FRONTERA]** VPIN, toxicidad de flujo · Easley, López de Prado & O'Hara (2012), RFS · III — *ver §Casos frontera (frontera con M5).*

### M5 · RÉGIMEN (como FILTRO/condicionador, NO estrategia)
*No es una fuente de alfa autónoma: es un conmutador que condiciona a otras señales (F0 §2 + ROADMAP: régimen solo descriptivo en 12 meses). La evidencia aquí respalda que la DETECCIÓN de régimen es factible y está documentada, no que genere retorno por sí sola.*

- **Familia: Detección de regímenes (Markov-switching / HMM)**
  - F1-026 · Markov-switching 2 estados sobre series no estacionarias · Hamilton (1989), Econometrica · III — *método econométrico fundacional.*
  - F1-027 · Cambios de régimen en tipos de interés · Ang & Bekaert (2002), JBES · III
  - F1-028 · Asignación de activos condicionada a régimen (HMM) · Nystrup, Madsen & Lindström (2018), Quantitative Finance · III
  - F1-029 · MS-GARCH + HMM para volatilidad de Bitcoin · Shakourloo & Azimli (2026), Res. Int. Bus. Fin. · III
  - F1-030 · MCMC bayesiano + HMM para régimen de precio de BTC · Paulavičius (2025), Mathematics (MDPI) · III

---

## Tabla de herencia de evidencia (consolidación por mecanismo)

| Mecanismo | Variantes | Papers de edge | Grupos independientes | Nivel máx. individual | **Nivel consolidado (prelim. F2; F3 confirma)** |
|---|---|---|---|---|---|
| M1 Persistencia | 7 | 6 (excl. la de equivalencia como meta) | ≥5 (Pedersen/AQR, CFM/Bouchaud, Imperial, Faber, practicantes Turtle) | III | **I–II candidato** — réplicas independientes multi-mercado y multi-siglo (1800-2016), ≥5 grupos; alto volumen e independencia de evidencia. (El ordenamiento entre mecanismos es F7, no F2.) |
| M2 Carry | 6 | 3 de edge (008, 009, 013) + 3 de teoría | 3 de edge | III | **II–III** — Koijen (general, multi-activo, cerca de I-II) sólido; la parte cripto-perp específica es III pero reciente/fina. Teoría (010-012) sustenta plausibilidad, no suma como réplica. |
| M3 Sobre-reacción | 5 | 5 | ≥4 (De Bondt-Thaler, Jegadeesh, Lo-MacKinlay, autores cripto) | III | **II** — tres seminales independientes en JF/RFS + extensión cripto; estructura por horizonte coherente. |
| M4 Microestructura | 7 | 6 (+ Kyle como teoría) | ≥5 | III | **III** — teoría fundacional sólida (Kyle) + OFI bien documentado; como edge PREDICTIVO en cripto es reciente (2024-2026). |
| M5 Régimen (filtro) | 5 | n/a (no es edge de alfa) | ≥4 | III | **Método I–II / alfa n/a** — la detección de régimen es econometría establecida (Hamilton); su valor aquí es como filtro, no como fuente de retorno. |

*Nota: los "niveles consolidados" son lectura preliminar de F2 por acumulación de fuentes; la regla de no-promediado de F0 §4 se respeta (el nivel es el máximo alcanzado por réplicas independientes, no un promedio). F3 audita la robustez reportada y sella el nivel final.*

---

## Casos frontera (declarados con doble ubicación, sin forzar — regla 3)

- **F1-018 (Dobrynskaya 2023) — entre M1 (Persistencia) y M3 (Sobre-reacción).** Documenta *momentum* a horizonte corto (2-4 semanas) **y** *reversión* a horizonte >1 mes en el mismo activo cripto. No es un error de clasificación: es la evidencia empírica de que persistencia y sobre-reacción son el **mismo fenómeno a distinto horizonte**. Se ancla provisionalmente en M3 pero se anota su pata de momentum en M1. F4 decide el tratamiento.
- **F1-020 (Amihud 2002, ILLIQ) — entre M4 (Microestructura) y M2 (Prima de riesgo).** La iliquidez es a la vez un fenómeno de microestructura y una **prima de riesgo priceada** (los activos ilíquidos exigen retorno extra). Provisionalmente en M4; frontera con M2 anotada.
- **F1-022 (VPIN, Easley et al. 2012) — entre M4 (Microestructura) y M5 (Régimen).** La toxicidad de flujo es una señal de **régimen de liquidez adverso**: microestructura por construcción, régimen por función (candidato a filtro). Provisionalmente en M4; frontera con M5 anotada.

---

## Conexión con el pipeline (trazabilidad, no priorización)

- **H-001** = implementación de **M1 (Persistencia)** vía Donchian (F1-007). Por la equivalencia de F1-005, hereda el cuerpo de evidencia III de la familia trend-following. Ya está en el pipeline (Fase B); el ciclo lo usa como referencia, no lo re-investiga.
- Los mecanismos M2 (carry), M3 (reversión) y M4 (microestructura) capturan ineficiencias **distintas** de la tendencia; M5 es un condicionador transversal. La lectura de complementariedad/redundancia y la selección de candidatas es **F7**, no F2.

---

## Fricciones de proceso registradas (instrumentación del ciclo, F0 §8)

1. **Edge vs. teoría en la herencia de evidencia.** La familia carry mezcla papers que documentan el *retorno* (edge) con papers que modelan el *funding* (teoría). Contarlos juntos inflaría el nivel de evidencia. Se separaron explícitamente; sugerencia para el F0 del C-002: añadir un campo `tipo: edge|teoria|metodo` al esquema de F1 para que la distinción sea estructural desde el origen.
2. **Niveles I–II emergen recién aquí.** Confirmado el hallazgo de F1: ningún paper individual alcanza I-II, pero la **consolidación** de M1 (multi-siglo, multi-mercado, ≥5 grupos) sí es candidata a I-II. Es exactamente el trabajo que F2/F3 deben hacer y que F1 no podía.
3. **Régimen no encaja en la métrica de "nivel de edge".** M5 tiene evidencia sólida como *método* pero es n/a como *fuente de alfa*. El esquema actual no distingue "nivel de evidencia del método" de "nivel de evidencia del edge de retorno"; anotado para el F0 del C-002.

> **F2 CERRADA (2026-07-20)** — dictamen A-04 **CONFORME** (v3, `F2_DICTAMEN_A04_v2.md`) tras producir el JSONL y eliminar la frase de ranking; aprobada por el IP. Observaciones O-1 (subdivisión de familia en la vista) y C-001 (contradicción del ORQUESTADOR sobre el JSONL de F2) → pendientes para el F0 del C-002. **F3 desbloqueada.**
