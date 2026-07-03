# Funding REAL integrado — ultima incognita cuantificable, RESUELTA

Funding historico real de Binance (5 simbolos, ~5400 registros 8h c/u, 2021-2026),
aplicado trade a trade: funding_pnl = -sign(side) * Σ fundingRate(t) * units * precio(t).

## PnL definitivo (cesta 5, risk 0.25%, fills pesimistas, FULL 2021-26)
| concepto | $ |
|---|---|
| PnL bruto | 12.561 |
| - fees | -2.815 |
| PnL neto fees | 9.746 |
| +/- funding REAL | -1.243 |
| **PnL neto fees+funding** | **8.503** (-12.8% vs neto fees) |

Funding por lado: longs -1.153$ (pagan), shorts -90$ (neutro).
=> Coherente: el sistema va largo en bull (funding positivo, longs pagan), pero
   las tendencias cubren el peaje.

## Veredicto
- El funding real es un recorte MODERADO (-12.8%), NO un asesino. Cae en el lado
  suave de la sensibilidad (~0.01%/8h neto). El edge SOBREVIVE a costes reales
  completos (fees+funding ~28% del bruto).
- El alfa baja de +11.6% a ~+10% anual: sigue positivo, sigue NO significativo.
  El funding elimina una via de muerte; no aumenta la confianza estadistica.

## Estado: incognitas cuantificables AGOTADAS
Resueltas por backtest/datos: costes, funding real, OOS, lockbox, regimen,
atribucion, correlacion, jackknife, alfa-beta, estructura de top trades.
Pendiente y NO cuantificable por backtest: EJECUCION real (slippage en vivo,
fills en el momento de las ~5 capturas clave, uptime). Solo paper + vivo.

## Clasificacion final (comite)
Hipotesis de tendencia descorrelacionada (beta 0.006), mecanismo repetible
(~14 episodios), alfa positivo ~+10% neto pero NO significativo (t<1), resultado
dominado por ~5 trades. Sobrevive a costes reales. CONFIANZA MODERADA-BAJA.
=> No archivar. No capital significativo. Sizing acorde a la confianza. Congelar
   y pasar a validacion operacional (paper fontaneria -> capital minimo).
