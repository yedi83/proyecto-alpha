# Registro de Hipótesis

> Append-only. Toda hipótesis que entra al pipeline se registra aquí y nunca se borra. Las rechazadas valen tanto como las validadas.

| ID | Nombre | Familia | Pre-registro | Etapa actual | Veredicto | Notas |
|---|---|---|---|---|---|---|
| [H-001](hipotesis/H-001-canal-donchian.md) | Canal de Donchian 512, perp USDT | Trend following | ✅ Original 2026-06-24, previo al backtest | Fase A APROBADA (07-14) · Fase B corriendo (re-corte 07-16) | ⏳ EN VALIDACIÓN — **CUESTIONADA (ADR-0006)** | exp-004 disparó veredicto letal de robustez de lookback (07-06); override formalizado por ADR-0006 (07-17): criterio mal especificado para patrón monótono, sin re-optimizar. Alfa no significativa (t=0.94). **Fase C condicionada a exp-008-R0 + cero disparos letales nuevos; un 2º disparo letal = retiro operativo sin nota interpretativa.** |

## Nota sobre H-001 (corregida 2026-07-02 tras inventario del lab original)

La nota anterior de esta sección afirmaba que H-001 tenía "pre-registro retroactivo". **Era incorrecta**: el inventario de `donchian512_lab` (ver `docs/MIGRACION.md`) encontró un pre-registro real del 2026-06-24 — parámetros congelados antes de correr, criterios de éxito y predicción del investigador registrada (y luego falsada y documentada) — más un PREREG propio de las Fases A/B escrito antes de acumular datos. Los originales están migrados en `research/H-001-canal-donchian/prereg/`. Se conserva esta corrección visible en cumplimiento de la regla append-only.

## Familias de hipótesis previstas

Trend following · Momentum · Carry/Funding · Relative strength · Mean reversion · Regímenes de mercado.

Cada nueva hipótesis toma el siguiente ID disponible (H-002, H-003, …) sin importar su familia.
