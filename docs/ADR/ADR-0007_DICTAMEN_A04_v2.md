# DICTAMEN A-04 — ADR-0007 (Acto fundacional) — v2 (re-arbitraje tras la cura de V-201/C-007)

```
DICTAMEN A-04
Artefacto evaluado: docs/ADR/ADR-0007-acto-fundacional-doctrina-de-excepcion.md
                    (Estado: "Propuesta"; Versión v2 — 2026-07-18; commit d2b975f;
                     reemplaza al ADR-0006 rechazado)
Re-arbitraje de: DICTAMEN A-04 v1 (ADR-0007_DICTAMEN_A04.md), que dictó NO CONFORME
                 por V-201 / C-007 (transitoria no eximía (9)(b)).
Estado: ☒ CONFORME   ☐ NO CONFORME
────────────
```

## Dieta de insumos (declaración obligatoria)

Modo VALIDADOR ESTRICTO. El artefacto es un ADR, no un documento de fase del Banco; se aplica la dieta del modo general (prompt A-04 + documentos normativos que apliquen) con **las prohibiciones y la plantilla del modo estricto**. Insumos recibidos y usados, exactamente los ordenados por el encargo de este re-arbitraje: `ADR-0007_ENCARGO.md`; `ADR-0006_DICTAMEN_A04.md` y `_v2.md`; `CONSTITUCION.md`; `PROTOCOLO.md`; `ADR-0000-plantilla.md`; `exp-004/` completo (PREREG, RESULTADO, NOTA); `exp-005/` completo (PREREG, RESULTADO, NOTA); ficha `H-001-canal-donchian.md`; `REGISTRO_HIPOTESIS.md`; `ESTADO.md`; `PREREG_FASE_AB.md` con su **ENMIENDA 1**; y — **por autorización expresa del encargo de re-arbitraje, y solo para la comparación v1↔v2 de la línea normativa cambiada** — el historial de git (`git show d2b975f`, estado v1 en `5dbee73`).

**Se declara y no se ignora:** `ADR-0007_REVISION_PREVIA.md` **no** es insumo normativo (lectura previa no vinculante de un tercero); no se leyó ni pesa en este dictamen. `exp-006/`, `exp-007/`, `exp-008/`, las actas de fase e `informe_cierre_faseA.md` **quedan fuera de la dieta**; sus contenidos no se dan por verificados (subsiste el límite O-001 del v1).

**Alcance.** Se verifica cumplimiento del método, con cita textual de la norma. No se juzga la calidad de la doctrina propuesta, ni si el criterio de `exp-004` estaba bien o mal especificado, ni si H-001 tiene edge, ni si la enmienda constitucional es buena norma: eso es del IP, compuerta separada. Carga de la prueba del artefacto: lo no verificable con la dieta cuenta contra la conformidad. Atendida la instrucción de §4.8 del propio ADR: **el documento no declara su propia conformidad — la dicta este dictamen.**

**Naturaleza de este dictamen.** Es un **re-arbitraje**. El v1 verificó y dio por ✔ el mandato de 4 partes, cinco de los seis requisitos técnicos y la resolución de todo el pasivo de los dos dictámenes previos, y reservó un único punto bloqueante: **V-201 / C-007** (la transitoria condicionaba la admisión del caso fundacional a «los demás requisitos en su integridad», cláusula que recapturaba el requisito (9)(b) — estructuralmente inalcanzable para un caso anterior al artículo — sin eximirlo de forma expresa). Este dictamen verifica **prioritariamente** si la cura de la v2 cierra ese punto a la letra, y **confirma contra git que ninguna otra línea normativa se ha modificado**.

## Verificación de la cura (V-201 / C-007) contra la condición de levantamiento del v1

La condición de levantamiento del v1 pedía, textualmente: *«Añadir a la disposición transitoria una cláusula expresa que exima al caso fundacional de los requisitos de admisibilidad (9)(a) y (9)(b) —en paralelo exacto a como ya exime el (4) “hacia adelante”—, o bien declarar expresamente que el régimen de admisibilidad del requisito (9) queda desplazado por la transitoria para este único caso.»*

Texto de la transitoria en v2 (principio 17, disposición transitoria única), verificado literalmente:

- **(i) Exención expresa de (9)(a) y (9)(b) para el caso fundacional — ✔ ACREDITADA.** «Ese caso no pudo cumplir el requisito (4) en su momento, **ni puede cumplir los requisitos de admisibilidad (9)(a) … y (9)(b) …, por ser estructuralmente un caso anterior a este artículo.** En exacto paralelo a como esta transitoria exime al caso fundacional del requisito (4) … **lo exime también, de forma expresa, de los requisitos de admisibilidad (9)(a) y (9)(b)**». Los dos sub-requisitos que el v1 señaló están nombrados uno a uno y eximidos en paralelo al (4), que es la forma exacta que pedía la condición de levantamiento.
- **(ii) Recaptura por «los demás requisitos en su integridad» — ✔ ROTA A LA LETRA.** «…de modo que la exigencia de que “satisfaga los demás requisitos en su integridad” **no comprende (9)(a) ni (9)(b), que no le son aplicables**.» Ésta es la frase que desactiva el bucle de autobloqueo que constituía V-201: «los demás requisitos… en su integridad» deja de recapturar (9)(b).
- **(iii) Desplazamiento del régimen del (9) solo para este caso — ✔ ACREDITADO.** «para este único caso, el régimen de admisibilidad del requisito (9) queda **desplazado** por esta disposición transitoria» + «Este desplazamiento del requisito (9) **se agota con el caso fundacional**».
- **(iv) Régimen (9) íntegro para todo caso posterior — ✔ ACREDITADO.** «**para todo caso posterior, el requisito (9) —incluidos (9)(a) y (9)(b)— rige íntegro, sin desplazamiento ni exención de ninguna clase**, y esta transitoria no puede invocarse para admitir un segundo caso anterior.»

La condición de levantamiento se cumple por **ambas** de las dos vías que ofrecía (exención expresa nominativa **y** declaración de desplazamiento acotado), no solo por una. La cura no crea vía para un segundo caso retroactivo: el desplazamiento se declara agotado con el caso fundacional y la retroactividad sigue clausurada para todo lo demás (párrafos finales de la transitoria, sin cambios).

## Verificación de «ninguna otra línea normativa cambió» (git v1 ↔ v2)

`git show d2b975f` (único commit sobre el ADR posterior al estado v1 `5dbee73`; el commit del dictamen v1 `65da7e4` no tocó el ADR) arroja **exactamente dos hunks**:

1. **Cabecera — línea «Versión: v2 …» añadida.** Es metadato de versión. Por la propia **convención de lectura del ADR (§4)**, solo el bloque citado del principio 17 (Parte III) es texto normativo; la cabecera es texto de motivos. No es línea normativa.
2. **Disposición transitoria — una línea sustituida (la cura).** Es la única modificación de texto **normativo**, y es precisamente la exigida.

El único texto normativo del ADR es el principio 17, y dentro de él solo cambió la transitoria. Esto acredita a la letra la afirmación de la cabecera v2: **«Ninguna otra línea normativa se modifica.»** Los requisitos (1)–(9) del principio 17, el párrafo de encabezamiento, «El veredicto mecánico jamás se edita», y todo el articulado restante son **byte-idénticos** a la v1. En consecuencia, todo lo que el v1 marcó ✔ sobre ese texto permanece ✔ sin necesidad de re-litigarlo.

## Requisitos verificados

**Mandato del IP — estructura de 4 partes (encargo §Mandato)** — texto idéntico a v1 (git); se reconfirma:

- ✔ **M-I.** Parte I — Reconocimiento expreso, con el literal «El laboratorio incumplió su propio protocolo entre el 6 y el 17 de julio de 2026. Sin matices…».
- ✔ **M-II.** Parte II — Declaración de nulidad; notas de `exp-004`/`exp-005` «nunca tuvieron efectos normativos»; alcance cerrado a las dos notas del 2026-07-06. **Verificado contra el repositorio:** existen **exactamente dos** ficheros `NOTA_*_interpretacion.md` (en `exp-004/` y `exp-005/`); no hay una tercera nota. La cláusula de alcance cerrado no omite ninguna.
- ✔ **M-III.** Parte III — Nueva doctrina como principio 17 (requisitos (1)–(9) + transitoria).
- ✔ **M-IV.** Parte IV — Cláusula única e irrepetible + transitoria: «Después de este caso, la retroactividad no puede volver a existir. Nunca.»

**Requisitos técnicos del encargo (6)**

