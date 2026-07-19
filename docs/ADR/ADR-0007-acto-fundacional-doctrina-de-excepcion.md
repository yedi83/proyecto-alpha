# ADR-0007 — Acto fundacional: doctrina de excepción por criterio mal especificado, y su cláusula de cierre

- **Fecha:** 2026-07-18
- **Estado:** **Propuesta** — pendiente de dictamen A-04 en sesión independiente y de ratificación del Investigador Principal. **Ningún efecto de este ADR surte hasta que ambos ocurran, en ese orden.**
- **Alcance:** Metodología · Proceso · **Enmienda constitucional propuesta** (Parte III)
- **Reemplaza a:** ADR-0006 (RECHAZADO por el IP el 2026-07-18). El ADR-0006 y sus dos dictámenes se conservan íntegros como registro del intento fallido. **Este documento se redacta desde cero: no reutiliza su texto.**
- **Redacción:** sesión nueva, distinta de la que redactó el ADR-0006, por encargo del IP (`ADR-0007_ENCARGO.md`, 2026-07-18).

**Insumos leídos para redactar:** `ADR-0007_ENCARGO.md` · `ADR-0006_EXPEDIENTE_DELIBERACION.md` · `ADR-0006-override-veredicto-exp004.md` (solo como registro de qué falló) · `ADR-0006_DICTAMEN_A04.md` y `_v2.md` · `exp-004/` (PREREG, RESULTADO, NOTA) · `exp-005/` (PREREG, RESULTADO, NOTA) · `exp-006/`, `exp-007/`, `exp-008/` (PREREG, RESULTADO) · `CONSTITUCION.md` · `PROTOCOLO.md` · `ADR-0000-plantilla.md` · `H-001-canal-donchian.md` · `REGISTRO_HIPOTESIS.md` · `ESTADO.md` · `CHANGELOG.md` · `CRITERIOS_FASES.md` · `informe_cierre_faseA.md` · `ACTA_RECORTE_2026-07-16.md` · `PREREG_FASE_C_BORRADOR.md` · `AGENDA_VALIDACION_2026-07-06.md` · `git log`.

---

## 1. ¿Qué problema intentábamos resolver?

El 2026-07-06, un umbral pre-escrito disparó y el laboratorio siguió trabajando como si no hubiera disparado. Ese es el hecho central, y no admite adorno.

El criterio letal de `exp-004` (sensibilidad de lookback) establecía: si un vecino del parámetro 512 va a `net ≤ 0` o `alpha ≤ 0`, **H-001 MUERE**. El vecino 384 dio `net −8.59%` y `alpha −28.64%`. El script escribió **«H-001 MATADA (edge no robusto al lookback)»** en `exp-004/RESULTADO.md`, donde sigue intacto. El mismo día, una **nota interpretativa** argumentó que el patrón observado (monótono: 384 < 512 < 640) no era el patrón que el criterio fue diseñado para cazar (un pico aislado de sobreajuste), degradó H-001 a «prometedora pero no probada», y el trabajo continuó. Ese mismo día, una **segunda nota** en `exp-005` sustituyó la lente de juicio de otra prueba (alfa → Sharpe) después de ver los resultados.

Ninguna de las dos notas es un canal reconocido. El Protocolo y la Constitución conocen un solo camino para no acatar un umbral pre-escrito, y ese camino no se recorrió. Durante **once días** los registros oficiales del laboratorio (`ficha`, `REGISTRO_HIPOTESIS.md`, `ESTADO.md`) siguieron describiendo a H-001 como una hipótesis en validación normal, y sobre esa base se aprobó una fase, se inició otra, se corrieron cuatro experimentos y se redactó el borrador de criterios de Fase C.

El intento de legalizarlo (ADR-0006, 2026-07-17) recibió **dos dictámenes A-04 NO CONFORME** en 24 horas, con seis violaciones, tres violaciones nuevas en la remediación y seis contradicciones normativas detectadas. El IP lo rechazó y encargó este documento.

Hay que decidir ahora por dos razones. La primera: mientras el caso siga abierto, el estatus de H-001 es indeterminado y la Fase C no tiene base normativa aunque la Fase B apruebe (cierre previsto ~2026-08-16). La segunda, y la que importa: **este es el primer caso de su tipo y habrá más.** El laboratorio no tiene doctrina para el caso doble — cuando se sostiene que un criterio pre-escrito estaba mal especificado **y**, además, el procedimiento fue vulnerado. Sin doctrina, cada caso futuro se resolverá por la impresión del día, que es exactamente lo que este laboratorio existe para impedir.

---

## 2. ¿Qué alternativas se evaluaron?

**(a) Acatar el MATA de `exp-004` sin más.** H-001.v1 pasa a RECHAZADA; la Fase C no se abre; si la idea vuelve, vuelve como H-001.v2 con pre-registro nuevo y pipeline completo.

- *A favor:* precedente cristalino — los umbrales son leyes incluso cuando el instrumento probablemente se equivocó. Cero puerta trasera. Protege contra un hecho incómodo: la alfa de H-001 nunca fue significativa (t=0.94), así que no se pierde una certeza sino una posibilidad.
- *En contra:* deja al laboratorio **sin doctrina igualmente**. El caso siguiente llegará y encontrará el mismo vacío, con el agravante de un precedente que dice «los criterios mal escritos son irrevocables» — que empuja al investigador futuro a escribir criterios laxos por miedo, degradando el rigor que se quiere proteger. Y no resuelve nada del incumplimiento de procedimiento: matar la hipótesis no repara los once días.

**(b) Un ADR simple de override, sin tocar la Constitución.** Es lo que intentó el ADR-0006.

- *A favor:* barato y rápido.
- *En contra:* **ya se probó y falló dos veces.** El preámbulo constitucional es explícito: «Cualquier decisión que los contradiga requiere modificar **primero** este documento mediante un ADR». Un ADR que exceptúa el principio 4 sin enmendar la Constitución carece de fuente normativa (V-001, subsistente en ambos dictámenes). Repetirlo sería el tercer intento del mismo error.

**(c) Seguir deliberando.** Nada operativo depende de la decisión hasta el cierre de Fase B.

- *A favor:* sin coste inmediato; cada semana de `paper_real` añade evidencia forward.
- *En contra:* la pausa deliberada ya se tomó y ya cumplió su función (el IP no decidió el día de dos dictámenes en contra). Prolongarla convierte la prudencia en decisión por omisión, y deja el estatus de H-001 en limbo mientras la Fase B corre hacia su cierre.

**(d) Acto fundacional: enmienda constitucional que crea la doctrina, la aplica a este caso como su acto fundacional, y cierra la puerta detrás de sí.** — *elegida.*

