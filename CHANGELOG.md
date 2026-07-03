# Changelog

## 2026-07-02 (hipótesis económica H-001)

- A-03: `research/H-001-canal-donchian/HIPOTESIS_ECONOMICA.md` — mecanismo (subreacción + cascadas de liquidación + límites al arbitraje conductuales), contraparte identificada, 5 predicciones falsables (P1 ya consistente), 4 señales de retiro conceptual. Formulada ex-post y así declarada.

## 2026-07-02 (inventario del lab original)

- **Inventario de `donchian512_lab`** (`docs/MIGRACION.md`): pre-registros y 17 informes migrados a `research/H-001-canal-donchian/`. Regla maestra: el sistema vivo no se toca hasta cerrar Fase A.
- **Enmienda de gobernanza** en `CRITERIOS_FASES.md`: la Fase A en curso se rige por su PREREG original (acta 2026-07-02 03:53 UTC); la tabla del repo queda como plantilla futura.
- **Ficha H-001 reescrita**: pre-registro reconocido como original (no retroactivo), 5 preguntas respondidas con evidencia, métricas consolidadas (Sharpe ~0.42, alfa t=0.94 NS, top-5 trades = 115% del neto), corrección visible en el registro de hipótesis.
- `.gitignore`: añadido `config.env` (el lab contiene API keys que jamás deben entrar al repo).

- **Criterios de la Fase A fijados antes de evaluar** (tarea 0.1 del plan): 28 días + ≥15 señales, uptime ≥99%, coincidencia bot/backtester 100%, latencia ≤60 s, velas perdidas ≤0.1%, reconexión automática ≤2 min. Regla: todos aprueban o la fase reprueba. Ficha H-001 actualizada: 512 velas de 15m (~5.3 días), 5 pares.

- Sistema de agentes (ADR-0002): A-01 Validador Estadístico, A-02 Auditor de Datos, A-03 Investigador Cuantitativo (restringido a H-001 hasta cerrar Etapa 0). Backlog de 13 agentes con condiciones de activación en `docs/AGENTES.md`. Principio 13 añadido a la Constitución: la IA no toma decisiones de trading.
- `docs/PLAN_TRABAJO.md`: análisis de arranque, etapas 0–4 (teoría → migración → programación), contratos a diseñar, disciplina de git.
- Convención de carpetas por hipótesis: `research/_template/` copiable, `research/H-001-canal-donchian/` creada, `strategies/` (biblioteca de validadas congeladas).

## 2026-07-01

- Creación del repositorio con estructura documental completa.
- ADR-0001: adopción del proceso centrado en hipótesis.
- H-001 (Canal de Donchian) registrada como hipótesis en validación, Fase A.
- Pendiente: migración del código existente (backtester, bot, dashboard) y completar campos PENDIENTE de criterios y riesgo.
