# PRE-REGISTRO — Fase C (capital real) — BORRADOR

- **Estado:** BORRADOR para decisión del IP. Se **sella ANTES** del primer día de Fase C, y **solo si la Fase B aprueba todos sus criterios**. Una vez sellado no se edita (regla del PREREG: cambios → ENMIENDA fechada).
- **Fecha borrador:** 2026-07-16. Autor material: asistente; **decide y sella el IP**.

> **Contexto que condiciona TODOS los criterios (no decorativo):** H-001 es una estrategia **convexa** — win rate ~20%, ~5 trades grandes al año, Sharpe ~0.42, **alfa t=0.94 (diversificador plausible, NO edge probado)**, maxDD de backtest **−18%** (vs B&H −88%). Sangra plano durante meses y paga raro y fuerte. Esto significa que **un stop de drawdown ingenuo la mata justo en el peor momento** (el sangrado normal ANTES del payoff). Cada número de abajo respeta esa naturaleza.

## 1. Precondición de entrada (sin "casi pasa")

Fase C inicia **solo** si Fase B APRUEBA todos sus criterios del PREREG: TE acumulado dentro de ±5% del modelo, slippage mediana de exceso ≤ 5 bps, cero omisiones BTC por min_notional sin decisión documentada, y ninguna desviación de métrica sin explicación. Un criterio reprobado = no se pasa a C.

## 2. Capital y cuenta  **[DECIDIDO — IP, 2026-07-16]**

- **DECISIÓN: $750**, en **cuenta dedicada**, separada de fondos personales, cuya pérdida total sea irrelevante. Riesgo por trade **congelado**: BTC 0.125%, resto 0.10% (exp-003); cap agregado 0.525% ≤ 0.60%.
- Sin escalado automático de capital: subir el tamaño = decisión documentada (ADR) tras una revisión.

## 3. Criterio de PARADA / retiro — *el número que faltaba*  **[DECISIÓN IP — el más importante]**

Se separa en **tres tipos**, porque mezclarlos es el error clásico. Se retira si se dispara **(a) O (b) O (c)**.

**(a) Drawdown FUERA de envolvente** (no un drawdown normal).  **[DECIDIDO — IP, 2026-07-16]**
- **DECISIÓN: al alcanzar un drawdown de 1.5× el maxDD de backtest (−18% → umbral ≈ −27%) desde el inicio de C** —o un nivel que el backtest de 5 años **nunca** produjo— **se SUSPENDE la operativa.**
- **Cláusula de suspensión y revisión (IP, 2026-07-16):** el −27% constituye un **umbral de suspensión y revisión** de la estrategia, **no un objetivo de pérdida** ni un nivel para "aguantar" indefinidamente. Al alcanzarse, **cesará la operativa** y se realizará un **análisis completo** —que verifique si el comportamiento observado sigue siendo compatible con el esperado por el backtest— **antes de autorizar cualquier reanudación**. La reanudación exige dictamen documentado + ADR; el umbral **nunca** se relaja durante el drawdown.
- Porqué el umbral está en −27% y no antes: un DD dentro de la envolvente histórica es **comportamiento esperado**, no señal de muerte. Solo un DD que **excede lo que el mecanismo ha producido jamás** dispara la suspensión. Un stop en −10% detendría la estrategia en su sangrado normal, justo antes del payoff.

**(b) Divergencia de comportamiento** (implementación rota, distinta de la mala suerte).
- Propuesta: tracking error sostenido live-vs-modelo fuera de **±5%** (banda de Fase B) durante **≥ 3 semanas** con causa no explicada. Esto detecta ejecución rota, no distribución adversa.
- **Decide el IP:** banda y plazo.

**(c) Retiro conceptual** (`HIPOTESIS_ECONOMICA.md §5` — manda sobre el equity).
- Cualquiera de las 4 señales: muerte de la persistencia de tendencias; institucionalización de la cesta; cambio estructural del apalancamiento de perpetuos; o **funding crónicamente extremo comiéndose la alfa (P4)**.
- Se retira **aunque el PnL esté bien**, porque el mecanismo murió. Medir (b)/(c) requiere el Data Lake / OI / funding → vínculo con ROADMAP §3.

Reingreso tras retiro: solo con nueva evidencia y ADR. Nunca se relaja este criterio durante un drawdown.

## 4. Kill switch: duro vs blando  **[DECIDIDO — IP, 2026-07-16]**

- **Estado actual (validado):** kill **blando** — a −5% diario bloquea aperturas nuevas y deja correr las abiertas a sus stops. Filosóficamente correcto para trend-following (cerrar a mercado en pánico realiza el peor precio).
- **DECISIÓN: mantener el blando** + añadir un **disyuntor catastrófico técnico** (no de precio): kill duro solo por fallo de integridad (desincronización estado↔exchange, pérdida de feed prolongada, corrupción de estado) que cierra y detiene. El drawdown lo gobierna §3, **no** el kill diario. (Se descarta el kill duro por precio: pelea contra la naturaleza convexa.)

## 5. Stop: en exchange (reduce-only) vs por vela cerrada  **[DECIDIDO — IP, 2026-07-16]**

- **Validado:** stop por **vela cerrada**, sin protección intrabar. Con dinero real, un gap / flash-crash intrabar puede exceder el stop.
- **Tensión:** añadir un stop **reduce-only residente en el exchange** mejora la protección, PERO es un **cambio de lógica → reinicia la validación** (regla del PREREG).
- **DECISIÓN: Fase C corre con el stop validado (vela cerrada)** para no romper comparabilidad; el stop en exchange se registra como **mejora candidata para C-002** (ADR). Se **acepta explícitamente el riesgo intrabar**, acotado (máx 5 posiciones × riesgo residual por stop).

## 6. Seguridad operativa (SECURITY)  *(redactada en `docs/SECURITY.md`; el IP ratifica al sellar)*

Checklist completo en `docs/SECURITY.md`: keys de producción con **retiros DESHABILITADOS** + **IP whitelist** + permisos solo-trading, secretos fuera de git, mínimo privilegio, auditoría con logs inmutables, validaciones pre-orden, **prohibición de intervención manual no registrada (§9)** y **Disyuntor Técnico por anomalía operacional (§10)** — este último concreta el disyuntor técnico de §4.

- **Decisión abierta (al sellar):** §9 (detección de intervención manual *durante* la operación) y §10 (parada por anomalía) **no** están en el bot de Fase B (congelado). Implementarlos antes de C = **bot nuevo a validar**; alternativa = diferir a C-002 con vigilancia manual reforzada. Se decide con ADR al sellar este PREREG. Sin la config de cuenta (§1-2 de SECURITY) resuelta, no arranca C.

## 7. Duración y revisión

- **Revisión formal cada 4 semanas** contra este documento, registrada en el diario de fase (y ADR si hay decisión). Duración mínima sugerida: **≥ 3 meses** o hasta observar ≥ 2-3 trades "clave", lo que ocurra más tarde (coherente con ~5 trades/año).

## 8. Qué NO cambia (congelado)

Señales, canales, ATR, sizing (exp-003), cesta, y kill blando: **idénticos a lo validado en A/B**. Fase C **no es para mejorar** la estrategia; es para ver si **sobrevive al capital real y a la fricción real**. Toda mejora identificada → ADR para C-002.
