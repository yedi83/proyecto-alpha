# DICTAMEN A-02 — Auditoría de Datos — dataset `datalake/funding/`

- **Fecha:** 2026-07-17
- **Auditor:** A-02 (Auditor de Datos adversarial — laboratorio Proyecto Alpha)
- **Objeto:** dataset de funding histórico (BTC, ETH, SOL, BCH, DOGE perp USDT), insumo de **exp-008** (H-001).
- **Compuerta:** este dictamen es requisito previo del PREREG de exp-008 (§Datos). ADR-0006 declarado y **explícitamente aislado del criterio**: el peso operativo de exp-008 no relaja ni un umbral de esta auditoría.

---

## DICTAMEN: **APTO** para investigación

El dataset se auditó asumiéndolo sucio. Cada anomalía señalada (intervalos ≠8h, extremos, cap −2%) se **resolvió con evidencia concreta y quedó atada a un evento de mercado documentado**, con corroboración externa a la hora exacta en el caso crítico (SOL/FTX). Integridad, monotonía, unicidad temporal, zona horaria y rango de valores pasan sin excepción. No se detectó ninguna contaminación que sesgue exp-008. El APTO se emite sobre un **artefacto congelado por hash** (abajo), no sobre "lo que devuelva el endpoint mañana".

### Artefacto auditado (SHA-256 — congelar en `DATOS.md` de exp-008)

| archivo | sha256 |
|---|---|
| BTC_funding.csv  | `801133db36c95488723264569af1a6ac05c01e885d80eaa145f5f3f0f86dda7a` |
| ETH_funding.csv  | `76c6a5187e42008157dbe5eb3954f3a1ee28c9244176449254ad10231d3b61a2` |
| SOL_funding.csv  | `590d760f9e8c57f737c91df2adbbec482e2760438e8837a1f99ca6901b13c8f7` |
| BCH_funding.csv  | `98239ab8b16f17f79e1494f763db6e11fc1ed07bc8ac653f29235f8c71564c87` |
| DOGE_funding.csv | `1fd25d55144784514ee6d2cc28627b3717887224dfba7b1122856236395f3ad8` |

---

## Resolución de las tres preguntas dirigidas

### P1 — SOL 5603 tramos (101.36% de la malla 8h, 75 de más): ¿legítimo o artefacto?

**LEGÍTIMO — cambio de cadencia oficial de Binance, no artefacto ni duplicado.**

- Los 75 tramos "de más" (5603 − 5528) provienen de **un único episodio contiguo**: `2022-11-09 16:00 → 2022-11-18 08:00 UTC`. Fuera de esa ventana, SOL es 8h puro. Los otros cuatro símbolos son 8h puro en todo el histórico (BTC/ETH/BCH/DOGE = 5528, diff 0).
- Dentro del episodio la cadencia pasa a **4h y luego 2h** (conteo SOL: 8h×5501, 4h×3, 2h×98). Progresión observada: 16:00 (último 8h) → 20:00 (4h) → 00:00/04:00 (4h) → 06:00 en adelante (2h) → reversión limpia a 8h el 18-nov.
- **Corroboración externa (a la hora exacta):** anuncio oficial de Binance *"Updates on Funding Rate Settlement Frequency and Capped Funding Rate Multiplier of SOLUSDT… (2022-11-09)"*, vigente **desde 2022-11-09 20:00 UTC** — que es precisamente el primer tramo no-8h de los datos. El episodio coincide con el colapso de FTX/Alameda (SOL era el activo núcleo de Alameda; cayó ~20% adicional ese día).
- **No es duplicado:** 0 timestamps duplicados (exactos y tras floor a 15min), serie estrictamente monótona creciente. Los 75 tramos son eventos de funding adicionales reales, no repeticiones. La etiqueta del QA "cobertura 101.36%" es un artefacto de **medir contra una malla 8h asumida**, no un exceso de datos: la cobertura real de eventos de funding es correcta.

### P2 — Extremos: SOL −2%/8h y ETH < −0.3%/8h: ¿eventos reales o corrupción?

**EVENTOS REALES. Todos los extremos caen en episodios de estrés identificables. Ninguno parece corrupto.**

