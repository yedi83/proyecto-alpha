# F0 — Protocolo del Banco de Mecanismos — **Ciclo C-001**

> Sesión conjunta 2026-07-10: Investigador Principal (humano) + Fable 5. Cierre sujeto a dictamen de A-04 en sesión separada + checklist de apertura de ciclo (ORQUESTADOR).
>
> **Regla de Inmutabilidad del Ciclo:** con el CONFORME de A-04, este documento queda INMUTABLE durante todo el C-001. Los problemas que aparezcan se registran como ADR pendiente y se incorporan al F0 del C-002 — nunca se parchea a mitad de ciclo (destruiría la comparabilidad entre protocolos del ciclo). Única excepción: defecto fatal → aborto del ciclo con acta y reinicio bajo protocolo nuevo.

## 1. Preguntas de investigación del Ciclo 1

1. ¿Qué mecanismos de ineficiencia tienen fundamento económico y evidencia suficientes para merecer un protocolo experimental en perpetuos cripto?
2. ¿Qué implementación canónica de cada mecanismo es la candidata natural para nuestro pipeline?
3. ¿Qué datos/infraestructura exigiría cada una (prioridades del Data Lake)?
4. **Meta-pregunta del piloto:** ¿el método del Banco produce protocolos sólidos y priorizaciones consistentes? (El Ciclo 1 valida el Banco, no agota el universo.)

## 2. Alcance del Ciclo 1 — piloto por mecanismos fundamentales

| Mecanismo | Familia representativa | Nota |
|---|---|---|
| Persistencia | Trend following / TS momentum | H-001 ya en pipeline: el ciclo lo usa como referencia, no lo re-investiga |
| Prima de riesgo | Carry / funding | Candidata natural a H-002 (datos ya disponibles) |
| Sobre-reacción | Mean reversion | Complemento conceptual directo de persistencia |
| Microestructura | Order flow / liquidez | Probable NO-VIAJA por datos hoy — se incluye a propósito: testea la maquinaria de F5 y alimenta prioridades del Data Lake |
| Régimen | Detección de regímenes (HMM, etc.) | **Como FILTRO/condicionador, no como estrategia** — coherente con ROADMAP (régimen solo descriptivo en 12 meses) |

**Fuera del Ciclo 1** (sin analizar en profundidad; anexo si aparecen): momentum cross-sectional completo, estacionalidad, convexidad/opciones, on-chain, arbitrajes estadísticos multi-venue, market making activo.

## 3. Rúbrica de puntuación (ADR provisional v1.0)

**Marco de decisión (del IP, textual):** *la economía decide qué hipótesis merecen entrar al Banco; la evidencia tiene la última palabra sobre qué se convierte en conocimiento aceptado.*

| Criterio | Peso | Ancla 0 | Ancla 3 | Ancla 5 |
|---|---|---|---|---|
| Fundamento económico | **35%** | Solo existe en el backtest; sin mecanismo ni perdedor identificable | Mecanismo plausible con perdedor identificado, pero límites al arbitraje difusos | Mecanismo causal + contraparte + límites al arbitraje + condiciones de falsación, todo explícito |
| Calidad de la evidencia | **30%** | Nivel VI-VII únicamente | Nivel III (un paper sólido) o IV abundante y reproducible | Nivel I-II: replicación independiente multi-mercado/multi-década |
| Transferibilidad a perpetuos cripto | **20%** | Ingredientes estructurales ausentes o costes lo matan | Viaja con condiciones verificables; datos alcanzables | Ingredientes presentes con evidencia; sobrevive costes reales; datos ya disponibles |
| Falsabilidad / claridad del protocolo | **10%** | No se puede formular predicción falsable | Falsable pero con criterios de rechazo vagos | Hipótesis en forma "si-entonces" + umbrales de rechazo naturales + señales de retiro observables |
| Complementariedad con mecanismos en pipeline | **5%** | Redundante con lo ya en curso (persistencia) | Parcialmente solapado | Captura distinta (carry/reversión/convexidad vs. tendencia) |

Reglas de la rúbrica: (a) pesos **provisionales**, documentados como decisión metodológica v1.0; (b) **análisis de sensibilidad OBLIGATORIO** (±20% por peso) antes de usar cualquier ranking para priorizar — si el orden del top cambia, se reporta la inestabilidad y decide el IP; (c) la **resiliencia adversarial no se puntúa: es COMPUERTA** — las amenazas a la validez de F6b deben quedar incorporadas al protocolo (como prueba o limitación declarada) o el protocolo no pasa a F7, tenga la nota que tenga.

## 4. Niveles de evidencia (jerarquía; no se promedia entre niveles)

I replicación independiente multi-mercado/multi-década · II varios papers independientes revisados por pares · III un paper sólido · IV working papers / backtests públicos reproducibles · V libros de practicantes reconocidos · VI blogs/foros técnicos · VII opinión. Cada edge se etiqueta con el nivel MÁXIMO alcanzado + volumen dentro de ese nivel. Cualquier cantidad de nivel inferior no asciende de nivel.

## 5. Fuentes aceptadas

Journals revisados por pares (JF, JFE, RFS, Quantitative Finance, JPM) > SSRN/arXiv con verificación > libros de practicantes reconocidos > informes de gestoras/CTAs con datos > blogs técnicos con código reproducible. Todo con autor/año/venue verificados por búsqueda web; lo demás `[memoria del modelo — verificar]`.

## 6. Formato del PROTOCOLO CANDIDATO (salida de F6, entrada al REGISTRO)

Encabezado (mecanismo/familia/variante del árbol, nivel de evidencia, puntuación y sensibilidad) · Hipótesis principal falsable ("si [condición estructural], entonces [señal] genera [efecto] en [universo]") + secundarias · Variables independientes/dependientes · Datos mínimos (universo, período, frecuencia, campos, fuente) · Espacio de parámetros acotado con justificación económica por rango · Criterios de éxito y rechazo PROPUESTOS (numéricos, con lógica; ratifica el IP) · Secuencia de pruebas del pipeline PIC · Amenazas a la validez (de F6b) incorporadas · Condiciones de retiro conceptual · Esfuerzo de implementación estimado.

## 7. Salida del ciclo: 0 a 5 protocolos (máximo 5, SIN mínimo)

**Principio (del IP, textual):** *el Banco no existe para producir candidatos; existe para filtrar rigurosamente cuáles merecen convertirse en experimentos.* Un ciclo con cero candidatos no fracasó: evitó invertir en hipótesis bajo el estándar.

## 8. Cierre de fases

Cada fase cierra con: documento fechado en `fases/` + dictamen CONFORME de A-04 (sesión separada, prompt en `agents/A-04`) + aprobación del IP. Sin dictamen, no se abre la siguiente.
