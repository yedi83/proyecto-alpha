# ADR-0006 — Override del veredicto letal de exp-004 (formalización retroactiva)

- **Fecha:** 2026-07-17 (formaliza una decisión operada de facto desde 2026-07-06)
- **Estado:** Propuesta — **requiere arbitraje A-04 en sesión separada + ratificación del IP**
- **Alcance:** Metodología

## 1. ¿Qué problema intentábamos resolver?

El criterio pre-escrito de exp-004 disparó MATA (vecino 384: net −8.6%, alfa −28.6%), pero el patrón observado (monótono: 384 < 512 < 640, con 640 en meseta superior) no es el que el criterio fue diseñado para cazar (pico aislado de sobreajuste). El laboratorio continuó H-001 hacia Fase B/C con una **nota interpretativa** junto al veredicto — un canal que la Constitución no reconoce para revertir un umbral pre-escrito. El registro oficial (ficha, REGISTRO, ESTADO) no reflejó el evento. Este ADR paga el precio constitucional de esa decisión: la hace explícita, arbitrable y falsable.

## 2. ¿Qué alternativas se evaluaron?

(a) **Acatar el MATA literal:** H-001 muere; todo lo operativo se detiene. Coste: matar por un criterio que su propio autor reconoce mal especificado (no distinguía pico de umbral) — un falso positivo del instrumento, no de la hipótesis. (b) **Sostener el override por nota interpretativa** (statu quo): decisión razonable por canal ilegítimo; precedente letal ("las notas pueden anular umbrales"). (c) **Override formal por ADR + arbitraje + degradación de estatus + condiciones falsables** — reconocer el disparo, declarar la falla del instrumento, y continuar bajo condiciones más duras y explícitas.

## 3. ¿Por qué se eligió esta?

Se elige (c). Fundamentos: el veredicto mecánico queda INTACTO en RESULTADO.md (no se reescribe historia); la falla de diseño del criterio es verificable (el criterio buscaba "512 alto con AMBOS vecinos derrumbados"; ocurrió monotonicidad con 640 superior — patrón de umbral); no hubo re-optimización (512 se mantiene); y la propia nota degradó honestamente el estatus ("prometedora pero NO probada... no se puede distinguir edge de suerte"). PERO un override así solo es legítimo si es caro: por eso este ADR impone condiciones (§4) y un precedente restrictivo (§5 de la plantilla → aquí punto 5).

## 4. ¿Qué consecuencias aceptamos?

1. **Estatus oficial de H-001 degradado en todos los registros** (ficha, REGISTRO, ESTADO): de "en validación" a **"EN VALIDACIÓN — CUESTIONADA: sobrevivió por override (ADR-0006) a un disparo letal de robustez de lookback; alfa no significativa (t=0.94); edge no distinguible de suerte con datos actuales."**
2. **La Fase C queda condicionada a evidencia ADICIONAL, no solo a que B apruebe:** (i) exp-008 (funding real) en nivel R0; (ii) ningún nuevo disparo letal en experimentos pendientes. Un segundo disparo letal de cualquier familia (p. ej. funding) **NO será interpretable por nota**: dos instrumentos independientes disparando = H-001 se retira del camino operativo y vuelve a investigación como H-001.v2, sin excepción — esta cláusula es el compromiso falsable de este ADR.
3. **Precedente restrictivo:** las notas interpretativas NUNCA anulan umbrales. El único canal es ADR + arbitraje A-04 + degradación de estatus + condiciones falsables. Este ADR es la única vía retroactiva admitida y no se repite: futuros disparos se gestionan por el canal formal DESDE EL DÍA del disparo.
4. Deuda de diseño registrada para el C-002 del Banco: los criterios de sensibilidad deben distinguir pico/umbral/monotonicidad (aprendizaje del instrumento).

## 5. ¿Qué evidencia futura podría justificar revisarla?

- **Contra H-001:** el disparo de cualquiera de las condiciones de §4.2 → retiro operativo automático (ya comprometido).
- **Contra este ADR como precedente:** si A-04 dicta VIOLACIÓN sobre esta formalización, el IP debe decidir entre acatar el MATA original o re-fundamentar; si en el futuro se detecta un segundo intento de override por nota, la Auditoría de Creencias lo trata como violación grave del método.
- **A favor de cerrar el caso:** forward con universo fijo (paper_real + Fase B/C) acumulando n suficiente para que la significancia deje de ser indistinguible de suerte — el árbitro final que la propia nota designó.
