# Plan de Trabajo — Análisis y Arranque por Etapas

> Cómo se arranca el proyecto de forma ordenada: primero teoría, luego migración, luego programación. Complementa a `ROADMAP.md` (el roadmap dice *qué* en 12 meses; este documento dice *cómo* empezar).

---

## 1. Análisis de la situación de partida

### Lo que hay

- Código funcional (backtester, bot, dashboard) fuera de este repo, sin estructura ni tests documentados.
- Una hipótesis (H-001, canal Donchian 512) con resultados históricos **no reproducibles todavía dentro del repo** y con cinco preguntas epistemológicas abiertas (ver su ficha).
- Una base documental completa pero con los números en PENDIENTE.

### El problema real a resolver

El proyecto no falla por falta de ideas ni de código: el riesgo es **perder información y autoengañarse**. Cada experimento no registrado es conocimiento perdido; cada criterio escrito después del resultado es sesgo. Por eso el arranque se ordena alrededor de dos invariantes:

1. **Nada se pierde:** todo experimento, hipótesis y decisión tiene un lugar fijo, un ID y una fecha. Las carpetas no se renombran ni se mueven según el resultado.
2. **La teoría precede al código:** los contratos (qué es una vela, qué es una señal, qué es un experimento) se diseñan en papel antes de programar, porque cambiarlos después cuesta 10x.

### Errores predecibles a evitar (los nombro porque los vas a sentir como tentaciones)

- Empezar a programar el Data Lake "porque es divertido" antes de llenar los criterios de Fase A. → Violación de la regla del 30% de la Constitución.
- Reorganizar carpetas cada mes buscando la estructura "perfecta". → La estructura de abajo es suficiente; se cambia solo por ADR.
- Guardar experimentos "buenos" y borrar los "malos". → El registro es append-only; un experimento borrado invalida la estadística de todos los demás.
- Migrar el código copiando todo de golpe sin tests. → Se migra componente por componente, cada uno entra con test mínimo.

---

## 2. Convención de carpetas por hipótesis (para que nada se pierda)

### Principio: el estado vive en el registro, no en la ubicación

Una hipótesis **nunca cambia de carpeta** por ser validada o rechazada. Mover carpetas rompe enlaces e historial de git. El veredicto vive en `docs/INVESTIGACION/REGISTRO_HIPOTESIS.md` y en la ficha; los artefactos se quedan donde nacieron.

### Estructura

```
docs/INVESTIGACION/hipotesis/H-XXX-nombre.md   ← ficha: pre-registro, veredicto, historial
research/H-XXX-nombre/                          ← todo el trabajo práctico de la hipótesis
├── README.md              enlace a la ficha + estado resumido
├── config/                espacio de parámetros PRE-REGISTRADO (yaml), congelado al crear la hipótesis
├── experiments/           append-only, numerado
│   ├── exp-001/           config exacta + resultados + fecha (nunca se borra ni se reescribe)
│   ├── exp-002/
│   └── ...
├── analysis/              notebooks y scripts de análisis (no cuentan como evidencia)
└── report/                informe final con números y veredicto
strategies/                 SOLO estrategias validadas, congeladas
└── H-XXX-nombre-v1/       copia congelada del código que pasó validación + hash del commit
```

### Reglas de flujo

1. **Crear hipótesis** = copiar `research/_template/` → `research/H-XXX-nombre/` + crear la ficha en docs + fila en el registro. Tres pasos, siempre los mismos.
2. **Cada experimento** es una carpeta numerada con su config exacta y sus resultados. Correr de nuevo con otro parámetro = nuevo `exp-NNN`, jamás sobrescribir.
3. **Rechazada:** se escribe el informe en `report/`, se actualiza el registro, y la carpeta queda intacta para siempre. Es biblioteca, no basura.
4. **Validada:** el código se **promueve** a `strategies/H-XXX-v1/` (copia congelada, con el hash del commit de validación). `research/` sigue siendo el laboratorio; `strategies/` es la vitrina de lo congelado. El bot solo ejecuta código de `strategies/`.
5. **Modificar una estrategia validada** = nueva hipótesis (H-YYY) o nueva versión (v2) que repite el pipeline completo. Nunca se edita una versión congelada.

Así, dentro de dos años, `research/` contendrá la historia completa —validadas y rechazadas—, `strategies/` solo lo que puede operar, y el registro dirá en una tabla qué pasó con cada idea.

---

## 3. Arranque por etapas

### Etapa 0 — Diseño teórico (semanas 1–3, cero código nuevo)

Orden estricto, porque cada punto alimenta al siguiente:

| # | Tarea | Entregable | Por qué primero |
|---|---|---|---|
| 0.1 | Llenar criterios de **Fase A** con números | `VALIDACION/CRITERIOS_FASES.md` sin PENDIENTE en Fase A | Todo lo que el dry run mida sin criterios previos queda contaminado |
| 0.2 | Llenar `RISK_POLICY.md` | Límites numéricos niveles 1 y 2 | Nada vivo sin límites escritos |
| 0.3 | Responder las 5 preguntas de H-001 | Ficha H-001 sin PENDIENTE en limitaciones | Define cuánta confianza merece el trabajo previo |
| 0.4 | **Diseñar los contratos** (ver §4) | `docs/CONTRATOS.md` | Es el plano de toda la programación posterior |
| 0.5 | Completar `DATA.md` | Fuentes, universo y sesgos de H-001 declarados | Sin esto, 0.3 no puede responderse con evidencia |

**Criterio de salida de la Etapa 0:** ningún PENDIENTE en Fase A, riesgo, ni contratos. Se marca en `ESTADO.md`.

### Etapa 1 — Migración ordenada del código (semanas 3–6)

1. **Inventario:** listar el código existente (archivos, qué hace, qué depende de qué) en `docs/MIGRACION.md` antes de mover nada.
2. **Orden de migración:** `backtester/` → `research/H-001/` (configs y resultados históricos que existan) → `bot/` → `dashboard/`.
3. **Regla de entrada:** ningún componente se migra sin (a) adaptarse a los contratos de 0.4, (b) test mínimo en `tests/`, (c) README actualizado. Si el código viejo no encaja en los contratos, se adapta el código, no el contrato — salvo ADR.
4. Durante la migración del bot se completan `RUNBOOK.md` y `SECURITY.md` con los procedimientos reales.

**Criterio de salida:** `ESTADO.md` marca los tres componentes ✅ con enlace a tests en verde.

### Etapa 2 — H-001 por el pipeline formal (semanas 6–10)

1. **Test de reproducibilidad:** re-correr el backtest de H-001 dentro del repo con la config pre-registrada. Si el resultado histórico no se reproduce, eso es un hallazgo mayor y se documenta.
2. Llenar la tabla de métricas de la ficha (IS/OOS/lockbox) con los números reproducidos.
3. Continuar/reiniciar la Fase A contra los criterios de 0.1. Registrar la decisión de fase con evidencia.

### Etapa 3 — Data Lake (paralelo desde la Etapa 2, ≤30% del tiempo)

Según `ROADMAP.md` §3. No arranca hasta que la Etapa 0 esté cerrada.

### Etapa 4 — H-002 (la prueba de fuego de la plataforma)

Primera hipótesis con pre-registro real desde el día cero. Medir cuánto costó vs. H-001: ese ratio es la métrica de éxito del proyecto entero.

---

## 4. Los contratos a diseñar en la Etapa 0.4 (diseño teórico)

Estos cinco contratos son el "diseño teórico" que precede a la programación. Se escriben en `docs/CONTRATOS.md` con esquemas concretos (campos, tipos, unidades, zona horaria):

1. **Vela:** timestamp (apertura o cierre — decidirlo y no cambiarlo jamás), OHLCV, símbolo, timeframe. La ambigüedad de timestamp es la fuente nº 1 de lookahead.
2. **Funding:** timestamp de aplicación, tasa, convención de signo.
3. **Señal:** lo que una estrategia emite (dirección, tamaño objetivo, timestamp de la vela que la generó). La estrategia no sabe de órdenes ni de exchanges.
4. **Experimento:** config de entrada (yaml) → resultados de salida (métricas + trades), ambos serializados. Un experimento es reproducible si config + datos + hash de código dan el mismo resultado.
5. **Evento del bot:** formato de log estructurado (heartbeat, orden, fill, error, kill switch) que el dashboard consume.

Regla: el backtester y el bot consumen **los mismos contratos de vela, funding y señal**. Esa es la única garantía estructural de que el tracking error mida ejecución y no discrepancias de definición.

---

## 5. Disciplina de git (para que "nada se pierda" también en el historial)

- Commit pequeño y frecuente; mensaje con prefijo: `docs:`, `research(H-001):`, `backtester:`, `bot:`, etc.
- **Tag en cada evento epistemológico:** apertura de lockbox (`lockbox-H001-abierto`), decisión de fase (`H001-faseA-aprobada`), promoción a strategies (`H001-v1-validada`). Los tags hacen el historial auditable.
- Rama `main` siempre estable; ramas cortas para trabajo en curso. Sin flujos complejos: eres un solo desarrollador.
- Push al remoto al final de cada sesión de trabajo, sin excepción: el repo local no es backup.
