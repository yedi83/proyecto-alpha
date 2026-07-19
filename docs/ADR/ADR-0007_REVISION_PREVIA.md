# Revisión previa del borrador ADR-0007 — lectura técnica, NO vinculante

> 2026-07-18. Revisor: la sesión que redactó el ADR-0006 (dos veces NO CONFORME) — por esa razón esta revisión es de SOLO LECTURA contra el encargo: reporta hallazgos, no edita el documento, no declara conformidad y no sustituye el arbitraje A-04. Las correcciones, si proceden, las hace la sesión redactora o el IP.

## Valoración general

El borrador cumple visiblemente la estructura del mandato (4 partes), los 6 requisitos del encargo tienen tratamiento localizable (Anexo A), las 6 contradicciones están elevadas con resolución propuesta, y no contiene declaraciones de completitud propia. La distinción "contenido probatorio vs. efecto normativo" (§4.1), la transitoria autoderogable (Parte III) y el requisito (8) anti-precedente son soluciones técnicamente sólidas a los defectos que hundieron al ADR-0006.

## Hallazgos (2 menores)

**H-1 — Efecto anunciado ausente de la lista de efectos.** §4.7bis C-001 dispone "Se añade nota aclaratoria a `ADR-0000-plantilla.md`", pero ese acto NO aparece en §4.6 (efectos diferidos) ni en la secuencia §4.7 paso 4. Un efecto que no está en la lista de efectos es exactamente el tipo de descuadre que A-04 caza. Corrección sugerida: añadirlo como §4.6.8 / paso 4.f.

**H-2 — Frontera reprobación-vs-aborto en P-1 sin palabra escrita.** §4.5.1 declara letal la "reprobación de cualquiera de sus criterios" de Fase B, y su horizonte admite extensión "solo por reinicio de reloj documentado". Pero el PREREG de Fases A/B distingue *aborto por corrección crítica* (bug → corrige → reinicia reloj) de *reprobación de criterios*. Sin una línea explícita, queda una vía de escape futura: reclasificar una reprobación incómoda como "bug crítico + reinicio" para esquivar el disparo. Corrección sugerida (una frase en §4.5.1): "La reprobación de un criterio no puede reclasificarse como corrección crítica ni como aborto; en caso de duda sobre la frontera, la clasificación la arbitra A-04 antes de reiniciar reloj alguno."

## Observación (para ratificar con conocimiento, no exige cambio)

**O-1 — Interacción entre la fecha de cierre (2026-09-30) y un posible reinicio de reloj de Fase B.** Si un reinicio legítimo lleva el cierre de B más allá del 30-09, la condición (ii) se declararía satisfecha por fecha con B aún corriendo; una reprobación posterior de B ya no retiraría a H-001 por la cláusula (aunque seguiría bloqueando la Fase C por la propia regla del PREREG_C — la protección de fondo no desaparece). El diseño es defendible (una condición debe poder cerrarse), pero el IP debe ratificarlo sabiéndolo.

## Recomendación de flujo

Una pasada breve de la sesión redactora para H-1 y H-2 (dos ediciones puntuales) → arbitraje A-04. Ir al arbitraje sin corregirlas es legítimo pero probablemente costoso: ambas son del tipo literal-verificable que el modo estricto detecta.
