# Criterios de las Fases de Validación Operativa

> **Regla constitucional:** los números de cada fase se escriben ANTES de iniciar (o continuar) esa fase. Un criterio escrito después del resultado no es un criterio.

## ⚖️ ENMIENDA DE GOBERNANZA (2026-07-02)

Al inventariar el laboratorio original (`donchian512_lab`) se descubrió que **la Fase A de H-001 ya estaba formalmente iniciada** (acta del 2026-07-02 03:53:46 UTC) bajo un pre-registro propio anterior y vinculado al sistema en ejecución: [`PREREG_FASE_AB.md`](../../research/H-001-canal-donchian/prereg/PREREG_FASE_AB.md) (migrado al repo, verbatim).

**Resolución:** no se mueven los postes a mitad de fase. La Fase A y B **en curso de H-001 se gobiernan por su PREREG original** (mínimo 10 días, 6 criterios, replay offline, criterios de aborto). La tabla de este documento **no aplica retroactivamente a la fase en curso**: queda como plantilla mínima para futuras hipótesis y futuras re-corridas de fase, donde ambos conjuntos deberán reconciliarse antes de iniciar. Este conflicto existió porque la tabla se escribió sin conocimiento del PREREG — se documenta en vez de ocultarse.

> Estado: 🟡 Fase A/B de H-001 → gobernadas por su PREREG. Tabla de este documento → plantilla para fases futuras. Fase C: los criterios del PREREG (§Paso a C) se complementarán con `RISK_POLICY.md` antes de iniciarla.

## Fase A — Dry Run

El bot corre conectado a datos reales sin enviar órdenes. **No se evalúa rentabilidad.**

Contexto que dimensiona estos números (H-001): velas de 15 minutos, 5 pares, canal Donchian 512 (~5.3 días), frecuencia estimada de señales > 10/mes (dato por confirmar en el informe del backtest). Velas esperadas: 5 pares × 96 velas/día ≈ 480/día ≈ 13 440 en 28 días.

**Inicio del reloj:** la Fase A formal comienza en la fecha del commit de estos criterios. Los días de dry run previos cuentan únicamente si sus logs permiten auditarlos retroactivamente contra esta tabla completa; si los logs son parciales, fueron rodaje y no son evidencia.

| Criterio | Umbral de aprobación | Umbral de reprobación |
|---|---|---|
| Duración mínima | ≥ 28 días continuos **y** ≥ 15 señales observadas (lo que ocurra más tarde) | — |
| Frecuencia de señales vs. backtest | Si en 28 días hay < 15 señales, se extiende la fase y se investiga la discrepancia con la frecuencia del backtest antes de aprobar | Discrepancia sin explicación documentada |
| Uptime del bot | ≥ 99.0% del período (≤ ~6.7 h acumuladas de caída en 28 días) | < 97.0% |
| Coincidencia señal a señal: bot vs. backtester sobre las mismas velas | 100% (misma vela, misma dirección, mismo tamaño objetivo) | ≥ 1 divergencia sin causa raíz documentada |
| Latencia de señal | Señal emitida ≤ 60 s tras el cierre de la vela de 15m, en ≥ 99% de los casos | > 5 min en cualquier señal |
| Velas atrasadas / perdidas | ≤ 0.1% de las velas esperadas (~13 en 28 días), todas detectadas y registradas por el bot | > 0.5%, o cualquier vela perdida NO detectada por el sistema |
| Señal generada sobre datos incompletos | 0 casos | ≥ 1 caso |
| Reconexiones | 100% de desconexiones recuperadas automáticamente en ≤ 2 min | ≥ 1 desconexión que exigió intervención manual, o ≥ 3 caídas en 24 h |
| Incidentes sin resolver en RUNBOOK | 0 sin causa raíz documentada | ≥ 1 sin causa raíz |

**Regla de evaluación:** la fase se aprueba solo si TODOS los criterios aprueban. Un criterio reprobado = fase reprobada; se corrige la causa y el reloj se reinicia (28 días desde el arreglo). "Casi pasa" = no pasa.

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
