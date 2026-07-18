# Estado del Proyecto

> Única fuente de verdad del estado. Última actualización: 2026-07-16.

## Fase actual

Reestructuración del proyecto sobre esta base documental + validación operativa de H-001 (Canal de Donchian).

## Componentes

| Componente | Estado | Notas |
|---|---|---|
| Motor de backtesting | 🔄 Existe — pendiente de migración | Código funcional en repo/carpeta anterior. Migrar a `backtester/` con tests. |
| Bot de ejecución | 🔄 Existe — pendiente de migración | Migrar a `bot/`. Documentar en RUNBOOK.md durante la migración. |
| Dashboard de auditoría | 🔄 Existe — pendiente de migración | Migrar a `dashboard/`. |
| Data Lake | 📋 Planificado | Ver ROADMAP. Prerrequisito de toda investigación futura. |
| QA / validación de datos | 📋 Planificado | Incluye tratamiento de pares delistados. |
| Motor de régimen | 📋 Planificado | Solo investigación descriptiva en los próximos 12 meses. |
| Asignación de capital / portafolio | 📋 Planificado | Necesario a partir de la segunda estrategia validada. |
| Capa de abstracción de exchange | 📋 Planificado | Hoy el bot está acoplado a Binance. |

Leyenda: ✅ operativo y verificado en este repo · 🔄 existe fuera de este repo, pendiente de migración · 📋 planificado, no existe.

**Regla:** ningún componente se marca ✅ sin enlace a su evidencia (tests en verde, informe de validación, o log auditado).

## Hipótesis en el pipeline

| ID | Nombre | Etapa | Veredicto |
|---|---|---|---|
| [H-001](INVESTIGACION/hipotesis/H-001-canal-donchian.md) | Canal de Donchian 512 (perp USDT) | Fase A APROBADA 6/6 (07-14). Fase B: corte del 07-14 **COMPROMETIDO** (contaminación: ensayo con keys idénticas operó la misma cuenta demo → doble bot). **RE-CORTE limpio 2026-07-16, corte 15:27:33 UTC** (`fase_B/ACTA_RECORTE_2026-07-16.md`): keys del ensayo neutralizadas, cuenta aplanada, tarea `faseB_donchian` (python directo, IgnoreNew), datos 07-14→16 anulados, reloj de 1 mes reiniciado. Corriendo: demo, eq=750, abiertas=0. **Estatus epistemológico: CUESTIONADA (ADR-0006, 07-17)** — exp-004 disparó letal de lookback y el override por nota se formalizó retroactivamente; **exp-008 CUMPLIDO EN R0 (07-17):** funding real mejora todas las ventanas (dataset APTO A-02, hashes congelados, paridad OK) → la mayor incógnita declarada de H-001 se cierra A FAVOR, **sujeto a ratificación del ADR-0006** (Propuesta v2 tras dictamen A-04 NO CONFORME del 07-18: 6 violaciones verificadas y remediadas — ficha al día, exp-005 cubierta, enmienda constitucional propuesta; pendiente re-arbitraje + ratificación del IP) | ⏳ En validación — **Fase B corriendo · CUESTIONADA; DECISIÓN DEL IP (07-18): ADR-0006 RECHAZADO → ADR-0007 "acto fundacional" encargado a sesión nueva (encargo en docs/ADR/ADR-0007_ENCARGO.md: reconocimiento sin matices, nulidad de las notas, nueva doctrina, retroactividad prohibida para siempre). Sin efectos hasta CONFORME + ratificación** |
| [H-002](INVESTIGACION/hipotesis/H-002-ruptura-bnb-d1.md) | Ruptura Donchian(20)+SMA200, diario, **solo largos** (majors) | **Banco APROBADO — confianza moderada** (2026-07-14, suite T1-T5 pre-registrado) → **forward en paper** multi-activo desde 07-15 (testigo, base + variante etiquetada). Hipótesis económica + ficha registradas 07-16. **Sin fase operativa formal** | ⏳ En paper/forward — overlay de tendencia reductor de DD, **no probado** (n=57); decisión de fase tras cerrar C-001 |

## Deuda documental abierta

