# DICTAMEN A-04 — ADR-0006 v2 (RE-ARBITRAJE)

```
DICTAMEN A-04
Artefacto evaluado: docs/ADR/ADR-0006-override-veredicto-exp004.md
                    versión v2 (Estado: "Propuesta v2", enmendada 2026-07-18, §6 "ENMIENDA v2")
                    Re-arbitraje del dictamen A-04 del 2026-07-18 (6 violaciones, 4 contradicciones)
Estado: ☐ CONFORME   ☒ NO CONFORME
────────────
```

## Dieta de insumos (declaración obligatoria)

Modo VALIDADOR ESTRICTO ordenado. Se recibieron: prompt A-04, dictamen previo `ADR-0006_DICTAMEN_A04.md`, artefacto v2. Se abrieron además, por ser **los registros donde la propia v2 afirma haber ejecutado la remediación** (no se puede verificar una cura sin abrir el registro curado): `hipotesis/H-001-canal-donchian.md`, `REGISTRO_HIPOTESIS.md`, `ESTADO.md`, `CONSTITUCION.md`, `PROTOCOLO.md`, `CHANGELOG.md`, `exp-005/{RESULTADO.md, NOTA_2026-07-06_interpretacion.md}`, `exp-004/RESULTADO.md`, `exp-008/PREREG.md`, `git log`/`git show HEAD`. Se declara y no se ignora.

**Alcance del re-arbitraje.** Se verifica **remediación**, no calidad de la decisión de fondo. Cada violación y contradicción del dictamen previo se contrasta una por una contra su condición de levantamiento textual. Carga de la prueba del artefacto: lo no verificable cuenta contra la conformidad.

## Requisitos verificados — una condición de levantamiento por línea

**Condición 1 (V-001) — Enmienda de `CONSTITUCION.md`, o declaración de la norma habilitante.**

- ✘ **NO CUMPLIDA.** `CONSTITUCION.md` sigue **sin modificación**: `grep -i "excepci|ADR-0006|enmienda"` sobre el fichero → **cero coincidencias**. El preámbulo conserva íntegro «Cualquier decisión que los contradiga requiere modificar **primero** este documento mediante un ADR». La v2 §6.4 **propone** un texto y declara expresamente que se incorporará «COMO PARTE de la ratificación (**no antes**)». Una propuesta no es una modificación. La excepción sigue, a fecha de este dictamen, sin fuente normativa vigente. Ver además C-005.

**Condición 2 (V-002) — Ratificación del IP fechada + declaración sobre la condición (i) consumida.**

- ✘ **PARCIAL.** La segunda mitad sí se cumple: la v2 §6.3 reconoce la violación de secuencia y re-etiqueta el efecto. Verificado literalmente en los tres registros:
  - `REGISTRO_HIPOTESIS.md`: ✔ «La condición (i) del ADR-0006 queda cumplida **SUJETA A RATIFICACIÓN del ADR-0006 (Propuesta v2…)**».
  - `ESTADO.md`: ✔ «**sujeto a ratificación del ADR-0006** (Propuesta v2 tras dictamen A-04 NO CONFORME del 07-18…)».
  - `H-001-canal-donchian.md`, fila 2026-07-17: ✔ «condición (i) cumplida **sujeta a ratificación del ADR-0006**».
  - La primera mitad **no puede cumplirse por el artefacto**: la ratificación del IP no consta y el ADR sigue en «Propuesta v2». El punto se dicta NO CUMPLIDO por falta de hecho, sin reproche al redactor. Residuo material en O-002.

**Condición 3 (V-003) — Inventario fechado, dentro del ADR, de los actos ejecutados entre 2026-07-06 y 2026-07-17, con pronunciamiento sobre la validez de cada uno.**

