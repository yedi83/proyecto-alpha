# Changelog

## 2026-07-23 (2) — Candidata ILLIQ-MR-001 (H-003) registrada en cola (no ejecutar)

- Del insight del IP (reversión de corto plazo **condicional a la iliquidez**; Zaremba et al., >3.600 criptoactivos: reversión en ilíquidas, momentum en líquidas). Consistente con la frontera M2/M4 de ILLIQ y F1-017 que el Banco ya marcó en F2/F4, y con el veredicto de F5 (ILLIQ `viaja_con_condiciones`: requiere universo amplio). Ficha: `docs/INVESTIGACION/BANCO/COLA_CANDIDATAS/ILLIQ-MR-001.md`.
- **Precisión central (IP):** NO asumir que ILLIQ *causa* la reversión. Null por defecto = **artefacto** (bid-ask bounce, stale prices, microestructura, sesgos de medición); la carga de la prueba es demostrar un edge real por encima. Compuertas de diseño: **cosechabilidad neta de impacto por quintil** (la iliquidez que crea la señal la come); controles de artefacto; ILLIQ **rolling** (no etiqueta fija); sin sesgo de supervivencia (incluye delistados); OOS. Universo estratificado A-D; extremo-ilíquido (D) solo como sensibilidad.
- **Decisión del IP:** candidata **en cola post-C-001** + **prioridad de Data Lake** (universo amplio estratificable + delistados + QA). **NO ejecutar** sobre el universo actual; **NO modificar F4/F5 ni abrir ADR**; formalizar como H-003 en C-002 solo tras definir universo + PREREG. F5 no se toca — la candidata es coherente con su veredicto (`viaja_con_condiciones`), no lo contradice. Valor si prospera: M3 no se descarta, se reconceptualiza como **edge condicional a la liquidez** (condicionador de régimen momentum↔reversión).

## 2026-07-23 — C-001 F5 EJECUTADA (transferibilidad a perpetuos cripto)

- **F5 ejecutada** (Opus, **directamente en la sesión principal** por límite de presupuesto de la cuenta — el subagente web se cortó a mitad; se ejecutó sin él. Afirmaciones estructurales apoyadas en conocimiento establecido + la evidencia ya verificada por web en F1-F4; lo dudoso etiquetado `[memoria del modelo — verificar]`). Producto: `fases/F5_transferencia.jsonl` (30 objetos = F4 heredado **verbatim, 0 alteraciones** + campo `transferibilidad{ingredientes, ingredientes_en_cripto, costes_liquidez, veredicto, condiciones, datos_infra, esfuerzo}`) + vista `F5_TRANSFERENCIA.md`. JSONL desde el inicio.
- **Veredictos: 8 viaja · 2 viaja_con_condiciones · 9 no_viaja · 11 n/a.**
  - **VIAJA:** persistencia (F1-001..007; ya es H-001, con OHLCV+funding que tienes) y carry (F1-008/009; el funding ES el carry, nativo del instrumento).
  - **VIAJA c/ condiciones:** F1-013 (arb funding CEX/DEX → requiere infra DEX inexistente); F1-020 ILLIQ (computable con volumen sin order book, pero requiere universo amplio).
  - **NO VIAJA:** M3 sobre-reacción (horizonte 3-5a incompatible con perp; la reversión de corto plazo se **invierte a momentum en el universo líquido**; varianza infinita en F1-018) y M4 microestructura (requiere order book L2/L3 que el laboratorio NO tiene; F0 §2 lo anticipó).
- Lectura del embudo (F5, **no** priorización): viajan limpiamente **persistencia** (=H-001, redundante) y **carry/funding** (el más nativo y el más distinto de H-001). La selección la decide F7.
- **F5 EJECUTADA, no CERRADA:** pendiente dictamen A-04 independiente + aprobación IP antes de F6. **El A-04 exige un subagente independiente (sesión aparte, dieta mínima) → requiere el presupuesto desbloqueado.**

## 2026-07-21 (3) — C-001 F4 CERRADA (A-04 CONFORME + aprobación del IP)

- **Dictamen A-04 sobre F4 = CONFORME, 0 violaciones** (`fases/F4_DICTAMEN_A04.md`). El árbitro verificó específicamente los 7 aspectos que el IP pidió escrutar (lenguaje de alcance, no sobre-generalizar M2, no preempción de F5/F6, degradaciones vs F5, falsabilidad sustantiva, fidelidad vista↔JSONL); 6 salieron limpios.
- Reportó **C-001** (contradicción, no violación): dos frases comparativas — (a) la contraparte de M1 con la coletilla "el holder pasivo paga el drawdown que la estrategia esquiva" (comparación de desempeño, no identificación de contraparte); (b) "nodo de evidencia más fuerte del ciclo" (superlativo cross-mecanismo, mismo patrón que fue violación en F2).
- **Resolución del IP:** corregir ambas frases **sin re-arbitraje** (solo se retira lenguaje que A-04 señaló; no cambia veredictos ni estructura). JSONL (las 7 entradas de M1) + vista corregidos; verificado: 0 apariciones, 0 campos de F3 alterados. → **F4 CERRADA.**
- **F5 (transferibilidad: cadena mecanismo→ingredientes→¿viaja a perpetuos cripto? + datos/infra requerida, Opus) DESBLOQUEADA.**

## 2026-07-21 (2) — C-001 F4 EJECUTADA (fundamento económico + falsabilidad, filtrado por mérito)

- **F4 ejecutada** (Opus). Producto: `fases/F4_economia.jsonl` (30 objetos = F3 heredado **verbatim, 0 alteraciones** + campos F4: `fundamento`{mecanismo_causal, contraparte, límites_arbitraje, regímenes}, `falsacion[]` condiciones de muerte, `f4_veredicto`, `f4_razon`) + vista `F4_ECONOMIA.md`. JSONL producido desde el inicio.
- Análisis **a nivel de MECANISMO** (M1-M4; M5 Régimen fuera como edge). F4 filtra por fundamento + falsabilidad (**sí degrada/descarta, no rankea**):
  - **`fundamento_solido`: 10** → M1 Persistencia (incl. Donchian/H-001, F1-007), M2 Carry (F1-008/009/013), y F1-014 (sobre-reacción de largo plazo, mecanismo conductual sólido).
  - **`degradado`: 9** → M3 (la reversión de corto plazo se invierte a **momentum en el universo líquido** = los perpetuos; contradicción viva de varianza infinita F1-018; confounds lead-lag/bid-ask) + M4 microestructura (OFI contemporáneo, no predictivo; sin order book L2/L3).
  - **`descartado`: 1** → F1-025 (estudio de determinantes de liquidez, no edge de retorno).
  - **`no_procede` (teoría/método): 10.**
