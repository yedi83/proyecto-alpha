# DICTAMEN A-04 — ADR-0006

```
DICTAMEN A-04
Artefacto evaluado: docs/ADR/ADR-0006-override-veredicto-exp004.md
                    (Estado: "Propuesta", fecha 2026-07-17; formaliza decisión de facto del 2026-07-06)
Estado: ☐ CONFORME   ☒ NO CONFORME
────────────
```

## Dieta de insumos (declaración obligatoria)

Se ordenó modo VALIDADOR ESTRICTO. Su dieta declarada es «prompt A-04 + ORQUESTADOR.md + el documento de fase a arbitrar». El artefacto **no es un documento de fase del Banco**, es un ADR, y el modo estricto se declara obligatorio para dictámenes de fase del Banco. Se recibieron además CONSTITUCION.md, PROTOCOLO.md, exp-004/PREREG.md, RESULTADO.md y NOTA_2026-07-06. **Se declara y no se ignora**: sin las normas no hay arbitraje posible, y el prompt general de A-04 exige explícitamente «los documentos normativos que apliquen». Se aplica la dieta del modo general con las **prohibiciones y la plantilla del modo estricto**.

Insumos adicionales consultados, todos **nombrados por el propio artefacto** en §4.1 y §4.2 (verificar una consecuencia impuesta exige abrir el registro donde se impone): `docs/INVESTIGACION/hipotesis/H-001-canal-donchian.md`, `docs/INVESTIGACION/REGISTRO_HIPOTESIS.md`, `docs/ESTADO.md`, `CHANGELOG.md`, `experiments/exp-008/PREREG.md`. Se consultaron también `exp-005/`, `exp-006/`, `exp-007/` para determinar el estado del universo de disparos al que §4.2 se refiere.

**Corrección al encargo.** El solicitante preseleccionó los principios aplicables (4, 14, 15, 16). La selección de norma aplicable es acto de arbitraje y no la fija el solicitante: se leyó la CONSTITUCION íntegra. Los principios decisivos en este dictamen resultaron ser el **preámbulo** y el **12**, no preseleccionados.

## Requisitos verificados

**Sobre el ADR como decisión metodológica (Constitución 11 y 15, ADR-0000)**

- ✔ **R1.** Las cinco preguntas de la plantilla están presentes (§1–§5). Verificado contra `ADR-0000-plantilla.md`.
- ✔ **R2.** Quinta pregunta obligatoria (condición observable de revisión) presente y específica: §5, «el disparo de cualquiera de las condiciones de §4.2 → retiro operativo automático».
- ✔ **R3.** Alternativas reales evaluadas, más de una, con contras declarados: §2 (a)(b)(c).
- ✔ **R4.** Alcance y estado declarados en cabecera.

**Sobre el reconocimiento de la violación original (pregunta (a))**

- ✔ **R5.** El veredicto mecánico permanece íntegro en `RESULTADO.md`: verificado, línea 19 conserva «**H-001 MATADA (edge no robusto al lookback)**» sin edición. No hay reescritura de historia en el registro del experimento.
- ✔ **R6.** El ADR nombra el canal como ilegítimo sin eufemismo: §1, «un canal que la Constitución no reconoce para revertir un umbral pre-escrito».
- ✘ **R7.** El ADR **no enumera los actos ejecutados bajo el veredicto anulado** entre 2026-07-06 y 2026-07-17 ni se pronuncia sobre su validez. §1 dice solo «continuó H-001 hacia Fase B/C». Ocurrieron al menos: exp-005, exp-006 y exp-007 (corridos 07-06→07-07); **Fase A APROBADA 6/6 el 07-14**; **re-corte de Fase B sellado el 07-16**. Ver V-003.
- ✘ **R8.** El ADR **no menciona el segundo uso del mismo canal**: `exp-005/NOTA_2026-07-06_interpretacion.md`, de la misma fecha, declara su criterio pre-escrito «inadecuado» y sustituye la lente de juicio (alpha → Sharpe) tras ver resultados. Ver V-005.

