# H-002.v2 — Ruptura Donchian(20) + filtro SMA200, diario, solo largos — PRE-REGISTRO DEL BANCO

> **ESTADO: SELLADO — 2026-07-19. NO CORRIDO (a la espera del push y de la secuencia de ejecución).**
> Fecha de redacción y sellado: 2026-07-19. Redactado y sellado ANTES de re-correr el banco y ANTES de mirar cualquier resultado nuevo. Regla 4 de los guardarraíles: PREREG sellado antes de correr. Todos los umbrales son explícitos y binarios; ninguno queda a interpretación (verificado, cero parámetros abiertos). Detalle del sellado: §9.

## 0. Por qué existe la v2 (qué cambió respecto a v1 y por qué)

La v1 fue **RECHAZADA el 2026-07-19** por disparo T1 firme (principio 17): su test decisivo pre-escrito disparó la regla MATA y fue anulado por vía interpretativa en el mismo `RESULTADO_BANCO.md`, sin ADR / A-04 / ratificación. La crítica de fondo a T1 —comparar contra *hold BNB crudo* sobre la historia completa mide un **outlier irrepetible** (el 40× de 2017-21), no la presencia de edge— es probablemente correcta, pero bajo el principio 17 solo es admisible si se especifica en el diseño, antes de ver el resultado. Eso hace esta v2.

**Cambios respecto a v1, todos pre-declarados aquí, todos antes de correr:**

1. **El test decisivo pasa a la cesta multi-activo + OOS forward**, no a un mono-activo historia-completa (§3, T1). La comparación mono-activo queda **descriptiva, no decisiva**.
2. **Se elimina "risk-matched"** como instrumento. Razón técnica: el Sharpe es invariante al apalancamiento (escalar retornos por *k* no cambia media/desv → mismo Sharpe) y el MAR con retornos simples es cuasi-invariante; igualar riesgo no movería las métricas que decidían, así que no resolvía el problema que pretendía. Lo que sí neutraliza el outlier es la sección cruzada (dilución) y el OOS post-pump.
3. **La conjunción decisiva se re-funda para NO reusar el lockbox quemado:** screen in-sample **pre-2023** ∧ decisivo **forward** (§3, §5). El tramo 2023-26 (lockbox abierto en v1) queda quemado y descriptivo.
4. **Funding (P3) entra al motor** en la corrida decisiva forward (§4). No puede quedar sin medir siendo la estrategia siempre larga.
5. **Dictamen A-01 obligatorio** sobre el resultado antes de cualquier veredicto (§6). La v1 no tuvo ninguno.
6. **Corrección por pruebas múltiples** explícita: N de configuraciones declarado y Deflated Sharpe (`PROTOCOLO §3`, §3 T4).

## 1. Hipótesis económica (heredada, sin cambios)

Misma que la v1 (`../HIPOTESIS_ECONOMICA.md`): subreacción/rebaño amplificada por apalancamiento, filtrada al régimen alcista (SMA200) y cosechada a 2R fijo. **Long-only, beta positiva declarada** — la ventaja postulada es timing de beta / reducción de drawdown, NO alfa market-neutral. Sin cambios en el mecanismo ⇒ no hay re-optimización de la señal (principio 17 requisito 5): la señal queda **idéntica** a v1.

## 2. Señal (congelada, idéntica a v1)

Entrada: ruptura del máximo de **20 días** (shift 1) con **precio > SMA200**, solo largos. Stop **2.5×ATR(14)**. Objetivo **2R fijo**. Riesgo **1.25%/trade**. Timeframe **diario**. Motor reutilizado *verbatim* (`../banco.py`). **La variante trailing sigue fuera** (más parámetros, autoflag dudosa). Universo: BTC, ETH, BNB, ADA, XRP, LTC (los 6, equiponderados en la cesta).

## 3. Tests y criterios de decisión (PRE-ESCRITOS, binarios)

Los tres tipos de consecuencia se mantienen **separados**: **MATA** (rechaza la hipótesis), **CAP** (limita confianza/sizing, no mata), **FLAG/descriptivo** (informa, no decide).

