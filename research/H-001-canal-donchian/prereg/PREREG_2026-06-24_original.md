# Donchian 512 — Lab independiente (NO es el bot de rango)

Carpeta separada a propósito. Reusa los CSV de `../backtest/cache/` pero NO toca
el motor de `iid_bot`/rango. Aquí solo se prueba **una** hipótesis: la ruptura de
canal Donchian 512 en 15m, largo y corto, sobre BTC, ETH, SOL, BCH, DOGE, HYPE.

## Hipótesis
Un canal de 512 velas (≈5.3 días en 15m) captura tendencias grandes y, al operar
poco, sobrevive al coste real de Zoomex (0.06%/lado taker + slippage).

## Parámetros CONGELADOS antes de correr (no se tunean sobre el retorno)
- Entrada: ruptura del máximo/mínimo de 512 velas (con shift(1), sin lookahead).
- Salida: canal opuesto de 256 velas (estilo Turtle) con piso catastrófico 3×ATR(14).
- Sizing: riesgo 0.5% del equity por trade; apalancamiento máx 3x; compounding.
- Coste por lado: taker 0.06% + slippage {BTC/ETH 0.01%, BCH 0.02%, SOL 0.03%, DOGE 0.04%, HYPE 0.05%}.
- Ventana común: 2024-07-05 → 2026-06-21 (HYPE: 2025-05-30 → 2026-06-21, MENOS muestra).

## Criterio de ÉXITO (pre-registrado)
Para CADA activo, la estrategia "tiene pulso" solo si cumple las 3:
1. NETO de costes > 0.
2. NETO > Buy&Hold del mismo activo y ventana (alfa > 0).
3. Estable: alfa > 0 en la MAYORÍA de los 4 segmentos temporales **y** en el lockbox.

Si no cumple las 3, la hipótesis está MUERTA para ese activo. Matarla barato es
una victoria.

## Validación (no es solo "correr y ver")
- 4 segmentos temporales independientes (jackknife en el tiempo): ¿es estable o
  depende de un tramo?
- Lockbox = último 20% del histórico, juzgado aparte como confirmación.
- 6 activos = jackknife en activos: ¿es un patrón o suerte de uno?
- Como NO se optimizan parámetros, no hay "entrenamiento": el riesgo no es
  sobreajuste de parámetros sino confundir beta (mercado alcista) con alfa.

## MI PREDICCIÓN (registrada ANTES de correr)
- Pocas operaciones por activo (decenas, no cientos): el coste pesará poco. Bien.
- El NETO será positivo en varios activos, pero **por beta**: 2024-2026 fue
  alcista en cripto. Apuesto a que **NO le gana al Buy&Hold** en la mayoría
  (alfa ≤ 0), sobre todo en BTC/ETH/SOL.
- Los CORTOS pierden en conjunto (mercado mayormente alcista).
- HYPE puede verse "mejor" por ventana favorable y corta — sesgo, no edge.
- Veredicto probable: MUERTA por "sin alfa" en casi todos. Si me equivoco, lo digo.

(Registrado el 2026-06-24, antes de ejecutar backtest_donchian512.py)
