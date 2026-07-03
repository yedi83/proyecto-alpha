# Risk Frontier — veredicto (senal CONGELADA, solo geometria de riesgo)

Pregunta: ¿la alfa sobrevive al quitar el exceso de riesgo? Respuesta: SI, pero
su MAGNITUD es dependiente de regimen (crisis alpha).

## Frontera FULL 2021-26 (funding 0.01%/8h) — mejores configs
| risk/trade | vol-tgt | NET% | maxDD% | Sharpe | Calmar |
|---|---|---|---|---|---|
| 0.10% | off | +24 | -17.8 | 0.42 | 1.35 |
| 0.10% | 15% | +51 | -21.3 | 0.58 | 2.38 |
| 0.25% | 15% | +73 | -31.7 | 0.56 | 2.30 |
| 0.50% | 15% | +88 | -42.1 | 0.54 | 2.10 |
| 0.50% | off | +49 | -63.0 | 0.42 | 0.78 |
| Buy&Hold cesta | — | +26 | **-88** | 0.43 | — |

Hallazgos de geometria:
- Bajar riesgo/trade: el Sharpe NO cambia (~0.42), el Calmar SI mejora (0.5% era sobreapuesta).
- TOPE NOCIONAL (100/75/50/25%): DESTRUYE la cesta (cada posicion ATR pesa ~0.5x;
  capar a 100% deja caber 1-2 activos -> mata diversificacion). Lever equivocado.
- VOL-TARGET: el unico lever que sube Sharpe (0.42->0.58) y Calmar (->2.4)... en FULL.

## PERO: el lift del vol-target es de REGIMEN (lo decisivo)
Config 0.10% + vol-target 15%:
| Regimen | NET% | maxDD% | Sharpe | Calmar |
|---|---|---|---|---|
| 2021-2023 (bear) | +26.6 | -13.9 | **0.82** | 1.91 |
| 2024-2026 (reciente) | +2.9 | -21.3 | **0.17** | 0.13 |

=> El Sharpe del periodo completo (0.58) lo paga casi entero el bear 2022. En el
regimen reciente la estrategia esta PLANA (Sharpe ~0.18, +3% en 2 anios), y con
funding real mayor podria ser <=0.

## Veredicto final honesto
- La alfa SOBREVIVE al de-risking (no era solo apalancamiento): bien.
- El vol-target mejora el perfil, pero NO es edge general: amplifica la crisis
  alpha. Cobra en bears sostenidos; en calma no aporta.
- Esto es, confirmado y afinado, un INSTRUMENTO DE CRISIS / cobertura: brilla
  cuando el cripto sangra, plano cuando no. No es un generador de retorno para
  todo clima.
- Incognitas vivas: funding real (no medido), todo cripto correlacionado, 2
  regimenes, win-rate 18-28%.

## Mi error registrado
Me entusiasme con el Sharpe 0.58 del periodo completo antes de cortar por
regimen. El corte mostro que es un artefacto del bear 2022. Corregido.

## Decision (del usuario)
A) Usarlo por lo que es: cobertura/diversificador de bajo riesgo (0.10% + vol-tgt
   ~15%), esperando aportar en caidas y ~nada en calma. Paper trading antes de real.
B) Conseguir funding real y re-confirmar magnitudes.
C) Cerrar aqui. El proceso (pre-registro->OOS->lockbox->matar barato->cuello medido)
   es la entrega que perdura.
