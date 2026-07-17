# H-002 — Ruptura Donchian(20) + filtro SMA200 (diario, solo largos)

| Campo | Valor |
|---|---|
| ID | H-002 |
| Familia | Trend following (mediano plazo, diario) con **filtro de régimen** (SMA200), **solo largos** |
| Mercado | Backtest y paper: **spot Binance** (klines públicas). Instrumento operativo (spot vs. perp) **por decidir** — afecta la exposición a funding (P3) |
| Universo | Banco: BNB + generalización cruzada BTC, ETH, ADA, XRP, LTC · Paper multi-activo: BTC, ETH, BNB, ADA, XRP, LTC |
| Estado | **Banco APROBADO — confianza moderada (2026-07-14)** → **forward en paper multi-activo desde 2026-07-15** (testigo, base + variante etiquetada). **Sin fase operativa formal declarada.** |
| Pre-registro | ✅ [`PREREG_BANCO.md`](../../../research/H-002-ruptura-bnb-d1/PREREG_BANCO.md) — suite T1-T5 escrito antes de correr |
| Hipótesis económica | [`research/H-002-ruptura-bnb-d1/HIPOTESIS_ECONOMICA.md`](../../../research/H-002-ruptura-bnb-d1/HIPOTESIS_ECONOMICA.md) |
| Última actualización de ficha | 2026-07-16 |

## Hipótesis económica (resumen)

Mismo motor conductual que H-001 (subreacción/rebaño + amplificación por apalancamiento), pero **filtrado al régimen alcista** (SMA200) y **cosechado con objetivo fijo 2R**. El filtro excluye el terreno de whipsaw (crashes/rango bajo SMA200) → de ahí la **reducción de drawdown**. Honestidad central: es **long-only, beta positiva** — su ventaja es **timing de beta / gestión de drawdown**, NO alfa market-neutral (a diferencia de H-001). Documento completo con 5 predicciones falsables y 4 señales de retiro: enlace arriba.

## Definición de la señal (congelada por el banco; solo la BASE)

Entrada: ruptura del máximo de **20 días** (shift 1) **con precio > SMA200** (filtro de tendencia), solo largos. Stop: **2.5×ATR**. Objetivo: **2R fijo**. Riesgo: **1.25%/trade**. Timeframe: **diario**. Motor: reutilizado *verbatim* del backtest del investigador. **La variante trailing NO pasa** (más parámetros, autoflag dudosa).

## Veredicto del banco (2026-07-14) — [`RESULTADO_BANCO.md`](../../../research/H-002-ruptura-bnb-d1/RESULTADO_BANCO.md)

| Test | Resultado |
|---|---|
| T1 — vs aguantar BNB (historia completa) | **Falla, pero por outlier** (el 40× irrepetible de BNB; la beta dimensionada la aplasta en ese único activo) |
| T2 — generalización cruzada | **Generaliza:** bate a aguantar (Sharpe y MAR) en **4/5 majors** (BTC, ETH, ADA, XRP) → es mecanismo, no un activo |
| T3 — sensibilidad | **Meseta, no pico** (N 10-40 × ATR 2-3 todos positivos; SMA200 no es el óptimo → no sobre-ajustado) |
| T4 — significancia | **Más sólida que H-001:** n=57, win 49%, top-5 = 44% del neto (no cuelga de la cola) |
| T5 — OOS (lockbox 2023-26) | **Aplasta a aguantar:** Sharpe 1.08 vs 0.26; +14.1% con MDD −4.8% |

**Veredicto:** overlay de tendencia **multi-activo, reductor de drawdown**, que bate a aguantar OOS y en la mayoría de majors, con meseta de parámetros y sin depender de la cola. **Confianza moderada** (mejor que H-001), **no probada** (muestra chica). Reglas anti-sobreajuste retenidas: no cherry-pick del mejor activo/param; multi-activo, no BNB solo; solo la base.

## Limitaciones vigentes (declaradas)

Muestra chica (n=57 trades) → confianza moderada, no prueba · **long-only ⇒ beta positiva** (no descorrelacionada) · **funding no medido** y exposición máxima al ser siempre larga (P3, la mayor incógnita) · survivorship (majors elegidos en 2026) · backtest/paper en **spot**; instrumento operativo por decidir.

## Estado de validación

- **Banco:** pre-registrado (T1-T5) y aprobado con confianza moderada. Hecho.
- **Forward (paper_real):** desplegado 2026-07-15, multi-activo, base + variante etiquetada, monitor diario, sin dinero ni keys. Es **testigo** de captura de señal going-forward, no fase operativa.
- **Fase operativa formal (A/B/C):** **NO declarada.** Decisión pendiente — lo natural es mantenerla en paper-observación hasta cerrar el ciclo C-001 (moratoria ADR-0004), y entonces decidir si entra al protocolo operativo completo.

## Nota meta (prueba de fuego de la plataforma)

El banco reutilizó el motor del investigador **verbatim** y corrió el suite completo en ~1 jornada, frente al arco largo de H-001. Primera evidencia —n=1, no prueba— a favor de la tesis central: la segunda hipótesis costó una fracción de la primera.

## Registro de eventos

| Fecha | Evento |
|---|---|
| 2026-07-14 | Banco pre-registrado (PREREG_BANCO) corrido: T1-T5. Veredicto: overlay de tendencia reductor de DD, confianza moderada, no probada. Solo la base avanza. |
| 2026-07-15 | Paper_real multi-activo desplegado (base + variante etiquetada), monitor diario. |
| 2026-07-16 | Hipótesis económica formulada (ex-post, declarado): mecanismo, contraparte, 5 predicciones falsables, 4 señales de retiro; honestidad sobre beta positiva. Ficha creada y registrada en ESTADO. |
