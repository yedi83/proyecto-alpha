# Dictámenes A-04 sobre F3 — Ciclo C-001

> Rastro append-only. Cada dictamen se produjo en sesión independiente aislada (dieta mínima: prompt A-04 + ORQUESTADOR + F3 [JSONL+vista] + F0 + F2). Secuencia: **v1 NO CONFORME** (la vista MD subcontaba las entradas verificadas: 10 vs. 11 del JSONL) → se regeneró la sección de trazabilidad desde el JSONL → **v2 CONFORME**. Ambos se conservan íntegros.

---

## Dictamen v1 — NO CONFORME (2026-07-21)

```
DICTAMEN A-04 — v1
Estado: NO CONFORME
Verificado CONFORME: regla 9 (JSONL existe, un objeto por entrada; MD declarada vista del JSONL; F3 añade nivel_evidencia_final + robustez_reportada[]); fidelidad a F2 (0 alteraciones); prompt F3(A) calidad de evidencia y (B) robustez reportada; reglas 1-2 (no verificable etiquetado, sin métricas inventadas, sin rankear); F0 §4 no-promediado (1 baja F1-006 III→IV justificada, 0 subidas); fechado, ejecutor declarado, cierre no autodeclarado.

V-001 — Norma (regla 9: la vista se genera DESDE el JSONL, que es "fuente de verdad"). Hecho: la sección "Trazabilidad de verificación" del MD listaba 10 entradas con verificacion_web=true, pero el JSONL contiene 11 (omitía F1-008, que en el JSONL lleva verificacion_web:"true (...)"). La vista no representaba fielmente al JSONL en su resumen; el criterio declarado ("true, sin etiquetas de memoria") era además incoherente (F1-001 listada pese a llevar un [memoria] en contradicciones; F1-008 excluida).

C-001 (contradicción reportada, no resuelta): la regla 9 impone nivel_evidencia_final por CADA entrada, mientras F0 §4 define la jerarquía I-VII "por edge"; las entradas tipo metodo/teoria (Régimen, teóricas) portan nivel pese a no ser edges. F3 ya lo documentó como fricción para C-002; resolución del IP vía ADR (regla 8 de inmutabilidad).

Condición de levantamiento: regenerar la sección de trazabilidad del MD desde el JSONL (lista y conteo de verificacion_web:true = 11, incl. F1-008; criterio coherente). Sin otras acciones.
Firma: A-04 · 2026-07-21 · sesión independiente
```

**Remediación aplicada (2026-07-21):** la sección "Trazabilidad de verificación" del MD se corrigió a **11 entradas** (F1-001/002/003/004/006/**008**/009/013/017/018/023), derivadas directamente del campo `verificacion_web` del JSONL, con criterio aclarado (una entrada verificada por web puede llevar un `[memoria]` en un sub-detalle sin dejar de estar verificada la fuente). No se tocó ningún dato del JSONL.

---

## Dictamen v2 — CONFORME (2026-07-21)

```
DICTAMEN A-04
Artefacto: F3_EVIDENCIA.md + F3_evidencia.jsonl (fuente de verdad) — Fase F3, Ciclo C-001.
Estado: ☑ CONFORME
────────────
✔ Regla 9 — JSONL (30 objetos, uno por entrada, secuencia completa).
✔ Regla 9 — vista declarada generada DESDE el JSONL (no al revés).
✔ Regla 9 — consistencia MD↔JSONL de listas/conteos, verificado objeto a objeto: verificacion_web:true=11 (lista idéntica), OOS reportado=6, 163 pruebas/36 reportado/127 no, walk-forward=0, bootstrap=0, MC=1, cross-market=tipo más reportado (17), niveles 1 baja/0 sube/29 igual, [memoria]=41 menciones en 21 entradas — todos coinciden.
✔ Regla 9 — campos añadidos por F3 (nivel_evidencia_final, robustez_reportada[]) presentes; campos de soporte de calidad compatibles.
✔ Fidelidad a F2 — 15 campos heredados, 0 discrepancias en las 30 entradas.
✔ Prompt F3(A) calidad de evidencia (escala F0 §4; riesgos reportado vs inferible; contradicciones; reproducibilidad) y (B) robustez reportada (OOS/WF/bootstrap/MC/cross-market, qué/cómo/resultado/limitaciones; "no reportado" como dato).
✔ Reglas 1-2 — no verificable etiquetado; cifras atribuidas a la fuente, ninguna calculada; sin evaluar rentabilidad ni rankear.
✔ F0 §4 — no-promediado; el único cambio de nivel justificado; 0 ascensos por acumulación.
✔ Fechado; ejecutor Opus; cierre no autodeclarado.
────────────
Violaciones: (ninguna)
Contradicciones: (ninguna reportable) — la granularidad por-entrada vs por-nodo está registrada por el artefacto como fricción para C-002 (regla 8), no como contradicción viva.
Observaciones: F1-030 cita un dictamen/contradicción previa heredada verbatim de F2 (fuera de dieta, no afecta); compuertas administrativas del cierre fuera de alcance.
Firma: A-04 · 2026-07-21 · sesión independiente
```

## Efecto

**F3 es CONFORME** tras una remediación (conteo de la vista alineado al JSONL). El dictamen v1 (NO CONFORME) se conserva íntegro. **F3 CERRADA por aprobación del IP el 2026-07-21.** La contradicción C-001 (niveles I-VII por-entrada vs. entradas "método/teoría") queda registrada como pendiente para el F0 del **C-002**. **F4 (fundamento económico + falsabilidad) desbloqueada.**
