# Datos

> Fuentes, calidad y sesgos conocidos. Actualizado 2026-07-03 con lo verificado en el inventario del lab (`MIGRACION.md`).

## Fuentes actuales (H-001)

| Dato | Fuente | Detalle | Estado |
|---|---|---|---|
| Velas 15m (backtest) | Cache local de CSVs (`../backtest/cache/{SYM}_15m_24m.csv` y ficheros de ventanas históricas), origen Binance | Ventanas usadas: 2024-07→2026-06 (in-sample+lockbox) y 2021-2023 (no vista); FULL 2021-26 para cesta | ✅ Verificado en código |
| Velas 15m (bot, Fase A) | `fetch_ohlcv` vía ccxt contra **Binance testnet** (`testnet.binancefuture.com`) | Solo velas cerradas (`df.iloc[:-1]`); las velas atrasadas del feed testnet se registran como eventos y NO son extrapolables a producción (anotado en diario de fase) | ✅ Verificado |
| Funding (backtest) | **Modelado**: 0.01%/8h uniforme; variante pesimista probada | **El funding real es la mayor incógnita de magnitud declarada** — Binance solo expone el último tramo histórico; con funding alto, 2024-26 queda ≈ 0 | ⚠️ Abierta; Fase B lo mide por trade |
| Costes | Modelo Zoomex: taker 0.06%/lado + slippage por símbolo (BTC/ETH 0.01% … HYPE 0.05%) | Fills del backtest optimistas en stops (declarado); variante con fills pesimistas probada | ✅ Documentado |
| Universo | BTC, ETH, SOL, BCH, DOGE (+HYPE solo backtest, descartado) | Elegido en 2026 entre majors vivos → **survivorship en la selección, declarado en la ficha** | ⚠️ Limitación aceptada |

## Sesgos conocidos y su tratamiento

| Sesgo | Riesgo | Tratamiento actual |
|---|---|---|
| Survivorship (universo de supervivientes; sin pares delistados) | Alto en generalización, medio para la cesta fija | Declarado en ficha H-001. Mitigante parcial: la tesis es la cesta fija sin selección. El Data Lake (Etapa 3) debe incluir delistados para futuras hipótesis |
| Lookahead | Alto si existiera | Señales con shift(1) sobre velas cerradas (verificado en especificación y código); replay offline de Fase A lo re-verifica en vivo |
| Funding mal modelado | Alto en magnitud del alfa | Declarado; medición real por trade en Fase B; predicción P4 de la hipótesis económica lo vigila |
| Fills optimistas en stops | Medio | Variante pesimista ya corrida (ETH/SOL aguantan); slippage real se mide en Fase B (mediana ≤5 bps de exceso) |
| Feed testnet ≠ producción (velas atrasadas) | Medio en Fase A | Eventos registrados por símbolo; tasa NO extrapolable, anotado en diario; re-evaluar al pasar a endpoint real |
| Huecos/duplicados en cache | Medio | 🔴 PENDIENTE: script de QA sobre los CSV del cache (conteo de huecos por símbolo/ventana) — primera tarea real del Auditor de Datos (A-02) |

## Reglas

1. Los datos crudos son inmutables: se versionan, nunca se corrigen in place.
2. Toda transformación es reproducible por script; nada manual.
3. El universo y período exactos de cada experimento quedan en la ficha/config de la hipótesis.
4. Los datos viven fuera de git (`data/` ignorado); los scripts que los regeneran, dentro.
5. Ningún dataset nuevo entra a investigación sin dictamen APTO de A-02.

## Data Lake (Etapa 3 — requisitos que este inventario confirma)

Recolección automatizada desde endpoint real (no testnet) · funding rate histórico completo por símbolo (la carencia nº 1 detectada) · open interest (lo exige la predicción P3 de la hipótesis económica) · inclusión de pares delistados · QA de integridad automatizado.
