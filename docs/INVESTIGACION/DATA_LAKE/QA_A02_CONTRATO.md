# QA / A-02 — Contrato de validación del Data Lake (v3, post-2º adversarial)

> **Fecha: 2026-07-29 · v3 · Autor: Opus (Claude) sobre la decisión del IP · Estado: PROPUESTA para 3er pase adversarial.**
> **v1 y v2 → NO CONFORME** (`QA_A02_DICTAMEN_ADVERSARIAL.md`). v3 **re-ancla la compuerta**: de *"independencia de proveniencia"* a **censo verificado + cota de survivorship + realismo de ejecución**, con **4 estados de certificación**. Deriva de `DATA_LAKE_ALCANCE_ESQUEMA.md` v2. No es código.

## 0. Reconocimiento de errores de v2 (honestidad — no se ocultan)

1. **v2 gateaba sobre el proxy equivocado.** Condicionaba en *nº de proveniencias independientes*; la propiedad que importa es la **completitud del censo**. Confundirlos sobre-bloquea (censo resuelto pero proveniencia única → CONDICIONADO eterno) y sub-bloquea (dos fuentes independientes que comparten el mismo hueco de arranque). **Corregido: la compuerta es censo verificado; la proveniencia independiente es *una* evidencia admisible, no la condición.**
2. **v2 invirtió el razonamiento de Tardis.** El survivorship de Binance nace del **momento de la consulta** (REST retroactivo: si borran el símbolo, desaparece), no de la entidad. Una **captura point-in-time del websocket** (Tardis) es un fósil que **retiene los deslistados** — antídoto contra survivorship (sí es espejo para error de *venue*). Confirmado por docs de Tardis. **Corregido: Tardis es evidencia admisible de completitud del censo; se re-confirma su política de retención en su contrato antes de pagar.**
3. **v2 llamó "irreducible por software" a una tarea de ingeniería.** Anuncios de Binance + `exchangeInfo` snapshotteable + Wayback + registros de terceros hacen la reconstrucción del censo un trabajo de 2-3 semanas, no un límite epistémico. **Retirado.** Se abre un spike de censo acotado (§8).

## 1. Reencuadre conceptual (la pregunta correcta)

**No:** "¿tengo dos fuentes independientes?" · **Sí:** *"¿puedo demostrar cuál era el universo elegible en cada momento, y cuantificar cuánto cambiaría mi conclusión si faltan observaciones?"* Las fuentes independientes son una **herramienta** para responderla, no la respuesta.

**La compuerta se ancla en tres cosas medibles:**
1. **Censo verificado** — universo elegible point-in-time, con cobertura documentada y cuantificable (§6, §8).
2. **Cota de survivorship** — no "cero survivorship" sino *cuánto podría cambiar la conclusión* si faltan observaciones (§3).
3. **Realismo de ejecución** — que el PnL no sea función de supuestos de slippage/venue en vez del mercado (§4).

## 2. Los cuatro estados de certificación

Reemplazan el binario APTO/CONDICIONADO y su patología (reetiquetar la hipótesis para que encaje con los datos, o congelar el lab). Los desks reales **dimensionan, no prohíben**.

| Estado | Condición | Efecto en promoción |
|---|---|---|
| **APTO** | Censo suficientemente verificado · sin sesgo de survivorship material · datos pasan QA/A-02 · la hipótesis supera sus pruebas | Pasa a candidata / capital sin cota especial |
| **APTO-ACOTADO** | Limitación de survivorship/cobertura **cuantificada** · cota razonable del impacto establecida · la hipótesis **sigue mostrando evidencia tras sensibilidad/peor caso** · la limitación se incorpora al **tamaño/alcance/interpretación** | Pasa a capital **con cota declarada y tamaño limitado**. **NO es automáticamente "listo para producción"** |
| **CONDICIONADO** | Evidencia interesante, pero la incertidumbre sobre universo/datos es **demasiado grande para cuantificarla** | **Solo exploración / generación de hipótesis.** NO promueve a candidata formal / pre-registro hasta resolver la condición |
| **NO APTO** | Sesgo/defecto conocido y grave que invalida la inferencia · **o** la estrategia deja de existir al corregir los problemas | Bloqueado |

