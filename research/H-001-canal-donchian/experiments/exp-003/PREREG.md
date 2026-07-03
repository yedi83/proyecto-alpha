# exp-003 — PRE-REGISTRO (escrito ANTES de correr)

Fecha: 2026-07-03. Investigador: decisión del humano; ejecución sesión Fable 5.

## Declaración de pruebas múltiples (obligatoria)

Este es el **segundo y ÚLTIMO intento** de validar riesgo asimétrico para BTC (N=2: exp-002 con 0.15% → RECHAZADO; exp-003 con 0.125%). El investigador fue advertido de que iterar variantes tras ver resultados constituye optimización retrospectiva; se acepta este único reintento bajo la justificación operativa de abajo, y **se compromete por escrito**: si exp-003 RECHAZA, el riesgo asimétrico queda descartado definitivamente y M1 se resuelve por capital ($1,200) o por omisión documentada de BTC ($750). No habrá exp-004 de esta familia.

## Justificación (operativa, no de curva)

0.125% es el escalón mínimo razonable sobre el mínimo operativo (~0.11% hoy) que libra el min_notional de producción ($100). Advertencia registrada: margen de volatilidad de solo ~13% (notional ≈ $113) — aun si ACEPTA, habrá omisiones de BTC en picos de ATR, medidas por la métrica de "omisión simulada" en Fase B.

## Umbral de decisión — IDÉNTICO al de exp-002, sin modificación

ACEPTA si, en FULL: Sharpe(btc0125) ≥ Sharpe(base) − 0.05 **y** Calmar(btc0125) ≥ 85% de Calmar(base), **y** en ninguna ventana el maxDD empeora más de 5 pp. Cualquier otro resultado = RECHAZA. "Casi pasa" = no pasa.

## Config

Idéntica a exp-002 (código congelado, mismas ventanas, funding 0.01%/8h, paridad verificada) con RISK_MAP: BTC 0.00125, resto 0.001.