- *A favor:* es la única que produce norma. Resuelve el caso concreto **y** deja al laboratorio con una regla para los siguientes, con la puerta de la retroactividad clausurada por la misma norma que la usa una vez.
- *En contra:* crea una puerta donde no había ninguna. Aunque la retroactividad quede clausurada, la anulación *prospectiva* de umbrales pasa a existir como figura jurídica, y cada disparo futuro tentará esa figura. H-001 cargará «CUESTIONADA + override» permanentemente. Y el coste de proceso es alto: tres arbitrajes, semanas de fricción, un ADR rechazado en el expediente. *(Ese coste alto es deliberado: es el disuasivo.)*
- *Riesgo declarado:* es también la opción **conveniente** — la única en la que todo sigue vivo. La conveniencia no la hace incorrecta, pero obliga a que la demostración de mala especificación se sostenga por sí sola, con independencia de que el resultado guste. El requisito 1 de la Parte III existe precisamente por eso.

---

## 3. ¿Por qué se eligió esta?

Tres razones, en orden de peso.

**La primera es que el problema del laboratorio no es H-001.** Fundamento de la decisión, textual del IP:

> *"Mi decisión no depende demasiado de H-001. Depende del laboratorio. Porque incluso si H-001 termina muriendo dentro de dos meses, el laboratorio habrá salido fortalecido. Y si sobrevive, también."*

Y, sobre por qué no bastaba con matar la hipótesis para demostrar dureza (textual del IP, 2026-07-18):

> *"Confiaría más en un laboratorio que fue capaz de reconocer públicamente un fallo de gobernanza, corregir su Constitución, imponer una excepción irrepetible y seguir adelante con reglas más fuertes, que en uno que simplemente mató una hipótesis para demostrar dureza o la salvó para demostrar pragmatismo."*

**La segunda es que el fondo nunca estuvo en disputa.** Ninguno de los dos dictámenes A-04 atacó el argumento de mala especificación — y no por descuido: A-04 declaró expresamente que el fondo no es su competencia. Lo que ambos dictámenes atacaron, con razón, fue el **instrumento** usado para conceder la excepción y la **secuencia** en que se ejecutó. Un ADR que corrige instrumento y secuencia ataca lo que efectivamente estaba mal.

**La tercera es que una excepción sin norma es un privilegio, y una norma sin cláusula de cierre es una puerta.** Por eso la decisión tiene dos mitades inseparables: se crea el mecanismo (Parte III) **y** se clausura su versión retroactiva en el mismo acto (Parte IV). Sin la segunda mitad, el razonamiento del IP es directo: cada experimento fallido tentará el «el criterio estaba mal diseñado», y el laboratorio morirá lentamente por erosión de sus propios umbrales. Con ella, el precedente queda cerrado en vez de abierto.

**Evidencia disponible al decidir:** el veredicto mecánico de `exp-004` intacto; el texto del propio PREREG de `exp-004` declarando qué patrón buscaba distinguir; los resultados de `exp-005` (BANDERA, no letal), `exp-006` (SOBREVIVE), `exp-007` (PROTEGE) y `exp-008` (R0); la Fase A aprobada 6/6 con replay 36/36; los dos dictámenes A-04; y la alfa no significativa de H-001 (t=0.94), que sigue siendo el hecho que más pesa sobre el valor real de todo esto.

---

## 4. ¿Qué consecuencias aceptamos?

> Las cuatro partes siguientes son la parte dispositiva de este ADR, en los términos del mandato del IP. Ninguna surte efecto antes de la secuencia de §4.7.
>
> **Convención de lectura — qué texto crea norma y qué texto la aplica.** Solo el bloque citado de la **Parte III** (el principio 17, con sus requisitos y su disposición transitoria) es **texto normativo**: es lo que se incorpora literalmente a `CONSTITUCION.md` al ratificar. **Todo lo demás de este ADR** —Partes I, II y IV, §4.5, §4.5.1, §4.6, §4.7bis, anexos y motivación— es **texto de aplicación o de motivos**: resuelve *este* expediente, no crea regla general, y no se incorpora a la Constitución. **En caso de discrepancia entre ambos niveles prevalece el texto de la Parte III**, y la formulación divergente del texto de aplicación se tiene por no puesta.

### PARTE I — Reconocimiento expreso

**El laboratorio incumplió su propio protocolo entre el 6 y el 17 de julio de 2026.** Sin matices, sin atenuantes y sin contexto que lo suavice.

Lo que se reconoce, con nombre:

1. Un veredicto letal producido por un umbral pre-escrito **no fue acatado** desde el instante en que se produjo (2026-07-06).
2. La anulación se ejerció por un canal — la nota interpretativa — que **ninguna norma del laboratorio reconoce** para ese efecto. Dos veces el mismo día (`exp-004` y `exp-005`).
3. Durante once días, los registros oficiales describieron a H-001 en un estado que **no le correspondía** bajo su propia regla.
4. El primer intento de formalización (ADR-0006) **invirtió la secuencia**: consumió efectos antes del arbitraje y antes de la ratificación, y declaró cumplida una de sus condiciones el mismo día en que la impuso.
5. En la remediación de ese ADR, el redactor declaró **tres veces en 48 horas** una completitud que no existía, siempre en la dirección que le favorecía. Consta en el expediente y en el `CHANGELOG`. Este ADR no repite esa figura: **no declara su propia conformidad ni su propia completitud** (§4.8).

Nada de lo anterior queda excusado por el hecho de que el argumento de fondo pueda ser correcto. **El laboratorio puede tener razón en el fondo y aun así haber violado su método**, y ese es exactamente el caso.

#### 4.1 — Inventario de actos ejecutados entre 2026-07-06 y 2026-07-17

Todos estos actos se ejecutaron mientras el veredicto letal de `exp-004` estaba vigente y no acatado. Se enumeran con fecha y con pronunciamiento expreso sobre su validez. *(El alcance de este inventario lo verifica A-04; si falta un acto, su ausencia es un defecto de este ADR y así debe dictarse.)*