- **SOL −2.000% (= −0.02):** 7 tramos consecutivos exactamente en `−0.02`, todos dentro del episodio FTX: `2022-11-09 20:00, 11-10 00:00, 04:00, 06:00, 08:00, 10:00, 12:00`. **−2% es el cap/floor de funding de Binance para SOL**, y el mismo anuncio del 2022-11-09 elevó el *Capped Funding Rate Multiplier* (0.75→1). Siete lecturas pegadas al floor durante lo peor del crash = comportamiento de capado legítimo, **no** dato corrupto. Signo negativo coherente: perp cotizando con descuento fuerte → shorts pagan a longs.
- **ETH −0.302% (`2022-09-15 00:00`):** cae en **The Merge de Ethereum** (fusión a PoS, 2022-09-15 ~06:42 UTC). El funding de ETH-perp se hundió pre-Merge por el trade de fork PoW (mantener spot / shortear perp). Extremo real y bien documentado.
- **DOGE −0.325% (`2021-09-07 16:00`):** día del crash de "El Salvador/BTC legal tender" (BTC ~52k→43k), sell-off general de cripto. Plausible y consistente en magnitud.
- **SOL <−0.3% fuera de FTX (6 tramos):** `2022-11-28` (réplica post-FTX), `2023-01-03/04` (fondo de SOL ~$8, temor a liquidación del estate de FTX), `2025-10-11` (dentro del rango del dataset; magnitud consistente con estrés, ver NO VERIFICABLE). Ninguno es outlier físico.

### P3 — Convención temporal y riesgo de lookahead / doble aplicación en el motor exp-008

**CONVENCIÓN CORRECTA. Sin desfase, sin timezone mixta, sin lookahead, sin doble aplicación.**

- **Malla:** salvo el episodio FTX, el 100% de los timestamps cae en 00/08/16 UTC. Jitter máximo de sub-segundo = 47 ms (formato Binance, p.ej. `08:00:00.004`); 0 filas con segundos > 1s. Los 75 timestamps "fuera de 00/08/16" son **exactamente** los del episodio FTX (horas pares 02/04/06/…), no desfases.
- **Zona horaria única:** todo `+00:00` (UTC), sin mezcla. Serie monótona creciente en los 5 símbolos.
- **Lookahead:** el motor (`load_funding`) hace `floor("15min")` del timestamp real y aplica el rate en la vela 15m que lo contiene (p.ej. funding sellado 08:00 → vela `[08:00,08:15)`). El rate es el **realizado** en ese instante; no se usa información futura. Además el bloque de funding se evalúa al inicio de la iteración de la vela `i` **antes** de procesar entradas/salidas de esa vela, leyendo el estado de posición de la vela previa: una posición que entra en la vela `i` **no** paga funding en `i` (no estaba abierta en el instante de funding), y una que sale en `i` **sí** lo paga (estaba abierta al open). Alineación correcta.
- **Doble aplicación:** el motor usa `arr[i] += r` para sumar tramos que caigan en la misma vela. El espaciamiento mínimo entre tramos es **2h** (episodio FTX) → nunca dos tramos en la misma vela de 15min. Verificado: 0 colisiones tras floor a 15min en los 5 símbolos. No hay doble cobro.

---

## HALLAZGOS CRÍTICOS (invalidan cualquier experimento)

**Ninguno.**

## HALLAZGOS MODERADOS (sesgan resultados)

**Ninguno.** No se identificó sesgo direccional atribuible al dato de funding.

## HALLAZGOS MENORES

1. **Reproducibilidad no fijada en el repo.** El dataset es una descarga de un endpoint público mutable (`fapi/v1/fundingRate`) y **no venía acompañado de hash/snapshot** versionado; el PREREG de exp-008 exige el hash en `DATOS.md` y no estaba presente. Mitigado por este dictamen (SHA-256 arriba), pero debe quedar registrado formalmente. — *(afecta re-auditabilidad, no la limpieza del dato)*
2. **Caveat obsoleto del recolector/QA.** La nota "SOL/DOGE pueden empezar después de 2021-07 (listing)" no aplica: ambos tienen dato real (no zero-fill) desde `2021-07-01 00:00` (SOL `8.824e-05`, DOGE `−2.631e-05`; 0 rates exactamente cero en todo el dataset). Los perps de SOL/DOGE se listaron en 2020, anteriores a la ventana. Sin huecos pre-listing dentro de la ventana del backtest (arranca 2021-07-22). Corregir la nota para no inducir a error.
3. **Métrica cosmética del QA.** "media anualizada" en el QA usa `sum/n·3·365` (aprox. que trata todo como 8h y no pondera el episodio 2h/4h de SOL). No afecta al motor de exp-008 (que consume el CSV, no el QA), pero el número reportado del QA para SOL es aproximado.
4. **Precio de aplicación del funding.** El motor cobra funding sobre el `close` de la vela 15m que contiene el timestamp, no sobre el precio exacto del instante de funding. Diferencia intra-vela de 15min, despreciable y **no** es lookahead.

