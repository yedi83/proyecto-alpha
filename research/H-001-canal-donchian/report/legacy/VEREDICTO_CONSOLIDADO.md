# Veredicto consolidado — Donchian 512 (15m) sobre cesta cripto

## El recorrido (qué se probó y qué murió)
1. Costes reales (Zoomex 0.06%/lado): mato el churn de 20 velas. Donchian 512 opera poco.
2. In-sample 6 activos: ETH/SOL/DOGE con alfa; BTC sin alfa; BCH/HYPE muertos.
3. Funding pesimista + fills peores: ETH/SOL aguantan; DOGE marginal.
4. Jackknife por trade: ETH/SOL sobreviven sin sus 2 mejores; DOGE no -> fuera.
5. Idea del "vigia" de tendencia: MEDIDA y descartada (alta tendencia rinde igual/peor).
6. Otra ventana 2021-2023 (no vista): alfa positiva en los 5 -> el edge no era solo 2024-26.
   PERO los ganadores ROTAN por regimen -> el objeto robusto es la CESTA, no monedas.
7. Cesta capital compartido: alfa positiva todas las ventanas, pero DD -63% (correlacion
   amplifica al apilar). El cuello NO es la entrada, es el SIZING.
8. Control de riesgo: bajar a 0.1-0.2%/trade PARTE el DD sin matar el retorno (0.5% era
   sobreapuesta). Tope bruto a 1.0x empeora; a 2.0x no toca.

## Frontera riesgo (FULL 2021-26, funding 0.01%/8h)
| risk/trade | NET% | maxDD% | Sharpe | Calmar |
|---|---|---|---|---|
| 0.5% | +49 | -63 | 0.42 | 0.78 (sobreapuesta) |
| 0.3% | +53 | -44 | 0.42 | 1.19 |
| 0.2% | +42 | -32 | 0.42 | 1.31 |
| 0.1% | +24 | -18 | 0.42 | 1.35 |

## Benchmark honesto (FULL 2021-26)
| | retorno | maxDD | Sharpe |
|---|---|---|---|
| Buy&Hold cesta (equiponderada) | +26% | **-88%** | 0.43 |
| Donchian 0.1%/trade | +24% | **-18%** | 0.42 |
| Donchian 0.2%/trade | +42% | -32% | 0.42 |

## VEREDICTO (sin celebrar ni matar)
- MISMO Sharpe que aguantar (~0.42). No es una mejora de Sharpe.
- La mejora REAL es el DRAWDOWN: retorno similar o mejor que el buy&hold con
  UNA QUINTA-UN TERCIO del drawdown (-18/-32% vs -88%). Eso vale: te da la
  exposicion cripto sin la sangria de perder el 88%.
- Es "CRISIS ALPHA": cobra esquivando/shorteando las grandes caidas; queda
  rezagada en bull fuerte. Es un DIVERSIFICADOR / reductor de drawdown, NO una
  maquina de imprimir que bate al mercado en Sharpe.

## Lo que sigue SIN saberse (no lo escondas)
- Funding real no medido (Binance solo expone el ultimo tramo). Con funding alto,
  2024-26 queda apenas en cero. Es la mayor incognita de magnitud.
- Todo es cripto, 1 clase correlacionada; "5 activos x 2 regimenes" no son 10
  apuestas independientes. Win-rate 18-28% (frágil por colas).
- 2 regimenes historicos no garantizan el tercero.

## Decision (es del usuario, no inercia)
A) Tratarlo como lo que es: overlay diversificador de bajo riesgo (0.1-0.2%/trade)
   cuyo valor es reducir drawdown, no batir Sharpe. Antes de real: paper trading.
B) Firmar magnitudes: conseguir funding real (otra fuente) y re-correr.
C) Aparcarlo con este veredicto. Reabrir = decision explicita, no inercia.

## Lo que perdura
El proceso: pre-registro -> OOS -> lockbox -> matar barato -> medir el cuello real
(aqui: sizing, no entrada). Reutilizable para la proxima hipotesis.
