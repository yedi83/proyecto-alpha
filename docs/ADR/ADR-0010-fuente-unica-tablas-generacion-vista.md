# ADR-0010 — Fuente única de verdad en fases con tablas: la vista se genera desde el JSONL y se audita celda-a-celda antes del A-04

- **Fecha:** 2026-07-25
- **Estado:** **PENDIENTE** — hallazgo metodológico del C-001; para consideración en el **F0 del C-002** (vía moratoria ADR-0004). No tiene efecto retroactivo sobre el C-001 ya cerrado.
- **Alcance:** Proceso / Gobernanza (regla dura 9, ejecución de fases del Banco)
- **Origen:** Instrumentación del C-001 (F0 §8) — evidencia que el laboratorio produjo sobre sí mismo durante F7.

## 1. ¿Qué problema intentábamos resolver?

La regla dura 9 exige que el JSONL sea la fuente de verdad y que el Markdown sea "una vista generada a partir de él — nunca al revés". En F7 esa regla se violó **dos veces seguidas por el mismo modo de fallo**: el ejecutor redactó primero la prosa editorial de la vista (celdas de justificación del §1, frase de complementariedad del §3) y solo después intentó reconstruirla en el JSONL. El A-04 independiente lo cazó en v1 (justificación de F1-013/F1-020 solo en la vista) y otra vez en v2 (frase del §3 ausente de la fuente). Recién en v3, tras **generar las tablas por script desde el JSONL y auditar celda-a-celda antes de arbitrar**, el dictamen salió CONFORME.

El hallazgo: la regla 9 no basta como principio declarado; el **orden de trabajo** ("prosa primero, fuente después") reintroduce la violación de forma recurrente aunque el ejecutor conozca la regla.

## 2. ¿Qué alternativas se evaluaron?

(a) Confiar en la disciplina del ejecutor (statu quo) — demostrado insuficiente: el mismo error reapareció en otra ubicación del mismo documento. (b) Dejar que el A-04 lo cace siempre — funciona, pero gasta dos ciclos de arbitraje independiente por fase con tablas (coste real de presupuesto y tiempo). (c) **Hacer obligatorio el flujo fuente→vista con auditoría automática previa al A-04** — mueve el control aguas arriba, al momento de construir, en vez de aguas abajo, al arbitraje.

## 3. ¿Por qué se propone esta?

En fases con tablas (F3, F4, F7 y cualquiera con celdas de scoring/clasificación), se propone como procedimiento obligatorio: **(1)** todo contenido de celda vive en un campo del JSONL; **(2)** la vista Markdown se **genera con script** desde el JSONL, sin texto tecleado a mano en las tablas; **(3)** una **auditoría celda-a-celda automática** (cada celda de tabla debe existir verbatim en un campo de la fuente) corre **antes** de convocar al A-04. Nunca redactar primero la prosa editorial de la vista y después intentar reconstruirla en la fuente.

Esto convierte la regla 9 de un principio que se verifica al final en una **propiedad garantizada por construcción**. El A-04 sigue siendo el control independiente, pero deja de gastarse en cazar un error prevenible.

## 4. ¿Qué consecuencias aceptamos?

La prosa narrativa (secciones de síntesis, conclusiones) sigue siendo interpretación legítima de la vista y NO se exige que esté literal en el JSONL; el requisito de trazabilidad aplica a **celdas de tabla y justificaciones de scoring**. Se acepta el coste de escribir un pequeño generador/auditor por fase con tablas, a cambio de eliminar una clase entera de NO CONFORME.

## 5. ¿Qué evidencia futura podría justificar revisarla o rechazarla?

El F0 del C-002 evaluará si el procedimiento previene el fallo sin introducir rigidez excesiva. Si en el C-002 las fases con tablas pasan el A-04 a la primera de forma consistente, el hallazgo se consolida como regla; si el generador automático resulta más costoso que el beneficio, se revisa.

> **Nota de retroactividad:** este ADR NO altera nada del C-001. F7 cerró CONFORME (v3) por el canal correcto (corrección + re-arbitraje independiente + aprobación del IP). Este registro es prospectivo: entra en vigor solo si el F0 del C-002 lo ratifica.
