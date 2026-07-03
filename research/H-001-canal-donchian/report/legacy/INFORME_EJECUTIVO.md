# INFORME EJECUTIVO — Donchian 512 (cesta cripto, 15m)
Proyecto: crypto_iid_rango / donchian512_lab. Datos: Binance Futuros 2021-07 a 2026-06.
Estado: FASE A (DRY_RUN) EN CURSO desde 2026-07-02 03:53:46 UTC — acta y
criterios pre-registrados en PREREG_FASE_AB.md. Actualizado: 2026-07-02.

## 1. Objetivo
Determinar si una ruptura de canal Donchian 512 en 15m sobre una cesta cripto
tiene edge real tras costes y ejecucion. Filosofia: matar hipotesis barato.

## 2. Clasificacion final (veredicto de comite)
Hipotesis de tendencia DESCORRELACIONADA, mecanismo REPETIBLE, evidencia
prometedora pero CONFIANZA ESTADISTICA MODERADA-BAJA.
=> No archivar. No capital significativo. Sizing acorde a la confianza. NO es edge probado.

## 3. Que se probo y que MURIO (matado barato)
- Donchian 20 / churn 15m -> muerto por coste por vuelta.
- BTC, BCH, HYPE individuales -> sin alfa en ventana base.
- Filtro "vigia" de tendencia -> medido y descartado (alta tendencia rinde igual/peor).
- Filtro de regimen "solo bear" -> REFUTADO (gana LONG en bull, no en bear).
- Seleccion de activos por rendimiento -> PROHIBIDO: ranking anti-transferible (Spearman -0.90).
- Tope nocional 25-100% -> destruye la cesta.
- NEAR (jun-2026) -> RECHAZADO (ver seccion 8).

## 4. Que SOBREVIVIO (validaciones)
- Costes reales (taker 0.06%/lado + slippage) + FUNDING REAL: neto positivo (+$8.503).
- Walk-forward por segmentos + lockbox: estable.
- Otra ventana 2021-2023 (no vista): alfa positiva -> no era solo el regimen 2024-26.
- Bootstrap por bloques (10.000): positivo en 75%, Sharpe mediana 0.43.
- Estructura top-trades: 14 episodios independientes (mecanismo repetible).

## 5. Naturaleza REAL (narrativa corregida por los datos varias veces)
- NO es crisis-alpha (gana LONG en bull, no shorteando bears).
- NO es beta disfrazada: beta vs cesta = 0.006, R2 = 0.000 (descorrelacionado).
- Trend market-neutral; el PnL sale del lado LARGO; los shorts dan la neutralidad.
- Alfa ~+10-11.6%/año neto PERO t=0.94 -> NO significativo.
- FRAGIL: ~5 trades cargan todo el PnL (quitar top-5 -> negativo). Convexidad
  tipo trend-following: muchas perdidas pequeñas, pocas ganancias enormes.

## 6. PARAMETROS CONGELADOS (entrada/salida/sizing)
- Universo: BTC, ETH, SOL, BCH, DOGE (USDT-perp Binance). Equiponderado. SIN seleccion.
- Timeframe: 15m, solo velas cerradas.
- Entrada LONG: plano y close > maximo(512)[shift1]. SHORT: close < minimo(512). Largo y corto.
- Salida: canal opuesto 256 (Turtle) + stop catastrofico 3xATR(14). Reversa en ruptura opuesta.
- Sizing: riesgo 0.10%/trade via stop ATR; apalancamiento max 3x/trade.
- Riesgo cartera: max 5 concurrentes; cap agregado 0.6%; kill-switch diario -5%.
- Apalancamiento exchange: 1-2x (encoded 2x). Margen: AISLADO.
- Ver detalle exacto en ESPECIFICACION_OPERATIVA.md.

## 7. Resultados con la config DESPLEGADA (0.10%/trade, sin vol-target)
Backtest FULL 2021-26 (cesta 5). OJO: son DOS corridas distintas (corregido 2026-07-01;
la version anterior las mezclaba como si fueran una sola):
- Corrida A (risk 0.10%, funding SUPUESTO 0.01%/8h): Neto +24% (5 años) | maxDD -18%
  | Sharpe 0.42 | Calmar 1.35. NO incluye funding real.
- Corrida B (risk 0.25%, funding REAL, export_trades+funding_apply): recorte funding
  -12.8% sobre neto fees; PnL neto fees+funding +$8.503 (1.884 trades).