| # | Fecha (UTC) | Acto | Pronunciamiento propuesto |
|---|---|---|---|
| 1 | 2026-07-06 | `exp-004/NOTA_2026-07-06_interpretacion.md` — sostiene la continuación de H-001 pese al disparo | **NULA de efectos normativos** (Parte II). Su contenido analítico se conserva como contexto técnico y es el insumo de la demostración de §4.5, que se somete al canal formal |
| 2 | 2026-07-06 | `exp-005/NOTA_2026-07-06_interpretacion.md` — declara inadecuado su propio criterio pre-escrito y sustituye la lente alfa→Sharpe tras ver resultados | **NULA de efectos normativos** (Parte II). Su contenido analítico se conserva como contexto técnico. No relajó ninguna consecuencia práctica (concluye «no probada, baja convicción»), lo que atenúa el daño y **no** legitima el canal |
| 3 | 2026-07-06 | `AGENDA_VALIDACION_2026-07-06.md` — plan de pruebas P1–P4 | **Válido como documento de trabajo, sin efecto normativo.** Su diagnóstico («baja convicción, no probada, no refutada») no depende del override |
| 4 | 2026-07-06 | `exp-006/PREREG.md` sellado (OOS por tiempo, régimen 2020) | **Válido.** Pre-registro sellado antes de datos; su validez experimental no depende del estatus de H-001 |
| 5 | 2026-07-07 03:37 | `exp-005` ejecutado — veredicto **BANDERA** (HYPE `net≤0` o `alpha≤0`), no letal | **Válido experimentalmente.** Veredicto mecánico intacto en su `RESULTADO.md`. *Discrepancia documental que se eleva sin resolver: la nota del acto 2 lleva fecha 07-06 y el `RESULTADO` timestamp 07-07 03:37 UTC; el orden real de redacción no es determinable desde el repositorio* |
| 6 | 2026-07-07 15:38 | `exp-006` ejecutado — veredicto **SOBREVIVE** (mantiene firma de seguro; DD −10.2% vs −69.9% del B&H) | **Válido experimentalmente.** No letal |
| 7 | 2026-07-07 18:47 | `exp-007` pre-registrado y ejecutado — veredicto **PROTEGE** (crash covid aislado) | **Válido experimentalmente.** No letal |
| 8 | ~2026-07-07 | `paper_real` arrancado con PREREG propio (forward sobre precios reales de mainnet, sin keys, cero órdenes) | **Válido como testigo.** Declarado NO-evidencia de Fases A/B por su propio PREREG. Erratum pendiente del IP (declara riesgo 0.1% uniforme; el código corre BTC 0.125%) — se mantiene pendiente, este ADR no lo resuelve |
| 9 | 2026-07-08 08:45 | Salida del trade #7 (LONG BCH) registrada — verificación clave del acta de inicio de Fase A | **Válido como evidencia de instrumentación** |
| 10 | 2026-07-09 | Causa raíz de velas atrasadas diagnosticada y cerrada | **Válido.** Acto de ingeniería, ajeno al estatus de la hipótesis |
| 11 | 2026-07-10 | Constitución ampliada (principios **14, 15, 16**), `PROTOCOLO §5` versionado científico, creación de **A-04**, ADR-0003 y ADR-0004, Banco de Mecanismos, `TEORIA.md` v0.1 | **Válidos.** Se hace constar un hecho relevante para juzgar este caso: **buena parte de las normas bajo las que hoy se juzga el disparo del 07-06 se escribieron el 07-10, cuatro días después.** No excusa nada — el principio 4 y el Protocolo ya existían el 07-06 y son los infringidos — pero es parte honesta del expediente |
| 12 | 2026-07-11 | Outage de feed (20 NetworkError, 03:45–06:00) recuperado automáticamente | **Válido.** Registrado como resiliencia según especificación |
| 13 | 2026-07-14 12:39 | **Fase A CERRADA — APRUEBA 6/6**, replay 36/36 sin divergencias, informe sellado, decisión registrada en `CRITERIOS_FASES.md` | **Evidencia íntegra y conservada; efecto de compuerta SUSPENDIDO.** El contenido probatorio (fidelidad bot↔modelo) es un hecho verificable que no depende del estatus de la hipótesis. Pero una aprobación de fase es un **paso del pipeline de una hipótesis**, y se obtuvo mientras esa hipótesis estaba formalmente muerta. **Su valor como compuerta superada del pipeline de H-001 queda suspendido y solo se convalida con la ratificación de este ADR.** Si el IP no ratifica, la Fase A se conserva como validación de plataforma, no como etapa aprobada de H-001 |
| 14 | 2026-07-14 15:13:16 | **Fase B iniciada** (corte), ENMIENDA 1 sellada en el PREREG, bot de frontera aplicado, acta de inicio sellada | **Efecto suspendido, igual que el acto 13.** Además quedó materialmente anulado por el acto 16 |
| 15 | 2026-07-14→15 | **Incidente de contaminación:** dos bots (oficial y ensayo) operando la misma cuenta demo con API keys idénticas → desincronización bot↔exchange | **Reconocido como incidente.** Es criterio de aborto del PREREG y fue gestionado como tal. No es acto de gobernanza: es fallo operativo, y se inventaría porque ocurrió dentro del período |
| 16 | 2026-07-16 15:27:33 | **Re-corte de Fase B:** datos 07-14→16 **anulados**, keys del ensayo neutralizadas, máquina esterilizada, reloj de un mes reiniciado. Acta sellada | **Válido y correcto en su mérito** (el laboratorio anuló su propia evidencia contaminada en vez de conservarla). **Efecto de compuerta suspendido** en los mismos términos que el acto 13 |
| 17 | 2026-07-16 | `PREREG_FASE_C_BORRADOR.md` redactado con decisiones del IP ($750; suspensión y revisión a −27%; kill blando + disyuntor técnico; stop por vela cerrada). `RISK_POLICY.md` y `SECURITY.md` actualizados | **Válido como borrador. SIN SELLAR y sin efecto.** Su sello exige Fase B aprobada; y, por este ADR, también la ratificación (§4.6) |
| 18 | 2026-07-17 | **ADR-0006 redactado** (Propuesta): estatus degradado a CUESTIONADA en los registros; Fase C condicionada | **RECHAZADO por el IP el 2026-07-18.** Sin efecto alguno. Se conserva íntegro como registro histórico |
| 19 | 2026-07-17 | `exp-008/PREREG.md` sellado (funding real, intento único, umbrales R0/R1/R2 ratificados por el IP, letal endurecido a petición suya) | **Válido.** Umbrales fijados antes del dato. *Se hace constar el residuo señalado por A-04 (O-002 del primer dictamen): su §«Contexto de acumulación» declara vinculante un ADR entonces en propuesta y hoy rechazado. El pre-registro está sellado y **no se edita**; §4.6 dispone el erratum fechado adjunto* |
| 20 | 2026-07-17 | Dictamen **A-02 APTO** sobre el dataset de funding (hashes SHA-256 congelados) | **Válido.** Compuerta de datos cumplida en su propio canal |
| 21 | 2026-07-17 17:00 | **`exp-008` ejecutado — veredicto R0 ACEPTABLE** (FULL: NET 27.26% vs 24.03%; Sharpe 0.47; 2426: +4.63%). Paridad OK | **Válido experimentalmente** (pre-registro sellado, dataset APTO, umbrales intactos, paridad verificada). **Su efecto normativo sobre la Fase C queda suspendido** y se re-declara en §4.5 bajo este ADR, con fecha de ratificación y no del 07-17 |
| 22 | 2026-07-17→18 | `TEORIA.md` v0.2 y su corrección de atribución causal (selección adversa, no carry); registros (`REGISTRO`, `ESTADO`, ficha) actualizados declarando la condición (i) cumplida | **La corrección de TEORIA es válida** (acto de honestidad intelectual, ajeno a este caso). **Las declaraciones de condición cumplida en los registros quedan sin efecto** y se re-escriben según §4.6 |

**Regla general del inventario.** Se distingue entre el **contenido probatorio** de un acto (un replay 36/36 es un hecho, y los hechos no se anulan por decreto) y su **efecto normativo dentro del pipeline de H-001** (una compuerta superada, una condición cumplida, un estatus). Lo primero se conserva íntegro. Lo segundo queda suspendido hasta la ratificación, y sin ratificación no revive.

---

### PARTE II — Declaración de nulidad

**Las notas interpretativas de `exp-004` y `exp-005`, ambas del 2026-07-06, nunca tuvieron efectos normativos.** No los pierden hoy: **no los tuvieron nunca**, porque el instrumento carecía de la potestad que se le atribuyó. Se declara, en consecuencia:

1. **Nulidad de origen.** Ninguna de las dos notas anuló, modificó, matizó, suspendió ni degradó veredicto alguno. Todo efecto que se les atribuyó entre el 2026-07-06 y hoy es inexistente.
2. **Los veredictos mecánicos rigen y permanecen intactos.** «H-001 MATADA (edge no robusto al lookback)» (`exp-004/RESULTADO.md`) y «BANDERA (HYPE net<=0 o alpha<=0)» (`exp-005/RESULTADO.md`) conservan su texto original y **no se editan jamás**. Este ADR no reescribe historia: escribe encima, fechado.
3. **Valor técnico conservado.** El contenido analítico de ambas notas se conserva como **contexto técnico y nada más**: material de análisis, insumo de deuda de instrumento, y — en el caso de `exp-004` — materia prima del argumento que este ADR somete al canal formal en §4.5. Un análisis puede ser correcto y aun así no ser una decisión. **Análisis conservable como contexto; jamás como decisión.**
4. **Alcance cerrado.** A fecha de redacción, el repositorio contiene exactamente dos notas interpretativas de este tipo, ambas del 2026-07-06 (`exp-004/` y `exp-005/`), y ambas quedan cubiertas por esta declaración. *La verificación de que no existe una tercera corresponde a A-04; este ADR no la da por hecha.*
5. **Regla permanente, desde hoy.** Ninguna nota, comentario, lectura, anexo ni documento no arbitrado altera un veredicto pre-escrito, **ni anulándolo, ni cambiando su lente de juicio, ni reinterpretando su alcance**. El único canal es el de la Parte III.

---

### PARTE III — Nueva doctrina: la Excepción de Criterio Mal Especificado

Se propone añadir a `CONSTITUCION.md` el **principio 17**, con el texto siguiente. La incorporación es parte del acto de ratificación y no antes (§4.7).

> **17. Excepción de Criterio Mal Especificado — única vía de anulación de un veredicto pre-escrito.**
>
> Un veredicto producido por un umbral pre-escrito es vinculante **desde el instante en que se produce**. Ninguna nota, comentario, lectura, anexo ni documento no arbitrado lo altera: **ni anulándolo, ni cambiando la lente de juicio con que se evalúa, ni reinterpretando su alcance**. Esta regla rige por igual para los veredictos letales y para los no letales. Solo puede anularse si concurren **todos** los requisitos siguientes; la ausencia de cualquiera de ellos hace la anulación inadmisible:
>
> **(1) Demostración de mala especificación.** Debe demostrarse que el criterio **no medía lo que su propio pre-registro declaraba medir**. La demostración se apoya en el texto del pre-registro y/o en evidencia **independiente del resultado que incomoda** — por ejemplo, que el mismo criterio también falla aplicado a casos favorables o neutrales. Un argumento cuya única prueba es el resultado que se quiere revertir no es una demostración: es una excusa (principio 4).
>
> **(2) Canal ADR.** La anulación se pide por ADR propio, que declara el disparo, la demostración, el inventario de actos afectados y las consecuencias que asume.
>
> **(3) Arbitraje A-04.** Dictamen **CONFORME** de A-04 en sesión independiente. A-04 juzga el cumplimiento del método, nunca la calidad de la demostración de fondo ni el mérito de la hipótesis.
>
> **(4) Ratificación del IP, fechada, ANTES de que la anulación surta efecto alguno.** Entre el disparo y la ratificación **rige el veredicto disparado**, con todas sus consecuencias. Ningún acto ejecutado en ese intervalo consolida derecho.
>
> **(5) Prohibición de re-optimización.** La anulación no autoriza cambiar el parámetro, la lente, la métrica ni el universo. Anular un veredicto mal producido no mejora la hipótesis: la devuelve al punto donde estaba, con el disparo registrado para siempre.
>
> **(6) Consecuencias mínimas obligatorias.** La hipótesis queda con estatus epistemológico **CUESTIONADA**, permanente y visible en su ficha; se registra la deuda de instrumento que causó el defecto; y se fija una **cláusula de segundo disparo** sobre un conjunto de pruebas **enumerado, cerrado y con horizonte temporal**, de modo que la condición pueda declararse **satisfecha** y no solo violada. Un segundo disparo letal proveniente de un instrumento independiente retira la hipótesis del camino operativo **sin excepción posible** y activa la regla de versionado. **Ese conjunto no se modifica por conveniencia:** añadir o retirar una prueba de la enumeración exige **ADR nuevo con dictamen A-04**, y ninguna prueba sin umbral letal pre-escrito puede incorporarse ni invocarse como disparo.
>
> **(7) Efecto sobre el versionado científico.** Cuando la anulación prospera, el disparo anulado **no cuenta como reprobación** a efectos de `PROTOCOLO §5`: no hubo veredicto válidamente producido que reprobara. El linaje conserva la anotación permanente del disparo y de la excepción. Si se produce el segundo disparo de (6), la regla de versionado se aplica íntegra y sin excepción: `H-XXX.v2`, pre-registro nuevo, pipeline completo.
>
> **(8) Límite expreso de alcance: este artículo no genera precedente automático.** Que una invocación anterior del requisito (7) —o de cualquier otro requisito de este artículo— haya prosperado **no es argumento en ningún expediente posterior**. Todo caso ulterior debe satisfacer **todos los requisitos de este artículo** por sí solo y demostrados de nuevo; la existencia de un caso anterior no acredita nada sobre el siguiente, no rebaja el estándar de la demostración de mala especificación, y no puede citarse como razón para conceder la excepción. Invocar «ya se concedió una vez» es, a los efectos de este artículo, no invocar nada. Este límite se escribe porque el requisito (7) es la disposición de mayor efecto práctico del artículo, y una disposición que concentra ese poder debe llevar su alcance acotado en su propio texto y no en la interpretación de quien la lea.
>
> **(9) Régimen de admisibilidad y de declaración.** (a) Un ADR que pretenda anular un veredicto **ya vigente en el momento de su redacción** es **inadmisible de plano**, y A-04 debe dictarlo NO CONFORME sin entrar en el fondo. (b) La petición debe iniciarse **antes de que se ejecute un solo acto que presuponga la anulación**: el día del disparo es el día del ADR. (c) El ADR que invoca este artículo **no declara su propia conformidad, completitud ni suficiencia**: la conformidad la dicta A-04 y la ratificación el IP. Toda declaración de completitud propia dentro de un ADR de excepción se tiene por no puesta y cuenta contra su conformidad.
>
> **El veredicto mecánico jamás se edita.** El `RESULTADO` del experimento conserva su texto original. La anulación vive en el ADR, nunca en el registro del experimento.
>
> **Disposición transitoria única — y última.** Este artículo **se aplica a sí mismo**. Se admite **un (1) solo caso anterior a su entrada en vigor**: el disparo de `exp-004` y la nota concurrente de `exp-005`, ambos del 2026-07-06, que son el caso que funda este artículo y que se admite **únicamente porque ocurrió cuando este artículo no existía**. Ese caso no pudo cumplir el requisito (4) en su momento. La admisión queda **condicionada** a que satisfaga los demás requisitos en su integridad —**lo que verifica A-04, no el propio ADR**— y a que cumpla el (4) hacia adelante, en el sentido de que **ningún efecto derivado de la anulación surte hasta la ratificación del ADR-0007**. Si el arbitraje no lo verifica, la transitoria no se activa y el veredicto disparado rige. **Agotado ese caso, esta disposición transitoria queda derogada por su propio cumplimiento.** Desde la ratificación del ADR-0007, **ninguna anulación retroactiva es admisible bajo ninguna circunstancia** — ni por este artículo, ni por ADR posterior que invoque este precedente. Un disparo cuya anulación no fue ratificada antes de surtir efectos es un **disparo firme**. **Esta disposición no puede reabrirse por ADR que la invoque, la interprete o la extienda:** reabrirla exige enmendar este artículo en su integridad, declarando por escrito y de forma expresa que se reintroduce la retroactividad — que es el acto que esta disposición existe para hacer imposible de cometer en silencio.

