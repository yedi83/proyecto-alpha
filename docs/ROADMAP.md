# Roadmap (12 meses)

> Orden justificado en la revisión inicial del proyecto. Fecha base: julio 2026.

## 1. Mes 1 — Escribir los criterios antes de seguir midiendo

- Completar `VALIDACION/CRITERIOS_FASES.md` con números (aprobación, reprobación, parada).
- Completar `RISK_POLICY.md` con límites cuantificados.
- Escribir el informe honesto de H-001 (`INVESTIGACION/hipotesis/H-001-canal-donchian.md`): cómo se eligieron los parámetros, cuántas variantes se probaron, qué datos se usaron.
- Migrar el código existente (backtester, bot, dashboard) a este repo con sus tests.

**Por qué primero:** todo lo que se mida sin criterios previos queda contaminado por sesgo de confirmación. Es escritura, no desarrollo: 2-3 semanas.

## 2. Meses 2–5 — Cerrar Fases A y B de H-001 contra los criterios escritos

- Sin excepciones ni "casi pasa". Si H-001 reprueba, es un éxito del proceso, no un fracaso del proyecto.

## 3. Meses 3–8 (paralelo, ≤30% del tiempo) — Data Lake con QA

- Recolección automatizada de datos Binance perp USDT.
- Incluir pares delistados (evitar survivorship bias).
- Auditoría de alineación temporal (velas, funding) sin lookahead.

**Por qué:** es el prerrequisito de toda investigación futura y no contamina la validación en curso.

## 4. Meses 6–10 — Segunda hipótesis, de familia distinta

- Candidata natural: carry/funding (datos ya disponibles del Data Lake).
- Debe seguir el protocolo completo de `INVESTIGACION/PROTOCOLO.md`.

**Por qué es la prueba de fuego:** si la plataforma es el activo, H-002 debe costar una fracción del tiempo que costó H-001. Si cuesta lo mismo, la tesis central del proyecto es falsa y hay que saberlo cuanto antes.

## 5. Meses 10–12 — Fase C (capital pequeño)

- Solo si la Fase B aprobó los criterios escritos.
- Asignación de capital básica si hay dos estrategias vivas.

## Explícitamente fuera de los próximos 12 meses

Meta-modelos, machine learning, clasificador de regímenes acoplado a ejecución, comercialización, otros mercados. El análisis de regímenes solo como investigación descriptiva sobre el Data Lake.
