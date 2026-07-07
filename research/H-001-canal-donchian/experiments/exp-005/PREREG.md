# exp-005 — PRE-REGISTRO (fuera de muestra por activo + descomposición largo/corto)

Fecha: 2026-07-06 (ANTES de correr). Familia: **generalización OOS**. Distinta de riesgo (002/003) y de lookback (004).

## Objetivo

¿El edge del canal 512 **generaliza** a monedas que el diseño NUNCA tocó? Se aplica la regla congelada, sin cambiar nada, a monedas fuera del universo original.

- **HYPEUSDT** = test **LIMPIO** (nunca se miró al construir la cesta). Es el juez.
- **NEARUSDT** = **CONTAMINADO** (se probó y se rechazó para la cesta) → solo contexto, no evidencia.
- **BTC/ETH/SOL/BCH/DOGE** = referencia **dentro de muestra** (los 5 originales, majors a priori).

## Reglas (congeladas)

512/256, riesgo uniforme 0.001, mecánica idéntica a exp-002/004. Cada moneda **standalone** (no cesta). Tres modos: **combinado / solo-largo / solo-corto**. Ventanas: "full" (rango propio de cada moneda) y "2426" (2024-07-05 → 2026-06-21, común a todas, incl. HYPE que solo tiene ~2 años). Slippage de las nuevas (NEAR/HYPE) = 0.0004 (conservador, = DOGE).

## Criterio de decisión — PRE-ESCRITO, en plano, sobre HYPE (el único limpio)

- **GENERALIZA / apoya el canal:** HYPE combinado con **net > 0 y alpha > 0** (le gana a comprar-y-aguantar) en su ventana disponible.
- **NO GENERALIZA / bandera:** HYPE con **net ≤ 0 o alpha ≤ 0**.
- **Límite honesto declarado:** n = 1 moneda, ~2 años. Es **orientativo, no definitivo**. Este resultado NO cierra H-001 en ningún sentido — suma o resta **un** dato a la pregunta de si el edge es real o suerte.

## Largo / corto

Descriptivo: sirve para **entender** qué aporta cada lado. **NO** se decide quitar el corto (ni nada) a partir de esto — eso exigiría su propia hipótesis, razón económica y prueba aparte.

## Nota de gobernanza

El árbitro **limpio y definitivo** sigue siendo el tiempo hacia adelante sobre **precios reales**, con universo fijo decidido de antemano (no volver a elegir ganadores). exp-005 es un sanity check histórico, lo mejor disponible hoy sin esperar.
