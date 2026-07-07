# exp-004 — sensibilidad de lookback (384/512/640) — 2026-07-06 18:32 UTC

Paridad full/512 vs FRONTIER 0.10%-off: ✅ OK

Riesgo uniforme 0.001 fijo; único eje = largo del canal (exit escalado ÷2).

| ventana | largo | NET% | maxDD% | Sharpe | Calmar |
|---|---|---|---|---|---|
| full | 384 | -8.59 | -25.4 | -0.09 | -0.34 |
| full | 512 | 24.03 | -17.8 | 0.42 | 1.35 |
| full | 640 | 28.88 | -16.6 | 0.49 | 1.74 |
| 2123 | 384 | -1.40 | -14.4 | -0.01 | -0.10 |
| 2123 | 512 | 9.52 | -9.9 | 0.48 | 0.97 |
| 2123 | 640 | 12.27 | -10.3 | 0.59 | 1.19 |
| 2426 | 384 | -7.65 | -20.7 | -0.29 | -0.37 |
| 2426 | 512 | 2.79 | -13.6 | 0.18 | 0.21 |
| 2426 | 640 | 2.86 | -12.8 | 0.19 | 0.22 |

## VEREDICTO (criterio por capas, FULL): **H-001 MATADA (edge no robusto al lookback)**

- Base 512 FULL: Calmar 1.353 · Sharpe 0.423 · net 24.03% · alpha 5.10%
- Vecino 384: Calmar -0.338 (-25% del base) · Sharpe -0.094 · net -8.59% · alpha -28.64% → **MATA**
- Vecino 640: Calmar 1.743 (129% del base) · Sharpe 0.492 · net 28.88% · alpha 13.79% → **MESETA**

Umbrales: MESETA≥70% Calmar (0.947) y Sharpe≥0.323; FRÁGIL<50% Calmar (0.677); MATA si net≤0 o alpha≤0.

**Recordatorio:** 512 NO se cambia. Un vecino mejor = meseta, no razón para re-optimizar.