### T1 — decisivo (MATA). Cesta multi-activo, dos tramos, conjunción.

Se compara la **cesta equiponderada de los 6 activos** de la estrategia contra la **cesta equiponderada de buy-and-hold** de los mismos 6 (ambas sin apalancar, retorno natural). Métricas: **Sharpe y MAR**. Dos tramos, ambos obligatorios:

- **T1-IS (screen in-sample, datos pre-2023):** la cesta-estrategia debe superar a la cesta-hold en **Sharpe Y MAR**, por margen estricto > 0.
- **T1-OOS (decisivo, forward desde 2026-07-15):** la cesta-estrategia debe superar a la cesta-hold en **Sharpe Y MAR**, por margen estricto > 0.

**MATA si falla T1-IS o falla T1-OOS** (conjunción — justificación en §8). El tramo **2023-26 no entra en T1** (lockbox quemado, `PROTOCOLO §5`); se reporta como contexto descriptivo, sin peso decisivo.

### T2 — generalización cruzada (FLAG, no mata). Descriptivo.

Misma señal congelada, por activo: ¿en cuántos de 6 la estrategia bate al hold (Sharpe y MAR)? Se **reporta el conteo**. BANDERA de selección si funciona en un activo pero falla en la mayoría. No decide por sí solo; informa la lectura de T1.

### T3 — sensibilidad de parámetros (FLAG + dato obligatorio).

Canal 20→{10,15,30,40}; SMA 200→{100,150,300}; ATR {2,2.5,3}. ¿Meseta o pico? Se reporta el **N total de configuraciones probadas** (obligatorio, `PROTOCOLO §3`), insumo del Deflated Sharpe de T4. BANDERA si los vecinos se derrumban (net≤0 o Sharpe colapsa).

### T4 — significancia y concentración (CAP de confianza, no mata).

Se aplica **CAP** (limita sizing, prohíbe "capital significativo") si se cumple **cualquiera** de:
- **n < 30** trades cerrados (en el tramo evaluado), **o**
- **top-5 trades > 50%** del PnL neto (concentración), **o**
- **Deflated Sharpe < 0** (con el N de configuraciones de T3).

El CAP no rechaza la hipótesis; la mantiene con confianza limitada.

## 4. Funding e instrumento (P3)

- **Instrumento decisivo: perp USDT con funding real.** Espejo **spot sin funding** = diagnóstico (no decisivo), para aislar el efecto del funding.
- **Screen in-sample (T1-IS) corre en spot** — es la base sobre la que v1 estableció el resultado histórico conocido; su papel es consistencia, no evidencia nueva. **La corrida decisiva forward (T1-OOS) corre en perp + funding real.** La asimetría es deliberada y está justificada en §8.
- El funding entra como coste por barra sobre la posición larga abierta, **condicional por símbolo y fecha** — nunca un promedio incondicional (lección de exp-008 / TEORIA v0.2: los promedios incondicionales sobredeclaran; la selección de posiciones de tendencia es adversa al promedio).
- Dataset de funding: **dictamen A-02 previo (APTO)** con hashes de fábrica congelados, igual que exp-008, antes de correr. Restricción declarada: el funding perp solo existe desde el lanzamiento de cada perp (post-2017); por eso lo decisivo es el forward, donde el dato existe con certeza.

## 5. Datos, particiones y horizonte (mecánico)

