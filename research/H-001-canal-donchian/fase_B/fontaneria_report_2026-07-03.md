# Fontanería de órdenes — 2026-07-03 15:00 UTC (testnet, cuenta separada)

## F1 — Límites por símbolo (según ccxt/testnet)

| Símbolo | min notional (cost.min) | min qty (amount.min) | precisión qty |
|---|---|---|---|
| BTC/USDT:USDT | 50.0 | 0.0001 | 0.0001 |
| ETH/USDT:USDT | 20.0 | 0.001 | 0.001 |
| SOL/USDT:USDT | 5.0 | 0.01 | 0.01 |
| BCH/USDT:USDT | 5.0 | 0.001 | 0.001 |
| DOGE/USDT:USDT | 5.0 | 1.0 | 1.0 |

**Verificación M1:** si cost.min de BTC es None, el guard del bot usa default 5.0 y el rechazo lo daría el exchange (sin evento). Si es ~100, el guard del bot omitirá BTC correctamente con equity $750.

## Balance

USDT total en la cuenta de pruebas: **4995.53**

## F2 — Round-trip real (DOGE/USDT:USDT)

- qty enviada: 260.0 (redondeo amount_to_precision desde 260.858224)
- respuesta create_order: average=None price=None status=closed timestamp=1783090802618
- fetch_order: average=0.07667 filled=260.0 status=closed
- **fee inline en la orden: None** | fee sumada de fills (fetch_my_trades): 0.00797368
  (si inline es None/0 y fills>0: el bot DEBE leer fees de los fills, no de la orden — bug latente del registro)
- **F5 latencia create_order→respuesta: 254 ms**
- cierre reduce-only: status=closed | contratos abiertos tras cierre: **0**

## F3 — Rechazo controlado por min_notional (BTC/USDT:USDT, ~$50)

- rechazo capturado (la firma que el bot vería SIN generar evento):
  - tipo: `InvalidOrder`
  - mensaje: `binance {"code":-4164,"msg":"Order's notional must be no smaller than 50 (unless you choose reduce only)."}`

## F4 — fetch_funding_rate_history en testnet

- OK: 5 tramos; último rate=5.433e-05

## ✅ Cuenta plana al terminar.