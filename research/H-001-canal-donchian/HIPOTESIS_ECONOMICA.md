# H-001 — Hipótesis Económica

> Redactada por A-03 (Investigador Cuantitativo) el 2026-07-02.
> **Declaración de honestidad:** este documento se escribe DESPUÉS de conocer los resultados del backtest. Explicar lo ya visto es barato; el compromiso real de esta hipótesis son sus predicciones verificables (§4) y sus señales de retiro (§5). Si esas fallan, la hipótesis falla, aunque la estrategia haya ganado.

## 1. La ineficiencia propuesta

**En perpetuos cripto existen tendencias direccionales de días a semanas que persisten más de lo que el precio inicial de la ruptura incorpora, porque la información y el capital entran lento y el posicionamiento apalancado amplifica el movimiento una vez iniciado.**

Mecanismo compuesto, en orden de peso:

1. **Subreacción y rebaño (underreaction → herding).** El mercado cripto sigue dominado por flujo minorista y narrativo. Las noticias/regímenes no se descuentan de golpe: el precio rompe, el rebaño confirma, el movimiento se extiende. Una ruptura de máximo/mínimo de ~5 días es un detector burdo pero robusto de que ese proceso arrancó.
2. **Amplificación por apalancamiento (cascadas de liquidación).** El mercado de perpetuos concentra apalancamiento alto. Un movimiento direccional fuerza cierres de posiciones contrarias (stops y liquidaciones) que alimentan el propio movimiento. Esto convierte tendencias moderadas en tendencias grandes — exactamente las que pagan un sistema con win rate 20% y payoff concentrado.
3. **Límites al arbitraje conductuales (por qué sigue vivo tras 40 años de Turtles).** El perfil de pago — perder el 80% de las veces, sangrar durante meses, y depender de ~5 trades en años — es psicológica e institucionalmente intolerable para casi todos los participantes. El edge no está protegido por secreto sino por **dolor**: es una prima por soportar una distribución que la mayoría abandona. Predicción incómoda incluida: la mayoría de quienes lo intenten lo abandonarán en el peor momento.

## 2. ¿Quién está al otro lado y por qué pierde?

- **Los que hacen fade de rupturas** (reversión a la media en el timeframe equivocado): venden la ruptura esperando el retorno al rango; en la minoría de casos en que la tendencia es real, financian el tramo grande.
- **Los que salen tarde y en pánico**: mantienen contra tendencia, capitulan en cascada, y su capitulación es el combustible del tramo final (el que más paga al canal).
- **El holder pasivo, en términos relativos**: la alfa vs. B&H de H-001 no viene de ganar más, sino de **no estar** (o estar corto) durante los colapsos. El holder "paga" con el drawdown -88% que la estrategia esquiva (-18%).

## 3. ¿Explica la hipótesis las anomalías observadas? (tensiones declaradas)

- **Todo el neto sale de los longs, pese a exposición 51/47.** Explicación propuesta: en cripto las subidas son tendencias largas que un canal de 5 días monta bien; las caídas son crashes rápidos + chop, donde el canal entra tarde y el whipsaw se come el tramo. Los cortos no son el motor: son la **prima de seguro** que compra la neutralidad (beta≈0) y la protección de cola. TENSIÓN: si esto es cierto, un H-001b "long-only" tendría mejor retorno con peor beta — verificable, y de hecho el diagnóstico por dirección ya lo sugiere.
- **BTC sin alfa, alts con alfa.** Consistente con el mecanismo 1: BTC es el par más institucionalizado y arbitrado (ETFs, market makers profesionales); la subreacción minorista vive en las alts. Esta es la predicción ex-post que más me creo — y la más vigilable hacia adelante.
- **Alfa estadísticamente no significativa (t=0.94).** La hipótesis lo acepta por diseño: una prima de convexidad con ~5 eventos efectivos en 5 años no puede ser significativa con estos datos. Por eso el veredicto correcto es "diversificador plausible", no "edge probado" — la hipótesis económica no cambia eso.

## 4. Predicciones falsables (el compromiso)

| # | Predicción | Cómo se verifica | Estado |
|---|---|---|---|
| P1 | La alfa es mayor en pares menos institucionalizados (alts) que en BTC | Ya verificable en los datos existentes | ✅ Consistente (BTC alfa -4.4%; ETH/SOL/DOGE +) |
| P2 | A medida que un par se institucionaliza, su alfa individual decae | Alfa rolling anual por par; vigilar ETH post-ETF | ⏳ Futuro |
| P3 | Los trades top que concentran el payoff coinciden con expansión de volatilidad y aumento de open interest (participación nueva), no con mercados quietos | Requiere OI del Data Lake; cruzar con top-5 trades | ⏳ Requiere datos (Etapa 3) |
| P4 | En tendencias alcistas fuertes el funding es alto y los longs lo pagan → el edge neto se comprime cuando el funding es extremo | Funding real por trade (la incógnita nº 1 ya declarada) | ⏳ Fase B la mide |
| P5 | El edge persiste públicamente (no depende de secreto); lo que lo protege es el perfil de pago | Si en 3-5 años el win rate "mejora" hacia 40-50% y el payoff se desconcentra, la estrategia cambió de naturaleza → sospechar régimen nuevo o bug, no celebrar | ⏳ Continuo |

## 5. Señales de retiro conceptual (qué vigilar ANTES de que el drawdown lo diga)

1. **Muerte de la persistencia:** si la frecuencia de tendencias multi-día colapsa de forma sostenida (p. ej., % de ventanas de 5 días con rango > k·ATR en mínimos históricos por 6-12 meses), el mecanismo 1-2 dejó de operar. El canal sangrará por whipsaw mucho antes de que el equity lo grite.
2. **Institucionalización del universo:** compresión estructural de spreads/funding y dominancia de flujo profesional en las alts de la cesta → esperar decaimiento estilo BTC (P2).
3. **Cambio de microestructura del apalancamiento:** si el mercado de perpetuos reduce estructuralmente el apalancamiento (regulación, deleverage duradero), el amplificador del mecanismo 2 se apaga.
4. **Funding crónicamente extremo:** si P4 muestra que el funding real se come la alfa en los regímenes donde la estrategia debería pagar, la hipótesis económica sobrevive pero la implementación en perpetuos muere (habría que reevaluar el instrumento, no la señal).

## 6. Qué NO afirma esta hipótesis

No afirma que H-001 tenga edge probado (t=0.94 manda). No afirma que el pasado se repita. No afirma que los cortos "funcionen" — los trata como coste de neutralidad, decisión que puede revisarse como hipótesis separada (H-00X long-only con beta declarada). No sustituye a la validación operativa en curso.
