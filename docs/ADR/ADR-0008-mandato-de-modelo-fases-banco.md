# ADR-0008 — Mandato de modelo para las fases del Banco (propuesta de resolución de V-001)

- **Fecha:** 2026-07-19
- **Estado:** **PROPUESTA — pendiente de ratificación del IP.** Sin efectos hasta ratificar. No modifica el ORQUESTADOR mientras no se ratifique.
- **Alcance:** Gobernanza · Mandato de modelo (ORQUESTADOR)
- **Origen:** Hallazgo **V-001** del dictamen A-04 NO CONFORME sobre F0 (`docs/INVESTIGACION/BANCO/fases/F0_DICTAMEN_A04.md`), documentado en `F0_EXPEDIENTE_NO_CONFORME.md` (F0 auditado: SHA-256 `b99c356…`, commit `0337152`).
- **Estructura:** mecánica de 7 puntos (a pedido del IP). ADR ordinario de metodología — **no** invoca el principio 17 ni anula ningún veredicto: el dictamen A-04 se mantiene; este ADR corrige la norma de fondo y el resultado lo juzga un re-arbitraje nuevo.

---

## 1. Problema detectado

A-04 (sesión independiente) dictó **V-001**: el ORQUESTADOR manda que la fase F0 se ejecute con **"Opus + humano"**, pero F0_PROTOCOLO.md (L3) declara que la sesión la ejecutó **"Investigador Principal (humano) + Fable 5"**. Ejecutor distinto del mandatado → violación de proceso que bloquea el cierre de F0 y la apertura de C-001. Detalle y evidencia: `F0_EXPEDIENTE_NO_CONFORME.md §4 (V-001)`.

La raíz no es un descuido puntual: es una **contradicción entre dos normas del propio laboratorio**. El ORQUESTADOR fija un modelo nominal ("Opus"), mientras que la tabla de modelos del `docs/TRASPASO.md` asigna el trabajo de diseño/arquitectura/hipótesis nuevas al **"mejor disponible"**. F0 (diseño del protocolo del Banco) es precisamente trabajo de diseño metodológico.

## 2. Norma vigente

- `ORQUESTADOR.md` L60 (tabla de Fases, fila F0): *"| F0 | Protocolo del banco | **Opus + humano** | … |"*.
- `ORQUESTADOR.md` L71: *"### F0 — Protocolo (**Opus + humano**, sesión conjunta)"*.
- `ORQUESTADOR.md` L119: *"Sesión F0 (**Opus + humano**). No se abre F1 sin F0 cerrada…"*.
- `TRASPASO.md`, tabla "Qué tarea exige qué modelo": *"Revisión adversarial de código nuevo, diseño de contratos/arquitectura, hipótesis nuevas → **El mejor disponible**"*.

Las tres primeras contradicen a la cuarta para el caso de F0.

## 3. Cambio propuesto (antes / después)

Se propone alinear el ORQUESTADOR con la política de modelos del TRASPASO, deferir al criterio del IP sobre "mejor disponible", y fijar un piso de capacidad. **No se toca F0** (su ejecutor queda reconocido, no reescrito).

**L60 — antes:**
`| F0 | Protocolo del banco | Opus + humano | \`F0_PROTOCOLO.md\`: … |`
**L60 — después:**
`| F0 | Protocolo del banco | Mejor modelo disponible para diseño metodológico + humano (piso: capacidad clase Opus; criterio del IP, según la tabla de modelos del TRASPASO) | \`F0_PROTOCOLO.md\`: … |`

**L71 — antes:** `### F0 — Protocolo (Opus + humano, sesión conjunta)`
**L71 — después:** `### F0 — Protocolo (mejor modelo disponible para diseño metodológico + humano, sesión conjunta)`

**L119 — antes:** `Sesión F0 (Opus + humano). No se abre F1 sin F0 cerrada…`
**L119 — después:** `Sesión F0 (mejor modelo disponible para diseño metodológico + humano, a criterio del IP). No se abre F1 sin F0 cerrada…`

**Cláusula de reconocimiento (nueva, a añadir en el ORQUESTADOR o en el acta de C-001):** *"La F0 del C-001 (2026-07-10) fue ejecutada por Fable 5 + humano. El IP afirma que fue una elección aceptable bajo la política de 'mejor disponible'. V-001 queda resuelta por esta alineación normativa, no por reescritura de F0."*

> Nota de honestidad: el redactor **no afirma** que Fable 5 sea superior o inferior a Opus — esa valoración de modelo es del IP. El cambio no rankea modelos; defiere al juicio del IP ya expresado en el TRASPASO.

## 4. Justificación

Fijar un nombre de modelo en la norma genera *drift*: los modelos cambian y la norma queda desactualizada, produciendo violaciones formales sin fondo. La política del TRASPASO ("mejor disponible") ya existe y es la que gobierna el resto del laboratorio; el ORQUESTADOR debería remitirse a ella, no competir con ella. La **calidad** de F0 no la garantiza la identidad del modelo, sino las dos compuertas que ya existen: A-04 (proceso) y el IP (fondo). Un piso de capacidad ("clase Opus") preserva la exigencia sin congelar un nombre.

**Alternativa considerada y no elegida:** rehacer F0 bajo Opus. Se descarta como primera vía porque es costosa, arriesga introducir cambios de contenido no relacionados (perdiendo trazabilidad de qué se corrigió), y no ataca la raíz (la contradicción normativa persistiría para F1-F7 y para C-002). Queda como último recurso si el IP prefiere no tocar la norma.

## 5. Impacto esperado

- **V-001 se levanta** una vez ratificado este ADR **y** superado un re-arbitraje A-04 independiente sobre la versión resultante.
- El mandato de modelo del Banco queda coherente con el TRASPASO para todas las fases (F0-F7), no solo para este caso.
- **Condición de revisión futura (principio 15):** revisar en el F0 del C-002 si el piso "clase Opus" sigue siendo el adecuado a la luz de los modelos disponibles entonces.

## 6. Compatibilidad hacia atrás

Reconoce la F0 v1 (Fable 5) como válida bajo la política; **no invalida** trabajo previo del ciclo ni obliga a rehacer nada ya producido. No afecta a H-001, H-002 ni a ningún registro fuera del ORQUESTADOR y el acta de C-001.

## 7. Estado

**PROPUESTA pendiente de ratificación del IP.** Secuencia: ratificación del IP → aplicación del cambio de texto en el ORQUESTADOR + cláusula de reconocimiento → re-arbitraje A-04 (sesión independiente nueva) sobre F0 y el checklist. Ningún efecto antes de la ratificación.