- **Correcciones de asignación** (F4 confirma/corrige F2): M3 reinterpretada (parte del efecto es lead-lag/rebote bid-ask, no sobre-reacción pura); **F1-020 ILLIQ → prima de iliquidez (M2)**; **F1-022 VPIN → filtro de régimen (M5)**.
- Verificado: **0 campos de F3 alterados; 0 edges en alcance sin condiciones de muerte** (falsabilidad obligatoria cumplida). Reserva viva `[memoria del modelo — verificar]`: F1-024 (afirmaciones OOS no re-verificadas).
- Fricciones para C-002: subcampo `causa_degradacion`; campo `frontera_resuelta_F4`; fijar la regla operativa aplicada (F4 degrada solo cuando la evidencia contradice el fundamento operable; el veredicto "no viaja" es de F5).
- **F4 EJECUTADA, no CERRADA:** pendiente dictamen A-04 independiente + aprobación del IP antes de abrir F5.

## 2026-07-21 — C-001 F3 CERRADA (A-04 CONFORME + aprobación del IP)

- Tras una remediación —la vista subcontaba las entradas verificadas por web (10 → **11**, alineado al JSONL fuente de verdad; faltaba F1-008)— F3 obtuvo dictamen A-04 **CONFORME** (v2, `fases/F3_DICTAMEN_A04.md`; el árbitro reconció todos los agregados objeto a objeto). **Aprobada por el IP → F3 CERRADA.** Rastro conservado: v1 NO CONFORME + v2 CONFORME.
- **Pendiente para el F0 del C-002:** C-001 — la escala de niveles I-VII (definida "por edge") no encaja con las entradas tipo `metodo`/`teoria` (Régimen, teóricas), que igualmente portan `nivel_evidencia_final`. Ya declarada por F3 como fricción, confirmada por A-04, no bloqueante (regla 8 de inmutabilidad).
- **F4 (fundamento económico + falsabilidad popperiana, Opus) DESBLOQUEADA** para cuando el IP quiera (≤30%). F4 es donde se decide, con el análisis económico, cuáles de estos mecanismos merecen de verdad convertirse en hipótesis.

## 2026-07-20 (6) — C-001 F3 EJECUTADA (evidencia + auditoría de robustez, 30 edges)

- **F3 ejecutada** (Opus + búsqueda web). Producto: `fases/F3_evidencia.jsonl` (30 objetos = F2 heredado **verbatim, 0 alteraciones** + campos F3: `nivel_evidencia_final`, `estudios_independientes`, `riesgos`{overfitting/data-snooping/publication-bias/survivorship, reportado vs inferible}, `contradicciones`, `reproducibilidad_detalle`, `robustez_reportada[]`, `verificacion_web`) + vista `F3_EVIDENCIA.md`. **JSONL producido desde el inicio** (lección de F2 / regla 9).
- **Niveles vs F1:** 29 mantienen, 1 baja (Faber III→IV por venue de práctica), 0 suben (no-promediado respetado — la acumulación es del nodo, no de la entrada). Régimen confirmado nivel III "(método)", alfa de retorno n/a.
- **Robustez reportada: 36 "reportado" / 127 "no reportado"** (walk-forward 0/30, bootstrap 0/30). La mayoría de edges NO tiene publicadas las pruebas más exigentes → esas pruebas caen del lado del pipeline PIC. "No reportado" es dato. 41 campos con `[memoria del modelo — verificar]` en 21 de 30 entradas (verificación web parcial; 9 entradas núcleo trend/carry/reversión cripto totalmente verificadas).
- **Hallazgos para F4/F5:** reversión de 1 día NO sobrevive en monedas líquidas (F1-017; crítico porque los perpetuos son el universo líquido); contradicción viva verificada en F1-018 (varianza posiblemente infinita → Sharpe/t-stat mal definidos); microestructura depende de order book L2/L3 no disponible hoy.
- **Resumen legible para el IP:** `docs/INVESTIGACION/BANCO/RESUMEN_ESTRATEGIAS.md` (estrategias por mecanismo + explicación de los niveles).
- Fricciones para C-002 (5, del ejecutor): granularidad entrada vs nodo en `nivel_evidencia_final`; la escala I-VII no encaja con `metodo`/`teoria`; `robustez_reportada` con tipos fijos infla filas "no reportado"; verificar 30 fuentes excede el presupuesto de una sesión; las contradicciones vivas carecen de campo de estado.
- **F3 EJECUTADA, no CERRADA:** pendiente dictamen A-04 independiente + aprobación del IP antes de abrir F4.

## 2026-07-20 (5) — C-001 F2 CERRADA (A-04 CONFORME v3 + aprobación del IP)

- Tras dos remediaciones —(1) producir el registro estructurado `F2_arbol.jsonl`; (2) eliminar la frase de ranking "el caso más fuerte del ciclo" (violación de alcance: F2 no prioriza, eso es F7)— F2 obtuvo dictamen A-04 **CONFORME** (v3, `fases/F2_DICTAMEN_A04_v2.md`). **Aprobada por el IP → F2 CERRADA.**
- Rastro append-only conservado íntegro: v1 NO CONFORME (falta JSONL) + v2 NO CONFORME (frase de ranking) + v3 CONFORME. El sistema de arbitraje independiente cazó dos desviaciones distintas en F2 antes del cierre.
- **Pendientes anotados para el F0 del C-002** (regla de inmutabilidad — no se parchea la norma a mitad de ciclo): **O-1** (la vista subdivide FAMILIA más fino que el campo `familia` del JSONL) y **C-001** (contradicción del ORQUESTADOR: la regla 9 exige JSONL a toda fase desde F1, pero la tabla de Fases y el prompt de F2 nombran solo el `.md` y la enumeración de campos omite F2).
- **F3 (evidencia + auditoría de robustez reportada, Opus) DESBLOQUEADA** para cuando el IP quiera (≤30%).

## 2026-07-20 (4) — C-001 F2: dictamen A-04 NO CONFORME (V-001) → JSONL producido, pendiente re-arbitraje

- **Dictamen A-04 sobre F2 (sesión independiente) = NO CONFORME** (`fases/F2_DICTAMEN_A04.md`). Única violación **V-001**: faltaba el registro estructurado JSONL que la **regla dura 9** exige a toda fase desde F1. Todo el fondo de F2 (árbol, herencia, casos frontera, fidelidad a F1) verificado CONFORME — el bloqueo era de FORMATO.
- Reportó **contradicción interna del ORQUESTADOR (C-001):** la regla 9 exige JSONL a "cada fase desde F1", pero la tabla de Fases y el prompt de F2 nombran solo el `.md` y la enumeración de campos de la regla 9 omite F2.
- **Expediente** (`fases/F2_EXPEDIENTE_NO_CONFORME.md`, procedimiento del IP): identificación por hash, norma literal, confirmación de que el único bloqueo es el JSONL, y **auditoría de expresabilidad** → F2 **sí** es expresable en el esquema JSONL (el árbol ya está codificado por-registro en `mecanismo/familia/variante` de F1; F2 añade enriquecimiento por-registro; la tabla de herencia es un agregado/vista). Por la regla de decisión del IP: JSONL obligatorio **y** expresable → producirlo, no exención.
- **`F2_arbol.jsonl` producido** heredando F1 **verbatim (0 campos alterados, verificado programáticamente)** + campos F2 trazables a la tabla de F2_ARBOL.md: `tipo_F2` (edge 20 / teoría 4 / método 5 / meta 1, coincide con los conteos de la tabla de herencia), `nivel_consolidado_mecanismo`, `frontera` (F1-018/020/022), `mecanismo_provisional`. Precaución del IP respetada: **cero información nueva.** `F2_ARBOL.md` redeclarada como VISTA del JSONL.
- **Contradicción C-001 del ORQUESTADOR → ADR pendiente para el F0 del C-002** (regla de inmutabilidad, regla 8: no se parchea la norma a mitad de ciclo; se aclara en C-002 que F2 produce JSONL y se añade a la enumeración de la regla 9).
- Pendiente: **re-arbitraje A-04** de F2 con el JSONL presente.