**Sobre las condiciones impuestas (pregunta (b))**

- ✔ **R9.** Condición §4.2(i) — «exp-008 (funding real) en nivel R0» — es verificable: umbral numérico pre-escrito (NET ≥ +10% y Sharpe ≥ 0.30), experimento ejecutado, resultado registrado.
- ✘ **R10.** Condición §4.2(ii) — «ningún nuevo disparo letal en **experimentos pendientes**» — **no es verificable**: el conjunto «experimentos pendientes» no está enumerado y la cláusula no tiene horizonte temporal. Una condición sobre un universo abierto y sin plazo puede falsarse pero nunca confirmarse. Carga de la prueba del artefacto → NO CONFORME. Ver V-006.
- ✘ **R11.** Ámbito temporal de la cláusula del segundo disparo **indeterminado**: no se declara si alcanza a los experimentos ya corridos entre el disparo y el ADR (exp-005 cerró con **BANDERA**, no letal, pero el ADR no fija la regla de cómputo). Ver O-002.
- ✘ **R12.** Consecuencia §4.1 — degradación de estatus **«en todos los registros (ficha, REGISTRO, ESTADO)»** — **incumplida en uno de los tres**. Ver V-004.

**Sobre autoridad y separación de funciones (Constitución 14, checklist A-04 §7)**

- ✘ **R13.** El ADR está en estado **«Propuesta — requiere arbitraje A-04 en sesión separada + ratificación del IP»** y sus efectos **ya fueron ejecutados y consumidos** antes de este dictamen y antes de la ratificación. Ver V-002.
- ✘ **R14.** El artefacto contradice el principio 4 sin activar el mecanismo que el **preámbulo** de la Constitución exige para contradecirlo. Ver V-001.
- ✔ **R15.** Separación de funciones respetada en el diseño del acto: el ADR se somete a arbitraje en sesión separada y reserva la resolución al IP. No hay invasión de rol por parte del árbitro ni del generador.
- ✔ **R16.** No hubo re-optimización: 512 se mantiene en todos los artefactos posteriores (verificado en exp-005, exp-008 y ficha). El compromiso anti-optimización del PREREG de exp-004 se cumplió.

```
────────────
```

## Violaciones

**V-001 — Excepción a un principio constitucional sin modificar la Constitución, y ejercida a posteriori.**

- Norma, textual (CONSTITUCION.md, preámbulo): «Estos principios son innegociables. **Cualquier decisión que los contradiga requiere modificar primero este documento mediante un ADR.**»
- Norma, textual (principio 4): «Los criterios de decisión se escriben antes de ver los resultados… **Un criterio escrito después del resultado no es un criterio: es una excusa.**»
- Hecho: ADR-0006 decide no acatar un umbral pre-escrito que disparó. Esa decisión contradice el principio 4. El preámbulo admite exactamente una vía: **modificar primero la Constitución** mediante ADR. ADR-0006 **no modifica ni una línea de CONSTITUCION.md** —no introduce una cláusula de excepción, no enmienda el principio 4, no altera el preámbulo— y actúa **once días después** del hecho, no «primero».
- Evidencia: `CONSTITUCION.md` sin modificación posterior al 2026-07-10 (últimos añadidos: principios 14, 15, 16); ADR-0006 §1 fechado 2026-07-17 sobre hecho del 2026-07-06; ADR-0006 no contiene sección de enmienda constitucional.
- Nota exigida por la regla de conducta: **el laboratorio puede tener razón en el fondo y aun así haber violado su método.** Que el criterio de exp-004 estuviera mal especificado no está en disputa aquí y no es competencia de este árbitro; el defecto es que la excepción se concedió por un instrumento que la propia norma no habilita para concederla.

**V-002 — Efectos consumados por un ADR en estado «Propuesta», antes de su arbitraje y ratificación.**