- ✔ **R1 — Inventario de actos 07-06→07-17.** §4.1: 22 actos fechados con pronunciamiento de validez uno a uno. Verificado dentro de la dieta: `exp-004` letal (acto 1/nota; RESULTADO «H-001 MATADA», 384 net −8.59%/α −28.64% → MATA, 640 MESETA, 512 no cambiado), `exp-005` BANDERA (acto 5; RESULTADO «BANDERA (HYPE net<=0 o alpha<=0)»), Fase B / re-corte y `exp-008` según ficha/ESTADO/PREREG. **Con la dieta entregada no se detecta ningún acto ni nota faltante** del período bajo el override de H-001; el subconjunto exigido por V-003 está íntegro. Límite de completitud plena declarado en **O-001** (actos que dependen de `exp-006/007/008`/actas quedan fuera de dieta: declarados, no verificados).
- ✔ **R2 — Enumeración cerrada de «experimentos pendientes».** §4.5.1: lista explícita (P-1 Fase B; P-2 sello de Fase C, excluido por no ser experimento), horizonte (P-1 cierre ≤ 2026-08-16; condición (ii) satisfecha a más tardar 2026-09-30), reglas de cómputo, prospectividad y dirección de cierre. **Verificado contra la fuente:** los criterios letales de P-1 (TE fuera de ±5%; slippage mediana de exceso > 5 bps; ≥1 omisión BTC por `min_notional` sin decisión documentada; desviación de métrica sin explicación) reproducen los criterios de `PREREG_FASE_AB.md` + **ENMIENDA 1** (2026-07-14); el horizonte «un mes desde el re-corte del 07-16» = 08-16 es correcto. Es lista cerrada, no fórmula abierta. Resuelve V-006.
- ✔ **R3a — Contradicciones elevadas y resueltas una a una.** §4.7bis: C-001…C-006, cada una con «Resolución propuesta» individual (texto idéntico a v1). A-04 verifica que consten **elevadas y resueltas una a una**; su resolución de fondo la ratifica o rechaza el IP.
- ✔ **R3b — C-005: transitoria que haga el propio ADR admisible bajo su propia regla.** **Antes ✘ (era el único bloqueante); ahora ✔.** La transitoria v2 exime expresamente (9)(a) y (9)(b) y declara desplazado el régimen del (9) solo para el caso fundacional. La autoadmisibilidad queda establecida **en el texto**, no en una lectura no escrita. Ver la sección «Verificación de la cura».
- ✔ **R4 — Adjudicación del caso de fondo.** §4.5/§4.5.1: demostración de mala especificación apoyada en el texto de `exp-004/PREREG.md` («MESETA … o … PICO aislado») y en el patrón monótono 384 < 512 < **640** (verificado en `exp-004/RESULTADO.md`: Calmar −0.34 / 1.35 / 1.74); 512 pre-registrado el 2026-06-24 y no re-optimizado pese a que 640 es superior; veredicto CUESTIONADA con literal y condiciones (i)/(ii). El propio ADR declara esta demostración como la «forma más débil» admitida por (1) — declaración honesta, no defecto de método.
- ✔ **R5 — Cero declaraciones de completitud propia.** Barrido literal sobre la v2: no aparece «remediación completa», «punto por punto», «cumple el encargo», «responde a todas» ni equivalente. §4.8 y el Anexo A se auto-limitan; (9)(c) eleva la prohibición a norma. La línea de cabecera añadida en v2 dice «Único cambio de fondo…» y «Ninguna otra línea normativa se modifica» — son afirmaciones **verificables y verificadas** sobre el alcance del cambio (no rótulos de completitud del cumplimiento del encargo), y se confirman contra git; no constituyen sobre-declaración prohibida por R5.
- ✔ **R6 — Formato.** Plantilla de 5 preguntas (§1–§5) conforme a `ADR-0000-plantilla.md`; estado «Propuesta»; secuencia explícita en §4.7 (dictamen A-04 CONFORME → ratificación IP → enmiendas + registros + efectos); anexos después de §5. Sin cambios respecto de v1.

**Resolución de las violaciones y contradicciones de los dos dictámenes previos** (texto idéntico a v1 salvo el punto curado):

- ✔ **V-001** (fuente normativa) — la excepción se concede por enmienda constitucional (principio 17), incorporación diferida a la ratificación (§4.7 paso 4.a). **Subsiste solo como pendiente de un acto del IP**, no del redactor.
- ✔ **V-002** (efectos consumados antes de ratificar) — §4.1 suspende el efecto de pipeline hasta la ratificación; §4.5(6) re-fecha la condición (i); requisito (4): «Ningún acto ejecutado en ese intervalo consolida derecho». **Pendiente de acto del IP.**
- ✔ **V-003** (inventario) — §4.1. ✔ **V-004** (ficha/duplicación) — §4.6.3 + C-002/C-006. ✔ **V-005** (nota de `exp-005`/lente) — Parte II + §4.1 acto 2 + principio 17. ✔ **V-006** (falsabilidad) — §4.5.1.
- ✔ **V-101 / V-102 / V-103** — §4.8 sin rótulo de cobertura; §4.6.5 corrige declaraciones al ratificar; §4.7bis eleva las tres contradicciones nominadas.
- ✔ **V-201 / C-007** (abiertas en el v1) — **CERRADAS por la cura de la v2.** Ver secciones «Verificación de la cura» y «Contradicciones».
- ✔ **C-001…C-006** — elevadas con resolución propuesta en §4.7bis; su resolución de fondo es del IP.

