# Robustez — Bootstrap + Jackknife (cesta 5, risk 0.25%, funding 0.01%)

## Atribucion de PnL (con MtM de abiertas; bug de solo-cerradas corregido)
| | FULL 21-26 | 2021-23 | 2024-26 |
|---|---|---|---|
| lider 1 | SOL 40% | BCH 50% | ETH 142% |
| lider 2 | ETH 33% | BTC 29% | SOL 46% |
| resto | BCH15/DOGE11/BTC1 | DOGE18/ETH5/SOL-2 | DOGE14/BTC-39/BCH-64 |
Los contribuyentes ROTAN por regimen. No hay un activo que cargue todo el tiempo.
=> argumento a favor de la cesta completa; en contra de seleccionar.

## Bootstrap por bloques (L=20d, N=10.000)
| metrica | p5 | p25 | p50 | p75 | p95 |
|---|---|---|---|---|---|
| CAGR% | -10.6 | -0.1 | 8.5 | 17.9 | 34.9 |
| Sharpe | -0.31 | 0.13 | 0.43 | 0.72 | 1.15 |
| maxDD% | -62.9 | -49.7 | -40.9 | -34.0 | -26.5 |
% Sharpe>0: 83% | % CAGR>0: 75% | % maxDD<-50%: 24%
=> Positivo mas veces que no, pero 25% de colas planas/negativas y DD severos frecuentes.

## Jackknife de trades (n=1884, win rate 20.3%)
- top-1 trade = 31% del neto.
- top-5 trades = 115% del neto -> SIN ellos NEGATIVO.
- Solo 4 trades ganadores cubren el 100% del neto.
=> TODO el edge cuelga de ~5 operaciones. Muestra efectiva = un punado de
   tendencias (probable: short bear 2022 + 2-3 movimientos limpios).

## Veredicto de robustez (honesto)
- Es la firma TEXTBOOK del trend-following: convexidad, no robustez estadistica.
  No es bug; es la naturaleza del estilo.
- PERO: confianza estadistica baja (≈5 trades efectivos). No distinguible de suerte
  con rigor. Si te pierdes 1-2 tendencias clave, caes en la cola negativa.
- Lo que hay NO es un motor de retorno estable: es una COBERTURA CONVEXA DE COLA
  / seguro de crisis. Sangra la mayoria del tiempo, paga raro y fuerte.

## Implicacion para el despliegue
Si se usa, se usa como SEGURO (tamaño pequeno, aceptando sangrado prolongado y
que el pago puede tardar anios o no llegar en una ventana dada). NO como fuente
de alfa constante. Sizing y supervivencia durante los flat = todo.
