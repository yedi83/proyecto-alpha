# Dictamen A-04 sobre F7 — Ciclo C-001

> Producido en sesión independiente (dieta cerrada: prompt A-04 + ORQUESTADOR + F0_PROTOCOLO + F6_protocolos.jsonl + F7_COLA.jsonl + F7_COLA.md) el 2026-07-25. Archivado verbatim, append-only. **Resultado v1: NO CONFORME** (1 violación de regla dura 9 + 1 contradicción para el IP). Dieta respetada; sin contexto externo.

```
DICTAMEN A-04
Artefacto: F7 — Priorización + cola, Ciclo C-001. F7_COLA.md (vista) + F7_COLA.jsonl (fuente, 30 objetos). Insumo: F6.
Estado: ☒ NO CONFORME
────────────
[✔] R1 Regla 9: JSONL = fuente de verdad, 30 objetos (30 líneas, 30 JSON válidos, 0 vacías); el .md se declara vista (líneas 3-4); F7 añade SOLO el campo `f7` (única clave nueva verificada programáticamente) sin borrar previos.
[✔] R2 Fidelidad a F6: 0 alteraciones. Los 30 objetos conservan f6/f5/f4/... verbatim (comparación clave-a-clave excluyendo f7: 0 alteradas, 0 nuevas fuera de f7, 0 borradas).
[✗] R3 Rúbrica F0: pesos 35/30/20/10/5 y escala 0-5 correctos; aritmética reproducida EXACTA (Carry 5·.35+3·.30+3·.20+5·.10+5·.05=4.00; CEX-DEX=2.15; ILLIQ=2.15). PERO "una justificación por celda" NO se cumple en la fuente de verdad: solo el carry (F1-008/F1-009) lleva el sub-objeto `justificacion` en el JSONL; F1-013 (CEX-DEX) y F1-020 (ILLIQ) carecen de `justificacion` en el JSONL — solo tienen `puntuaciones`, `complementariedad_H001` y `estado`.
[✔] R4 Sensibilidad ±20%: presente (§2); top-1 (carry) estable — la brecha 4.00 vs 2.15 no se revierte con ±20% por peso; el empate 2.15/2.15 se declara inmaterial (ambos bloqueados). Conclusión coherente con los datos.
[✔] R5 Complementariedad SIN pesos: §3 clasifica captura + relación con H-001 (COMPLEMENTARIO/REDUNDANTE/DISTINTO); no reintroduce pesos ni inventa criterio nuevo.
[✔] R6 Salida = cola (F0 §7): candidatas quedan "CANDIDATA EN COLA"/"BLOQUEADO"/condicionadas; NO promovidas a hipótesis ni declaradas edges; umbrales/scoring declarados PROPUESTAS (líneas 4, 43) conforme regla dura 6.
[✔] R7 No sobre-afirmación: cadena "mecanismo plausible ≠ edge demostrado ≠ estrategia ejecutable" respetada explícitamente (§5, línea 43); no se hallan superlativos que declaren candidatas validadas.
[✔] R8 Fechado (2026-07-23), ejecutor declarado (Opus/Claude, sesión directa), cierre NO autodeclarado: "F7 EJECUTADA — no CERRADA. Falta dictamen A-04 (sesión independiente) + aprobación del IP" (línea 49).
[✗] R9 Coherencia JSONL↔MD: las puntuaciones y ponderados del .md reflejan el JSONL (4.00/2.15/2.15 idénticos). PERO el .md (§1) presenta celdas de justificación para CEX-DEX ("misma prima M2 + riesgo on-chain", "6 meses + survivorship de venues", etc.) y para ILLIQ ("degradado por F4 (confound tamaño)", "Amihud III...", etc.) que NO tienen respaldo alguno en la fuente de verdad JSONL — la vista carga contenido normativo (justificación de rúbrica) ausente del objeto fuente.
────────────
Violaciones:
- V-001 (regla dura 9 — fuente de verdad, + R3/R9): la vista .md contiene justificaciones por celda para 2 de las 3 candidatas puntuadas (F1-013, F1-020) que NO existen en el JSONL fuente de verdad. Norma: regla dura 9 (ORQUESTADOR) — "una vista Markdown generada a partir de él — nunca al revés" + requisito F7 (ORQUESTADOR §Prompts F7) "una línea de justificación por celda". Hecho: F1-013 y F1-020 carecen del sub-objeto `justificacion` en el JSONL; el requisito de justificación por celda solo se satisface en la vista, no en la fuente, y la vista excede a la fuente → generación en dirección inversa o fuente incompleta. Evidencia: parseo de F7_COLA.jsonl (objetos F1-013, F1-020 sin clave `justificacion`) vs F7_COLA.md §1 (celdas justificadas para ambas).
────────────
Contradicciones (reportadas, las resuelve el IP):
- C-001: el carry se puntúa en DOS objetos (F1-008 y F1-009), ambos con idéntico 4.00 y misma justificación; la narrativa (§4/§5) lo trata como "1 candidata". No es alteración de campos heredados ni error aritmético, pero conviene que el IP fije si la cola cuenta 1 candidata carry o 2 objetos puntuados equivalentes.
────────────
Observaciones: Dieta respetada — se leyeron únicamente los 6 archivos autorizados, en orden; sin web; el shell se usó solo para reproducir aritmética del scoring, contar objetos y comparar campos F6↔F7 (permitido por el prompt). No se recibió contexto fuera de la dieta. R3 y R9 fallan por la MISMA causa raíz (justificación por celda presente solo en la vista); subsanable regenerando el JSONL con el sub-objeto `justificacion` para F1-013 y F1-020, o poblando la fuente antes de derivar la vista. El resto del artefacto (fidelidad, aritmética, sensibilidad, no-sobre-afirmación, cierre no autodeclarado) es conforme.
Firma: A-04 · 2026-07-25 · sesión independiente
```