**Puente con la compuerta dura (cierra la ambigüedad del 2º dictamen):** la COMPUERTA de promoción (alcance §0.9 / regla 5 `DATA.md`) se satisface con **APTO** o **APTO-ACOTADO** (este último con cota y tamaño declarados); **CONDICIONADO y NO APTO NO la satisfacen.** No hay estado intermedio ambiguo que se cuele.

**Caducidad y responsable (cierra "permanente por omisión"):** todo **CONDICIONADO** y **APTO-ACOTADO** lleva **fecha de revisión** y **responsable nombrado**. Sin ambos, el estado no es válido.

## 3. Test de cota de survivorship (el mecanismo central)

Con el censo reconstruido (§8), para cada símbolo **ausente** del dataset se asume el **peor caso plausible** (p.ej. −100% en la ventana de delisting, sin liquidez de salida) y se **re-corre la estrategia**:

- **El edge sobrevive a la cota** → survivorship **NO vinculante** para esa hipótesis (con proveniencia única o no) → hacia **APTO**.
- **El edge no sobrevive** → tienes **un número, no una etiqueta**: la magnitud del impacto → **APTO-ACOTADO** (si acotable y la hipótesis aún muestra evidencia) o **NO APTO** (si el edge desaparece).

Esto convierte el survivorship de una propiedad binaria imposible de probar en una **cantidad acotada**.

## 4. Realismo de ejecución (para altcoins ilíquidas pesa MÁS que el survivorship)

Orden de riesgo para mean-reversion en baja liquidez (survivorship en 3er lugar, no 1º):

1. **Realismo de fills.** Sin libro de órdenes, el PnL de altcoins ilíquidas es función de tus supuestos de slippage, no del mercado. Inflación de Sharpe típicamente **mayor** que la del survivorship. → exigir curva de sensibilidad al slippage + breakeven (ya en F6 AC-5); sin libro, el resultado vale como señal de existencia a tamaño ~0.
2. **Wash trading en el venue.** **Punto ciego estructural:** *ninguna* independencia de proveniencia lo detecta — todas las fuentes registran los mismos trades falsos. Se marca como riesgo declarado; se mitiga con filtros de volumen/actividad sospechosa, no con más fuentes.
3. **Restatement de klines.** Binance revisa datos históricos → cubierto por INT + caducidad de dictamen (§7).

## 5. Survivorship de selección y de contrato (más allá del dato)

- **De selección:** BTC/ETH se eligieron **porque sobrevivieron**. Es survivorship a nivel de **selección del investigador**, no del dato — lo juzga **F0/metodología**, no A-02, pero se **nombra explícitamente** para que no se ignore.
- **De contrato:** aun en BTC/ETH hay survivorship a nivel de contrato (cambios de especificación, tiers de liquidación, migración coin-margined → USDT-margined). **A-02 lo marca** en los metadatos del instrumento. El riesgo en majors **no es ~cero.**

## 6. Censo: de compuerta binaria a propiedad medible

- La **completitud del censo** es la propiedad gateada; se **cuantifica** (§8), no se declara.
- La **proveniencia independiente** es **una evidencia admisible** de completitud, no la condición. Admisibles: captura point-in-time (Tardis), anuncios, snapshots de `exchangeInfo`, Wayback, cruces de terceros — cada una con su nivel de confianza.
- El **raw como corroboración** sigue valiendo (símbolo observado y ausente del censo → fallo del censo), reconociendo que es **unidireccional** (no revela lo ausente de raw *y* censo — por eso no es suficiente solo).

## 7. Controles QA heredados (integridad/calidad) — corregidos

