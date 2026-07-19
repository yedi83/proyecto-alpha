# DICTAMEN A-04 — ADR-0007 (Acto fundacional)

```
DICTAMEN A-04
Artefacto evaluado: docs/ADR/ADR-0007-acto-fundacional-doctrina-de-excepcion.md
                    (Estado: "Propuesta", 2026-07-18; reemplaza al ADR-0006 rechazado)
Estado: ☐ CONFORME   ☒ NO CONFORME
────────────
```

## Dieta de insumos (declaración obligatoria)

Modo VALIDADOR ESTRICTO. El artefacto es un ADR, no un documento de fase del Banco; se aplica la dieta del modo general (prompt A-04 + documentos normativos que apliquen) con **las prohibiciones y la plantilla del modo estricto**. Insumos recibidos y usados, exactamente los ordenados por el encargo del arbitraje: `ADR-0007_ENCARGO.md`; `ADR-0006_DICTAMEN_A04.md` y `_v2.md`; `CONSTITUCION.md`; `PROTOCOLO.md`; `ADR-0000-plantilla.md`; `exp-004/` completo (PREREG, RESULTADO, NOTA, metricas.json); `exp-005/` completo (PREREG, RESULTADO, NOTA, metricas.json); ficha `H-001-canal-donchian.md`; `REGISTRO_HIPOTESIS.md`; `ESTADO.md`; `PREREG_FASE_AB.md` con su **ENMIENDA 1**.

**Se declara y no se ignora:** `ADR-0007_REVISION_PREVIA.md` **no** es insumo normativo (lectura previa no vinculante de un tercero); no se leyó ni pesa en este dictamen. Se consultó además `CRITERIOS_FASES.md` **solo** porque la propia ficha de H-001 remite a él como sede de la enmienda de gobernanza y del registro de decisión de Fase A (07-14); su uso se limita a corroborar el acto 13 del inventario. No se consultaron `exp-006/`, `exp-007/`, `exp-008/`, las actas de fase ni `informe_cierre_faseA.md`: **quedan fuera de la dieta y sus contenidos no se dan por verificados** (ver O-001).

**Alcance.** Se verifica cumplimiento del método, con cita textual de la norma. No se juzga la calidad de la doctrina propuesta, ni si el criterio de exp-004 estaba bien o mal especificado, ni si H-001 tiene edge, ni si la enmienda constitucional es buena norma: eso es del IP, compuerta separada. Carga de la prueba del artefacto: lo no verificable con la dieta cuenta contra la conformidad. Atendida la instrucción de §4.8 del propio ADR: el documento no declara su conformidad — la dicta este dictamen.

## Requisitos verificados

**Mandato del IP — estructura de 4 partes (encargo §Mandato)**

- ✔ **M-I.** Parte I — Reconocimiento expreso. Presente en §4·Parte I con el literal exigido: «El laboratorio incumplió su propio protocolo entre el 6 y el 17 de julio de 2026. Sin matices, sin atenuantes y sin contexto que lo suavice.» Enumera los cinco hechos con nombre.
- ✔ **M-II.** Parte II — Declaración de nulidad. Presente en §4·Parte II: las notas de exp-004 y exp-005 «nunca tuvieron efectos normativos»; valor técnico conservado «jamás como decisión». Alcance cerrado a las dos notas del 2026-07-06.
- ✔ **M-III.** Parte III — Nueva doctrina. Presente como **principio 17** con los cuatro requisitos que el encargo nombra (demostración de mala especificación (1); canal ADR (2); arbitraje A-04 (3); ratificación del IP antes de cualquier efecto (4)), más (5)–(9) y disposición transitoria.
- ✔ **M-IV.** Parte IV — Cláusula única e irrepetible. Presente en §4·Parte IV + disposición transitoria de la Parte III: «Después de este caso, la retroactividad no puede volver a existir. Nunca.»

**Requisitos técnicos del encargo (6)**

