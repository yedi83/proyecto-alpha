# F1 — Mapeo sistemático estilo PRISMA — Catálogo crudo — Ciclo C-001

> **Fecha: 2026-07-20 · Ejecutor: Sonnet (Claude, vía búsqueda web) · Fase: F1 — Mapeo (ORQUESTADOR §F1)**
> Fuente de verdad: `F1_catalogo.jsonl` (30 registros, uno por línea, esquema de la regla dura 9 del ORQUESTADOR). Este documento es una VISTA generada desde el JSONL, no al revés.
> Ejecución: ejecutor puro conforme F0 — no se evaluó, concluyó, priorizó ni comparó nada más allá de los criterios de exclusión de F0 §2. No hay puntuaciones, rankings ni veredictos de validación en este documento.

## Notas obligatorias de alcance

1. **La asignación de `mecanismo`/`familia` en cada entrada es PROVISIONAL.** F2 (árbol genealógico) la confirma, corrige o reagrupa por herencia de evidencia. Ninguna cifra de "nivel de evidencia" de este documento debe leerse como veredicto final: es una etiqueta preliminar por FUENTE INDIVIDUAL, no por edge consolidado (eso lo hace F2/F3).
2. **Esto NO es priorización ni validación.** No hay pesos, scoring ni comparación entre entradas. La priorización es F7; la validación empírica es el pipeline PIC (backtest → OOS/WF → lockbox) tras el pre-registro humano. F1 solo cataloga literatura.
3. Conforme a la jerarquía de F0 §4, la evidencia NO se promedia entre niveles y cada entrada individual recibe el nivel máximo que alcanza por sí sola (mayormente III/IV/V a nivel de fuente individual; los niveles I-II, que requieren múltiples estudios independientes, se resuelven en F2/F3 al consolidar por edge).
4. Todas las afirmaciones cuantitativas citadas (t-stats, rangos de fechas, tamaños de muestra) provienen de los resúmenes/abstracts verificados por búsqueda web de cada fuente — no son cálculos de este ejecutor (regla dura 2 del ORQUESTADOR: auditar, no calcular).

---

## Tabla-resumen

