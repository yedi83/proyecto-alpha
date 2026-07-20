# Expediente — Dictamen A-04 NO CONFORME sobre F0 (Ciclo C-001)

> Abierto 2026-07-19. Append-only. Reúne, con identificación inequívoca, todo lo necesario para que el IP decida el tratamiento (ADR) de los hallazgos y para que un tercero pueda auditar la separación de funciones. **No decide el tratamiento** — eso es del IP. El dictamen íntegro vive en `F0_DICTAMEN_A04.md` (fuente única); aquí se clasifica y fundamenta.

## 1. Identificación inequívoca del artefacto auditado

| Ítem | Valor |
|---|---|
| Archivo | `docs/INVESTIGACION/BANCO/fases/F0_PROTOCOLO.md` |
| SHA-256 | `b99c3569cfe33d357288463f25be3564e53ec3c8511d225772a305fc587557f4` |
| git blob | `e597a4691f818b8de9fab8baf2644afa38ef8c75` |
| Último commit que lo tocó | `0337152` (2026-07-11) |
| Fecha de contenido (encabezado) | 2026-07-10 (sesión conjunta) |
| Working tree vs HEAD | **idéntico** (sin cambios sin commitear) → la versión auditada es exactamente la versionada en git |
| Versión declarada | El encabezado no lleva nº de versión propio; se identifica por hash + commit |

## 2. Normas contra las que se auditó (fijadas por hash)

| Documento | SHA-256 | git blob | Commit |
|---|---|---|---|
| `docs/INVESTIGACION/BANCO/ORQUESTADOR.md` | `f5334d96a7a633845a13e9b3ef8182ebc7e9d1afe769879ac34b0142f72d8f6d` | `b192292a0932b5c3a7d040f3fe56dbbaa64dccd0` | `9e3e930` (2026-07-11) |
| `agents/A-04-arbitro-metodologia.md` (prompt del auditor) | `b373ec93bedb21dd1804e87f75c5b7e4c62b182b4d2d1c14da81058aaf42f439` | `c13a3a2b9f0692a1fff0e756e4020cc966bf6334` | `9e3e930` (2026-07-11) |

## 3. Constancia de la dieta de insumos del auditor (lo que hace fiable la independencia)

El dictamen se produjo en un **subagente aislado**, arrancado en frío, **sin ningún acceso al contexto de esta conversación** (ni H-002, ni la agenda de C-001, ni opinión alguna del investigador).

**Insumos entregados (dieta cerrada, exactamente los que exige A-04 en Modo VALIDADOR ESTRICTO):**
1. `agents/A-04-arbitro-metodologia.md` — su prompt de rol.
2. `docs/INVESTIGACION/BANCO/ORQUESTADOR.md` — norma aplicable.
3. `docs/INVESTIGACION/BANCO/fases/F0_PROTOCOLO.md` — artefacto a arbitrar.

**Prohibiciones dadas al auditor (verbatim de la instrucción):** "NO leas, listes ni busques ningún otro archivo (nada de README, CONSTITUCION, CHANGELOG, ESTADO, historial, ni fichas de hipótesis)… NO tienes ningún contexto de conversación previa… Si un requisito exige evidencia que no está en esos tres archivos, ese requisito es NO VERIFICABLE y cuenta contra la conformidad."

**Evidencia de que respetó la dieta:**
- Consumo de herramientas del subagente: **3 lecturas de archivo** (`tool_uses: 3`), consistente con leer exactamente los tres archivos de la dieta y ninguno más.
- El propio dictamen **se auto-limita**: declaró NO VERIFICABLE / FUERA DE MI ALCANCE los puntos del checklist que exigían documentos fuera de la dieta (consistencia con la Constitución, estado de ADRs, estado del repositorio/tag, acta de una línea). Un auditor que hubiera mirado más no habría necesitado declararlos no verificables. Esa auto-declaración es prueba positiva del respeto a la frontera.
- Arranque en frío: contexto de conversación = 0 (subagente nuevo).

## 4. Dictamen y hallazgos clasificados

Veredicto: **NO CONFORME**. Texto íntegro archivado en `F0_DICTAMEN_A04.md` (firmado "A-04 · 2026-07-19 · sesión independiente"). Clasificación de cada hallazgo:

### V-001 — VIOLACIÓN (obligatoria, bloqueante)