- Norma, textual (ADR-0006, cabecera): «**Estado:** Propuesta — **requiere arbitraje A-04 en sesión separada + ratificación del IP**».
- Norma, textual (checklist A-04 §7 — Autoridad): «¿alguien (humano o agente) ejerció una autoridad que los documentos no le otorgan? (…adopción de un cambio sin el ADR/enmienda que su norma exige)».
- Hecho: siendo aún propuesta no arbitrada, el ADR fue tratado como norma vigente y **una de sus dos condiciones fue declarada CUMPLIDA el mismo día 2026-07-17**.
- Evidencia:
  - `exp-008/PREREG.md`, §«Contexto de acumulación (**ADR-0006 — vinculante**)»: un ADR en propuesta se declara vinculante en el pre-registro de otro experimento.
  - `REGISTRO_HIPOTESIS.md`: «La condición (i) del ADR-0006 queda **CUMPLIDA** → Fase C vuelve a depender del veredicto de Fase B».
  - `ESTADO.md`: «**exp-008 CUMPLIDO EN R0 (07-17)** … Fase C vuelve a depender solo del veredicto de Fase B».
  - `CHANGELOG.md` 2026-07-17: «Pendiente: arbitraje A-04 en sesión separada + ratificación del IP» — el propio registro reconoce que el arbitraje estaba pendiente **mientras** las consecuencias ya se aplicaban.
  - `git log`: `05c3b8d` (ADR-0006 + PREREG exp-008 en el mismo commit) → `3b74d91` (exp-008 R0, condición cumplida).
- Consecuencia registrada: la condición (i) fue **impuesta y consumida dentro de la misma jornada**, con el experimento que la satisface pre-registrado el mismo día por el mismo proceso que redactó la condición. El requisito no operó como compuerta prospectiva.

**V-003 — Reconocimiento incompleto: no se declaran los actos ejecutados bajo el veredicto anulado.**

- Norma, textual (PROTOCOLO.md §Ciclo de vida): «reprobación en cualquier punto → **RECHAZADA (se documenta y se conserva)**».
- Norma, textual (CONSTITUCION principio 14): «el Registro conserva el historial **íntegro** (versionado, append-only)».
- Hecho: entre el disparo (07-06) y el ADR (07-17), H-001 estaba formalmente MATADA y el laboratorio ejecutó actos que presuponen lo contrario. El ADR los resume como «continuó H-001 hacia Fase B/C» sin enumerarlos ni pronunciarse sobre su validez.
- Evidencia: exp-005 / exp-006 / exp-007 con veredictos propios fechados 07-06→07-07; `REGISTRO_HIPOTESIS.md`: «Fase A APROBADA (07-14)»; `fase_B/ACTA_RECORTE_2026-07-16.md` (re-corte sellado 07-16, «reloj de 1 mes reiniciado»).
- Por qué cuenta: el ADR afirma en §3 que «no se reescribe historia». Es cierto respecto de `RESULTADO.md`. **No es completo** respecto del período de vigencia del veredicto: una formalización retroactiva que no inventaría los actos que ampara deja sin estatus decidido a una aprobación de fase (Fase A, 6/6) obtenida mientras la hipótesis estaba muerta.

**V-004 — Consecuencia §4.1 incumplida en la ficha.**

- Norma, textual (ADR-0006 §4.1): «**Estatus oficial de H-001 degradado en todos los registros (ficha, REGISTRO, ESTADO)**: de "en validación" a "EN VALIDACIÓN — CUESTIONADA: sobrevivió por override (ADR-0006)…"».
- Hecho: dos de tres registros cumplen; **la ficha no**.
  - `REGISTRO_HIPOTESIS.md`: ✔ «⏳ EN VALIDACIÓN — **CUESTIONADA (ADR-0006)**».
  - `ESTADO.md`: ✔ «**Estatus epistemológico: CUESTIONADA (ADR-0006, 07-17)**».
  - `docs/INVESTIGACION/hipotesis/H-001-canal-donchian.md`: ✘ campo Estado = «⏳ EN VALIDACIÓN — **Fase A iniciada 2026-07-02**»; «Última actualización de ficha: **2026-07-02**»; el «Registro de eventos» termina el 2026-07-02 y **no contiene fila alguna** para el disparo letal de exp-004 (07-06), ni para la nota interpretativa, ni para el ADR-0006.