Se conservan los controles de v2 de integridad y calidad, con las correcciones del 2º dictamen:

- **PIT-01 e INT-02 se MANTIENEN AMBOS** — detectan fallas distintas (huecos vs restatement); no se sustituye uno por otro.
- **Detección de hueco de borde (corrige colapso PIT-01):** un hueco al inicio/fin del raw se coteja contra el **censo (§8)** — si el censo dice que el símbolo cotizaba, es hueco (🔴/🟠), no listing/delisting falso.
- **INT-02:** byte-identidad prueba estabilidad de transporte, **no corrección**; donde exista una captura genuinamente independiente (Tardis), se cotejan muestras.
- **Agregación determinista** (§4 de v2) para los controles de integridad/calidad: cualquier 🔴 → dimensión NO CONFORME; se añade estado **"no evaluado"** para controles que la precedencia salta.

## 8. Spike de censo (ANTES de congelar v3) — acotado, con criterios de éxito y fracaso

- **Objetivo:** reconstruir el universo histórico de instrumentos. **Filosofía: cuantificar y ACOTAR el survivorship, NO probar que es cero.**
- **Fuentes:** Binance histórico · Tardis (si su retención conserva deslistados — re-confirmar) · anuncios de Binance · snapshots de `exchangeInfo` · Wayback / archivados · otras con fechas de listado/delisting.
- **Salida (por símbolo):** `symbol · listing_date · delisting_date · fuente_evidencia · fecha_captura · nivel_confianza · conflictos_entre_fuentes`.
- **Criterio de éxito:** cobertura **documentada y cuantificable** del universo histórico.
- **Criterio de fracaso (cierra "el spike corre indefinidamente"):** no reconstruir una fracción **material** del universo tras un esfuerzo **previamente acotado en tiempo** (time-box declarado). Si fracasa, se declara y se pasa a operar con la cota del peor caso (§3), no se congela el lab.

## 9. Entregables + dictamen (4 estados)

```
A02_REPORT.md/.json · MANIFEST.json (raw+parser+censo+a02 hashes) · CENSO_RECONSTRUIDO.csv ·
COVERAGE_REPORT.csv · SURVIVORSHIP_BOUND.md (test §3) · GAPS.csv · ANOMALIES.csv · HASHES.sha256
```

```
A-02 DATA QUALITY DICTAMEN
Dataset / Versión / Manifest / a02_version / parser_version / censo_hash / Fecha
──────────────
INTEGRIDAD / CALIDAD:   CONFORME / NO CONFORME  (controles §7)
CENSO:                  cobertura documentada X% · nivel de confianza · conflictos
COTA DE SURVIVORSHIP:   vinculante / NO vinculante · magnitud si vinculante (§3)
REALISMO DE EJECUCIÓN:  fills · wash-trading · restatement (§4)
──────────────
ESTADO: APTO / APTO-ACOTADO / CONDICIONADO / NO APTO
  (si APTO-ACOTADO o CONDICIONADO → cota + fecha de revisión + responsable nombrado)
Firma: A-02 · <fecha> · <a02_version>
```

## 10. Orden de trabajo + 3er pase adversarial

1. Spike de censo (§8) con su time-box y criterios. 2. Test de cota (§3) sobre el censo reconstruido. 3. Completar los controles QA (§7). 4. **3er pase adversarial independiente de esta v3.** 5. Si sobrevive → congelar; si no → v4.

> **Independencia (patrón A-04/F6b):** el revisor expone, no corrige; sesión distinta de quien redactó v3.

## 11. Lo que este contrato NO hace

No implementa controles, no fija aún los valores numéricos finales (cota material, time-box del spike, umbrales de wash-trading — los ubica y les asigna dueño), no reconstruye el censo (eso es el spike), y no reemplaza a F0 en juzgar suficiencia ni survivorship de selección. Y **no está congelado**: debe sobrevivir el 3er pase adversarial.
