# Paquete de transición a Fase B

> Preparado 2026-07-03, con los resultados de `fontaneria_report_2026-07-03.md`. La Fase B NO arranca hasta que la Fase A cierre aprobada (mín. 2026-07-12, replay + 6 criterios). Este paquete existe para que la transición sea el mismo día.

## 1. Decisión M1 registrada (capital y BTC)

**Decisión (2026-07-03, del investigador):** capital de Fases B y C = **$750**. BTC recibe riesgo especial **0.15%/trade** (resto 0.10%) para librar el min_notional de producción (~$100 mainnet; demo es $50).

- Números: con 0.15%, notional BTC ≈ $136 al ATR actual; margen hasta ATR +36%; en picos de volatilidad BTC se omitirá igualmente (evento registrado, PnL fantasma visible). Riesgo agregado peor caso: 4×0.10% + 0.15% = 0.55% ≤ cap 0.60% ✓.
- ⚠️ **Condición previa obligatoria:** esto modifica la estrategia validada (cesta con riesgo uniforme). Antes de adoptarlo: **experimento offline** — cesta FULL 2021-26 con BTC 0.15%, funding 0.01%/8h, comparar NET/maxDD/Sharpe/Calmar contra la base uniforme. Si degrada materialmente, la decisión se revisa. Registrar como `experiments/exp-002/` (el exp-001 queda reservado para el test de reproducibilidad del backtest).
- La ENMIENDA correspondiente se añade al PREREG_FASE_AB (sección ENMIENDA, fechada) **antes** de que la Fase B acumule datos.

## 2. Cambios del bot en la frontera de fase (los 4, juntos, con acta)

Descubiertos por la fontanería ANTES de que corrompieran la fase — ninguno se aplica durante la Fase A:

| # | Cambio | Evidencia |
|---|---|---|
| F0 | `set_sandbox_mode` → `enable_demo_trading(True)` + keys de demo.binance.com (Binance retiró el testnet de futuros; ccxt ≥4.5 lo bloquea) | Error NotSupported al primer intento |
| B-fix1 | **Precio de fill:** `create_order` devuelve `average=None, price=None`; el bot debe hacer `fetch_order(id)` tras crear y tomar `average` de ahí. Sin esto: entradas con precio None → estado corrupto → aborto | F2: create_order average=None; fetch_order average=0.07667 |
| B-fix2 | **Fees:** la orden trae `fee=None`; las fees reales están en los fills (`fetch_my_trades`, sumar por order id). Sin esto: fees=0 registradas (el "bug de registro" que el PREREG anticipó) | F2: fee inline None; fills 0.00797 |
| B-fix3 | **Riesgo por símbolo:** mapa `{BTC: 0.0015, resto: 0.001}` + cap agregado calculado como suma de riesgos reales (no n×riesgo uniforme) | Decisión M1 (condicionada al exp-002) |

Regla: los 4 cambios entran en un solo commit etiquetado, con el acta de inicio de Fase B, y se verifica el primer trade end-to-end contra ellos.

## 3. Métrica nueva obligatoria de Fase B (brecha demo/producción)

El demo tiene min_notional $50 en BTC; producción ~$100. **Toda señal BTC ejecutada en demo con notional < $100 se cuenta como "omisión simulada de producción"** en el informe de fase. Sin esta métrica, la B aprobaría B3 y la C nos daría la sorpresa. (Cero omisiones simuladas esperadas con 0.15%; si aparecen, son picos de ATR — documentar.)

## 4. Borrador de acta de inicio de Fase B (rellenar y sellar el día D)

> "Inicio oficial de la Fase B (demo trading). Fecha/hora del corte: ____ UTC. La Fase A cerró APROBADA el ____ (informe: replay_report_____.md, 6/6 criterios). Cambios aplicados en esta frontera y solo en ella: F0 (demo trading), B-fix1 (fill via fetch_order), B-fix2 (fees de fills), B-fix3 (riesgo BTC 0.15%, respaldado por exp-002: resultado ____). DRY_RUN=false; keys demo con retiros N/A; capital demo ajustado a $750 para reflejar C. Posiciones al corte: ____. Sin otros cambios de lógica, señales ni gestión."

## 5. Checklist de arranque (día D, en orden)

1. [ ] Fase A cerrada: replay 6/6 + informe + diario al día.
2. [ ] exp-002 corrido y veredicto anotado (condición de B-fix3).
3. [ ] ENMIENDA del PREREG escrita (riesgo BTC + métrica demo/producción + demo trading en lugar de testnet).
4. [ ] Los 4 cambios aplicados y commiteados con tag `H001-faseB-frontera`.
5. [ ] Cuenta demo: balance ajustado a $750 (transferir excedente fuera o cuenta nueva), sin posiciones abiertas, keys en config.env del bot (jamás en git).
6. [ ] Relanzar bot en modo demo; primer ciclo: reconciliación limpia, heartbeat, evento de arranque en diario.
7. [ ] Primer trade end-to-end auditado a mano: precio de fill ≠ None, fee > 0 desde fills, funding al cierre, fila correcta en registro_live.csv.
8. [ ] Vigía activo (vigia.log escribiendo OK) — lección de la línea base.
9. [ ] Sellar el acta en PREREG_FASE_AB y fila de inicio en el diario.

## 6. Criterios de la Fase B

Los del PREREG (TE ±5%, slippage mediana ≤5 bps de exceso, B3 sobre BTC ahora con la métrica del §3, métricas obligatorias del informe) — sin cambios salvo lo enmendado. Duración: 1 mes.