| id | mecanismo | familia | variante (resumen) | nombre | fuente | nivel | verificada |
|---|---|---|---|---|---|---|---|
| F1-001 | Persistencia | Trend following / TS momentum | TSM 1-12m multi-activo | Time Series Momentum | Moskowitz, Ooi & Pedersen (2012), JFE | III | ✅ |
| F1-002 | Persistencia | Trend following / TS momentum | Replicación multi-siglo 1880-2016 | A Century of Evidence on Trend-Following | Hurst, Ooi & Pedersen (2017), JPM | III | ✅ |
| F1-003 | Persistencia | Trend following / TS momentum | Replicación dos siglos 1800-2013 | Two Centuries of Trend Following | Lempérière et al. (2014), arXiv/CFM | IV | ✅ |
| F1-004 | Persistencia | Trend following / TS momentum | Replicación vía CTAs 1978-2012 | Momentum Strategies in Futures Markets... | Baltas & Kosowski (2013), SSRN | IV | ✅ |
| F1-005 | Persistencia | Trend following / TS momentum | Equivalencia TSM ≡ MA-crossover | Which Trend Is Your Friend? | Levine & Pedersen (2016), FAJ | III | ✅ |
| F1-006 | Persistencia | Trend following / TS momentum | SMA 10 meses, TAA | A Quantitative Approach to Tactical Asset Allocation | Faber (2007), J. of Wealth Mgmt | III | ✅ |
| F1-007 | Persistencia | Trend following / TS momentum | Ruptura canal 20/55d | Donchian Channel / Turtle Rules | Donchian/Dennis-Eckhardt; Faith (2007), libro | V | ✅ |
| F1-008 | Prima de riesgo | Carry / funding | Composite multi-activo | Carry | Koijen, Moskowitz, Pedersen & Vrugt (2018), JFE | III | ✅ |
| F1-009 | Prima de riesgo | Carry / funding | Base perpetuos cripto vs. spot | Crypto Carry | Schmeling, Schrimpf & Todorov (2023), BIS WP/Mgmt Sci | III | ✅ |
| F1-010 | Prima de riesgo | Carry / funding | Marco no-arbitraje perpetuos | Fundamentals of Perpetual Futures | He, Manela, Ross & von Wachter (2022), SSRN/arXiv | IV | ✅ |
| F1-011 | Prima de riesgo | Carry / funding | Precio de anclaje estocástico | Perpetual Futures Pricing | Ackerer, Hugonnier & Jermann (2025), Math. Finance | III | ✅ |
| F1-012 | Prima de riesgo | Carry / funding | Funding como regla de feedback | Funding Rate Mechanism in Perpetual Futures | Zhang (2026), SSRN | IV | ✅ |
| F1-013 | Prima de riesgo | Carry / funding | Arbitraje funding CEX/DEX | Exploring Risk and Return Profiles... | Werapun et al. (2025), Blockchain: Research & Applications | III | ✅ |
| F1-014 | Sobre-reacción | Mean reversion | Reversión 3-5 años | Does the Stock Market Overreact? | De Bondt & Thaler (1985), JF | III | ✅ |
| F1-015 | Sobre-reacción | Mean reversion | Reversión mensual | Evidence of Predictable Behavior of Security Returns | Jegadeesh (1990), JF | III | ✅ |
| F1-016 | Sobre-reacción | Mean reversion | Autocorrelación cruzada | When Are Contrarian Profits Due to Overreaction? | Lo & MacKinlay (1990), RFS | III | ✅ |
| F1-017 | Sobre-reacción | Mean reversion | Reversión 1 día, cripto | Up or down? Short-term reversal... crypto | Zaremba et al. (2021), IRFA | III | ✅ |
| F1-018 | Sobre-reacción | Mean reversion | Momentum corto / reversión largo, cripto | Cryptocurrency Momentum and Reversal | Dobrynskaya (2023), J. Alt. Investments | III | ✅ |
| F1-019 | Microestructura | Order flow / liquidez | Modelo insider/noise/MM | Continuous Auctions and Insider Trading | Kyle (1985), Econometrica | III | ✅ |
| F1-020 | Microestructura | Order flow / liquidez | Medida ILLIQ | Illiquidity and Stock Returns | Amihud (2002), J. Financial Markets | III | ✅ |
| F1-021 | Microestructura | Order flow / liquidez | Order Flow Imbalance (OFI) | The Price Impact of Order Book Events | Cont, Kukanov & Stoikov (2014), JFEc | III | ✅ |
| F1-022 | Microestructura | Order flow / liquidez | VPIN, toxicidad de flujo | Flow Toxicity and Liquidity in a High-Frequency World | Easley, López de Prado & O'Hara (2012), RFS | III | ✅ |
| F1-023 | Microestructura | Order flow / liquidez | OFI en exchanges cripto centralizados | Order Flow Impact and Price Formation in Centralized Crypto Exchanges | Alexander, Heck, Kaeck & Riordan (2024), SSRN | IV | ✅ |
| F1-024 | Microestructura | Order flow / liquidez | Order flow internacional → retornos cripto | Order Flow and Cryptocurrency Returns | Anastasopoulos et al. (2026), J. Financial Markets | III | ✅ |
| F1-025 | Microestructura | Order flow / liquidez | Informatividad de trade flow, Bitcoin LOB | Trade Informativeness and Liquidity in Bitcoin Markets | Westland (2021), PLOS ONE | III | ✅ |
| F1-026 | Régimen | HMM/regímenes (FILTRO) | Markov-switching 2 estados | A New Approach to the Economic Analysis of Nonstationary Time Series | Hamilton (1989), Econometrica | III | ✅ |
| F1-027 | Régimen | HMM/regímenes (FILTRO) | Regímenes en tipos de interés | Regime Switches in Interest Rates | Ang & Bekaert (2002), JBES | III | ✅ |
| F1-028 | Régimen | HMM/regímenes (FILTRO) | Asignación condicionada a régimen HMM | Dynamic Portfolio Optimization Across Hidden Market Regimes | Nystrup, Madsen & Lindström (2018), Quant. Finance | III | ✅ |
| F1-029 | Régimen | HMM/regímenes (FILTRO) | MS-GARCH + Copula HMM, volatilidad BTC | Regime-Switching in Bitcoin Volatility Under Global Uncertainty | Shakourloo & Azimli (2026), RIBF | III | ✅ |
| F1-030 | Régimen | HMM/regímenes (FILTRO) | MCMC bayesiano + HMM, régimen de precio BTC | Bitcoin Price Regime Shifts | Paulavičius (2025), Mathematics | III | ✅ |

**30/30 fuentes verificadas por búsqueda web (100%).** Ninguna entrada lleva el tag `[memoria del modelo — verificar]`. Una observación puntual (estatus de publicación en journal de F1-023, aún working paper SSRN) queda anotada para seguimiento en F2/F3. La autoría de F1-030 (Paulavičius, R.) fue confirmada vía metadatos MDPI (DOI 10.3390/math13101577) el 2026-07-20 — corrección de consistencia del dictamen A-04 (C-001).

---

## Desglose por familia (conteo de entradas del catálogo)

| Familia | Nº entradas | Niveles presentes |
|---|---|---|
| Persistencia — Trend following / TS momentum | 7 (F1-001 a F1-007) | III ×4, IV ×2, V ×1 |
| Prima de riesgo — Carry / funding | 6 (F1-008 a F1-013) | III ×4, IV ×2 |
| Sobre-reacción — Mean reversion | 5 (F1-014 a F1-018) | III ×5 |
| Microestructura — Order flow / liquidez | 7 (F1-019 a F1-025) | III ×5, IV ×2 |
| Régimen — HMM (filtro/condicionador) | 5 (F1-026 a F1-030) | III ×5 |
| **Total** | **30** | |

