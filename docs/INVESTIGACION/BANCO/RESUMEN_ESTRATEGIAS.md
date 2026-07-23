# Las estrategias del Banco — resumen para leer con calma

> Escrito 2026-07-20 para lectura tranquila. Resume lo que el Banco de Mecanismos (fases F1→F3 del ciclo C-001) encontró en la **literatura académica** sobre 30 mecanismos de mercado. Lenguaje llano; los detalles técnicos están en `fases/F1_CATALOGO.md`, `F2_ARBOL.md` y `F3_EVIDENCIA.md`.

## Antes de nada: qué es esto y qué NO es

Esto es lo que **la ciencia publicada dice** sobre 30 formas de ganar dinero en los mercados. Es una **auditoría de papers**, no estrategias tuyas ni validadas. **Ninguna se ha probado con tus datos todavía.** La única que está en tu pipeline es **H-001 (Donchian)**; el resto son candidatas para el futuro. El Banco solo **audita y verifica fuentes** — tiene prohibido inventar números o decir "esto es rentable".

## Los niveles de evidencia (I a VII), en cristiano

Es una escala prestada de la medicina (donde se usa para clasificar cuánta confianza merece un tratamiento). Mide **cuánto respalda la ciencia a un fenómeno**, de más fuerte (I) a más débil (VII):

| Nivel | Qué significa |
|---|---|
| **I** | Replicación independiente en **muchos mercados y muchas décadas**. Lo más sólido que existe. |
| **II** | **Varios** papers independientes, revisados por pares, que coinciden. |
| **III** | **Un** paper sólido, revisado por pares. |
| **IV** | Working papers / backtests públicos y reproducibles (aún sin sello de revista). |
| **V** | Libros de practicantes reconocidos (p. ej. las reglas de las Turtle Traders). |
| **VI** | Blogs / foros técnicos. |
| **VII** | Opinión sin evidencia. |

**Tres cosas importantes para leerlos bien:**

1. **El nivel NO mide rentabilidad.** Mide *confianza en que el fenómeno existe*. Un edge nivel I puede dar poco dinero, y uno nivel V puede funcionar. No confundas "bien documentado" con "rentable".
2. **La evidencia no se promedia.** Mil blogs (VI) no suman un paper serio (III). Cada fuente lleva el nivel **máximo** que alcanza por sí sola.
3. **Los niveles I-II casi nunca los tiene un paper suelto** — emergen al *juntar* varios estudios independientes sobre el mismo edge. Por eso verás que casi todas las entradas están en III o IV: la fuerza real aparece cuando el mecanismo acumula réplicas (eso lo hará la fase F4).

## Las estrategias, por mecanismo (5 familias)

### 1) PERSISTENCIA (seguir la tendencia) — la mejor respaldada
**La idea:** los precios reaccionan *tarde* a la información, así que las tendencias siguen. Compras lo que sube. **Quién pierde al otro lado:** quien vende demasiado pronto por sesgo conductual.
- Time Series Momentum (Moskowitz, Ooi & Pedersen 2012) — **III**
- "Un siglo de evidencia" 1880-2016 (Hurst, Ooi & Pedersen 2017) — **III**
- "Dos siglos" 1800-2013 (Lempérière et al. 2014) — **IV**
- Replicación vía CTAs 1978-2012 (Baltas & Kosowski 2013) — **IV**
- "Donchian ≡ cruce de medias ≡ TSM son el mismo edge" (Levine & Pedersen 2016) — **III** (pieza clave: demuestra que son lo mismo)
- Media móvil de 10 meses (Faber 2007) — **IV**
- **Canal de Donchian / Turtle 20-55 días — V — ⭐ esta es la de tu H-001**

**Lo importante:** tu Donchian, como regla de libro, es nivel V (lo más flojo). **Pero hereda toda la evidencia de la persistencia** (multi-siglo, ≥5 grupos de investigación independientes) porque Levine-Pedersen probó que es el *mismo mecanismo* que el momentum académico. Es el mecanismo con más respaldo de todo el ciclo.

### 2) CARRY / PRIMA DE RIESGO — el más ligado a tu instrumento
**La idea:** el "carry" (lo que ganas si el precio no se mueve) te paga por asumir un riesgo. En perpetuos cripto, ese carry **es el funding**.
- Carry multi-activo (Koijen, Moskowitz, Pedersen & Vrugt 2018) — **III**
- Crypto Carry, base perp vs. spot (Schmeling, Schrimpf & Todorov 2023) — **III**
- Arbitraje de funding CEX vs. DEX (Werapun et al. 2025) — **III**
- *Teoría* del funding (por qué existe; no son estrategias): He et al. (IV), Ackerer et al. (III), Zhang (IV)

