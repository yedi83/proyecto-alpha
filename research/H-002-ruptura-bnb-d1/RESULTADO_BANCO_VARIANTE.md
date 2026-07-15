# H-002 VARIANTE (trailing Chandelier) — Veredicto del banco (2026-07-15)

> Variante: misma entrada que la base + gestión "2R → breakeven+colchón → trailing Chandelier 3×ATR", filtro anti-sobreextensión (10 ATR). Motor reutilizado VERBATIM (`backtest_2r_trail.py` del investigador). Se juzga con **más exigencia** que la base (más parámetros; el propio autor la marcó "dudosa-favorable").

## Resultados (BNB) vs la base

| test | Base | Variante |
|---|---|---|
| T1 BNB (vs hold) | MATA (Sharpe 0.89, MAR 0.74) | **PASA** (Sharpe 0.76, MAR 0.92; Ret +60% vs +38%) |
| T2 cruzado | 4/5 gana-hold | ~6/6 gana-hold |
| T5 OOS | Sharpe **1.08** | Sharpe 0.79 |
| T4 concentración | top-5 = 44%, n=57, WR 49% | **top-1 = 54%, top-5 = 90%, n=34, WR 53%** |
| T3 | meseta | mayormente estable; `ch_mult=3.0` en pico leve de retorno |

## Lo bueno (real)

Bate a aguantar (MAR 0.92 > 0.78) donde la base falló, generaliza en los majors, sobrevive OOS. El titular "mejor ratio, menos pérdidas netas" del investigador es cierto en superficie.

## El veneno (T4)

**El trade #1 solo = 54% del neto; el top-5 = 90%.** La variante logra su ratio **dejando correr un monstruo** (casi seguro el pump de BNB). Quítale ese trade y se desinfla. Es la **misma fragilidad** que hizo a H-001 de baja confianza (top-5 = 115%). El trailing compra un titular más bonito a cambio de que **todo cuelgue de una operación**. La base, con TP fijo 2R, capa cada ganador → resultado repartido (57 trades, top-5 = 44%), Sharpe y OOS mejores.

## Veredicto

Por la regla pre-acordada ("solo despliega si no es más frágil"): **la variante ES más frágil que la base** (cuelga de un trade, OOS peor, más parámetros). **No la reemplaza.** No es inválida — su ventaja es real pero es un **espejismo de una operación**, no robustez.

## Decisión (del investigador)

**Correr en paralelo como CANDIDATA ETIQUETADA de alta varianza / concentrada** en paper-real, junto a la base. El forward decide. Regla: NO dejar que su titular seduzca; si en vivo su resultado depende otra vez de 1-2 trades, confirma la fragilidad. La **base** sigue siendo la desplegada de referencia.
