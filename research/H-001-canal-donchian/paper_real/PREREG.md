# PRE-REGISTRO — Paper trading sobre precios REALES (mainnet), sin dinero

Fecha: 2026-07-07 (ANTES de arrancar). Es el paso operacional que faltaba: forward sobre precios reales, **sin capital**.

## Por qué existe (el hueco que llena)

Las fases A/B corren sobre **testnet (precios falsos)** → validan la máquina, no el edge. El backtest está agotado (costes, funding real, OOS, régimen, crisis: todo hecho). La única incógnita que queda es **operacional**: como el edge cuelga de ~5 capturas clave, ¿se generan y capturan esas señales bien sobre **precios reales**? Ningún backtest lo responde. Esto sí, sin arriesgar dinero.

## Qué es y qué NO es

- **ES:** forward sobre klines reales de mainnet (públicas), reglas congeladas, fills **simulados** con el modelo de costes del backtest. Registra paper-trades + equity.
- **NO es:** ejecución real. El slippage y los fills reales solo aparecen con órdenes reales (Fase C, capital mínimo). Esto prueba **captura de señal sobre precios reales**, no fricción de ejecución.
- **Seguro por construcción:** sin API keys → no puede colocar órdenes → cero riesgo de dinero.

## Diseño

- Datos: ccxt mainnet público (sin keys), 15m, cesta BTC/ETH/SOL/BCH/DOGE.
- Reglas congeladas: ENTRY 512 / EXIT 256 / ATR 14×3, riesgo 0.1%/trade, cap agregado, mismo modelo de slippage+fees+funding que el backtest.

> **ENMIENDA 2026-07-10 (confirmada por el investigador):** el código desplegado es el bot de frontera, que incluye el RISK_MAP con **BTC a 0.125%** (resto 0.10%) — la decisión concertada del 2026-07-03 para no sacar a BTC de la cesta por min_notional, validada por exp-003 (umbral pre-escrito, N=2 declarado). La línea de arriba quedó desactualizada al escribirse este PREREG. Se corrige sin reiniciar la instancia porque lo que este forward mide (generación y captura de señales) no depende del sizing; el sizing de BTC en el registro refleja 0.125% desde el inicio.
- Estado persistente (`paper_state.json`), log de eventos y de trades cerrados (CSV), curva de equity.
- Proceso cada 15 min (al cierre de vela), lanzador con reinicio + tarea del Programador.

## Cómo se juzga (horizonte LARGO, no pass/fail rápido)

- **Continuo (semanal):** las señales sobre precios reales coinciden con lo que el backtest generaría sobre esas mismas velas (coherencia lógica). Uptime, sin huecos.
- **Por evento (cuando ocurra):** cuando llegue una tendencia grande (un trade "clave"), verificar que se capture limpio — entrada/salida en la vela correcta, sin omisión.
- **Acumulado (meses):** el equity paper sigue el perfil esperado (convexo: sangra plano, paga raro y fuerte). NO se espera ganancia en cualquier ventana corta; ~3 trades clave al año.
- **Bandera:** divergencia sistemática señal-real vs backtest sin causa; o fallo de captura en un trade clave. Eso sí sería hallazgo.

## Límite honesto

Meses-años para acumular evidencia. Fills modelados (no reales). Es el penúltimo escalón; el último es capital mínimo real (Fase C). Confianza de partida: moderada-baja (edge no significativo). El sizing lo refleja.