- Evidencia adicional: mtime del fichero de ficha anterior al ADR; `grep -i "CUESTIONADA|ADR-0006|exp-004|MATA"` sobre la ficha → **cero coincidencias**.
- Efecto: el documento de cabecera de la hipótesis sigue presentando a H-001 sin el disparo letal ni el override. Para un lector que entre por la ficha —la fuente que el propio ADR nombra primero— el evento no existe.

**V-005 — El precedente de §4.3 deja fuera un artefacto vivo del mismo canal.**

- Norma, textual (ADR-0006 §4.3): «las notas interpretativas NUNCA anulan umbrales. El único canal es ADR + arbitraje A-04 + degradación de estatus + condiciones falsables. **Este ADR es la única vía retroactiva admitida y no se repite.**»
- Hecho: existe una **segunda** nota interpretativa de la misma fecha, `exp-005/NOTA_2026-07-06_interpretacion.md`, que declara su propio criterio pre-escrito inadecuado y sustituye la métrica de juicio **después** de ver resultados: «El criterio "HYPE con alpha > 0" es **inadecuado** para esta prueba… **La lente correcta es el Sharpe, no el alpha.** (Segundo criterio mío que salió mal en la sesión…)». El ADR no la menciona, no la anula, no la ampara y no la excluye.
- Norma que activa (checklist A-04 §1): «¿La versión que se aplicó es la registrada, **sin reinterpretación**?»
- Por qué cuenta pese a no ser letal: §4.3 se enuncia como cierre general del canal («no se repite»), y al cerrarlo declara resuelto un caso —el de exp-004— dejando en pie otro del mismo canal y la misma fecha, no arbitrado. La afirmación «única vía retroactiva admitida» es, a fecha de este dictamen, **fácticamente falsa dentro del propio repositorio**.

**V-006 — §4.2(ii) no es falsable en el sentido que el ADR reclama.**

- Norma, textual (ADR-0006 §4.2): «(ii) ningún nuevo disparo letal en **experimentos pendientes**… **esta cláusula es el compromiso falsable de este ADR**».
- Norma, textual (CONSTITUCION principio 15): «Las decisiones, como las hipótesis, **deben ser falsables**.»
- Hecho: «experimentos pendientes» no se enumera en ninguna parte del ADR ni en documento enlazado, y no se fija plazo. La cláusula es asimétrica: puede dispararse en contra de H-001 en cualquier momento futuro, pero **nunca puede declararse satisfecha**, porque el conjunto no está cerrado. La condición (i), en cambio, sí está cerrada y sí se declaró cumplida.
- Efecto verificado: al cumplirse (i), los registros ya escriben «Fase C vuelve a depender **solo** del veredicto de Fase B + cero disparos letales nuevos». Una compuerta cuyo lado abierto se cierra en un día y cuyo lado cerrado no puede cerrarse nunca no es una condición verificable: es una cláusula de un solo sentido.
- Carga de la prueba: el artefacto no aporta la enumeración → el requisito se dicta **no verificable** y cuenta contra la conformidad.

```
────────────
```

## Contradicciones detectadas (se reportan, JAMÁS se resuelven)

**C-001 — Preámbulo constitucional vs. mecanismo empleado.** El preámbulo exige «modificar **primero** este documento mediante un ADR» para cualquier decisión que contradiga un principio. El principio 15 y ADR-0000 describen el ADR como instrumento para «excepciones concedidas» sin exigir enmienda constitucional. Un texto exige modificar la Constitución; el otro admite conceder la excepción por ADR simple. **El ADR-0006 opera bajo la segunda lectura sin declarar que la primera existe ni que las dos chocan.** Resolución: del IP, por ADR. No es de este árbitro.

