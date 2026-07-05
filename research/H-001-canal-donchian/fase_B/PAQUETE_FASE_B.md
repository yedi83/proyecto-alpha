# Paquete de transición a Fase B

> Preparado 2026-07-03, con los resultados de `fontaneria_report_2026-07-03.md`. La Fase B NO arranca hasta que la Fase A cierre aprobada (mín. 2026-07-12, replay + 6 criterios). Este paquete existe para que la transición sea el mismo día.

## 1. Decisión M1 registrada (capital y BTC)

**Decisión final (2026-07-03, tras exp-002 y exp-003):** capital de Fases B y C = **$750**. Riesgo BTC = **0.125%/trade** (resto 0.10%).

- Historia completa (auditabilidad): la propuesta original de 0.15% fue **RECHAZADA por exp-002** (Calmar 84.6% < umbral 85%; Sharpe 2024-26 degradado un tercio). El 0.125% se pre-registró como segundo y ÚLTIMO intento (`experiments/exp-003/PREREG.md`, N=2 declarado) y fue **ACEPTADO** con el mismo umbral sin modificar (Calmar 91.8%, Sharpe −0.016).
- Caveats vigentes, declarados: (a) margen de volatilidad de solo ~13% (notional ≈ $113) — habrá omisiones de BTC en picos de ATR, medidas por la métrica del §3; (b) multiplicidad N=2 registrada — esta evidencia es más débil que la de un intento único; (c) la degradación direccional en 2024-26 persiste (Sharpe 0.18→0.15), dentro del umbral.
- Riesgo agregado peor caso: 4×0.10% + 0.125% = 0.525% ≤ cap 0.60% ✓.
- La ENMIENDA correspondiente se añade al PREREG_FASE_AB (sección ENMIENDA, fechada) **antes** de que la Fase B acumule datos. exp-001 sigue reservado para el test de reproducibilidad.

## 2. Cambios del bot en la frontera de fase (los 4, juntos, con acta)

Descubiertos por la fontanería ANTES de que corrompieran la fase — ninguno se aplica durante la Fase A:

| # | Cambio | Evidencia |
|---|---|---|
| F0 | `set_sandbox_mode` → `enable_demo_trading(True)` + keys de demo.binance.com (Binance retiró el testnet de futuros; ccxt ≥4.5 lo bloquea) | Error NotSupported al primer intento |
| B-fix1 | **Precio de fill:** `create_order` devuelve `average=None, price=None`; el bot debe hacer `fetch_order(id)` tras crear y tomar `average` de ahí. Sin esto: entradas con precio None → estado corrupto → aborto | F2: create_order average=None; fetch_order average=0.07667 |
| B-fix2 | **Fees:** la orden trae `fee=None`; las fees reales están en los fills (`fetch_my_trades`, sumar por order id). Sin esto: fees=0 registradas (el "bug de registro" que el PREREG anticipó) | F2: fee inline None; fills 0.00797 |
| B-fix3 | **Riesgo por símbolo:** mapa `{BTC: 0.00125, resto: 0.001}` + cap agregado calculado como suma de riesgos reales (no n×riesgo uniforme) | exp-003 ACEPTA (umbral pre-escrito; N=2 declarado) |

Regla: los 4 cambios entran en un solo commit etiquetado, con el acta de inicio de Fase B, y se verifica el primer trade end-to-end contra ellos.

## 3. Métrica nueva obligatoria de Fase B (brecha demo/producción)

El demo tiene min_notional $50 en BTC; producción ~$100. **Toda señal BTC ejecutada en demo con notional < $100 se cuenta como "omisión simulada de producción"** en el informe de fase. Sin esta métrica, la B aprobaría B3 y la C nos daría la sorpresa. (Cero omisiones simuladas esperadas con 0.15%; si aparecen, son picos de ATR — documentar.)

**Implementada 2026-07-04 (B-fix4, hallazgo del ensayo de Fase B):** el bot compara el notional contra `MAINNET_MIN_NOTIONAL = {BTC: $100}` y, cuando el demo ejecuta pero el notional < $100, emite un evento en `eventos.csv` con `resultado=omision_simulada_produccion`, `motivo=min_notional_mainnet`, **sin alterar la ejecución en demo**. Primer caso real capturado el 2026-07-04: BTC con notional ~$81.6 (0.0013 × 62797.5), ejecutado en demo pero omitible en producción. Solo BTC instrumentado; otros símbolos pendientes si se necesitan.

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