- ✘ **SIN RESPUESTA ALGUNA.** La §6 de la v2 enumera cuatro puntos (ficha, exp-005, condición (i), enmienda constitucional). **Ninguno es V-003.** El cuerpo del ADR conserva sin cambio la fórmula «continuó H-001 hacia Fase B/C» de §1. No hay inventario, no hay fechas, no hay pronunciamiento sobre la validez de exp-005/006/007, de la **aprobación de Fase A 6/6 del 07-14** ni del **re-corte de Fase B del 07-16**. Lo añadido a la **ficha** (fila «2026-07-14→16») es registro de eventos, no pronunciamiento normativo, y está fuera del ADR, que es donde la condición lo exigía. Ver V-101.

**Condición 4 (V-004) — Ficha al literal de §4.1 + filas append-only para exp-004 (07-06), nota interpretativa (07-06) y ADR-0006 (07-17).**

- ✔ **CUMPLIDA en lo exigido.** Verificado en `H-001-canal-donchian.md`:
  - Fila 2026-07-06: disparo letal de exp-004 con cifras, nota interpretativa del mismo día, canal declarado ilegítimo, **y** la segunda nota de exp-005. ✔
  - Fila 2026-07-17: ADR-0006, estatus degradado, exp-008 R0 sujeto a ratificación. ✔
  - Fila 2026-07-18: dictamen A-04 NO CONFORME y remediación. ✔
  - Campo nuevo «Estatus epistemológico»: «**EN VALIDACIÓN — CUESTIONADA (ADR-0006 en Propuesta)**…». Visible en cabecera. ✔
  - «Última actualización de ficha: 2026-07-18». ✔
- Residuos que **no llegan a violación** (mismo criterio literal aplicado en O-003 del dictamen previo: los elementos existen): el campo `Estado` de la misma tabla conserva «⏳ EN VALIDACIÓN — Fase A iniciada 2026-07-02» sin degradar, y el literal «edge no distinguible de suerte con datos actuales» de §4.1 no aparece textualmente. Ver C-006 y O-001.

**Condición 5 (V-005) — Pronunciamiento expreso sobre `exp-005/NOTA_2026-07-06_interpretacion.md` + ampliación del precedente a criterios no letales.**

- ✔ **CUMPLIDA.** Verificado:
  - Pronunciamiento expreso: v2 §6.2 la ampara con tratamiento declarado idéntico — «su veredicto mecánico (BANDERA por HYPE alfa≤0) queda INTACTO en su RESULTADO; el cambio de lente alfa→Sharpe post-hoc se reconoce como override por canal ilegítimo». ✔
  - Veredicto mecánico efectivamente intacto: `exp-005/RESULTADO.md` línea 50 conserva «**VEREDICTO (criterio pre-escrito, HYPE combinado): BANDERA (HYPE net<=0 o alpha<=0)**» sin edición. ✔ Igual `exp-004/RESULTADO.md` línea 19 («**H-001 MATADA**»). ✔
  - Ampliación del precedente: §4.3 v2 añade «ni **cambian lentes de juicio**» — cubre exactamente la reinterpretación de criterios no letales que el dictamen señaló fuera del texto original. ✔
  - Cita de la nota comprobada: la nota concluye literalmente «exp-005 no cambia el estado de H-001: no probada, baja convicción». La v2 la reproduce fielmente. ✔
  - **Corrección de la afirmación falsa de §4.3:** ✔ «Este ADR es la única vía retroactiva admitida» aparece **tachado** con reconocimiento expreso de su falsedad. Verificado en el diff de `39d62fa`. La sustitución («cubre AMBAS… y con ello agota la vía retroactiva») se verificó por búsqueda exhaustiva: en el repositorio existen **exactamente dos** notas interpretativas (`exp-004/` y `exp-005/`, ambas 2026-07-06). La afirmación sustituta es, hoy, fácticamente cierta. Se anota que la verificación la hizo el árbitro, no el artefacto: la v2 no enumera el conjunto que declara agotado (O-003).

**Condición 6 (V-006) — Enumeración cerrada de los «experimentos pendientes» de §4.2(ii) con horizonte temporal.**

