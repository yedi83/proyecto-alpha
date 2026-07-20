# H-002.v2 — Screen in-sample (T1-IS) — EJECUCIÓN OFICIAL DEL IN-SAMPLE, NO VEREDICTO

> Corrido 2026-07-19 con `banco_v2_is_screen.py` (SHA-256 `5812407…`, motor `../banco.py` verbatim), bajo el PREREG v2 **+ ENMIENDA 1** que fija la construcción de la cesta (§2bis). **Es la ejecución oficial del screen in-sample**, pero **NO es el veredicto de v2**: es la condición *necesaria, no suficiente*. No aprueba ni rechaza la hipótesis; el veredicto exige el forward + A-01.

## Qué se corrió

Cesta equiponderada de los 6 activos (BTC, ETH, BNB, ADA, XRP, LTC), **solo datos anteriores a 2023-01-01** (in-sample de desarrollo), **spot** (sin funding), **sin risk-match**. Métricas Sharpe y MAR a nivel cesta. Regla sellada T1-IS: PASA si la cesta-estrategia supera a la cesta-hold en Sharpe **y** MAR, margen estricto > 0.

## Resultado

| Cesta | Sharpe | MAR | Ret | MDD |
|---|---|---|---|---|
| Estrategia | 1.878 | 1.461 | +17.5% | −2.4% |
| Buy & hold | 0.799 | 0.499 | +347.4% | −73.9% |

- **T1-IS: PASA** (Sharpe 1.878 > 0.799 y MAR 1.461 > 0.499). Necesario, no suficiente.
- Por activo (pre-2023): la estrategia bate al hold en Sharpe y/o MAR en **5/6**; excepción **BNB** (hold Sh 1.13/MAR 1.18 > estrategia 0.90/0.78 — efecto del pump histórico de BNB, ya diluido en la cesta).
- T4 (info, cap de confianza): n=151 trades agrupados, win 51.0%, **top-5 = 14.8% del neto** (muy repartido; v1 era 44%). Deflated Sharpe pendiente (exige el N de configuraciones de T3, no corrido aquí).

## Caveats (por qué esto NO es el veredicto)

1. **In-sample = dato de desarrollo.** No prueba nada hacia adelante. El veredicto decisivo de v2 es el **forward OOS** (≥30 trades y ≥6 meses desde 2026-07-15; no antes de ~2027) + **A-01**.
2. **Instrumento spot, sin funding.** La corrida decisiva de v2 es perp + funding real (P3), con dictamen A-02 previo del dataset.
3. **La construcción de la cesta** (media de curvas normalizadas, rebalanceo diario a equiponderación) quedó **sellada en el PREREG §2bis (ENMIENDA 1, 2026-07-19)** y congelada al script por hash. Cautela declarada: se selló tras ver el número in-sample; mitigado porque se congeló lo que el script ya hacía (sin optimizar) y porque el in-sample no es decisivo (lo es el forward, aún inexistente).
4. El Sharpe de cesta (1.88) supera al de cualquier activo suelto por **diversificación** (menor volatilidad de cartera), no por mayor edge individual.

## Estado

Adelanto informativo. La hipótesis sigue **EN VALIDACIÓN / NO PROBADA / "evidencia insuficiente"** hasta que el forward cumpla su criterio y pase A-01. Nada cambia en los registros oficiales por este adelanto.