## 2026-07-20 (3) — C-001 F2 EJECUTADA (árbol genealógico, 30 entradas consolidadas)

- **F2 (árbol genealógico por mecanismos) ejecutada** (Opus, coherente con el mandato del ORQUESTADOR). Producto: `fases/F2_ARBOL.md`. Reorganiza las 30 entradas de F1 en **5 mecanismos → familias → variantes** con herencia de evidencia hacia arriba. Verificado: las 30 entradas ubicadas, ninguna perdida.
- Consolidación preliminar (F3 audita/confirma): **M1 Persistencia = el caso más fuerte, candidato a nivel I-II** (réplicas multi-siglo/multi-mercado, ≥5 grupos independientes; H-001/Donchian hereda este cuerpo por la equivalencia de Levine-Pedersen 2016); **M2 Carry II-III** (Koijen sólido + cripto-perp reciente; teoría del funding separada del edge para no inflar el nivel); **M3 Sobre-reacción II**; **M4 Microestructura III** (edge cripto reciente 2024-26); **M5 Régimen = método I-II pero alfa n/a** (es filtro, no fuente de retorno).
- 3 casos frontera declarados con doble ubicación sin forzar (regla 3): F1-018 momentum/reversión (M1↔M3), F1-020 Amihud iliquidez (M4↔M2), F1-022 VPIN toxicidad (M4↔M5).
- Fricciones para C-002 (F0 §8): (1) separar edge/teoría/método en el esquema de F1 (campo `tipo`); (2) los niveles I-II emergen recién en la consolidación de F2; (3) el nivel de "método" (régimen) ≠ nivel de "edge de retorno".
- **F2 EJECUTADA, no CERRADA:** falta dictamen A-04 independiente + aprobación del IP antes de abrir F3 (evidencia + auditoría de robustez).

## 2026-07-20 (2) — C-001 F1 CERRADA: A-04 CONFORME + contradicción F1-030 resuelta

- **Dictamen A-04 sobre F1 = CONFORME, 0 violaciones** (sesión independiente, dieta mínima; `fases/F1_DICTAMEN_A04.md`). Reportó una sola contradicción menor (C-001): F1-030 con `verificada:true` + el tag reservado `[memoria del modelo — verificar]` (autoría exacta no confirmada en su momento).
- **Resolución — corrección de consistencia de metadatos, NO cambio de contenido epistemológico:** se verificaron los autores del paper de F1-030 vía metadatos MDPI (DOI 10.3390/math13101577) → autor único **Remigijus Paulavičius**; `fuente.autores` corregido del placeholder a "Paulavičius, R.", `verificada:true` ahora legítimo (autor+año+venue confirmados), tag reservado retirado. Verificado que **ninguna otra entrada** tenía la misma contradicción (solo F1-030). JSONL revalidado: 30/30 esquema, contradicciones = 0.
- **Sin re-arbitraje** (criterio del IP): la contradicción era *reportada*, no violación; su solución no cambia el diseño ni el resultado de F1 — usar un arbitraje para esto sería desproporcionado.
- **F1 CERRADA por aprobación del IP (2026-07-20).** **F2 (árbol genealógico por mecanismos, Opus) queda desbloqueada**, a ejecutar cuando el IP quiera (≤30%). Ejecución de F1 versionada en commit `71c7bf3`; esta corrección + cierre, en el commit siguiente.

## 2026-07-20 — C-001 F1 EJECUTADA (mapeo bibliográfico, 30 entradas verificadas)

- **F1 (mapeo sistemático PRISMA) ejecutada** por sesión **Sonnet** (ejecutor puro, búsqueda web — coherente con el mandato de modelo del ORQUESTADOR). Producto: `fases/F1_catalogo.jsonl` (30 entradas, esquema de la regla 9 validado 30/30) + vista `fases/F1_CATALOGO.md`. **30/30 fuentes verificadas por web** (24 consultas). PRISMA: ~70 identificadas → ~36 cribadas → 30 incluidas.
- Cobertura de las 5 familias en alcance de F0 §2: trend/TS-momentum 7 (referencia H-001), carry/funding 6, mean-reversion 5, order-flow/liquidez 7, régimen-como-filtro 5. Exclusiones respetadas (Jegadeesh-Titman momentum XS y Makarov-Schoar arb multi-venue descartados explícitamente).
- Revisión del IP-facilitador: esquema válido 30/30, familias en alcance, muestra de ~10 fuentes canónicas verificada contra datos propios (Moskowitz-Ooi-Pedersen 2012, Koijen et al. 2018, Kyle 1985, Amihud 2002, De Bondt-Thaler 1985, Hamilton 1989, Cont-Kukanov-Stoikov 2014…) — reales y bien citadas.
- **F1 EJECUTADA, no CERRADA:** falta **dictamen A-04 (sesión independiente)** + aprobación del IP antes de abrir F2 (árbol genealógico). Reglas 4 y 10 del ORQUESTADOR.
- Fricciones registradas para C-002 (instrumentación, F0 §8): (1) el "nivel de evidencia preliminar" por fuente choca con la definición I-II de F0 §4 (exige múltiples estudios independientes) → aclarar que el nivel de F1 es por fuente y que I/II emergen en F2/F3; (2) varias fuentes cripto-nativas son 2025-26, sin revisión por pares consolidada (nivel IV), acortan el margen de réplicas; (3) caso frontera Dobrynskaya 2023 (momentum corto / reversión largo) anotado sin forzar su familia, como pide F2.

## 2026-07-19 (3) — C-001 ABIERTO: ADR-0008/0009 ratificados, F0 CONFORME en re-arbitraje

