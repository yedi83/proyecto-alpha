# ESPECIFICACION OPERATIVA — Donchian 512 (CONGELADA)
Derivada del codigo bot/live_bot.py. Todo se evalua sobre VELAS CERRADAS de 15m,
por simbolo (BTC, ETH, SOL, BCH, DOGE). Sin look-ahead.

## Variables (cada vela cerrada t)
- upper_t      = max(high de las 512 velas anteriores a t)      [Donchian 512 high, shift 1]
- lower_t      = min(low  de las 512 velas anteriores a t)      [Donchian 512 low]
- salida_low_t = min(low  de las 256 velas anteriores a t)      [canal salida largos]
- salida_high_t= max(high de las 256 velas anteriores a t)      [canal salida cortos]
- ATR_t        = media simple 14 del True Range
- c_t,low_t,high_t = close/low/high de la vela cerrada t
- k = 3.0  (multiplo de ATR)

## ENTRADA LONG
Condicion exacta: estar PLANO en el simbolo  Y  c_t > upper_t.
Accion: comprar a mercado.

## ENTRADA SHORT
Condicion exacta: estar PLANO en el simbolo  Y  c_t < lower_t.
Accion: vender a mercado.

(Reversa: si estas LARGO y c_t < lower_t  -> cierras y abres SHORT en la misma vela.
          si estas CORTO y c_t > upper_t  -> cierras y abres LONG  en la misma vela.)

## STOP INICIAL (formula exacta)
ATR_entrada = ATR_t en el momento de entrar (se CONGELA).
- Largo: stop = max( precio_entrada - k*ATR_entrada , salida_low_t )
- Corto: stop = min( precio_entrada + k*ATR_entrada , salida_high_t )

## GESTION (mover stop o no)
SI se mueve. El stop se RECALCULA en cada vela cerrada con la formula de arriba:
canal de salida 256 + suelo de k*ATR_entrada. En tendencia, el canal 256 acompaña
al precio y el stop trailing sube (largo) / baja (corto). Nunca rebasa el suelo de
3*ATR desde la entrada. No hay take-profit fijo.

## SALIDA (condicion exacta)
La posicion se cierra cuando ocurre lo PRIMERO de:
1. Stop tocado en la vela:  largo si low_t <= stop ; corto si high_t >= stop.
2. Ruptura opuesta del 512: largo si c_t < lower_t ; corto si c_t > upper_t
   (esta tambien reabre en sentido contrario).

## SIZING (formula exacta)
units = min( (equity * 0.001) / (k*ATR_t) ,  equity * 3 / precio )
      -> redondeado a la precision del exchange.
Riesgo objetivo por trade = 0.10% del equity (un movimiento de 3*ATR en contra = 0.10%).
Apalancamiento por posicion <= 3x (segundo termino del min).
Si units*precio < notional minimo del simbolo -> NO se abre (capital insuficiente, se registra).

## RIESGO MAXIMO CARTERA (regla exacta)
- Maximo 5 posiciones simultaneas (1 por simbolo; no se apilan mas).
- No abrir nueva si (n_abiertas + 1) * 0.10% > 0.60%  (cap de riesgo agregado).
- Kill-switch diario: si equity <= equity_inicio_dia * 0.95 -> no se abren NUEVAS
  posiciones el resto del dia (las abiertas se siguen gestionando/cerrando).

## MANEJO DE ERRORES (regla exacta)
- Toda excepcion del ciclo se captura, se registra y el bot CONTINUA (reintenta en
  la siguiente vela). No se cae.
- Solo velas CERRADAS (la vela en curso se descarta: df.iloc[:-1]).
- Estado guardado tras CADA operacion (bot_state.json).
- Al arrancar: RECONCILIACION con el exchange (recupera posiciones abiertas sin
  duplicarlas; limpia estado fantasma).
- Lanzador reinicia el proceso si muere (apagon/internet/error).
- Gating de seguridad: DRY_RUN -> testnet -> real.
- LIMITACION conocida: el stop se evalua en cada vela cerrada (cada 15m), NO es una
  orden stop residente en el exchange. Entre velas no hay proteccion intrabar.
  Mejora opcional (no desplegada): colocar stop reduce-only en el exchange.

## OBSERVABILIDAD (anadido 2026-07-01 — NO afecta la logica de trading)
- paper/eventos.csv: registro UNIFICADO de eventos por vela: senal ejecutada/
  omitida (motivos: kill_switch, max_concurrentes, cap_riesgo_agregado, qty_cero,
  min_notional), salida (stop/reversa), vela atrasada (la API no publico vela
  nueva para ese simbolo en el ciclo), datos insuficientes.
- Garantias: SOLO escritura, best-effort (try/except propio): un fallo del
  logging jamas interrumpe el ciclo ni cambia una decision. Ningun estado del
  registro es leido por la logica de trading.
- Proposito: hacer visibles los trades OMITIDOS (PnL fantasma, invisible para
  el tracking error) y discriminar retrasos de datos por simbolo (caso BCH
  2026-06-29 18:15).
- LIMITACION conocida: un rechazo de orden del exchange (p.ej. margen
  insuficiente) sigue el manejo de errores previo y NO genera evento propio
  (instrumentarlo tocaria el flujo de excepciones -> pospuesto a fin de fase A).

## CICLO DE VIDA (nacimiento -> muerte) — la respuesta de 2 minutos
1. Cierra una vela 15m -> se calculan upper/lower/canales/ATR.
2. Si estoy plano y el cierre rompe el Donchian 512 -> NACE la operacion (largo si
   rompe arriba, corto si rompe abajo). Congelo ATR_entrada, calculo tamaño al 0.10%
   de riesgo, fijo el stop inicial = max/min(entrada -/+ 3*ATR, canal 256).
3. En cada vela siguiente recalculo el stop (trailing canal 256 con suelo 3*ATR).
4. MUERE cuando el precio toca el stop, o cuando rompe el Donchian 512 opuesto
   (que ademas la reencarna en sentido contrario).
5. Al cerrar registro gross, fees, funding REAL y net -> al dashboard (tracking error).
