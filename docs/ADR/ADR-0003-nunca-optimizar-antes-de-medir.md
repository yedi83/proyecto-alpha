# ADR-0003 — Nunca optimizar antes de medir

- **Fecha:** 2026-07-10
- **Estado:** Aceptada
- **Alcance:** Metodología / Proceso

## 1. ¿Qué problema intentábamos resolver?

Con la arquitectura completa (Constitución, Banco, agentes, pipeline), la siguiente amenaza es el entusiasmo de mejora: "podemos mejorar F3" antes de que F3 haya corrido una sola vez. Las mejoras sin evidencia son la forma respetable de la deriva metodológica, y contradicen todo lo que el laboratorio exige a sus hipótesis.

## 2. ¿Qué alternativas se evaluaron?

(a) Mejorar componentes cuando parezca razonable (statu quo implícito) — barato, pero convierte la arquitectura en blanco móvil y hace incomparables los ciclos. (b) Congelar todo indefinidamente — mata el aprendizaje sobre el propio sistema. (c) **Regla: toda mejora requiere evidencia operativa del ciclo que la motiva, y se aplica en el ciclo siguiente.**

## 3. ¿Por qué se eligió esta?

Es la misma epistemología del laboratorio aplicada a sí mismo: los componentes son hipótesis de diseño (principio 16) y las hipótesis se juzgan por evidencia, no por intuición. La pregunta obligatoria ante cualquier propuesta de mejora es: **¿qué evidencia del ciclo en curso muestra que esto necesita mejorar?** Sin esa evidencia, la mejora espera al ciclo siguiente como ADR pendiente. La instrumentación que produce esa evidencia quedó definida en F0 §8 (latencias, bloqueos de compuertas, fricciones, esquema).

## 4. ¿Qué consecuencias aceptamos?

Mejoras obvias esperarán un ciclo entero (coste asumido: la comparabilidad vale más que la velocidad de mejora). El registro de instrumentación añade una carga pequeña por fase. Riesgo residual: registrar fricciones puede volverse ritual vacío — lo vigila la Auditoría de Simplicidad.

## 5. ¿Qué evidencia futura podría justificar revisarla?

Si al cierre de dos ciclos la evidencia muestra que los defectos detectados eran tan obvios al inicio que esperar costó más que la comparabilidad ganada (p. ej., un campo JSONL ausente que obligó a re-anotar todo el catálogo), se revisará hacia una categoría de "corrección trivial pre-aprobada" con definición estricta — vía ADR nuevo, no reinterpretando este.
