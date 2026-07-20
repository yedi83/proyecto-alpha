# ADR-0008 — Mandato de modelo para las fases del Banco (enmienda de política + ratificación de la F0 del C-001)

- **Fecha:** 2026-07-19
- **Estado:** **ACEPTADA — RATIFICADA por el IP el 2026-07-19.** Aplicada al ORQUESTADOR (L60/L71/L119 + nota de ratificación de la F0 por Fable 5). El hallazgo V-001 quedó **resuelto**: la versión enmendada del ORQUESTADOR obtuvo dictamen A-04 CONFORME (`F0_DICTAMEN_A04_v2.md`, 2026-07-19). El dictamen v1 (NO CONFORME) se conserva íntegro en el registro.
- **Alcance:** Gobernanza · Mandato de modelo (ORQUESTADOR)
- **Origen:** Hallazgo **V-001** del dictamen A-04 NO CONFORME sobre F0 (`F0_DICTAMEN_A04.md`), documentado en `F0_EXPEDIENTE_NO_CONFORME.md` (F0 auditado: SHA-256 `b99c356…`, commit `0337152`).
- **Reencuadre (v2 del borrador):** la v1 planteaba esto como "resolver una contradicción" ORQUESTADOR↔TRASPASO, lo que dependía de un salto interpretativo (que F0 fuera "diseño de arquitectura"). Se reencuadra como lo que realmente es: **una enmienda de política deliberada del IP + la ratificación de la ejecución de F0 por Fable 5.** También se elimina el "piso clase Opus" de la v1 (regla extra innecesaria).
- **Nota:** ADR ordinario de metodología. No invoca el principio 17 ni anula el dictamen A-04 (que se mantiene): la violación V-001 fue real bajo el texto anterior; se resuelve enmendando ese texto —cosa que el IP tiene autoridad para hacer— y ratificando la ejecución pasada. La versión resultante la juzga un re-arbitraje nuevo.

---

## 1. Problema detectado

A-04 (sesión independiente) dictó **V-001**: el ORQUESTADOR manda que la fase F0 se ejecute con **"Opus + humano"**, pero F0_PROTOCOLO.md (L3) declara que la sesión la ejecutó **"Investigador Principal (humano) + Fable 5"**. Bajo el texto vigente, es una violación real: se usó un modelo distinto del nominado. Detalle y evidencia: `F0_EXPEDIENTE_NO_CONFORME.md §4 (V-001)`.

## 2. Norma vigente

- `ORQUESTADOR.md` L60 (tabla de Fases, fila F0): *"| F0 | Protocolo del banco | **Opus + humano** | … |"*.
- `ORQUESTADOR.md` L71: *"### F0 — Protocolo (**Opus + humano**, sesión conjunta)"*.
- `ORQUESTADOR.md` L119: *"Sesión F0 (**Opus + humano**). No se abre F1 sin F0 cerrada…"*.
- Contexto (política de modelos del laboratorio): `TRASPASO.md` L71: *"Revisión adversarial de código nuevo, diseño de contratos/arquitectura, hipótesis nuevas → **El mejor disponible**"*.

## 3. Cambio propuesto (antes / después)

Enmienda deliberada: el ORQUESTADOR deja de nominar un modelo fijo para F0 y remite a la política de "mejor disponible a criterio del IP". **No se toca F0** (su ejecutor se ratifica, no se reescribe).

**L60 — antes:** `| F0 | Protocolo del banco | Opus + humano | \`F0_PROTOCOLO.md\`: … |`
**L60 — después:** `| F0 | Protocolo del banco | Mejor modelo disponible a criterio del IP + humano | \`F0_PROTOCOLO.md\`: … |`

**L71 — antes:** `### F0 — Protocolo (Opus + humano, sesión conjunta)`
**L71 — después:** `### F0 — Protocolo (mejor modelo disponible a criterio del IP + humano, sesión conjunta)`

**L119 — antes:** `Sesión F0 (Opus + humano). No se abre F1 sin F0 cerrada…`
**L119 — después:** `Sesión F0 (mejor modelo disponible a criterio del IP + humano). No se abre F1 sin F0 cerrada…`

**Cláusula de ratificación (nueva, a añadir al pie de la fila F0 en el ORQUESTADOR o en el acta de C-001):** *"La F0 del C-001 (2026-07-10) fue ejecutada por Fable 5 + humano. El IP la ratifica como ejecución válida bajo esta política. El hallazgo V-001 queda resuelto por esta enmienda de política + ratificación, no por reescritura de F0."*

## 4. Justificación

Es una **decisión de política**, no la reparación de un descuido: el IP prefiere que el modelo de cada fase lo fije "el mejor disponible" a su criterio (como ya hace el resto del laboratorio en el TRASPASO), en vez de clavar un nombre de modelo que envejece y genera violaciones formales sin fondo cada vez que cambian los modelos. La **calidad** de F0 la garantizan las dos compuertas existentes —A-04 (proceso) y el IP (fondo)—, no la identidad del modelo. Se reencuadra respecto a la v1 del borrador para **no depender de afirmar una "contradicción"** que un árbitro estricto podría rechazar; una enmienda de política es inatacable porque el IP tiene la autoridad para dictarla. Se elimina el "piso clase Opus" de la v1 por ser una regla añadida que no hacía falta para resolver V-001.

**Alternativa considerada y no elegida:** rehacer F0 bajo Opus. Se descarta por costosa, por arriesgar cambios de contenido no relacionados (perdiendo trazabilidad) y por no resolver el fondo (el nombre de modelo clavado seguiría chocando con la política para F1-F7 y C-002).

## 5. Impacto esperado

- **El hallazgo V-001 queda resuelto** mediante este ADR; la versión enmendada del ORQUESTADOR obtuvo dictamen A-04 CONFORME (`F0_DICTAMEN_A04_v2.md`). El dictamen v1 NO CONFORME permanece en el registro (no se borra ni se anula).
- El mandato de modelo del Banco queda alineado con la política del laboratorio para todas las fases.
- **Condición de revisión futura (principio 15):** revisar en el F0 del C-002 si "mejor disponible a criterio del IP" sigue siendo el criterio adecuado.

## 6. Compatibilidad hacia atrás

Ratifica la F0 v1 (Fable 5) como válida; **no invalida** trabajo previo del ciclo ni obliga a rehacer nada. No afecta a H-001, H-002 ni a registros fuera del ORQUESTADOR y el acta de C-001.

## 7. Estado

**PROPUESTA (v2) pendiente de ratificación del IP.** Secuencia: ratificación → aplicar el cambio de texto en el ORQUESTADOR + cláusula de ratificación → re-congelar F0 → re-arbitraje A-04 (sesión independiente nueva). Ningún efecto antes de la ratificación.