---

## Dictamen v2 (2026-07-25) — NO CONFORME

> Segundo arbitraje tras corregir la justificación del §1 y consolidar el carry (F1-008+F1-009 → unidad M2, decisión del IP). Resultado: **NO CONFORME** — la vista aún excedía a la fuente en UNA celda del §3 (mismo modo de fallo que v1, en otra ubicación). Dieta respetada.

```
DICTAMEN A-04 (v2) — Estado: NO CONFORME
Pasaron: R1 estructura, R2 fidelidad F6 (0 alteraciones), R3 rúbrica/aritmética (4.00/2.15/2.15 exactos),
R4 no doble conteo (3 unidades; F1-009 puntuada:false, consolidada_en F1-008), R5 sensibilidad, R6 complementariedad,
R7 cola, R8 no sobre-afirmación, R9 cierre no autodeclarado.
Falló: R10 coherencia JSONL↔MD. Violación V-001 (regla dura 9): la celda §3 (fila Carry) contenía la frase
"Es exactamente lo que un segundo motor debería aportar: diversificación de fuente de retorno, no otra forma de lo mismo",
ausente del JSONL (grep "fuente de retorno"/"segundo motor" en la fuente = 0). Vista excede a la fuente.
Firma: A-04 · 2026-07-25 · sesión independiente
```

**Corrección aplicada:** se añadió `f7.captura` a las 3 unidades y se completó `f7.complementariedad_H001` de F1-008 con esa frase en el JSONL; §1 y §3 se regeneraron verbatim desde la fuente; auditoría programática confirmó 0 celdas huérfanas.

---

## Dictamen v3 (2026-07-25) — CONFORME

> Tercer arbitraje tras llevar TODO el contenido de tablas (§1 y §3) al JSONL y regenerar la vista verbatim. Resultado: **CONFORME, 0 violaciones, 0 contradicciones.** Dieta respetada (leídos solo los 6 insumos; sin dictámenes previos ni web).

```
DICTAMEN A-04 (v3) — Estado: CONFORME
[✔] R1 Regla 9: JSONL fuente 30 objetos; .md vista generada desde el JSONL; F7 añade `f7` sin borrar previos.
[✔] R2 Fidelidad F6: 0 alteraciones (diff objeto-a-objeto; cada objeto añade EXACTAMENTE la clave `f7`).
[✔] R3 Rúbrica F0: pesos 35/30/20/10/5, escala 0-5; justificacion (5 criterios) en JSONL; ponderados 4.00/2.15/2.15 reproducidos exactos.
[✔] R4 No doble conteo: 3 unidades puntuadas (F1-008/F1-013/F1-020); carry M2 puntuado una vez (F1-009 puntuada:false, score null, consolidada_en F1-008); coincide con la tabla.
[✔] R5 Sensibilidad ±20%: top-1 (carry) domina en cada criterio; ninguna perturbación invierte el orden.
[✔] R6 Complementariedad SIN pesos.  [✔] R7 Salida = cola (no hipótesis, scoring = PROPUESTA).
[✔] R8 No sobre-afirmación (cadena mecanismo≠edge≠estrategia presente).  [✔] R9 Fechado, ejecutor declarado, cierre no autodeclarado.
[✔] R10 CRÍTICO: cotejo celda-a-celda §1 (15 celdas + 3 ponderados) y §3 (3 captura + 3 complementariedad) — TODAS existen verbatim en la fuente. La vista NO excede a la fuente. Defecto de v1/v2 corregido.
Violaciones: ninguna.  Contradicciones: ninguna.
Observación (menor, no bloqueante): el rótulo de fila "Arb. funding CEX-DEX" es una contracción de `f7.candidata` de F1-013 ("Arbitraje de funding CEX vs DEX") — contiene MENOS que la fuente, no la excede; el IP puede uniformarlo si desea coherencia literal.
Firma: A-04 · 2026-07-25 · sesión independiente
```

**F7 es CONFORME (v3).** Pendiente únicamente la **aprobación explícita del IP** para cerrar F7 y con ella el ciclo C-001. El cierre no se autodeclara.
