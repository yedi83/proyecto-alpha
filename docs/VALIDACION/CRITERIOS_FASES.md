# Criterios de las Fases de Validación Operativa

> **Regla constitucional:** los números de cada fase se escriben ANTES de iniciar (o continuar) esa fase. Un criterio escrito después del resultado no es un criterio.
>
> Estado: 🔴 INCOMPLETO — los campos PENDIENTE deben llenarse antes de evaluar la Fase A de H-001.

## Fase A — Dry Run

El bot corre conectado a datos reales sin enviar órdenes. **No se evalúa rentabilidad.**

| Criterio | Umbral de aprobación | Umbral de reprobación |
|---|---|---|
| Duración mínima | PENDIENTE (sugerido: ≥ 4 semanas continuas) | — |
| Uptime del bot | PENDIENTE (sugerido: ≥ 99%) | < PENDIENTE |
| Señales del bot vs. señales del backtester sobre los mismos datos | PENDIENTE (sugerido: 100% coincidencia) | Cualquier divergencia no explicada |
| Velas atrasadas / datos perdidos | PENDIENTE | > PENDIENTE |
| Reconexiones fallidas | PENDIENTE | > PENDIENTE |
| Incidentes sin resolver en RUNBOOK | 0 | ≥ 1 sin causa raíz documentada |

## Fase B — Testnet

Ejecución completa en testnet. Se mide la fricción de ejecución.

| Criterio | Umbral de aprobación | Umbral de reprobación |
|---|---|---|
| Duración mínima | PENDIENTE (sugerido: ≥ 8 semanas) | — |
| Tracking error (PnL live vs. modelo) | PENDIENTE | > PENDIENTE |
| Slippage medio vs. asumido en backtest | PENDIENTE | > PENDIENTE |
| Órdenes fallidas / rechazadas | PENDIENTE | > PENDIENTE |
| Divergencia de funding aplicado vs. modelado | PENDIENTE | > PENDIENTE |

## Fase C — Capital real

Solo comienza si A y B aprobaron **todos** sus criterios. Sin "casi pasa".

| Criterio | Valor |
|---|---|
| Capital inicial máximo | PENDIENTE (sugerido: cantidad cuya pérdida total sea irrelevante) |
| Límites de riesgo | Los de `../RISK_POLICY.md`, sin excepciones |
| **Criterio de parada (retiro de la estrategia)** | PENDIENTE — escribir ANTES de iniciar: p. ej. drawdown > X%, o tracking error > Y durante Z días, o métrica live fuera del intervalo de confianza del backtest |
| Revisión programada | PENDIENTE (sugerido: evaluación formal cada 4 semanas contra este documento) |

## Registro de decisiones de fase

Toda decisión de aprobación/reprobación se registra aquí con fecha y evidencia enlazada.

| Fecha | Hipótesis | Fase | Decisión | Evidencia |
|---|---|---|---|---|
| — | — | — | — | — |
