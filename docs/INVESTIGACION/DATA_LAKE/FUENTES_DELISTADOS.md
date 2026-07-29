# Data Lake — Fuentes de pares delistados (investigación de fuentes)

> **Fecha: 2026-07-26 · Autor: Opus (Claude) para el IP · Estado: HALLAZGOS, no decisión.**
> Objetivo: responder la pregunta que puede hundir el Data Lake — *¿de dónde salen los pares delistados?* Es el bloqueante #1 (survivorship de la cola del carry-crash, F6 AC-8; y AI-1 de ILLIQ). Sin fuente viable, el Data Lake nace cojo.
> Alcance: solo **fuentes** (cobertura, coste, formato, sesgos). NO es diseño del esquema ni recolector. NO es un dictamen A-02.

## 1. Resumen ejecutivo

Hay **dos caminos viables y complementarios**, y el problema es **menos grave de lo temido**:

1. **`data.binance.vision` (oficial, GRATIS)** — dumps diarios/mensuales por símbolo de klines, funding rate, trades y aggTrades para futuros USD-M y COIN-M. El README oficial afirma *"All symbols are supported"* y los archivos son **inmutables por símbolo/fecha** con `.CHECKSUM` de integridad. Todo indica que **retiene los delistados** (el propio ejemplo del README usa `ADABKRW`, un par ya delistado). **Es el candidato a fuente primaria.**
2. **`Tardis.dev` (PAGO)** — datasets explícitamente **survivorship-bias-free**: incluyen instrumentos *delistados, expirados o renombrados*. Binance USD-M desde 2019-11-17, con funding (markPrice), open interest (desde 2020-05-12) y **order book L2 real**. Es el estándar de oro para delistados y lo único que da profundidad de libro. **Candidato a complemento**, no a base (por coste y granularidad).

**El "no se puede" que temíamos no aplica:** la historia de delistados sí es obtenible.

