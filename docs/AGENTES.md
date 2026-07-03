# Sistema de Agentes

> Agentes de IA que asisten al laboratorio. Decisión y alcance en `ADR/ADR-0002-agentes.md`. Los prompts operativos viven en `agents/`.

## Principios del sistema de agentes

1. **La IA no toma decisiones de trading.** Ningún agente decide comprar, vender ni asignar capital. Investigan, auditan, clasifican y documentan; la evidencia cuantitativa decide.
2. **Un agente es una tarea verificable, no un rol.** Cada agente tiene entradas y salidas concretas. No existen agentes "todoterreno" ni agentes cuyo output sea solo opinión sin checklist.
3. **Los agentes más valiosos son adversariales.** El laboratorio tiene un solo investigador humano; su mayor riesgo es el sesgo de confirmación. Los agentes revisores (validador, auditor) existen para intentar destruir el trabajo, no para aprobarlo.
4. **Un agente nuevo se crea solo cuando su tarea ya existe y duele.** No se crean agentes para fases futuras.
5. **El output de un agente es insumo, nunca veredicto.** Los veredictos los emite el proceso definido en `INVESTIGACION/PROTOCOLO.md`.

## Plantilla de definición (obligatoria antes de implementar cualquier agente)

Misión · Responsabilidades · Entradas · Salidas · Límites (qué tiene prohibido) · Herramientas · Interacción con otros agentes · Autoridad · Métricas de desempeño.

---

## Agentes activos (Fase 1)

### A-01 · Validador Estadístico — adversarial

| Campo | Definición |
|---|---|
| Misión | Intentar destruir todo informe de experimento antes de que cuente como evidencia. |
| Responsabilidades | Verificar cumplimiento del protocolo: pre-registro previo, N de configuraciones declarado, corrección por pruebas múltiples, particiones respetadas, lockbox íntegro, métricas dentro de umbrales pre-escritos. |
| Entradas | Informe de experimento (`research/H-XXX/report/` o `experiments/exp-NNN/`) + ficha de la hipótesis + `PROTOCOLO.md`. |
| Salidas | Dictamen estructurado: violaciones detectadas (bloqueantes/menores), preguntas sin responder, y recomendación APTO / NO APTO como evidencia. |
| Límites | No propone mejoras a la estrategia (eso sería co-investigar y perdería independencia). No emite veredictos de hipótesis. |
| Autoridad | Un NO APTO bloquea el uso del experimento como evidencia hasta resolverse. |
| Métricas | Violaciones bloqueantes detectadas que el humano había pasado por alto. |

### A-02 · Auditor de Datos — adversarial

| Campo | Definición |
|---|---|
| Misión | Impedir que datos contaminados entren a investigación o ejecución. |
| Responsabilidades | Buscar lookahead (alineación temporal velas/funding), survivorship (universo vs. delistados), huecos, duplicados, outliers imposibles, cambios de convención del exchange. |
| Entradas | Dataset o script de descarga + `DATA.md` + descripción del universo declarado en la hipótesis. |
| Salidas | Informe de auditoría: hallazgos por severidad, sesgos no tratados, y APTO / NO APTO para investigación. |
| Límites | No corrige datos (propone; el humano ejecuta y re-audita). No opina sobre estrategias. |
| Autoridad | Un NO APTO impide usar el dataset en cualquier experimento. |
| Métricas | Sesgos detectados antes de que un experimento los consumiera. |

### A-03 · Investigador Cuantitativo — generativo, con autoridad restringida

| Campo | Definición |
|---|---|
| Misión | Formular hipótesis económicas rigurosas y diseñar su pre-registro. |
| Responsabilidades | Redactar hipótesis económica (quién pierde al otro lado), predecir regímenes de aplicabilidad, acotar espacio de parámetros, definir predicciones falsables y umbrales de rechazo. |
| Entradas | Datos auditados (APTO de A-02), literatura, fichas existentes. |
| Salidas | Fichas de pre-registro completas (`docs/INVESTIGACION/hipotesis/`), análisis exploratorios en `research/H-XXX/analysis/`. |
| Límites | **Restricción vigente: mientras la Etapa 0 del `PLAN_TRABAJO.md` no esté cerrada, su única misión es completar el pre-registro retroactivo de H-001** (hipótesis económica, regímenes esperados, las 5 preguntas). No genera hipótesis nuevas hasta entonces. Nunca ejecuta backtests "rápidos" fuera del pipeline. |
| Autoridad | Ninguna sobre veredictos. Sus hipótesis entran al pipeline como cualquier otra. |
| Métricas | Calidad de pre-registros (¿el Validador los aprueba a la primera?); honestidad de predicciones de régimen verificadas ex-post. |

### Flujo entre los tres

```
Investigador (A-03) → pre-registro → Auditor de Datos (A-02) valida el dataset
                                            ↓
                        humano ejecuta experimentos (pipeline)
                                            ↓
                  Validador Estadístico (A-01) dictamina APTO/NO APTO
                                            ↓
                        el protocolo emite el veredicto
```

---

## Backlog (no se crean hasta que su tarea exista y duela)

| Agente | Se crea cuando… |
|---|---|
| Documentalista/Gobernanza | Los PENDIENTE y las inconsistencias entre docs se acumulen más rápido de lo que se resuelven |
| Ingeniero de Datos | Arranque la construcción del Data Lake (Etapa 3) |
| Constructor de Regímenes | Exista Data Lake auditado (ROADMAP: investigación descriptiva) |
| Analista de Estrategias | Existan ≥2 estrategias validadas que comparar |
| Risk Manager / Portfolio Manager | Exista ≥2 estrategias en producción y asignación de capital real |
| Auditor Live | H-001 entre a Fase C |
| Especialista ML | Fase de ML del roadmap (fuera de los 12 meses) |
| Analista Macro / On-chain / Derivados | El Data Lake incorpore esas fuentes (hoy fuera de alcance) |
| Ejecutor | Nunca como IA generativa: la ejecución es código determinista (`bot/`), no un agente LLM |
| Director de Proyecto / Arquitecto | Probablemente nunca como agentes: sus funciones verificables ya las cubren `ESTADO.md`, los ADR y el Documentalista |