- **ADR-0008 ratificado** (reescrito como enmienda de política, no como "contradicción"): el mandato de modelo del ORQUESTADOR para F0 pasa de "Opus" a **"mejor modelo disponible a criterio del IP"** (alineado con el TRASPASO); se **ratifica** la F0 del C-001 ejecutada por Fable 5. Aplicado a ORQUESTADOR L60/L71/L119 + nota. Resuelve el hallazgo V-001 (la versión enmendada obtuvo A-04 CONFORME; el dictamen v1 se conserva).
- **ADR-0009 ratificado:** ORQUESTADOR L73 alineado con F0 — criterios puntuados = falsabilidad/claridad (no resiliencia), **resiliencia = compuerta**. Resuelve el hallazgo C-001.
- **Re-arbitraje A-04 (sesión independiente, dieta mínima) = CONFORME** (`F0_DICTAMEN_A04_v2.md`): cero violaciones, cero contradicciones; consistencia criterios y modelo verificada a la letra. F0 sin cambios (SHA-256 `b99c356…`); ORQUESTADOR nuevo hash `7594d6b…`.
- **Acta de apertura sellada** (`ACTA_APERTURA_C001_borrador.md`): checklist de 6 puntos completa salvo el tag; acta de una línea: *"Ciclo C-001 abierto el 2026-07-19 bajo F0 v1"*. **Abrir ≠ correr F1 ya** (F1 cuando el IP quiera, ≤30%, moratoria ADR-0004 vigente).
- **Pendiente (acto del IP):** `git tag banco-C001-abierto` + commit. Hasta entonces, la apertura consta sellada documentalmente pero no versionada.
- Nota meta: el sistema de arbitraje independiente hizo su trabajo de punta a punta — cazó dos desviaciones (V-001, C-001), se resolvieron por el canal correcto (ADR ratificados), y confirmó la resolución en una sesión nueva. Justo el ciclo que la meta-pregunta de F0 §1.4 quería observar.

## 2026-07-19 (2) — Apertura de C-001 BLOQUEADA: dictamen A-04 sobre F0 = NO CONFORME

- Dictamen A-04 producido en **sesión independiente** (subagente aislado, dieta mínima: prompt A-04 + ORQUESTADOR + F0, sin contexto de diseño). Archivado en `docs/INVESTIGACION/BANCO/fases/F0_DICTAMEN_A04.md`. **Resultado: NO CONFORME** → F0 no cierra, C-001 no abre (falla el punto "Dictamen A-04 = CONFORME" del checklist de apertura).
- **V-001 (violación):** ORQUESTADOR manda F0 = "Opus + humano"; F0 (L3) declara ejecución por "IP + Fable 5". Ejecutor distinto del mandatado. A-04 no juzga la calidad, juzga que la norma otorgaba la fase a otro modelo.
- **C-001 (contradicción, A-04 la reporta sin resolverla):** ORQUESTADOR enumera "resiliencia" como criterio puntuado de la rúbrica; F0 §3(c) la reclasifica a compuerta (no puntúa) y añade "Falsabilidad/claridad" (10%), criterio no enumerado por la norma. Tensión directa norma↔artefacto.
- **Condición de levantamiento:** resolución del IP de V-001 y C-001 (vía ADR, canal exigido para desviaciones de método) + **re-arbitraje A-04 en sesión nueva**. Ningún acto de apertura (tag, acta) es válido antes del CONFORME; no se sella nada.
- **Expediente abierto** (`fases/F0_EXPEDIENTE_NO_CONFORME.md`): identificación inequívoca de F0 auditado (SHA-256 `b99c356…` / blob `e597a46` / commit `0337152`, working tree == HEAD), hashes de las normas usadas, constancia de la dieta del auditor (3 lecturas, arranque en frío, auto-declaración de ítems fuera de dieta), y hallazgos clasificados (V-001 violación · C-001 contradicción · OBS-1/2 observaciones). Análisis de causa raíz: hallazgos independientes → apuntan a dos ADR (decisión del IP).
- **Dos ADR borrador (propuestas, pendientes de ratificación — NO son norma vigente):** `ADR-0008` (propone resolver V-001: propondría alinear el mandato de modelo del ORQUESTADOR con la política "mejor disponible" del TRASPASO y reconocer la F0 por Fable 5) y `ADR-0009` (propone resolver C-001: propondría reconciliar la lista de criterios del ORQUESTADOR hacia la rúbrica de F0 — resiliencia como compuerta, no criterio puntuado). Separados, de propósito único, aceptables por separado; ninguno toca ORQUESTADOR/F0 hasta que el IP ratifique y un re-arbitraje A-04 independiente lo valide.
- Nota meta (primer dato del C-001 sobre su propia maquinaria): el arbitraje independiente con dieta mínima cazó dos desviaciones que la sesión interesada habría racionalizado. El diseño funcionó — igual que con H-001/ADR-0006.

## 2026-07-19 — H-002.v1 RECHAZADA (disparo T1 firme) + apertura de H-002.v2

- **Hallazgo (verificación del IP):** el banco de H-002 (07-14) aprobó apoyándose en la **anulación interpretativa de un veredicto letal pre-escrito**. T1 —marcado "el decisivo" con regla MATA en el PREREG— disparó (estrategia BNB 0.89/0.74 vs hold 0.97/0.78, no batió Sharpe ni MAR); el propio `RESULTADO_BANCO.md` reconoce "MATA" y acto seguido lo anula en el mismo documento ("test defectuoso"), sin ADR, sin A-04, sin ratificación, y avanzó a paper (deploy 07-15). Es el canal que proscribe el **principio 17**.
- **Reconocido firme por el IP.** La transitoria del principio 17 se agotó con su único caso admitido (exp-004, 07-06); T1 (07-14) no está cubierto y "ninguna anulación retroactiva es admisible bajo ninguna circunstancia"; un ADR de rescate sería inadmisible de plano por (9)(a). **Agravante (req. 1):** el defecto de T1 estaba **pre-declarado** en el PREREG ("El riesgo #1 es que el retorno sea BETA de BNB") — riesgo previsto y elegido, luego usado como excusa, no mala especificación descubierta de forma independiente. Verificado además que **ninguna pieza de la evidencia de H-002 tiene dictamen A-01**.
- **Actos (append-only, `RESULTADO_BANCO.md` intacto por principio 17):** alta tardía de H-002 en `REGISTRO_HIPOTESIS.md` (nunca se había registrado) con v1 RECHAZADA y v2 EN VALIDACIÓN; ficha v1 → RECHAZADA con recuadro del disparo; ficha v2 creada; nota de estatus honesto en `paper_real`; ESTADO actualizado.
- **H-002.v2 ordenada y SELLADA (2026-07-19):** `research/H-002-ruptura-bnb-d1/v2/PREREG_BANCO.md`. Señal idéntica a v1 (sin re-optimizar, req. 5). Tras revisión punto por punto del IP: test decisivo = **cesta multi-activo, screen in-sample (pre-2023) ∧ forward OOS** (la conjunción se refundó al detectar que "período completo ∧ forward" reusaba el lockbox 2023-26 quemado — corregido); **"risk-matched" eliminado** (invariancia de escala del Sharpe: no separaba edge de beta); **funding real** en la corrida decisiva perp (P3); **A-01 obligatorio**; horizonte forward **mecánico** (≥30 trades ∧ ≥6 meses, lo que ocurra más tarde, evaluación sin discreción); **cláusula de "evidencia insuficiente"** para la baja frecuencia (ni confirmada ni refutada mientras falten datos); §8 de justificación de umbrales escrita antes de todo resultado; eliminado el último parámetro interpretativo ("banderas graves"). Verificado: cero parámetros abiertos. **No corrido**; falta el push (`tanda.ps1`, acto del IP), luego A-02 → `banco.py` → disparo mecánico del forward → A-01 → veredicto.
- Nota de guardia: el sistema volvió a exhibir el patrón que A-04 ya cazó en H-001 —anular un umbral pre-escrito por nota tras ver el resultado— esta vez en H-002 y detectado por el IP, no por el arbitraje. El fondo de la crítica puede tener razón; la vía (después del resultado) no es admisible. La corrección legítima es re-especificar antes de correr.

