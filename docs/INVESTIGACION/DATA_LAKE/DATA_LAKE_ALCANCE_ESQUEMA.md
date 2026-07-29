# Data Lake — Alcance y esquema (documento de diseño)

> **Fecha: 2026-07-26 · v2 · Autor: Opus (Claude) sobre el plan del IP · Estado: CONTRATO CONGELADO por aprobación del IP (2026-07-26).** No se modifica el alcance; cambios futuros = nueva versión con justificación.
> **Esto NO es código, NO es un recolector, NO es una hipótesis nueva.** Es el contrato de datos a **congelar antes** de construir nada (generalización de ADR-0010: fuente y esquema primero, código después).
> **Gobernanza:** el C-001 está cerrado; este diseño es material para el **F0 del C-002** (moratoria ADR-0004). No modifica ningún experimento en curso.

## 0. Decisiones metodológicas congeladas (el contrato en 8 puntos)

1. **Visión:** Data Lake histórico **amplio y reutilizable** del mercado cripto, **no diseñado para una sola hipótesis**.
2. **Point-in-time = ley fundamental.** El universo elegible se determina con la información disponible **en cada fecha histórica**: *fecha t → información en t → universo elegible en t → señal → operación*.
3. **Estratificación:** inicialmente **por liquidez as-of** (turnover/volumen medio, derivable del OHLCV), **no** por market cap actual. Los tiers de capitalización quedan como **extensión futura condicionada a datos históricos de supply** (fuente extra, con su propio point-in-time).
4. **Instrumentos separados** — el universo distingue explícitamente por tipo:
   - **Perpetuos UM** → Carry / Funding.
   - **Spot** → ILLIQ y estrategias cross-sectional.
   - **Otros instrumentos** → extensiones futuras.
5. **V1 acotada:** construir primero **perps UM + su spot correspondiente + funding + delistados**, a granularidad **15m/1h**. OI y universos adicionales quedan para incrementos posteriores.
6. **Pin de datos:** cada experimento **registra los hashes del manifiesto exacto** del slice usado → reproducibilidad byte a byte (como exp-008).
7. **A-02:** no basta validar archivos sueltos. Debe verificar **integridad + coherencia + cobertura**, incluyendo una **auditoría contra un censo externo** para detectar survivorship.
8. **Separación de capas:**
   `Data Lake` (almacena evidencia histórica) → `QA/A-02` (certifica integridad, cobertura, trazabilidad) → `F0 C-002` (formula la pregunta) → `F1–F7` (investiga y filtra).
9. **Regla de uso vs. promoción (COMPUERTA DURA):** el Data Lake **puede usarse como infraestructura de investigación antes de estar certificado**, pero **ningún resultado experimental que dependa de él puede considerarse evidencia válida para promoción hasta que el slice de datos utilizado tenga QA/A-02 CONFORME y su manifiesto esté pineado.** Explorar con datos no certificados: permitido. Promover con ellos: prohibido. Así el entusiasmo por el C-002 no puede presionar a la infraestructura para producir datos "suficientemente buenos".

## 1. Principio rector

**El Data Lake NO se diseña para validar Carry. Se diseña como infraestructura reutilizable** para cualquier investigación que requiera universo histórico amplio, activos delistados y datos reproducibles. Construir una tubería para el Carry (o para H-002) y luego rehacerla para `ILLIQ-MR-001`, microestructura u otras hipótesis es el error que este principio previene. El Carry es *un consumidor* del lago, no su especificación.

## 2. Distinción epistémica (la afirmación correcta)

