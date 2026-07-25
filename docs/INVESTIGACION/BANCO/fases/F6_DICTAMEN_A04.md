# Dictamen A-04 sobre F6 — Ciclo C-001

> Producido en sesión independiente (dieta: prompt A-04 + ORQUESTADOR + F6_protocolos.jsonl + F6_PROTOCOLOS.md + F6_PROTOCOLOS_6a.md + F6_AMENAZAS_6b.md + F5 + F0) el 2026-07-23. Archivado verbatim, append-only. **Resultado: CONFORME.** Reportó una contradicción menor (C-001) que el IP resolvió por alineación de consistencia (ver "Resolución"). El árbitro verificó explícitamente los **10 aspectos** que el IP pidió escrutar.

```
DICTAMEN A-04
Artefacto: F6 — Diseño experimental (fusión 6a + 6b), Ciclo C-001. F6_PROTOCOLOS.md (vista) + F6_protocolos.jsonl (fuente de verdad, 30 objetos) + F6_PROTOCOLOS_6a.md + F6_AMENAZAS_6b.md. Insumo: F5.
Estado: ☑ CONFORME
────────────
✔ R1 Regla 9 (JSONL 30 objetos/uno por entrada; MD declarada vista; F6 añade `f6`; 30=30).
✔ R2 Alcance: solo candidatas que viajan (F5), cotejado exacto. ✔ R3 Persistencia=H-001 sin protocolo nuevo. ✔ R4 Bocetos con prerrequisito.
✔ R5 6a: los 7 elementos de F0 §6. ✔ R6 6b: sesión adversarial declarada, sin contexto de 6a, el diseñador no se revisa.
✔ R7 (F0 §3c COMPUERTA): las 16 AC + AX-1/2 + AI-1/2 incorporadas como prueba o limitación; cotejo una a una completo; ninguna quedó fuera.
✔ R8 Ninguna amenaza neutralizada por reformulación cosmética (AC-7 reescribe la hipótesis a funding conocido en t + auditoría replay; AC-8 declara Sharpe=límite superior).
✔ R9 Pruebas ejecutables y falsables. ✔ R10 Limitaciones bloqueantes (🔒) separadas de pruebas (⚠️).
✔ R11 No adelanta F7 (sin scoring/selección; "no es priorización — eso es F7"). ✔ R12 Mecanismo ≠ edge ≠ estrategia (textual). ✔ R13 Evidencia insuficiente ≠ refutación (AC-15).
✔ R14 JSONL↔MD fieles (con salvedad C-001). ✔ R15 F6 no altera F5 (0 diferencias). ✔ R16 Sin ranking encubierto (superlativos califican amenazas, no candidatas; no aparece "el mejor candidato").
✔ R17 Fechado, ejecutor declarado, cierre no autodeclarado.
────────────
Violaciones: ninguna.
Contradicciones (reportadas, las resuelve el IP):
C-001 — Clasificación divergente MD↔JSONL en AC-11/AC-14/AC-15 y uso de la etiqueta "AJUSTE" (tercera categoría ajena al binario prueba/limitación de F0 §3c). Las tres ESTÁN incorporadas y son sustantivas (compuerta satisfecha); solo su tipificación no era coherente entre artefactos.
Observaciones: 6b no nombra el modelo (no exigido); F1-020 tratada como M2 por reasignación de F4 mientras F5 conserva mecanismo=Microestructura (no es alteración de F5 — herencia de F4).
Firma: A-04 · 2026-07-23 · sesión independiente
```

## Resolución de C-001 (alineación de consistencia, 2026-07-23)

Se unificó la clasificación de AC-11/AC-14/AC-15 entre la vista y el JSONL, y se eliminó la etiqueta "AJUSTE" (ajena a F0 §3c): las tres quedan como **PRUEBA** (AC-14/15 como "PRUEBA (ajuste de criterio)"; AC-11 como PRUEBA de estrés sintético — su limitación de cola censurada la cubre AC-8). En el JSONL, AC-11 pasó de `limitaciones` a `pruebas`. Total invariable: **16 amenazas del carry = 11 pruebas + 5 limitaciones.** F5 intacto (0 alteraciones). Sin re-arbitraje: solo se alinearon etiquetas que el propio A-04 señaló; ningún veredicto ni contenido cambió.

**F6 es CONFORME. CERRADA por aprobación explícita del IP el 2026-07-23.** F7 (priorización + cola) queda desbloqueada.