## 2026-07-18 (4) — ADR-0007 RATIFICADO. El caso fundacional queda cerrado

- Ratificación fechada del IP tras dictamen A-04 v2 CONFORME. Ejecutado el §4.7 paso 4: principio 17 incorporado íntegro a CONSTITUCION (con su transitoria autoderogable); PROTOCOLO §6 nuevo (eje de estatus epistemológico, ortogonal al pipeline) y excepción del requisito (7) anotada en §5; ficha H-001 como fuente única del estatus (literal de §4.5(6)) con REGISTRO y ESTADO en puntero; erratum adjunto a exp-008/PREREG; nota aclaratoria C-001 en la plantilla ADR; ADR-0007 → ACEPTADA.
- Efectos vigentes desde la ratificación: notas interpretativas nulas de origen; retroactividad inadmisible para siempre; Fase A convalidada como etapa del pipeline de H-001; re-corte de Fase B convalidado; condición (i) (exp-008-R0) vigente; cláusula de segundo disparo armada sobre P-1 (Fase B, cierre ≤ 2026-09-30); Fase C dependiente del veredicto de Fase B y del sello de su PREREG.
- V-001 y V-002 de los dictámenes del ADR-0006: cerradas por este acto (enmienda efectiva + ratificación fechada).

## 2026-07-18 (3) — ADR-0007: dictamen A-04 v2 CONFORME. Correcciones de registro

- **CONFORME al tercer arbitraje:** la cura de V-201/C-007 verificada a la letra (exención expresa de (9)(a)/(9)(b) en la transitoria, régimen del (9) desplazado solo para el caso fundacional, íntegro para todo caso posterior; `git show d2b975f`: exactamente dos líneas). Pendiente: ratificación del IP (§4.7 paso 3-4).
- **Corrección de un mensaje de commit previo:** la tanda "…anexo A sincronizado, backup eliminado…" sobre-declaró — el Anexo A NO se tocó (no era necesario); el backup sí se eliminó (git es el historial, v1 en commit `5dbee73`). El texto del mensaje fue redactado por el asistente ANTES de verificar el diff — cuarta sobre-declaración del mismo origen registrada en el expediente; regla adoptada: los mensajes de commit se redactan tras verificar, nunca antes. Cabecera del ADR-0007 corregida (referencia al commit en lugar del fichero inexistente).

## 2026-07-18 (2) — Segundo dictamen A-04: NO CONFORME. CORRECCIÓN de este changelog

- **Corrección (V-102):** la entrada anterior decía "remediación completa" y "6 violaciones remediadas" — FALSO: la v2 respondió 4 de 10 puntos (V-004 y V-005 levantadas; V-003 y V-006 sin respuesta; C-002/003/004 no elevadas). Tercera sobre-declaración del redactor en 48 h, siempre autofavorable — el patrón queda registrado. Contradicciones nuevas: C-005 (el texto constitucional propuesto exige ratificación previa a efectos → haría inadmisible al propio ADR-0006) y C-006 (doble estatus en la ficha — corregido: fila Estado convertida en puntero único).
- Por el compromiso pre-declarado: **sin tercera remediación exprés. La decisión sube al IP** — acatar el MATA de exp-004, o re-fundamentar desde cero (ADR-0007) con inventario completo, experimentos pendientes enumerados, contradicciones elevadas una a una y cláusula transitoria que resuelva C-005.
- **DECISIÓN FINAL DEL IP (mismo día): ADR-0006 RECHAZADO → ADR-0007 como acto fundacional** — estructura de 4 partes (reconocimiento expreso sin matices; nulidad de las notas interpretativas; nueva doctrina para el caso doble criterio-mal-especificado + procedimiento-vulnerado; cláusula única: la retroactividad muere en el acto que la usa por única vez). Encargo emitido (`ADR-0007_ENCARGO.md`) a sesión redactora NUEVA con los requisitos de ambos dictámenes; el redactor del 0006 no redacta. Secuencia: borrador → arbitraje A-04 → ratificación → solo entonces, efectos.
- ~~Decisión del IP: EN DELIBERACIÓN~~ (superada el mismo día) (pausa deliberada; plazo natural antes del cierre de Fase B ~08-16). Mientras tanto: cero efectos de lo sujeto-a-ratificación; Fase B y paper_real continúan; H-002 y C-001 no dependen de esta decisión y pueden avanzar.

## 2026-07-18 — Dictamen A-04 sobre ADR-0006: NO CONFORME → remediación completa (v2)

- Las 6 violaciones verificadas como ciertas (3 del propio redactor de la sesión): ficha H-001 sin actualizar (remediada, eventos 07-06→07-18 añadidos), segunda nota-override en exp-005 sin cubrir (ADR v2 la incorpora con idéntico tratamiento), condición (i) consumida bajo ADR no ratificado (re-etiquetada "sujeta a ratificación" en REGISTRO/ESTADO/ficha), y falta de enmienda constitucional (v2 propone la excepción al principio 4, a incorporar SOLO al ratificar). **Pendiente: re-arbitraje A-04 de la v2 + decisión del IP.** El sistema de arbitraje cazó al mentor dos veces en 24h — funcionando como diseño.

## 2026-07-18 — Corrección de atribución causal en TEORIA v0.2 (revisión cruzada)

- La entrada v0.2 atribuía el ahorro de funding a "cobrar carry en alts": **FALSO** — verificado contra la tabla condicional del propio exp-008: la cesta pagó en los 5 símbolos y ambos lados (−$453 total vs −$776 del modelo); el ahorro es sobrecarga del modelo uniforme. Mecanismo nuevo registrado: selección adversa de las posiciones de tendencia contra el promedio incondicional de funding. **Implicación para ADR-0005 (funding-carry):** su diseño debe usar análisis condicional, jamás promedios incondicionales. Lección de guardia: dos cazadas del auditor en un resultado favorable — la guardia baja sola cuando el resultado gusta.

## 2026-07-17 (tarde) — exp-008: R0 ACEPTABLE — la incógnita nº 1 se cierra A FAVOR

