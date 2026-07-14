# H-002 — Ruptura Donchian + SMA200, BNB/USDT diario — PRE-REGISTRO DEL BANCO

Fecha: 2026-07-XX (ANTES de correr el banco y ANTES de mirar resultados). Estrategia: canal 20, filtro SMA200, stop 2.5×ATR(14), objetivo 2R, riesgo 1.25%, **solo largos, un activo**. Variante con trailing = **más parámetros, más sospechosa** (el propio autor la marcó "dudosa-favorable"); se juzga aparte y con más exigencia.

## Preocupación central (declarada)

Long-only sobre **BNB**, un token que subió ~1000x. El riesgo #1 es que el retorno sea **BETA de BNB**, no edge: "estar largo del cohete cuando el cohete sube". El banco existe para separar eso.

## Tests y criterios de decisión (PRE-ESCRITOS)

**T1 — ¿Bate a comprar-y-aguantar BNB? (el decisivo, matar barato).** Se compara la estrategia contra hold BNB en el MISMO período, **ajustado por riesgo** (no retorno bruto).
- MATA / es beta: la estrategia NO mejora el Sharpe **ni** el Calmar/MAR del hold. Si solo "gana menos con menos drawdown" sin mejorar riesgo-ajustado, es beta con pasos extra.
- PASA: mejora Sharpe o Calmar del hold de forma clara.

**T2 — ¿Generaliza a otros activos? (¿fue elegido BNB?).** Mismas reglas congeladas sobre BTC, ETH, ADA, XRP, LTC.
- BANDERA de selección: funciona en BNB pero falla (net≤0 o no bate hold) en la mayoría de los otros → estaba pegado a BNB.
- APOYA: rinde parecido en varios → es un mecanismo, no un ajuste a un activo.

**T3 — Sensibilidad de parámetros.** Canal 20 → {10,15,30,40}; SMA 200 → {100,150,300}. ¿20/200 es una meseta o un pico?
- FRÁGIL: los vecinos se derrumban (net≤0 o Sharpe colapsa) → sobreajuste.
- ROBUSTA: los vecinos aguantan parecido.

**T4 — Significancia y concentración.** Nº de trades; jackknife (¿el neto cuelga de los top-N?).
- Cap de confianza: <30 trades o neto dominado por ≤5 → confianza baja (no mata, limita el sizing y prohíbe "capital significativo").

**T5 — OOS por tiempo.** Reservar el último ~30% del período como lockbox (nunca tocado al leer los otros tests) y verificar que el edge sobrevive ahí.
- BANDERA: el edge desaparece fuera de muestra.

## Regla anti-sobreajuste

No se re-optimizan parámetros por lo que se vea. No se elige el mejor activo con retrovisor. La variante trailing NO se prueba en vivo hasta que la base pase T1-T5. Cada resultado se acepta como salga.

## Veredicto

Solo pasa a paper-en-real quien apruebe T1 (bate al hold ajustado por riesgo) y no dispare banderas graves en T2/T5. Confianza y sizing según T4.
