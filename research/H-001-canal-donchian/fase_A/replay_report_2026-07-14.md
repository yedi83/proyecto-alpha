# Replay offline — Fase A (corte 2026-07-02T03:53:46+00:00 → 2026-07-14 12:39 UTC)

Señales/salidas esperadas por el modelo: **36** · eventos del bot: **36**

| Criterio PREREG | Resultado | Detalle |
|---|---|---|
| C1 señal→evento | ✅ CUMPLE | 0 sin evento; 0 explicadas por vela atrasada |
| C2 evento→modelo | ✅ CUMPLE | 0 sin respaldo del modelo |
| C4 latencia | ✅ CUMPLE | mediana 8.7s · p95 14.9s · n=36 |
| C5 atrasadas | ℹ️ 104 eventos — revisar diario | por símbolo: {'BCH/USDT:USDT': 37, 'DOGE/USDT:USDT': 24, 'ETH/USDT:USDT': 21, 'SOL/USDT:USDT': 19, 'BTC/USDT:USDT': 3} |

(C3 caídas/estado y C6 diario se verifican manualmente: bot.log, vigia.log, DIARIO_FASE_A.md)

## Divergencias

Ninguna. Instrumentación coherente con el modelo en todo el período.