**Lo importante:** es el mecanismo más directamente conectado con tu setup (funding de perpetuos), justo lo que exp-008 ya midió en H-001. Candidato natural a próxima hipótesis.

### 3) SOBRE-REACCIÓN (reversión) — cuidado con el horizonte
**La idea:** a veces los precios se pasan de frenada y **vuelven**. Pero depende del horizonte: muy corto plazo revierte, medio plazo sigue (momentum), largo plazo revierte otra vez.
- Reversión a 3-5 años (De Bondt & Thaler 1985) — **III**
- Reversión mensual (Jegadeesh 1990) — **III**
- Reversión por lead-lag (Lo & MacKinlay 1990) — **III**
- Reversión a 1 día en cripto (Zaremba et al. 2021) — **III**
- Momentum-corto / reversión-largo en cripto (Dobrynskaya 2023) — **III**

**Aviso de F3 (importante para ti):** la reversión de 1 día **NO sobrevive en las monedas líquidas** — y los perpetuos son justo el universo líquido. Y el paper de Dobrynskaya tiene una contradicción viva (otro estudio sugiere que la varianza podría ser infinita, con lo que el Sharpe "no existiría" bien definido). Este mecanismo hay que mirarlo con lupa antes de nada.

### 4) MICROESTRUCTURA / LIQUIDEZ — probablemente no viaja hoy
**La idea:** el flujo de órdenes de los informados y la (i)liquidez empujan el precio.
- Modelo de impacto de Kyle (1985) — **III** (teoría)
- Iliquidez ILLIQ (Amihud 2002) — **III**
- Order Flow Imbalance (Cont, Kukanov & Stoikov 2014) — **III**
- Toxicidad de flujo VPIN (Easley, López de Prado & O'Hara 2012) — **III**
- OFI en cripto (Alexander et al. 2024) — **IV**; order flow→cripto (Anastasopoulos et al. 2026) — **III**; Bitcoin LOB (Westland 2021) — **III**

**Aviso de F3:** casi ninguno reporta una prueba fuera de muestra de un edge *operable*, y dependen de datos de libro de órdenes (niveles L2/L3) que **hoy no tienes**. Coherente con la sospecha de F0 de que esta familia "probablemente no viaja por datos".

### 5) RÉGIMEN — es un FILTRO, no una estrategia
**La idea:** detectar en qué "estado" está el mercado (alcista / bajista / alta volatilidad) para **condicionar** otras señales. Por sí solo **no genera dinero** — es una herramienta de apoyo.
- Markov-switching de Hamilton (1989) — **III** (método)
- Regímenes en tipos (Ang & Bekaert 2002), HMM para asignación (Nystrup et al. 2018), MS-GARCH Bitcoin (Shakourloo & Azimli 2026), Bayesian HMM Bitcoin (Paulavičius 2025) — todos **III (método)**

**Lo importante:** su "alfa" figura como *no aplicable* a propósito. Es un condicionador de otras estrategias, no una fuente de retorno.

## El hallazgo incómodo de F3 (y por qué es sano)

De **163** pruebas de robustez posibles, la literatura solo **reporta 36**; las otras **127 son "no reportado"**. En concreto: **walk-forward = 0 de 30. Bootstrap = 0 de 30.** Es decir: la mayoría de estos edges **no tienen publicadas las pruebas de robustez más exigentes.**

Eso **no los mata** — significa que esas pruebas las tendrás que hacer **tú** cuando alguno entre al pipeline (es exactamente para lo que sirve tu pipeline: backtest → OOS → lockbox). "No reportado" es un dato valioso: te dice **dónde hay que mirar con lupa**.

## Para tu tranquilidad

- Nada de esto es operable todavía. Son candidatas de la literatura, no estrategias tuyas.
- F3 casi no movió niveles: solo Faber bajó (III→IV); las otras 29 se mantuvieron.
- Tu **H-001** sigue su curso (Fase B, cierre ~16-ago). **H-002.v2** espera su forward.
- F3 está **ejecutada pero no cerrada**: mañana pasa por su árbitro independiente (A-04) y tu aprobación, igual que F1 y F2. La siguiente fase (F4) es "¿por qué económicamente existe cada edge y qué lo mataría?" — ahí es donde se decide cuáles merecen de verdad convertirse en hipótesis.

Que descanses. Mañana seguimos.