- ✘ **SIN RESPUESTA ALGUNA.** §4.2 del ADR no fue tocado por la v2 (verificado en el diff: la línea 2 del §4 es idéntica antes y después). No hay enumeración, no hay plazo. La cláusula que el propio ADR designa como «el compromiso falsable de este ADR» sigue siendo declarable solo en contra y nunca a favor. Ver V-102.

**Condición 7 (C-001 a C-004) — Elevadas al IP para resolución por ADR.**

- ✘ **PARCIAL.** C-001 (preámbulo vs. ADR simple) sí se eleva y se le propone cauce en §6.4. **C-002 (principio 12, duplicación), C-003 (estado «CUESTIONADA» no previsto en PROTOCOLO.md) y C-004 (regla de versionado H-001.v1/v2) no reciben mención individual alguna.** La v2 se limita a la fórmula global «El dictamen encontró 6 violaciones y 4 contradicciones. Todas verificadas como ciertas.» Reconocer que existen no es elevarlas identificadas con petición de resolución. `PROTOCOLO.md` sigue enumerando solo «EN VALIDACIÓN · VALIDADA · RECHAZADA · EN PRODUCCIÓN · RETIRADA» y su §5 de versionado sigue intacto. Ver V-103.

```
────────────
```

## Violaciones

*(numeración continuada desde el dictamen previo; V-001 a V-006 conservan su identidad)*

**V-001 — SUBSISTE.** Excepción a un principio constitucional sin modificar la Constitución. Norma textual (preámbulo): «requiere modificar **primero** este documento mediante un ADR». Hecho: `CONSTITUCION.md` sin una sola línea nueva a fecha de hoy; la v2 propone el texto y difiere su incorporación a la ratificación. Evidencia: fichero sin coincidencias para «excepción», «enmienda» ni «ADR-0006»; §6.4 «(no antes)». **Estado: pendiente de acto del IP, no del redactor.**

**V-002 — SUBSISTE (mitigada).** Efectos consumados por un ADR en «Propuesta». La cura declarativa está ejecutada y verificada en los tres registros; la ratificación fechada no existe. **Estado: pendiente de acto del IP.** Residuo no curado: O-002.

**V-003 — SUBSISTE ÍNTEGRA, SIN RESPUESTA.** Ver condición 3. Ninguno de los cuatro puntos de §6 la aborda.

**V-004 — LEVANTADA.** Ver condición 4.

**V-005 — LEVANTADA.** Ver condición 5.

**V-006 — SUBSISTE ÍNTEGRA, SIN RESPUESTA.** Ver condición 6.

**V-101 (nueva) — La v2 declara una remediación de alcance total que no ejecuta.**

- Norma, textual (ADR-0006 v2 §6, encabezado): «El dictamen… encontró 6 violaciones y 4 contradicciones. Todas verificadas como ciertas. **Respuesta punto por punto:**»
- Hecho: bajo el rótulo «punto por punto» se responden **4 de 10** puntos. V-003, V-006, C-002, C-003 y C-004 no tienen punto. La numeración de §6 (1–4) tampoco mapea a los identificadores del dictamen, de modo que la omisión no es legible desde el propio artefacto.
- Evidencia: §6 puntos 1–4; ausencia de toda mención a «inventario», «experimentos pendientes», «principio 12», «versionado» o «H-001.v2» en el texto añadido (`git show 39d62fa -- docs/ADR/ADR-0006-override-veredicto-exp004.md`).
- Por qué cuenta: el checklist A-04 §5 exige trazabilidad verificable. Un rótulo de cobertura total sobre una cobertura parcial impide al IP ver, desde el artefacto que va a ratificar, qué quedó abierto.

**V-102 (nueva) — El CHANGELOG y los registros describen la remediación como completa.**

