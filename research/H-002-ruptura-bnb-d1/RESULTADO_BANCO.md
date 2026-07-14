# H-002 — Veredicto del banco (2026-07-14)

> Estrategia: ruptura Donchian(20) + filtro SMA200, stop 2.5×ATR, objetivo 2R, riesgo 1.25%, solo largos, diario. Motor: reutilizado VERBATIM del backtest del investigador. Datos: spot Binance (BNB 3.173 velas, 2017-11 → 2026-07; ≈ los 3.143 del original → paridad razonable).

## T1 — vs comprar-y-aguantar BNB (historia completa): **FALLA, pero por un outlier**

| | Ret | MDD | Sharpe | MAR |
|---|---|---|---|---|
| Estrategia BNB | +37.9% | −5.5% | 0.89 | 0.74 |
| Aguantar BNB | **+4363%** | −76% | 0.97 | 0.78 |

Por la regla pre-escrita: MATA (no bate Sharpe ni MAR). Peor: con solo ~7% del capital en BNB (resto caja) tendrías el mismo −5.5% de DD y **+314%** en vez de +38% → sobre la historia completa, la **beta dimensionada la aplasta**.

**PERO ese T1 está dominado por el 40x irrepetible de BNB (2017-2021).** No se puede comprar BNB de 2017. El resto del suite pre-registrado lo corrige.

## T2 — generalización cruzada: **el mecanismo generaliza**

Bate a aguantar (Sharpe **y** MAR) en **4 de 5** majors: BTC, ETH (brutal: Sharpe 0.97 vs 0.54), ADA, XRP. Solo BNB (por el pump) y LTC (wash) son la excepción. → No estaba pegado a un activo; es un mecanismo.

## T3 — sensibilidad: **meseta, no pico**

N∈{10..40} × atr∈{2,2.5,3}: Sharpe 0.45-0.89, todos positivos; N=20/atr2.5 es la cima de una **meseta** (vecinos 0.7-0.86), no un pico solitario. SMA: 100→1.00, 200→0.89, 300→0.67 — SMA200 **no** es óptimo (100 daba más), así que no se sobre-optimizó ese eje. Robusto.

## T4 — significancia: **más sólido que H-001**

n=57 trades, win rate 49%, top-5 = 44% del neto (top-1 solo 9%). NO cuelga de la cola (H-001 era 115% en top-5). Muestra chica pero mucho mejor repartida.

## T5 — OOS (lockbox último 30%, 2023-2026): **APLASTA a aguantar**

Estrategia OOS: Sharpe **1.08**, +14.1%, MDD −4.8%. Aguantar BNB OOS: Sharpe **0.26**, +0.6%. En el régimen reciente/representativo (post-pump), la estrategia añade valor ajustado por riesgo claro, y bate incluso a la beta dimensionada.

## Reconciliación y honestidad de proceso

- T1 (decisivo pre-escrito) falló, pero era un test **defectuoso** al aplicarse sobre un solo activo con un pump único: confunde "batir un outlier irrepetible" con "no tener edge". El suite completo (T2, T5, también pre-registrados) lo corrige.
- El autor del banco (Claude) venía con prior "probablemente es beta"; el banco mostró que **era demasiado pesimista**. Actualización registrada.

## Veredicto

**NO es beta con pasos extra, y NO está muerta.** Es un **overlay de tendencia multi-activo, reductor de drawdown**, que bate a aguantar **fuera de muestra** y en la **mayoría de majors**, con meseta de parámetros y sin depender de la cola. **Confianza moderada** (mejor que H-001), **no probada** (57/19 trades = muestra chica).

## Reglas retenidas (anti-sobreajuste)

1. **No cherry-pick:** no cambiar a ETH (mejor activo) ni SMA100 (mejor param) por lo visto. El mecanismo generaliza; elegir el ganador ex-post es sobreajuste en espejo.
2. **BNB single-asset es el caso más débil** (T1). Si se opera, que sea **multi-activo** sobre majors, juzgado contra aguantar.
3. **La variante trailing NO** pasa a vivo: más parámetros, autoflag "dudosa-favorable". Solo la base.
4. Avanza a **paper-real multi-activo** sobre sus méritos (T2/T5), no sobre el backtest de BNB.
