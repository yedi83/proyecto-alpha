# Resumen de las 3 instancias — 2026-07-10 ~15:00 UTC

> Análisis de solo lectura. Recordatorio del PREREG: el PnL con n≈10 trades NO significa nada — lo que se evalúa es instrumentación y ejecución.

## Instancias

| | FASE A (lab) | ENSAYO B (demo) | PAPER_REAL (mainnet) |
|---|---|---|---|
| Modo | DRY sobre feed testnet | Órdenes reales en demo | DRY sobre feed real |
| Rol | Evidencia de fase (PREREG) | Depurar código frontera — NO evidencia | Comparador de feed — NO evidencia |
| Trades cerrados | 11 (post-corte) | 10 | 3 |
| Win rate | 36% | 10% | 0% |
| PnL neto | +$3.43 (equity 750) | −$7.09 (750) | −$29.56 (equity paper 10 000 ≈ −0.30%) |
| Fees registradas | 0 (DRY, sesgo TE documentado) | **0.697 en 10/10 trades ✓** | 0 (DRY, esperado) |
| Funding | +2.00 | +0.32 | +0.33 |
| Salidas | 12 stops, 0 reversas | 10 stops | 3 stops |
| Velas atrasadas/día/símbolo | ~1.5 | ~2.2 | **~0.9** |
| Abiertas ahora | (estado no legible desde la sesión — verificar en máquina) | ninguna | ninguna |

## Lectura de resultados

1. **El ensayo B validó los fixes de frontera — su único trabajo:** fees > 0 en 10/10 trades (B-fix2 ✓), 0 fills sin precio y 0 eventos `precio_aprox` (B-fix1 ✓, el fallback nunca se activó), BTC operó con órdenes reales (mapa de riesgo 0.125% + EQUITY_CAP funcionando ✓), funding real recuperado en demo ✓. **El código de frontera está listo para el día D.**
2. **Mercado en régimen de rango estos 8 días:** las tres instancias sangran por stops (0 reversas, 0 tendencias montadas). Es el perfil esperado del estilo — el trend following paga raro y sangra el resto. Ninguna conclusión de edge con n=24 total.
3. **Feed mainnet ≠ feeds de prueba, cuantificado:** mainnet ~0.9 atrasadas/día/símbolo vs testnet ~1.5 y demo ~2.2. Confirma la hipótesis del diario (el retraso era del feed, no del bot) y fija expectativa realista para Fase C. Nota: ni el mainnet es cero — el replay y los criterios deben seguir tolerando atrasadas explicadas.
4. **Las señales difieren entre feeds** (lab 10L/2S vs paper_real 1L/2S en el solape): feeds distintos → canales distintos → trades distintos. Esperado, y es exactamente lo que paper_real existe para medir. Implicación seria para Fase C: el backtest se hizo con datos de un origen; producción operará el feed real — paper_real es la mejor referencia de qué señales habría dado producción.

## Acciones

- 🔴 **Verificar bot_state.json del lab EN LA MÁQUINA** (desde la sesión se leyó con error "Extra data" — probablemente lectura a mitad de escritura vía caché, pero la corrupción de estado es criterio de ABORTO del PREREG, así que se verifica, no se asume):
  `python -c "import json;json.load(open(r'D:\ESTRATEGIA_ALEX\crypto_iid_rango\donchian512_lab\bot\bot_state.json'));print('ESTADO OK')"`
- 🟠 **Seguridad de paper_real:** su config.env tiene API keys de mainnet que el modo DRY no necesita (solo usa endpoints públicos). Recomendado: dejarlas vacías o crear keys de solo-lectura. Está protegido por .gitignore, pero una clave innecesaria es riesgo innecesario.
- 🟡 Documentar paper_real como instancia oficial de comparación de feed (README con reglas, como el del ensayo) y añadirla a la rutina de vigilancia.