- PnL por activo (de la corrida B): SOL 35%, ETH 30%, BCH 17%, DOGE 13%, BTC 6%.
- PENDIENTE: no existe corrida a 0.10% con funding REAL; regenerar export a 0.001.
- Sensibilidad a ejecucion de stops (exp. 2026-07-01, flag stop_fill en backtest_cesta):
  fill al stop vs fill al CLOSE de la vela (replica del bot, que evalua stops en vela
  cerrada): FULL +24.0%->+25.4%, Sharpe 0.42->0.44 -> INSENSIBLE a la politica de fill.
  Lo que el experimento NO cubre: bot caido en crash sin stop residente (riesgo de cola).
Variante OPCIONAL (NO desplegada): +vol-target 15% sube Sharpe a 0.58 / Calmar 2.38,
pero su mejora es de regimen (bear 2022) -> fuera por simplicidad/robustez.

## 8. NEAR — caso de estudio (rechazado, la disciplina funcionando)
Motivo de la consulta: "se comporta muy bien ultimamente". Analisis por regimen:
| ventana | NET% | B&H% | ALFA% | Sharpe |
|---|---|---|---|---|
| 2021-23 | -4.5 | -38.7 | +34.2 | -0.30 |
| 2024-26 | +2.9 | -52.5 | +55.4 | +0.22 |
| FULL | +1.5 | -0.4 | +1.9 | 0.08 |
| reciente abr-jun26 | +4.9 | +44.2 | -39.3 | 3.16 |
- Sharpe 0.08 (vs 0.42 de la cesta) = VEHICULO PEOR. Net apenas positivo/negativo.
- Su "buen comportamiento" reciente = el PRECIO de NEAR volo +44%; la estrategia
  capturo solo +4.9% (alfa -39%). Ilusion de beta/recencia.
- LECCION: mi criterio pre-registrado ("alfa>0 en ambos regimenes") fue DEMASIADO
  BLANDO (NEAR lo pasa solo porque su B&H se hundio). Barra correcta: Sharpe >= al
  de la cesta Y net positivo. NEAR no la pasa. Veredicto: FUERA.
- Regla reafirmada: no se añade por rendimiento reciente; la barra es ">= lo que ya tengo".

## 9. CAPA OPERATIVA (construida y en marcha)
- bot/live_bot.py: ejecuta la logica congelada en testnet/real (mismo codigo, flag).
  Incluye: solo velas cerradas, guard de frescura (sincronia con cierres Binance),
  funding REAL por trade, guards (min-notional, max 5, cap agregado, kill-switch),
  recuperacion de estado + reconciliacion con exchange tras caida/apagon, auto-config
  de apalancamiento/margen, logging a bot/logs/bot.log.
- bot/lanzar_bot.bat: lanzador con auto-reinicio.
- bot/check_sizing.py: a $750 los 5 simbolos PASAN (BTC borderline en alta volatilidad).
- paper/dashboard.py: tracking error (PnL live vs modelo), slippage, funding.
- auditoria.py + tarea programada diaria 9:05: revisa señales/errores/reinicios/registro/sizing.
- Monitoreo en 3 niveles (2026-07-02): vigia.py (tiempo real, cada 15 min),
  auditoria.py extendida (diaria, criterios fase A), checklist semanal -> MONITOREO.md.
- paper/eventos.csv (añadido 2026-07-01, solo observabilidad): registro unificado de
  eventos — señales ejecutadas/OMITIDAS con motivo, salidas, velas atrasadas. Hace
  visible el PnL fantasma de trades omitidos (invisible para el tracking error) y
  discrimina retrasos de datos por símbolo. No toca la lógica de trading.

## 10. Validacion cruzada (confianza en la implementacion)
El Pine de TradingView y el backtest de Python dan IDENTICO en ETH 15m
(30abr-26jun): 13 operaciones, 3 ganadoras / 10 perdedoras, 23% win-rate.
Confirma que ambas implementaciones son la misma estrategia. Win-rate 23% y ~6
trades/mes/activo = comportamiento esperado.

## 11. Bugs cazados en PAPER (valor de la fase, sin arriesgar dinero)
- KeyError heartbeat ('posiciones' vs 'positions') -> corregido.
- iso() fallaba con numpy.int64 (podia perder registros de entrada) -> corregido.
- Kill-switch falso al cambiar PAPER_EQUITY a media jornada -> robustecido en DRY_RUN.
- PAPER_EQUITY: el DRY_RUN dimensionaba a $10k en vez de $750 -> configurable, default 750.
Todos en la capa operativa; la LOGICA DE TRADING quedo intacta desde que se congelo.