- ✔ **R1 — Inventario de actos 07-06→07-17.** Presente en §4.1: 22 actos fechados, con pronunciamiento de validez uno a uno. El subconjunto exigido por V-003 del primer dictamen está íntegro y verificado contra la dieta: exp-005 (acto 5, RESULTADO 07-07 03:37), Fase A APROBADA 6/6 (acto 13, corroborado en `CRITERIOS_FASES.md` y ficha), Fase B iniciada 07-14 15:13:16 (acto 14, `PREREG_FASE_AB`/ACTA), re-corte de Fase B 07-16 15:27:33 (acto 16, `ESTADO.md`/ficha), exp-008 (actos 19 y 21). Límite de verificación declarado en O-001.
- ✔ **R2 — Enumeración cerrada de «experimentos pendientes».** Presente en §4.5.1: lista explícita (P-1 Fase B; P-2 excluido por no ser experimento), horizonte temporal (cierre P-1 ≤ 2026-08-16; condición (ii) satisfecha a más tardar 2026-09-30), reglas de cómputo, prospectividad y dirección de cierre. Resuelve el defecto de no-falsabilidad de V-006. Es una lista, no una fórmula abierta.
- ✔ **R3a — Contradicciones elevadas y resueltas una a una.** Presente en §4.7bis: C-001…C-006, cada una con «Resolución propuesta» individual. Cubre las cinco que el encargo nombra (C-002, C-003, C-004, C-005, C-006) y añade C-001.
- ✘ **R3b — C-005: transitoria que haga el propio ADR admisible bajo su propia regla.** La transitoria existe y admite expresamente el caso fundacional, pero **su condición literal no es hermética**: ver V-201 y C-007. Este es el único punto que impide el CONFORME.
- ✔ **R4 — Adjudicación del caso de fondo.** Presente en §4.5 y §4.5.1: demostración de mala especificación (patrón monótono 384<512<640 vs. pico aislado, apoyada en el texto del `exp-004/PREREG.md` «MESETA … o … PICO aislado»); 512 pre-registrado el 2026-06-24 y no re-optimizado (640 superior y aun así no adoptado); veredicto CUESTIONADA con literal, condiciones (i)/(ii) y cláusula del segundo disparo. El propio ADR declara esta demostración como la «forma más débil» admitida por el requisito (1) — declaración honesta, no defecto de método.
- ✔ **R5 — Cero declaraciones de completitud propia.** Verificado por barrido literal: no aparece «remediación completa», «punto por punto», «cumple el encargo», «responde a todas» ni equivalente. §4.8 y el Anexo A se auto-limitan expresamente («No es una declaración de cumplimiento… la insuficiencia es del ADR»). El principio 17 (9)(c) eleva la prohibición a norma. Roza el límite en §4.5.1 y Anexo A, pero cada afirmación queda cubierta (O-003).
- ✔ **R6 — Formato.** Plantilla de 5 preguntas (§1–§5) verificada contra `ADR-0000-plantilla.md`; estado «Propuesta»; secuencia explícita en §4.7 (dictamen A-04 CONFORME → ratificación IP → enmiendas + registros + efectos). Anexos después de §5 (corrige O-004 del v2).

**Resolución de las violaciones y contradicciones de los dos dictámenes previos**

- ✔ **V-001** (fuente normativa de la excepción) — atacada en su raíz: la excepción se concede por **enmienda constitucional** (principio 17), no por ADR simple. Incorporación diferida a la ratificación (§4.7 paso 4.a), que es la secuencia correcta. Pendiente de acto del IP, no del redactor.
- ✔ **V-002** (efectos consumados antes de ratificar) — §4.1 suspende el efecto normativo de todos los actos de pipeline hasta la ratificación; §4.5(6) re-fecha la condición (i) a la ratificación, no al 07-17; requisito (4): «Ningún acto ejecutado en ese intervalo consolida derecho».
- ✔ **V-003** (inventario) — resuelta: §4.1 (era «sin respuesta» en ambos dictámenes previos).
- ✔ **V-004** (ficha / duplicación) — §4.6.3 (ficha como fuente única) + resolución de C-002/C-006.
- ✔ **V-005** (nota de exp-005 + lente de juicio) — Parte II + §4.1 acto 2 + principio 17 cubre «cambiar la lente de juicio».
- ✔ **V-006** (falsabilidad de «experimentos pendientes») — §4.5.1 (ver R2).
- ✔ **V-101/V-102/V-103** (rótulo de cobertura; registros que declaran remediación completa; C-002/003/004 no elevadas) — §4.8 no emplea rótulo de cobertura; §4.6.5 corrige las declaraciones al ratificar; §4.7bis eleva las tres contradicciones nominadas.
- ✔ **C-001…C-006** — elevadas y con resolución propuesta en §4.7bis. Su **resolución** es del IP; A-04 solo verifica que consten elevadas y resueltas una a una: lo están.

**Coherencia interna / admisibilidad bajo su propia transitoria**

- ✘ **AI-1.** El ADR es internamente coherente salvo en un punto, y ese punto es precisamente el de su autoadmisibilidad. Ver V-201 y C-007.

```
────────────
```

## Violaciones