- Norma, textual (CONSTITUCION principio 14): «el Registro conserva el historial **íntegro**».
- Hecho: el mensaje de commit `39d62fa` reza «dictamen A-04 NO CONFORME sobre ADR-0006 → **remediacion v2 completa**»; `ESTADO.md` escribe «6 violaciones **verificadas y remediadas**». Dos de las seis (V-003, V-006) no están remediadas y dos más dependen de un acto futuro del IP.
- Evidencia: `git log --oneline -1`; `ESTADO.md`, fila H-001; `H-001-canal-donchian.md`, fila 2026-07-18 («Remediación aplicada»).
- Por qué cuenta: es el mismo defecto que V-004 castigaba en su día —el registro oficial diciendo algo distinto de lo verificable— con el signo invertido.

**V-103 (nueva) — Contradicciones C-002/C-003/C-004 no elevadas identificadas.**

- Norma, textual (dictamen previo, condición de levantamiento 7): «Elevadas al IP para resolución por ADR. **Basta que consten elevadas.**»
- Norma, textual (prompt A-04): «Si las normas del laboratorio se contradicen entre sí, no resuelvas la contradicción: **repórtala**».
- Hecho: no constan. Ninguna aparece nombrada, descrita ni sometida a decisión en la v2.
- Evidencia: texto íntegro de §6; `PROTOCOLO.md` §Ciclo de vida y §5 sin cambio ni nota de conflicto.

```
────────────
```

## Contradicciones detectadas (se reportan, JAMÁS se resuelven)

**C-001 a C-004 — SUBSISTEN.** C-001 se eleva y recibe cauce propuesto (§6.4); C-002, C-003 y C-004 siguen sin reportar por el artefacto. Su resolución es del IP.

**C-005 (nueva) — El texto constitucional propuesto prohíbe el acto que viene a legitimar.**

- Texto propuesto, literal (v2 §6.4): «…mediante ADR arbitrado por A-04 y ratificado por el IP **ANTES de que la anulación surta efectos**».
- Hecho: en ADR-0006 la anulación surtió efectos el **2026-07-06**; el ADR se redactó el **07-17**; el arbitraje llegó el **07-18**; la ratificación no ha llegado. Bajo la norma que el propio ADR propone, ADR-0006 sería inadmisible.
- Por qué se reporta y no se resuelve: la v2 no declara si la excepción propuesta se aplica a sí misma (efecto retroactivo) o solo a futuro, dejando la propia validez de ADR-0006 indeterminada bajo su propia enmienda. Resolver esto es del IP.

**C-006 (nueva) — Dos estatus simultáneos en la misma tabla de la ficha.**

- `H-001-canal-donchian.md`, campo **Estado**: «⏳ EN VALIDACIÓN — **Fase A iniciada 2026-07-02**».
- `H-001-canal-donchian.md`, campo **Estatus epistemológico**: «**EN VALIDACIÓN — CUESTIONADA (ADR-0006 en Propuesta)**…».
- La instrucción de §4.1 era **degradar** el estatus, no añadir un segundo campo junto al no degradado. Es la materialización, dentro de un mismo documento, del bug que el principio 12 tipifica y que C-002 ya señalaba entre documentos.

```
────────────
```

## Observaciones

**O-001 — Divergencia de literal, sin llegar a violación.** El estatus de §4.1 incluye «edge no distinguible de suerte con datos actuales»; la ficha lo sustituye por «exp-008 R0 a favor, sujeto a ratificación» y conserva «NO es edge probado» en el cuerpo. Se aplica el mismo criterio literal que O-003 del dictamen previo concedió a REGISTRO y ESTADO: los elementos existen.

**O-002 — Residuo de V-002 fuera del alcance de la cura.** La §6.3 re-etiqueta «REGISTRO/ESTADO/ficha». **No alcanza a `exp-008/PREREG.md`**, cuyo §«Contexto de acumulación (**ADR-0006 — vinculante**)» sigue declarando vinculante un ADR en propuesta. El documento está sellado como pre-registro y no debe editarse, de modo que el registro conservará permanentemente esa declaración. Se anota para que el IP decida si requiere erratum fechado adjunto —no edición— o no.

**O-003 — La verificación de «agota la vía retroactiva» la hizo el árbitro.** La afirmación resultó cierta (dos notas en el repositorio, ambas cubiertas), pero el artefacto no enumera el conjunto. Bajo carga de la prueba estricta, una afirmación de agotamiento sin enumeración es del mismo tipo lógico que la que V-006 reprocha a §4.2(ii). Hoy no falla; no está blindada.