- Dictamen A-02: APTO (SOL 4h/2h = episodio FTX legítimo; extremos = eventos reales; hashes SHA-256 congelados en el dictamen — crítica de proceso aceptada: el recolector debe emitir hash de fábrica). Script blindado: verifica integridad 5/5 contra los hashes antes de correr.
- **exp-008 ejecutado: R0 — el funding real 2021-26 MEJORA todas las ventanas** vs el modelo pesimista (FULL: NET 27.26% vs 24.03%, Sharpe 0.47 vs 0.42, Calmar 1.66 vs 1.35; 2426: +4.63% vs +2.79%). Paridad OK. Condición (i) del ADR-0006 CUMPLIDA: Fase C vuelve a depender solo de Fase B + cero disparos letales. TEORIA v0.2: creencia nueva ✓ sobre funding; versión fuerte de P4 refutada como efecto agregado. Registros actualizados.

## 2026-07-17 — ADR-0006 (override de exp-004 formalizado) + arranque Propuesta 1

- **ADR-0006:** el veredicto letal de exp-004 (lookback) fue anulado el 07-06 por nota interpretativa — canal que la Constitución no reconoce. Se formaliza retroactivamente: H-001 degradada a **CUESTIONADA** en todos los registros; Fase C condicionada a exp-008-R0 + cero disparos letales nuevos; **un segundo disparo letal = retiro operativo automático, sin nota interpretativa**; precedente restrictivo (las notas jamás anulan umbrales). Pendiente: arbitraje A-04 en sesión separada + ratificación del IP.
- **exp-008 pre-registrado** (funding real histórico, intento único, umbrales R0/R1/R2 ratificados por el IP con letal endurecido) + `datalake/funding/recolector_funding.py` (público, sin keys, idempotente, QA integrado). Secuencia: recolectar → dictamen A-02 → correr exp-008.

## 2026-07-16 (tarde) — H-002 formalizada (hipótesis económica + ficha de pipeline)

- Se aclara que el **banco de H-002 ya estaba registrado** (PREREG_BANCO + RESULTADO_BANCO, T1-T5, veredicto: overlay de tendencia reductor de DD, confianza moderada, no probado). Lo que faltaba y se completa hoy: (1) `research/H-002-ruptura-bnb-d1/HIPOTESIS_ECONOMICA.md` — el "por qué económico", con honestidad sobre que es **long-only / beta positiva** (no market-neutral), 5 predicciones falsables (incl. P3: exposición máxima a funding por ser siempre larga) y 4 señales de retiro; (2) ficha de pipeline `docs/INVESTIGACION/hipotesis/H-002-ruptura-bnb-d1.md`; (3) registro en la tabla de hipótesis de ESTADO. Nota meta capturada: el banco reusó el motor del investigador *verbatim* en ~1 jornada = primera evidencia (n=1) de que la plataforma abarató la 2ª hipótesis (prueba de fuego del roadmap §4). Sin fase operativa formal aún (decisión tras cerrar C-001, por moratoria).

## 2026-07-16 (tarde) — Criterios de Fase C en borrador (decisiones del IP)

- Redactado `research/H-001-canal-donchian/fase_C/PREREG_FASE_C_BORRADOR.md`, anclado en RISK_POLICY §Pendiente, el PREREG y `HIPOTESIS_ECONOMICA.md §5`. Decisiones del IP: capital **$750**; criterio de retiro = **umbral de suspensión y revisión a −27%** (1.5× maxDD; cesa operativa + análisis completo antes de reanudar, cláusula del IP) separado de la divergencia de comportamiento y de las 4 señales de retiro conceptual; kill **blando + disyuntor técnico** (se descarta kill duro por precio); stop por **vela cerrada** (el stop en exchange → C-002). **Falta sellar** antes del día 1 de C, solo si Fase B aprueba. RISK_POLICY §Pendiente actualizado.

## 2026-07-16 — FASE B RE-CORTADA (incidente de contaminación resuelto)

- **Incidente:** el corte de Fase B del 07-14 quedó comprometido. Causa raíz **verificada**: el ensayo (`ensayo_faseB/bot/`) tenía las **mismas API keys demo** que el bot oficial (`donchian512_lab/bot/`) → una sola cuenta, dos bots colisionando (el ensayo adoptaba las posiciones del oficial). El diario del 07-14 decía "ensayo detenido y cuenta aplanada"; fue intención no cumplida.
- **Remediación:** máquina esterilizada (0 procesos); keys del ensayo **vaciadas** + banner RETIRADO; **lanzador blindado** (`lanzar_bot.bat` + `contar_faseB.ps1`) con guardián anti-doble-instancia (cuenta cualquier `live_bot.py` del lab, venv o sistema) + reinicio solo ante caída + rutas completas; tarea `faseB_donchian` (ONLOGON, `MultipleInstances=IgnoreNew`); `aplanar_cuenta.py` para dejar la cuenta en 0 posiciones.
- **Evidencia:** datos del bot oficial 07-14→16 **ANULADOS** (cuenta contaminada); estado respaldado como `bot_state.pre_recorte_2026-07-16.json`. Fase A (6/6, 07-14) **intacta**. Reloj de Fase B reinicia 1 mes desde el nuevo corte. Acta: `research/H-001-canal-donchian/fase_B/ACTA_RECORTE_2026-07-16.md`.

## 2026-07-14 (tarde) — FASE B INICIADA (corte 15:13:16 UTC)

- Día D completo en la misma jornada del cierre de A: ensayo detenido y cuenta demo aplanada; ENMIENDA 1 sellada en el PREREG (demo trading, 4 fixes de frontera, riesgo BTC 0.125% por exp-003, métrica de omisión simulada, EQUITY_CAP=750); bot de frontera aplicado al lab (con respaldo del de Fase A); arranque verificado (demo=True, DRY_RUN=False, eq=750, reconciliación limpió la posición paper); acta de inicio sellada; DIARIO_FASE_B creado. paper_real continúa como testigo. Pendientes del día: tag `H001-faseB-frontera` (usuario), adaptar auditoría programada, auditar primer trade cuando ocurra.

## 2026-07-14 — CIERRE DE FASE A: APRUEBA 6/6

- Replay de la fase completa: **36 señales del modelo = 36 eventos del bot, 0 divergencias**, latencia mediana 8.7 s (p95 14.9), 104 atrasadas con causa cerrada. Informe sellado (`informe_cierre_faseA.md`), decisión registrada en CRITERIOS_FASES, diario completado (07-11→14, con outage del 07-11 recuperado solo y blip del 07-14 verificado sano por vigía 12:27/12:42). Primera revisión de TEORIA: sin cambios de creencias de mercado. Siguiente: día D de Fase B.

## 2026-07-10

