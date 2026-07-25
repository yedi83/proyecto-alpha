# F6 — Protocolos de validación (diseño + adversarial fusionados) — Ciclo C-001

> **Fecha: 2026-07-23 · Fusión de las dos sesiones de F6** (ORQUESTADOR prompt F6): **6a diseñador** (`F6_PROTOCOLOS_6a.md`, protocolo base, preservado íntegro) + **6b adversarial** (`F6_AMENAZAS_6b.md`, revisor hostil sin el contexto de 6a, preservado íntegro). Este documento incorpora cada amenaza de 6b al protocolo como **prueba** o como **limitación declarada** (F0 §3c: la resiliencia adversarial es COMPUERTA — cada amenaza entra o el protocolo NO pasa a F7).
> **Fuente de verdad estructurada:** `F6_protocolos.jsonl` (enriquece los 30 objetos de F5 con el campo `f6`). Este `.md` es la vista legible del protocolo.
> **Alcance:** solo las candidatas que viajan (F5). Persistencia = H-001 (referencia, §1). **Carry = protocolo principal (§2).** CEX-DEX e ILLIQ = bocetos bloqueados por prerrequisito (§3). No se calcula, no se rankea (F7), no se declara conformidad (A-04 + IP).

## 1. Persistencia — NO se re-investiga
Es H-001 (Donchian), ya en Fase B. F0 §2 la fija como referencia. Sin protocolo nuevo; su redundancia con H-001 la trata F7.

## 2. PROTOCOLO CARRY / FUNDING (M2, F1-008+F1-009) — base + compuerta adversarial

**Base del protocolo (7 puntos, formato F0 §6): íntegra en `F6_PROTOCOLOS_6a.md §2`** (hipótesis falsable *market-neutral, larga de la prima de funding / corta de la volatilidad del carry, beta≈0*; secundarias H2a-H2d; variables; datos mínimos; espacio de parámetros acotado con justificación económica; criterios G1/E1-3/R1-3; secuencia PIC; retiro conceptual). Se preserva sin cambios.

**COMPUERTA ADVERSARIAL (F0 §3c) — incorporación de las 16 amenazas de 6b.** Cada una entra como PRUEBA A AÑADIR o como LIMITACIÓN DECLARADA:

| # | Amenaza (6b) | Incorporación al protocolo |
|---|---|---|
| **AC-7** ⚠️ | Lookahead: la señal usa el funding *realizado* (conocido en t+1) | **PRUEBA (obligatoria):** la señal usa solo funding **conocido en t** (`shift`); replay offline audita en código que t no toca info de t+1. La más letal — sin esto, todo PnL positivo es sospechoso. |
| **AC-8** 🔒 | Survivorship censura la cola: LUNA/UST fuera del universo = el carry-crash que la tesis debe pagar | **LIMITACIÓN DECLARADA (no cubrible con 5 símbolos):** Sharpe = límite superior; métricas de cola = límite inferior del riesgo real. Prerrequisito Data Lake: universo con delistados + su funding. |
| **AC-5** ⚠️ | Slippage inventado + turnover alto (2 patas × 8h) | **PRUEBA:** curva de sensibilidad al slippage {0 / conservador / 2-3×} + **breakeven de slippage**; descomposición de coste por fuente + turnover anualizado; test de que el edge no dependa del rehedge 8h. |
| **AC-9** 🔒 | Espejo spot sintético (perp−funding) → descomposición funding/base no-identificable | **LIMITACIÓN BLOQUEANTE (H2a):** exige **precio spot real** por símbolo; A-02 debe pronunciarse sobre la procedencia de la serie spot antes de correr. Si es sintético, H2a no es validable. |
| **AC-1** ⚠️ | 2021-26 es un régimen de funding estructuralmente positivo → el resultado puede ser el régimen, no la señal | **PRUEBA:** partición del PnL por **régimen de funding** (alto/bajo/neutro/negativo); y batir el benchmark ingenuo "cobrar siempre funding positivo" (si no lo bate, H2b se refuta). |
| **AC-10** 🔒 | Lockbox contaminado: exp-008/H-002 ya inspeccionaron este dataset | **LIMITACIÓN:** declarar qué sub-períodos ya se vieron; reservar lockbox no consultado o **declarar contaminación** y exigir período nuevo (forward). |
| **AC-2** | La pata negativa (short-spot) asume borrow gratis | **PRUEBA/límite:** modelar coste/disponibilidad de borrow, **o** restringir a la pata long-spot/short-perp y declarar que el funding negativo no es cosechable hoy. |
| **AC-3** | Crowding ya materializado dentro de la muestra (institucionalización 2023-25) | **PRUEBA:** PnL y funding medio por año; test de **tendencia decreciente** hacia el final (la prima puede haber muerto antes del pre-registro). |
| **AC-4** 🔒 | Capacidad no estimable sin order book | **LIMITACIÓN:** resultado vale como señal de existencia a tamaño ~0, no como estrategia dimensionable. Prerrequisito: profundidad/OI (P3). |
| **AC-6** | Coste de re-hedge escala con volatilidad, no modelado | **PRUEBA:** coste de re-hedge **condicional a la volatilidad realizada**; reportar coste en el decil de mayor vol. |
| **AC-11** ⚠️ | Sharpe alto oculta el carry-crash, y el peor está fuera de muestra (AC-8) | **PRUEBA:** evaluar R3 con **estrés sintético** (de-peg −X%, liquidación forzada, salto de funding), no solo peor caída histórica; se declara que R3 se apoya en estrés hipotético (la limitación de la cola censurada la cubre AC-8). |
| **AC-12** | beta≈0 al símbolo no descarta beta a factor cripto agregado | **PRUEBA:** medir beta también contra factor de mercado agregado (BTC/índice) y contra el funding agregado. |
| **AC-13** | La pata perp corta puede liquidarse antes de que la spot se monetice (backtest asume margen infinito) | **PRUEBA:** **simular el margen de la pata perp** (liquidación forzada); reportar cuántos períodos habrían gatillado margin-call. |
| **AC-14** ⚠️ | G1 ("cubrir su peaje") es una compuerta demasiado baja | **PRUEBA (ajuste de criterio):** el umbral debe exigir **margen sobre costes que compense el riesgo de cola** (funding neto ≥ múltiplo del coste), o condicionar la promoción a E1/E2 y no a G1. |
| **AC-15** ⚠️ | n de eventos independientes bajo → R2 lo trata como CAP cuando debería ser "evidencia insuficiente" | **PRUEBA (ajuste de criterio):** convertir el mínimo de eventos en **compuerta de evidencia insuficiente** (ni confirma ni refuta, no refutación); reportar n *efectivo* (descontar autocorrelación del funding). |
| **AC-16** 🔒 | Solo la forma serie-de-tiempo (la más débil) es testeable hoy | **LIMITACIÓN:** ningún resultado positivo de la forma débil se presenta como confirmación del mecanismo completo; el corte transversal (H2d) queda fuera hasta el Data Lake. |

