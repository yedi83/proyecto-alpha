# Checklist Nivel 3 — Línea base (2026-07-03, día 1.5 de Fase A)

> Primera pasada del checklist de MONITOREO.md, en modo solo lectura. No es la revisión semanal formal (esa toca el domingo); es la verificación de que la instrumentación registra lo que la fase necesita. Hora de la revisión: 2026-07-03 ~13:45 UTC.

## Resultados por ítem

| # | Ítem | Resultado |
|---|---|---|
| 1 | TE dashboard | No evaluado (1.5 días, n=1 trade cerrado post-corte). Recordatorio vigente: en DRY el TE tiene sesgo positivo ≈ +fees modeladas |
| 2 | Tasa de omisión | ✅ 0 omitidas / 4 ejecutadas post-corte (ETH, SOL, BTC long 07-02; DOGE long 07-03). Sin eventos min_notional |
| 3 | Velas atrasadas | ✅ 0 post-corte |
| 4 | Latencias señal→registro | ✅ Entradas: 7.5–15 s tras cierre de vela (criterio: mediana <30 s). Salida SOL: 14.8 s |
| 5 | Continuidad del vigía | 🔴 **vigia.log NO EXISTE** → el Nivel 1 de monitoreo no está corriendo (ver hallazgo H2) |
| 6 | Diario | Filas del 07-02 correctas. Falta añadir hallazgos de hoy (H1, H2) |
| 7 | ¿Investigación necesaria? | Sí: H1 (heartbeat) — inmediata |

## Verificaciones adicionales (acta de inicio)

- ✅ Trade #7 (LONG BCH) íntegro en `bot_state.json`: entry=204.54, atr=1.3493, qty=0.185 — exactamente lo que el acta exigía.
- ✅ Cero errores en bot.log post-corte (los 9 ERROR existentes son pre-corte: 06-25/06-26, ya históricos).
- ✅ Cruce eventos↔estado consistente: cada posición abierta tiene su evento de señal con vela y precio coherentes.
- ✅ Riesgo dentro de límites: 4 posiciones abiertas (todas long) → riesgo agregado 0.4% ≤ cap 0.6%; queda espacio para 1 más.
- ℹ️ Cartera 100% long en este momento — direccional transitoriamente; sin regla violada (la neutralidad es propiedad de largo plazo).

## HALLAZGOS

### H1 — ✅ RESUELTO: falsa alarma por caché de lectura (2026-07-03 ~13:50 UTC)

La vista de esta sesión mostraba bot.log hasta las 12:30 UTC; la verificación **en la máquina** mostró el ciclo de las **13:45:12 UTC** en horario (cadencia 15 min intacta). El bot nunca dejó de latir. **Lección metodológica registrada:** la vista de archivos de estas sesiones de auditoría puede atrasarse >1 h en archivos de cambio frecuente → las sesiones remotas solo auditan en frío; la detección en caliente es responsabilidad exclusiva del vigía local (refuerza H2). Procedimiento de verificación usado: `Get-Content bot.log -Tail 3` + `[DateTime]::UtcNow` comparando contra cadencia de 15 min.

### H2 — 🔴 El vigía (Nivel 1) no está operativo

`bot/logs/vigia.log` no existe → la tarea programada de vigia.py no se registró o nunca corrió. Precisamente H1 es el tipo de evento que el vigía habría alertado en ≤15 min. **Acción: registrar la tarea** (comando exacto en MONITOREO.md, schtasks cada 15 min) y **anotar en el diario** que entre el 02-jul y hoy el Nivel 1 no estuvo activo (los Niveles 2 y 3 sí cubren el período: bot.log + eventos.csv están íntegros, así que no se perdió evidencia de fase — se perdió velocidad de alerta).

## Sugerencia de fila para DIARIO_FASE_A.md (la escribe el humano, no esta sesión)

> | 2026-07-03 | Sí | Checklist línea base: instrumentación OK (latencias 7-15s, 0 omitidas, 0 atrasadas, estado íntegro, 0 errores post-corte). Hallazgo real: vigia.py sin registrar en el Programador (Nivel 1 inactivo desde inicio de fase). Falsa alarma descartada: heartbeat verificado vivo en máquina (ciclo 13:45 UTC); el lector remoto veía log con ~75 min de caché. | Registrar tarea del vigía (schtasks, comando en MONITOREO.md) y confirmar mañana que vigia.log existe y escribe OK. |
