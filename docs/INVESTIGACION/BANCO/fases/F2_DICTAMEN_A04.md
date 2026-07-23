# Dictamen A-04 sobre F2 — Ciclo C-001

> Producido en sesión independiente (subagente aislado, dieta mínima: prompt A-04 + ORQUESTADOR.md + F2_ARBOL.md + F0_PROTOCOLO.md + F1_catalogo.jsonl, sin contexto de conversación) el 2026-07-20. Archivado verbatim, append-only. **Resultado: NO CONFORME** por V-001 (falta el artefacto estructurado JSONL de F2 que exige la regla dura 9). Reporta además una contradicción interna del ORQUESTADOR (C-001). Todo lo demás de F2 quedó verificado CONFORME.

```
DICTAMEN A-04
Artefacto evaluado: F2_ARBOL.md — "Árbol genealógico por mecanismos" (fechado 2026-07-20, ejecutor Opus) · Ciclo C-001
Estado: ☐ CONFORME  ☒ NO CONFORME
────────────
Requisitos (según lo que ORQUESTADOR / F0 exigen a esta fase):

□ ✔ Estructura de árbol MECANISMO → FAMILIA → VARIANTE (prompt F2). M1..M5 con familias y variantes F1-xxx.
□ ✔ Agrupamiento por ineficiencia, no por indicador (regla 1). Donchian/MA-cross/TSM unificados vía F1-005.
□ ✔ Herencia de evidencia hacia arriba + tabla de herencia (regla 2). Distingue edge vs. teoría/fundamento.
□ ✔ Evidencia específica de variante anotada (regla 2). Cada nodo conserva su nivel individual.
□ ✔ Casos dudosos con doble ubicación, sin forzar (regla 3). F1-018 (M1↔M3), F1-020 (M4↔M2), F1-022 (M4↔M5).
□ ✔ Asignación de mecanismo PROVISIONAL, la confirma F4 (regla 4).
□ ✔ Fidelidad a F1 — 30 entradas ubicadas (M1=7, M2=6, M3=5, M4=7, M5=5 = 30); niveles idénticos al JSONL de F1.
□ ✔ No se inventaron entradas / variantes / fuentes fuera de F1 (regla dura 2).
□ ✔ Auditar, no calcular (regla dura 2). Sin retornos/Sharpe/pesos; consolidación cualitativa, no-promediado respetado.
□ ✔ Ejecutor se abstiene de priorizar / rankear / seleccionar / emitir veredictos (F0; §10) — con Observación O-1.
□ ✔ Documento fechado; ejecutor declarado (Opus); cierre no autodeclarado.
□ ✘ Artefacto estructurado (JSONL) + vista Markdown generada a partir de él (regla dura 9) — NO VERIFICABLE. La dieta contiene solo F2_ARBOL.md; no consta JSONL de F2, y el documento no declara derivarse de uno. Carga de la prueba en el artefacto → cuenta contra la conformidad. Ligado a C-001.

────────────
Violaciones:
V-001 — Norma (regla dura 9, textual): "desde F1, cada fase produce su registro en formato estructurado (JSONL: un objeto por entrada) más una vista Markdown generada a partir de él — nunca al revés." · Hecho: F2 es fase "desde F1"; no se aporta ni se declara ningún artefacto estructurado JSONL de F2, y F2_ARBOL.md no indica derivarse de uno. · Evidencia: F2_ARBOL.md (sin referencia a JSONL); ausencia de artefacto estructurado en la dieta entregada.

────────────
Contradicciones detectadas (se reportan, JAMÁS se resuelven):
C-001 — Contradicción interna del ORQUESTADOR sobre si F2 debe producir JSONL: (a) regla dura 9 exige JSONL a "cada fase desde F1"; frente a (b) la tabla de Fases, que fija el producto de F2 como solo "F2_ARBOL.md"; (c) la enumeración de fases que AÑADEN campos al JSONL (F3/F4/F5/F7), que OMITE a F2; y (d) el prompt F2, que fija "Producto: el árbol completo + tabla de herencia de evidencia" sin mencionar JSONL. No la resuelvo; corresponde al IP vía ADR. (Nota: para F1 la tabla también nombra solo el .md pese a existir JSONL obligatorio, lo que impide inferir la exención por el mero nombrado del .md.)

────────────
Observaciones:
O-1 — La tabla rotula M1 "El caso más fuerte del ciclo": lenguaje comparativo que roza la priorización. Se registra; no se eleva a violación porque describe la consolidación de evidencia (mandato de herencia de F2), no una selección/scoring de candidatas (F7).
O-2 — Referencias a H-001 / "Donchian 512" pertenecen al pipeline, fuera de dieta → no verificables; no se presentan como fuentes de F1, no afectan la fidelidad.
O-3 — Compuertas administrativas de cierre quedan fuera de dieta y downstream; F2 las declara pendientes y no se autodeclara cerrada (correcto).

────────────
Condición de levantamiento: se levanta V-001 con cualquiera de dos vías: (1) exhibir el artefacto estructurado JSONL de F2 (fuente de la vista .md) conforme a regla dura 9; o (2) que el IP resuelva C-001 por ADR, declarando a F2 exenta de la cláusula JSONL de regla 9 (producto = árbol .md + tabla) e incorporándolo al F0 del C-002. Con cualquiera, y sin nuevos hallazgos, los demás requisitos de F2 quedan CONFORMES.

────────────
Firma: A-04 · 2026-07-20 · sesión independiente
```

## Efecto

F2 queda **NO CONFORME** hasta el levantamiento de V-001. Todo el trabajo sustantivo de F2 (árbol, herencia, casos frontera, fidelidad a F1) está verificado CONFORME; el único bloqueo es de **formato**: falta el registro estructurado JSONL que la regla dura 9 exige a toda fase desde F1. El dictamen se conserva íntegro; su resolución (producir el JSONL, o ADR de exención) es del IP.