**V-201 — La transitoria condiciona la admisión del caso fundacional a un requisito que ese caso no puede satisfacer, y que no exime.**

- Norma, textual (principio 17, requisito (9)(b)): «La petición debe iniciarse **antes de que se ejecute un solo acto que presuponga la anulación**: el día del disparo es el día del ADR.»
- Norma, textual (principio 17, disposición transitoria): «La admisión queda **condicionada a que satisfaga los demás requisitos en su integridad** —lo que verifica A-04, no el propio ADR— **y a que cumpla el (4) hacia adelante**…».
- Hecho: el caso fundacional (disparo 2026-07-06; ADR 2026-07-18) ejecutó una veintena de actos que presuponen la anulación **antes** de la petición (todo el inventario de §4.1). Por tanto **no cumple (9)(b)** y no puede cumplirlo: es un caso anterior al artículo. La transitoria exime expresamente el requisito **(4)** («hacia adelante») y, al decir «se admite un (1) solo caso anterior», exime de hecho el **(9)(a)** («inadmisible de plano»). Pero **no menciona el (9)(b)**, que queda dentro de «los demás requisitos… en su integridad» que la transitoria exige satisfacer. Leído a la letra, el caso fundacional es a la vez admitido (por la transitoria) y no admisible (por (9)(b) recapturado por la propia transitoria).
- Evidencia: §4.1 (actos 1–22, todos anteriores a la petición del 07-18); principio 17 (9)(b) y disposición transitoria, citados arriba; §4.7 paso 1 fecha la Propuesta el 07-18.
- Por qué cuenta: el encargo (req. 3, C-005) exige que la transitoria haga al propio ADR-0007 **admisible bajo su propia regla**. La admisibilidad queda dependiendo de una lectura no escrita —que «los demás requisitos» excluye (9)(b), o que el régimen de admisibilidad (9) entero queda desplazado por la transitoria como *lex specialis*—. La regla de conducta prohíbe a A-04 suplir esa lectura («nunca interpretes intenciones»). Con la dieta y el texto en la mano, la autoadmisibilidad **no está establecida de forma hermética**; el requisito se dicta no verificado y cuenta contra la conformidad. Nota exigida por la regla: esto no juzga el fondo — la doctrina puede ser correcta y el caso merecer la excepción, y aun así el texto que la concede tiene una junta abierta en el punto exacto que el encargo mandó blindar.

```
────────────
```

## Contradicciones detectadas (se reportan, JAMÁS se resuelven)

**C-007 (nueva) — Contradicción interna del principio 17: requisito (9)(b) vs. su disposición transitoria.**

- Requisito (9)(b): la petición debe iniciarse antes de todo acto que presuponga la anulación.
- Disposición transitoria: admite «un (1) solo caso anterior a su entrada en vigor» y condiciona la admisión a «los demás requisitos… en su integridad» + «(4) hacia adelante».
- El texto no declara si (9)(a) y (9)(b) están entre «los demás requisitos» exigidos «en su integridad» o si el régimen de admisibilidad de (9) queda íntegramente desplazado por la transitoria para el caso fundacional. Bajo la primera lectura, la transitoria se autobloquea; bajo la segunda, no. Resolverlo es del IP por ADR (o por corrección del texto antes de ratificar); A-04 lo reporta y no lo resuelve.

*(Las contradicciones C-001…C-006 del expediente ADR-0006 quedan **elevadas y con resolución propuesta** por el propio ADR-0007 en §4.7bis; no se re-reportan aquí como abiertas. Su resolución de fondo la ratifica o rechaza el IP.)*

```
────────────
```

## Observaciones

**O-001 — Límite de verificación del inventario por la dieta.** El encargo pide inventario «completo». Dentro de la dieta se verifican los actos 1, 2, 5, 13, 14, 16, 18, 19, 21 y 22 (y se corrobora el subconjunto V-003 íntegro). Los actos 3, 4, 6, 7, 8, 9, 10, 11, 12, 17 y 20 —y varios *timestamps* internos— dependen de `exp-006/`, `exp-007/`, `exp-008/`, actas e informes que **quedan fuera de la dieta**: se toman como declarados y **no** se dan por verificados. Con la dieta entregada **no se detecta ningún acto faltante** del período bajo el override de H-001, y el alcance exigido por V-003 está cubierto; por eso R1 pasa. La completitud plena de los 22 actos no es confirmable desde esta dieta.

