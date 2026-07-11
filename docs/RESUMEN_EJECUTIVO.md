# Resumen Ejecutivo — Proyecto Alpha

> Corte: 2026-07-10, cierre de la fase de arquitectura. Cubre el laboratorio original (`donchian512_lab`, junio 2026) y el repositorio `proyecto-alpha` (julio 2026).
>
> No confundir con: `research/H-001-canal-donchian/report/legacy/INFORME_EJECUTIVO.md` (informe del lab de junio, solo H-001, congelado como registro histórico — no se actualiza) ni `report/resumen_instancias_2026-07-10.md` (foto operativa de las 3 instancias). Este documento es la síntesis viva de TODO el proyecto y es el único que se actualiza en hitos mayores.

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

## Estado operativo (2026-07-10)

| Instancia | Modo | Rol | Estado |
|---|---|---|---|
| Lab (donchian512_lab) | DRY sobre feed testnet | **Fase A oficial** (acta 2026-07-02, PREREG propio) | Día 8/10; 11 trades, +$3.43; instrumentación limpia; cierre elegible **2026-07-12** |
| Ensayo B (ensayo_faseB) | Órdenes reales en demo | Depurar código de frontera — no evidencia | **Validó los 4 fixes**: fees de fills 10/10, cero fills sin precio, BTC con riesgo 0.125% |
| paper_real | Paper sobre feed real mainnet | Comparador de feed + forward de señal (PREREG propio) | Corriendo; feed real ~0.9 velas atrasadas/día/símbolo vs 1.5-2.2 de los feeds de prueba |

**Decisiones cerradas por experimento:** riesgo BTC 0.15% RECHAZADO (exp-002) y 0.125% ACEPTADO (exp-003, pre-registrado como intento final, N=2 declarado) — capital B/C $750. **Hallazgos que evitaron daño:** Binance retiró el testnet de futuros (F0 → migración a demo trading), `create_order` devuelve precio None y fees solo en fills (2 bugs corregidos en el bot de frontera antes de operar), min_notional demo $50 vs mainnet $100 (métrica de brecha creada).

## Próximos hitos

1. **2026-07-12:** replay offline + 6 criterios del PREREG = cierre de Fase A (+ primera revisión de la Teoría).
2. **Día D (si A aprueba):** checklist de 9 pasos → Fase B en demo, 1 mes (TE ±5%, slippage ≤5 bps de exceso).
3. **Paralelo ≤30%:** dictamen A-04 sobre F0 → apertura C-001 → F1 (mapeo con Sonnet + web).
4. **Tras B:** Fase C con capital real mínimo, previa RISK_POLICY completa (criterio de retiro, kill duro/blando).
5. **La prueba de fuego de la tesis:** que H-002 cueste una fracción de lo que costó H-001.

## El criterio de éxito vigente (del Investigador Principal)

El C-001 — y el laboratorio — se juzgan por una sola cosa: *producir decisiones metodológicas respaldadas por evidencia, incluso cuando esa evidencia contradiga las expectativas previas.* Ya ocurrió tres veces (0.15% rechazado, crisis-alpha falsada, predicción original fallada y documentada). Ese historial, no el PnL, es el activo.