**O-004 — Orden físico de las secciones.** La §6 se insertó **antes** de la §5 en el fichero. Sin efecto normativo; se registra porque la plantilla ADR-0000 fija cinco preguntas en orden y un lector puede dar por terminado el ADR en §6.

**O-005 — Metadato desactualizado.** `ESTADO.md` conserva en su cabecera «Última actualización: **2026-07-16**» mientras su contenido fue modificado el 07-18 (commit `39d62fa`). Sobre el documento que el principio 12 designa única fuente de verdad.

```
────────────
```

## Respuesta a la pregunta única del encargo

**¿La v2 responde a CADA violación y contradicción del dictamen previo?** **No.** Responde a cuatro de diez puntos; dos de esas cuatro quedan pendientes de un acto del IP que aún no ocurre.

| Punto | Estado tras v2 |
|---|---|
| V-001 enmienda constitucional | Propuesta redactada; Constitución sin tocar → **subsiste** |
| V-002 condición (i) consumida | Cura declarativa ejecutada y verificada; falta ratificación → **subsiste mitigada** |
| V-003 inventario de actos 07-06→07-17 | **Sin respuesta** |
| V-004 ficha | **Levantada** |
| V-005 nota de exp-005 + §4.3 | **Levantada** |
| V-006 «experimentos pendientes» | **Sin respuesta** |
| C-001 | Elevada, con cauce propuesto |
| C-002 / C-003 / C-004 | **No elevadas** |
| Nuevas | V-101, V-102, V-103; C-005, C-006 |

Lo que sí está bien hecho y se acredita sin reservas: la ficha quedó al día con filas append-only y estatus visible; la segunda nota de exp-005 fue cubierta con el mismo tratamiento y su veredicto mecánico está intacto; §4.3 retiró una afirmación falsa reconociéndola como tal en lugar de borrarla, y cerró el hueco de las «lentes de juicio»; los tres registros dicen ahora «sujeta a ratificación». Eso es remediación real y verificable.

## Condición de levantamiento (actualizada)

1. **V-003** — Inventario fechado **dentro del ADR** de exp-005, exp-006, exp-007, aprobación de Fase A 6/6 del 07-14 y re-corte de Fase B del 07-16, con pronunciamiento expreso sobre la validez de cada uno.
2. **V-006** — Enumeración cerrada de los «experimentos pendientes» de §4.2(ii) con horizonte temporal, de modo que la cláusula pueda declararse satisfecha y no solo violada.
3. **V-103 / C-002, C-003, C-004** — Elevación nominal de las tres al IP, identificadas, dentro del ADR.
4. **V-101** — Mapa explícito V-00X → punto de §6, incluyendo los puntos que se declaran deliberadamente no remediados.
5. **V-102** — Corrección del literal «remediación completa» / «6 violaciones remediadas» en `ESTADO.md`, `CHANGELOG.md` y ficha, al alcance verificable.
6. **V-001 y V-002** — Ratificación del IP fechada, con incorporación efectiva del texto de §6.4 a `CONSTITUCION.md` en ese mismo acto. **No dependen del redactor y no pueden levantarse en sede arbitral.**
7. **C-005 y C-006** — Reportadas. Su resolución es del IP por ADR; basta que consten.

**Alcance de lo que este dictamen NO dice.** No juzga si el override es defendible, si el criterio de exp-004 estaba mal especificado, si H-001 tiene edge, ni si la enmienda constitucional propuesta es buena norma. Nada de eso es competencia de A-04; lo ratifica o lo rechaza el IP, que es compuerta separada. Este dictamen dice una sola cosa: **la remediación v2 es real en lo que toca, e incompleta respecto de lo que su propio encabezado declara cubrir.**

```
────────────
Firma: A-04 · 2026-07-18 · sesión independiente · re-arbitraje
```
