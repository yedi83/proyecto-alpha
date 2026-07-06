# Análisis de operaciones — Fase A (dry run) y ensayo de Fase B

> Fecha: 2026-07-06. **Nota de análisis, NO veredicto de fase.** No modifica criterios ni el PREREG. Los datos son de **testnet/demo** (feed sintético y poco fiable): sirven para validar la máquina, no el edge.

## 1. Fase A (lab, dry run sobre testnet) — `paper/registro_live.csv`

12 operaciones cerradas + 1 abierta (BCH #7). 4 ganadoras, 8 perdedoras (win rate ~33%). **Neto ≈ +$3.49** sobre ~$750 (+0.47%).

| # | Símbolo | Lado | Net PnL | Nota |
|---|---|---|---|---|
| 1 | DOGE | short | −0.79 | |
| 2 | SOL | long | −0.88 | |
| 3 | SOL | long | −0.07 | |
| 4 | BCH | long | −0.83 | |
| 5 | DOGE | short | −0.65 | |
| 6 | BTC | short | −0.69 | |
| 9 | SOL | long | +1.18 | |
| 12 | SOL | long | −0.66 | |
| 13 | SOL | long | −0.95 | |
| 10 | BTC | long | +1.74 | hold 02→06-jul; funding +0.26 |
| 8 | ETH | long | **+5.52** | hold 02→06-jul; funding +0.51 |
| 11 | DOGE | long | +0.57 | funding +1.11 |

Observaciones:

- **Un solo trade (ETH #8, +$5.52) es mayor que todo el neto.** Las otras tres ganadoras cubren ocho pérdidas pequeñas. Perfil clásico de trend-following, consistente con el backtest real ("top-5 trades = 115% del neto"). Es una comprobación de **comportamiento**, no de edge.
- Los holds de varios días validaron la **captura de funding acumulado** (B relevante).
- BTC, ETH y DOGE salieron casi simultáneamente el 06-jul ~12:00 — probable evento del feed testnet, no tres señales independientes. Refuerza que el dato no es fiable.

## 2. Ensayo de Fase B (demo) — `ensayo_faseB/paper/registro_live.csv`

3 cerradas + BCH abierta. **Neto ≈ −$2.29**, las tres pérdidas pequeñas.

| # | Símbolo | Lado | Net PnL | Funding |
|---|---|---|---|---|
| 1 | SOL | long | −1.06 | 0.00 |
| 2 | BTC | long | −0.68 | +0.22 |
| 4 | ETH | long | −0.54 | −0.01 |

Validó: fills reales (B-fix1), fees de fills (B-fix2), funding, ciclo completo entrada→salida, y resiliencia ante `502 Bad Gateway` en `/order` + velas atrasadas sin corromper estado.

## 3. Lectura honesta

**El P&L de ambas no significa nada.** Datos testnet falsos, muestras minúsculas (12 y 3 trades), y en Fase A un solo trade carga todo el resultado. No se concluye nada de edge de aquí.

- El **edge** se validó en el backtest sobre datos reales de mainnet (VEREDICTO, exp-002/003). Estas fases live validan la **máquina** (arquitectura, entradas/salidas, funding, reconcile, resiliencia), no la estrategia.
- El valor de esa validación está **muy front-loaded**: cubierta la superficie de fallos (entrada, salida por stop y por canal, funding en hold largo, reconexión, 502, frontera de día, kill-switch), el tiempo extra sobre testnet añade más de lo mismo. Alargarlo meses sería desperdicio.
- Lo que justifica un **mínimo** (no indefinido) no es el tiempo sino la **cobertura de eventos**: el Donchian512 opera lento, así que se necesitan días para acumular suficientes entradas/salidas y cruces de funding. Un mínimo modesto es seguro barato contra bugs raros; estirarlo, no.
- Lo que ninguna fase testnet valida por mucho que se alargue: la **brecha testnet↔mainnet** (slippage, latencia, liquidez, funding real, mínimos de notional — B-fix4). Eso solo lo prueba **Fase C** con dinero real. Ahí sí "dejarlo mucho tiempo" gana su sueldo, porque mide edge y fricción reales.

## 4. Recomendación

Definir el cierre de Fase A por **cobertura de criterios + tipos de evento** (ya casi completa), cumpliendo el mínimo pre-registrado por gobernanza, con el replay y los 6 criterios — **no por calendario por inercia**. No usar el P&L testnet como señal (falsa confianza / falsa alarma). Reservar el tiempo largo para Fase C.
