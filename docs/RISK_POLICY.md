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

> **Decisiones tomadas en borrador (2026-07-16):** `research/H-001-canal-donchian/fase_C/PREREG_FASE_C_BORRADOR.md`. Falta **sellarlo** antes del día 1 de C (solo si Fase B aprueba). No es evidencia hasta el sello.

- [x] Capital inicial: **$750**, cuenta dedicada (ratificado; borrador §2).
- [x] **Criterio de retiro/parada:** drawdown a **1.5× maxDD ≈ −27%** = **umbral de suspensión y revisión** (cesa la operativa + análisis completo antes de reanudar, con ADR); + divergencia de comportamiento (TE fuera de ±5% sostenido) + señales de retiro conceptual de `HIPOTESIS_ECONOMICA.md` §5 (borrador §3).
- [x] **Kill duro vs. blando:** blando validado + disyuntor catastrófico **técnico** (no de precio); se descarta el kill duro por precio (borrador §4).
- [x] **Stop:** vela cerrada (validado) para C; stop residente en exchange → mejora candidata a C-002 (borrador §5).
- [x] Checklist de seguridad **redactado** en `SECURITY.md` (keys sin retiros + IP whitelist, mínimo privilegio, auditoría, validaciones pre-orden, prohibición de intervención manual no registrada §9, y Disyuntor Técnico §10). **Abierto:** decidir al sellar si §9/§10 se implementan+validan antes de C o se difieren a C-002 (implican bot nuevo, no se toca el de Fase B).

## Regla de modificación

Estos límites solo se relajan mediante ADR, nunca durante un drawdown ni el día de un incidente. Endurecerlos no requiere ADR pero sí registro en el diario de fase. Durante una fase de validación rige el PREREG: prohibido cambiar límites salvo corrección crítica documentada.
