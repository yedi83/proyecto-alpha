# Datos

> Fuentes, calidad y sesgos conocidos. Ningún dato entra a investigación o ejecución sin pasar por aquí.

## Fuentes actuales

| Dato | Fuente | Frecuencia | Estado |
|---|---|---|---|
| Velas (OHLCV) perp USDT | Binance API | PENDIENTE (timeframe usado por H-001) | PENDIENTE documentar |
| Funding rates | Binance API | 8h | PENDIENTE documentar |
| Universo de pares | PENDIENTE | — | PENDIENTE |

## Sesgos conocidos y su tratamiento

| Sesgo | Riesgo | Tratamiento actual |
|---|---|---|
| Survivorship (pares delistados excluidos) | Alto: infla resultados de backtest | 🔴 PENDIENTE — declarar si el universo de H-001 incluyó pares delistados |
| Lookahead (velas/funding desalineados temporalmente) | Alto: alfa falsa | PENDIENTE — documentar la auditoría de alineación |
| Cambios de reglas del exchange (tick size, límites, delistings) | Medio | PENDIENTE |
| Huecos y duplicados en velas | Medio | PENDIENTE — describir la validación del backtester |

## Reglas

1. Los datos crudos son inmutables: se versionan, nunca se corrigen in place.
2. Toda transformación es reproducible por script (nada manual).
3. El universo de cada backtest queda registrado en la ficha de la hipótesis (lista exacta de pares y período).
4. Los datos locales viven en `data/` y **no se versionan en git**; los scripts para regenerarlos, sí.

## Data Lake (planificado)

Ver `ROADMAP.md` §3. Requisitos mínimos: recolección automatizada, inclusión de delistados, QA de integridad, almacenamiento versionado.
