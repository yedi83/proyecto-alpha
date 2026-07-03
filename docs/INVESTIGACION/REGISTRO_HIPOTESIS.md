# Registro de Hipótesis

> Append-only. Toda hipótesis que entra al pipeline se registra aquí y nunca se borra. Las rechazadas valen tanto como las validadas.

| ID | Nombre | Familia | Pre-registro | Etapa actual | Veredicto | Notas |
|---|---|---|---|---|---|---|
| [H-001](hipotesis/H-001-canal-donchian.md) | Canal de Donchian 512, perp USDT | Trend following | ✅ Original 2026-06-24, previo al backtest | Fase A (iniciada 2026-07-02, acta) | ⏳ EN VALIDACIÓN | Caso de prueba de la plataforma; veredicto de investigación: diversificador plausible, NO edge probado |

## Nota sobre H-001 (corregida 2026-07-02 tras inventario del lab original)

La nota anterior de esta sección afirmaba que H-001 tenía "pre-registro retroactivo". **Era incorrecta**: el inventario de `donchian512_lab` (ver `docs/MIGRACION.md`) encontró un pre-registro real del 2026-06-24 — parámetros congelados antes de correr, criterios de éxito y predicción del investigador registrada (y luego falsada y documentada) — más un PREREG propio de las Fases A/B escrito antes de acumular datos. Los originales están migrados en `research/H-001-canal-donchian/prereg/`. Se conserva esta corrección visible en cumplimiento de la regla append-only.

## Familias de hipótesis previstas

Trend following · Momentum · Carry/Funding · Relative strength · Mean reversion · Regímenes de mercado.

Cada nueva hipótesis toma el siguiente ID disponible (H-002, H-003, …) sin importar su familia.
