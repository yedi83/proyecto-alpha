# Resumen Ejecutivo — Proyecto Alpha

> Corte: **2026-07-20** — cierre fundacional de gobernanza (ADR-0007) y arranque productivo del Banco de Mecanismos (C-001: F1 y F2 cerradas). Extiende el corte previo del 2026-07-17 (funding real de H-001). Cubre el laboratorio original (`donchian512_lab`, junio 2026) y el repositorio `proyecto-alpha` (julio 2026).
>
> No confundir con: `research/H-001-canal-donchian/report/legacy/INFORME_EJECUTIVO.md` (informe del lab de junio, solo H-001, congelado como registro histórico — no se actualiza) ni `report/resumen_instancias_2026-07-10.md` (foto operativa de las 3 instancias). Este documento es la síntesis viva de TODO el proyecto y es el único que se actualiza en hitos mayores.

## Titular del corte (2026-07-20) — la gobernanza cierra su caso fundacional y el Banco empieza a producir

**Tres hitos encadenados en 72 horas, guiados por un mismo principio nuevo.** (1) El **ADR-0007** cerró el caso fundacional: el **principio 17** entró en la Constitución — los veredictos de umbral pre-escrito no se anulan por nota, nunca más; la retroactividad muere en el único acto que la usó. (2) Ese mismo principio disciplinó a **H-002**: su banco del 07-14 se apoyaba en anular su test decisivo por nota (T1 disparó "MATA" y fue anulado en el mismo documento), así que **H-002.v1 quedó RECHAZADA** (disparo firme, sin rescate) y se re-diseñó como **H-002.v2** — sellada, con el test decisivo bien especificado desde el diseño; su screen in-sample oficial ya pasó, y el veredicto decisivo espera al forward (~2027). (3) El **Banco de Mecanismos abrió su C-001** y produjo sus dos primeras fases: **F1** (30 mecanismos de la literatura, 100% verificados por búsqueda web) y **F2** (árbol genealógico por ineficiencia, con **H-001 heredando la evidencia multi-siglo de la persistencia**). En las tres líneas, el arbitraje independiente A-04 cazó y forzó a corregir varias desviaciones antes de cada cierre — incluidas dos del propio mentor.

**La foto en una frase:** el laboratorio pasó de *tener* reglas a *ejercerlas contra sí mismo*, repetidamente y en días — que es exactamente su criterio de éxito.

## Titular previo (2026-07-17) — la incógnita nº 1 se cierra a favor

**El funding real 2021-26 no destruyó el edge: lo mejoró.**

*Qué estaba en juego, en lenguaje llano.* El backtest siempre asumió un **peaje fijo** por mantener posiciones abiertas: 0.01% cada 8 horas. Nunca supimos cuál había sido el peaje *real* de esos cinco años. Era la mayor duda pendiente de H-001 — si el funding real resultaba caro, buena parte del edge podía ser una ilusión contable. El veredicto original de junio ya lo advertía: *"con funding alto, 2024-26 queda ≈ 0"*.

*Qué se hizo.* exp-008 tomó los **27.715 tramos de funding reales** de Binance (2021-07 → 2026-07, los 5 símbolos), auditados por A-02 **hasta el hash**, y los aplicó al backtest en el instante exacto de cada cobro — pre-registrado como **intento único**, con umbrales sellados antes de mirar y paridad de motor verificada al centavo.

*La respuesta fue la contraria al miedo.* El peaje real resultó **más barato que el asumido**: la cesta pagó **$452.79** de funding en la ventana FULL frente a ~$776 que le cobraba el modelo uniforme — un **~42% menos**. Con costes reales la estrategia rinde **mejor** que con el modelo:

| ventana | modelo uniforme | **funding REAL** |
|---|---|---|
| FULL 2021-26 | NET 24.03% · Sharpe 0.42 · Calmar 1.35 | **NET 27.26% · Sharpe 0.47 · Calmar 1.66** |
| 2021-23 | NET 9.52% · Sharpe 0.48 | **NET 10.26% · Sharpe 0.51** |
| 2024-26 (la temida) | NET 2.79% · Sharpe 0.18 | **NET 4.63% · Sharpe 0.26** |

**Veredicto: R0 — ACEPTABLE.** La "mayor incógnita de magnitud" declarada desde junio queda **CERRADA a favor** para el período medido, y la **condición (i) del ADR-0006 queda CUMPLIDA**: el camino a capital real vuelve a depender de una sola cosa — **que la Fase B apruebe**. La cláusula de seguridad sigue intacta: si algún experimento futuro dispara letal, H-001 se retira sin discusión.

*De dónde salió el ahorro (matiz que evita una lectura optimista de más).* No salió de "cobrar" funding: **la cesta pagó en los 5 símbolos y en ambos lados** (longs −$413, shorts −$40 netos). Salió de que el modelo uniforme cobraba 0.01%/8h a **toda** posición abierta, siempre y en cualquier signo, mientras el funding real fue en promedio más barato. Ojo con un atajo tentador: SOL y BCH tuvieron funding medio *incondicional* negativo (−2.81% y −2.59% anualizado), pero **los longs de la cesta en esos dos símbolos igualmente pagaron** (SOL −$69, BCH −$3) — la estrategia estaba larga precisamente cuando el funding era positivo. El promedio del mercado no es el promedio que paga tu posición.

*Encuadre que acompaña al titular:* H-001 sigue **CUESTIONADA** por ADR-0006 (el letal de robustez de exp-004) y la cláusula del **segundo disparo** sigue vigente — exp-008 elimina un riesgo de muerte específico, no rehabilita la hipótesis.

## Qué es

Un laboratorio cuantitativo personal cuyo objetivo no es una estrategia ganadora sino **un proceso que produce conocimiento confiable sobre los mercados** — con la premisa de que las estrategias son temporales y la infraestructura permanece, y con un diseño explícito contra el único adversario interno: el autoengaño del investigador.

## Etapa 1 — El laboratorio original (donchian512_lab, junio 2026)

Investigación completa de la primera hipótesis, **H-001: canal de Donchian 512 en velas de 15m sobre perpetuos cripto** (BTC, ETH, SOL, BCH, DOGE), con un rigor inusual para un proyecto personal: pre-registro con parámetros congelados ANTES de correr (2026-06-24), predicción propia registrada y luego falsada y documentada ("FALLÉ"), OOS por segmentos, lockbox (último 20%), ventana no vista 2021-23, jackknife por trades y por tiempo, bootstrap por bloques, regresión alfa/beta, frontera de riesgo y corte por regímenes.

**Veredicto honesto de esa investigación:** trend-following market-neutral (beta 0.006), Sharpe ~0.42 (igual al buy&hold), pero maxDD -18% vs -88% del buy&hold; alfa +11.6%/año **no significativa** (t=0.94); todo el neto cuelga de ~5 trades (win rate 20%). Clasificación: *diversificador plausible / seguro de convexidad — NO edge probado.* Mayor incógnita declarada: el funding real.

## Etapa 2 — El repositorio proyecto-alpha (2026-07-01 → 07-10)

Sobre esa base se construyó el sistema de gobernanza completo:

**Gobernanza:** Constitución de 16 principios (datos>opiniones; criterios antes que resultados; lockbox de un solo uso; la IA no toma decisiones de trading; separación generación-de-conocimiento/producción-de-evidencia; Costo de Gobernanza) · ADRs de primera clase con condición de revisión obligatoria (4 emitidos) · versionado científico H-XXX.vN · dos auditorías anuales (Simplicidad y Creencias, primera 2027-07).