- **IS (desarrollo):** todo lo **anterior a 2023-01-01**. Se usa para T1-IS, T2, T3, T4.
- **Quemado (descriptivo):** **2023-01-01 → 2026-07-15** (lockbox v1 abierto + tramo hasta el arranque del forward). No entra en ningún criterio que mate o limite; solo contexto.
- **OOS limpio (decisivo):** **forward desde 2026-07-15**, el `paper_real` multi-activo que corre sin tocar.
- **Horizonte y momento de evaluación (regla mecánica, sin discreción):** el análisis de T1-OOS se ejecuta **exactamente cuando se cumplen por primera vez, de forma simultánea, ambas condiciones**: **≥ 30 trades cerrados** en la cesta forward **Y** **≥ 6 meses** transcurridos desde 2026-07-15 (es decir, en o después de 2026-01-15). "Trade cerrado" = posición salida por TP o SL registrada en el log del forward. No hay discreción para adelantar ni para esperar más: se evalúa en el primer cierre diario en que ambas se satisfacen a la vez.
- **Estado mientras el criterio no se cumpla (estrategia de baja frecuencia):** mientras el forward no alcance simultáneamente los ≥30 trades y los ≥6 meses, el estado de H-002.v2 es **"evidencia insuficiente"** — pipeline EN VALIDACIÓN, estatus epistemológico NO PROBADA. **No podrá declararse confirmada ni refutada por ausencia de datos.** Un forward lento no es éxito ni fracaso: es, simplemente, aún no evaluable. No se adelanta el veredicto ni se reinterpreta la espera como señal.

## 6. Validación y veredicto

- **A-02** sobre el dataset de funding (si perp) antes de correr.
- **A-01 obligatorio:** el resultado del banco (métricas por tramo, N, Deflated Sharpe, jackknife) pasa por **dictamen A-01** antes de cualquier veredicto. Sin dictamen, no hay veredicto — subsana el hueco central de la v1.
- **Veredicto:** APRUEBA (pasa a la siguiente etapa del pipeline, going-forward) solo si **T1-IS y T1-OOS** aprueban (conjunción) **y** A-01 dictamina CONFORME. La confianza y el sizing los fija T4. **T2 y T3 son diagnósticos: se reportan y alimentan la lectura de A-01, pero no constituyen una compuerta binaria propia** (no existe umbral de "bandera grave"; su papel es informar, no decidir). Mientras el forward no cumpla el criterio de §5, el estado es "evidencia insuficiente" (ni confirmada ni refutada). Si T1-OOS falla una vez cumplido el criterio, **la hipótesis muere — sin nota interpretativa posible.**

## 7. Reglas anti-sobreajuste (retenidas y reforzadas)

1. Ningún parámetro se re-optimiza por lo visto. Espacio de §3 cerrado de antemano; N reportado.
2. No cherry-pick de activo ni de parámetro con retrovisor.
3. La variante trailing NO se prueba en vivo.
4. Cada resultado se acepta como salga.
5. Los umbrales se congelan con el sellado del IP; después no se renegocian ("casi pasa = no pasa").

## 8. Justificación de los criterios decisivos (escrita antes de cualquier resultado de v2)

Esta sección no crea ninguna regla nueva; deja constancia de **por qué** los umbrales son los que son, antes de que exista dato de v2, para que ninguno parezca elegido por conveniencia a posteriori.

**Por qué la cesta y no el mono-activo (T1).** El fallo de v1 fue dejar que un único 40× irrepetible dominara el criterio decisivo. La cesta equiponderada diluye cualquier outlier de un solo activo: el mecanismo postulado es "trend-timing con filtro de régimen", que es una afirmación **de sección cruzada** ("funciona en varios activos"), no sobre un activo. Juzgar el mecanismo con una cesta es medir lo que la hipótesis realmente afirma.

**Por qué Sharpe Y MAR (conjunción de métricas).** La hipótesis promete dos cosas distintas: retorno ajustado por riesgo (Sharpe) y, sobre todo, **reducción de drawdown** (MAR = CAGR/MDD, sensible al DD). Exigir ambas evita aprobar una estrategia que mejora una a costa de destrozar la otra. Son propiedades no redundantes; se piden las dos.

**Por qué la conjunción IS ∧ OOS, y por qué no forward-solo.** Dos modos de fallo independientes: (a) que nunca hubiera edge y el forward favorable sea suerte; (b) que hubiera edge in-sample pero se haya sobreajustado/decaído. El screen in-sample (pre-2023) rechaza (a): sin base histórica, no promovemos por una ventana corta afortunada. El OOS forward rechaza (b): es el único dato no visto y es lo que decide. **Forward-solo se descartó** porque una muestra de ~30 trades / 6 meses tiene poca potencia estadística; hacerla juez único la vuelve rehén de la varianza de una sola ventana —el error espejo de v1—. El screen in-sample es un seguro barato que no reusa dato quemado (corre pre-2023, no sobre el lockbox 2023-26).