**C-002 — Principio 12 vs. ADR §4.1.** Principio 12, textual: «**Una sola fuente de verdad por tema.** El estado vive en `ESTADO.md`… **La duplicación de información es un bug documental.**» §4.1 ordena escribir la misma cadena de estatus en **tres** documentos (ficha, REGISTRO, ESTADO). El ADR consagra la duplicación que el principio 12 tipifica como bug. **V-004 es precisamente el fallo que el principio 12 predice**: tres copias, una se desincroniza. No reportada por el artefacto.

**C-003 — Estados del PROTOCOLO vs. estatus creado.** PROTOCOLO.md enumera los estados posibles: «`EN VALIDACIÓN` · `VALIDADA` · `RECHAZADA` · `EN PRODUCCIÓN` · `RETIRADA`». ADR-0006 §4.1 crea y aplica **«EN VALIDACIÓN — CUESTIONADA»**, estado no previsto, sin enmendar PROTOCOLO.md. No reportada por el artefacto.

**C-004 — Regla de versionado vs. continuidad de H-001.** PROTOCOLO.md, anti-autoengaño §5, textual: «los protocolos e hipótesis **nunca se sobrescriben ni se editan tras un veredicto — se VERSIONAN**. Nomenclatura: `H-XXX.v1` (**rechazada**) → `H-XXX.v2` (modificada, nuevo pre-registro…). **Una versión nueva repite el pipeline completo desde el inicio.**» Y §Ciclo de vida: «reprobación en cualquier punto → RECHAZADA». Bajo esas dos reglas, el MATA del 07-06 producía H-001.v1 RECHAZADA y obligaba a H-001.v2 con pipeline completo. ADR-0006 mantiene la continuidad de v1 y reserva «H-001.v2» únicamente para el **segundo** disparo (§4.2). El artefacto **no reporta** que su decisión colisiona con la regla de versionado.

```
────────────
```

## Observaciones

**O-001 — Endurecimiento del umbral letal del experimento que servía de condición.** `exp-008/PREREG.md` declara: «umbrales ratificados por el IP en sesión (…el nivel letal **endurecido a petición suya**: "matar exige evidencia clara, no un borde")». Los umbrales se fijaron **antes** del dato, por lo que el principio 4 se cumple **formalmente** y esto **no es violación**. Se registra porque el mismo ADR designa la cláusula del segundo disparo como su «compromiso falsable», y el nivel letal del único experimento capaz de activarla se endureció en la misma jornada en que se redactó el compromiso. La verificación literal pasa; la consecuencia sobre la fuerza del compromiso queda para el IP, que es compuerta separada.

**O-002 — Regla de cómputo del «segundo disparo» sin definir.** No se declara si el cómputo alcanza a experimentos ya corridos (exp-005 cerró con **BANDERA**, no letal; exp-006 y exp-007 con SOBREVIVE y PROTEGE). Con los datos actuales ningún artefacto previo activa la cláusula, pero la regla queda indeterminada para el futuro.

**O-003 — Divergencia de literal en el estatus.** §4.1 prescribe una cadena de estatus concreta que incluye «alfa no significativa (t=0.94); edge no distinguible de suerte con datos actuales». `REGISTRO_HIPOTESIS.md` y `ESTADO.md` la abrevian a «CUESTIONADA (ADR-0006)», con los elementos completos desplazados a la columna de notas. Verificación literal: los elementos **existen** en ambos documentos. No llega a violación.

**O-004 — Sobre la formulación del encargo.** El encargo describía el hecho como «una nota interpretativa lo anuló 11 días antes de que existiera este ADR». Contrastado con los artefactos: la nota **no anula** `RESULTADO.md` —lo declara intocado y así está—; lo que hizo fue **operar** el laboratorio como si el veredicto no obligara. La distinción importa para el registro: no hubo edición destructiva (principio 14 intacto en ese punto); hubo inobservancia de un veredicto vigente durante once días. El artefacto lo formula correctamente en §1; el encargo, no.