**LUNA (tarea #26, verificado 2026-07-26) demuestra que el bloqueo técnico de AC-8 es RESOLUBLE. NO demuestra que el universo histórico esté libre de survivorship.** Por eso, y hasta que A-02 audite el censo y emita dictamen, la afirmación correcta NO es *"el Data Lake está libre de survivorship"* sino **"el Data Lake está DISEÑADO PARA CONTROLAR survivorship"**. La cobertura no se declara: se **demuestra** por el proceso de §5. Afirmar lo contrario antes del dictamen sería la sobre-afirmación que el laboratorio evita.

## 3. Universo, instrumentos y estratificación

- **Universo objetivo:** todo el mercado histórico con fuente (≈2019-11+), guardando el crudo **completo** (vivos **y** delistados). La estratificación y el filtrado son *downstream* (de cada hipótesis), no del lago.
- **Separación por instrumento (decisión #4):** el "universo elegible en t" es **específico por tipo de instrumento**. Una small-cap sin perp no es elegible para una estrategia de perps; el corte transversal de iliquidez probablemente vive en spot. El lago guarda ambos, pero cada hipótesis declara *sobre qué instrumento* corre.

  | Instrumento | Consumidor típico | En V1 |
  |---|---|---|
  | Perpetuos UM | Carry / Funding | **Sí** |
  | Spot | ILLIQ, cross-sectional | **Sí (el correspondiente a los perps)** |
  | COIN-M, opciones, otros | Extensiones futuras | No |

- **Point-in-time (decisión #2):** exige `listing_date` + `delisting_date` por símbolo como dato de primera clase. Sin esto, cualquier corte transversal amplio mete look-ahead.
- **Estratificación por liquidez as-of (decisión #3):** el tier (alta/media/baja liquidez) se calcula **con datos disponibles hasta t** (p.ej. turnover trailing), nunca con el dato de hoy — o se reintroduce look-ahead en la propia estratificación. Tiers por market cap = extensión futura (requiere supply histórico, fuente aparte).
- **Delistados:** se incluyen **siempre** en el crudo, marcados con `delisting_date` y motivo si se conoce. Nunca se omite un delistado "porque ya no cotiza" — es justo lo que mata el survivorship.

## 4. Datasets — tabla de requisitos (contrato)

| Requisito | Necesidad | Fuente candidata | Cobertura histórica | Delistados | Integridad | Estado | Bloqueante |
|---|---|---|---|---|---|---|---|
| **OHLCV (klines)** | Base de todo | binance.vision `futures/um/klines` + `spot/klines` | 2019-11+ | **Sí (verificado, LUNA)** | `.CHECKSUM` sha256 | **LISTO** | No |
| **Funding rate** | Carry, coste real | binance.vision `futures/um/fundingRate` | 2019-11+ | Sí (probable; verificar) | `.CHECKSUM` | ALTO | No — **capturar `interval` por evento** (8h→4h/1h con caps; asumir 8h corrompe el Carry) |
| **Spot real** | Carry AC-9 (descomposición funding/base), ILLIQ | binance.vision `spot/klines` | Por símbolo, si hay par spot | Parcial (spot puede delistar en otra fecha que el perp) | `.CHECKSUM` | MEDIO | **Sí, parcial** — ver trampa multiplicador |
| **Open Interest** | Predicción P3, capacidad AC-4 | binance.vision `futures/um/metrics` (limitado) **o** Tardis | metrics: fecha tardía, granularidad gruesa; Tardis: 2020-05+ | metrics: dudoso para delistados | — | **BAJO en gratis** | **Sí — probablemente exige Tardis (pago). Fuera de V1.** |
| **Metadatos listado/delisting** | Point-in-time, anti-look-ahead | Anuncios Binance / `exchangeInfo` / lista Tardis | — | **Crítico** | — | **POR DEFINIR** | **Sí — sin esto no hay universo point-in-time** |
| **Order book L2** | Microestructura, capacidad fina | Tardis (pago) | 2019-11+ | Sí | secuencia `pu`/`u` | **FUERA de alcance** | Diferido (bajo demanda) |

**Trampas registradas (no olvidar al construir):**
- **Multiplicador spot↔perp:** `1000SHIB`/`1000LUNC`/`1000PEPE` cotizan el perp en ×1000; el spot es el token base. El contrato lleva `perp_symbol → spot_symbol → multiplicador`, o la descomposición AC-9 sale mal por un factor de 1000.
- **OI = eslabón débil del camino gratis:** candidato #1 a pagar Tardis; no darlo por hecho. Fuera de V1.

## 5. Prueba de cobertura (auditoría de survivorship) — DEMOSTRAR, no declarar

Entregable con dictamen A-02 (no una afirmación):

1. **Censo independiente:** lista de *todos los símbolos que existieron* desde una fuente **externa** a binance.vision (anuncios Binance / símbolos Tardis / CoinGecko). Es el denominador.
2. **Inventario real:** enumerar lo que binance.vision efectivamente tiene (recorrido del bucket S3).
3. **Delta:** símbolos del censo ausentes, clasificados por causa (nunca hubo dump / purgado / fuera de rango).
4. **Reporte de cobertura:** % + lista de faltantes + su materialidad (¿relevantes para carry/ILLIQ o no?).
5. **Spot-check de cola:** además de LUNA, N delistados con su cola verificada hasta `delisting_date`.

Solo con este reporte APTO se puede pasar de *"diseñado para controlar survivorship"* a *"cobertura X% demostrada"*.

## 6. QA / A-02 — definido ANTES del recolector (integridad + coherencia + cobertura)

- **Checksums:** sha256 vs `.CHECKSUM` del origen.
- **Huecos temporales:** velas/eventos faltantes por símbolo e intervalo.
- **Duplicados:** timestamps repetidos.
- **Timestamps:** monótonos y unidad correcta (binance.vision pasó a **microsegundos** desde 2025-01; detectar ms vs µs por rango, no asumir).
- **Precios razonables:** rangos/saltos absurdos (0, negativos, ×10^n).
- **Funding:** intervalo correcto por evento; spot↔perp realmente correspondientes (multiplicador).
- **Continuidad:** sin saltos entre archivos mensuales.
- **Consistencia de símbolos:** nombre estable, multiplicadores declarados, sin colisiones de renombrado.
- **Series truncadas:** distinguir fin por *bug de recolección* de un delisting real (cotejar `delisting_date`).
- **Universo respeta existencia:** cada símbolo solo aparece entre su `listing_date` y `delisting_date`.
- **Cobertura (§5):** auditoría contra censo externo — survivorship.
- **Reproducibilidad / pin (decisión #6):** que *los datos usados en una investigación sean exactamente los archivados* → cada experimento fija los hashes del manifiesto del slice consumido.

Ningún dataset entra a investigación sin **dictamen A-02 APTO** (regla 5 de `DATA.md`).

## 7. Estructura de almacenamiento (capas — decisión #8)

```
data/                      (fuera de git — regla 4; solo scripts/manifests/qa se versionan)
├── raw/                   fuente ORIGINAL, inmutable (bytes + .CHECKSUM del origen). Nunca se corrige in place (regla 1).
├── normalized/            esquema canónico: tipado, UTC en ms, generado POR SCRIPT desde raw (nunca a mano).
├── qa/                    un reporte de controles por dataset/corrida (§6).
└── manifests/             por archivo: sha256 (raw y normalized), fecha de extracción, URL de origen, versión del script.
```

- **`raw/` es sagrado:** si la fuente corrige un archivo, entra como **nueva versión** con nuevo hash, no se sobre-escribe.
- **Trazabilidad:** `manifests/` responde siempre "¿de dónde salió este byte y cuándo lo bajé?".

## 8. Contrato de datos a congelar (esquemas canónicos normalizados)

Antes del recolector, congelar el esquema `normalized/` (esbozo a ratificar):

- **OHLCV:** `symbol, instrument_type, open_time_utc_ms, open, high, low, close, volume, quote_volume, trades, close_time_utc_ms`.
- **Funding:** `symbol, funding_time_utc_ms, funding_rate, funding_interval_hours, mark_price`.
- **Metadatos:** `symbol, instrument_type, base_asset, quote_asset, multiplier, spot_symbol, listing_date, delisting_date, status`.

## 9. V1 acotada vs visión completa (guardarraíl de scope)

**Esquema/contrato = visión completa** (extensible). **Primera recolección = V1 mínima** que desbloquea lo cercano:

- **V1:** perps UM + su spot correspondiente + funding + **delistados incluidos**, a 15m/1h.
- **Diferido a incrementos posteriores:** OI (vía Tardis), universos solo-spot de baja cap, order book L2, COIN-M/opciones, tiers por market cap.

Construir el esquema completo **no obliga** a llenar el lago completo de una. Esto evita el cathedral-building que hunde las infra.

## 10. Orden de ejecución (decisión del IP) + regla de paralelismo

1. **Congelar** alcance/esquema (este doc). 2. **Especificar** QA/A-02 en detalle. 3. **Construir** el recolector V1 contra el contrato congelado. 4. **Recolectar** V1. 5. **Ejecutar** QA/A-02 (integridad + cobertura). 6. **Con datos certificados**, retomar el **F0 del C-002**.

> **Regla de paralelismo (decisión #9):** el F0 del C-002 **no tiene que esperar** a que exista todo el Data Lake — puede formularse y explorar en paralelo. Pero **ningún resultado que dependa de datos aún no certificados por A-02 (con manifiesto pineado) puede presentarse como evidencia de promoción.** Explorar sí; promover no. Así infraestructura e investigación avanzan sin contaminarse.

## 11. Lo que este documento NO hace (honestidad)

No implementa nada, no fija el universo final de símbolos, no cotiza Tardis, **no afirma que el universo esté libre de survivorship** (lo *diseña para controlarlo*, §2/§5), y no valida ninguna hipótesis. Es el contrato; la ejecución viene por pasos y con dictámenes.