- **Norma (textual):** ORQUESTADOR L60, tabla de Fases, fila F0, col. Modelo: *"| F0 | Protocolo del banco | **Opus + humano** | …"*; y L71: *"### F0 — Protocolo (**Opus + humano**, sesión conjunta)"*; refrendado en L119: *"Sesión F0 (Opus + humano)."*
- **Hecho:** F0_PROTOCOLO.md L3: *"Sesión conjunta 2026-07-10: Investigador Principal (humano) + **Fable 5**."*
- **Incumplimiento:** el ejecutor de la fase no es el mandatado por la norma (Fable 5 en lugar de Opus). A-04 no juzga si Fable 5 lo hizo bien; juzga que la fase se otorgó a un modelo distinto del que la norma le asigna.
- **Evidencia:** líneas citadas + hashes de §1 y §2.

### C-001 — CONTRADICCIÓN norma↔artefacto (requiere resolución del IP; bloqueante hasta resolver)

- **Norma (textual):** ORQUESTADOR L73, prompt F0, criterios de la rúbrica: *"(3) rúbrica: criterios (calidad de evidencia, fundamento económico, transferibilidad, **resiliencia**, complementariedad conceptual con lo ya en pipeline)…"*.
- **Hecho:** F0 §3 (L32-36) puntúa: Fundamento económico 35%, Calidad de la evidencia 30%, Transferibilidad 20%, **Falsabilidad/claridad del protocolo 10%**, Complementariedad 5%. **No puntúa "resiliencia"**; F0 §3(c) (L38): *"la **resiliencia adversarial no se puntúa: es COMPUERTA**"*. Es decir: sustituye el criterio enumerado "resiliencia" por uno no enumerado ("Falsabilidad/claridad") y traslada la resiliencia a compuerta.
- **Naturaleza:** A-04 la reporta y **no la resuelve** (por diseño). La tensión es entre el texto normativo (criterios enumerados) y el artefacto (reclasificación + criterio añadido).
- **Evidencia:** líneas citadas + hashes.

### OBS-1 — Observación (no bloqueante)

Rúbrica rotulada "ADR provisional v1.0" con "pesos provisionales" (F0 §3, §3(a)). A-04 anota que "provisional" no contradice por sí solo la inmutabilidad intra-ciclo (F0 la circunscribe a revisión inter-ciclo). Para el registro.

### OBS-2 — Observación (no bloqueante)

Anclas verbales fijadas solo en los puntos 0/3/5 de la escala 0–5; los puntos 1/2/4 quedan sin ancla textual. Suficiente para la casilla literal; anotado.

## 5. Análisis de causa raíz (insumo para la decisión del IP — no la decide)

Los dos hallazgos bloqueantes parecen **conceptualmente independientes**, con causas y remedios distintos:

- **V-001** es sobre **quién ejecutó** F0 (gobernanza del mandato de modelo). Su raíz probable es una contradicción latente entre ORQUESTADOR ("Opus + humano" para F0) y la tabla de modelos del TRASPASO ("arquitectura/hipótesis nuevas → el mejor disponible"). Remedio candidato: ADR que reconcilie ambas normas y reconozca la ejecución por Fable 5.
- **C-001** es sobre **qué contiene** F0 (diseño de la rúbrica). Su raíz es una divergencia entre la lista de criterios del prompt del ORQUESTADOR y la rúbrica efectiva de F0. Remedio candidato: enmienda fechada al ORQUESTADOR que actualice sus criterios para reflejar F0 (resiliencia-compuerta + falsabilidad), o revertir F0.

Como no comparten causa raíz ni un único cambio los resuelve, tu propio criterio ("un ADR por decisión; dos ADR si son problemas distintos") apunta a **dos ADR separados**. Esto es un análisis, no una decisión: la tomas tú.

Nota: OBS-1 y OBS-2 no requieren ADR; se dejan registradas y, si acaso, se atienden en el F0 del C-002 (regla de inmutabilidad: no se parchea a mitad de ciclo).

## 6. Estado y condición de levantamiento

**F0 no cierra; C-001 no abre.** Ningún acto de apertura (tag `banco-C001-abierto`, acta) es válido antes del CONFORME. Condición de levantamiento: el IP resuelve V-001 y C-001 por el canal ADR/enmienda fechada, y luego **re-arbitraje A-04 en sesión independiente nueva** (sobre la versión resultante, con su nuevo hash). El re-arbitraje no puede reutilizar este dictamen ni presuponer su levantamiento.