**Por qué in-sample en spot y decisivo en perp+funding (§4).** El screen in-sample solo verifica consistencia con el resultado histórico ya conocido (que v1 estableció en spot); no aporta evidencia nueva, así que su instrumento es secundario. El veredicto real es el forward, y debe correr en el **instrumento operable** (perp) con su **coste dominante medido** (funding), que es además donde el dato de funding existe con certeza. Poner el funding donde decide, y no donde solo se confirma lo ya sabido, concentra el rigor donde importa.

**Por qué los umbrales de T4 (n<30, top-5>50%, DSR<0).** n<30: piso convencional de tamaño de muestra por debajo del cual el Sharpe muestral es demasiado ruidoso para fiar sizing. top-5>50%: si más de la mitad del neto cuelga de 5 trades, el resultado depende de la cola y no del proceso repetible (H-001 llegó a 115% en top-5 — lección directa). DSR<0: tras corregir por el N de configuraciones probadas, un Deflated Sharpe negativo dice que el mejor resultado es indistinguible de buscar entre ruido. Los tres **limitan confianza**, no matan, porque son afirmaciones sobre la *fuerza* de la evidencia, no sobre la *ausencia* de edge.

**Por qué ≥30 trades Y ≥6 meses, lo que ocurra más tarde, y evaluación mecánica.** El piso de trades (≥30) alinea el OOS con el mismo umbral de muestra de T4. El piso temporal (≥6 meses) evita concluir en un tramo corto y potencialmente atípico aunque los trades lleguen rápido. "Lo que ocurra más tarde" y la evaluación en el primer cierre en que ambas se cumplen eliminan la discreción de fecha —el grado de libertad "¿esperamos un poco más?" que permite pescar el momento favorable—. La regla es completamente mecánica: dispara sola.

---

## Decisiones fijadas (explícitas y binarias) — congeladas por el sellado (§9)

| # | Punto | Valor fijado |
|---|---|---|
| 1 | Umbral T1 | Cesta 6 activos, Sharpe **y** MAR, margen estricto >0, en **T1-IS (pre-2023) Y T1-OOS (forward)**. MATA si falla cualquiera. Mono-activo descriptivo. |
| 2 | "Risk-matched" | **Eliminado** (invariancia de escala del Sharpe). No se usa apalancamiento de matching en ningún test. |
| 3 | Instrumento | **Perp USDT + funding real = decisivo** (forward); **spot sin funding = diagnóstico**; screen in-sample en spot. |
| 4 | Umbral T4 (CAP, no mata) | n<30 **o** top-5>50% del neto **o** Deflated Sharpe<0. |
| 5 | Horizonte forward OOS | **≥30 trades cerrados Y ≥6 meses desde 2026-07-15, lo que ocurra más tarde**; evaluación mecánica en el primer cierre en que ambas se cumplen. |

## 9. Sellado

**SELLADO 2026-07-19.** Umbrales congelados; a partir de aquí no se renegocian (regla 5, "casi pasa = no pasa"). El sellado se produjo tras revisión punto por punto del IP en la sesión del 2026-07-19: refundación de la conjunción a screen in-sample (pre-2023) ∧ forward OOS —sin reusar el lockbox 2023-26 quemado—, horizonte de evaluación mecánico, cláusula de "evidencia insuficiente" para la baja frecuencia, eliminación del último parámetro interpretativo ("banderas graves" en el veredicto), y verificación de cero parámetros abiertos.

Ratificado por el **Investigador Principal (Yeison Díaz)** en esa sesión. La firma en el registro inmutable se consuma con el **push (`tanda.ps1`)**, acto que ejecuta el IP; hasta ese push, este sellado consta redactado pero no versionado en git.

**Nada se ha corrido.** Secuencia de ejecución tras el push: A-02 del dataset de funding (hashes congelados) → correr `banco.py` (IS pre-2023 + configuraciones de T3) → esperar el disparo **mecánico** del forward (§5) → A-01 sobre el resultado → veredicto.