## 12. Incognitas restantes (NO resolubles por backtest)
- EJECUCION real: slippage/fills en el momento de las ~5 capturas clave, latencia,
  uptime. -> se valida con paper/testnet + tracking error.
- Persistencia futura del trending cripto (apuesta de fondo).

## 13. Plan operativo (fases)
A) DRY_RUN minimo 10 dias. [EN CURSO desde 2026-07-02 03:53:46 UTC] Criterios
   pre-registrados (PREREG_FASE_AB.md): instrumentacion y coherencia, NO PnL.
B) Testnet real 1 mes. Criterios pre-registrados: TE acumulado ±5% del PnL
   modelo, slippage mediana <=5 bps de EXCESO sobre lo modelado (p95 vigilado),
   cero omisiones min_notional en BTC sin decision documentada.
C) Real ~$750, aislado, 1-2x, sizing 0.10%. Solo si A y B aprueban todo.
Regla de oro: NO tocar parametros. El riesgo ahora es destruir lo que sobrevive
por seguir optimizando.

## 14. Mapa de archivos clave
- backtest_donchian512.py, grid_frontier.py, backtest_cesta.py ... backtests/frontera.
- robustez_boot.py, analisis_cartera.py, top_trades_estructura.py, alfa_beta.py ... validaciones.
- funding_apply.py, export_trades.py, descargar_funding.py ... funding real.
- bot/ (live_bot.py, lanzar_bot.bat, check_sizing.py, config.example.env) ... ejecucion.
- paper/ (dashboard.py, ver_dashboard.bat, registro_live.csv) ... validacion operacional.
- ESPECIFICACION_OPERATIVA.md, ARRANQUE.md, GUIA_OPERACION.md ... operativa.
- *_VEREDICTO.md / RESULTADO_*.md ... cadena de veredictos por test.
- PREREG_FASE_AB.md, DIARIO_FASE_A.md, MONITOREO.md, vigia.py ... fase A:
  pre-registro, diario de incidencias, monitoreo en 3 niveles (2026-07-02).

## 15. Auditoria de divergencias modelo<->ejecucion (sesion 2026-07-01/02)
Revisados: fills, fees, funding, redondeos, sizing, timestamps, sincronizacion
de velas, ejecucion de stops, reconciliacion. Hallazgos:
- Fills de stop: backtest llena AL NIVEL del stop; el bot evalua en vela
  cerrada y sale a mercado. Experimento (flag stop_fill): INSENSIBLE
  (FULL +24.0%->+25.4%, Sharpe 0.42->0.44). Ver seccion 7.
- Redondeo de qty: peor caso ±3% del riesgo objetivo (BTC) -> despreciable.
- Sizing live: fetch_balance (ccxt->fapi v3 account) devuelve marginBalance =
  INCLUYE PnL no realizado; el backtest dimensiona con equity realizado.
  Divergencia pro-ciclica pequeña. Prueba de plomeria pendiente en testnet.
- DRY_RUN: fees=0 en el registro -> el tracking error tiene sesgo positivo
  estructural (~ +fees modeladas). Se interpreta con ese descuento.
- Existen TRES "modelos" distintos: backtest (taker + slippage doblemente
  contado + penalidades = conservador), modelo del dashboard (solo taker a
  precios de señal) y ejecucion real. TE~0 significa replicar el modelo del
  dashboard, NO ganar lo del backtest.
- Retraso BCH 29-jun (entrada 1 ciclo tarde): bot puntual segun logs; causa =
  feed de datos. El bot toma klines de testnet.binancefuture.com -> velas
  atrasadas ESPERABLES en fase A y NO extrapolables a produccion.
- Punto ciego corregido: trades omitidos eran invisibles para el TE ->
  eventos.csv los registra con motivo (min_notional, caps, kill-switch).
- Riesgo de cola NO cubierto por backtest ni TE: bot caido durante crash sin
  stop residente en exchange. Mitigacion opcional (stop reduce-only) pospuesta
  deliberadamente; ver ESPECIFICACION_OPERATIVA.
- Correccion documental: la seccion 7 mezclaba dos corridas (0.10% funding
  supuesto vs 0.25% funding real); corregida con procedencias explicitas.