**Coherencia interna / admisibilidad bajo su propia transitoria**

- ✔ **AI-1.** Resuelto el único punto que el v1 dejó abierto: el ADR es ahora **admisible bajo su propia regla en el texto**, sin apelar a lectura no escrita. La transitoria admite el caso fundacional, exime expresamente (4), (9)(a) y (9)(b) hacia atrás, exige (4) hacia adelante y el resto de requisitos, y se autoderoga por cumplimiento.
- ✔ **AI-2 (revisado tras la cura).** Se comprobó que la cura no abre contradicción nueva con Parte IV (puntos 3 y 4: (9)(a) inadmisibilidad de plano y «este ADR no es precedente») — ambos son prospectivos «desde la ratificación» y no alcanzan al propio ADR-0007, eximido por la transitoria. Coherente.

```
────────────
```

## Violaciones

**Ninguna.** El único punto que impedía el CONFORME en el v1 (V-201) queda subsanado a la letra por la disposición transitoria de la v2. Los residuos V-001 y V-002 **no son violaciones del redactor**: son pasos que, por diseño de la secuencia (§4.7), solo puede ejecutar el IP (incorporación efectiva del principio 17 y ratificación fechada), y ocurren **después** de un dictamen A-04 CONFORME. No pueden levantarse en sede arbitral y no cuentan contra la conformidad de este artefacto.

```
────────────
```

## Contradicciones detectadas (se reportan, JAMÁS se resuelven)

**Ninguna abierta.**

- **C-007** (abierta en el v1: ambigüedad sobre si (9)(a)/(9)(b) estaban entre «los demás requisitos… en su integridad») **queda cerrada** por el texto de la v2, que declara expresamente que esa exigencia **«no comprende (9)(a) ni (9)(b)»** y que el régimen del (9) queda desplazado solo para el caso fundacional. Ya no hay dos lecturas: el texto elige una y la escribe.
- **C-001…C-006** permanecen **elevadas y con resolución propuesta** por el propio ADR en §4.7bis; su resolución de fondo la ratifica o rechaza el IP. No se re-reportan aquí como abiertas.

```
────────────
```

## Observaciones (de proceso; no bloquean la conformidad)

**O-001 — Límite de verificación del inventario por la dieta (subsiste del v1).** El encargo pide inventario «completo». Los actos que dependen de `exp-006/`, `exp-007/`, `exp-008/`, actas e informes quedan fuera de la dieta: se toman como declarados y no se dan por verificados. Con la dieta entregada **no se detecta ningún acto ni nota faltante** del período bajo el override de H-001, y el subconjunto exigido por V-003 está cubierto; por eso R1 pasa. La completitud plena de los 22 actos no es confirmable desde esta dieta.

**O-006 (nueva) — Referencia a un fichero de respaldo inexistente en la cabecera de versión.** La línea «Versión: v2» añadida por la cura afirma: «**v1** = redacción original del 2026-07-18 (conservada como `ADR-0007-…v1-backup-2026-07-18.md`)». Verificado contra el repositorio: **ese fichero no existe** en el árbol de trabajo y **nunca estuvo versionado** (el propio commit `d2b975f` declara «backup eliminado (git es el historial)»). Es una referencia colgada en texto de **metadato/motivos** (no normativo por la convención de §4), por lo que **no afecta a ninguna de las 4 partes, a los 6 requisitos, ni a la admisibilidad**, y no bloquea el CONFORME. Se hace constar porque una casilla de verificación literal debe señalar una afirmación documental falsa. **Corrección sugerida (opcional, no condición de levantamiento):** sustituir la referencia al fichero por el puntero real al historial (p. ej., «v1 = commit `5dbee73`»).

