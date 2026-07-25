# F7 — Priorización + complementariedad + cola — Ciclo C-001 (fase final)

> **Fecha ejecución: 2026-07-23 · Corrección v3: 2026-07-25 · Ejecutor: Opus (Claude), sesión directa** (por presupuesto; la independencia se mantiene en el A-04). **Fuente de verdad: `F7_COLA.jsonl`** (enriquece los 30 objetos de F6 con el campo `f7`; 0 campos heredados de F6 alterados). **Todas las celdas de las tablas §1 y §3 se generan verbatim desde el JSONL** (regla dura 9 — nunca al revés).
> **Los umbrales y el scoring son PROPUESTAS del banco** (regla dura 6); nada aquí es validación. La priorización ordena candidatas para la cola; **no las promueve a hipótesis** — eso lo hace el IP ratificando el pre-registro formal.

> **Regla de unidad de priorización (decisión del IP 2026-07-25):** *F7 puntúa candidatas/mecanismos **consolidados**, no entradas individuales de F1. Las entradas F1 son evidencia y trazabilidad; varias entradas pueden sustentar una única candidata.* Aplicación: **F1-008 + F1-009 → una sola candidata consolidada `Carry / Funding (M2)`**, puntuada una única vez (el score vive en F1-008; F1-009 es entrada de sustento, `puntuada:false`, sin score propio).

## 1. Scoring (rúbrica de F0 §3 — pesos 35/30/20/10/5)

Escala 0-5 por criterio, **una justificación por celda (toda en el JSONL fuente, campo `f7.justificacion`)**. Se puntúan las **unidades consolidadas**; **persistencia = H-001 (referencia, no se puntúa como candidata nueva).**

| Candidata (unidad consolidada) | Fund. econ. (35%) | Calidad ev. (30%) | Transfer. (20%) | Falsab./claridad (10%) | Complem. (5%) | **Ponderado** |
|---|---|---|---|---|---|---|
| **Carry / Funding (M2)** | 5 — mecanismo causal + contraparte + límites al arbitraje + condiciones de muerte, todo explícito (F4); ancla cripto-nativa Schmeling-Schrimpf-Todorov | 3 — consolidado II-III (Koijen III multi-activo; crypto carry III), pero la evidencia cripto-nativa es reciente/fina (F3) | 3 — VIAJA (el funding ES el carry), pero validación limpia bloqueada por prerrequisitos (F5/F6: survivorship de la cola, spot real, capacidad) | 5 — protocolo completo, hipótesis falsable + condiciones de muerte + compuertas numéricas, endurecido por 16 amenazas adversariales (F6) | 5 — captura distinta (prima de riesgo) frente a H-001 (tendencia) | **4.00** |
| Arb. funding CEX-DEX | 3 — misma prima M2 + riesgo on-chain | 2 — 6 meses + survivorship de venues | 1 — BLOQUEADO (infra DEX) | 2 — boceto | 2 — redundante con carry | **2.15** |
| Prima de iliquidez (ILLIQ) | 2 — degradado por F4 (confound tamaño) | 3 — Amihud III, robustez fuera de microcaps discutida | 1 — BLOQUEADO (Data Lake) | 2 — boceto | 3 — distinto (liquidez) | **2.15** |

> La unidad **Carry / Funding (M2)** se sustenta en las entradas F1 F1-008 + F1-009 (F4 las fusionó en el mecanismo M2); se puntúa **una sola vez**. F1-009 queda en el JSONL como entrada de sustento sin score propio (`consolidada_en: F1-008`).

## 2. Análisis de sensibilidad (±20% por peso)

**El top-1 (carry) es ESTABLE:** variando cada peso ±20% (uno a uno), el máximo sigue siendo el carry en todos los casos (brecha 4.00 vs 2.15, no reversible). El empate CEX-DEX/ILLIQ en 2.15 puede romperse bajo perturbación, pero es **inmaterial**: ambos están bloqueados por prerrequisito y ninguno pasa a la cola activa. No hay top-3 inestable que reportar.

## 3. Mapa conceptual de complementariedad (SIN pesos)

Qué captura cada edge y su relación con lo ya en pipeline (**H-001 = tendencia/persistencia**). Celdas `captura` y relación tomadas verbatim de `f7.captura` y `f7.complementariedad_H001` del JSONL:

| Candidata | Captura | Relación con H-001 |
|---|---|---|
| **Carry / Funding (M2)** | Prima de riesgo / carry | COMPLEMENTARIO — prima de riesgo/carry vs tendencia/persistencia; ineficiencia distinta de la tendencia, baja correlacion esperada. Es exactamente lo que un segundo motor deberia aportar: diversificacion de fuente de retorno, no otra forma de lo mismo. |
| Arb. funding CEX-DEX | Prima de riesgo (M2) + arb de venue | REDUNDANTE con el carry núcleo (mismo mecanismo M2, capa extra de riesgo on-chain) |
| Prima de iliquidez (ILLIQ) | Liquidez / reversión | DISTINTO (liquidez/reversión) — conecta con la candidata ILLIQ-MR-001 ya en cola |

## 4. Salida del ciclo — top-N a la cola del REGISTRO (N lo ratifica el IP)

Propuesta (F0 §7: 0-5 candidatas, sin mínimo; N final lo fija el IP):

- **TOP-1 → `Carry / Funding (M2)`: CANDIDATA EN COLA** (unidad consolidada de F1-008+F1-009), complementaria a H-001, **condicionada al Data Lake** para una validación limpia (survivorship de la cola del carry-crash, serie spot real por A-02, capacidad). Protocolo completo en `F6_PROTOCOLOS.md §2`. Candidata natural al próximo H-XXX del pipeline **tras** el Data Lake y el pre-registro formal.
- **Bocetos (CEX-DEX, ILLIQ): NO pasan a la cola activa** — bloqueados por prerrequisito (infra DEX / Data Lake). Quedan documentados para cuando su prerrequisito exista.
- **Ya en cola (del insight del IP):** `ILLIQ-MR-001` (H-003 candidata, reversión condicional a la iliquidez), también dependiente del Data Lake.

## 5. Conclusión del Ciclo C-001 (meta-pregunta de F0 §1.4)

La pregunta que el C-001 debía responder no era "¿cuántas hipótesis produce el Banco?" sino **"¿el método del Banco produce protocolos sólidos y priorizaciones consistentes?"** Respuesta, honesta:

- El Banco corrió **F0→F7 de punta a punta**, cada fase con **dictamen A-04 independiente** y aprobación del IP; el arbitraje cazó desviaciones reales en casi todas las fases (incluidas varias del mentor) y las forzó a corregirse por el canal correcto — **incluida esta F7** (A-04 v1 y v2 NO CONFORME por justificación presente solo en la vista; corregida poblando la fuente y regenerando la vista verbatim).
- Produjo **una candidata con fundamento económico explícito y protocolo de validación completo, falsable y endurecido adversarialmente (carry) — pero cuya eficacia como edge y cuya ejecutabilidad aún no han sido demostradas** (mecanismo plausible ≠ edge demostrado ≠ estrategia ejecutable, F6). Y, sobre todo, **honestamente acotada**: no "aquí tienes la estrategia", sino "aquí tienes el candidato y exactamente qué falta para validarlo".
- Identificó el **Data Lake** (universo amplio + delistados + funding + spot real) como el **cuello de botella de infraestructura** que desbloquea a **la candidata que ocupa el primer lugar en la rúbrica de priorización de F7** *y* a la candidata ILLIQ-MR-001. Es el hallazgo de inversión más accionable del ciclo.
- Generó, además, una candidata extra (`ILLIQ-MR-001`) del cruce entre el proceso y el juicio del IP.

**El valor de C-001 no es una hipótesis lista para mañana. Es que el proceso funcionó: filtró 30 mecanismos de la literatura hasta 1 candidata bien fundada y honestamente condicionada, sin autoengaño, y te dijo qué construir para seguir.** Un ciclo con una candidata en cola (condicionada) no fracasó (F0 §7).

> **F7 CERRADA 2026-07-25** — A-04 CONFORME (v3, `F7_DICTAMEN_A04.md`; rastro append-only v1/v2 NO CONFORME → v3 CONFORME) + **aprobación explícita del IP**. Con el cierre de F7 se **CIERRA EL CICLO C-001 completo**. Hallazgo de gobernanza registrado como ADR-0010 (Pendiente, para el F0 del C-002). El rótulo "Arb. funding CEX-DEX" se mantiene por decisión del IP (contracción del nombre en fuente, no excede).