**O-002 — Actos de H-002 en la misma ventana, fuera de alcance.** `ESTADO.md` registra actos de gobernanza de H-002 dentro del 07-06→07-17 (Banco APROBADO 07-14, forward en paper 07-15, ficha 07-16). El inventario de §4.1 se acota expresamente a los actos ejecutados **bajo el override del veredicto de exp-004 (pipeline de H-001)**; los de H-002 no lo están y su exclusión es correcta por ese alcance definido. Se registra para dejar constancia de que se verificó.

**O-003 — R5 roza el límite sin cruzarlo.** §4.5.1 («el compromiso falsable restante se reduce a un único experimento pendiente: P-1») y el Anexo A afirman cierre/localización de puntos; ambas quedan cubiertas porque la enumeración cerrada es precisamente lo que el req. 2 exige y porque el Anexo se auto-declara no-cumplimiento. No llega a violación.

**O-004 — Discrepancia documental heredada, bien elevada.** El acto 5 hace constar que la nota de exp-005 lleva fecha 07-06 y el `RESULTADO` timestamp 07-07 03:37, y la eleva «sin resolver». Es el tratamiento correcto; se anota que la verificación de esa discrepancia excede la determinabilidad del repositorio y no afecta a este dictamen.

```
────────────
```

## Respuesta a las cuatro preguntas del encargo del arbitraje

- **(a) ¿Cumple el mandato de 4 partes?** **Sí.** Partes I, II, III y IV presentes con el contenido y los literales exigidos (M-I…M-IV).
- **(b) ¿Cumple los 6 requisitos técnicos?** **Cinco sí (R1, R2, R4, R5, R6) y R3 parcialmente.** Las contradicciones se elevan y resuelven una a una (R3a ✔); pero la sub-exigencia de C-005 —transitoria que blinde la admisibilidad del propio ADR— no queda hermética (R3b ✘). Ver V-201.
- **(c) ¿Resuelve cada violación y contradicción de los dos dictámenes?** **Sí, todas quedan atendidas.** V-003 y V-006 (antes «sin respuesta») ahora resueltas; V-004/V-005 mantenidas; V-101/102/103 atendidas; C-001…C-006 elevadas con resolución propuesta. **V-001 y V-002 subsisten solo como pendientes de un acto del IP** (enmienda efectiva + ratificación fechada), por diseño de la secuencia y no por defecto del redactor.
- **(d) ¿Coherencia interna, incluida la admisibilidad bajo su propia transitoria?** **Coherente salvo en un punto, y es el de la autoadmisibilidad.** La transitoria admite el caso fundacional y exime expresamente el requisito (4) y, de hecho, el (9)(a); **omite el (9)(b)**, que su propia cláusula «los demás requisitos en su integridad» recaptura y que el caso no puede satisfacer. La admisibilidad depende de una lectura no escrita. Es una junta abierta, estrecha y de arreglo trivial — pero es exactamente la que el encargo mandó cerrar.

## Condición de levantamiento

Para que este dictamen pase a CONFORME basta **una** corrección, previa a la ratificación:

1. **V-201 / C-007** — Añadir a la disposición transitoria una cláusula expresa que exima al caso fundacional de los requisitos de admisibilidad **(9)(a) y (9)(b)** —en paralelo exacto a como ya exime el (4) «hacia adelante»—, o bien declarar expresamente que el régimen de admisibilidad del requisito (9) queda desplazado por la transitoria para este único caso. Con esa frase, «los demás requisitos… en su integridad» deja de recapturar un requisito estructuralmente inalcanzable y la autoadmisibilidad queda establecida en el texto, no en la interpretación.

**Fuera del alcance de este levantamiento (dependen del IP, no del redactor):** la incorporación efectiva del principio 17 a `CONSTITUCION.md` y la ratificación fechada (V-001, V-002). No pueden levantarse en sede arbitral; se ejecutan en el acto de ratificación según §4.7, y solo después de un dictamen A-04 CONFORME.

**Alcance de lo que este dictamen NO dice.** No juzga si la doctrina del principio 17 es buena norma, si la excepción es defendible en el fondo, si el criterio de exp-004 estaba mal especificado, ni si H-001 tiene edge. Ninguna de esas preguntas es competencia de A-04; las resuelve el IP, compuerta separada. Este dictamen dice una sola cosa: el ADR-0007 es, con mucha diferencia, un artefacto sólido que cumple el mandato de cuatro partes, cinco de los seis requisitos técnicos y la resolución de todo el pasivo de los dos dictámenes previos — **y falla en un solo punto verificable: la transitoria no cierra a la letra la admisibilidad del propio ADR bajo su propia regla, que es la pieza que el encargo señaló como crítica (C-005).**

```
────────────
Firma: A-04 · 2026-07-18 · sesión independiente
```
