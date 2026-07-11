# Banco de Mecanismos — Orquestador (v3)

> **Cambio de lenguaje (2026-07-10):** este banco cataloga MECANISMOS; las estrategias son solo sus implementaciones. "Donchian 55" no es un objeto de estudio: es la implementación N de la hipótesis de persistencia. El árbol de F2 es el corazón del banco, no una fase más.

> Pipeline de investigación bibliográfica que produce **protocolos experimentales pre-registrables** para el laboratorio. v1: 2026-07-10 (cirugía del borrador original). v2: 2026-07-10, incorporando las correcciones del investigador: deduplicación por familias, auditoría (no cálculo) de robustez, transferibilidad como fase propia, diseño experimental completo como producto, mapa de complementariedad sin pesos.

## Principio rector

**El banco no termina donde empieza el pipeline: el banco entrega el diseño experimental del pipeline.** Su producto es un protocolo de validación completamente especificado — hipótesis, variables, datos, criterios de éxito/rechazo, pruebas a ejecutar, amenazas a la validez — de modo que el laboratorio no decide cómo validar: ejecuta un protocolo previamente registrado. Como el banco diseña ANTES de ver nuestros datos, el pre-registro es genuinamente ciego.

Lo que el banco JAMÁS produce: números calculados por LLM (robustez, retornos, pesos), veredictos de validación, o estrategias "aprobadas". Audita literatura y diseña experimentos; el motor PIC ejecuta y decide.

## Reglas duras (todas las fases)

1. **Ninguna afirmación cuantitativa sin fuente verificable** (búsqueda web; autor/año/venue comprobables). Lo no verificable se etiqueta `[memoria del modelo — verificar]`.
2. **Auditar, no calcular.** "El paper X reporta bootstrap con p=0.03 y estas limitaciones" ✓ · "Mi estimación del Sharpe es..." ✗.
3. Alcance: familias ejecutables con datos actuales/próximos del laboratorio (perpetuos cripto 15m–1d, funding, OI próximo). El resto, a anexo sin profundizar.
4. Cada fase → un documento fechado en `fases/`; la N+1 consume la N; el humano (Director de Investigación) aprueba cada cierre, **con dictamen previo de A-04 (Árbitro de Metodología): ¿la fase siguió el protocolo de F0?** Un NO APTO de A-04 bloquea el cierre.
5. Rúbricas y escalas se fijan en F0 y no cambian sin enmienda fechada.
6. Los umbrales de éxito/rechazo que proponga el banco son **propuestas**: el humano los ratifica (o ajusta, con justificación fechada) en el pre-registro formal. El investigador principal es humano.
7. Presupuesto: trabajo paralelo, regla del ≤30% mientras haya validación operativa abierta.
8. **Regla de Inmutabilidad del Ciclo:** con el dictamen CONFORME de A-04 sobre F0, ningún criterio, peso, compuerta o definición metodológica se modifica durante ese ciclo. Si aparece un problema: se registra como **ADR pendiente → se incorpora en el F0 del ciclo siguiente** — nunca "v1.3 a mitad de ciclo", porque destruye la comparabilidad entre protocolos del mismo ciclo. Única excepción: defecto FATAL que invalide el ciclo → el ciclo se ABORTA (con acta) y se reinicia bajo protocolo nuevo. Continuar registrando, o abortar; jamás parchear.
9. **Artefactos estructurados, no solo narrativos (añadido 2026-07-10):** desde F1, cada fase produce su registro en formato estructurado (JSONL: un objeto por entrada) **más** una vista Markdown generada a partir de él — nunca al revés. Esquema del registro de F1: `{id, mecanismo, familia, variante, nombre, mecanismo_economico_1frase, mercados_documentados, fuente:{autores, año, venue, verificada:bool}, nivel_evidencia_preliminar, reproducibilidad, observaciones}`. Las fases posteriores AÑADEN campos al mismo registro (F3: nivel_evidencia_final, robustez_reportada[]; F4: fundamento, falsacion[]; F5: transferibilidad; F7: puntuaciones) — un solo objeto por edge, enriquecido fase a fase. Razón: con cientos de registros, "todas las hipótesis nivel II sobre carry" debe ser un filtro, no una lectura.
10. **Compuertas objetivas entre fases:** el paso de fase depende de artefactos verificables — dictamen A-04 archivado (`FN_DICTAMEN_A04.md`) + artefacto estructurado completo + aprobación del IP — nunca de juicios informales. El ejecutor de cada fase (Sonnet) ejecuta exactamente lo definido en F0: no evalúa, no concluye, no prioriza, no descarta fuera de sus criterios.
11. **Ciclos identificados y trazables:** cada ciclo del banco lleva ID (`C-001`, `C-002`, …). Todo protocolo candidato cita su ciclo de origen, y el REGISTRO_HIPOTESIS anota el ciclo del que proviene cada H-XXX — dentro de un año debe poder decirse "todo lo producido entre H-021 y H-034 pertenece al C-001".

