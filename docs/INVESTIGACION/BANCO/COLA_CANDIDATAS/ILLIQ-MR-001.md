# ILLIQ-MR-001 / H-003 (candidata) — Reversión de corto plazo condicional a la iliquidez

> **Estado: CANDIDATA EN COLA (post-C-001) · prioridad de Data Lake · NO EJECUTAR.** Sin PREREG hasta definir el universo. Formalización solo en C-002, tras universo + pre-registro. **No modifica F4/F5 ni abre ADR** (decisión del IP, 2026-07-23).
> Origen: insight del IP (2026-07-23) tras revisión de literatura (Zaremba et al., >3.600 criptoactivos: reversión diaria en las menos líquidas, momentum diario en las grandes/líquidas). Consistente con lo que el Banco ya había marcado: frontera M2/M4 de ILLIQ (F2/F4), F1-017 condicionada por liquidez, y el veredicto de F5 (ILLIQ `viaja_con_condiciones`: requiere universo amplio; reversión `no_viaja` en majors porque se invierte a momentum). **El Banco no descarta M3: lo reconceptualiza como posible edge condicional.**

## Pregunta de investigación (abierta — sin narrativa comprometida)

¿El comportamiento del retorno de corto plazo en cripto (momentum vs. reversión) cambia de signo/magnitud según el nivel de iliquidez (Amihud ILLIQ)? Y —lo decisivo— si cambia: ¿es un **edge condicional cosechable**, o un **artefacto de microestructura/medición**?

## Precisión metodológica CENTRAL (IP): correlación ≠ causa

**NO asumir que ILLIQ causa la reversión.** El diseño debe **distinguir explícitamente**:
- relación causal/condicional (ILLIQ modula un edge de retorno real), frente a
- correlación espuria con **bid-ask bounce, stale prices, microestructura y sesgos de medición** — que producen reversión *mecánica en el precio medido*, no un edge operable.

**Null por defecto:** la reversión aparente en el quintil ilíquido es un **artefacto**. La carga de la prueba es demostrar que hay algo real y cosechable por encima de eso. Sin esta disciplina, el experimento nace comprometido con la conclusión que quiere encontrar.

## Compuertas de diseño (deben cumplirse, o no pasa)

1. **Cosechabilidad neta (compuerta dura):** el edge se juzga **neto de costes de impacto realistas por quintil de liquidez**. La misma iliquidez que crea la señal es la que la come al operarla; es plausible una reversión real y robusta en el quintil ilíquido que **no sea capturable tras impacto**. Bruto positivo pero neto ≤ 0 → no es edge, es un hecho estadístico.
2. **Controles de artefacto:** aislar bid-ask bounce (p. ej. saltar la vela de entrada / retornos con hueco / precios mid), excluir períodos de precio congelado (stale), y controlar microestructura. Si el "edge" desaparece al controlar artefactos → se declara artefacto.
3. **ILLIQ como variable de clasificación ROLLING, no etiqueta fija:** una moneda migra ilíquida→líquida→ilíquida; los quintiles se recalculan en cada fecha (nada de "esta moneda es ilíquida para siempre").
4. **Sin sesgo de supervivencia ni retrospectivo:** universo construido **históricamente** con las monedas que cumplían los criterios en cada fecha, **incluidos delistados**.
5. **OOS + réplica en distintos períodos.**

## Universo estratificado por liquidez (diseño del IP)

| Grupo | Característica | Propósito |
|---|---|---|
| A / Control | Muy líquidas (majors) | Comprobar si el efecto DESAPARECE / se invierte a momentum al subir la liquidez (no busca alfa) |
| B / Mid-cap | Líquidas, historial suficiente, sin precio congelado | Comparación |
| C / Small-cap líquidas | Menor volumen, mayor ILLIQ, aún negociables | **Zona de interés principal** |
| D / Extremadamente ilíquidas | — | **FUERA del test principal → solo análisis de sensibilidad** (alto riesgo de artefacto/manipulación/discontinuidad) |

## Marco conceptual (separar mecanismo de condicionador)

- **Mecanismo 1 — Mean reversion** (variable explicativa: retorno pasado extremo).
- **Mecanismo 2 — Iliquidez** (variable explicativa: Amihud ILLIQ).
- **Interacción — Mean Reversion × ILLIQ:** ¿ILLIQ modifica la magnitud o el **signo** del retorno predictivo? ¿Existe un **umbral de iliquidez** donde el comportamiento pasa de momentum a reversión?

Si la interacción es robusta y cosechable, el producto no es "otra estrategia de mean-reversion": es un **condicionador de régimen por liquidez** (cuándo esperar momentum vs. reversión).

## Prerequisito DURO: Data Lake (no existe hoy)

Exige una cesta cripto **amplia, histórica, estratificable por ILLIQ, con delistados y QA de integridad** — trabajo del Data Lake aún pendiente (ROADMAP). Correrlo sobre el universo actual (6 majors) o datos ad-hoc produciría **exactamente** los sesgos que esta ficha existe para evitar. → **Prioridad de Data Lake: universo amplio estratificable + pares delistados + QA.**

## Métrica de medición

Amihud ILLIQ (≈ media de |retorno| / volumen en $) es **computable con OHLCV+volumen, sin order book L2/L3** — encaja con los datos del laboratorio. (Ninguna medida de liquidez es perfecta; ILLIQ es razonable como clasificador. `[verificar en la literatura de medición de liquidez cripto al formalizar]`.)

## Qué NO es esto todavía

No es hipótesis formal (sin PREREG), no se ejecuta, no toca el universo actual, no modifica F4/F5, no abre ADR. Es una **candidata en cola** para el F7/C-002 del Banco que, solo tras definir universo + PREREG, podría convertirse en **H-003**.
