# ¿Alfa independiente o el mismo trade x5? (senal congelada, FULL 21-26, fund 0.01%)

## P1 — Correlacion de SENALES (stance -1/0/+1)
Media 0.57 (BTC-ETH 0.69, min BCH-SOL 0.47). Substancial, no identica.
=> Direccion compartida la mayor parte del tiempo: ~un motor, no cinco.

## P2 — Atribucion de PnL
| Activo | aporte | acum |
|---|---|---|
| SOL | 39.9% | 39.9% |
| ETH | 33.3% | 73.3% |
| BCH | 15.1% | 88.4% |
| DOGE | 10.9% | 99.3% |
| BTC | 0.7% | 100% |
SOL+ETH = 73%. BTC = peso muerto (0.7%).

## P4 — Correlacion de RETORNOS (pnl/barra)
Media 0.34. Menor que la de senales (hay algo de diversificacion en el PnL).

## P3 — Stress de concentracion (cap nº posiciones)
| config | NET% | maxDD% | Sharpe | Calmar |
|---|---|---|---|---|
| sin cap | 48.7 | -38.5 | 0.42 | 1.26 |
| max 3 | 19.4 | -30.9 | 0.28 | 0.63 |
| max 2 | -6.7 | -30.8 | -0.01 | -0.22 |
Capar destruye, PERO el cap elige por orden de llegada (sesgado). Test confundido.

## Test limpio de redundancia — quitar activos
| cesta | NET% | maxDD% | Sharpe | Calmar |
|---|---|---|---|---|
| 5 todos | 48.7 | -38.5 | 0.42 | 1.26 |
| 4 sin BTC | 57.4 | -27.6 | 0.50 | 2.08 |
| 3 ETH+SOL+DOGE | 47.9 | -22.5 | 0.50 | 2.13 |
| 2 ETH+SOL | 41.3 | -14.2 | 0.58 | 2.92 |
| 1 SOL solo | 23.6 | -15.0 | 0.52 | 1.57 |
MENOS activos = MEJOR risk-adjusted. La cesta de 5 dilduye, no diversifica.

## LA TRAMPA (lo mas importante)
"Quedarse con ETH+SOL" es SELECCION IN-SAMPLE. Los lideres ROTAN:
- 2021-23: estrellas BTC/BCH/DOGE (BTC +40% alfa).
- 2024-26: estrellas ETH/SOL.
El 0.7% de BTC full = promedio de fuerte(21-23) + muerto(24-26).
=> "Quitar BTC / tradear ETH+SOL" NO es desplegable: apuesta a repetir ganadores.

## Respuesta a la pregunta ampliada
¿Sobrevive la alfa al quitar exceso de riesgo + concentracion + redundancia a la vez?
- Exceso de riesgo: SI sobrevive.
- Redundancia: existe y es real -> es ~UN motor correlacionado (corr senal 0.57;
  1 activo ya captura casi todo el Sharpe), NO cinco independientes.
- Pero eliminar redundancia eligiendo activos = hindsight (lideres rotan).
=> NO hay fuente de alfa independiente multiple. Hay UN motor crisis-alpha de
   tendencia, correlacionado, mejor concentrado, sin forma fiable de pre-elegir.

## Posturas defendibles (ninguna es "trade ETH+SOL")
A) Cesta equiponderada aceptando el drag ("no se predecir ganadores").
B) Un solo activo liquido (SOL/ETH) = el mismo motor con menos piezas.
"Elegir los 2 que ganaron" NO es defendible.
