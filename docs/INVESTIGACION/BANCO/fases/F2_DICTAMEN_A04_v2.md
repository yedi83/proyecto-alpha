# Dictámenes A-04 sobre F2 — re-arbitrajes (Ciclo C-001)

> Rastro append-only de los dos re-arbitrajes posteriores al dictamen v1 (`F2_DICTAMEN_A04.md`, NO CONFORME por V-001 = falta del JSONL). Secuencia: v1 NO CONFORME (JSONL) → se produjo `F2_arbol.jsonl` → **v2 NO CONFORME** (frase de ranking) → se corrigió la frase + se alineó el campo redundante → **v3 CONFORME**. Cada dictamen se produjo en sesión independiente aislada (dieta mínima). Los tres se conservan íntegros.

---

## Dictamen v2 (re-arbitraje tras producir el JSONL) — NO CONFORME

> Diete: A-04 + ORQUESTADOR + F2_arbol.jsonl + F2_ARBOL.md + F0 + F1. Resultado: NO CONFORME por V-001 (frase comparativa que jerarquiza mecanismos). El JSONL/regla 9 quedó verificado CONFORME en este dictamen (V-001 del v1, levantada).

```
DICTAMEN A-04 — v2
Estado: NO CONFORME
Verificado CONFORME: regla 9 (JSONL existe, un objeto por entrada; MD declarada vista del JSONL; consistencia), fidelidad a F1 (0 campos alterados), estructura árbol, reglas 1-4, fechado, ejecutor, cierre no autodeclarado.
V-001 — Norma (prompt F2: "No hay pesos, ranking ni selección de candidatas (eso es F7)"; regla 10: el ejecutor "no prioriza"). Hecho: la tabla de herencia (celda M1) concluía "El caso más fuerte del ciclo" — juicio comparativo que ordena mecanismos por superioridad, excede el mandato de F2 y contradice su propia Nota 2.
C-001 (contradicción reportada): la vista enumeraba 4 campos F2 pero el JSONL contenía además `nivel_individual` (duplicado de `nivel_evidencia_preliminar`).
Condición de levantamiento: eliminar/reformular la frase "El caso más fuerte del ciclo" sin ordenar mecanismos; alinear la enumeración de campos con el JSONL.
Firma: A-04 · 2026-07-20 · sesión independiente
```

**Remediación aplicada (2026-07-20):** (1) celda M1 reformulada a descripción de volumen/independencia de evidencia con disclaimer explícito "(El ordenamiento entre mecanismos es F7, no F2.)"; (2) campo redundante `nivel_individual` eliminado del JSONL (los 4 campos F2 = `tipo_F2`, `nivel_consolidado_mecanismo`, `frontera`, `mecanismo_provisional` coinciden ahora con la enumeración de la vista; fidelidad a F1 re-verificada: 0 alteraciones).

---

## Dictamen v3 (re-arbitraje tras la remediación) — CONFORME

```
DICTAMEN A-04
Artefacto evaluado: F2_ARBOL.md + F2_arbol.jsonl — Fase F2 (Árbol genealógico por mecanismos), Ciclo C-001, fechado 2026-07-20, ejecutor Opus.
Estado: ☒ CONFORME
────────────
✔ Regla 9 — JSONL existe (30 objetos, uno por entrada).
✔ Regla 9 — vista declarada generada DESDE el JSONL (no al revés).
✔ Regla 9 — consistencia JSONL↔MD (entradas y valores; M2=II-III, M3=II, M4=III, M5="método I-II/alfa n/a").
✔ Regla 9 — enumeración de campos F2 de la vista coincide con el JSONL (tipo_F2, nivel_consolidado_mecanismo, frontera, mecanismo_provisional).
✔ Fidelidad a F1 — 11 campos F1 reproducidos verbatim (incl. observaciones largas y objeto frontera); nada inventado ni ausente. "0 alteraciones" consistente.
✔ Estructura MECANISMO→FAMILIA→VARIANTE.
✔ Regla 1 — agrupamiento por ineficiencia.
✔ Regla 2 — herencia + tabla, edge vs teoría/método, no-promediado, sin pesos.
✔ Regla 3 — casos frontera F1-018/020/022 con doble ubicación sin forzar; concuerda con frontera del JSONL.
✔ Regla 4 — mecanismo_provisional:true en las 30.
✔ Regla 10 — sin priorización/ranking/selección; disclaimer "(El ordenamiento entre mecanismos es F7, no F2.)"; complementariedad diferida a F7.
✔ Documento fechado; ejecutor declarado (Opus); cierre no autodeclarado.
────────────
Violaciones: (vacío)
Contradicciones: (ninguna que altere valores de F1)
Observaciones:
- O-1 (regla 9, menor): la vista introduce subdivisiones de FAMILIA (M2: carry general vs. carry/funding perp cripto; M4: order flow vs. iliquidez/toxicidad) más finas que el campo `familia` del JSONL (uniforme "Carry / funding" y "Order flow / liquidez"). No altera ni contradice valores; granularidad narrativa. Se registra.
- O-2 (fuera de dieta): la vista refiere a H-001 como "Donchian 512" mientras F1-007 dice "Donchian 20/55"; objetos distintos (implementación del lab vs variante canónica), H-001 fuera de dieta; sin efecto sobre fidelidad.
Firma: A-04 · 2026-07-20 · sesión independiente
```

## Efecto

**F2 es CONFORME** tras dos remediaciones (JSONL producido; frase de ranking eliminada). Los dictámenes v1 (NO CONFORME) y v2 (NO CONFORME) se conservan íntegros — no se borran. **F2 CERRADA por aprobación del IP el 2026-07-20.** Observación O-1 (subdivisión de familia en la vista) y la contradicción C-001 del ORQUESTADOR (regla 9 vs. tabla/prompt) → registradas como pendientes para el F0 del C-002 (regla de inmutabilidad). **F3 desbloqueada.**
