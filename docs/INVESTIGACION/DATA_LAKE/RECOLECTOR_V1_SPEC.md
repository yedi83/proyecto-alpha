# Recolector V1 — Especificación (universo + estructura raw/manifiesto)

> **Fecha: 2026-07-29 · Alcance: pequeño pero representativo.** Objetivo: que el **archivo real** responda las preguntas empíricas que el diseño abstracto no cerró (ruleset R8). NO recolectar "la mayoría de las criptos": una muestra estratificada que **fuerce** a la fuente a mostrar su comportamiento. El raw **nunca** se transforma ni se "arregla".

## 1. Universo inicial — **CONGELADO 2026-07-29** (22 símbolos)

> Lista **fija antes del primer run** (condición del IP): así distinguimos "no estaba en el universo elegido" de "lo intentamos y la fuente no lo tenía". Un símbolo que no exista en binance.vision **NO se borra ni se corrige** — queda en `errors_{run}.jsonl`. La ausencia es un dato.

| Estrato | Símbolos (perp USD-M salvo nota) | Por qué está |
|---|---|---|
| H-001 (base + estudio) | `BTCUSDT` `ETHUSDT` `SOLUSDT` `BCHUSDT` `DOGEUSDT` | Los 5 de H-001; historia larga; alta liquidez |
| Large caps extra | `BNBUSDT` `XRPUSDT` | Liquidez alta, distinta a BTC |
| Mid caps | `LINKUSDT` `LTCUSDT` `ATOMUSDT` `AVAXUSDT` | Banda intermedia de liquidez |
| Small caps / baja-liq | `CVCUSDT` `FLMUSDT` `DENTUSDT` `STMXUSDT` | Donde muerden fills / iliquidez / reversión (tier real a confirmar por volumen) |
| Delistados | `LUNAUSDT` `FTTUSDT` `SRMUSDT` `ANCUSDT` | Retención de la cola del deslistado (LUNA crash; FTT/SRM/ANC ecosistemas colapsados) |
| Caso especial multiplicador | `1000LUNCUSDT` `1000SHIBUSDT` | Rename/fork + multiplicador ×1000: caso `perp→spot→mult` |
| Delistado antiguo (sonda) | `COCOSUSDT` | Borde temprano: ¿hasta dónde llega la historia gratuita? |

## 1bis. Resolución por símbolo (1d / 1h / 15m)

- **`1d` → los 22** (historia completa): prueba de **cobertura histórica + detección de delisting**. Barato.
- **`1h` → subconjunto de estudio (8):** los 5 de H-001 (`BTC ETH SOL BCH DOGE`) + `LUNAUSDT` + **2 small caps** (`FLMUSDT`, `DENTUSDT`) — como los 5 de H-001 son todos líquidos, se añaden **dos** small caps para tener el caso de baja liquidez (condición del IP).
- **`15m` → grupo mínimo (2):** `BTCUSDT` + `FLMUSDT` — solo para probar **granularidad y tamaño del pipeline**, no para estudio. V1 no necesita 15m para todo.
- **Funding:** todos los perps USD-M del universo.
- **Spot:** el correspondiente donde exista (mapeo `perp→spot`, ojo `1000SHIB→SHIB`, `1000LUNC→LUNC`); `1d` para todos los mapeables, `1h` para el subconjunto de estudio.

## 2. Datos a bajar por símbolo (sin transformar)

- **Klines `1d`** — historia completa (todos los meses disponibles). Barato; sirve para **cobertura histórica + detección de delisting** (hasta qué mes llega la serie).
- **Klines `1h` y/o `15m`** — **solo** para el subconjunto que realmente se vaya a estudiar (no para todos: ahorra almacenamiento).
- **Funding** (`fundingRate`) — para los perps.
- **Spot correspondiente** — `spot/klines` del símbolo base, **cuando exista** (mapear `perp→spot`; ojo multiplicadores `1000*`).
- **Metadata del instrumento** — snapshot de campos de `exchangeInfo` (base/quote asset, multiplicador, status, fechas si las hay).

## 3. Estructura del raw (inmutable) + manifiesto

```
data/                                  (fuera de git — regla 4)
├── raw/binance_vision/
│   ├── futures_um/klines/{SYMBOL}/{INTERVAL}/{SYMBOL}-{INTERVAL}-{YYYY-MM}.zip   (+ .CHECKSUM del origen)
│   ├── futures_um/fundingRate/{SYMBOL}/{SYMBOL}-fundingRate-{YYYY-MM}.zip        (+ .CHECKSUM)
│   ├── spot/klines/{SPOT_SYMBOL}/{INTERVAL}/{SPOT_SYMBOL}-{INTERVAL}-{YYYY-MM}.zip (+ .CHECKSUM)
│   └── metadata/{SYMBOL}.exchangeInfo.json
├── manifests/
│   ├── manifest_{run_id}.jsonl        (un objeto por archivo bajado — fuente de verdad del run)
│   └── errors_{run_id}.jsonl          (un objeto por símbolo/mes NO encontrado o con problema)
```

**Esquema del manifiesto (una línea JSON por archivo raw):**
```
{ "run_id", "file_path", "symbol", "instrument_type",        // futures_um | spot | coin_m
  "data_type",                                                // klines | fundingRate | metadata
  "interval",                                                 // 1d/1h/15m/null
  "period_yyyymm", "source_url",
  "capture_date_utc",                                         // R4: FECHA DE CAPTURA, separada del periodo
  "sha256", "bytes",
  "origin_checksum_present", "checksum_verified" }            // R1
```

**Esquema del log de errores (una línea por hueco):**
```
{ "run_id", "symbol", "data_type", "interval", "period_yyyymm",
  "reason",                                                   // not_found_404 | http_error | checksum_mismatch | zip_corrupt
  "http_status", "capture_date_utc" }
```

**Invariantes (del ruleset):**
- **R1** — SHA-256 de cada archivo crudo; verificación contra `.CHECKSUM` del origen cuando exista.
- **R4** — `capture_date_utc` en **cada** objeto del manifiesto.
- **Raw inmutable** — se guardan los bytes originales; **nada** se descomprime, normaliza ni corrige en `raw/`.
- **Ausencia visible** — todo símbolo/mes no encontrado va al log de errores; el hueco es un dato explícito, no silencio.

## 4. Preguntas empíricas que las ~2 semanas deben responder (R8)

1. **¿La cola del deslistado está completa?** ¿Hasta qué mes/precio llega cada delistado (LUNA, FTT, SRM) antes de cortarse? ¿Coincide con su delisting real?
2. **¿El censo es reconstruible y hasta dónde?** ¿Cuántos de los símbolos sospechosos/delistados aparecen vs cuántos van al log de errores? El log **es** el primer censo empírico de huecos.
3. **¿Hay restatements?** Re-descargar un subconjunto tras N días y comparar SHA-256: ¿binance.vision reemite archivos históricos?
4. **¿Cómo se ven las migraciones?** ¿`1000LUNC` / `1000SHIB` / `BTCUSD_PERP` aparecen como símbolos separados, con qué historia y qué relación con el símbolo base?

El dataset resultante —y sobre todo su **log de errores**— reescribe el A-02 definitivo. Eso es lo que cinco pases abstractos no podían producir.