- [ ] Completar los números de `RISK_POLICY.md` (hoy tiene campos PENDIENTE).
- [x] Criterios de Fase A: resuelto por enmienda de gobernanza — la fase en curso se rige por el PREREG original del lab (ver `CRITERIOS_FASES.md`).
- [x] Informe honesto de H-001: las 5 preguntas respondidas con evidencia en la ficha (2026-07-02, tras inventario del lab).
- [x] Inventario del código existente: `docs/MIGRACION.md`.
- [x] `DATA.md` completado con el inventario (2026-07-03): fuentes verificadas en código, sesgos con tratamiento, requisitos del Data Lake.
- [x] `RISK_POLICY.md` completado (2026-07-03): límites transcritos del sistema vivo; pendientes de Fase C marcados (criterio de retiro, kill duro vs. blando).
- [x] Test de sensibilidad 384/512/640: **verificado que NO se ejecutó** (solo listado como test futuro en VEREDICTO.md). Decisión de hacerlo o no → antes de Fase C.
- [ ] Copiar scripts de investigación y CSV pequeños a `research/H-001-canal-donchian/` (sin tocar el sistema vivo).
- [x] `docs/CONTRATOS.md` (tarea 0.4, 2026-07-03): cinco contratos codificados desde las convenciones del sistema vivo. **Con esto la Etapa 0 del PLAN_TRABAJO queda CERRADA.**
- [ ] QA de los CSV del cache (huecos/duplicados por símbolo) — primera tarea de A-02.
- [ ] Migrar bot y observabilidad al repo **solo al cerrar la Fase A** (regla maestra de MIGRACION.md).
- [x] Fontanería ejecutada (2026-07-03): informe en `fase_B/`. Descubrió 2 bugs pre-B del bot (fill price None en create_order; fees solo en fills) además de F0. Los 4 cambios de frontera consolidados en `fase_B/PAQUETE_FASE_B.md`.
- [x] **Decisión M1 registrada:** capital B/C = $750 con riesgo BTC 0.15% (resto 0.10%), **condicionada al exp-002** (cesta 2021-26 con riesgo por símbolo; si degrada, se revisa). Métrica nueva de B: "omisión simulada de producción" (señal BTC con notional < $100 mainnet, aunque el demo la ejecute con su mínimo de $50).
- [x] **exp-002 ejecutado (2026-07-03): RECHAZA** BTC 0.15% (Calmar 84.6% < 85%; paridad con frontera verificada al centavo).
- [x] **exp-003 ejecutado (2026-07-03): ACEPTA** BTC 0.125% (pre-registrado como intento final, N=2 declarado; Calmar 91.8%, Sharpe −0.016). M1 resuelto: $750, riesgo BTC 0.125%. Caveat: margen de volatilidad ~13% — habrá omisiones BTC en picos de ATR.
- [ ] Riesgo vigilado: si Binance apaga el feed testnet a mitad de Fase A, bot y replay pierden velas a la vez (incidente detectable, no corrupción silenciosa).
- [x] **Vigía (Nivel 1) operativo** (2026-07-04): tarea `vigia_donchian` (schtasks cada 15 min, ruta completa al `pythonw` del venv). `bot/logs/vigia.log` escribe `OK` a cadencia. H2 cerrado.
- [x] **Ensayo general de Fase B arrancado** (2026-07-04, `ensayo_faseB/`): bot de frontera con órdenes reales en la cuenta demo, aislado, NO-evidencia. Montaje OK, keys demo corregidas (−2014/−1022 resueltos), conecta con `eq=750`, una sola instancia. Auto-reinicio (`bot/lanzar_ensayo.bat`) + tarea `ensayo_faseB_lanzador` (arranque al iniciar sesión). Se detiene al arrancar la B oficial. **Validación completada (2026-07-10):** 10 trades con fees>0 (10/10), cero fills sin precio, cero eventos `precio_aprox`, BTC operando con su mapa de riesgo — los 4 fixes de frontera funcionan.
- [x] **paper_real documentado** (`research/H-001-canal-donchian/paper_real/`, corre desde ~07-07 con PREREG propio del 07-07): bot de frontera en paper sobre feed REAL de mainnet, sin keys (verificado), cero órdenes. Rol: comparador de feed y forward de captura de señal — insumo de la decisión de Fase C, NO evidencia de A/B. Pendiente del humano: erratum fechado en su PREREG (declara riesgo 0.1% uniforme; el código corre RISK_MAP con BTC 0.125%).
- Resumen de las 3 instancias al día 8: `research/H-001-canal-donchian/report/resumen_instancias_2026-07-10.md`.