```
────────────
```

## Respuesta a las cuatro preguntas del encargo

- **(a) ¿Reconoce íntegramente la violación sin reescribir historia?** Reconoce el canal como ilegítimo y conserva el veredicto mecánico intacto — eso está bien hecho y se acredita (R5, R6). **No es íntegro**: no inventaría los actos ejecutados bajo el veredicto anulado, incluida una aprobación de fase (V-003), y omite el segundo uso del mismo canal (V-005).
- **(b) ¿Las condiciones de §4 son verificables y falsables?** La (i) sí, y ya se declaró cumplida — el mismo día que se impuso, con el ADR aún sin arbitrar (V-002). La (ii) **no**: universo abierto, sin plazo, imposible de declarar satisfecha (V-006). Y §4.1 impone una consecuencia que **no se ejecutó completa** (V-004).
- **(c) ¿El precedente de §4.3 cierra la puerta?** **La cierra en el texto y la deja abierta en los hechos.** Prohíbe que las notas anulen *umbrales*, dejando fuera la reinterpretación por nota de criterios *no letales* — que es exactamente lo que hace la nota de exp-005, viva, no arbitrada y no mencionada (V-005). Y la afirmación «única vía retroactiva admitida» es falsa dentro del propio repositorio a fecha de hoy.
- **(d) ¿Contradicciones sin reportar?** **Cuatro**: C-001, C-002, C-003, C-004. El artefacto no reporta ninguna. Son de resolución del IP por ADR; este árbitro no las resuelve.

## Condición de levantamiento

Para que este dictamen pase a CONFORME deben ocurrir **todas**:

1. **V-001** — Enmienda explícita de `CONSTITUCION.md` que habilite la excepción (o texto en ADR-0006 que declare qué norma le otorga la potestad de exceptuar el principio 4 sin enmienda). Sin esto, la excepción carece de fuente.
2. **V-002** — Ratificación del IP fechada, y declaración expresa sobre el estatus de la condición (i), consumida antes del arbitraje: se convalida o se re-verifica bajo el ADR ya ratificado.
3. **V-003** — Inventario fechado, dentro del ADR, de los actos ejecutados entre 2026-07-06 y 2026-07-17 (exp-005/006/007, aprobación de Fase A del 07-14, re-corte de Fase B del 07-16), con pronunciamiento sobre la validez de cada uno.
4. **V-004** — Ficha `H-001-canal-donchian.md` actualizada al literal de §4.1, con filas append-only en su «Registro de eventos» para: disparo letal de exp-004 (07-06), nota interpretativa (07-06), ADR-0006 (07-17).
5. **V-005** — Pronunciamiento expreso sobre `exp-005/NOTA_2026-07-06_interpretacion.md`: amparada por este ADR, anulada, o arbitrada aparte. Y ampliación del precedente para cubrir la reinterpretación de criterios no letales, o declaración expresa de que queda fuera.
6. **V-006** — Enumeración cerrada de los «experimentos pendientes» de §4.2(ii) con horizonte temporal, de modo que la condición pueda declararse satisfecha y no solo violada.
7. **C-001 a C-004** — Elevadas al IP para resolución por ADR. Basta que consten elevadas; su resolución no es requisito de este levantamiento.

**Alcance de lo que este dictamen NO dice.** No juzga si el criterio de exp-004 estaba bien o mal especificado, si H-001 tiene edge, si continuar fue acertado, ni si el override es defendible en el fondo. Ninguna de esas preguntas es competencia de A-04. Este dictamen dice una sola cosa: **la formalización, tal como está escrita y tal como se ejecutó, no cumple el método que este laboratorio se dio a sí mismo.**

```
────────────
Firma: A-04 · 2026-07-18 · sesión independiente
```