## NO VERIFICABLE (cuenta contra el APTO; declarado)

1. **Igualdad byte-a-byte contra un pull fresco de Binance hoy.** El sandbox de auditoría no tiene salida a Binance; no puedo re-descargar y diferenciar. Mitigación: el APTO queda anclado a los **SHA-256** listados; exp-008 debe correrse contra exactamente esos hashes.
2. **Verificación tramo-a-tramo de la cadencia 2h/4h de SOL** contra el registro oficial de Binance: confirmé el *inicio* del cambio a la hora exacta (2022-11-09 20:00) y la coherencia interna del bloque, pero no contrasté los 101 timestamps uno a uno contra un histórico oficial de la cadencia.
3. **Evento SOL `2025-10-11`** (−0.3028%): dentro del rango del dataset y consistente en magnitud con un episodio de estrés, pero no lo contrasté contra una fuente primaria en esta sesión.
4. **Proxy Binance→Zoomex:** limitación ya declarada en el PREREG (misma mecánica de índice, no idénticos; no existe histórico de Zoomex). No es un defecto del dataset; es una brecha de validez externa que hereda exp-008.

## ACCIONES REQUERIDAS (yo no corrijo datos; propongo — el humano ejecuta y yo re-audito si aplica)

1. **Congelar el artefacto:** registrar los 5 SHA-256 de este dictamen en `exp-008/DATOS.md` y enlazar este dictamen. Correr exp-008 **solo** contra esos hashes. *(cierra el hallazgo menor #1 y el NO VERIFICABLE #1)*
2. **Corregir la nota del recolector/QA** sobre "listing SOL/DOGE" (no aplica) — evitar interpretación errónea futura.
3. **Documentar en `DATA.md`** el episodio de cadencia variable de SOL (2022-11-09→18, 4h/2h, cap −2%) con el enlace al anuncio de Binance, para que ningún consumidor futuro lo lea como hueco/duplicado.
4. *(Opcional, robustez)* Añadir al recolector un check explícito de `fundingIntervalHours`/`FundingRateCap` por símbolo desde el endpoint de info de funding, para dejar traza de cambios de cadencia/cap en vez de inferirlos.

---

### Evidencia de respaldo (resumen verificable)

- Integridad (5/5): 0 duplicados (exactos y floor-15min), serie monótona, 0 huecos >12h, 0 rates == 0, todos los rates en `[−0.02, +0.0015]` (rangos de funding, no de precio).
- Cobertura real: BTC/ETH/BCH/DOGE = 5528 (malla 8h exacta); SOL = 5603 (5528 + 75 del episodio FTX). Ventana 2021-07-01 → 2026-07-17, cubre la FULL del backtest (2021-07-22 → 2026-06-21).
- Corroboración externa: anuncio de Binance sobre frecuencia de settlement y cap de SOL (2022-11-09, vigente 20:00 UTC); The Merge de ETH (2022-09-15).

**Fuentes externas:**
- [Binance — Updates on Funding Rate Settlement Frequency and Capped Funding Rate Multiplier of SOLUSDT… (2022-11-09)](https://www.binance.com/en/support/announcement/updates-on-funding-rate-settlement-frequency-and-capped-funding-rate-multiplier-of-solusdt-solbusd-and-solusd-perpetual-futures-contracts-2022-11-09-e8be17e1e544418490e86723d84759f0)
- [Binance Futures — Funding Rate Info API (FundingRateCap/Floor/fundingIntervalHours)](https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-Info)
- [CNBC — Binance backs out of FTX rescue; Solana loses another ~20% (2022-11-09)](https://www.cnbc.com/2022/11/09/cryptocurrencies-pressured-as-investors-digest-ftx-fallout-solana-loses-another-20percent.html)
