# agents/

Prompts operativos de los agentes de IA del laboratorio. Definiciones formales, principios y backlog: `docs/AGENTES.md`. Decisión de alcance: `docs/ADR/ADR-0002-agentes.md`.

| Agente | Tipo | Archivo |
|---|---|---|
| A-01 Validador Estadístico | Adversarial | `A-01-validador-estadistico.md` |
| A-02 Auditor de Datos | Adversarial | `A-02-auditor-datos.md` |
| A-03 Investigador Cuantitativo | Generativo (autoridad restringida) | `A-03-investigador-cuantitativo.md` |

Regla de uso: el output de un agente es **insumo**, nunca veredicto. Los dictámenes NO APTO de A-01 y A-02 son bloqueantes hasta resolverse.