- `docs/RESUMEN_EJECUTIVO.md`: síntesis de las dos etapas (lab original + proyecto-alpha), estado operativo de las 3 instancias, decisiones cerradas por experimento, hallazgos que evitaron daño, y próximos hitos.
- **ADR-0004 — Moratoria de diseño hasta cerrar C-001:** toda idea/mejora → ADR pendiente para C-002; únicas excepciones, las ya definidas (defecto fatal, violación metodológica). Criterio de éxito del ciclo incorporado al acta: decisiones metodológicas respaldadas por evidencia, aun contra las expectativas. Último acto de diseño de la fase de arquitectura.
- **Cierre de la fase de arquitectura:** ADR-0003 "Nunca optimizar antes de medir" (mejoras exigen evidencia operativa del ciclo; se aplican en el siguiente); F0 §8 instrumentación del propio ciclo (latencias, bloqueos, fricciones) inaugurando la métrica de latencia del conocimiento; acta de apertura del C-001 en borrador (texto del IP), pendiente de sellado tras dictamen A-04.
- **Operacionalización del flujo del Banco:** A-04 con modo VALIDADOR ESTRICTO (dieta de insumos mínima, verificación literal, plantilla fija de dictamen, calidad fuera del alcance — la juzga el IP); regla 9 artefactos estructurados (JSONL fuente de verdad + Markdown como vista, un objeto por edge enriquecido fase a fase); regla 10 compuertas objetivas (dictamen + artefacto + aprobación IP, nunca juicio informal); F1 como ejecutor puro.
- **Auditoría anual de Creencias** (regla 9 de TEORIA.md, mismo día que la de Simplicidad): ¿qué damos por cierto que hace un año era hipótesis? Todo ascenso de estatus debe citar su veredicto del pipeline; ascenso sin veredicto trazable se revierte de oficio. Contra el riesgo humano de "esta vez ya sabemos la respuesta".
- **Regla de Inmutabilidad del Ciclo + apertura administrativa:** F0 inmutable durante el ciclo tras CONFORME de A-04 (problemas → ADR pendiente → F0 del ciclo siguiente; defecto fatal → aborto con acta); ciclos identificados (C-001…) con checklist de apertura de 6 puntos y tag de git; hipótesis trazables a su ciclo de origen.
- **F0 del Banco de Mecanismos cerrada (pendiente dictamen A-04):** ciclo 1 piloto por mecanismos (persistencia/carry/reversión/microestructura/régimen-como-filtro), rúbrica 35/30/20/10/5 con anclas y sensibilidad obligatoria, resiliencia como compuerta (no puntaje), salida 0-5 protocolos sin mínimo, niveles de evidencia I-VII.
- **Principio 16 — Costo de Gobernanza** (absorbe tres propuestas en una pieza, aplicándose a sí mismo): toda regla nueva justifica qué error evita, qué cuesta y qué elimina; los componentes del laboratorio son hipótesis de diseño; Auditoría de Simplicidad anual (primera 2027-07). TEORIA.md: entradas como "estado actual de la evidencia" con confianza en bandas (no porcentajes de precisión falsa). Banco renombrado a **Banco de Mecanismos** (estrategias = implementaciones). Dormidos con disparador: Cementerio Científico (~50 hipótesis), Curador del Conocimiento (~2027-01, en backlog de agentes).
- **`docs/TEORIA.md` fundada (v0.1):** Teoría del Laboratorio — documento vivo de creencias sobre mecanismos con estados epistémicos (✓/△/✗/⊘), cada una con su linaje de evidencia; las rechazadas alimentan con el mismo peso; no normativo (nada se opera desde ahí). Sembrada con lo ya aprendido de H-001: rotación de contribuyentes ✓, convexidad no consistencia ✓, crisis-alpha-por-shorts falsada ✗, persistencia mayor en alts △, funding ⊘.
- **Principios 14 y 15 en la Constitución:** separación explícita generación-de-conocimiento / producción-de-evidencia (Banco genera, Pipeline evidencia, Registro conserva, A-04 vigila, humano decide — nadie invade a nadie) y ADR de primera clase con las 5 preguntas, incluida la obligatoria condición de revisión futura. Plantilla ADR v2.
- **Banco v3 + A-04** (segunda ronda de correcciones del investigador): niveles de evidencia I-VII en F0 (sin promediar entre niveles), F2 elevada a árbol genealógico enraizado en MECANISMOS con herencia de evidencia, falsabilidad económica popperiana obligatoria en F4, versionado científico H-XXX.vN formalizado en PROTOCOLO, y **A-04 Árbitro de Metodología** creado (agents/): audita cumplimiento del proceso en todo el laboratorio, dictamen VIOLACIÓN bloqueante, sin opinión sobre trading.
- **Banco v2** (mismo día, correcciones del investigador aceptadas): F2 deduplicación por edge subyacente (nueva), auditoría de robustez fusionada en evidencia (audita, no calcula), transferibilidad como cadena mecanismo→ingredientes→veredicto, F6 diseño experimental en dos sesiones (diseñador/adversarial separados), mapa de complementariedad sin pesos, y principio rector reformulado: "el banco entrega el diseño experimental del pipeline" — protocolos pre-registrables, umbrales ratificados por el humano.
- **Banco de Estrategias** (`docs/INVESTIGACION/BANCO/`): orquestador F0–F6 creado desde el borrador del investigador, con cirugía documentada — F4 redefinida a "traducibilidad" (un LLM no mide robustez), F7-portafolio eliminada (requiere estrategias validadas; es el componente Asignación de Capital), F8 absorbida en las fichas. Reglas duras: fuentes verificadas, prohibido inventar métricas, producto final = fichas candidatas para el REGISTRO.

- Resumen de las 3 instancias (día 8 de Fase A): fixes de frontera validados en el ensayo (fees 10/10, 0 fills sin precio); feed mainnet cuantificado (~0.9 atrasadas/día/símbolo vs 1.5 testnet / 2.2 demo); bot_state del lab verificado OK en máquina.
- paper_real documentado con sección de gobernanza (no-evidencia de A/B; insumo de la decisión de C; keys vacías confirmadas — el hallazgo de seguridad del resumen era falso positivo). Detectada discrepancia PREREG (0.1% uniforme) vs código (RISK_MAP BTC 0.125%): erratum del investigador pendiente.
- `.gitignore`: `paper_real/bot/` fuera de git; `paper_real/paper/` (serie de comparación de feed) sí se versiona.

## 2026-07-04

- **Vigía operativo:** tarea `vigia_donchian` (schtasks cada 15 min, ruta completa al `pythonw` del venv para evitar fallo silencioso por PATH); `vigia.log` escribiendo `OK`. H2 cerrado — el hallazgo del checklist estaba desactualizado (el vigía ya corría).
- **Ensayo de Fase B arrancado:** montaje completado, keys demo corregidas (−2014 formato → −1022 firma → OK), conecta a demo con `eq=750`, una sola instancia. F0 confirmado en vivo (enable_demo_trading + assert de endpoint demo → se niega a operar si no es demo).
- **Arranque automático del ensayo:** `bot/lanzar_ensayo.bat` (auto-reinicio, sleep headless-safe con `ping`) + tarea `ensayo_faseB_lanzador` (al iniciar sesión). La ruta con espacios sin comillas daba `0x80070002` (archivo no encontrado); re-registrada con `Register-ScheduledTask` (ejecutable + directorio separados, runtime ilimitado, batería) y probada OK.
- **Rescate de git:** índice corrupto en la copia de trabajo (`bad signature`); reconstruido trasplantando el `.git` de un clon limpio, 0 pérdida de datos (working tree == HEAD, solo CRLF). `core.autocrlf=true` para cortar el conflicto CRLF Windows/Linux; pendiente `.gitattributes` commiteado (`* text=auto eol=lf`).

