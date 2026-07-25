# Dictamen A-04 sobre F5 — Ciclo C-001

> Producido en sesión independiente (dieta mínima: prompt A-04 + ORQUESTADOR + F5 [JSONL+vista] + F0 + F4 + DATA.md) el 2026-07-23. Archivado verbatim, append-only. **Resultado: NO CONFORME** por V-001 (incoherencia del estado del funding real frente a DATA.md). Todo lo demás de F5 verificado CONFORME. Pendiente de resolución + re-arbitraje.

```
DICTAMEN A-04
Artefacto: F5_transferencia.jsonl (30 objetos) + F5_TRANSFERENCIA.md (vista) · Ciclo C-001
Estado: ☒ NO CONFORME
────────────
✔ Regla 9 — JSONL (un objeto/entrada); MD declarada vista del JSONL (no al revés); F5 añade `transferibilidad` (7 subclaves) en las 30; conteos JSONL=MD (8 viaja/2 con_condiciones/9 no_viaja/11 n/a).
✔ Fidelidad a F4 — 30 id y 30 f4_veredicto coinciden 1:1; herencia verbatim, solo se añade transferibilidad.
✔ Cadena F5 por superviviente (mecanismo→ingredientes→cripto→costes→veredicto→datos→esfuerzo); 19 evaluados (10 sólido+9 degradado), 11 n/a.
✔ Reglas 1/2 — sin rankear/seleccionar/evaluar rentabilidad (MD: "es transferibilidad, no selección… lo decide F7"); [memoria del modelo — verificar] usada 21 veces. EXCEPCIÓN: afirmación de funding (V-001).
✔ Coherencia con DATA.md de order book ❌, OI/P3, OHLCV 2021-26, taker 0.06% — EXCEPTO funding (V-001).
✔ Fechado, ejecutor Opus, cierre no autodeclarado.
────────────
V-001 — Incoherencia/misatribución del estado del funding real frente a DATA.md (data-coherence + regla 1).
- Hecho: F5 declara el funding de carry como YA disponible atribuyéndolo a DATA.md (MD L11: "funding real 2021-26 ✅"; JSONL F1-008 datos_infra: "Funding recolectado 2021-26 por exp-008"; nota M2 "exp-008 mostró que el funding real no destruye el edge"). DATA.md NO lo sostiene y afirma lo contrario: Funding = "Modelado 0.01%/8h uniforme", "la mayor incógnita de magnitud declarada", "⚠️ Abierta; Fase B lo mide por trade", §Data Lake: "funding histórico completo… la carencia nº 1 detectada". La afirmación no está etiquetada [memoria] y se apoya en exp-008, fuera de la dieta → no verificable y contradicha por la fuente que la propia F5 cita.
C-001 (contradicción reportada): misma tensión funding F5 vs DATA.md; la resuelve el IP.
Observaciones: "no hay order book" es lectura por ausencia del inventario (razonable, no violación); "H-001 en Fase B" vs DATA.md que lo cita en Fase A (imprecisión leve, inmaterial).
────────────
Condición de levantamiento: corregir en el JSONL (fuente de verdad) y su vista el estado del funding: o alinear con DATA.md (funding real = modelado/incógnita, carencia nº 1), o aportar/citar dentro de la dieta la evidencia de la recolección y etiquetar como [memoria del modelo — verificar] toda apoyatura en exp-008 mientras no sea verificable.
Firma: A-04 · 2026-07-23 · sesión independiente
```

## Resolución (Camino 1, decisión del IP 2026-07-23) + dictamen v2 CONFORME

Raíz: `DATA.md` estaba **desactualizado** (escrito 2026-07-03, antes de que exp-008 recolectara el funding real 2021-26). Corrección aplicada (Camino 1):
1. **`DATA.md` actualizado** para reflejar exp-008 (funding real 2021-26 recolectado para los 5 símbolos de H-001, A-02 APTO, hashes congelados; R0 ACEPTABLE; el modelo uniforme queda como baseline histórico). Corrige una deuda documental real.
2. **Afirmación de F5 afinada** (JSONL F1-008 + MD): funding recolectado **para los 5 símbolos de H-001**; un universo de carry más amplio requeriría recolección adicional. 0 campos de F4 alterados.

```
DICTAMEN A-04 — v2 (re-arbitraje)
Estado: ☑ CONFORME
✔ Regla 9 (JSONL/vista/consistencia/campo transferibilidad) · ✔ Fidelidad a F4 (0 alteraciones) · ✔ Cadena F5 por superviviente · ✔ 19 evaluados + 11 n/a · ✔ Reglas 1-2 (etiquetas [memoria], sin métricas inventadas, sin ranking).
✔ CLAVE — coherencia de datos con DATA.md: funding real 2021-26 en F5 (JSONL F1-008 + MD) COINCIDE literalmente con la fila Funding y la sección Data Lake de DATA.md (recolectado solo para los 5 símbolos de H-001; universo amplio pendiente). Sin sobre-declaración.
Violaciones: ninguna. Contradicciones: ninguna.
Observaciones: O-1 F5 ejecutada en sesión directa sin subagente web (declarado; anclajes cuantitativos vienen de DATA.md y de evidencia verificada en F1-F4; lo incierto etiquetado — no es violación). O-2 "viaja_con_condiciones" vs "viaja con condiciones" (cosmético).
Firma: A-04 · 2026-07-23 · sesión independiente
```

**F5 es CONFORME.** El dictamen v1 (NO CONFORME) se conserva íntegro. **F5 CERRADA por aprobación del IP el 2026-07-23.** F6 (diseño experimental) queda desbloqueada.