**Por qué el requisito (1) está redactado así.** Es la junta blanda de toda la doctrina: A-04 verifica procedimiento, no fondo, de modo que sin un estándar objetivo el requisito (1) se convertiría en «el IP cree que el criterio estaba mal». El estándar de **independencia del resultado** lo convierte en algo comprobable por un tercero: o el pre-registro dice por escrito qué patrón buscaba distinguir y el patrón observado es otro, o el mismo criterio falla sobre casos que no incomodan. Cualquier otra cosa es opinión.

---

### PARTE IV — Cláusula única e irrepetible

**Esta excepción retroactiva solo puede usarse porque ocurrió antes de que la doctrina existiera. Es el acto que la funda, y es el único acto retroactivo que este laboratorio admitirá jamás.**

**Después de este caso, la retroactividad no puede volver a existir. Nunca.**

**Nota de técnica normativa.** Los puntos siguientes **no crean regla nueva**: son la aplicación a este expediente de disposiciones que ya viven en el texto constitucional de la Parte III, y se enuncian aquí porque el mandato del IP exige que esta cláusula conste como parte dispositiva propia. Cada punto lleva su remisión. **Si alguno divergiera del texto de la Parte III, prevalece la Parte III.**

Concretamente, desde la ratificación de este ADR:

1. Todo disparo de un umbral pre-escrito **rige desde el instante en que se produce**, sin excepción y sin ventana de gracia. *(Aplicación del párrafo de encabezamiento y del requisito (4).)*
2. Toda petición de anulación debe iniciarse por el canal de la Parte III **antes de que se ejecute un solo acto que presuponga la anulación**. El día del disparo es el día del ADR. *(Aplicación del requisito (9)(b).)*
3. Un ADR que pretenda anular un veredicto ya vigente en el momento de su redacción es **inadmisible de plano**, y A-04 debe dictarlo NO CONFORME sin entrar en el fondo. *(Aplicación del requisito (9)(a).)*
4. **Este ADR-0007 no es precedente de retroactividad.** Invocarlo para justificar una anulación retroactiva futura es invocar una disposición derogada por su propio cumplimiento. *(Aplicación de la disposición transitoria; el requisito (8) extiende la misma prohibición a todo precedente, retroactivo o no.)*
5. La disposición transitoria **no puede reabrirse por ADR posterior**: exige enmendar el principio 17 en su integridad, declarándolo por escrito. *(Aplicación del párrafo final de la disposición transitoria.)*

**Razón del IP, textual:** sin esta cláusula, cada experimento fallido tentará el «el criterio estaba mal diseñado» y el laboratorio morirá lentamente; con ella, el precedente queda cerrado, no abierto.

---

### 4.5 — Adjudicación del caso de fondo bajo la nueva doctrina

Se resuelve el caso `exp-004` / H-001 como **caso fundacional**, aplicando uno a uno los requisitos del principio 17.

**(1) Demostración de mala especificación.**

- *Lo que el criterio declaraba medir, textual de `exp-004/PREREG.md`:* «**Robustez, NO optimización.** Comprobar si el largo del canal 512 […] es una **MESETA** (edge estructural real, robusto a variación razonable del lookback) o un **PICO aislado** (sobreajuste al parámetro).»
- *La forma de la regla:* MATA si **algún** vecino va a `net ≤ 0` o `alpha ≤ 0`. Una regla de disyunción sobre vecinos individuales, insensible al orden y a la forma del conjunto.
- *El patrón observado:* monótono creciente en las tres ventanas — 384 (Calmar −0.34) < 512 (1.35) < **640 (1.74)**.
- *La demostración:* la firma de un **pico aislado por sobreajuste** es 512 alto con **ambos** vecinos derrumbados. Aquí un vecino es superior al centro. La regla escrita no podía distinguir un pico de un **efecto umbral** (el edge, si existe, vive en canales largos y 384 cae por debajo del umbral), porque no examinaba la forma del conjunto en absoluto. El defecto es demostrable **desde el propio texto del pre-registro**, sin apelar a que el resultado incomode.
- *Elementos de refuerzo, verificables:* 512 fue pre-registrado el 2026-06-24 **antes del primer backtest** y no se tuneó sobre el retorno; el vecino superior es 640 y **512 no se cambió** — no hubo re-optimización en ningún artefacto posterior (`exp-005`, `exp-008`, ficha).
- *Límite honesto que se declara:* esta demostración es de la **forma más débil** admitida por el requisito (1) — se apoya en el texto del pre-registro, no en contraejemplos independientes. La demostración fuerte del mismo tipo existe en el laboratorio y es la de `exp-005` (el criterio de alfa también falla sobre BTC y SOL *dentro* de muestra, luego era malo con independencia de HYPE). Se hace constar la diferencia para que no se cite este caso como estándar de exigencia.
- *Lo que la demostración NO dice:* que 384 perdiendo dinero sea irrelevante. **Es una falla de robustez real**, y por eso el resultado de esta adjudicación no es la absolución.

**(2) Canal ADR.** Este documento.

**(3) Arbitraje A-04.** Pendiente, en sesión independiente, sobre este ADR. **No se anticipa su resultado.**

**(4) Ratificación del IP.** Pendiente. Ningún efecto de §4.5 y §4.6 rige antes de ella.

**(5) Prohibición de re-optimización.** Se reafirma y se extiende: `ENTRY_LEN` permanece en **512** (`EXIT_LEN` 256), la cesta permanece en los 5 símbolos, la lente de juicio de cada prueba es la de su pre-registro, y **el lado corto no se retira** pese a que `exp-005` muestre largo > corto en las 7 monedas. Nada de lo visto en backtest cambia la especificación.

**(6) Veredicto sobre H-001 y consecuencias mínimas:**

