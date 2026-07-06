# exp-004 — PRE-REGISTRO (sensibilidad del largo del canal: 384 / 512 / 640)

Fecha: 2026-07-06 (ANTES de correr). Investigador: decisión del humano. Familia: **sensibilidad de lookback** (distinta de la familia de riesgo de exp-002/003).

## Objetivo y tipo de test

**Robustez, NO optimización.** Comprobar si el largo del canal 512 —pre-registrado en el VEREDICTO original— es una **MESETA** (edge estructural real, robusto a variación razonable del lookback) o un **PICO aislado** (sobreajuste al parámetro). No se busca el "mejor" largo.

## Declaración de pruebas múltiples (obligatoria)

N=2 vecinos, elegidos **ex-ante** como ±25% del base: 512×0.75 = **384**, 512×1.25 = **640**. No es una búsqueda ni un barrido fino: se prueban exactamente estos dos y ninguno más de esta familia. Iterar más largos tras ver resultados sería optimización retrospectiva (prohibido).

## Parámetros

- `ENTRY_LEN` ∈ {384, 512, 640}. `EXIT_LEN` **escalado proporcional** (÷2): {192, 256, 320}. Ratio entry:exit = 2:1 constante — se prueba el *timescale* de la estrategia como un solo knob.
- Todo lo demás **IDÉNTICO a exp-002/003**: cesta 2021-2026, código congelado, funding 0.01%/8h, mismas ventanas (full / 2123 / 2426), paridad de motor verificada.
- **Riesgo: uniforme 0.001** (la config validada de la cesta, misma "base" de exp-002/003 que produce Calmar 1.353). Se mantiene fijo para que la **longitud sea el único eje**. El ajuste M1 (btc0125) es un eje ortogonal, ya evaluado en exp-003, y no cambia la pregunta de robustez del lookback. (Corrección pre-corrida 2026-07-06: la versión inicial citaba btc0125 por error; se fija en uniforme para que la paridad reproduzca la base 1.353.)
- **512/256 = base de referencia** (ya conocida): FULL Calmar 1.353, Sharpe 0.423, net +24.0%, alpha +5.1%.

## Métricas

Primarias: **Calmar** y **Sharpe** en **FULL** (mayor muestra). Se reportan también net, alpha y maxDD por ventana (full / 2123 / 2426). El juicio primario va sobre FULL; la ventana 2024-26 es **contexto**, no corte (la base ya es marginal ahí: Sharpe 0.18, Calmar 0.21).

## Criterio de decisión — falsación PRE-ESCRITA, por capas (evaluada en FULL, sobre CADA vecino)

- **MATA H-001** — si algún vecino (384 o 640) va a **net ≤ 0** o **alpha ≤ 0**. Interpretación: el edge desaparece con un cambio menor de parámetro → no era un edge real, era ruido/curva.
- **FRAGILIDAD SERIA** (H-001 gravemente debilitada) — si algún vecino tiene **Calmar < 50% del 512** (< 0.677) aunque siga positivo. 512 sería un pico aislado.
- **MESETA ROBUSTA** (H-001 sobrevive, robustez confirmada) — si **AMBOS** vecinos cumplen: **Calmar ≥ 70% del 512** (≥ 0.947) **y** **Sharpe ≥ 0.32** (base 0.423 − 0.10) **y** net > 0 **y** alpha > 0.
- **ZONA INTERMEDIA** (Calmar entre 50% y 70% del base, o Sharpe entre 0.32 y el de base, con net/alpha positivos) — **no concluyente**: se documenta como **fragilidad parcial / caveat**; H-001 sobrevive con la advertencia registrada, y la decisión de pasar a Fase C se toma con ese caveat a la vista.

"Casi pasa = no pasa" aplica a las fronteras meseta/fragilidad: no se renegocian tras ver resultados.

## Compromiso anti-optimización (obligatorio)

512 fue pre-registrado en el VEREDICTO original y **NO se cambia pase lo que pase este test.** Si un vecino resulta "mejor" que 512, eso es evidencia de meseta (bueno), **NO** una razón para re-optimizar a ese largo — hacerlo sería mover los postes. El único output accionable de este experimento es un veredicto sobre H-001 (robusta / frágil / caveat); **nunca** "adoptar 384 o 640".

## Ejecución

Correr con la plantilla de `exp-002/exp002_riesgo_por_simbolo.py`, cambiando solo `ENTRY_LEN`/`EXIT_LEN` por corrida. **Verificar paridad** primero: la corrida 512/256 debe reproducir la base al centavo (net 24.03 / maxDD −17.8 / Sharpe 0.42 / Calmar 1.35), como hicieron exp-002/003. Sin esa paridad, la corrida no es válida. Resultados a `exp-004/`: `RESULTADO.md`, `metricas.json`, `DATOS.md`.

## Nota de gobernanza

El "no habrá exp-004 de esta familia" del PREREG de exp-003 se refería a la familia de **riesgo asimétrico**. Este exp-004 es de otra familia (**sensibilidad de lookback**, pre-Fase C) y no reabre la decisión de riesgo (M1 sigue cerrado: $750 + BTC 0.125%).
