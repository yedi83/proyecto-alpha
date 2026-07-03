# Runbook de Operación

> Qué hacer cuando algo falla, escrito antes de que falle. Se completa durante la migración del bot con los procedimientos reales.

## Escenarios

### El bot se cae con una posición abierta

1. PENDIENTE — documentar durante la migración: cómo verificar la posición real en el exchange, cómo decidir cierre manual vs. reinicio, cómo registrar el incidente.

### Divergencia de reconciliación (posición según bot ≠ según exchange)

1. Kill switch inmediato (automático según RISK_POLICY.md).
2. PENDIENTE — procedimiento de diagnóstico.

### Pérdida de conexión / heartbeat

1. PENDIENTE — comportamiento esperado del bot (reconexión automática, timeout, estado de las órdenes en vuelo).

### Kill switch disparado

1. No reiniciar sin diagnóstico escrito de causa raíz.
2. PENDIENTE — checklist de reinicio seguro.

### Datos anómalos en vivo (vela imposible, funding fuera de rango)

1. PENDIENTE — reglas de cuarentena de datos.

## Registro de incidentes

Todo incidente se registra aquí (append-only): fecha, síntoma, causa raíz, resolución, cambio preventivo.

| Fecha | Incidente | Causa raíz | Resolución |
|---|---|---|---|
| — | — | — | — |