- **Estatus epistemológico: CUESTIONADA**, permanente y visible en su ficha, con el literal: *«CUESTIONADA (ADR-0007): sobrevivió por excepción de criterio mal especificado a un disparo letal de robustez de lookback (exp-004, 2026-07-06); alfa no significativa (t=0.94); edge no distinguible de suerte con los datos actuales.»*
- **Estado de pipeline: EN VALIDACIÓN**, con Fase A convalidada (acto 13) y Fase B en curso.
- **Deuda de instrumento registrada** para el ciclo C-002 del Banco: (a) los criterios de sensibilidad de parámetro deben distinguir explícitamente **pico / umbral / monotonicidad** y declarar la forma del conjunto que consideran evidencia de sobreajuste; (b) los criterios de OOS deben elegir su lente (alfa vs. Sharpe) **en el pre-registro** y justificar por qué es la adecuada para una estrategia de baja volatilidad.
- **Condición (i) — `exp-008` en nivel R0.** El experimento es válido y su veredicto R0 está verificado (paridad OK, dataset APTO de A-02 con hashes congelados). **Su efecto normativo se declara aquí y rige desde la ratificación de este ADR, no desde el 2026-07-17.** Se hace constar sin atenuarlo que el nivel letal de este mismo experimento fue **endurecido** el día de su pre-registro, a petición del IP y antes de ver el dato (O-001 del primer dictamen: verificación literal correcta, principio 4 cumplido; la consecuencia sobre la fuerza del compromiso es del IP).
- **Condición (ii) — cláusula del segundo disparo**, sobre el conjunto cerrado de §4.5.1.

**(7) Versionado.** Al prosperar la excepción, el disparo del 07-06 no activa `PROTOCOLO §5`: H-001 conserva su linaje **v1** con la anotación permanente del disparo y de la excepción. Si se produce el segundo disparo, se aplica sin excepción: **H-001.v2**, pre-registro nuevo, pipeline completo desde el inicio.

#### 4.5.1 — Enumeración cerrada de los «experimentos pendientes» de la cláusula del segundo disparo

Esta es la lista **explícita y cerrada** a la que se refiere la condición (ii). No es una fórmula abierta. Solo lo enumerado aquí puede disparar la cláusula.

| # | Prueba pendiente | Umbral letal pre-escrito | Fuente | Horizonte |
|---|---|---|---|---|
| P-1 | **Fase B (testnet) de H-001** | Reprobación de cualquiera de sus criterios: TE acumulado fuera de ±5% del modelo; slippage mediana de exceso > 5 bps; ≥1 omisión BTC por `min_notional` sin decisión documentada; desviación de métrica sin explicación. «Casi pasa = no pasa» | `prereg/PREREG_FASE_AB.md` + ENMIENDA 1 | Cierre previsto **≤ 2026-08-16** (un mes desde el re-corte del 07-16); se extiende solo por reinicio de reloj documentado |

**Frontera reprobación / aborto, cerrada expresamente:** la reprobación de un criterio de P-1 **no puede reclasificarse como corrección crítica ni como aborto** para esquivar el disparo; en caso de duda sobre la frontera, la clasificación la arbitra **A-04 antes de reiniciar reloj alguno**.
| P-2 | **Sello del `PREREG_FASE_C`** | No es experimento: es compuerta. Se enumera para excluirlo expresamente — **no puede disparar la cláusula**; su no-sello bloquea la Fase C por su propia regla | `fase_C/PREREG_FASE_C_BORRADOR.md` §1 | — |

**Alcance real del compromiso, declarado sin adorno.** Cerrados `exp-002` a `exp-008`, **el compromiso falsable restante se reduce a un único experimento pendiente: P-1 (Fase B).** Esta circunstancia **no amplía ni modifica los requisitos de validación**; refleja el estado real del expediente. Se declara expresamente para que la brevedad de la lista no se lea como omisión. Ensanchar la enumeración con pruebas inventadas para que el compromiso «pese más» sería inflarlo, no endurecerlo. Si el IP quiere aumentar la exigencia, la vía correcta es **pre-registrar un experimento nuevo con su propio umbral letal** e incorporarlo a esta lista por ADR — nunca reinterpretar la cláusula.

**Reglas de cómputo, declaradas para que la condición pueda cerrarse y no solo abrirse:**

- **Prospectividad.** La cláusula rige **desde la ratificación de este ADR hacia adelante**. No alcanza a experimentos ya corridos, cuyos veredictos quedan inventariados y adjudicados en §4.1: `exp-005` **BANDERA** (no letal), `exp-006` **SOBREVIVE**, `exp-007` **PROTEGE**, `exp-008` **R0**. Esto resuelve la indeterminación señalada como O-002 en el primer dictamen.
- **Recuento a la fecha de ratificación: cero disparos letales pendientes.**
- **Qué NO cuenta como disparo.** `paper_real` y cualquier serie de forward **no** disparan la cláusula, porque **no tienen umbral letal pre-escrito** y su propio PREREG los declara no-evidencia de fases. Son insumo de decisión, no compuerta. Se declara expresamente para que la lista no tenga bordes difusos.
- **Cierre de la condición.** La condición (ii) se declara **satisfecha** cuando P-1 cierre con aprobación y sin disparo, o cuando se alcance el **2026-09-30** sin disparo, lo que ocurra primero. Satisfecha o violada: ambas direcciones son alcanzables, que es lo que la falsabilidad exige (principio 15).
- **Cierre del conjunto.** Añadir una prueba a esta lista exige **ADR nuevo**. Retirar una prueba de esta lista **también** exige ADR nuevo, con dictamen A-04. La lista no crece por conveniencia ni encoge por incomodidad.
- **Consecuencia del disparo.** Un disparo letal en P-1 retira a H-001 del camino operativo de forma automática: la Fase C no se abre, la hipótesis vuelve a investigación como **H-001.v2**, **sin nota interpretativa posible y sin excepción posible** — la doctrina de la Parte III ya se consumió para esta hipótesis y la Parte IV impide toda retroactividad.

#### 4.6 — Actualización de registros y erratas (efectos diferidos)

Al ratificarse, y no antes:

1. **`CONSTITUCION.md`** — se incorpora el principio 17 con el texto íntegro de la Parte III, incluida su disposición transitoria.
2. **`PROTOCOLO.md`** — se añade el eje de **estatus epistemológico** (resolución de C-003, §4.7bis) y la remisión al principio 17 en el ciclo de vida.
3. **Ficha `H-001-canal-donchian.md`** — fuente única del estatus (resolución de C-002 y C-006): un solo campo de estatus epistemológico, con el literal de §4.5(6); filas append-only en el registro de eventos para el rechazo del ADR-0006, este ADR y su ratificación.
4. **`REGISTRO_HIPOTESIS.md` y `ESTADO.md`** — llevan **puntero a la ficha**, no copia del literal.
5. **Declaraciones a corregir**, por decir hoy algo distinto de lo verificable: toda mención a la condición (i) como «cumplida» o «sujeta a ratificación del ADR-0006» pasa a referirse a **este** ADR; y las menciones al ADR-0006 como norma viva se sustituyen por su estado real (**RECHAZADO**).
6. **Erratum fechado adjunto a `exp-008/PREREG.md`** — el pre-registro está sellado y **no se edita**; se adjunta un erratum que hace constar que su §«Contexto de acumulación» invocaba el ADR-0006, hoy rechazado, y que la cláusula aplicable es la de este ADR. El texto original permanece.
7. **`CHANGELOG.md`** — entrada fechada de la ratificación, sin adjetivos de completitud.
8. **`ADR-0000-plantilla.md`** — se añade la nota aclaratoria de la resolución de C-001 (§4.7bis): «excepciones concedidas» por ADR alcanza solo a normas de rango infra-constitucional; ninguna excepción a un principio constitucional se concede por ADR simple.

