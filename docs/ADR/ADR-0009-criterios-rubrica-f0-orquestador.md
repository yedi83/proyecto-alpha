# ADR-0009 — Criterios de la rúbrica de F0 en el ORQUESTADOR (propuesta de resolución de C-001)

- **Fecha:** 2026-07-19
- **Estado:** **PROPUESTA — pendiente de ratificación del IP.** Sin efectos hasta ratificar. No modifica el ORQUESTADOR ni F0 mientras no se ratifique.
- **Alcance:** Gobernanza · Rúbrica del Banco (ORQUESTADOR)
- **Origen:** Hallazgo **C-001** (contradicción) del dictamen A-04 NO CONFORME sobre F0 (`F0_DICTAMEN_A04.md`), documentado en `F0_EXPEDIENTE_NO_CONFORME.md` (F0 auditado: SHA-256 `b99c356…`, commit `0337152`).
- **Estructura:** mecánica de 7 puntos (a pedido del IP). ADR ordinario de metodología — no invoca el principio 17.

---

## 1. Problema detectado

A-04 reportó **C-001** (contradicción, que por diseño no resuelve): la lista de criterios de la rúbrica en el prompt F0 del ORQUESTADOR **no coincide** con la rúbrica efectiva de F0. El ORQUESTADOR enumera "resiliencia" como criterio puntuado; F0 §3 **no la puntúa** —la trata como compuerta (§3(c))— y en su lugar puntúa "Falsabilidad/claridad del protocolo" (10%), criterio no enumerado por el ORQUESTADOR. Detalle y evidencia: `F0_EXPEDIENTE_NO_CONFORME.md §4 (C-001)`.

## 2. Norma vigente

- `ORQUESTADOR.md` L73 (prompt F0), criterios de la rúbrica: *"(3) rúbrica: criterios (calidad de evidencia, fundamento económico, transferibilidad, **resiliencia**, complementariedad conceptual con lo ya en pipeline), escala 0–5 con anclas verbales, pesos declarados;"*.
- `F0_PROTOCOLO.md` §3 (L32-36): puntúa Fundamento económico (35%), Calidad de la evidencia (30%), Transferibilidad (20%), **Falsabilidad/claridad del protocolo (10%)**, Complementariedad (5%).
- `F0_PROTOCOLO.md` §3(c) (L38): *"la **resiliencia adversarial no se puntúa: es COMPUERTA** — las amenazas a la validez de F6b deben quedar incorporadas al protocolo … o el protocolo no pasa a F7, tenga la nota que tenga."*

## 3. Cambio propuesto (antes / después)

Se reconcilia **hacia F0** (no se toca F0): se actualiza el ORQUESTADOR L73 para que su lista de criterios refleje la rúbrica efectiva de F0.

**L73 (fragmento de criterios) — antes:**
`(3) rúbrica: criterios (calidad de evidencia, fundamento económico, transferibilidad, resiliencia, complementariedad conceptual con lo ya en pipeline), escala 0–5 con anclas verbales, pesos declarados;`

**L73 (fragmento de criterios) — después:**
`(3) rúbrica: criterios PUNTUADOS (calidad de evidencia, fundamento económico, transferibilidad, falsabilidad/claridad del protocolo, complementariedad conceptual con lo ya en pipeline), escala 0–5 con anclas verbales, pesos declarados; la RESILIENCIA adversarial NO se puntúa: es COMPUERTA (no criterio ponderado) — ver F0 §3(c);`

Ningún otro texto del ORQUESTADOR ni de F0 se modifica.

## 4. Justificación

El diseño de F0 §3(c) es **más estricto y más correcto** que la lista original del ORQUESTADOR: una amenaza de robustez potencialmente fatal no debe poder compensarse con un puntaje alto en otros criterios (que es lo que permitiría tratarla como criterio ponderado). Convertirla en compuerta —pasa/no pasa, con la amenaza incorporada al protocolo o el protocolo no avanza— es la decisión rigurosa. Por eso se reconcilia **hacia F0** en lugar de revertir F0: revertir debilitaría la compuerta. El criterio "falsabilidad/claridad" es un añadido coherente con el objetivo del Banco (protocolos pre-registrables y falsables) y ya está anclado con anclas verbales 0/3/5 en F0 §3.

**Alternativa considerada y no elegida:** revertir F0 para volver a puntuar "resiliencia" y quitar "falsabilidad/claridad". Se descarta porque degradaría el diseño (perdería la compuerta) y tocaría un artefacto de fase ya fechado.

## 5. Impacto esperado

- **C-001 se levanta** una vez ratificado este ADR **y** superado un re-arbitraje A-04 independiente.
- ORQUESTADOR y F0 quedan consistentes en la lista de criterios; la rúbrica operativa (la de F0) no cambia.
- **Condición de revisión futura (principio 15):** en el F0 del C-002, revisar si el conjunto de criterios puntuados + compuerta sigue siendo el adecuado con la evidencia de uso del C-001.

## 6. Compatibilidad hacia atrás

No hay resultados del Banco aún (F1 no ha corrido), así que la reconciliación **no altera ningún ranking ni puntuación previa**. Solo alinea la norma (ORQUESTADOR) con el artefacto ya fechado (F0). Sin impacto sobre H-001, H-002 ni registros externos.

## 7. Estado

**PROPUESTA pendiente de ratificación del IP.** Secuencia: ratificación → aplicación del cambio de texto en el ORQUESTADOR L73 → re-arbitraje A-04 (sesión independiente nueva). Ningún efecto antes de la ratificación.

---

> **Independencia de ADR-0008 y ADR-0009 (a pedido del IP):** son borradores separados, de propósito único, aceptables o rechazables por separado. Si uno se aprueba y el otro no, no queda un cambio a medias. El re-arbitraje A-04 solo puede dar CONFORME cuando **ambos** hallazgos bloqueantes (V-001 y C-001) estén resueltos; si solo se ratifica uno, F0 sigue sin cerrar por el otro.
