# Contratos de Datos y Componentes

> Tarea 0.4 del PLAN_TRABAJO. Regla de origen: estos contratos **codifican las convenciones del sistema vivo** (eventos.csv, registro_live.csv, bot_state.json, ESPECIFICACION_OPERATIVA), no inventan nuevas. Todo componente futuro (backtester migrado, Data Lake, dashboard, H-002+) DEBE consumir estos contratos. Cambiarlos requiere ADR + plan de migración.
>
> **Regla de oro:** backtester y bot consumen los mismos contratos de vela, funding y señal. Es la única garantía estructural de que el tracking error mida ejecución y no discrepancias de definición.

## Convenciones globales (aplican a todo)

| Convención | Valor | Nota |
|---|---|---|
| Zona horaria | **UTC, siempre.** ISO-8601 con offset explícito (`2026-07-02T09:30:00+00:00`) | Ningún timestamp local en ningún archivo. Los logs humanos (bot.log) también van en UTC |
| Decimales | Punto decimal, sin separador de miles | CSVs parseables por pandas sin locale |
| Moneda | Precios y PnL en USDT (quote); cantidades en unidad base del símbolo | `qty=0.047` ETH significa 0.047 ETH |
| Símbolos | Formato ccxt de perpetuo: `ETH/USDT:USDT` | El de los archivos vivos. Para nombres de fichero se usa el ticker corto (`ETH`) |
| Archivos | CSV con cabecera, UTF-8, append-only para registros de eventos/trades | Nada se reescribe; correcciones = fila nueva o archivo nuevo |

## 1. Contrato VELA

**⚠️ La decisión irreversible nº 1:** una vela se identifica por su **timestamp de APERTURA** (convención Binance/ccxt, ya adoptada por el sistema vivo). La vela `09:30` cubre 09:30:00–09:44:59 y **cierra a las 09:45:00**.

| Campo | Tipo | Descripción |
|---|---|---|
| `dt` | ISO-8601 UTC | Timestamp de apertura (identidad de la vela) |
| `open, high, low, close` | float | Precios USDT |
| `volume` | float | Volumen en unidad base |

Reglas: (1) Solo se opera/analiza sobre **velas cerradas** — la vela en curso se descarta (`df.iloc[:-1]` en el bot). (2) Ningún indicador puede usar datos de la propia vela t para decidir en t: señales con `shift(1)` sobre el histórico previo. (3) **Trampa documentada:** toda latencia se mide contra el CIERRE real (= `dt` + 15 min), no contra `dt`. Confundirlos infla o desinfla latencias en 15 minutos exactos (ya advertido en PREREG y MONITOREO).

## 2. Contrato FUNDING

| Campo | Tipo | Descripción |
|---|---|---|
| `symbol` | str ccxt | Par |
| `ts` | ISO-8601 UTC | Momento de aplicación (cada 8h en Binance: 00/08/16 UTC) |
| `rate` | float | Tasa del tramo (0.0001 = 0.01%) |

**Convención de signo (la del registro vivo):** en el PnL de un trade, `funding` es la **contribución neta cobrada**: positivo = el trade cobró funding; negativo = lo pagó. `net_pnl = gross_pnl - fees + funding`. El Data Lake almacenará la tasa cruda; la conversión a contribución por trade es responsabilidad de quien calcula PnL.

## 3. Contrato SEÑAL

Lo que una estrategia emite. La estrategia **no sabe** de órdenes, exchanges ni fills.

| Campo | Tipo | Descripción |
|---|---|---|
| `vela_ts` | ISO-8601 UTC | Apertura de la vela cerrada que generó la señal |
| `symbol` | str ccxt | Par |
| `accion` | enum | `entrada_long` · `entrada_short` · `salida` · `reversa_long` · `reversa_short` |
| `precio_ref` | float | Close de la vela señal (referencia, no promesa de fill) |
| `qty_objetivo` | float | Tamaño objetivo en unidad base (calculado por la capa de sizing, no por la señal pura) |

Reglas: (1) Una señal por símbolo por vela como máximo. (2) El destino de toda señal es **obligatoriamente** un evento (contrato 5): ejecutada, omitida (con motivo) o descartada. Señal sin evento = violación del criterio 1 de Fase A. (3) Determinismo: mismas velas + mismo estado → misma señal, en backtester y en bot.

## 4. Contrato EXPERIMENTO

Un experimento es reproducible si `config + versión de datos + hash de código` producen el mismo resultado.

```
research/H-XXX/experiments/exp-NNN/
├── config.yaml      # entrada exacta (copia congelada, no referencia)
├── DATOS.md         # qué ficheros/versión de datos consumió (ruta + rango + hash o fecha)
├── CODIGO.txt       # hash del commit del código usado (git rev-parse HEAD)
├── metricas.json    # salida: métricas estándar (abajo)
└── trades.csv       # salida: trades con el esquema del contrato 5b
```

`metricas.json` mínimo: `periodo`, `n_trades`, `win_rate`, `net_pct`, `max_dd_pct`, `sharpe`, `n_configuraciones_probadas_acumuladas` (el contador de pruebas múltiples de la hipótesis, obligatorio).

## 5. Contrato EVENTO (observabilidad)

### 5a. Eventos de ciclo — esquema de `eventos.csv` (ya vivo, se adopta tal cual)

```
ts_utc, modo, symbol, vela_ts, evento, resultado, motivo, precio, qty, detalle
```

- `modo`: `DRY` · `TESTNET` · `REAL`
- `evento`: `senal` · `salida` · `vela_atrasada` · `datos_insuficientes` (+ futuros, solo por adición)
- `motivo` (omisiones): `kill_switch` · `max_concurrentes` · `cap_riesgo_agregado` · `qty_cero` · `min_notional`
- Garantía: la escritura de eventos es best-effort y JAMÁS altera una decisión de trading (ya implementado así).
- Extensión pendiente (post-Fase A, ya identificada en la especificación): evento propio para `orden_rechazada` por el exchange.

### 5b. Trades — esquema de `registro_live.csv` (ya vivo, se adopta tal cual)

```
trade_id, symbol, side, entry_time_signal, entry_time_fill, entry_price_signal, entry_price_fill,
exit_time_signal, exit_time_fill, exit_price_signal, exit_price_fill, qty, fees, funding, gross_pnl, net_pnl
```

- **Trampa documentada:** `entry_time_signal` lleva la APERTURA de la vela señal (contrato 1). Latencia real de fill = `entry_time_fill − (entry_time_signal + 15 min)`.
- El backtester migrado deberá emitir trades en ESTE esquema (columnas `*_fill` = simuladas) para que el dashboard compare modelo vs. live sin traducción.

## Decisiones irreversibles resumidas (las tres que no se pueden cambiar barato)

1. **Vela = timestamp de apertura, UTC.** Todo lo demás (latencias, joins de funding, replay) depende de esto.
2. **Señal ≠ orden.** La estrategia emite intención; ejecución y riesgo son capas aparte. Ya es la arquitectura del sistema y de AGENTES.md (el Ejecutor jamás es un LLM).
3. **Todo registro es append-only y todo trade/señal es trazable** señal → evento → fill → PnL por `trade_id` + `vela_ts`.