## Apertura de ciclo — punto de control administrativo (2 minutos, obligatorio antes de F1)

```
□ F0 congelada (documento fechado en fases/)
□ ADRs del ciclo anterior incorporados o declarados pendientes
□ Constitución y ORQUESTADOR consistentes con F0 (sin contradicciones conocidas)
□ Dictamen A-04 sobre F0 = CONFORME (sesión separada, archivado en fases/)
□ Versión del Banco etiquetada (git tag banco-CNNN-abierto)
□ Acta de una línea: "Ciclo C-NNN abierto el AAAA-MM-DD bajo F0 vN"
```

## Flujo

```
F0 Protocolo → F1 Mapeo PRISMA → F2 Consolidación de familias (dedup)
      → F3 Evidencia + auditoría de robustez → F4 Fundamento económico
      → F5 Transferibilidad → F6 Diseño experimental (hipótesis falsables
        + amenazas a la validez) → F7 Priorización + mapa de complementariedad
                                        │
                                        ▼
              PROTOCOLOS CANDIDATOS → REGISTRO_HIPOTESIS (EN COLA)
                                        │
                     humano ratifica → pre-registro formal H-XXX
                                        ▼
        Pipeline PIC: backtest → OOS/WF → lockbox → Fase A → B → C
```

**El banco termina antes del primer backtest.**

## Fases

| # | Fase | Modelo | Producto (`fases/`) |
|---|---|---|---|
| F0 | Protocolo del banco | Opus + humano | `F0_PROTOCOLO.md`: preguntas, familias en alcance, rúbrica (criterios/escalas 0-5 con anclas/pesos), fuentes aceptadas, formato del protocolo candidato |
| F1 | Mapeo sistemático (PRISMA adaptado) | Sonnet + web | `F1_CATALOGO.md`: catálogo crudo con fuentes verificadas + flujo PRISMA |
| F2 | Árbol genealógico por mecanismos | Opus | `F2_ARBOL.md`: mecanismo → familia → variante, con herencia de evidencia |
| F3 | Evidencia + auditoría de robustez | Opus | `F3_EVIDENCIA.md`: matriz de calidad + qué pruebas REPORTA la literatura, cómo, resultados y limitaciones |
| F4 | Fundamento económico | Opus | `F4_ECONOMIA.md`: mecanismo, contraparte, límites al arbitraje, regímenes a priori |
| F5 | Transferibilidad | Opus | `F5_TRANSFERENCIA.md`: cadena mecanismo→ingredientes→¿viaja a perpetuos cripto? + datos/infra requerida |
| F6 | Diseño experimental | Opus (2 sesiones: diseño y adversarial separadas) | `F6_PROTOCOLOS.md`: protocolo de validación completo por candidata |
| F7 | Priorización + complementariedad | Opus | `F7_COLA.md`: scoring transparente + sensibilidad + mapa conceptual + top-N a REGISTRO |

## Prompts

### F0 — Protocolo (Opus + humano, sesión conjunta)

> Actúa como metodólogo de investigación cuantitativa. Definimos el protocolo del banco ANTES de recopilar nada: (1) preguntas de investigación; (2) familias en alcance (ejecutables con velas 15m–1d de perpetuos cripto + funding; OI próximo) y las excluidas; (3) rúbrica: criterios (calidad de evidencia, fundamento económico, transferibilidad, resiliencia, complementariedad conceptual con lo ya en pipeline), escala 0–5 con anclas verbales, pesos declarados; (4) **jerarquía de niveles de evidencia** (adaptada de medicina a finanzas cuantitativas): Nivel I replicación independiente multi-mercado/multi-década · II varios papers independientes revisados por pares · III un paper sólido · IV working papers/backtests públicos reproducibles · V libros de practicantes reconocidos · VI blogs/foros técnicos · VII opinión sin evidencia. **Regla: la evidencia no se promedia entre niveles** — cualquier cantidad de nivel VI no suma un nivel III; cada edge se etiqueta con el nivel MÁXIMO que alcanza y el volumen dentro de ese nivel; (5) formato exacto del PROTOCOLO CANDIDATO (ver F6). Nada cambia después sin enmienda fechada. No recopiles estrategias todavía.