#### 4.7 — Secuencia de eficacia (ningún paso se adelanta)

```
1. ADR-0007 en estado Propuesta  ......................  ← hoy, 2026-07-18
2. Dictamen A-04, sesión independiente  ...............  CONFORME requerido
3. Ratificación del IP, fechada  ......................  acto único
4. Solo entonces, en el mismo acto de ratificación:
   4.a  enmienda de CONSTITUCION.md (principio 17)
   4.b  enmienda de PROTOCOLO.md (eje de estatus epistemológico)
   4.c  actualización de ficha / REGISTRO / ESTADO / CHANGELOG (§4.6)
   4.d  erratum adjunto a exp-008/PREREG.md
   4.e  nota aclaratoria de C-001 añadida a ADR-0000-plantilla.md
   4.f  efectos: convalidación de Fase A y del re-corte de Fase B;
        condición (i) vigente; cláusula del segundo disparo vigente;
        Fase C dependiente del veredicto de Fase B y del sello de su PREREG
```

Si el dictamen del paso 2 **no** es CONFORME, no se pasa al paso 3 y nada de lo anterior surte efecto. Si el IP no ratifica, rige el veredicto letal de `exp-004` con todas sus consecuencias, incluida la regla de versionado.

#### 4.7bis — Contradicciones elevadas y resueltas, una a una

Se elevan al IP y se propone resolución para cada una. A-04 las reportó y no las resolvió, que es su función; resolverlas es del IP por ADR, y este es el ADR.

**C-001 — Preámbulo constitucional («modificar *primero* la Constitución») vs. `ADR-0000` y principio 15 (el ADR como instrumento para «excepciones concedidas»).**
*Resolución propuesta:* **prevalece el preámbulo.** «Excepciones concedidas» en `ADR-0000` se refiere a excepciones a normas de rango infra-constitucional (protocolo, criterios de fase, reglas de proceso). **Ninguna excepción a un principio constitucional puede concederse por ADR simple**: requiere enmienda previa del texto, que es lo que hace la Parte III. Se añade nota aclaratoria a `ADR-0000-plantilla.md`. *(Con esto, el defecto que hundió al ADR-0006 queda cerrado en su raíz, no parcheado.)*

**C-002 — Principio 12 («una sola fuente de verdad»; «la duplicación de información es un bug documental») vs. la orden de escribir el mismo estatus en tres registros.**
*Resolución propuesta:* **prevalece el principio 12.** El estatus epistemológico de una hipótesis vive **solo en su ficha**. `REGISTRO_HIPOTESIS.md` y `ESTADO.md` llevan **puntero**, nunca copia del literal. La desincronización que A-04 detectó como V-004 es exactamente el fallo que el principio 12 predice; se corrige eliminando la duplicación, no vigilándola. *(Coste declarado: el lector de `ESTADO.md` necesita un salto más para ver el literal completo. Se acepta.)*

**C-003 — Estados del `PROTOCOLO` (`EN VALIDACIÓN · VALIDADA · RECHAZADA · EN PRODUCCIÓN · RETIRADA`) vs. el estatus «CUESTIONADA», no previsto.**
*Resolución propuesta:* son **dos ejes distintos y se separan formalmente**. El **estado de pipeline** conserva exactamente los cinco valores del Protocolo, y no se le añade ninguno. El **estatus epistemológico** es un eje nuevo, ortogonal, que describe la calidad de la evidencia y no la posición en el pipeline; sus valores iniciales son `NO PROBADA` · `CUESTIONADA` · `PROBADA`. `CUESTIONADA` **no** es un estado de pipeline. Se enmienda `PROTOCOLO.md` para declarar el eje, sus valores y quién lo fija (el ADR que lo impone). *(Coste declarado por el principio 16: un eje nuevo que mantener. Lo que evita: que cada excepción invente un estado ad-hoc, que es lo que ocurrió aquí.)*

**C-004 — Regla de versionado (`PROTOCOLO §5`: reprobación → `H-XXX.v1` RECHAZADA → `v2` con pipeline completo) vs. la continuidad de H-001.v1.**
*Resolución propuesta:* la colisión es real y se resuelve **en el texto constitucional, no por interpretación**: el requisito (7) del principio 17 declara expresamente que un disparo cuya anulación prospera **no es una reprobación** a efectos del versionado, porque no hubo veredicto válidamente producido. Fuera de ese supuesto — es decir, **en todos los demás casos** — `PROTOCOLO §5` se aplica sin matices. Y si llega el segundo disparo de la cláusula (ii), se aplica íntegro. *(Se hace constar que esta resolución es la más gravosa del ADR: es la que efectivamente mantiene viva a H-001.v1. Por eso se escribe en la Constitución, donde es visible y enmendable, y no en una lectura del Protocolo.)*

*Salvaguarda de alcance.* Precisamente porque el requisito (7) concentra casi toda la utilidad práctica de esta doctrina — y será, previsiblemente, el párrafo más citado del artículo —, su alcance queda acotado **en el propio texto constitucional** por el requisito (8): las resoluciones dictadas bajo el requisito (7) **no constituyen precedente automático**, y todo expediente posterior deberá satisfacer íntegramente el principio 17 sin invocar la existencia del presente caso como argumento suficiente. El límite es explícito y no implícito, por la misma razón por la que la resolución es constitucional y no interpretativa: lo que no está escrito, se acaba leyendo como uno quiere.

**C-005 — El texto constitucional propuesto exigía ratificación *antes* de los efectos, lo que hacía inadmisible al propio ADR que lo proponía.**
*Resolución propuesta:* **la disposición transitoria única de la Parte III.** El requisito (4) se conserva íntegro y sin rebajas para todo caso futuro; el caso fundacional se admite por una transitoria **expresa, nominativa y autoderogable**, que lo identifica (`exp-004` + nota de `exp-005`, 2026-07-06), lo admite solo por su anterioridad al artículo, le exige el cumplimiento íntegro de los demás requisitos, le exige el requisito (4) hacia adelante (cero efectos antes de la ratificación), y **se deroga por su propio cumplimiento**. Con ello, ADR-0007 es admisible bajo su propia regla sin abrir ninguna vía para un segundo caso. Esta es la resolución del defecto lógico que el segundo dictamen señaló como C-005.

**C-006 — Dos estatus simultáneos en la misma tabla de la ficha.**
*Resolución propuesta:* la misma que C-002, aplicada dentro del documento: **un único campo de estatus epistemológico** en la ficha; el campo `Estado` queda como estado de pipeline puro (eje de C-003) y no duplica información. El bug era intra-documento; la regla es la misma.

#### 4.8 — Lo que este ADR no declara

