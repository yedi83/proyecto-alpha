# exp-008 — PRE-REGISTRO: la cesta H-001 con FUNDING REAL histórico

> Escrito 2026-07-17, ANTES de recolectar el dato y de correr nada. Umbrales ratificados por el IP en sesión (estructura R0/R1/R2; el nivel letal endurecido a petición suya: "matar exige evidencia clara, no un borde"). **N declarado: intento único** — no habrá exp-008b con otra fuente de funding si el resultado incomoda. Familia: costes reales (distinta de riesgo 002/003, lookback 004, OOS 005/006, comportamiento 007).

## Contexto de acumulación (ADR-0006 — vinculante)

H-001 está **CUESTIONADA**: exp-004 disparó un veredicto letal de robustez (override formalizado por ADR-0006). Por la cláusula §4.2 de ese ADR: **si este experimento dispara su nivel letal (R2), es el segundo disparo independiente y H-001 se retira del camino operativo automáticamente** — sin nota interpretativa posible, sin excepción. Y la Fase C exige R0: un R1 también la bloquea (suspende el sello del PREREG_FASE_C).

## Pregunta

El backtest usa funding uniforme 0.01%/8h; el veredicto original declara: "con funding alto, 2024-26 queda ≈ 0". **¿Sobrevive la magnitud del edge al funding real de 2021-2026?**

## Datos

- Funding histórico por símbolo (BTC, ETH, SOL, BCH, DOGE perp USDT) del endpoint público `fapi/v1/fundingRate` de Binance mainnet, 2021-07-01 → presente, recolectado por `datalake/funding/recolector_funding.py` (QA integrado: cadencia 8h, huecos, duplicados, cobertura).
- **Compuerta previa: dictamen APTO de A-02** sobre el dataset (sesión separada con su prompt) antes de correr el experimento.
- Limitación declarada: funding de Binance como proxy de Zoomex (misma mecánica de índice, no idénticos; no existe histórico de Zoomex). Se acepta como la mejor evidencia disponible.

## Método (congelado)

- Motor: el de exp-002/003/004 (paridad verificada al centavo), con UN cambio: el funding deja de ser `rate/32` uniforme por vela y se aplica **en la vela que contiene cada timestamp real** (00/08/16 UTC) sobre posiciones abiertas: `eq -= units × precio × rate × signo` (long paga rate positivo y cobra negativo; short al revés). Símbolo sin dato en un timestamp (pre-listing): funding 0 y se reporta la cobertura.
- Config: riesgo uniforme 0.10%, ENTRY 512/EXIT 256, ventanas full/2123/2426, stop_fill="stop", gross_cap=0 — idéntico a la base validada.
- **Paridad obligatoria:** la corrida base (0.01%/8h uniforme) debe reproducir NET +24.03 / maxDD −17.8 / Sharpe 0.42 / Calmar 1.35. Sin paridad, experimento inválido.

## Umbrales (ventana FULL 2021-26 salvo indicación; referencia base NET +24%, Sharpe 0.42)

| Nivel | Condición | Consecuencia |
|---|---|---|
| **R0 — ACEPTABLE** | NET ≥ +10% **y** Sharpe ≥ 0.30 | La magnitud sobrevive al funding real. Fase C queda condicionada solo al veredicto de Fase B (y al resto del ADR-0006). |
| **R1 — ADVERTENCIA** | NET en (0, +10%), **o** Sharpe < 0.30, **o** NET(2024-26) < 0 | Degradación significativa: sello de PREREG_FASE_C **suspendido**; investigación de dónde muerde el funding (símbolo/régimen/lado) y cualquier continuación exige ADR. |
| **R2 — LETAL** (evidencia clara) | NET ≤ **−5%**, **o** [NET ≤ 0 **y** NET(2024-26) < 0 a la vez] | El funding real destruye la ventaja de forma inequívoca. **Por ADR-0006 §4.2: segundo disparo letal → H-001 se retira del camino operativo** (Fase B puede completarse como validación de plataforma; C no se abre). Vuelta a investigación solo como H-001.v2. |

Lectura en orden R2→R1→R0; "casi pasa = no pasa" en todas las fronteras; nada se renegocia.

## Salidas

`exp-008/`: RESULTADO.md (base vs funding-real por ventana + funding neto pagado/cobrado por símbolo y por año + descomposición por lado long/short), metricas.json, DATOS.md (dataset + hash + dictamen A-02 enlazado), script exacto. El veredicto alimenta: decisión de PREREG_FASE_C, TEORIA.md (contraste histórico de la predicción P4), DATA.md, y el estatus de H-001 en el REGISTRO.