**Pipeline de validación:** toda idea es hipótesis con pre-registro → backtest → OOS → lockbox → Fase A (dry run) → B (demo, órdenes) → C (capital real ~$750) → producción auditada → retiro. Contratos de datos congelados (vela=apertura UTC, señal≠orden, registros append-only). Réplica offline como instrumento de cierre de fase (selftest validado).

**Agentes IA (4):** A-01 Validador Estadístico y A-02 Auditor de Datos (adversariales, dictamen bloqueante), A-03 Investigador, A-04 Árbitro de Metodología (valida cumplimiento del proceso, modo validador estricto). Backlog de 13 con disparadores.

**Banco de Mecanismos (C-001, F0 congelada):** pipeline F0–F7 que audita literatura (nunca calcula), deduplica por árbol genealógico de mecanismos, exige falsabilidad popperiana, y entrega **protocolos experimentales pre-registrables** (0-5 por ciclo, sin mínimo) — el banco diseña el experimento antes de ver nuestros datos. Artefactos JSONL como fuente de verdad. Regla de inmutabilidad del ciclo + moratoria de diseño (ADR-0004) vigentes.

**Teoría del Laboratorio (v0.1):** documento vivo de creencias sobre mecanismos con estados epistémicos y linaje de evidencia. Ya contiene 4 creencias ganadas (rotación de contribuyentes, convexidad como naturaleza del estilo, valor en drawdown+descorrelación, feeds materialmente distintos) y 1 falsación (crisis-alpha por shorts).

## Etapa 3 — Validación operativa y cierre de la incógnita nº 1 (2026-07-10 → 07-17)

Siete días densos en los que el proceso se puso a prueba a sí mismo tres veces: cerró una fase, detectó y remedió una contaminación propia, y resolvió a favor la incógnita que colgaba sobre la hipótesis desde junio.

**Fase A CERRADA — aprueba 6/6 (07-14).** Replay offline de la fase completa: **36 señales del modelo = 36 eventos del bot, 0 divergencias**, latencia mediana 8.7 s (p95 14.9 s), 104 velas atrasadas con causa cerrada. Informe sellado; primera revisión de la Teoría sin cambios de creencias de mercado.

**Fase B iniciada, contaminada y RE-CORTADA (07-14 → 07-16).** El corte del 07-14 quedó comprometido: el ensayo tenía las **mismas API keys demo** que el bot oficial → una cuenta, dos bots colisionando. El diario declaraba "ensayo detenido"; fue intención no cumplida. Remediación: keys del ensayo vaciadas, cuenta aplanada, lanzador blindado con guardián anti-doble-instancia, datos 07-14→16 **anulados** y reloj de 1 mes reiniciado desde el **re-corte limpio del 2026-07-16 15:27:33 UTC**. Fase A quedó intacta. *El incidente es evidencia a favor del proceso: se detectó, se documentó y costó datos, no dinero.*

**ADR-0006 — el override de exp-004 formalizado (07-17).** El veredicto letal de robustez de exp-004 había sido anulado por una nota interpretativa, canal que la Constitución no reconoce. Se formalizó retroactivamente: H-001 degradada a **CUESTIONADA** en todos los registros, Fase C condicionada a exp-008-R0 + cero disparos letales nuevos, y **un segundo disparo letal = retiro operativo automático, sin nota interpretativa posible**. Precedente restrictivo sentado: las notas jamás anulan umbrales. Pendiente: arbitraje A-04 + ratificación del IP.

**Data Lake, pieza 1 — funding histórico real (07-17).** `datalake/funding/`: 5 símbolos, 2021-07-01 → 2026-07-17, endpoint público de Binance mainnet, recolector idempotente sin keys y con QA integrado. **Dictamen A-02: APTO**, con las tres anomalías resueltas con evidencia: los 75 tramos extra de SOL son el episodio documentado de cadencia 4h/2h del **colapso de FTX** (corroborado con el anuncio de Binance a la hora exacta, 2022-11-09 20:00 UTC), los extremos son eventos reales (FTX, The Merge de ETH, crash 2021-09) y el −2% es el cap legítimo de Binance; malla UTC limpia, sin lookahead ni doble aplicación. El artefacto quedó **congelado por SHA-256** y el script aborta si los bytes no coinciden. Crítica de proceso aceptada: el recolector debe emitir hash y metadatos de intervalo de fábrica.

