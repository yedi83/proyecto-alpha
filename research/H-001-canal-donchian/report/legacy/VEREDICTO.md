# Veredicto — Donchian 512 (15m), in-sample, 6 activos

Ventana: 2024-07-05 → 2026-06-21 (HYPE desde 2025-05-30). Coste real por activo
(taker 0.06%/lado + slippage). Largo y corto. Sizing riesgo 0.5%, máx 3x.

## Resultados
| Activo | NET% | B&H% | ALFA% | #tr | win% | maxDD% | Sharpe | seg+ | lockbox alfa | Veredicto |
|---|---|---|---|---|---|---|---|---|---|---|
| BTC | +4.6 | +9.0 | -4.4 | 158 | 21.5 | -14.5 | 0.22 | 2/4 | +5.8 | SIN ALFA |
| ETH | +39.0 | -44.1 | +83.1 | 135 | 26.7 | -12.7 | 0.73 | 4/4 | +11.0 | candidata |
| SOL | +16.2 | -49.6 | +65.7 | 153 | 26.8 | -12.0 | 0.42 | 3/4 | +25.8 | candidata |
| BCH | -7.3 | -43.2 | +36.0 | 166 | 19.3 | -31.9 | 0.04 | 1/4 | +88.8 | MUERTA (net<0) |
| DOGE | +9.6 | -24.6 | +34.2 | 164 | 22.0 | -14.8 | 0.30 | 3/4 | +14.4 | candidata |
| HYPE | -13.6 | +84.5 | -98.1 | 101 | 19.8 | -18.2 | -0.49 | 1/4 | -61.9 | MUERTA |

## Diagnóstico de dirección (net% aislando libro)
| Activo | LONG-only | SHORT-only |
|---|---|---|
| BTC | +5.3 | -0.6 |
| ETH | +20.8 | +15.0 |
| SOL | +6.5 | +9.1 |
| BCH | -20.3 | +16.4 |
| DOGE | +20.1 | -8.8 |
| HYPE | +4.1 | -17.0 |

## Mi predicción vs realidad (registrada antes de correr) — FALLÉ
- Dije "no le gana al B&H en la mayoría" → FALSO: le ganó en 4/6 (ETH, SOL, BCH, DOGE).
  Causa de mi error: asumí ventana alcista; en realidad ETH/SOL/BCH/DOGE CAYERON
  fuerte y un sistema que puede ponerse corto los superó.
- Dije "el alfa es solo el libro de cortos" → FALSO: mixto. ETH/SOL ganan con AMBOS
  libros; DOGE gana con LARGOS; solo BCH depende del corto. No es sesgo bajista puro.
- Acerté: HYPE engaña por ventana corta y alcista (su corto lo destroza), y los
  win-rate son bajísimos (19-27%).

## Veredicto honesto
NO es edge probado. Es la PRIMERA hipótesis que no muere trivialmente: 3 activos
(ETH, SOL, DOGE) quedan net-positivos, pagando costes, batiendo B&H, estables en
segmentos y lockbox, y sin depender solo de cortos. Eso merece un test más duro,
NO capital. Razones para no creérselo todavía:

1. UNA sola ventana y un solo régimen. 2024-2026 tuvo tendencias largas (alts
   sangrando) = terreno ideal para seguimiento de tendencia. Eso puede ser SUERTE
   de régimen, no habilidad persistente.
2. Win-rate 19-27% = frágil. Depende de pocas operaciones grandes (riesgo de cola).
3. Multiplicidad mal contada: los 6 activos cripto están MUY correlacionados. "3 de
   6" no son 3 confirmaciones independientes; es ~1 apuesta repetida.
4. El motor es OPTIMISTA: los stops rellenan al precio exacto (en la realidad
   resbalan, peor en rupturas/liquidaciones) y NO modela funding (relevante en
   posiciones de varios días). Falta re-correr con fills pesimistas + funding.
5. BCH/HYPE fallan y BTC no da alfa: 3 de 6 ya caen in-sample.

## Próximos tests para MATAR o confirmar (en orden)
1. Funding real + fills pesimistas (stop al siguiente open, slippage extra). Si el
   alfa se evapora, muerto.
2. Jackknife por OPERACIÓN: quitar las 1-2 mejores trades por activo. Si se da la
   vuelta, era cola, no edge.
3. Otra ventana/régimen: bajar 2021-2023 (bull 2021 + bear 2022) y repetir. Es el
   test más fuerte disponible.
4. Sensibilidad de parámetros (384/512/640): ver si 512 es un punto de navaja o una
   meseta. No para optimizar: para detectar fragilidad.
