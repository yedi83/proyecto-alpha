# ADR-0002 — Sistema de agentes de IA: adopción incremental y adversarial

- **Fecha:** 2026-07-02
- **Estado:** Aceptada

## Contexto

Se propuso un sistema multiagente de 16 roles cubriendo todas las áreas del laboratorio (dirección, datos, investigación, régimen, estrategias, operación). El proyecto tiene un solo desarrollador humano y está en Etapa 0 (diseño teórico) con una validación operativa abierta (H-001, Fase A).

## Alternativas consideradas

1. **Implementar los 16 agentes ahora** — organigrama completo desde el día uno. Contras: la mayoría son roles sin tarea verificable hoy; meses de meta-trabajo que compiten con la Etapa 0; un "Director de Proyecto" LLM genera texto que suena a dirección, no dirección.
2. **Ningún agente** — descarta el beneficio real: un desarrollador solo no tiene revisión independiente, y los agentes adversariales mitigan el sesgo de confirmación.
3. **Adopción incremental: 3 agentes alineados a la etapa actual, backlog documentado con condiciones de activación.**

## Decisión

Opción 3. Se crean A-01 Validador Estadístico (adversarial), A-02 Auditor de Datos (adversarial) y A-03 Investigador Cuantitativo (generativo, con autoridad restringida hasta cerrar la Etapa 0: su única misión es el pre-registro retroactivo de H-001). Los 13 restantes quedan en backlog en `docs/AGENTES.md`, cada uno con la condición que dispara su creación. Principios rectores: la IA no toma decisiones de trading; un agente es una tarea verificable, no un rol; el output de un agente es insumo, nunca veredicto; el Ejecutor jamás será un LLM (la ejecución es código determinista).

El principio "la IA no toma decisiones de trading" se eleva a la Constitución (principio 13).

## Consecuencias

- Se gana: revisión independiente inmediata (dictámenes NO APTO bloqueantes) sin desviar la Etapa 0; criterio objetivo para crear futuros agentes ("la tarea existe y duele").
- Se pierde: la visión completa del multiagente queda diferida; parte del documento propuesto (áreas, fases 1–6, data lake ampliado) no se adopta ahora — el roadmap vigente sigue siendo `ROADMAP.md`.
- Riesgo asumido: A-03 es generativo y tentador; se mitiga con la restricción escrita en su prompt y en `AGENTES.md`.