**exp-008 — R0 ACEPTABLE (07-17).** Ver titular. Resultado que **refuta la versión fuerte de la predicción P4** ("el edge se comprime con funding extremo") como efecto agregado histórico: el coste real fue *menor* que el supuesto uniforme, no porque se cobrara carry sino porque el modelo uniforme sobrecargaba a toda posición siempre. **TEORIA v0.2** incorpora la creencia nueva con confianza alta para el período medido — y ese mismo día registró su **primera corrección de atribución causal** (la versión inicial explicaba el ahorro como "cobrar carry en alts": falsa contra la tabla condicional del propio experimento). Mecanismo que queda en la Teoría: **las posiciones de tendencia están adversamente seleccionadas contra el promedio incondicional de funding**. Implicación viva para ADR-0005 (funding-carry): su diseño debe apoyarse en análisis condicional, nunca en promedios incondicionales.

**H-002 formalizada (07-16).** Banco APROBADO con confianza moderada (suite T1-T5 pre-registrada) → forward en paper multi-activo desde 07-15. Declarada con honestidad como **long-only / beta positiva** (no market-neutral), no probada (n=57). Nota meta capturada: el banco reusó el motor del investigador *verbatim* en ~1 jornada = **primera evidencia (n=1) de que la plataforma abarató la segunda hipótesis** — la prueba de fuego del roadmap.

## Etapa 4 — Cierre fundacional de gobernanza y arranque productivo del Banco (2026-07-18 → 07-20)

**ADR-0007 RATIFICADO — el caso fundacional queda cerrado (07-18).** El ADR-0006 (override de exp-004 por nota) fue **RECHAZADO** por el IP tras dos dictámenes A-04 NO CONFORME, y reemplazado por un acto fundacional redactado desde cero en sesión nueva. Su Parte III entró en la Constitución como **principio 17**: un veredicto de umbral pre-escrito es vinculante desde que se produce y solo se anula por ADR + dictamen A-04 CONFORME + ratificación del IP *antes* de surtir efecto; una **disposición transitoria autoderogable** admitió el único caso anterior (exp-004/exp-005) y **prohibió la retroactividad para siempre**. Efectos: Fase A convalidada, re-corte de Fase B convalidado, condición (i) (exp-008-R0) vigente, cláusula de segundo disparo armada sobre la Fase B.

**H-002 disciplinada por el mismo principio (07-19).** Verificación del IP: el banco de H-002 (07-14) había aprobado apoyándose en anular su test decisivo pre-escrito por vía interpretativa — exactamente el canal que el principio 17 acababa de proscribir, y sin rescate posible (transitoria cerrada). **H-002.v1 → RECHAZADA** (disparo T1 firme; el RESULTADO original se conserva intacto). **H-002.v2 → SELLADA**: mismo edge, pero el test decisivo bien especificado desde el diseño (cesta multi-activo; screen in-sample pre-2023 ∧ forward OOS; "risk-matched" eliminado por invariancia de escala del Sharpe; funding real en la corrida decisiva; A-01 obligatorio; lockbox 2023-26 quemado → el OOS limpio es el forward). Screen in-sample **oficial**: la cesta bate al hold en Sharpe y MAR (1.88/1.46 vs 0.80/0.50) — *necesario, no suficiente*. El veredicto decisivo espera al forward (≥30 trades ∧ ≥6 meses; no antes de ~2027), con recordatorio mensual automático.

