# Acta de Apertura — Banco C-001

> **SELLADA 2026-07-19.** (Historia del día, por honestidad: este ciclo estuvo brevemente aparcado el 2026-07-19 tras un A-04 NO CONFORME sobre F0; se reabrió el mismo día tras ratificar el IP los ADR-0008 y ADR-0009, aplicarlos al ORQUESTADOR, y obtener un re-arbitraje A-04 CONFORME sobre la versión corregida.)

> Texto del Investigador Principal (2026-07-10). Firmado con fecha al completar la checklist de apertura (dictamen A-04 CONFORME + tag `banco-C001-abierto`).

El objetivo de este ciclo no es maximizar la cantidad de hipótesis aceptadas ni demostrar la eficacia del Banco. El objetivo es ejecutar íntegramente el proceso definido, generar evidencia sobre el funcionamiento del propio sistema y registrar cualquier desviación metodológica, limitación o aprendizaje. Toda modificación derivada de esta evidencia será considerada para el C-002 mediante el proceso formal de ADR. Durante el C-001, la arquitectura permanece congelada salvo las excepciones definidas por la Regla de Inmutabilidad del Ciclo.

**Criterio de éxito del ciclo:** el C-001 se declarará exitoso si el laboratorio fue capaz de producir decisiones metodológicas respaldadas por evidencia, incluso cuando esa evidencia contradijo expectativas previas — independientemente de cuántas hipótesis sobrevivan o cuánto alfa aparezca.

Rige la moratoria de diseño del ADR-0004: toda idea nueva durante el ciclo → ADR pendiente para el C-002.

## Checklist de apertura (ORQUESTADOR §Apertura de ciclo)

- [x] **F0 congelada** (documento fechado en `fases/`): F0_PROTOCOLO.md, 2026-07-10, SHA-256 `b99c3569…5557f4`, sin cambios (working tree == HEAD).
- [x] **ADRs incorporados o declarados pendientes:** C-001 es el primer ciclo (no hay "ciclo anterior"). ADR-0008 y ADR-0009 (ratificados 2026-07-19) incorporados al ORQUESTADOR. Moratoria ADR-0004 vigente: ideas nuevas → ADR pendiente para C-002.
- [x] **Constitución y ORQUESTADOR consistentes con F0:** verificado por el IP. F0 y las enmiendas (mandato de modelo, criterios de rúbrica) no tocan materia constitucional (el principio 17 rige anulación de veredictos, ortogonal a F0). Sin contradicciones conocidas.
- [x] **Dictamen A-04 sobre F0 = CONFORME** (sesión independiente, archivado): `F0_DICTAMEN_A04_v2.md`, 2026-07-19. Los hallazgos V-001 y C-001 quedaron resueltos mediante ADR-0008/0009 y la versión enmendada del ORQUESTADOR obtuvo este CONFORME; el dictamen v1 se conserva íntegro.
- [ ] **Versión del Banco etiquetada** (`git tag banco-C001-abierto`): **acto final del IP** (comando en el CHANGELOG / entregado por la sesión). Al ejecutarlo queda marcado este punto.
- [x] **Acta de una línea** (abajo).

## Acta de una línea

**Ciclo C-001 abierto el 2026-07-19 bajo F0 v1 (2026-07-10, SHA-256 `b99c3569…5557f4`).**

---

— Investigador Principal · Fecha de sellado: **2026-07-19** · F0: v1 (2026-07-10, `b99c3569…5557f4`) · Dictamen A-04: **CONFORME** (`F0_DICTAMEN_A04_v2.md`)

> Nota: abrir C-001 significa que la fase F0 cerró y el ciclo está formalmente abierto — **no** obliga a correr F1 ya. F1 (mapeo bibliográfico) se ejecuta cuando el IP quiera, como trabajo secundario (≤30%). El tag `banco-C001-abierto` es el último acto administrativo; hasta ejecutarlo, la apertura consta sellada documentalmente pero no versionada en git.