Se hace constar expresamente, como lección de las tres sobre-declaraciones que constan en el expediente del ADR-0006:

- **Este ADR no declara que cumpla los requisitos del encargo**, ni que responda a todas las violaciones y contradicciones de los dos dictámenes, ni que su inventario sea exhaustivo, ni que su enumeración sea la correcta, ni que su remediación sea completa. Ninguna de esas afirmaciones aparece en este texto, y si alguna se hubiera colado, debe leerse como defecto y no como hecho.
- **La conformidad la dicta A-04**, en sesión independiente, y solo A-04. La ratificación la otorga el IP, y solo el IP.
- El **Anexo A** es un localizador para facilitar la verificación: indica dónde buscar cada punto, **no afirma que lo encontrado sea suficiente**.

---

## 5. ¿Qué evidencia futura podría justificar revisarla?

Condiciones observables y específicas. Cuando una ocurra, se abre el ADR de revisión — **este no se reinterpreta**.

**Sobre H-001 (revisión automática, sin margen de apreciación):**

- **Disparo letal en P-1** (§4.5.1) → retiro operativo automático, Fase C cerrada, vuelta a investigación como `H-001.v2` con pipeline completo. Sin nota, sin excepción, sin ADR de rescate.
- **Cierre de Fase B con aprobación y sin disparo, o llegada del 2026-09-30 sin disparo** → la condición (ii) se declara satisfecha y se cierra; la Fase C queda dependiente únicamente del sello de su PREREG.
- **Cualquiera de las 4 señales de retiro conceptual** de `HIPOTESIS_ECONOMICA.md §5` → retiro aunque el PnL acompañe.
- **Acumulación de forward suficiente** (`paper_real` + Fases B/C, universo fijo) para que la significancia deje de ser indistinguible de suerte, en cualquiera de las dos direcciones. Es el árbitro que la propia nota del 07-06 designó y sigue siéndolo.

**Sobre la doctrina del principio 17 (revisión de la norma, no del caso):**

- **Segunda invocación del principio 17 en el laboratorio** — aunque sea prospectiva y aunque prospere. Una excepción usada dos veces deja de ser excepción: obliga a auditar si el problema está en los criterios que se escriben, y la respuesta correcta puede ser endurecer el requisito (1) o derogar el artículo entero.
- **Un dictamen A-04 que declare CONFORME una invocación cuya demostración de mala especificación resulte después insostenible** → el requisito (1) es demasiado laxo y debe reescribirse.
- **Un caso en el que un investigador escriba criterios deliberadamente laxos** para no verse en esta situación → la doctrina estará produciendo el incentivo perverso que dice evitar, y debe revisarse contra el principio 16 (Costo de Gobernanza).
- **Auditoría de Simplicidad de 2027-07** — el principio 17 se somete a ella como cualquier otra pieza: ¿qué error evita, cuánto cuesta, qué absorbe o elimina?
- **Intento de invocar este ADR como precedente de retroactividad** → violación grave del método, tratada como tal por la Auditoría de Creencias; y recordatorio de que se invoca una disposición derogada.

---

## Anexo A — Localizador para el arbitraje

No es una declaración de cumplimiento. Indica dónde está tratado cada punto, para que la verificación de A-04 pueda ser literal. **Si un punto está tratado de forma insuficiente, la insuficiencia es del ADR.**

| Origen | Punto | Dónde se trata |
|---|---|---|
| Mandato IP | Parte I — reconocimiento sin matices | §4 · Parte I |
| Mandato IP | Parte II — nulidad de las notas | §4 · Parte II |
| Mandato IP | Parte III — nueva doctrina | §4 · Parte III (principio 17) |
| Mandato IP | Parte IV — cláusula única e irrepetible | §4 · Parte IV + transitoria de la Parte III |
| Encargo, req. 1 | Inventario de actos 07-06→07-17 con validez | §4.1 (22 actos fechados) |
| Encargo, req. 2 | Enumeración cerrada de experimentos pendientes | §4.5.1 (P-1, P-2 + reglas de cómputo y cierre) |
| Encargo, req. 3 | Contradicciones una a una | §4.7bis (C-001…C-006) |
| Encargo, req. 3 | C-005 en particular: transitoria que hace admisible a este ADR | Parte III, disposición transitoria · §4.7bis C-005 |
| Encargo, req. 4 | Adjudicación del caso de fondo | §4.5 y §4.5.1 |
| Encargo, req. 5 | Sin declaraciones de completitud propia | §4.8 (este ADR) · Parte III, principio 17 **(9)(c)** (regla general) |
| Prueba de autosuficiencia | Garantías migradas de la explicación al articulado | Parte III: apertura del artículo (lente de juicio y veredictos no letales) · **(6)** (conjunto cerrado no modificable sin ADR+A-04) · **(9)** (inadmisibilidad de plano, día del disparo, no autodeclaración) · transitoria (no reabrible por ADR que la invoque) |
| Encargo, req. 6 | Plantilla de 5 preguntas, estado Propuesta, secuencia | §1–§5 · cabecera · §4.7 |
| Dictamen v1 | V-001 fuente normativa de la excepción | Parte III (enmienda constitucional) · §4.7 paso 4.a |
| Dictamen v1 | V-002 efectos consumados antes de ratificar | §4.1 actos 13, 14, 16, 21, 22 · §4.5(6) · §4.7 |
| Dictamen v1 | V-003 inventario | §4.1 |
| Dictamen v1 | V-004 ficha / duplicación de estatus | §4.6.3–4 · §4.7bis C-002 |
| Dictamen v1 | V-005 nota de exp-005 | Parte II · §4.1 acto 2 |
| Dictamen v1 | V-006 «experimentos pendientes» no falsable | §4.5.1 |
| Dictamen v1 | O-001 endurecimiento del letal de exp-008 | §4.5(6), hecho constar sin atenuar |
| Dictamen v1 | O-002 regla de cómputo del segundo disparo | §4.5.1, regla de prospectividad |
| Dictamen v2 | V-101 rótulo de cobertura total sobre cobertura parcial | §4.8 (no se emplea ningún rótulo de cobertura) |
| Dictamen v2 | V-102 registros que declaran remediación completa | §4.6.5 · §4.8 |
| Dictamen v2 | V-103 C-002/003/004 no elevadas | §4.7bis |
| Dictamen v2 | C-005, C-006 | §4.7bis |
| Dictamen v2 | O-002 residuo en exp-008/PREREG | §4.1 acto 19 · §4.6.6 (erratum adjunto, sin editar el sellado) |
| Dictamen v2 | O-004 orden de secciones | §1–§5 en orden canónico; anexos después de §5 |
| Dictamen v2 | O-005 metadato desactualizado en ESTADO | §4.6.4 |

---

## Anexo B — Fundamento conservado (textual del IP)

> *"Mi decisión no depende demasiado de H-001. Depende del laboratorio. Porque incluso si H-001 termina muriendo dentro de dos meses, el laboratorio habrá salido fortalecido. Y si sobrevive, también."*

---

*ADR-0007 · Propuesta · 2026-07-18 · sesión redactora independiente · pendiente de dictamen A-04 y de ratificación del IP.*
