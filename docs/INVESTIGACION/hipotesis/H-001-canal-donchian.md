# H-001 — Canal de Donchian sobre perpetuos USDT (Binance)

| Campo | Valor |
|---|---|
| ID | H-001 |
| Familia | Trend following |
| Mercado | Futuros perpetuos USDT, Binance |
| Estado | ⏳ EN VALIDACIÓN — Fase A (dry run) |
| Pre-registro | ⚠️ Retroactivo (la investigación original precede a este protocolo) |
| Fecha de esta ficha | 2026-07-01 |

## Hipótesis económica

> PENDIENTE — completar por el investigador.
> Formular: ¿por qué las rupturas de canal capturan una ineficiencia real en perpetuos cripto? ¿Quién está al otro lado (por qué pierde dinero el que vende la ruptura)? ¿Por qué esa ineficiencia no ha sido arbitrada?

## Regímenes esperados

> PENDIENTE — declarar antes de continuar la validación.
> ¿En qué regímenes debería funcionar (tendencia sostenida, alta volatilidad direccional)? ¿En cuáles debería perder (rango, chop)? Estas predicciones se verificarán después contra los datos, no al revés.

## Definición de la señal

- Canal de Donchian, parámetro de ventana: **512** (unidad temporal: PENDIENTE — ¿velas de qué timeframe?).
- Reglas de entrada/salida: PENDIENTE — documentar exactamente.
- Position sizing: PENDIENTE — referenciar la regla exacta usada por el backtester.

## Declaración de limitaciones epistemológicas (obligatoria)

Esta hipótesis se investigó antes de que existiera el protocolo. Deben responderse honestamente:

1. **¿Cómo se eligió la ventana 512?** ¿A priori, o tras probar variantes? PENDIENTE.
2. **¿Cuántas configuraciones se probaron en total** (ventanas, filtros, sizing)? PENDIENTE. Sin este número, ninguna métrica reportada es interpretable.
3. **¿Se aplicó corrección por pruebas múltiples** (p. ej. Deflated Sharpe)? PENDIENTE.
4. **¿El lockbox se definió antes de la investigación y se abrió una sola vez?** ¿Hay registro de la fecha de apertura? PENDIENTE.
5. **¿Los datos incluyen pares delistados?** ¿Cuál fue el universo exacto y el período? PENDIENTE.

Si alguna de estas preguntas no puede responderse con evidencia, la validación operativa (Fases A/B/C) sigue siendo válida como test de infraestructura, pero el paso a capital real (Fase C) exigirá umbrales más conservadores, definidos en `../../VALIDACION/CRITERIOS_FASES.md`.

## Resultados de investigación (a completar con números)

| Métrica | In-Sample | Out-of-Sample | Lockbox |
|---|---|---|---|
| Período | PENDIENTE | PENDIENTE | PENDIENTE |
| Sharpe | PENDIENTE | PENDIENTE | PENDIENTE |
| Max drawdown | PENDIENTE | PENDIENTE | PENDIENTE |
| Nº de trades | PENDIENTE | PENDIENTE | PENDIENTE |
| % en pocos grandes ganadores | PENDIENTE | PENDIENTE | PENDIENTE |
| Correlación con BTC | PENDIENTE | PENDIENTE | PENDIENTE |

Costes incluidos: funding real ✓ · comisiones ✓ · slippage: PENDIENTE (se medirá en Fase B).

## Limitaciones conocidas (declaradas por el investigador)

- Dependencia de pocos grandes ganadores (característica estructural del trend following).
- Alfa estadísticamente modesta.

## Validación operativa

Sigue las fases y criterios de `../../VALIDACION/CRITERIOS_FASES.md`. Los criterios deben estar completos **antes** de evaluar la Fase A.

## Registro de eventos

| Fecha | Evento |
|---|---|
| 2026-07-01 | Ficha creada; hipótesis formalizada retroactivamente dentro del nuevo protocolo. |