> **✅ VERIFICADO 2026-07-26 (tarea #26, corrido por el IP):** se descargó de `data.binance.vision` el `klines` + `fundingRate` de **LUNAUSDT** (delistado mayo-2022) y **la cola del colapso SÍ está presente**. Esto era el peor caso exacto que F6 citó (AC-8: cola del carry-crash censurada por survivorship). El go/no-go del camino gratis **PASÓ**. Caveat de rigor: es **un** símbolo (el canónico peor-caso); al definir el universo conviene un spot-check de 1-2 delistados más, pero la señal es fuerte.

## 2. Fuentes evaluadas

| Fuente | Coste | Delistados | Qué da | Formato | Veredicto |
|---|---|---|---|---|---|
| **data.binance.vision** | Gratis | Sí (todos los símbolos; dumps inmutables) | Klines OHLCV, **funding rate**, trades, aggTrades (USD-M + COIN-M); spot aparte | ZIP + `.CHECKSUM` por archivo, por símbolo/mes | **Fuente primaria** (pendiente verificación §4) |
| **Tardis.dev** | Pago (suscripción + datos) | **Sí, survivorship-free explícito** (delistados/expirados/renombrados) | Funding, **OI**, **order book L2**, trades, liquidaciones; Binance USD-M desde 2019-11-17 | CSV normalizado / stream WS crudo | **Complemento** para lo que binance.vision no da (libro L2, cross-check) |
| CoinAPI | Pago | Parcial | Funding histórico multi-exchange | API/CSV | Alternativa; útil si se quiere multi-exchange |
| Amberdata / Kaiko | Pago (enterprise) | Sí | Datos institucionales completos | API | Sobredimensionado/caro para esta etapa |
| CryptoDataDownload | Gratis/parcial | Limitado | CSV OHLCV agregados | CSV | Insuficiente (poca granularidad, cobertura de delistados incierta) |

## 3. Cómo se descarga de data.binance.vision (el camino gratis)

Estructura de URL, por símbolo/mes (patrón del README oficial):

```
# Klines (OHLCV) futuros USD-M
https://data.binance.vision/data/futures/um/monthly/klines/{SYMBOL}/{INTERVAL}/{SYMBOL}-{INTERVAL}-{YYYY-MM}.zip
# Funding rate futuros USD-M
https://data.binance.vision/data/futures/um/monthly/fundingRate/{SYMBOL}/{SYMBOL}-fundingRate-{YYYY-MM}.zip
# Cada .zip trae su .CHECKSUM (sha256) al lado, para verificar integridad
```

- `shell/fetch-all-trading-pairs.sh` del repo `binance-public-data` enumera símbolos; para delistados hay que **enumerar el bucket S3** (los símbolos vivos no los listan, pero los archivos históricos siguen ahí).
- Encaja con la disciplina del lab: crudo inmutable + hash SHA-256 (regla 1 de `DATA.md`), igual que hizo exp-008 con el funding de los 5 majors.

## 4. CAVEAT CRÍTICO — verificar antes de confiar

**"Existe el símbolo delistado" ≠ "está la cola del crash".** El riesgo real no es que falte LUNAUSDT, sino que **el trading se haya detenido/delistado ANTES de que la caída terminara**, dejando la cola —justo lo que la tesis del carry debe pagar— **parcialmente censurada de todos modos**. Esto le pasa por igual a binance.vision y a Tardis: ninguno puede grabar lo que el exchange dejó de cotizar.

Por eso el **go/no-go del camino gratis** es una prueba de 30 minutos (tarea #26):

1. Descargar de binance.vision el `fundingRate` + `klines 15m` de **LUNAUSDT** (USD-M) de **abril–mayo 2022**.
2. Verificar el `.CHECKSUM`.
3. Confirmar que las velas del **de-peg (9–13 mayo 2022)** están presentes y hasta qué fecha/precio llega la serie antes del delisting.
4. Repetir con 1–2 delistados más (p.ej. algún token muerto con perp) para no generalizar de un caso.

Si la cola llega razonablemente hasta el colapso → el camino gratis es viable como base. Si se corta mucho antes → hay que declararlo como límite estructural (ningún proveedor lo arregla) y ajustar el alcance/expectativas del carry.

## 5. Recomendación (para decisión del IP)

**Arquitectura de dos niveles:**

- **Base = `data.binance.vision` (gratis):** klines + funding + spot real, universo amplio **incluyendo delistados**, crudo inmutable con hash. Cubre lo que necesitan el carry (funding, cola censurada parcial) y ILLIQ (universo amplio). Es coherente con exp-008 y barato.
- **Complemento = `Tardis.dev` (pago), solo si hace falta:** para **order book L2 real** (capacidad/microestructura, carry AC-4 e ILLIQ) y como **cross-check** de la cobertura de delistados. No se contrata hasta saber que binance.vision se queda corto en algo concreto.

**Primer paso concreto, antes de escribir cualquier recolector:** ejecutar la **verificación #26** (descargar LUNAUSDT delistado y mirar la cola). Es el go/no-go que decide si el camino gratis sirve de base o si hay que replantear.

## 6. Qué NO resuelve esta investigación (honestidad)

- ~~No confirma aún que binance.vision sirva `LUNAUSDT` futuros.~~ **CERRADO 2026-07-26: verificado con archivo en mano (tarea #26) — la cola del colapso está presente.** Queda pendiente el spot-check de 1-2 delistados adicionales al fijar el universo.
- No cotiza Tardis (habría que pedir precio según volumen de símbolos/fechas/canales).
- No cubre el **spot real** para todos los símbolos: binance.vision tiene spot, pero un perp puede no tener par spot o tenerlo delistado en otra fecha — a verificar por símbolo cuando se defina el universo.

## Fuentes
- [Binance Public Data (README oficial)](https://github.com/binance/binance-public-data) — "All symbols are supported"; estructura de dumps; CHECKSUM.
- [Binance Data Collection](https://data.binance.vision/) — bucket público.
- [Tardis.dev — Binance USDS-M Futures](https://docs.tardis.dev/historical-data-details/binance-futures) — cobertura desde 2019-11-17; funding/OI/L2.
- [Tardis.dev — Data FAQ (survivorship-bias-free)](https://docs.tardis.dev/faq/data) — incluye delistados/expirados/renombrados.
- [CoinAPI — Historical funding rates](https://www.coinapi.io/blog/historical-crypto-funding-rates-api-coinapi) — alternativa multi-exchange.
- [Binance funding rate history endpoint](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History) — API en vivo (complemento).
