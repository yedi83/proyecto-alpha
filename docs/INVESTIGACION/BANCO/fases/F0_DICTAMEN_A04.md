# Dictamen A-04 sobre F0 — Ciclo C-001

> Producido en sesión independiente (subagente aislado, dieta de insumos mínima: prompt A-04 + ORQUESTADOR.md + F0_PROTOCOLO.md, sin contexto de diseño ni conversación) el 2026-07-19. Archivado verbatim, append-only. **Resultado: NO CONFORME → el cierre de F0 y la apertura de C-001 quedan bloqueados hasta el levantamiento.**

```
DICTAMEN A-04
Artefacto evaluado: `F0_PROTOCOLO.md` — Protocolo del Banco de Mecanismos, Ciclo C-001 (sesión fechada 2026-07-10; sin nº de versión propio en el encabezado)
Estado: ☐ CONFORME  ☒ NO CONFORME
────────────
Requisitos (según lo que ORQUESTADOR/F0 exigen a esta fase):

Contenido exigido a F0 (ORQUESTADOR tabla fila F0 + prompt F0 + F0 mismo):
□ ✔ Preguntas de investigación — presente. F0 §1 (4 preguntas, incl. meta-pregunta del piloto). Ref. ORQUESTADOR L60/L73(1).
□ ✔ Familias en alcance + excluidas — presente. F0 §2 (tabla de mecanismos en alcance + bloque "Fuera del Ciclo 1"). Ref. ORQUESTADOR L60/L73(2).
□ ✔ Rúbrica con escala 0–5 y anclas verbales — presente. F0 §3 (anclas verbales en 0/3/5). Ref. ORQUESTADOR L60/L73(3).
□ ✔ Pesos declarados — presente y suman 100% (35/30/20/10/5). F0 §3. Ref. ORQUESTADOR L73(3).
□ ✘ Rúbrica con los criterios enumerados por la norma — el criterio "resiliencia" NO se puntúa (se traslada a compuerta) y se añade "Falsabilidad / claridad del protocolo", no enumerado en el prompt. Ver C-001. Ref. ORQUESTADOR L73(3) vs F0 §3 y §3(c).
□ ✔ Análisis de sensibilidad OBLIGATORIO (±20% por peso) — presente. F0 §3(b). Ref. F0 §3(b).
□ ✔ Jerarquía de niveles de evidencia I–VII + regla de no-promediado — presente. F0 §4. Ref. ORQUESTADOR L73(4).
□ ✔ Fuentes aceptadas — presente. F0 §5. Ref. ORQUESTADOR L60.
□ ✔ Formato exacto del PROTOCOLO CANDIDATO — presente. F0 §6. Ref. ORQUESTADOR L60/L73(5).
□ ✔ Cláusula "nada cambia sin enmienda fechada" / rúbrica fijada en F0 — presente. F0 §3(a) + encabezado. Ref. ORQUESTADOR regla 5 (L19).
□ ✔ Regla de Inmutabilidad del Ciclo enunciada en el artefacto — presente. F0 encabezado. Ref. ORQUESTADOR regla 8 (L22).
□ ✔ Ciclo identificado con ID trazable — presente ("Ciclo C-001"). F0 título. Ref. ORQUESTADOR regla 11 (L25).
□ ✘ Ejecución por el modelo mandatado — la norma exige "Opus + humano"; F0 declara "Investigador Principal (humano) + Fable 5". Ver V-001. Ref. ORQUESTADOR L60/L71 vs F0 L3.

Cierre administrativo (solo lo comprobable con la dieta):
□ ✔ Documento fechado en `fases/` — F0 encabezado, 2026-07-10.
□ ✔ Rúbrica con anclas y pesos — F0 §3.
□ ✔ Jerarquía de niveles con regla de no-promediado — F0 §4.
□ ✔ Formato del protocolo candidato — F0 §6.
□ ✔ Regla de sensibilidad obligatoria — F0 §3(b).
□ ✔ Regla de inmutabilidad del ciclo — F0 encabezado + ORQUESTADOR regla 8.

Checklist de apertura de ciclo (ORQUESTADOR L29–36) — puntos FUERA DE DIETA, no verificables con estos tres documentos; decisión FUERA DE MI ALCANCE:
□ NO VERIFICABLE — "ADRs del ciclo anterior incorporados o declarados pendientes" (exige registro de ADRs, no en dieta).
□ NO VERIFICABLE — "Constitución y ORQUESTADOR consistentes con F0" (la Constitución no está en dieta; solo pude cotejar ORQUESTADOR↔F0).
□ NO VERIFICABLE — "Versión del Banco etiquetada (git tag banco-C001-abierto)" (exige estado de repositorio).
□ NO VERIFICABLE — "Acta de una línea: Ciclo C-001 abierto…" (no aparece en ninguno de los tres archivos).
□ NO APLICABLE aún — "Dictamen A-04 sobre F0 = CONFORME": es el presente dictamen; no puede tratarse como insumo preexistente.
────────────
Violaciones:
V-001 — Norma (textual): ORQUESTADOR, tabla de Fases fila F0, col. Modelo "Opus + humano"; y prompt "### F0 — Protocolo (Opus + humano, sesión conjunta)". Hecho: F0_PROTOCOLO.md L3 declara la sesión ejecutada por "Investigador Principal (humano) + Fable 5", modelo distinto del mandatado por la norma para F0. Evidencia: F0 encabezado (L3) vs ORQUESTADOR L60 y L71. No juzga la calidad del protocolo; juzga que el ejecutor no es el que la norma otorga a esta fase.
────────────
Contradicciones detectadas (se reportan, JAMÁS se resuelven):
C-001 — ORQUESTADOR prompt F0 (L73) enumera como criterios de la rúbrica "…transferibilidad, **resiliencia**, complementariedad conceptual…". F0 §3 NO puntúa "resiliencia" y §3(c) declara "la resiliencia adversarial no se puntúa: es COMPUERTA", sustituyéndola por un criterio no enumerado por la norma, "Falsabilidad / claridad del protocolo" (10%). Texto normativo (criterios enumerados) y texto del artefacto (reclasificación a compuerta + criterio añadido) están en tensión directa. No la resuelvo: la dirime el humano vía ADR.
────────────
Observaciones: (1) La rúbrica (F0 §3) se rotula "ADR provisional v1.0" con "pesos provisionales"; el término "provisional" no contradice por sí solo la inmutabilidad intra-ciclo (F0 encabezado la circunscribe a revisión inter-ciclo), pero se anota para el registro. (2) Las anclas verbales se fijan en los puntos 0/3/5 de la escala 0–5; suficiente para la casilla literal, se anota que los puntos 1/2/4 quedan sin ancla textual.
────────────
Firma: A-04 · 2026-07-19 · sesión independiente
```

## Condición de levantamiento (para pasar a CONFORME)

Resolución por el IP de V-001 y C-001 (vía ADR, canal que la Constitución exige para desviaciones de método), y luego **re-arbitraje A-04 en sesión independiente nueva**. Ningún acto de apertura (tag, acta) es válido antes del CONFORME. La resolución NO la decide A-04 ni esta sesión.