## 2026-07-03

- `docs/TRASPASO.md`: plan de trabajo para próximas sesiones con cualquier modelo — guardarraíles, tareas fechadas (cierre Fase A 07-12, día D, rutinas), y tabla de qué tarea exige qué modelo.
- `ensayo_faseB/`: ensayo general aislado del bot de frontera (órdenes demo, EQUITY_CAP=750, reglas no-evidencia).
- `bot/live_bot_faseB.py` (staged, NO ejecutar en Fase A): versión de frontera con los 4 cambios aprobados — demo trading, fill vía fetch_order con fallback declarado, fees desde fills, riesgo por símbolo con cap por suma real. Se aplica el día D con el checklist del paquete.
- **exp-002 y exp-003 (riesgo por símbolo):** 0.15% RECHAZADO por umbral pre-escrito; 0.125% pre-registrado como intento final (N=2) y ACEPTADO con el mismo umbral. M1 cerrado: $750 + BTC 0.125%. Paridad del motor con la frontera original verificada (24.03/-17.8/0.42).
- **Fontanería ejecutada + `PAQUETE_FASE_B.md`:** BTC min demo $50 vs mainnet $100 (brecha demo/producción → métrica nueva de B); bugs pre-B descubiertos: fill price None en create_order (B-fix1) y fees solo en fills (B-fix2). Decisión M1: $750 + riesgo BTC 0.15% condicionada a exp-002. Acta borrador y checklist de arranque de B listos.
- **Hallazgo F0** (primer intento de fontanería): ccxt ≥4.5 retiró el testnet de futuros de Binance → script migrado a `enable_demo_trading` (keys de demo.binance.com); el bot necesitará la misma migración al arrancar Fase B. Registrado como bloqueante pre-B en ESTADO.
- `fontaneria_ordenes.py` (prep. Fase B, cuenta testnet separada): límites reales por símbolo (verifica M1), round-trip con inspección de fees, firma exacta del rechazo por min_notional en BTC, funding history, limpieza verificada. Decisión M1 (capital/BTC) diferida a sus resultados, registrada.
- `replay_offline.py` (cierre de Fase A): recomputa señales con fórmulas congeladas, estado dirigido por eventos reales, criterios C1/C2/C4/C5 del PREREG, clasificación de velas saltadas (M2), selftest sin red en verde.
- Revisión adversarial de código (bot vs. especificación vs. backtester): señal idéntica confirmada, 0 divergencias bloqueantes. Hallazgos M1 (omisión BTC por min_notional casi cierta con $750 — decisión pre-B desbloqueada), M2 (vela saltada invisible — requisito del replay), M3 (maxDD por activo del veredicto inicial subestimado; cifras válidas = cesta corregida). Informe en `research/H-001-canal-donchian/report/`.
- `docs/CONTRATOS.md` (tarea 0.4): vela (identidad = apertura UTC), funding (signo = contribución cobrada), señal (intención, no orden), experimento (config+datos+hash), eventos/trades (esquemas vivos adoptados tal cual). **Etapa 0 cerrada.**
- Checklist línea base de Fase A: instrumentación OK; hallazgo real (vigía sin registrar); falsa alarma de heartbeat resuelta (caché del lector remoto, lección registrada).
- `RISK_POLICY.md`: límites transcritos del sistema vivo (0.10%/trade, cap 0.60%, máx 5, kill diario -5% blando) + matiz documentado del kill switch + pendientes de Fase C.
- `DATA.md`: fuentes verificadas en código (cache 15m origen Binance; bot en testnet), sesgos con tratamiento, funding real como incógnita nº 1, requisitos del Data Lake.
- Verificado: el test de sensibilidad 384/512/640 NO se ejecutó — decisión pendiente antes de Fase C.

## 2026-07-02 (hipótesis económica H-001)

- A-03: `research/H-001-canal-donchian/HIPOTESIS_ECONOMICA.md` — mecanismo (subreacción + cascadas de liquidación + límites al arbitraje conductuales), contraparte identificada, 5 predicciones falsables (P1 ya consistente), 4 señales de retiro conceptual. Formulada ex-post y así declarada.

## 2026-07-02 (inventario del lab original)

- **Inventario de `donchian512_lab`** (`docs/MIGRACION.md`): pre-registros y 17 informes migrados a `research/H-001-canal-donchian/`. Regla maestra: el sistema vivo no se toca hasta cerrar Fase A.
- **Enmienda de gobernanza** en `CRITERIOS_FASES.md`: la Fase A en curso se rige por su PREREG original (acta 2026-07-02 03:53 UTC); la tabla del repo queda como plantilla futura.
- **Ficha H-001 reescrita**: pre-registro reconocido como original (no retroactivo), 5 preguntas respondidas con evidencia, métricas consolidadas (Sharpe ~0.42, alfa t=0.94 NS, top-5 trades = 115% del neto), corrección visible en el registro de hipótesis.
- `.gitignore`: añadido `config.env` (el lab contiene API keys que jamás deben entrar al repo).

- **Criterios de la Fase A fijados antes de evaluar** (tarea 0.1 del plan): 28 días + ≥15 señales, uptime ≥99%, coincidencia bot/backtester 100%, latencia ≤60 s, velas perdidas ≤0.1%, reconexión automática ≤2 min. Regla: todos aprueban o la fase reprueba. Ficha H-001 actualizada: 512 velas de 15m (~5.3 días), 5 pares.

- Sistema de agentes (ADR-0002): A-01 Validador Estadístico, A-02 Auditor de Datos, A-03 Investigador Cuantitativo (restringido a H-001 hasta cerrar Etapa 0). Backlog de 13 agentes con condiciones de activación en `docs/AGENTES.md`. Principio 13 añadido a la Constitución: la IA no toma decisiones de trading.
- `docs/PLAN_TRABAJO.md`: análisis de arranque, etapas 0–4 (teoría → migración → programación), contratos a diseñar, disciplina de git.
- Convención de carpetas por hipótesis: `research/_template/` copiable, `research/H-001-canal-donchian/` creada, `strategies/` (biblioteca de validadas congeladas).

## 2026-07-01

- Creación del repositorio con estructura documental completa.
- ADR-0001: adopción del proceso centrado en hipótesis.
- H-001 (Canal de Donchian) registrada como hipótesis en validación, Fase A.
- Pendiente: migración del código existente (backtester, bot, dashboard) y completar campos PENDIENTE de criterios y riesgo.
