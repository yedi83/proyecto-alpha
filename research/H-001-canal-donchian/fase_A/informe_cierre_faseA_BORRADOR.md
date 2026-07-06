# Informe de cierre — Fase A (H-001 Canal Donchian) — BORRADOR / PLANTILLA

> **Plantilla para rellenar el 2026-07-12** (o cuando se cumplan ≥10 días + los 6 criterios). Gobernada por `prereg/PREREG_FASE_AB.md`. **No es un veredicto** hasta rellenarla y sellarla el día de cierre. Borrador escrito el 2026-07-06 (con Opus recomendado para el juicio de cierre).

## 0. Procedimiento de cierre (en orden, en la máquina del bot)

1. Correr `python research/H-001-canal-donchian/fase_A/replay_offline.py` → genera el informe de replay (tabla C1/C2/C4/C5) y, si hay, `replay_divergencias.csv`.
2. Evaluar los 6 criterios con: informe de replay (C1/C2/C4/C5), `bot.log` + `vigia.log` (C3), `DIARIO_FASE_A.md` (C6).
3. Rellenar este informe: veredicto por criterio con evidencia enlazada.
4. Registrar la decisión en `docs/VALIDACION/CRITERIOS_FASES.md` y en el diario.
5. Si REPRUEBA: causa raíz, corrección documentada y decisión de reinicio de reloj (PREREG §"Regla de cambios"). **No pasar a B.**

## 1. Datos de la fase (rellenar)

- Corte de comparabilidad: **2026-07-02 03:53:46 UTC** (verificado en log).
- Fecha/hora de cierre: __________ UTC.
- Días de calendario transcurridos: ____ · **Requisito: ≥10** (elegible desde 2026-07-12).
- Símbolos activos: BTC, ETH, SOL, BCH, DOGE (5).
- Nº de señales / salidas en el período (contexto, **no** criterio): ____.
- Evaluador / modelo: ____.

## 2. Verificación del reinicio (ACTA de inicio)

Del PREREG: el primer ciclo post-reinicio debía mostrar `abiertas=1` y mantener el trade #7 (LONG BCH) con `entry=204.54, atr=1.3493, qty=0.185` intactos (si no → corrupción de estado → aborto).

- [ ] Estado íntegro verificado en la línea base (`checklist_2026-07-03_linea_base.md`, ya confirmado ✅ el 2026-07-03 — enlazar).
- Trade #7: entrada **pre-corte** (no cuenta para métricas de entrada); su **salida** sí cuenta como evidencia de instrumentación (evento de salida, latencia, coherencia stop/reversa). Salida registrada: ____.

## 3. Evaluación de los 6 criterios (rellenar el día de cierre)

**Todos obligatorios. Uno que reprueba = la fase reprueba** ("casi pasa = no pasa").

| # | Criterio (PREREG) | Fuente de evidencia | Veredicto | Detalle / nº |
|---|---|---|---|---|
| C1 | Ninguna señal del modelo queda sin evento (ejecutada / omitida / descartada, con motivo) | Informe replay (fila C1) + `replay_divergencias.csv` | [ ] APRUEBA [ ] REPRUEBA | ____ sin evento |
| C2 | Ninguna operación ejecutada carece de señal previa correspondiente | Informe replay (fila C2) | [ ] APRUEBA [ ] REPRUEBA | ____ sin respaldo |
| C3 | Cero errores críticos de proceso (caída no recuperada por el lanzador, pérdida de estado no reconciliada, corrupción de registros) | **Manual**: `bot.log` (reinicios del lanzador), `vigia.log`, `bot_state.json` | [ ] APRUEBA [ ] REPRUEBA | ____ |
| C4 | Latencia **mediana** señal→registro **< 30 s** (medida contra el cierre real = ts_señal + 15 min) | Informe replay (fila C4: mediana + p95) | [ ] APRUEBA [ ] REPRUEBA | mediana ____ s · p95 ____ s · n ____ |
| C5 | Toda vela atrasada queda explicada por los registros de eventos | Informe replay (fila C5) + diario | [ ] APRUEBA [ ] REPRUEBA | ____ eventos |
| C6 | Toda divergencia detectada tiene causa identificada y documentada **antes** de iniciar la Fase B | **Manual**: sección "Divergencias" del replay + diario | [ ] APRUEBA [ ] REPRUEBA | ____ |

Recordatorio de interpretación (PREREG): **PnL, tracking error y win-rate NO son criterios de Fase A**. En DRY_RUN el TE tiene sesgo positivo estructural (registro con fees=0). No se toca código para "arreglarlo" durante la fase. (Ver nota `analisis_2026-07-06_operaciones_A_B.md`: el P&L testnet es ruido, no evidencia.)

## 4. Criterios de aborto (confirmar que ninguno quedó pendiente)

- [ ] **Operación ejecutada que el modelo nunca señaló** — no ocurrió.
- [ ] **Corrupción de estado** (`bot_state.json` ilegible/inconsistente) — no ocurrió.
- [ ] **Divergencias repetidas sin causa identificable** — no ocurrió.
- [ ] **Pérdida de sincronización bot↔exchange** — no ocurrió.

(Si alguno se disparó y se gestionó durante la fase: enlazar el registro, la corrección y la decisión de reinicio de reloj. Abortar no es fracasar: es el sistema de medición funcionando.)

## 5. Veredicto final (rellenar y sellar)

- [ ] **APRUEBA** — los 6 criterios cumplen y ningún aborto quedó pendiente → proceder al **DÍA D de Fase B** siguiendo el checklist de `fase_B/PAQUETE_FASE_B.md` §5.
- [ ] **REPRUEBA** — ≥1 criterio no cumple → causa raíz: ____ · corrección: ____ · decisión de reinicio de reloj: ____ · **NO pasar a B**.

Sello: ____________ · Fecha/hora UTC: ____________

## 6. Evidencia a adjuntar / enlazar

- Informe generado por `replay_offline.py` (y `replay_divergencias.csv` si hubo divergencias).
- Ventana de `bot.log` del período (reinicios del lanzador, errores) — C3.
- `vigia.log` (continuidad del Nivel 1) — C3.
- `DIARIO_FASE_A.md` (filas del período; hallazgos C3/C6).
- Nota `analisis_2026-07-06_operaciones_A_B.md` (contexto de operaciones; el P&L testnet no es criterio).