**C-001 abierto y el Banco produce sus dos primeras fases (07-19 → 07-20).** Para abrir C-001, dos hallazgos A-04 sobre F0 se resolvieron por ADR ratificados (**ADR-0008** mandato de modelo → "mejor disponible a criterio del IP"; **ADR-0009** criterios de rúbrica → resiliencia como compuerta) y F0 obtuvo re-arbitraje CONFORME. Después:
- **F1 (mapeo bibliográfico) — CERRADA:** catálogo de **30 mecanismos/estrategias** de la literatura, **100% verificados por búsqueda web** (autor/año/venue), en las 5 familias en alcance; JSONL como fuente de verdad. A-04 CONFORME (una contradicción menor de un flag resuelta verificando el autor real, no redefiniendo).
- **F2 (árbol genealógico) — CERRADA:** las 30 entradas reorganizadas por *ineficiencia subyacente* con herencia de evidencia hacia arriba. Hallazgo clave: **H-001 (Donchian) hereda el cuerpo de evidencia de la persistencia** — réplicas multi-siglo (1800-2016), ≥5 grupos independientes, candidato a nivel I-II — porque Levine-Pedersen (2016) demuestra que Donchian, cruce de medias y TSM son el mismo edge. Régimen queda marcado como *filtro*, no fuente de alfa; 3 casos frontera declarados sin forzar. A-04 CONFORME tras dos remediaciones (produjo el JSONL que faltaba; eliminó una frase de ranking impropia de F2).

*Nota meta:* en estas fases el arbitraje independiente cazó **cinco desviaciones distintas** (2 en F0, 1 en F1, 2 en F2) antes de cada cierre — dos de ellas del propio mentor. La maquinaria del Banco validándose a sí misma es la meta-pregunta declarada de F0.

## Estado operativo (2026-07-20)

| Instancia | Modo | Rol | Estado |
|---|---|---|---|
| Lab (donchian512_lab) | Órdenes reales en demo, eq=750 | **Fase B oficial** (re-corte 2026-07-16 15:27:33 UTC) | Corriendo limpia; abiertas=0 al corte; reloj de 1 mes → cierre elegible **~2026-08-16** |
| Ensayo B (ensayo_faseB) | **Neutralizado** (keys vaciadas, banner RETIRADO) | Cumplió su rol: validó los 4 fixes de frontera | Retirado tras ser la causa raíz de la contaminación del 07-14 |
| paper_real | Paper sobre feed real mainnet, sin keys | Comparador de feed + forward de señal (PREREG propio) | Corriendo como testigo; feed real ~0.9 velas atrasadas/día/símbolo vs 1.5-2.2 de los feeds de prueba |

**Decisiones cerradas por experimento:** riesgo BTC 0.15% RECHAZADO (exp-002) y 0.125% ACEPTADO (exp-003, pre-registrado como intento final, N=2 declarado) — capital B/C $750 · **funding real R0 ACEPTABLE (exp-008, intento único declarado)**. **Hallazgos que evitaron daño:** Binance retiró el testnet de futuros (F0 → migración a demo trading), `create_order` devuelve precio None y fees solo en fills (2 bugs corregidos antes de operar), min_notional demo $50 vs mainnet $100 (métrica de brecha creada), y **keys compartidas entre ensayo y bot oficial** (contaminación detectada y datos anulados antes de que contaran como evidencia).

## Cómo seguimos — en orden

1. **Corriendo solas, sin acción del IP:** la **Fase B de H-001** (demo, cierre elegible **~16-ago** — el próximo hito real) y el **forward de H-002.v2** (evidencia decisiva ~2027, con recordatorio mensual automático ya puesto). El único trabajo es la rutina de Fase B: **auditoría diaria, diario al día, checklist semanal**. Nada que acelerar.
2. **Banco C-001, abierto y productivo:** F0, F1 y F2 cerradas (todas con A-04 CONFORME + aprobación del IP). Siguiente fase natural = **F3** (evidencia + auditoría de robustez reportada, Opus), cuando el IP quiera (≤30%). Pendientes anotados para el F0 del **C-002**: aclarar el JSONL de F2 en la regla 9 (contradicción tabla/prompt) y la granularidad de sub-familias; más las fricciones de F1/F2 (campo `tipo` edge/teoría/método, niveles I-II que emergen recién en la consolidación).
3. **Si la Fase B aprueba en agosto:** se sella el `PREREG_FASE_C` — decisiones en borrador; queda la **elección §9/§10** (detección de intervención manual y disyuntor *antes* de C, o diferirlos a C-002 con vigilancia reforzada). Entonces H-001 toca **dinero real por primera vez — $750**, con todo lo que estos días construyeron vigilándolo.

