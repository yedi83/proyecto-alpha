# PRE-REGISTRO — Fases A (DRY_RUN) y B (testnet)
Escrito: 2026-07-01, ANTES de acumular los datos que evaluara.
Regla: este documento NO se edita despues de empezar a acumular datos. Cualquier
cambio va en una seccion "ENMIENDA" nueva, con fecha y motivo. Mover los postes
sin dejar rastro invalida la fase (leccion NEAR).

## ENMIENDA 1 — Frontera A→B (2026-07-14, ANTES de acumular datos de Fase B)

Escrita tras el cierre APROBADO 6/6 de la Fase A (informe sellado 2026-07-14; replay 36/36, 0 divergencias) y antes del reinicio que abre la B. Motivos y cambios:

1. **"Testnet" pasa a ser DEMO TRADING de Binance** (demo.binance.com): Binance retiro el testnet de futuros y ccxt >= 4.5 lo bloquea (hallazgo F0, fontaneria 2026-07-03). Toda mencion a "testnet" en la seccion Fase B se lee como "demo trading". La cuenta demo es la ya probada en el ensayo general (decision del IP, 2026-07-14), aplanada antes del corte.
2. **Cambios de codigo de frontera (4), validados con ordenes reales en el ensayo general (informe 2026-07-10: fees pobladas 10/10, 0 fills sin precio):** F0 enable_demo_trading; B-fix1 precio de fill via fetch_order (create_order devuelve average=None); B-fix2 fees sumadas de los fills; B-fix3 riesgo por simbolo BTC 0.125% / resto 0.10% con cap agregado por suma real (0.525% <= 0.60%). B-fix3 respaldado por exp-003 (pre-registrado como intento final, N=2 declarado, umbral pre-escrito: ACEPTA; exp-002 con 0.15% fue RECHAZADO).
3. **Metrica nueva obligatoria de Fase B — "omision simulada de produccion":** el demo tiene min_notional $50 en BTC; produccion ~$100. Toda señal BTC ejecutada en demo con notional < $100 se cuenta como omision simulada en el informe de fase (cierra la brecha demo/produccion para el criterio B3).
4. **EQUITY_CAP=750:** el sizing usa min(equity_demo, 750) para reflejar el capital previsto de Fase C aunque la cuenta demo tenga mas balance virtual.
5. La posicion DRY abierta al corte (#23 SOL short, paper de Fase A) se cierra ADMINISTRATIVAMENTE al cambiar de modo: era simulada, no genera trade real ni cuenta para metricas de B.

Sin otros cambios: logica de señales, canales, ATR, stops, kill switch y criterios de Fase B del pre-registro original permanecen identicos.

ACTA DE INICIO DE FASE B (sellada 2026-07-14):
"Inicio oficial de la Fase B (demo trading). **Corte: 2026-07-14 15:13:16 UTC**
(primer ciclo verificado). La Fase A cerro APROBADA 6/6 el 2026-07-14 (replay
36/36, 0 divergencias; informe en el repo). Cambios aplicados en esta frontera
y solo en ella: los 4 de la ENMIENDA 1 (demo trading, fill via fetch_order,
fees de fills, riesgo BTC 0.125%) + EQUITY_CAP=750. Verificado en el arranque:
encabezado FASE-B con demo=True DRY_RUN=False, mapa de riesgo impreso, cuenta
isolated 2x en 5 simbolos, eq=750.00 (cap sobre balance demo), abiertas=0.
La posicion paper abierta al corte (ETH long, sucesora de la #23 SOL citada en
ENMIENDA §5 con vista desfasada) fue limpiada por la reconciliacion — sin
impacto: era simulada, de Fase A. Cuenta demo: la del ensayo general, aplanada
antes del corte (posicion ETH del ensayo cerrada a mercado por el IP).
El ensayo general queda DETENIDO (tarea deshabilitada). paper_real continua
como testigo del feed real. Duracion de fase: 1 mes. Criterios: los del
pre-registro original + metrica de omision simulada (ENMIENDA §3).
Datos anteriores al corte: Fase A, no evidencia de B."
Ejecucion material: sesion Fable 5 por instruccion del IP; sella el IP.


Corte de comparabilidad: el reinicio del bot que activa la observabilidad
(eventos.csv). Fecha/hora del reinicio: 2026-07-02 03:53:46 UTC (verificado en log).
Datos anteriores al corte: solo contexto, no evidencia de fase A.

ACTA DE INICIO (decidida 2026-07-02, antes del reinicio):
"Inicio oficial de la Fase A. Se reinicia el bot con una posicion LONG BCH ya
abierta (trade #7, entrada 204.54 el 2026-07-01 02:45 UTC). El reinicio
incorpora unicamente mejoras de observabilidad y prerregistro metodologico.
No existen cambios en la logica de señales, sizing, gestion de riesgo ni
ejecucion. La continuidad de la posicion se mantiene mediante bot_state.json."
Tratamiento del trade #7 (cruza el corte): su ENTRADA es pre-corte (no cuenta
para metricas de entrada de fase A); su SALIDA, gestionada por el codigo
reiniciado, SI cuenta como evidencia de instrumentacion (evento de salida,
latencia, coherencia stop/reversa). Verificacion adicional del reinicio: el
primer ciclo post-reinicio debe mostrar abiertas=1 y mantener el trade #7 con
entry=204.54, atr=1.3493, qty=0.185 intactos (si no, es corrupcion de estado
-> criterio de aborto).

## FASE A — DRY_RUN (minimo 10 dias de calendario, 5 simbolos activos)
Objetivo: validar INSTRUMENTACION y coherencia interna. NO valida edge,
NO valida PnL. Un mes bueno o malo de PnL aqui no significa nada (n≈5).

Criterios de aprobacion (todos obligatorios):
1. Ninguna señal generada por el modelo queda sin evento registrado
   (ejecutada / omitida / descartada, con motivo).
   Verificacion: replay offline — recalcular señales sobre las velas
   descargadas del periodo y cruzar contra eventos.csv + registro_live.csv.
2. Ninguna operacion ejecutada carece de señal previa correspondiente.
3. Cero errores criticos de proceso: caida no recuperada por el lanzador,
   perdida de estado no reconciliada, corrupcion de registros.
4. Latencia mediana señal->registro < 30 segundos.
   (Medida contra el CIERRE real de la vela = ts_señal + 15min; el campo
   entry_time_signal usa el open de la vela por convencion Binance.)
5. Toda vela atrasada queda explicada por los registros de eventos.
6. Toda divergencia detectada tiene causa identificada y documentada antes
   de iniciar la fase B.

NO son criterios de fase A: PnL, tracking error, win-rate.
Nota de interpretacion: en DRY_RUN el TE tiene sesgo positivo estructural
(el registro lleva fees=0; el modelo del dashboard cobra taker). Se lee con
ese descuento. No se toca codigo para "arreglarlo" durante la fase.

## FASE B — testnet (1 mes)
Objetivo: validar EJECUCION (fontaneria con ordenes reales). Sigue sin
validar edge: con Sharpe ~0.42 harian falta años para eso, no un mes.

Criterios cuantitativos (umbral + justificacion, no falsa precision):
1. Tracking error acumulado dentro de ±5% del PnL modelado.
   Justificacion: representa aproximadamente la variacion esperada de la
   ejecucion respecto al modelo dado que los costes ya estan incorporados
   en el, refinable con la variabilidad observada en fase A. NO mide
   rentabilidad; mide que la ejecucion reproduce el modelo.
2. Slippage de entrada: MEDIANA del exceso sobre lo modelado <= 5 bps.
   (Exceso, no absoluto: el modelo ya incorpora slippage por simbolo.)
   Ademas se reporta el percentil 95 para vigilar colas (metrica
   obligatoria, no criterio de corte en esta fase).
3. Cero señales omitidas por min_notional en BTC. Si ocurre una, la
   decision (subir capital / aceptar cesta reducida) se toma y documenta
   ANTES de pasar a C, no sobre la marcha.
4. Desviacion persistente de cualquier metrica => requiere explicacion
   documentada; sin explicacion, no se pasa a C.

Metricas obligatorias del informe final de fase B (no criterios de corte):
- Tasa de señales omitidas: % sobre señales generadas, y distribucion por
  motivo (min_notional, kill_switch, cap_agregado, max_concurrentes, qty_cero).
- Percentil 95 del slippage de entrada y de salida.
- Velas atrasadas por simbolo (recuento y horas).
- Funding real vs funding estimado por trade.
- Fees reales vs modeladas (verifica que el campo fee de la orden llega
  poblado; s