# Resultado — TEST #1 (funding + fills pesimistas)

Umbral pre-registrado: >=2 de {ETH,SOL,DOGE} con net>0, alpha>0, lockbox alpha>0.

## Funding 0.01%/8h + fills pesimistas (entrada +5bps, stop +10bps)
| Activo | NET% | B&H% | ALFA% | lockbox alfa% | sobrevive |
|---|---|---|---|---|---|
| BTC | -11.2 | +9.0 | -20.2 | +3.6 | no |
| ETH | +28.8 | -44.1 | +72.9 | +9.7 | SI |
| SOL | +8.0 | -49.6 | +57.5 | +24.3 | SI |
| BCH | -14.2 | -43.2 | +29.1 | +86.7 | no (net<0) |
| DOGE | +1.7 | -24.6 | +26.3 | +13.2 | SI (justo) |
| HYPE | -17.1 | +84.5 | -101.5 | -63.3 | no |

Sobreviven 3/3 → **APRUEBA** (umbral >=2).

## Sensibilidad funding 0.03%/8h (mas duro, informativo)
ETH net +21.7 (vive), SOL net +2.6 (vive justo), DOGE net -2.4 (MUERE).
=> ETH y SOL aguantan funding alto; DOGE es fragil.

## Lectura honesta
- PASA el umbral. El edge no se evaporo con funding pesimista + stops peores.
- ETH y SOL: colchon solido (alfa 58-73, net positivo incluso con funding 3x).
- DOGE: marginal. Muere con funding alto. No me apoyaria en DOGE.
- BTC/BCH/HYPE: muertos, confirmado.
- Sigue siendo UN solo regimen (2024-2026) y funding es un proxy de estres, no
  el dato real. La prueba decisiva pendiente es OTRA ventana (2021-2023).
