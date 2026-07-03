# Test de transferibilidad — ¿el ranking de activos sirve OOS?

## Sharpe standalone por activo y ranking
| activo | Sharpe 21-23 | rank | Sharpe 24-26 | rank |
|---|---|---|---|---|
| BCH | 0.59 | 1 | -0.41 | 5 |
| BTC | 0.49 | 2 | -0.35 | 4 |
| DOGE | 0.30 | 3 | 0.11 | 3 |
| ETH | 0.09 | 4 | 0.98 | 1 |
| SOL | -0.01 | 5 | 0.32 | 2 |

**Correlacion de ranking (Spearman) = -0.90**  (se INVIERTE)
Top-2 21-23: BCH, BTC.  Top-2 24-26: ETH, SOL.  Solape = 0.

## Coste de seleccionar (operar lo "entrenado")
Train 2021-23 -> opera 2024-26:
| seleccion | net | DD | Sharpe |
|---|---|---|---|
| top2 entrenado (BCH,BTC) | -11.8% | -28.8% | -0.47 |
| cesta completa (5) | +2.9% | -30.6% | 0.19 |
| oraculo top2 (ETH,SOL) | +18.7% | -12.7% | 0.74 |

Train 2024-26 -> opera 2021-23:
| seleccion | net | DD | Sharpe |
|---|---|---|---|
| top2 entrenado (ETH,SOL) | -0.3% | -14.2% | 0.05 |
| cesta completa (5) | +19.8% | -22.6% | 0.48 |
| oraculo top2 (BCH,BTC) | +16.5% | -15.6% | 0.66 |

## Conclusion (con dato)
- El ranking de activos NO es transferible: es anti-transferible (-0.90).
- Seleccionar ganadores del pasado = comprar los perdedores del futuro. Es la
  PEOR opcion en ambas direcciones (negativa o plana).
- La cesta completa SIN seleccionar es la unica robusta: positiva y estable en
  ambos regimenes.
=> Si se opera, se opera la CESTA EQUIPONDERADA completa (o un subconjunto
   elegido por LIQUIDEZ, nunca por rendimiento pasado). Nada de seleccionar activos.
