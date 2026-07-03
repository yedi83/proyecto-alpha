# Resultado — CESTA (5 activos, capital compartido, riesgo 0.5%/trade)
Fills pesimistas incluidos. Funding = sensibilidad (no medible real).

| Ventana | fund/8h | NET% | B&H% | ALFA% | maxDD% | Sharpe |
|---|---|---|---|---|---|---|
| 2021-2023 | 0.00 | +38.8 | -37.3 | +76.2 | -38.7 | 0.59 |
| 2021-2023 | 0.01 | +25.4 | -37.3 | +62.7 | -40.3 | 0.48 |
| 2021-2023 | 0.03 | +2.2 | -37.3 | +39.6 | -45.8 | 0.28 |
| 2024-2026 | 0.00 | +7.9 | -29.7 | +37.6 | -50.3 | 0.33 |
| 2024-2026 | 0.01 | -5.9 | -29.7 | +23.8 | -51.9 | 0.20 |
| 2024-2026 | 0.03 | -28.4 | -29.7 | +1.3 | -61.9 | -0.08 |
| FULL 21-26 | 0.01 | +49.1 | +18.9 | +30.2 | -63.0 | 0.42 |

## Verdad doble (no se la celebra ni se la mata)
- EL EDGE EXISTE: alfa POSITIVA en todas las ventanas antes de funding, y en la
  ventana completa incluso con funding (+30% vs B&H +19%).
- EL RIESGO ES INACEPTABLE tal cual: maxDD -50% a -63%. Sharpe 0.2-0.6.
  Nadie aguanta -63%; con apalancamiento = ruina/liquidacion.

## Diagnostico (el cuello de botella MEDIDO)
La "diversificacion" NO funciono: los 5 activos estan muy correlacionados, asi
que apilar 5 posiciones de riesgo igual AMPLIFICA el drawdown en vez de
reducirlo. La cesta DD (-63%) es MUCHO peor que cada activo aislado (-11 a -24%).
=> El problema ya NO es la entrada (hay alfa); es la GEOMETRIA/SIZING de apilar
   posiciones correlacionadas. Mismo patron que el lab de rango: el cuello no era
   el detector.

## Funding = espada encima
Con funding 0.01%/8h la ventana 2024-26 ya da net NEGATIVO. Y no podemos medir
el funding real (Binance solo expone el ultimo tramo). Es la mayor incertidumbre
de magnitud que queda.

## Siguiente experimento (atacar el cuello medido)
Control de riesgo a nivel CARTERA, no por activo:
1. Bajar riesgo/trade (0.5% -> 0.2%) y/o CAPAR exposicion bruta total.
2. Vol-targeting de cartera (objetivo de volatilidad fijo).
3. Sizing consciente de correlacion (tratar la cesta como ~1 apuesta).
Meta: misma alfa con DD a la mitad. Si no se puede bajar el DD sin matar la
alfa, no es desplegable.