### F1 — Mapeo (Sonnet + búsqueda web)

> **Ejecuta F1 exactamente como fue definida en F0 (adjunto). No evalúes. No concluyas. No priorices. No compares. No descartes fuera de los criterios de exclusión de F0. Solo construye la revisión sistemática.**
>
> Actúa como investigador académico en finanzas cuantitativas. Construye el mapeo sistemático estilo PRISMA de las familias en alcance de F0 §2. Usa búsqueda web y VERIFICA cada fuente (autor, año, venue). Lo no verificable: `verificada:false` + nota `[memoria del modelo — verificar]`. Reporta el flujo PRISMA (identificadas→cribadas→incluidas, con exclusiones según F0).
>
> **Formato de salida obligatorio (regla 9 del orquestador):** artefacto estructurado `fases/F1_catalogo.jsonl` — un objeto JSON por línea con el esquema exacto de la regla 9 — y después una vista `F1_CATALOGO.md` generada desde el JSONL (tabla resumen + flujo PRISMA). El JSONL es la fuente de verdad; el Markdown, la vista.

### F2 — Árbol genealógico por mecanismos (Opus)

> Recibe F0-F1. Muchas entradas del catálogo son la misma idea con distinto nombre (Donchian/Turtle/Channel Breakout comparten edge; RSI-reversal/Bollinger-reversion/Z-score comparten edge). Tu trabajo es construir el **ÁRBOL GENEALÓGICO enraizado en MECANISMOS**, con tres niveles:
>
> ```
> MECANISMO (la ineficiencia)     → persistencia · sobre-reacción · prima de riesgo/carry · liquidez · microestructura · convexidad
>   └── FAMILIA (la forma de explotarla) → p.ej. persistencia → trend following, momentum TS, momentum XS
>         └── VARIANTE (la implementación)  → p.ej. trend following → Donchian, Turtle, MA cross, ATR breakout
> ```
>
> Reglas: (1) la pregunta de agrupamiento es ¿explotan la misma ineficiencia?, no ¿se parecen los indicadores?; (2) **la evidencia se hereda hacia arriba**: los papers de las variantes se acumulan al nodo de familia/mecanismo — así 5 papers de Donchian + 4 de Turtle + 3 de breakout cuentan como evidencia de UN edge, no de tres; la evidencia específica de una variante se anota en su nodo; (3) los casos dudosos se declaran dudosos con las dos ubicaciones posibles, sin forzar; (4) la asignación de mecanismo aquí es PROVISIONAL — F4 la confirma o corrige con el análisis económico. Producto: el árbol completo + tabla de herencia de evidencia. Este árbol ES el catálogo del banco de ahora en adelante: una estrategia deja de ser "Donchian 55" y pasa a ser "implementación N de la hipótesis de persistencia". Sin esto, el ranking posterior premia popularidad editorial, no calidad.

### F3 — Evidencia + auditoría de robustez (Opus)

> Recibe F0-F2. Para cada edge canónico, DOS trabajos, ninguno implica calcular nada: (A) calidad de la evidencia con la escala de F0 — nº de estudios independientes, riesgo de overfitting/data-snooping/publication-bias/survivorship (reportado vs. inferible, distinguido), contradicciones, reproducibilidad; (B) **auditoría de robustez reportada**: ¿la literatura reporta OOS / walk-forward / bootstrap / Monte Carlo / pruebas entre mercados? ¿Cómo se hicieron? ¿Qué resultados y qué limitaciones declaran (o callan)? Si no se reporta, escribe "no reportado" — eso también es un dato. Prohibido: inventar métricas, evaluar rentabilidad, rankear.

### F4 — Fundamento económico + falsabilidad (Opus)

