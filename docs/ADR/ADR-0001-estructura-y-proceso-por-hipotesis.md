# ADR-0001 — Estructura del repositorio y proceso centrado en hipótesis

- **Fecha:** 2026-07-01
- **Estado:** Aceptada

## Contexto

El proyecto existía como código funcional (backtester, bot, dashboard) más documentación dispersa y cronológica. La primera estrategia (canal de Donchian) se trataba como "validada" sin criterios escritos previos ni registro del proceso de investigación. Una revisión crítica externa identificó: ausencia de criterios cuantitativos pre-escritos, riesgo de sobreajuste no auditado, doble fuente de verdad documental y mezcla de componentes reales con planificados.

## Alternativas consideradas

1. **Mantener la documentación como informe cronológico** — fácil de escribir, pero se degrada con el tiempo y no fuerza disciplina metodológica.
2. **README extenso como documento único** — una sola fuente, pero mezcla estado, filosofía y visión; diverge de la realidad en semanas.
3. **Repositorio estructurado con docs/ modular y proceso por hipótesis** — más trabajo inicial; convierte la documentación en parte del método.

## Decisión

Se adopta la opción 3:

- README corto que enlaza; el estado vive solo en `ESTADO.md`.
- Toda idea de trading es una **hipótesis** (H-XXX) que entra a un pipeline con pre-registro, veredicto explícito y registro append-only, incluidas las rechazadas.
- El canal de Donchian se reclasifica de "estrategia validada" a **H-001: hipótesis en validación**, con sus limitaciones epistemológicas declaradas (pre-registro retroactivo).
- Los criterios de las fases A/B/C y los límites de riesgo se escriben antes de las decisiones que gobiernan.
- Los regímenes de aplicabilidad se predicen en el pre-registro y se verifican después, nunca al revés.

## Consecuencias

- Se gana: trazabilidad, defensa contra sesgo de confirmación, base para que la segunda hipótesis cueste menos que la primera (test de la tesis del proyecto).
- Se pierde: velocidad aparente; escribir criterios antes de medir es incómodo por diseño.
- Deuda asumida: H-001 tiene pre-registro retroactivo; sus resultados históricos son menos confiables que los de futuras hipótesis y así se declara.