**O-007 (nueva) — Texto de aplicación de §4.7bis C-005 no re-redactado tras la cura.** La resolución de C-005 en §4.7bis conserva la formulación pre-cura «le exige el cumplimiento íntegro de los demás requisitos» sin el nuevo inciso que excluye (9)(a)/(9)(b). **No es contradicción** con la transitoria curada: §4.7bis es **texto de aplicación** (enumerado como tal en la convención de lectura de §4), y esa misma convención dispone que «en caso de discrepancia entre ambos niveles prevalece el texto de la Parte III». La prevalencia neutraliza cualquier lectura divergente. Se anota solo para dejar constancia de que la coherencia se re-verificó después de la cura y de que, si se desea pulcritud plena, convendría alinear la redacción de §4.7bis con el inciso nuevo — sin que ello sea condición de nada.

**O-008 (nueva) — Constancia sobre el mensaje de commit, fuera del artefacto.** El mensaje de `d2b975f` menciona «anexo A sincronizado»; el diff muestra que el Anexo A **no** se modificó. No es defecto del ADR (el Anexo A no requería cambio: sus referencias a (9)/(9)(c) son ajenas a la exención de (9)(a)/(9)(b)); el mensaje de commit no forma parte del artefacto arbitrado. Se registra únicamente para dejar constancia de que se cotejó.

```
────────────
```

## Respuesta a las cuatro preguntas del encargo

- **(a) ¿Cumple el mandato de 4 partes?** **Sí.** Partes I–IV presentes con el contenido y los literales exigidos (M-I…M-IV), texto idéntico al ya verificado en v1 (git).
- **(b) ¿Cumple los 6 requisitos técnicos?** **Sí, los seis.** R1, R2, R4, R5, R6 ya ✔ en v1 y con texto inalterado; **R3 pasa ahora íntegro**: R3a (contradicciones elevadas y resueltas) y **R3b** (la transitoria blinda la admisibilidad del propio ADR) tras la cura.
- **(c) ¿Resuelve cada violación y contradicción de los dos dictámenes?** **Sí, todo el pasivo queda atendido.** V-003 y V-006 resueltas; V-004/V-005 mantenidas; V-101/102/103 atendidas; C-001…C-006 elevadas con resolución propuesta; y **V-201/C-007 —el único residuo del propio v1— cerrados a la letra**. V-001 y V-002 subsisten solo como **pendientes de un acto del IP** (enmienda efectiva + ratificación fechada), por diseño de la secuencia y no por defecto del redactor.
- **(d) ¿Coherencia interna, incluida la admisibilidad bajo su propia transitoria?** **Sí, ahora sin excepción.** La junta abierta que el v1 identificó (la autoadmisibilidad dependiente de una lectura no escrita) está cerrada en el texto: la transitoria exime expresamente (9)(a) y (9)(b), desplaza el régimen del (9) solo para el caso fundacional, lo restituye íntegro para todo caso posterior, y se autoderoga por cumplimiento. La cura no introduce contradicción nueva (verificado contra Parte IV y §4.7bis vía la regla de prevalencia).

## Veredicto

**CONFORME.** El ADR-0007 v2 cumple el mandato de cuatro partes, los seis requisitos técnicos del encargo y la resolución de todo el pasivo de los dos dictámenes previos, y es internamente coherente y **admisible bajo su propia transitoria**. La única violación que bloqueaba el v1 (V-201) y su contradicción asociada (C-007) están subsanadas a la letra, y git confirma que la cura tocó exclusivamente la línea normativa exigida más un metadato de versión: **ninguna otra línea normativa cambió**.

## Qué queda pendiente (acto del IP, no del redactor)

Este dictamen CONFORME es el paso 2 de la secuencia de §4.7. **No** convalida efecto alguno por sí mismo. Restan, en este orden y como acto único del IP (§4.7 pasos 3–4): la **ratificación fechada**; y solo entonces la incorporación efectiva del principio 17 a `CONSTITUCION.md`, la enmienda de `PROTOCOLO.md`, la actualización de ficha/`REGISTRO`/`ESTADO`/`CHANGELOG`, el erratum adjunto a `exp-008/PREREG.md`, la nota de C-001 en `ADR-0000-plantilla.md` y los efectos (convalidación de Fase A y del re-corte de Fase B; condición (i) vigente; cláusula del segundo disparo vigente). Si el IP no ratifica, rige el veredicto letal de `exp-004` con todas sus consecuencias, incluida la regla de versionado.

**Alcance de lo que este dictamen NO dice.** No juzga si la doctrina del principio 17 es buena norma, si la excepción es defendible en el fondo, si el criterio de `exp-004` estaba mal especificado, ni si H-001 tiene edge. Ninguna de esas preguntas es competencia de A-04; las resuelve el IP, compuerta separada.

```
────────────
Firma: A-04 · 2026-07-18 · sesión independiente · re-arbitraje v2 (cura de V-201/C-007)
```
