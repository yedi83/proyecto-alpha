# Registro de Hipótesis

> Append-only. Toda hipótesis que entra al pipeline se registra aquí y nunca se borra. Las rechazadas valen tanto como las validadas.

| ID | Nombre | Familia | Pre-registro | Etapa actual | Veredicto | Notas |
|---|---|---|---|---|---|---|
| [H-001](hipotesis/H-001-canal-donchian.md) | Canal de Donchian 512, perp USDT | Trend following | ✅ Original 2026-06-24, previo al backtest | Fase A APROBADA (07-14) · Fase B corriendo (re-corte 07-16) | ⏳ EN VALIDACIÓN — **CUESTIONADA (ADR-0006)** | exp-004 disparó veredicto letal de robustez de lookback (07-06); override formalizado por ADR-0006 (07-17): criterio mal especificado para patrón monótono, sin re-optimizar. Alfa no significativa (t=0.94). **exp-008 (funding real, 07-17): R0 — ACEPTABLE** con paridad OK y dataset APTO de A-02 (hashes congelados): el funding real 2021-26 MEJORA todas las ventanas vs. el modelo pesimista (FULL: NET 27.3% vs 24.0%, Sharpe 0.47 vs 0.42; 2426: +4.6% vs +2.8%). La condición (i) del ADR-0006 queda CUMPLIDA → Fase C vuelve a depender del veredicto de Fase B + cero disparos letales nuevos (la cláusula del 2º disparo sigue vigente). |

## Nota sobre H-001 (corregida 2026-07-02 tras inventario del lab original)

La nota anterior de esta sección afirmaba que H-001 tenía "pre-registro retroactivo". **Era incorrecta**: el inventario de `donchian512_lab` (ver `docs/MIGRACION.md`) encontró un pre-registro real del 2026-06-24 — parámetros congelados antes de correr, criterios de éxito y predicción del investigador registrada (y luego falsada y documentada) — más un PREREG propio de las Fases A/B escrito antes de acumular datos. Los originales están migrados en `research/H-001-canal-donchian/prereg/`. Se conserva esta corrección visible en cumplimiento de la regla append-only.

## Familias de hipótesis previstas

Trend following · Momentum · Carry/Funding · Relative strength · Mean reversion · Regímenes de mercado.

Cada nueva hipótesis toma el siguiente ID disponible (H-002, H-003, …) sin importar su familia.
