# ADR-0006 — Override del veredicto letal de exp-004 (formalización retroactiva)

- **Fecha:** 2026-07-17 · **v2: 2026-07-18** (enmendada tras dictamen A-04 NO CONFORME — ver §6)
- **Estado:** Propuesta v2 — **requiere RE-arbitraje A-04 + ratificación del IP**
- **Alcance:** Metodología + propuesta de enmienda constitucional (§6.4)

## 1. ¿Qué problema intentábamos resolver?

El criterio pre-escrito de exp-004 disparó MATA (vecino 384: net −8.6%, alfa −28.6%), pero el patrón observado (monótono: 384 < 512 < 640, con 640 en meseta superior) no es el que el criterio fue diseñado para cazar (pico aislado de sobreajuste). El laboratorio continuó H-001 hacia Fase B/C con una **nota interpretativa** junto al veredicto — un canal que la Constitución no reconoce para revertir un umbral pre-escrito. El registro oficial (ficha, REGISTRO, ESTADO) no reflejó el evento. Este ADR paga el precio constitucional de esa decisión: la hace explícita, arbitrable y falsable.

## 2. ¿Qué alternativas se evaluaron?

(a) **Acatar el MATA literal:** H-001 muere; todo lo operativo se detiene. Coste: matar por un criterio que su propio autor reconoce mal especificado (no distinguía pico de umbral) — un falso positivo del instrumento, no de la hipótesis. (b) **Sostener el override por nota interpretativa** (statu quo): decisión razonable por canal ilegítimo; precedente letal ("las notas pueden anular umbrales"). (c) **Override formal por ADR + arbitraje + degradación de estatus + condiciones falsables** — reconocer el disparo, declarar la falla del instrumento, y continuar bajo condiciones más duras y explícitas.

## 3. ¿Por qué se eligió esta?

Se elige (c). Fundamentos: el veredicto mecánico queda INTACTO en RESULTADO.md (no se reescribe historia); la falla de diseño del criterio es verificable (el criterio buscaba "512 alto con AMBOS vecinos derrumbados"; ocurrió monotonicidad con 640 superior — patrón de umbral); no hubo re-optimización (512 se mantiene); y la propia nota degradó honestamente el estatus ("prometedora pero NO probada... no se puede distinguir edge de suerte"). PERO un override así solo es legítimo si es caro: por eso este ADR impone condiciones (§4) y un precedente restrictivo (§5 de la plantilla → aquí punto 5).

## 4. ¿Qué consecuencias aceptamos?

1. **Estatus oficial de H-001 degradado en todos los registros** (ficha, REGISTRO, ESTADO): de "en validación" a **"EN VALIDACIÓN — CUESTIONADA: sobrevivió por override (ADR-0006) a un disparo letal de robustez de lookback; alfa no significativa (t=0.94); edge no distinguible de suerte con datos actuales."**
2. **La Fase C queda condicionada a evidencia ADICIONAL, no solo a que B apruebe:** (i) exp-008 (funding real) en nivel R0; (ii) ningún nuevo disparo letal en experimentos pendientes. Un segundo disparo letal de cualquier familia (p. ej. funding) **NO será interpretable por nota**: dos instrumentos independientes disparando = H-001 se retira del camino operativo y vuelve a investigación como H-001.v2, sin excepción — esta cláusula es el compromiso falsable de este ADR.
3. **Precedente restrictivo:** las notas interpretativas NUNCA anulan umbrales ni cambian lentes de juicio. El único canal es ADR + arbitraje A-04 + degradación de estatus + condiciones falsables. ~~Este ADR es la única vía retroactiva admitida~~ **(v2: la afirmación original era fácticamente falsa — existía una segunda nota del mismo canal en exp-005; este ADR cubre AMBAS, ver §6.2, y con ello agota la vía retroactiva)**. Futuros disparos se gestionan por el canal formal DESDE EL DÍA del disparo.
4. Deuda de diseño registrada para el C-002 del Banco: los criterios de sensibilidad deben distinguir pico/umbral/monotonicidad (aprendizaje del instrumento).

## 6. ENMIENDA v2 (2026-07-18) — respuesta al dictamen A-04 NO CONFORME

El dictamen (ADR-0006_DICTAMEN_A04.md) encontró 6 violaciones y 4 contradicciones. Todas verificadas como ciertas. Respuesta punto por punto:

1. **Ficha sin actualizar (violación de §4.1 por el propio redactor):** remediada el 2026-07-18 — la ficha H-001 incorpora el disparo de exp-004, ambas notas, este ADR, exp-008 y el dictamen, con el estatus CUESTIONADA en su encabezado.
2. **Segunda nota del mismo canal (exp-005) sin cubrir:** este ADR extiende su alcance a la nota de exp-005 con idéntico tratamiento — su veredicto mecánico (BANDERA por HYPE alfa≤0) queda INTACTO en su RESULTADO; el cambio de lente alfa→Sharpe post-hoc se reconoce como override por canal ilegítimo; su contenido interpretativo se acepta como *contexto degradado* (la propia nota ya concluía "no cambia el estado de H-001: no probada, baja convicción" — no relajó ninguna consecuencia práctica, lo que atenúa el daño pero no legitima el canal). Deuda de instrumento registrada para el Banco C-002: los criterios de OOS deben elegir su lente (alfa vs. Sharpe) EN el pre-registro.
3. **Condición (i) consumida bajo ADR no ratificado (exp-008 "vinculante"/"cumplida" el mismo día):** se reconoce como violación de secuencia del propio redactor. Cura: todas las declaraciones "CUMPLIDA" en REGISTRO/ESTADO/ficha quedan re-etiquetadas **"sujeta a ratificación de este ADR"**; si el IP no ratifica, exp-008 conserva su validez experimental (prereg sellado, dataset APTO, umbrales intactos) pero su efecto sobre la Fase C queda sin base normativa hasta nueva decisión.
4. **Falta de enmienda constitucional (contradicción con el preámbulo):** este ADR **propone** el texto que el preámbulo exige, a añadir a la Constitución COMO PARTE de la ratificación (no antes): *"Excepción única al principio 4: un veredicto de umbral pre-escrito solo puede ser anulado si su criterio se demuestra mal especificado para el patrón observado, mediante ADR arbitrado por A-04 y ratificado por el IP ANTES de que la anulación surta efectos. Las notas interpretativas carecen de fuerza normativa. (Origen: ADR-0006.)"*

## 5. ¿Qué evidencia futura podría justificar revisarla?

- **Contra H-001:** el disparo de cualquiera de las condiciones de §4.2 → retiro operativo automático (ya comprometido).
- **Contra este ADR como precedente:** si A-04 dicta VIOLACIÓN sobre esta formalización, el IP debe decidir entre acatar el MATA original o re-fundamentar; si en el futuro se detecta un segundo intento de override por nota, la Auditoría de Creencias lo trata como violación grave del método.
- **A favor de cerrar el caso:** forward con universo fijo (paper_real + Fase B/C) acumulando n suficiente para que la significancia deje de ser indistinguible de suerte — el árbitro final que la propia nota designó.
