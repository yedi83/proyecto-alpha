# Política de Riesgo

> Transcripción formal de los límites **congelados y operando** en el bot de H-001 (verificados en `live_bot.py` y `config.env` el 2026-07-03). Fuente de verdad operativa: el código; este documento la formaliza y añade lo que falta para Fase C.
>
> Estado: 🟡 Límites de Fase A/B completos (transcritos del sistema vivo). Pendientes de Fase C marcados.

## Nivel 1 — Por estrategia (H-001, congelado)

| Límite | Valor | Aplicación |
|---|---|---|
| Riesgo por trade | **0.10% del equity** (un movimiento de 3×ATR en contra = -0.10%) | `RISK_PER_TRADE=0.001`, sizing por fórmula |
| Apalancamiento máximo por posición | **3x** (cap en el sizing); apalancamiento configurado en exchange: 2x | `MAX_LEV=3.0`, `LEVERAGE=2` |
| Stop | Trailing canal 256 con piso catastrófico 3×ATR de entrada; evaluado por vela cerrada | Limitación declarada: sin protección intrabar |
| Notional mínimo | Si units×precio < mínimo del símbolo → NO se abre y se registra el evento | Evento `min_notional` en eventos.csv |

## Nivel 2 — Portafolio (congelado)

| Límite | Valor | Acción al superarlo |
|---|---|---|
| Posiciones simultáneas | **Máx 5** (1 por símbolo, sin apilar) | Señal omitida y registrada (`max_concurrentes`) |
| Riesgo agregado | **(n_abiertas+1) × 0.10% ≤ 0.60%** | No se abre la nueva (`cap_riesgo_agregado`) |
| Kill switch diario | Equity ≤ 95% del equity de inicio del día | **Halt de aperturas** el resto del día; las abiertas se siguen gestionando (`kill_switch`) |

## Matiz importante del kill switch (decisión documentada)

El kill switch actual **no cierra posiciones**: bloquea aperturas nuevas y deja que las abiertas se gestionen por sus stops. Es una decisión razonable para trend following (cerrar a mercado en pánico realiza el peor precio), pero significa que la pérdida diaria real puede exceder el -5% si las posiciones abiertas siguen cayendo hasta sus stops. Cota de exposición: máx 5 posiciones × riesgo residual por stop. Se acepta para Fases A/B; **para Fase C debe decidirse explícitamente** si se añade un kill duro (cerrar todo a partir de -X% diario) además del blando.

## Salvaguardas operativas (verificadas en el sistema)

- Estado persistido tras cada operación (`bot_state.json`); reconciliación con el exchange al arrancar; corrupción de estado = criterio de aborto de fase (PREREG).
- Lanzador reinicia el proceso si muere; vigía externo cada 15 min (heartbeat >25 min, errores, estado ilegible).
- Gating de despliegue: DRY_RUN → testnet → real.
- Toda señal omitida por límites queda registrada con motivo (PnL fantasma visible).

## Pendiente para Fase C (completar ANTES de iniciarla)

- [ ] Capital inicial: ~$750 según PREREG — ratificar cifra y cuenta dedicada.
- [ ] **Criterio de retiro de la estrategia** (el número que falta): drawdown máximo aceptado desde inicio de Fase C, y/o tracking error sostenido, y/o señales de retiro conceptual de `HIPOTESIS_ECONOMICA.md` §5. Se escribe antes del primer día de Fase C.
- [ ] Decisión kill duro vs. blando (ver matiz arriba).
- [ ] Decisión sobre stop residente en exchange (reduce-only) vs. stop por vela cerrada — la mejora está identificada pero no desplegada; cambiarla reinicia validación según PREREG.
- [ ] Checklist de seguridad de `SECURITY.md` (API keys de producción con retiros deshabilitados, IP restringida).

## Regla de modificación

Estos límites solo se relajan mediante ADR, nunca durante un drawdown ni el día de un incidente. Endurecerlos no requiere ADR pero sí registro en el diario de fase. Durante una fase de validación rige el PREREG: prohibido cambiar límites salvo corrección crítica documentada.