Nota: "Persistencia" se cataloga con profundidad reducida respecto a las demás familias porque F0 §2 la marca como REFERENCIA (H-001 ya en pipeline) y no como objeto de re-investigación — las 7 entradas documentan el linaje canónico (TSM académico, replicaciones independientes, variantes de practicante) sin agotar la literatura.

---

## Flujo PRISMA (adaptado a revisión bibliográfica cuantitativa)

```
Fuentes candidatas IDENTIFICADAS mediante búsqueda web
(24 consultas de búsqueda ejecutadas sobre las 5 familias EN ALCANCE de F0 §2)
        │  ~70 títulos distintos localizados (tras deduplicar resultados
        │  repetidos entre consultas)
        ▼
CRIBADAS por pertinencia temática a una de las 5 familias EN ALCANCE
        │  Excluidas en la criba (duplicados, blogs sin sustancia verificable,
        │  resultados no pertinentes al mecanismo buscado, o secundarios a una
        │  fuente ya incluida): ~34
        │  Excluidas EXPLÍCITAMENTE por criterio de F0 §2 ("Fuera del Ciclo 1"),
        │  con al menos un ejemplo real localizado durante la búsqueda y
        │  descartado a propósito (no incluido en el JSONL, solo anotado aquí):
        │    - Momentum cross-sectional completo → Jegadeesh & Titman (1993),
        │      JF 48(1):65-91 ("Returns to Buying Winners and Selling Losers"):
        │      localizado en la búsqueda de persistencia, EXCLUIDO por ser
        │      momentum de corte transversal (no TS momentum), anexo sin
        │      profundizar conforme F0 §2.
        │    - Arbitraje estadístico multi-venue → Makarov & Schoar (2020),
        │      JFE, "Trading and Arbitrage in Cryptocurrency Markets":
        │      localizado en la búsqueda de microestructura cripto, EXCLUIDO
        │      por ser arbitraje entre exchanges, anexo sin profundizar.
        │    - Estacionalidad, convexidad/opciones, on-chain, market making
        │      activo: 0 candidatas registradas — no se buscaron
        │      deliberadamente, coherente con la exclusión de F0 §2.
        ▼
INCLUIDAS en el catálogo estructurado (F1_catalogo.jsonl)
        │  30 entradas, 30/30 verificadas por búsqueda web
        ▼
      F2 (árbol genealógico por mecanismos) — próxima fase
```

Los conteos de "identificadas" y "cribadas" son estimaciones honestas del propio proceso de búsqueda ejecutado en esta sesión (24 llamadas de búsqueda web), no un recuento exhaustivo de universo bibliográfico — coherente con el carácter de "primera pasada" pedido para F1. No se declara aquí ninguna exhaustividad: F1 es mapeo, no meta-análisis.

---

## Advertencias de alcance (para lectura de F2 en adelante)

- **Nivel de evidencia por fuente, no por edge.** Varias entradas documentan el MISMO mecanismo (p. ej. F1-001/002/003/004 son todas TS momentum). F0 §4 prohíbe promediar niveles, pero SÍ permite que el volumen de estudios independientes en un mismo nivel eleve la clasificación consolidada del edge — esa consolidación es tarea de F2 (herencia) y F3 (auditoría de robustez), no de este documento.
- **Casos frontera marcados, no resueltos.** F1-018 (Dobrynskaya) documenta momentum de corto horizonte y reversión de horizonte largo en el MISMO activo cripto — se deja anotado como caso dudoso entre las familias "Persistencia" y "Sobre-reacción" para que F2 decida su ubicación, sin forzarlo aquí.
- **Régimen es FILTRO, no estrategia.** Las 5 entradas de F1-026 a F1-030 se documentan explícitamente como condicionador/filtro de otras señales, nunca como fuente de alfa autónoma — coherente con F0 §2 y con el ROADMAP del laboratorio (régimen solo descriptivo en 12 meses).
- **Microestructura probablemente "NO-VIAJA por datos hoy".** F1-021, F1-023 y parcialmente F1-022 requieren datos de libro de órdenes (nivel 2/3) que el laboratorio no tiene confirmados como disponibles; se incluyen a propósito, conforme la nota explícita de F0 §2, para alimentar las prioridades del Data Lake en fases posteriores.
- **Ningún número de este documento es un resultado de backtest ni una estimación de Sharpe/retorno.** Todas las cifras citadas (t-stats, rangos de muestra, tamaños de universo) son las reportadas por cada fuente original, auditadas por búsqueda web — no calculadas por este ejecutor (regla dura 2).

---

## Cierre de fase (pendiente, no autodeclarado)

Este documento y `F1_catalogo.jsonl` son el producto de F1 conforme al ORQUESTADOR (§Fases, fila F1) y a F0 §9 (cierre de fases). **El ejecutor no dictamina su propia conformidad.** El cierre formal de F1 requiere: dictamen A-04 (sesión separada, `F1_DICTAMEN_A04.md`) + aprobación del Investigador Principal, conforme a la Regla 10 del ORQUESTADOR (compuertas objetivas entre fases).
