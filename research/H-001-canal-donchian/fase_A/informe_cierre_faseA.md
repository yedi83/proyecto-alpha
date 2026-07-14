# Informe de cierre — Fase A (H-001 Canal Donchian) — **SELLADO: APRUEBA**

> Gobernado por `prereg/PREREG_FASE_AB.md`. Plantilla del 2026-07-06; evaluado y sellado el **2026-07-14** con el replay de la fase completa (36/36, 0 divergencias). Veredicto: **APRUEBA 6/6**.

## 0. Procedimiento de cierre (en orden, en la máquina del bot)

1. Correr `python research/H-001-canal-donchian/fase_A/replay_offline.py` → genera el informe de replay (tabla C1/C2/C4/C5) y, si hay, `replay_divergencias.csv`.
2. Evaluar los 6 criterios con: informe de replay (C1/C2/C4/C5), `bot.log` + `vigia.log` (C3), `DIARIO_FASE_A.md` (C6).
3. Rellenar este informe: veredicto por criterio con evidencia enlazada.
4. Registrar la decisión en `docs/VALIDACION/CRITERIOS_FASES.md` y en el diario.
5. Si REPRUEBA: causa raíz, corrección documentada y decisión de reinicio de reloj (PREREG §"Regla de cambios"). **No pasar a B.**

## 1. Datos de la fase (rellenar)

- Corte de comparabilidad: **2026-07-02 03:53:46 UTC** (verificado en log).
- Fecha/hora de cierre: **2026-07-14 12:39 UTC** (momento del replay).
- Días de calendario transcurridos: **12.4** · **Requisito: ≥10** ✅ (elegible desde 2026-07-12).
- Símbolos activos: BTC, ETH, SOL, BCH, DOGE (5) — 1 722 velas por símbolo en el período.
- Nº de señales / salidas en el período (contexto, **no** criterio): **36 del modelo = 36 eventos del bot**.
- Evaluador: replay offline (`replay_report_2026-07-14.md`) + `revision_historia_2026-07-14.md` + sesión Fable 5; **sella el Investigador Principal**.

## 2. Verificación del reinicio (ACTA de inicio)

Del PREREG: el primer ciclo post-reinicio debía mostrar `abiertas=1` y mantener el trade #7 (LONG BCH) con `entry=204.54, atr=1.3493, qty=0.185` intactos (si no → corrupción de estado → aborto).

- [x] Estado íntegro verificado en la línea base (✅ 2026-07-03) y re-verificado en máquina el 07-10 (ESTADO OK; el error de lectura remota fue caché).
- Trade #7: entrada **pre-corte** (no cuenta para métricas de entrada); su **salida** sí cuenta como evidencia de instrumentación. **Salida registrada: 2026-07-08 08:45:08 UTC @234.46 (stop, qty 0.185), evento y bot.log con timestamp idéntico, latencia 8.5 s, net +5.91$** (diario 07-08). ✅ La verificación clave del acta quedó satisfecha.

## 3. Evaluación de los 6 criterios (rellenar el día de cierre)

**Todos obligatorios. Uno que reprueba = la fase reprueba** ("casi pasa = no pasa").

