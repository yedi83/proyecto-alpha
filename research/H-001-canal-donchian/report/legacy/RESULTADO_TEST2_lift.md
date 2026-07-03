# Resultado — Jackknife por operacion + Lift por regimen

## (1) Jackknife: ¿cuelga de pocas trades? (PnL aditivo $, eq0=10000)
| Activo | PnL total$ | top1$ | top2$ | sin top1 | sin top2 |
|---|---|---|---|---|---|
| BTC | 970.9 | 781.3 | 1521.2 | 189.6 | -550.3 |
| ETH | 4257.6 | 2094.3 | 3212.1 | 2163.3 | 1045.5 |
| SOL | 2023.0 | 686.3 | 1349.9 | 1336.8 | 673.2 |
| BCH | -408.7 | 2332.6 | 2725.4 | -2741.4 | -3134.1 |
| DOGE | 1401.2 | 1040.8 | 1820.4 | 360.3 | -419.3 |
| HYPE | -1147.5 | 337.6 | 665.1 | -1485.1 | -1812.6 |

- ETH y SOL: positivos incluso sin sus 2 mejores trades -> NO es solo cola.
  (ETH concentrado: top1 = 49% del total; dependiente de cola, vigilar.)
- DOGE: sin top2 se vuelve NEGATIVO -> fragil. Se descarta DOGE.

## (2) Lift por regimen — Efficiency Ratio 96 velas, terciles
| | bajo ER | medio ER | alto ER |
|---|---|---|---|
| ETH win% / meanPnl$ | 33.3 / 86.6 | 17.8 / -25.7 | 28.9 / 33.7 |
| SOL win% / meanPnl$ | 29.4 / 13.8 | 29.4 / 29.8 | 21.6 / -3.9 |
| Pooled win% / meanPnl$ | 31.2 / 47.8 | 26.0 / 7.6 | 22.9 / 10.0 |

### Lectura
La hipotesis del "vigia" (operar SOLO en alta tendencia) NO se sostiene: el
tercil de ALTA tendencia rinde IGUAL o PEOR. Los mejores trades llegan con
tendencia reciente BAJA (breakout saliendo de base). El Donchian 512 ya ES el
filtro de tendencia; anadir un vigia de "ya hay tendencia" borraria las mejores
entradas. => No se anade el filtro.

Nota: muestras pequenas (45-51/bucket), in-sample. El indicio inverso (favorecer
bases de baja eficiencia) queda como hipotesis para la OTRA ventana, no para
adoptar ahora (evitar p-hacking).
