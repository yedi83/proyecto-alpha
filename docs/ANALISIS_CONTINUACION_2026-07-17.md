# Análisis de Continuación — 2026-07-17

> Sesión Fable 5, a petición del IP: análisis profundo del estado y las dos mejores propuestas de continuación.

## Situación (día 1 del nuevo reloj de Fase B)

**Operación:** Fase B re-cortada el 07-16 tras el incidente de contaminación (causa raíz verificada: keys compartidas ensayo/oficial → dos bots en una cuenta; datos 07-14→16 anulados; remediación con lanzador blindado y guardián anti-doble-instancia). Reloj: 1 mes desde el nuevo corte → cierre elegible ~**2026-08-16**. Primeros trades del nuevo período limpios (fees ✓, fills ✓). Fase A intacta (6/6). paper_real corriendo. **La Fase B, bien instrumentada, ya casi no consume atención: es esperar y auditar.**

**Investigación:** H-002 (ruptura BNB D1, long-only) formalizada con hipótesis económica y ficha — **en ~1 jornada**, primera medición (n=1) de la prueba de fuego del proyecto. Sin fase operativa; espera decisión. C-001 del Banco: F0 congelada, dictamen A-04 pendiente.

**Fase C:** PREREG en borrador con las decisiones del IP tomadas (capital $750, suspensión a −27%, disyuntor técnico, stop por vela). SECURITY §11 deja UNA decisión abierta: ¿implementar reconciliación continua + disyuntor (§9/§10) antes de C, o diferirlos a C-002?

## El análisis en una frase

Las próximas ~4 semanas son un regalo: la Fase B corre sola, y la pregunta es en qué invertir ese mes. Hay dos inversiones defendibles, y se distinguen por qué riesgo atacan primero: **el riesgo operacional** (el incidente demostró que es real) o **el riesgo epistemológico** (la incógnita nº 1 de H-001 sigue abierta y decide si la Fase C merece existir).

---

## PROPUESTA 1 — "Conocimiento que decide la Fase C" (recomendada)

**Tesis:** no se pone dinero real sin cerrar la mayor incógnita declarada del proyecto: **el funding real**. Tu propio veredicto lo dice — "con funding alto, 2024-26 queda ≈ 0". La Fase B mide funding por trade en demo, pero la pregunta histórica (¿el edge sobrevive al funding real de 5 años?) solo la responde un **mini Data Lake de funding histórico** + re-corrida del backtest de cesta.

**El mes, en orden:**
1. **Semana 1:** recolector de funding histórico real por símbolo (fuentes alternativas a Binance, que solo expone el último tramo) + OI si es barato. Auditoría A-02 del dataset.
2. **Semana 2:** exp-004 (pre-registrado): re-correr la cesta 2021-26 con funding REAL en vez del 0.01%/8h uniforme. Umbral pre-escrito de qué resultado pone en duda la Fase C. **Este experimento puede matar o confirmar la ida a capital real — por eso va antes que cualquier preparación de C.**
3. **Semanas 2-3:** dictamen A-04 sobre F0 → apertura formal C-001 → H-002 por el pipeline de investigación (datos D1 BNB, backtest con costes, OOS/lockbox pre-registrados). Todo offline, sin tocar operación. Métrica: costo total de H-002 vs H-001 (latencia del conocimiento).
4. **Semana 4:** papeleo de C listo-para-sellar (cuenta real configurada según SECURITY §1-2, PREREG_C actualizado con el resultado de exp-004) — sellar solo si B aprueba Y exp-004 no mató la ida.

**Qué compra:** la decisión de Fase C se toma sabiendo lo que hoy no sabes; una segunda hipótesis con veredicto de investigación; el C-001 en marcha; la tesis del proyecto medida por segunda vez.
**Qué pospone:** los controles §9/§10 van a C-002 (como SECURITY §11 ya contempla), mitigados por guardián + vigilancia + capital mínimo.

## PROPUESTA 2 — "Producción blindada primero"

**Tesis:** el incidente demostró que el mayor riesgo real del laboratorio es operacional, no estadístico — y con dinero real no hay re-cortes baratos. Antes de C, el bot debe tener los controles que SECURITY §9/§10 describen: **reconciliación continua** (no solo al arranque — la lección literal del incidente) y **disyuntor técnico** (rechazos consecutivos, mismatch persistente, gap de datos, techo de latencia/slippage con el p95 que la Fase B está midiendo).

**El mes, en orden:**
1. **Semanas 1-2:** `live_bot_faseC.py` staged: reconciliación por ciclo + disyuntor técnico + validaciones pre-orden de SECURITY §6. Revisión adversarial de código (como se hizo con el de frontera).
2. **Semana 3:** ensayo general de C en demo con cuenta separada (el patrón que ya funcionó — esta vez con keys distintas de verdad, lección aprendida).
3. **Semana 4:** cuenta real configurada (keys sin retiros + IP whitelist), PREREG_C sellado con umbrales del disyuntor confirmados con datos de B, día D de C preparado.

**Qué compra:** una Fase C que arranca con los controles implementados y validados, no diferidos ni prometidos.
**Qué pospone:** exp-004/funding, H-002 y C-001 → el riesgo es llegar al cierre de B con la incógnita nº 1 aún abierta y decidir C "porque toca", que es exactamente la inercia que el proyecto existe para impedir.

---

## Recomendación del mentor

**Propuesta 1**, por una asimetría simple: la 2 produce seguridad para una Fase C *cuya justificación aún no está completa*; la 1 produce la información que decide si esa Fase C merece existir. Si exp-004 mata la magnitud del edge, la 2 habría sido un mes blindando una puerta que no había que cruzar. Y la 1 no es imprudente: C solo arranca si B aprueba, con $750, guardián activo y la cláusula de suspensión a −27% ya decidida — mientras que §9/§10 quedan honestamente diferidos a C-002, que es lo que SECURITY §11 ya contemplaba como opción.

Punto de higiene independiente de la elección: el DIARIO_FASE_B necesita sus filas del 15-17 (el acta del re-corte existe; el diario debe reflejarlo).
