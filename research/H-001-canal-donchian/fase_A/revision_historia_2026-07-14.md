# Revisión de la historia de Fase A — 2026-07-14 (pre-cierre)

> Sesión Fable 5, solo lectura. NO es el veredicto: es la evaluación provisional por criterio + los pasos exactos que faltan para sellar el informe de cierre. El mínimo de 10 días se cumplió el 2026-07-12 03:53 UTC — la fase es elegible para cierre.

## La historia en números (2026-07-02 03:53 → 2026-07-14)

- **12+ días de operación continua**, ciclos de 15 min ininterrumpidos salvo el episodio del 07-11 (abajo). Vigía activo desde el 07-03 (965 líneas de log, "OK" a cadencia de 15 min).
- **Trades cerrados post-corte: #8–#22** (~15) + entrada SOL short del 07-13 aún abierta. Todos con señal→evento→registro coherentes en los cruces manuales del diario.
- **El hito de la fase (07-08):** salida del trade #7 (LONG BCH que cruzaba el corte, la prueba definida en el acta) — cerrado @234.46, evento + log con timestamp idéntico, latencia 8.5 s, net +5.91$. **La verificación pendiente del acta quedó satisfecha.**
- **Incidente mayor (07-11, 03:45–~06:00 UTC):** ráfaga de 20 `NetworkError` contra el feed testnet (~2.5 h sin klines). El bot **se recuperó solo** reintentando por diseño, sin intervención, sin pérdida de estado — el comportamiento exacto que la especificación promete. Es el criterio C3 funcionando, no fallando… siempre que quede documentado en el diario (hoy NO está).
- **Velas atrasadas:** fenómeno del feed testnet, ya diagnosticado y cerrado el 07-09 (retraso constante de 2 velas, lógica idempotente, 0 omisiones, cruce 10/10; alarma ajustada con `--smart-atrasadas`). Corroborado externamente por paper_real: el feed mainnet tiene ~40% de la tasa.
- **⚠️ Incidente de HOY (07-14 11:42 UTC):** el vigía alertó "heartbeat frío 27 min + 1 NetworkError". Mi vista del log llega hasta ayer (caché); **hay que verificar en la máquina** si fue un blip recuperado o si el bot está detenido ahora.

## Evaluación provisional por criterio

| # | Criterio | Estado provisional | Qué falta |
|---|---|---|---|
| C1 | Toda señal → evento | 🟡 Evidencia manual favorable (2 salidas validadas: #7 el 07-08 y #19 el 07-10; cruce 10/10 el 07-09) | **El replay** es la verificación exhaustiva |
| C2 | Toda operación → señal | 🟡 Cruces manuales limpios | El replay |
| C3 | Cero errores críticos | 🟢 Outage del 07-11 recuperado solo; sin reinicios no recuperados; estado íntegro (verificado 07-10) | Verificar la alerta de HOY + fila de diario del 07-11 |
| C4 | Latencia mediana <30 s | 🟢 Muestras manuales 7–15 s en toda la fase | El replay da mediana/p95 formales |
| C5 | Atrasadas explicadas | 🟢 Causa diagnosticada, cerrada y hasta corroborada con feed alterno | El replay clasifica las señales perdidas si las hay |
| C6 | Divergencias con causa antes de B | 🟡 Sin divergencias abiertas conocidas | **Diario incompleto: faltan filas 07-11 → 07-14** (el criterio exige diario al día) |

**Lectura honesta:** todo apunta a APRUEBA — pero el veredicto no existe hasta que el replay corra y el diario esté completo. "Casi pasa" también aplica al papeleo.

## Pasos para concluir (en orden, en la máquina)

1. **Verificar la alerta del vigía de hoy:** `Get-Content bot.log -Tail 5` + hora UTC → si el bot late, anotar blip; si está caído, relanzar y anotar (caída recuperada no viola C3).
2. **Completar el diario (filas propuestas abajo — revisar y pegar).**
3. **Correr el replay:** `python "D:\PIC\Proyecto Investigación cuantitativa PIC\proyecto-alpha\research\H-001-canal-donchian\fase_A\replay_offline.py"`
4. Rellenar `informe_cierre_faseA_BORRADor.md` con el informe del replay + este documento, marcar los 6 criterios, sellar veredicto.
5. Registrar la decisión en `CRITERIOS_FASES.md` (tabla de decisiones) y el diario. Si APRUEBA → día D con el checklist del PAQUETE_FASE_B. Recordar la primera revisión de TEORIA.md ("¿qué aprendimos?").

## Borradores de filas para el DIARIO (verificar antes de pegar; las escribe el humano)

> | 2026-07-11 | Sí | Ráfaga de 20 NetworkError contra klines testnet (03:45–~06:00 UTC, ~2.5 h sin feed). Recuperación automática por reintentos, sin intervención, sin pérdida de estado ni reinicio del lanzador — comportamiento según especificación. Después: trade #20 ETH long (18:45→23:00, stop). 8/7/5/7 atrasadas en BCH/DOGE/ETH/SOL. | Ninguna pendiente. Evidencia C3: caída de feed recuperada sola. |
> | 2026-07-12 | Hito | **03:53 UTC: se cumple el mínimo de 10 días de la fase.** Operación normal: trade #21 SOL short (00:45→03:15, stop). 2 atrasadas. | Fase elegible para cierre; se decide cerrar tras replay. |
> | 2026-07-13 | No | Trade #22 ETH long (00:15→00:45, stop). Entrada SOL short 13:45 (abierta). Atrasadas dispersas (4 BCH, 2 DOGE). | Ninguna. |
> | 2026-07-14 | Sí | Alerta del vigía 11:42 UTC: heartbeat frío 27 min + 1 NetworkError. Verificación en máquina: ____ (blip recuperado / caída relanzada a las ____). | Anotar resolución. Cierre de fase en curso. |
