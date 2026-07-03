# Política de Riesgo

> Límites cuantificados e innegociables. El bot los aplica automáticamente; el kill switch los respalda.
>
> Estado: 🔴 INCOMPLETO — completar los PENDIENTE antes de cualquier operación con capital real (Fase C).

## Nivel 1 — Por estrategia

| Límite | Valor | Acción al superarlo |
|---|---|---|
| Tamaño máximo de posición (% del capital asignado) | PENDIENTE | Rechazar orden |
| Pérdida máxima diaria | PENDIENTE | Detener la estrategia hasta revisión manual |
| Drawdown máximo desde máximo histórico | PENDIENTE | Retiro de la estrategia (ver criterio de parada en CRITERIOS_FASES.md) |
| Apalancamiento máximo | PENDIENTE | Rechazar orden |

## Nivel 2 — Portafolio (global, domina al nivel 1)

| Límite | Valor | Acción al superarlo |
|---|---|---|
| Pérdida máxima diaria global | PENDIENTE | Kill switch: cerrar todo |
| Exposición neta máxima total | PENDIENTE | Bloquear nuevas posiciones |
| Nº máximo de posiciones simultáneas | PENDIENTE | Bloquear nuevas posiciones |

## Kill switch

- Disparo automático: cualquier límite de nivel 2, pérdida de heartbeat > PENDIENTE segundos, o divergencia de reconciliación (posición según bot ≠ posición según exchange).
- Disparo manual: siempre disponible, documentado en `RUNBOOK.md`.
- Tras un disparo: no se reinicia sin diagnóstico escrito de causa raíz.

## Regla de modificación

Estos límites solo se relajan mediante ADR con justificación escrita, nunca durante un drawdown ni el mismo día de un incidente. Endurecerlos no requiere ADR.
