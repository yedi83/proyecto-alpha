# ADR-0004 — Moratoria de diseño hasta el cierre del C-001

- **Fecha:** 2026-07-10
- **Estado:** Aceptada
- **Alcance:** Proceso / Gobernanza

## 1. ¿Qué problema intentábamos resolver?

La arquitectura está completa y el laboratorio entra en operación. El riesgo dominante ya no es el mal diseño: es la iteración continua sobre un experimento en ejecución. El C-001 tiene DOS objetos de estudio — los mecanismos de mercado y el propio laboratorio — y ningún experimento produce buena evidencia si se modifica mientras corre.

## 2. ¿Qué alternativas se evaluaron?

(a) Seguir mejorando cuando surjan buenas ideas — cada mejora parece barata; la suma destruye la comparabilidad y convierte al laboratorio en objeto inobservable. (b) Moratoria absoluta sin excepciones — ignora defectos fatales. (c) **Moratoria con las excepciones ya definidas** (defecto fatal → aborto con acta; violación metodológica → corrección crítica documentada, según Inmutabilidad del Ciclo y PREREG).

## 3. ¿Por qué se eligió esta?

Toda idea nueva, todo entusiasmo, toda mejora evidente durante el C-001 sigue una sola ruta: **ADR pendiente → consideración para el C-002.** La pregunta de cada revisión deja de ser "¿cómo mejoramos el laboratorio?" y pasa a ser **"¿qué evidencia produjo el laboratorio sobre sí mismo?"** (instrumentación de F0 §8). Sin excepciones por calidad de la idea: la moratoria protege del entusiasmo igual que la regla 9 protege del exceso de confianza.

## 4. ¿Qué consecuencias aceptamos?

Ideas valiosas esperarán semanas o meses. Se acumulará una cola de ADR pendientes (es el diseño funcionando, no fallando). El criterio de éxito del ciclo queda desacoplado del alfa: **el C-001 es exitoso si el laboratorio produce decisiones metodológicas respaldadas por evidencia, incluso cuando esa evidencia contradiga expectativas previas** — independientemente del resultado de las estrategias.

## 5. ¿Qué evidencia futura podría justificar revisarla?

El cierre del C-001: su registro de instrumentación dirá si la moratoria fue protección o rigidez (¿cuántos ADR pendientes resultaron urgentes de verdad?). La revisión ocurre en el F0 del C-002, no antes.
