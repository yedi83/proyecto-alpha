# ENCARGO DE REDACCIÓN — ADR-0007 (Acto Fundacional)

> Emitido por el IP el 2026-07-18. Este documento es el *brief* para la sesión redactora — que debe ser una sesión NUEVA (Opus o superior), **no** el redactor del ADR-0006 (falló dos arbitrajes con tres sobre-declaraciones; preparó este brief pero no escribe el documento). El texto del ADR-0006 **no se reutiliza**: se escribe desde cero.

## Mandato del IP (estructura obligatoria, en sus términos)

**Parte I — Reconocimiento expreso.** El laboratorio incumplió su propio protocolo entre el 6 y el 17 de julio de 2026. Sin matices.

**Parte II — Declaración de nulidad.** Las notas interpretativas (exp-004 y exp-005, ambas del 2026-07-06) nunca tuvieron efectos normativos. Solo valor técnico (análisis conservable como contexto, jamás como decisión).

**Parte III — Nueva doctrina.** Crear el mecanismo constitucional para el caso doble: cuando se demuestra que un criterio pre-escrito estaba mal especificado **y** el procedimiento también fue vulnerado. Definir sus requisitos (demostración de mala especificación, canal ADR, arbitraje A-04, ratificación del IP **antes** de cualquier efecto).

**Parte IV — Cláusula única e irrepetible.** Esta excepción retroactiva solo puede usarse porque ocurrió antes de existir la doctrina — es el acto que la funda. Después de este caso, **la retroactividad no puede volver a existir. Nunca.** (Razón del IP: sin esta cláusula, cada experimento fallido tentará el "el criterio estaba mal diseñado" y el laboratorio morirá lentamente; con ella, el precedente queda cerrado, no abierto.)

## Requisitos técnicos heredados de los dos dictámenes A-04 (obligatorios, verificables)

1. **Inventario completo de actos** del 2026-07-06 → 07-17 realizados bajo el override informal (V-003 del primer dictamen): qué se decidió, corrió, registró y declaró en ese período, con fechas.
2. **Enumeración cerrada de los "experimentos pendientes"** a los que aplica la cláusula del segundo disparo letal (V-006) — lista explícita, no fórmula abierta.
3. **Cada contradicción de los dictámenes elevada y resuelta una a una** (C-002, C-003, C-004 del primer dictamen; C-005 y C-006 del segundo — leerlos en los archivos DICTAMEN). En particular C-005: el texto constitucional de la Parte III debe incluir la transitoria de la Parte IV de forma que el propio ADR-0007 sea admisible bajo su propia regla.
4. **Adjudicación del caso de fondo bajo la nueva doctrina** (como caso fundacional): el disparo letal de exp-004, el argumento de mala especificación (patrón monótono vs. pico; 512 elegido a ciegas; 640 superior), y el veredicto que corresponda a H-001 con sus condiciones (estatus CUESTIONADA, condiciones falsables, cláusula del segundo disparo con la lista del punto 2).
5. **CERO declaraciones de completitud propia** ("remediación completa", "punto por punto", etc.) — la conformidad la declara únicamente A-04. Lección de las 3 sobre-declaraciones del redactor anterior, que constan en el expediente.
6. Formato: plantilla ADR de 5 preguntas (`ADR-0000-plantilla.md`), estado inicial "Propuesta", secuencia explícita: dictamen A-04 CONFORME → ratificación del IP → solo entonces: enmienda a CONSTITUCION.md + actualización de registros (ficha/REGISTRO/ESTADO) + efectos.

## Fundamento de la decisión (conservar en el ADR, textual del IP)

*"Mi decisión no depende demasiado de H-001. Depende del laboratorio. Porque incluso si H-001 termina muriendo dentro de dos meses, el laboratorio habrá salido fortalecido. Y si sobrevive, también."*

## Insumos de lectura obligatoria para la sesión redactora

`docs/ADR/ADR-0006_EXPEDIENTE_DELIBERACION.md` (la historia completa) · `docs/ADR/ADR-0006-override-veredicto-exp004.md` (el intento fallido — SOLO como registro de qué no hacer; su texto no se reutiliza) · `docs/ADR/ADR-0006_DICTAMEN_A04.md` y `_v2.md` (las violaciones/contradicciones exactas) · `experiments/exp-004/` y `exp-005/` completos (PREREG, RESULTADO, NOTA) · `docs/CONSTITUCION.md` · `docs/INVESTIGACION/PROTOCOLO.md` · ficha `H-001-canal-donchian.md` · `REGISTRO_HIPOTESIS.md`.

## Salida esperada

`docs/ADR/ADR-0007-acto-fundacional-doctrina-de-excepcion.md` (estado: Propuesta) + tanda de git. Después, en OTRA sesión: arbitraje A-04.
