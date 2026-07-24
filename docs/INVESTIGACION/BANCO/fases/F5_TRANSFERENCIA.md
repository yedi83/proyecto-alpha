# F5 — Transferibilidad a perpetuos cripto — Ciclo C-001

> **Fecha: 2026-07-23 · Ejecutor: Opus (Claude) · Fase: F5 — Transferibilidad (ORQUESTADOR §F5)**
> **Fuente de verdad: `F5_transferencia.jsonl`** (30 objetos, cada uno hereda **verbatim** los campos de F4 + añade `transferibilidad{ingredientes_requeridos, ingredientes_en_cripto, costes_liquidez, veredicto, condiciones, datos_infra_requerida, esfuerzo_implementacion}`). Este documento es una **VISTA** de ese JSONL — no al revés (regla dura 9).
> **Nota de honestidad (ejecución directa):** por límite de presupuesto, F5 se ejecutó en la sesión principal (Opus) sin el subagente de búsqueda web. Las afirmaciones estructurales sobre el mercado cripto se apoyan en conocimiento establecido y en la evidencia **ya verificada por web en F1-F4**; lo genuinamente incierto va etiquetado `[memoria del modelo — verificar]`. El árbitro A-04 y el IP validan aparte.

## Alcance

Se evalúa la transferibilidad de los **supervivientes de F4** (10 `fundamento_solido` + 9 `degradado`). Los `descartado`/`no_procede` quedan `na` (fuera de alcance). Esto **NO es priorización ni scoring** (eso es F7); F5 solo juzga si el mecanismo *viaja* a perpetuos cripto y con qué datos/esfuerzo.

**Realidad de datos del laboratorio (de `DATA.md`):** OHLCV 15m ✅ · funding real 2021-26 ✅ · open interest ❌ (planeado, lo exige P3) · order book L2/L3 ❌.

---

## Resumen (edge → veredicto → datos → esfuerzo)

| Edge | Mecanismo | F4 | **F5 transferibilidad** | Datos | Esfuerzo |
|---|---|---|---|---|---|
| F1-001/002/003/004/006/007 | Persistencia | sólido | **VIAJA** | OHLCV+funding ✅ | bajo |
| F1-008 Carry (general) | Carry | sólido | **VIAJA** | funding+OHLCV ✅ | bajo-medio |
| F1-009 Crypto carry | Carry | sólido | **VIAJA** | funding+spot+OHLCV | bajo-medio |
| F1-013 Funding arb CEX/DEX | Carry | sólido | **VIAJA c/ condiciones** | funding CEX+DEX | alto |
| F1-020 ILLIQ (prima iliquidez) | → M2 | degradado | **VIAJA c/ condiciones** | OHLCV+volumen ✅ | medio |
| F1-014 Reversión 3-5 años | Sobre-reacción | sólido | **NO VIAJA** | — | — |
| F1-015/016 Reversión corto | Sobre-reacción | degradado | **NO VIAJA** | — | — |
| F1-017 Reversión 1 día | Sobre-reacción | degradado | **NO VIAJA** | — | — |
| F1-018 Momentum/reversión cripto | Sobre-reacción | degradado | **NO VIAJA** | — | — |
| F1-021/022/023/024 Order flow/VPIN | Microestructura | degradado | **NO VIAJA** | order book L2/L3 ❌ | — |
| F1-005/010/011/012/019/025/026-030 | teoría/método/descartado | — | n/a | — | — |

**Conteo:** 8 viaja · 2 viaja-con-condiciones · 9 no-viaja · 11 n/a.

---

## La cadena, por mecanismo

### M1 · Persistencia (tendencia) — **VIAJA**
- **Ingredientes:** retraso informacional/subreacción, herding, apalancamiento forzado (cascadas de liquidación).
- **¿En perp cripto?** Sí, amplificados — apalancamiento minorista alto → cascadas documentadas. **Evidencia directa: H-001 (Donchian) es una implementación de este mecanismo en perp cripto, ya en Fase B.**
- **Costes/liquidez:** baja frecuencia (holds de días) → taker ~0.06%/lado + funding tolerables; exp-008 mostró que el funding real no destruye el edge.
- **Veredicto: VIAJA.** Datos: OHLCV+funding (ya los tienes). Esfuerzo: **bajo** (motor de H-001).
- *Nota:* coincide con H-001 ya en pipeline → redundancia, observación para F7 (no descarte).

### M2 · Carry / funding — **VIAJA** (el más nativo del instrumento)
- **Ingredientes:** un carry cobrable.
- **¿En perp cripto?** Sí, de forma directa: **el funding ES el carry**, observable y cobrable cada 8h.
- **Costes/liquidez:** el funding es la señal; riesgo de cola (carry crashes / de-peg) señalado en F4.
- **Veredicto: VIAJA** (F1-008 general como mecanismo, F1-009 la implementación cripto). Datos: funding (ya recolectado 2021-26) + OHLCV; OI recomendable. Esfuerzo: **bajo-medio**.
- **F1-013 (arb funding CEX/DEX): VIAJA CON CONDICIONES** — requiere infraestructura DEX (gas, latencia, custodia) que hoy no existe. Esfuerzo alto.

### M3 · Sobre-reacción (reversión) — **NO VIAJA**
- **F1-014 (reversión 3-5 años):** el horizonte largo es incompatible con el perp (funding acumulado a años erosiona el edge), la muestra cripto es corta, y la base era equity. **NO VIAJA.**
- **F1-015/016 (reversión corto/lead-lag):** confounds (rebote bid-ask, lead-lag ≠ sobre-reacción); en majors líquidos se diluye. **NO VIAJA.**
- **F1-017 (reversión 1 día):** F3 verificó que **se invierte a MOMENTUM en el universo líquido** = tus perpetuos. Lo que queda es momentum, que ya es M1. **NO VIAJA.**
- **F1-018:** contradicción viva (varianza posiblemente infinita → prima quizá no realizable) + solapamiento con M1. **NO VIAJA.**

### M4 · Microestructura / liquidez — **NO VIAJA** (por datos)
- **Ingrediente-dato:** order book L2/L3 / datos a nivel de trade. **No existen en el laboratorio** (solo OHLCV+funding). F0 §2 ya lo anticipó. F1-021/022/023/024 → **NO VIAJA** (no testeable aquí hoy). Esfuerzo alto (infra de captura de order book).
- **Excepción — F1-020 ILLIQ (reasignado a prima de iliquidez, M2):** la medida de Amihud se computa con OHLCV+volumen, **sin** order book → **VIAJA CON CONDICIONES**: requiere un universo cripto amplio (no solo 6 majors) para ordenar por iliquidez; la señal es débil en pocos majors. `[memoria del modelo — verificar magnitud en cripto]`. Esfuerzo medio.

---

## Lectura honesta del embudo (F5, no priorización)

De los 30 candidatos de la literatura, los que **viajan limpiamente a tu instrumento** son **persistencia** (que ya es H-001 — redundante) y **carry/funding** (el más nativo de los perpetuos y el más *distinto* de lo que ya operas). Reversión y microestructura **no viajan** a tu setup actual (horizonte incompatible / se invierte a momentum en líquidos / faltan datos de order book). ILLIQ y el arb de funding viajarían solo con condiciones de infraestructura o universo que hoy no tienes.

**Esto es transferibilidad, no selección.** Cuál merece convertirse en la próxima hipótesis —y cómo pesa la redundancia de persistencia con H-001— lo decide **F7**, no F5.

> **F5 EJECUTADA — no CERRADA.** Falta dictamen A-04 (sesión independiente) + aprobación del IP antes de abrir F6. El cierre no se autodeclara.
