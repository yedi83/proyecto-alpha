# DIARIO DE INCIDENCIAS — Fase B (demo trading)

Inicio: 2026-07-14 15:13:16 UTC (ver PREREG_FASE_AB.md, ENMIENDA 1 + acta de inicio de Fase B).
Mismas reglas que el diario de Fase A: una fila por dia aunque no haya incidencias;
las incidencias se cruzan con eventos.csv y bot.log; ninguna queda sin causa al cierre.
Vigilancia especifica de B: fees > 0 en cada trade (B-fix2), fills con precio real
(B-fix1; evento `orden/precio_aprox` = investigar), funding real al cierre, TE vs ±5%,
slippage, y señales BTC con notional < $100 (omision simulada de produccion).

| Fecha | ¿Incidencias? | Descripcion | Accion |
|---|---|---|---|
| 2026-07-14 | Hito — INICIO | Corte 15:13:16 UTC. Frontera aplicada (ENMIENDA 1): bot de frontera (4 fixes validados en ensayo), keys demo, EQUITY_CAP=750, DRY_RUN=false. Arranque limpio: demo=True, mapa de riesgo OK, cuenta isolated 2x, eq=750, abiertas=0; posicion paper ETH de Fase A limpiada por reconciliacion (esperado). Ensayo detenido y su cuenta aplanada; paper_real sigue. Fase A cerrada APROBADA 6/6 el mismo dia. | Pendientes: auditar el primer trade end-to-end cuando ocurra (precio real, fees>0, funding); adaptar la auditoria programada a metricas de B. |
