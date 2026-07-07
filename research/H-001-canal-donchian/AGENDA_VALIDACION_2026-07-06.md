# Agenda de validación de la cesta — 2026-07-06

> Objetivo: pruebas que **aportan conocimiento** (validar / entender si funciona y cómo), **no** mejorarla. Escrita tras revisar los veredictos previos + los exp-004/005 de hoy.

## 1. Dónde está H-001, honestamente (lo que YA se sabe)

Los veredictos legacy ya lo establecieron, y hoy lo re-confirmamos:

- **No es una máquina de alfa; es un seguro de crisis / reductor de drawdown.** Mismo Sharpe que aguantar (~0.42), pero con ~1/5 del drawdown (−18% vs −88% del buy&hold). Paga esquivando las grandes caídas; se rezaga en bull fuerte.
- **El edge cuelga de ~5 trades** (top-5 = 115% del neto). Win rate 20%. Firma textbook de trend-following: **convexidad, no robustez estadística.** "No distinguible de suerte con rigor."
- **Ya probado:** OOS 2021-2023 (alfa positiva held-out), bootstrap por bloques (Sharpe p50 0.43, pero 25% de colas planas/negativas), jackknife, costes reales, fills adversos, "solo tendencia" (descartada), rotación de líderes por régimen (→ el objeto robusto es la cesta, no seleccionar monedas).
- **exp-004/005 (hoy):** el canal necesita ser largo (384 se cae, 512/640 aguantan); por moneda es débil (HYPE OOS no aportó edge); largo>corto en todas = **deriva del toro cripto, no skill**. Todo consistente con "seguro convexo", no hallazgos nuevos.

**Conclusión honesta:** idea de **baja convicción**, correctamente dimensionada chica (0.1-0.2%/trade), cuyo valor —si existe— es reducir drawdown, no batir el mercado. No probada, no refutada.

## 2. Lo que de verdad falta saber (priorizado)

**P1 — Funding real (la mayor incógnita nombrada).** Binance solo expone el último tramo; con funding alto, 2024-26 queda apenas en cero. Existe `funding_apply.py` y una carpeta `funding/` en el cache. Acción: revisar si hay funding histórico real aplicable y re-correr con él. **Esto puede mover la magnitud del veredicto más que cualquier backtest nuevo.**

**P2 — exp-006: OOS por tiempo, régimen 2020 (crash covid).** Pre-registrado ya (`exp-006/PREREG.md`). Es la prueba más directa de si la "crisis alpha" **aparece cuando hay una crisis de verdad**, en datos no vistos. **Pendiente de extender el cache antes de 2021** (ver §3).

**P3 — Estudio de comportamiento como seguro/diversificador.** La tesis es "cobra en crisis". Medirlo de frente: retorno de la estrategia durante los peores meses del mercado (2022 LUNA/FTX), su correlación con el buy&hold de la cesta, y si un overlay (aguantar + una manga de la estrategia) mejora el riesgo-ajustado. Verificar si `regimen_estudio.py` ya lo cubre; si no, es conocimiento decisión-relevante que falta.

**P4 — Forward sobre precios REALES (el árbitro final).** Las fases A/B corren sobre testnet (datos falsos). Un paper trading sobre precios reales de mainnet, universo fijo, sizing mínimo, es el único juez limpio que queda para un edge débil. Es lento (meses) pero es el que zanja.

## 3. Estado de la descarga de datos (bloqueante para P2)

El **descargador no está en la carpeta montada** (`donchian512_lab`). Los scripts leen del cache en `crypto_iid_rango\backtest\cache`, poblado por un descargador que vive probablemente en `crypto_iid_rango\backtest\` (no montada). Para extender la fecha necesito una de dos:

- Montar `D:\ESTRATEGIA_ALEX\crypto_iid_rango\backtest` (donde debería estar el descargador), o
- Que me apuntes al script con el que bajaste el cache.

Con eso reviso el descargador y armo la extensión a ~2020 (con el límite: solo las monedas con historia perp pre-2021).

## 4. Lo que NO hacer (disciplina)

- **No re-optimizar** (no cambiar 512 por 640, no recortar el corto) por lo que se vio. Eso es curve-fitting.
- **No seleccionar** monedas por resultado. El objeto es la cesta; los líderes rotan.
- **No re-correr** tests esperando un número mejor. Cada test se pre-registra y se acepta su veredicto.
- La **decisión** es tuya, no inercia: (A) desplegarla chica como seguro/diversificador tras paper en real; (B) conseguir funding real y re-firmar magnitudes; (C) aparcarla con este veredicto. Reabrir = decisión explícita.
