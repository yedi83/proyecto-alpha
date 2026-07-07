# Nota interpretativa de exp-004 (2026-07-06)

> No modifica `RESULTADO.md` ni el criterio pre-escrito: ambos quedan tal como se corrieron. Esta nota añade la lectura honesta por encima del veredicto mecánico.

## El criterio pre-escrito falló — se registra tal cual

384 dio net −8.6% y alpha −28.6% → por la regla que pre-registramos ("net≤0 o alpha≤0 en un vecino = MATA"), el script marca **MATADA**. No se toca. Un vecino a priori razonable (384) pierde dinero: eso es una falla de robustez real.

## Pero el patrón NO es el que el criterio buscaba

El criterio binario fue diseñado para cazar un **pico aislado** (sobreajuste: 512 alto con AMBOS vecinos derrumbados). Lo que hay es distinto — **monótono**: 384 (Calmar −0.34) < 512 (1.35) < 640 (1.74). Es un **efecto umbral**: el edge (si existe) vive en canales largos y 384 está por debajo del umbral. Esto es una **limitación de mi diseño del criterio** (demasiado crudo para distinguir pico de umbral), no un rescate de la hipótesis.

## Lectura honesta, en las dos direcciones

- El lado de **canal largo (512 y 640) es consistente y positivo** en las tres ventanas. 640 incluso mejor. La consistencia que el investigador percibía es real.
- 512 **no es óptimo** (640 lo supera), pero se eligió **a ciegas**, sin optimizar el largo → no hay sesgo de curva en ese eje.
- **Regla que se mantiene:** NO re-optimizar (no cambiar 512 por 640 porque "ganó más"). Eso sería mover los postes.
- El **sesgo de selección** de la cesta es **mínimo** (solo NEAR se probó y rechazó; los 5 son majors a priori). Corrige una sobre-afirmación previa de la sesión.

## El concern real que queda

No es el largo del canal — es la **significancia**. Sharpe 0.42, alpha **no significativa** (t=0.94). Con estos datos **no se puede distinguir edge de suerte**.

## Estado de H-001

**Prometedora pero NO probada.** No muerta, no vindicada. Siguiente evidencia: exp-005 (fuera de muestra limpio con HYPE) y, como árbitro final, **forward sobre precios reales** con universo fijo. No quitar lados ni monedas por lo visto en backtest.