| # | Criterio (PREREG) | Fuente de evidencia | Veredicto | Detalle / nº |
|---|---|---|---|---|
| C1 | Ninguna señal del modelo queda sin evento | Replay 2026-07-14 | [x] **APRUEBA** | **0 sin evento** (36/36); 0 necesitaron explicación por vela atrasada |
| C2 | Ninguna operación sin señal previa | Replay 2026-07-14 | [x] **APRUEBA** | **0 sin respaldo**; cruce con registro_live limpio |
| C3 | Cero errores críticos de proceso | bot.log + vigia.log + estado | [x] **APRUEBA** (sujeto a §3b) | Único episodio: outage de feed 07-11 (20 NetworkError, 03:45–06:00 UTC) **recuperado automáticamente**, sin intervención, sin pérdida de estado — resiliencia según especificación. 0 caídas no recuperadas; vigía continuo desde 07-03 |
| C4 | Latencia mediana < 30 s | Replay 2026-07-14 | [x] **APRUEBA** | **mediana 8.7 s · p95 14.9 s · n=36** — margen 3.4× sobre el umbral |
| C5 | Velas atrasadas explicadas | Replay + diario | [x] **APRUEBA** | 104 eventos, todos del fenómeno del feed testnet con **causa raíz diagnosticada y cerrada el 07-09** (retraso 2 velas, lógica idempotente, 0 omisiones); corroborado con feed alterno (paper_real ≈40% de la tasa). BCH 37 · DOGE 24 · ETH 21 · SOL 19 · BTC 3 |
| C6 | Divergencias con causa documentada antes de B | Replay + diario | [x] **APRUEBA** (sujeto a §3b) | Divergencias del replay: **NINGUNA** en todo el período |

### §3b — Confirmaciones previas al sello: RESUELTAS

1. [x] Alerta del vigía del 2026-07-14 11:42 UTC: **blip de feed recuperado solo** — vigia.log muestra OK a las 12:27 y 12:42 (lectura directa del disco, líneas 967-968). Nota adicional: gap del vigía 00:27→10:57 (PC inactivo); el replay, corrido después y cubriendo toda la fase, confirma 0 señales del modelo perdidas en esa ventana.
2. [x] Diario completo: filas 07-11 → 07-14 añadidas (sesión Fable a instrucción del IP, 2026-07-14) y filas "(verificar)" del 07-04→07-10 confirmadas por el IP en la fila de cierre.

Recordatorio de interpretación (PREREG): **PnL, tracking error y win-rate NO son criterios de Fase A**. En DRY_RUN el TE tiene sesgo positivo estructural (registro con fees=0). No se toca código para "arreglarlo" durante la fase. (Ver nota `analisis_2026-07-06_operaciones_A_B.md`: el P&L testnet es ruido, no evidencia.)

## 4. Criterios de aborto (confirmar que ninguno quedó pendiente)

- [x] **Operación ejecutada que el modelo nunca señaló** — no ocurrió (replay C2: 0 en 36).
- [x] **Corrupción de estado** — no ocurrió (verificaciones 07-03 y 07-10; recuperación íntegra tras el outage del 07-11).
- [x] **Divergencias repetidas sin causa identificable** — no ocurrió (replay: 0 divergencias; único fenómeno repetido —velas atrasadas— con causa raíz cerrada el 07-09).
- [x] **Pérdida de sincronización bot↔exchange** — no aplica en DRY (sin órdenes); estado interno consistente todo el período.

(Si alguno se disparó y se gestionó durante la fase: enlazar el registro, la corrección y la decisión de reinicio de reloj. Abortar no es fracasar: es el sistema de medición funcionando.)

## 5. Veredicto final (rellenar y sellar)

- [x] **APRUEBA** — los 6 criterios cumplen y ningún aborto quedó pendiente → proceder al **DÍA D de Fase B** siguiendo el checklist de `fase_B/PAQUETE_FASE_B.md` §5.
- [ ] ~~REPRUEBA~~

Sello: **Investigador Principal (Yeison Díaz), por instrucción explícita transcrita en sesión ("haz todo lo anterior por mí"); ejecución material: sesión Fable 5** · Fecha/hora UTC: **2026-07-14 ~12:50**

## 6. Evidencia a adjuntar / enlazar

- Informe generado por `replay_offline.py` (y `replay_divergencias.csv` si hubo divergencias).
- Ventana de `bot.log` del período (reinicios del lanzador, errores) — C3.
- `vigia.log` (continuidad del Nivel 1) — C3.
- `DIARIO_FASE_A.md` (filas del período; hallazgos C3/C6).
- Nota `analisis_2026-07-06_operaciones_A_B.md` (contexto de operaciones; el P&L testnet no es criterio).
