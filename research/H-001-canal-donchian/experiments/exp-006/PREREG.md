# exp-006 — PRE-REGISTRO (fuera de muestra por tiempo: régimen 2020)

Fecha: 2026-07-06 (ANTES de correr y ANTES de mirar datos pre-2021). Familia: **generalización OOS por tiempo**. **PENDIENTE DE DATOS** (requiere extender el cache antes de 2021-07).

## Objetivo

¿La firma de la cesta —seguro de crisis: alfa sobre el buy&hold de la cesta y **drawdown muy inferior**— sobrevive en un **régimen genuinamente anterior y no visto**? El período 2020 trae el crash del covid (marzo 2020) y el arranque del bull 2020-2021: condiciones distintas a 2021-2026. El veredicto ya hizo OOS en 2021-2023 (held-out); esto añade un **tercer régimen** más viejo.

Requisito de limpieza: **solo vale si nunca se miró pre-2021 al construir la estrategia.** Si se miró, está contaminado y no cuenta.

## Datos (límite honesto)

Los perp de Binance arrancan ~sept 2019. Realistamente: BTC/ETH (quizá alguno más) se pueden estirar a ~2020 / fin 2019; SOL/HYPE no tienen historia más vieja. Así que el test será con las monedas que TENGAN datos pre-corte, no las 5. Ventana objetivo: **2019-12 → 2021-07** (lo que exista), aislada del período ya usado.

## Reglas (congeladas)

Motor idéntico (`backtest_cesta` / exp-002), 512/256, riesgo uniforme 0.001, funding 0.01%/8h. Cesta con los símbolos que tengan datos pre-2021. Se reporta net, alpha (vs B&H de esos símbolos), maxDD, Sharpe, y **el drawdown del B&H equiponderado** en la misma ventana (para la comparación de "seguro").

## Criterio de decisión — PRE-ESCRITO (alineado con lo que la estrategia ES)

No se juzga "¿bate al mercado en 2020?" (ya sabemos que no es su función). Se juzga si mantiene su **firma de seguro**:

- **SOBREVIVE el régimen:** en 2020, la cesta muestra **(net > 0 o alpha > 0)** **Y** un **maxDD materialmente menor** que el del buy&hold equiponderado de la ventana (p. ej. ≤ mitad). Es decir, sigue dando exposición con mucho menos drawdown.
- **NO SOBREVIVE / bandera:** net < 0 **y** sin ventaja de drawdown sobre B&H. La cobertura no apareció justo cuando debía (un crash real).
- **Límite honesto:** un régimen más, cripto correlacionado, pocas monedas con historia. NO resuelve la significancia; suma o resta convicción sobre "es un seguro de crisis de verdad".

## Nota

Este test es especialmente relevante porque 2020 tiene un **crash real** (covid): es la prueba más directa de si la "crisis alpha" que el veredicto le atribuye **aparece cuando hay crisis de verdad**, en datos que el diseño no usó.
