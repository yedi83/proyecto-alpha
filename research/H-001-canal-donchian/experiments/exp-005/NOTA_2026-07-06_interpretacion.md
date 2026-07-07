# Nota interpretativa de exp-005 (2026-07-06)

> No modifica `RESULTADO.md` ni el criterio pre-escrito. Añade la lectura honesta.

## Mi criterio pre-escrito estaba mal diseñado

El criterio "HYPE con alpha > 0 (le gana a comprar-y-aguantar)" es **inadecuado** para esta prueba, y se demuestra **independiente del resultado de HYPE**: falla también en los majors dentro de muestra (BTC alpha −57%, SOL −115%). Si el criterio fuera bueno, BTC/SOL deberían pasarlo. No lo hacen.

Motivo: la estrategia arriesga 0.1%/trade — es de bajísima volatilidad (maxDD −3 a −10% vs −70%+ del buy&hold). Pedirle que gane en retorno bruto a aguantar un cripto que hizo +100% es absurdo; el signo del alpha lo decide si esa moneda subió o bajó, no la habilidad. **La lente correcta es el Sharpe, no el alpha.** (Segundo criterio mío que salió mal en la sesión; es limitación de mi diseño, no rescate de la hipótesis.)

## Lectura justa (por Sharpe)

- **HYPE (OOS limpio) combinado: Sharpe −1.12, pierde.** Solo-largo apenas +0.58% (Sharpe 0.26). Frente a los majors standalone (BTC 0.03, ETH 0.42, SOL 0.52, BCH 0.23, DOGE 0.18), HYPE queda al fondo. → **HYPE no muestra el edge.** Señal en contra de la generalización, pero **débil** (n=1, ~2 años, y hasta BTC standalone es casi plano).
- **Patrón en las 7 monedas: largo > corto sin excepción**; los cortos pierden casi siempre. Valida la intuición de "solo largos", PERO es casi seguro **deriva del toro cripto (beta), no skill** — un "solo largos" que gana porque el mercado subió no es un edge.

## Coherencia con lo ya sabido

Consistente con el veredicto de robustez: **por moneda el edge es débil; el objeto robusto es la CESTA como seguro convexo, no las monedas sueltas.** exp-005 no cambia el estado de H-001: no probada, baja convicción.
