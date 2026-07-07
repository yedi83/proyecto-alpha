# exp-007 — PRE-REGISTRO (comportamiento en el crash de covid, aislado)

Fecha: 2026-07-07 (ANTES de correr). Familia: **estudio de comportamiento** (P3 de la AGENDA). Depende de los datos `_84m` (ya descargados).

## Objetivo

exp-006 mostró que la cesta atraviesa 2019-2021 con drawdown ~1/7 del buy&hold. Pero esa ventana **mezcla** el crash del covid con el bull 2021. Aquí **aislamos el crash**: ¿la estrategia protege (o cobra) **durante** el desplome del covid?

Importa porque el covid fue un **flash crash** (−50% en días, marzo 2020). Un trend-follower lento (canal de ~5 días) protege bien en bears **lentos** (2022: tuvo tiempo de shortear), pero puede quedar **atrapado** en una caída de un día. Esta es la prueba de si la "crisis alpha" vale para crashes rápidos o solo para bears lentos.

## Datos y ventana (definida por el EVENTO, no por peeking)

BTC/ETH/BCH (los que existían en 2020). Warmup desde 2019-12 (los canales llegan calientes al crash). Ventana pre-registrada **por calendario del covid**, no por dónde luce mejor la estrategia:

- Ventana del crash: **2020-02-14 → 2020-04-30** (pico → Black Thursday 12-mar → recuperación temprana).
- Días del desplome (para ver exposición): **2020-03-08 → 2020-03-20**.

## Criterio de decisión — PRE-ESCRITO

Se mide sobre la ventana del crash: retorno y maxDD de la estrategia vs el B&H equiponderado, y la **exposición neta** (larga/corta/plana) en los días del desplome.

- **PROTEGE (crisis alpha en crash rápido):** retorno estrategia **≫** B&H **y** maxDD estrategia **≤ 1/3** del maxDD de B&H (idealmente exposición neta ≤ 0 —corto/plano— en los días del desplome).
- **NO PROTEGE el crash rápido:** cae parecido al B&H (maxDD comparable). → La cobertura es para bears **lentos**, no flash crashes. Es un **refinamiento** de qué hace la estrategia, NO un kill.

## Límite

Un crash, 3 monedas. **Ilustrativo del mecanismo, no prueba estadística.** Responde "¿cómo se comporta en este tipo de crisis?", no "¿tiene edge?".