> Recibe F0-F3. Solo para edges con evidencia suficiente según F3: (1) mecanismo causal de la ineficiencia — confirma o corrige la asignación provisional del árbol de F2; (2) quién pierde al otro lado y por qué persiste; (3) por qué no está arbitrada (límites al arbitraje: conductuales, institucionales, capacidad, riesgo); (4) regímenes donde debería ganar y perder, a priori y falsables; (5) **FALSABILIDAD ECONÓMICA (obligatoria, estilo Popper): ¿qué tendría que ocurrir en el mundo para que esta teoría dejara de ser cierta?** — p.ej. para underreaction: información instantánea generalizada, institucionalización del flujo, costes que superen el drift, competencia que agote la prima. Una teoría que no puede especificar sus condiciones de muerte no es una teoría: es una narrativa, y se descarta o degrada. Estas condiciones alimentan directamente las "señales de retiro conceptual" del protocolo de F6. Descarta lo que solo se sostiene en backtests. Clasifica con la escala de F0. Referencia de calidad: `research/H-001-canal-donchian/HIPOTESIS_ECONOMICA.md` (§5 es el ejemplo de condiciones de falsación).

### F5 — Transferibilidad (Opus)

> Recibe F0-F4. Para cada superviviente, recorre la cadena explícitamente y por escrito: mecanismo (de F4) → ¿qué ingredientes estructurales requiere? (p.ej. retraso informacional, flujo minorista, apalancamiento forzado, carry cobrable) → ¿existen esos ingredientes en perpetuos cripto? (con evidencia, no por asumido) → ¿los costes reales (taker ~0.06%/lado, funding) y la liquidez de la cesta lo dejan vivo? → VEREDICTO: viaja / viaja con condiciones / no viaja. Añade: datos e infraestructura que exigiría testearlo aquí (¿basta OHLCV+funding? ¿OI? ¿order book?) y esfuerzo de implementación en el backtester existente (bajo/medio/alto, justificado).

### F6 — Diseño experimental (Opus, DOS sesiones separadas)

> **Sesión 6a (diseñador):** Recibe F0-F5. Para cada candidata que viaja, redacta el PROTOCOLO DE VALIDACIÓN completo: (1) hipótesis principal en forma falsable ("si existe [condición estructural], entonces [señal] debería generar [efecto medible] en [universo]") + hipótesis secundarias; (2) variables independientes y dependientes; (3) datos mínimos (universo, período, frecuencia, campos); (4) espacio de parámetros ACOTADO con justificación económica de cada rango — no "probemos de 10 a 1000"; (5) criterios de éxito y de rechazo PROPUESTOS, numéricos, con su lógica; (6) secuencia de pruebas que el motor PIC deberá ejecutar (backtest → particiones → OOS/WF → lockbox) según PROTOCOLO.md del laboratorio; (7) condiciones de retiro conceptual.
>
> **Sesión 6b (adversarial, sesión NUEVA sin el contexto de 6a):** Recibe los protocolos de 6a + F0-F5. Actúa como revisor hostil de un comité científico: para cada protocolo, lista las AMENAZAS A LA VALIDEZ — qué régimen lo mata, crowding/saturación, sensibilidad a costes, fugas probables del diseño (lookahead, survivorship del universo propuesto), formas en que podría "parecer que funciona" sin funcionar, y qué le falta al protocolo para detectarlo. Cada amenaza debe entrar al protocolo como prueba o limitación declarada. El diseñador no se revisa a sí mismo.

### F7 — Priorización + complementariedad (Opus)

> Recibe F0-F6. (1) Aplica la rúbrica de F0 (weighted scoring, pesos declarados, una línea de justificación por celda); sensibilidad: varía cada peso ±20% y reporta qué posiciones cambian — si el top-3 es inestable, dilo. (2) **Mapa conceptual de complementariedad, SIN pesos:** clasifica qué captura cada edge (tendencia / carry / reversión / convexidad / flujo) y su relación con lo ya en pipeline (H-001 = tendencia): redundante / complementario / cobertura. Es clasificación, no requiere datos. (3) Selecciona top-N (N lo fija el humano) y entrega sus protocolos candidatos con estado CANDIDATA EN COLA. Nada de esto constituye validación; los umbrales son propuestas hasta ratificación humana.

## Arranque

Sesión F0 (Opus + humano). No se abre F1 sin F0 cerrada. Cadencia: una fase por sesión (F6 son dos), dentro del presupuesto del 30%.