⚠️ = prueba crítica a añadir · 🔒 = limitación no cubrible hoy (bloqueada por prerrequisito).

## 2bis. Veredicto honesto de F6 sobre el carry (no es priorización — eso es F7)

El protocolo de carry está **completo como diseño metodológico**, y su **mecanismo económico es plausible** (fundamento teórico en F4). Esto **NO** demuestra que exista una prima cosechable neta de costes ni una estrategia ejecutable: **mecanismo económico plausible ≠ edge demostrado ≠ estrategia ejecutable** — probar esa cadena es justo lo que el protocolo y el pipeline PIC deben hacer, no F6. **Y su validación *limpia* está BLOQUEADA por prerrequisitos de datos**, con limitaciones que no son menores: (1) **la cola del carry-crash está censurada por survivorship** (AC-8) — el riesgo exacto por el que la estrategia cobra prima no está en los 5 símbolos; (2) la **descomposición funding/base no es identificable** sin serie spot real (AC-9, bloqueante para H2a); (3) el **lockbox puede estar contaminado** (AC-10); (4) la **capacidad no es estimable** (AC-4); (5) solo la **forma débil** (serie de tiempo) es testeable, y es justo la más expuesta al confound de régimen (AC-1/AC-16).

**Conclusión operativa:** un piloto de 5 símbolos es posible, pero con puntos ciegos declarados severos (sobre todo la cola). La validación **completa** del candidato de carry exige el **Data Lake** (universo amplio + delistados + su funding + serie spot real) — **el mismo prerrequisito que bloquea `ILLIQ-MR-001`**. El Data Lake emerge como un **cuello de botella de infraestructura** del ciclo (constatación de qué falta para validar, **no** un juicio de prioridad entre candidatas — eso es F7).

## 3. Bocetos bloqueados por prerrequisito
- **CEX-DEX arb (F1-013):** bloqueado por infra DEX inexistente. Amenazas AX-1 (evidencia de 6 meses + survivorship de venues; exige ventana multi-año + riesgo smart-contract/puente) y AX-2 (hereda AC-1/3/5/7/8/11 + riesgo on-chain). No ejecutable hoy.
- **ILLIQ prima de iliquidez (F1-020):** bloqueado por universo amplio + delistados (Data Lake; conecta con `ILLIQ-MR-001`). Amenazas AI-1 (survivorship al alza — sin delistados, sesgada por construcción) y AI-2 (confound tamaño en majors; control por tamaño obligatorio).

## 4. Handoff
Con la compuerta adversarial incorporada, el protocolo de carry queda listo para **F7** (priorización + mapa de complementariedad — donde se pesa la redundancia con H-001 y el bloqueo por Data Lake) y, tras ratificación del IP, como **pre-registro formal** de una hipótesis (candidata natural a H-XXX). Los bocetos y `ILLIQ-MR-001` esperan al Data Lake / C-002.

> **F6 CERRADA 2026-07-23** — A-04 CONFORME (`F6_DICTAMEN_A04.md`, verificados los 10 aspectos del IP) + aprobación del IP. La contradicción C-001 (etiquetas AC-11/14/15) se resolvió alineando MD↔JSONL (todas → PRUEBA; 16 = 11 pruebas + 5 limitaciones). **F7 (priorización + cola) desbloqueada.**