**Deuda técnica viva:** QA de los CSV del cache de velas (huecos/duplicados) sigue abierta; y el recolector de datos debe emitir hash y metadatos de intervalo **de fábrica**.

## La foto grande

Hace una semana había una hipótesis cuestionada por su propio instrumento y una incógnita gigante colgando de ella. Hoy: la incógnita **cerrada con datos auditados hasta el hash**, la hipótesis con **su condición cumplida**, y un solo árbitro por delante — la Fase B.

El arco de estas horas es el laboratorio entero en miniatura: una hipótesis cuestionada por su propio instrumento → un ADR que le puso condiciones falsables → un dataset auditado adversarialmente hasta el hash → un experimento con umbrales sellados antes de ver un número → y un veredicto que nadie eligió. **Hace tres semanas esa cadena no existía; hoy corre en una tarde.** El laboratorio está haciendo exactamente aquello para lo que fue diseñado: reducir, experimento a experimento, lo que queda por creer a ciegas.

## El criterio de éxito vigente (del Investigador Principal)

El C-001 — y el laboratorio — se juzgan por una sola cosa: *producir decisiones metodológicas respaldadas por evidencia, incluso cuando esa evidencia contradiga las expectativas previas.* Ya ocurrió **siete veces**: 0.15% rechazado (exp-002), crisis-alpha falsada, predicción original fallada y documentada, el override por nota interpretativa revertido contra el propio interés (ADR-0006), la contaminación de Fase B declarada y sus datos anulados en vez de aprovechados, **P4 refutada en su versión fuerte por exp-008** — una expectativa previa contradicha, esta vez a favor — y, el mismo día, **la atribución causal de ese resultado favorable corregida contra sí misma** (el ahorro de funding no era "cobrar carry en alts"; la cesta pagó en los 5 símbolos y ambos lados). Ese historial, no el PnL, es el activo.

**Actualización al 2026-07-20:** el historial creció sin cambiar de naturaleza. **H-002.v1 fue rechazada acatando su disparo firme** — contra el deseo de conservar una segunda hipótesis que parecía prometedora — en cuanto se vio que su banco se apoyaba en anular un umbral por nota. Y el arbitraje del propio Banco **corrigió al mentor dos veces más** en F2 (un JSONL omitido y una frase de ranking impropia), cada una detectada por una sesión independiente. La regla se mantiene: la evidencia y el proceso ganan a la conveniencia, también cuando la conveniencia es de quien redacta.

> **Nota de calibración (07-17):** las cinco primeras entradas corrigieron al laboratorio *en contra* de su deseo; la sexta lo hizo *a favor* — y la séptima es la más instructiva, porque corrigió la *explicación* de un resultado que ya gustaba. El riesgo cambia de signo pero no desaparece: cuando el número es favorable nadie audita el mecanismo. Dos hallazgos del auditor en un mismo resultado a favor (el hash omitido y la atribución falsa) son el recordatorio de que **la guardia baja sola cuando el resultado gusta**. Un R0 con umbrales sellados y dataset auditado es evidencia legítima, y precisamente por eso no debe usarse para relajar lo que sigue abierto: H-001 CUESTIONADA, cláusula del 2º disparo vigente, ADR-0006 aún en "Propuesta", Fase B sin cerrar.
