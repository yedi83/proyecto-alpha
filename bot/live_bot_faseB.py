#!/usr/bin/env python3
"""
BOT Donchian 512 — VERSION DE FRONTERA PARA FASE B (staged; NO ejecutar durante la Fase A).

Identico a bot/live_bot.py del lab salvo los 4 CAMBIOS-FRONTERA aprobados en
PAQUETE_FASE_B.md §2, todos respaldados por la fontaneria del 2026-07-03:
  F0    : enable_demo_trading (Binance retiro el testnet de futuros; ccxt >= 4.5)
  B-fix1: precio de fill via fetch_order (create_order devuelve average=None)
  B-fix2: fees sumadas de los fills (la orden trae fee=None)
  B-fix3: riesgo por simbolo {BTC 0.125%, resto 0.10%} + cap agregado por suma real
          (exp-003 ACEPTA, umbral pre-escrito, N=2 declarado)

Se aplica el dia D (cierre aprobado de Fase A) siguiendo el checklist del paquete:
reemplaza a live_bot.py en el lab, commit con tag H001-faseB-frontera, acta sellada.
Requiere: pip install ccxt pandas numpy
"""
import os, sys, time, json, csv, math
from datetime import datetime, timezone
from pathlib import Path
import numpy as np, pandas as pd, ccxt

def _load_env():
    p=Path(__file__).resolve().parent/"config.env"
    if p.exists():
        for line in p.read_text().splitlines():
            line=line.strip()
            if line and not line.startswith("#") and "=" in line:
                k,v=line.split("=",1); os.environ.setdefault(k.strip(), v.split("#")[0].strip())
_load_env()

LOGDIR=Path(__file__).resolve().parent/"logs"; LOGDIR.mkdir(exist_ok=True)
LOGF=LOGDIR/"bot.log"
def log(*a):
    msg=" ".join(str(x) for x in a)
    sys.stdout.write(msg+"\n"); sys.stdout.flush()
    try:
        with open(LOGF,"a",encoding="utf-8") as f:
            f.write(datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S ")+msg+"\n")
    except Exception: pass

# ---------------- CONFIG (parametros CONGELADOS) ----------------
EXCHANGE_ID   = os.getenv("EXCHANGE_ID", "binance")
EXCHANGE_TESTNET = os.getenv("EXCHANGE_TESTNET", "true").lower()=="true"   # true = DEMO trading
API_KEY       = os.getenv("API_KEY", "")
API_SECRET    = os.getenv("API_SECRET", "")
DRY_RUN       = os.getenv("DRY_RUN", "true").lower()=="true"
PAPER_EQUITY  = float(os.getenv("PAPER_EQUITY", "750"))
LEVERAGE      = int(os.getenv("LEVERAGE", "2"))
MARGIN_MODE   = os.getenv("MARGIN_MODE", "isolated")

SYMBOLS = ["BTC/USDT:USDT","ETH/USDT:USDT","SOL/USDT:USDT","BCH/USDT:USDT","DOGE/USDT:USDT"]
TIMEFRAME = "15m"
ENTRY_LEN, EXIT_LEN, ATR_LEN, ATR_MULT = 512, 256, 14, 3.0   # CONGELADO
# CAMBIO-FRONTERA B-fix3: riesgo por simbolo (exp-003; PAQUETE_FASE_B §1)
RISK_MAP = {s: 0.001 for s in SYMBOLS}
RISK_MAP["BTC/USDT:USDT"] = 0.00125
MAX_LEV = 3.0
MAX_CONCURRENT = 5
AGG_RISK_CAP = float(os.getenv("AGG_RISK_CAP", "0.006"))
DAILY_LOSS_KILL = float(os.getenv("DAILY_LOSS_KILL", "0.05"))

STATE_FILE = Path(__file__).resolve().parent/"bot_state.json"
LOG_FILE   = Path(__file__).resolve().parent.parent/"paper"/"registro_live.csv"
LOG_COLS=["trade_id","symbol","side","entry_time_signal","entry_time_fill",
"entry_price_signal","entry_price_fill","exit_time_signal","exit_time_fill",
"exit_price_signal","exit_price_fill","qty","fees","funding","gross_pnl","net_pnl"]

def apply_account_config(ex):
    if DRY_RUN: return
    for sym in SYMBOLS:
        try: ex.set_margin_mode(MARGIN_MODE, sym)
        except Exception as e: log(f"  margin_mode {sym}: {e}")
        try: ex.set_leverage(LEVERAGE, sym)
        except Exception as e: log(f"  leverage {sym}: {e}")
    log(f"Cuenta configurada: modo={MARGIN_MODE} apalancamiento={LEVERAGE}x en {len(SYMBOLS)} simbolos")

def make_exchange():
    ex=getattr(ccxt, EXCHANGE_ID)({"apiKey":API_KEY,"secret":API_SECRET,
        "enableRateLimit":True,"options":{"defaultType":"future"}})
    # CAMBIO-FRONTERA F0: demo trading en lugar del testnet retirado
    if EXCHANGE_TESTNET:
        if hasattr(ex, "enable_demo_trading"):
            ex.enable_demo_trading(True)
            api = ex.urls.get("api", {})
            fapi = str(api.get("fapiPrivate","")) if isinstance(api, dict) else str(api)
            assert "demo" in fapi.lower(), f"endpoint no parece demo trading: {fapi}"
        else:
            raise RuntimeError("ccxt sin enable_demo_trading: actualizar ccxt (>=4.5)")
    ex.load_markets(); return ex

def now(): return datetime.now(timezone.utc)
def iso(t):
    if isinstance(t, str): return t
    if hasattr(t, "isoformat"): return t.isoformat()
    return pd.to_datetime(int(t), unit="ms", utc=True).isoformat()

def load_state():
    if STATE_FILE.exists(): return json.loads(STATE_FILE.read_text())
    return {"positions":{}, "day":None, "day_start_equity":None, "halted":False, "next_id":1}
def save_state(s): STATE_FILE.write_text(json.dumps(s,indent=2,default=str))

def log_trade(row):
    LOG_FILE.parent.mkdir(parents=True, exist_ok=True)
    new=not LOG_FILE.exists()
    with open(LOG_FILE,"a",newline="") as f:
        w=csv.DictWriter(f,fieldnames=LOG_COLS)
        if new: w.writeheader()
        w.writerow(row)

# ---------------- OBSERVABILIDAD (congelada 2026-07-01; sin cambios) ----------------
EVENTS_FILE = Path(__file__).resolve().parent.parent/"paper"/"eventos.csv"
EVENT_COLS = ["ts_utc","modo","symbol","vela_ts","evento","resultado","motivo","precio","qty","detalle"]
_last_candle_seen = {}

def log_event(symbol, vela_ts, evento, resultado, motivo="", precio="", qty="", detalle=""):
    try:
        EVENTS_FILE.parent.mkdir(parents=True, exist_ok=True)
        new = not EVENTS_FILE.exists()
        with open(EVENTS_FILE,"a",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=EVENT_COLS)
            if new: w.writeheader()
            w.writerow({"ts_utc":iso(now()),
                "modo":"DRY" if DRY_RUN else ("TESTNET" if EXCHANGE_TESTNET else "REAL"),
                "symbol":symbol,"vela_ts":iso(vela_ts) if vela_ts!="" else "",
                "evento":evento,"resultado":resultado,"motivo":motivo,
                "precio":precio,"qty":qty,"detalle":detalle})
    except Exception:
        pass

# ---------------- RECONCILIACION (sin cambios) ----------------
def reconcile_positions(ex, st):
    if DRY_RUN: return
    try:
        poss=ex.fetch_positions(SYMBOLS)
        actual={p["symbol"]:p for p in poss if abs(float(p.get("contracts") or 0))>0}
    except Exception as e:
        log("reconcile: no se pudieron leer posiciones:", e); return
    for sym in SYMBOLS:
        has_state=bool(st["positions"].get(sym)); has_real=sym in actual
        if has_real and not has_state:
            p=actual[sym]; sg=signals(ex,sym); atr=sg["atr"] if sg else 0.0
            log(f"[RECUPERACION] {sym}: posicion en exchange sin estado local -> adoptada (stop aprox).")
            st["positions"][sym]={"side":p["side"],"entry":float(p.get("entryPrice") or 0),"atr":atr,
                "qty":abs(float(p["contracts"])),"ts_signal":iso(now()),"px_signal":float(p.get("entryPrice") or 0),
                "entry_fill_ts":iso(now()),"entry_fill_ms":ex.milliseconds(),"entry_fee":0.0,"id":st["next_id"]}
            st["next_id"]+=1
        elif has_state and not has_real:
            log(f"[RECUPERACION] {sym}: estado local con posicion pero exchange sin ella -> limpiado.")
            st["positions"][sym]=None
    save_state(st)

# ---------------- senales (identico al backtest; sin cambios) ----------------
def signals(ex, sym):
    o=ex.fetch_ohlcv(sym, TIMEFRAME, limit=ENTRY_LEN+50)
    df=pd.DataFrame(o, columns=["ts","open","high","low","close","vol"]).iloc[:-1]
    if len(df)<ENTRY_LEN+ATR_LEN+1: return None
    h,l,c=df["high"].values,df["low"].values,df["close"].values
    upper=pd.Series(h).rolling(ENTRY_LEN).max().shift(1).iloc[-1]
    lower=pd.Series(l).rolling(ENTRY_LEN).min().shift(1).iloc[-1]
    exlo =pd.Series(l).rolling(EXIT_LEN).min().shift(1).iloc[-1]
    exhi =pd.Series(h).rolling(EXIT_LEN).max().shift(1).iloc[-1]
    tr=np.maximum.reduce([h[1:]-l[1:],np.abs(h[1:]-c[:-1]),np.abs(l[1:]-c[:-1])])
    atr=pd.Series(np.concatenate([[np.nan],tr])).rolling(ATR_LEN).mean().iloc[-1]
    return dict(close=c[-1], low=l[-1], high=h[-1], upper=upper, lower=lower,
               exlo=exlo, exhi=exhi, atr=atr, ts=df["ts"].iloc[-1])

def ex_round_amount(units, mkt):
    step=mkt.get("precision",{}).get("amount")
    if step is None: return units
    return round(units, step) if isinstance(step,int) else (math.floor(units/step)*step)

def size(equity, atr, price, mkt, risk):
    # CAMBIO-FRONTERA B-fix3: el riesgo llega por parametro (mapa por simbolo)
    sd=ATR_MULT*atr
    if sd<=0: return 0.0
    units=min((equity*risk)/sd, equity*MAX_LEV/price)
    return float(ex_round_amount(units, mkt))

def min_notional(mkt, price):
    lim=mkt.get("limits",{})
    mn=(lim.get("cost",{}) or {}).get("min")
    if mn: return mn
    ma=(lim.get("amount",{}) or {}).get("min")
    return (ma*price) if ma else 5.0

def fetch_funding(ex, sym, since_ms, until_ms, units, entry_px, side):
    sgn=1 if side=="long" else -1
    try:
        if not DRY_RUN:
            hist=ex.fetch_funding_history(symbol=sym, since=int(since_ms)-1)
            if hist:
                return float(sum(h["amount"] for h in hist if since_ms<=h["timestamp"]<=until_ms))
        fr=ex.fetch_funding_rate_history(sym, since=int(since_ms)-1)
        rate=sum(f["fundingRate"] for f in fr if since_ms<=f["timestamp"]<=until_ms)
        return float(-sgn*rate*units*entry_px)
    except Exception as e:
        log("funding fetch fallo:", e); return 0.0

def market_order(ex, sym, side, qty):
    if DRY_RUN:
        px=ex.fetch_ticker(sym)["last"]
        return {"price":px,"timestamp":ex.milliseconds(),"fee":0.0,"dry":True}
    o=ex.create_order(sym,"market",side,qty)
    oid=o.get("id")
    px=o.get("average") or o.get("price")
    fee=(o.get("fee") or {}).get("cost") or 0.0
    # CAMBIO-FRONTERA B-fix1/B-fix2 (fontaneria F2): la respuesta inmediata trae
    # average=None y fee=None; el precio real esta en fetch_order y las fees en los fills.
    try:
        time.sleep(1.0)
        od=ex.fetch_order(oid, sym) if oid else {}
        px=od.get("average") or px
        if not fee:
            tr=ex.fetch_my_trades(sym, limit=10)
            fee=sum((t.get("fee") or {}).get("cost") or 0.0 for t in tr if t.get("order")==oid)
    except Exception as e:
        log("market_order: fetch_order/fills fallo:", e)
    if not px:
        px=ex.fetch_ticker(sym)["last"]
        log(f"[{sym}] AVISO: fill sin precio en orden {oid}; usando ticker como aproximacion (revisar en auditoria).")
        log_event(sym,"","orden","precio_aprox","fill_sin_average","",qty,f"orden={oid}")
    return {"price":float(px),"timestamp":o.get("timestamp") or ex.milliseconds(),
            "fee":float(fee or 0.0),"dry":False}

# ---------------- bucle principal ----------------
def run_once(ex, st):
    eq=PAPER_EQUITY if DRY_RUN else float(ex.fetch_balance()["total"].get("USDT",0))
    log(f"CICLO {iso(now())} eq={eq:.2f} abiertas={sum(1 for p in st['positions'].values() if p)}")
    today=now().date().isoformat()
    if st["day"]!=today or DRY_RUN:
        st["day"]=today; st["day_start_equity"]=eq; st["halted"]=False
    if st["day_start_equity"] and eq<=st["day_start_equity"]*(1-DAILY_LOSS_KILL):
        if not st["halted"]: log("KILL-SWITCH diario activado. No se abren nuevas posiciones.")
        st["halted"]=True
    open_syms=[s for s,p in st["positions"].items() if p]
    for sym in SYMBOLS:
        mkt=ex.market(sym); sg=signals(ex,sym)
        if not sg:
            log_event(sym,"","datos","omitido","sin_datos_suficientes"); continue
        prev=_last_candle_seen.get(sym)
        if prev is not None and not sg["ts"]>prev:
            log_event(sym,sg["ts"],"vela","atrasada","api_sin_vela_nueva")
        _last_candle_seen[sym]=sg["ts"]
        pos=st["positions"].get(sym); c=sg["close"]
        if pos:
            side=pos["side"]
            stop=(max(pos["entry"]-ATR_MULT*pos["atr"], sg["exlo"]) if side=="long"
                  else min(pos["entry"]+ATR_MULT*pos["atr"], sg["exhi"]))
            hit_stop=(sg["low"]<=stop) if side=="long" else (sg["high"]>=stop)
            reverse=(side=="long" and c<sg["lower"]) or (side=="short" and c>sg["upper"])
            if hit_stop or reverse:
                fill=market_order(ex, sym, "sell" if side=="long" else "buy", pos["qty"])
                log_event(sym,sg["ts"],"salida","ejecutada",("stop" if hit_stop else "reversa"),fill["price"],pos["qty"])
                _close_log(ex, st, sym, pos, sg, fill, exit_px_signal=(stop if hit_stop else c))
                st["positions"][sym]=None; open_syms=[s for s in open_syms if s!=sym]; pos=None
                save_state(st)
        long_sig=c>sg["upper"]; short_sig=c<sg["lower"]
        if (pos is None) and (long_sig or short_sig):
            if len(open_syms)>=MAX_CONCURRENT or st["halted"]:
                log_event(sym,sg["ts"],"senal","omitida",("kill_switch" if st["halted"] else "max_concurrentes"),c); continue
            # CAMBIO-FRONTERA B-fix3: cap agregado como suma de riesgos reales
            if sum(RISK_MAP[s2] for s2 in open_syms)+RISK_MAP[sym]>AGG_RISK_CAP:
                log("Cap riesgo agregado alcanzado, salto",sym)
                log_event(sym,sg["ts"],"senal","omitida","cap_riesgo_agregado",c); continue
            qty=size(eq, sg["atr"], c, mkt, RISK_MAP[sym])
            if qty<=0:
                log_event(sym,sg["ts"],"senal","omitida","qty_cero",c); continue
            if qty*c < min_notional(mkt,c):
                log(f"[{sym}] notional {qty*c:.1f}$ < minimo {min_notional(mkt,c):.1f}$ -> SALTADO (capital insuficiente)")
                log_event(sym,sg["ts"],"senal","omitida","min_notional",c,qty,
                          "notional=%.2f<min=%.2f"%(qty*c,min_notional(mkt,c))); continue
            side="long" if long_sig else "short"
            fill=market_order(ex, sym, "buy" if side=="long" else "sell", qty)
            log_event(sym,sg["ts"],"senal","ejecutada",side,fill["price"],qty)
            st["positions"][sym]={"side":side,"entry":fill["price"],"atr":sg["atr"],"qty":qty,
                "ts_signal":iso(sg["ts"]),"px_signal":c,"entry_fill_ts":iso(fill["timestamp"]),
                "entry_fill_ms":fill["timestamp"],"entry_fee":fill["fee"],"id":st["next_id"]}
            st["next_id"]+=1; open_syms.append(sym); save_state(st)
            log(f"[{sym}] ENTRADA {side} qty {qty} @ {fill['price']} (DRY={fill.get('dry')})")
    save_state(st)

def _close_log(ex, st, sym, pos, sg, fill, exit_px_signal):
    side=pos["side"]; sgn=1 if side=="long" else -1
    gross=pos["qty"]*(fill["price"]-pos["entry"])*sgn
    fees=pos.get("entry_fee",0.0)+fill.get("fee",0.0)
    funding=fetch_funding(ex, sym, pos.get("entry_fill_ms", ex.milliseconds()),
                          fill["timestamp"], pos["qty"], pos["entry"], side)
    net=gross-fees+funding
    log_trade({"trade_id":pos["id"],"symbol":sym,"side":side,
        "entry_time_signal":pos["ts_signal"],"entry_time_fill":pos["entry_fill_ts"],
        "entry_price_signal":pos["px_signal"],"entry_price_fill":pos["entry"],
        "exit_time_signal":iso(sg["ts"]),"exit_time_fill":iso(fill["timestamp"]),
        "exit_price_signal":exit_px_signal,"exit_price_fill":fill["price"],
        "qty":pos["qty"],"fees":fees,"funding":funding,"gross_pnl":gross,"net_pnl":net})
    log(f"[{sym}] SALIDA {side} @ {fill['price']} | net {net:.2f}$ (funding {funding:.2f})")

def main():
    log(f"BOT Donchian512 FASE-B | exchange={EXCHANGE_ID} demo={EXCHANGE_TESTNET} DRY_RUN={DRY_RUN}")
    log(f"riesgo/trade={{'BTC':0.125, 'resto':0.10}}% | cap agregado={AGG_RISK_CAP*100}% | kill diario={DAILY_LOSS_KILL*100}%")
    ex=make_exchange(); apply_account_config(ex); st=load_state(); reconcile_positions(ex, st)
    last_bar=0
    while True:
        try:
            sg=None
            for _ in range(40):
                sg=signals(ex, SYMBOLS[0])
                if sg and sg["ts"]>last_bar: break
                time.sleep(5)
            run_once(ex, st)
            if sg: last_bar=sg["ts"]
        except Exception as e:
            log("ERROR:", type(e).__name__, e)
        nxt=(900-(int(time.time())%900))+5; log(f"...durmiendo {nxt}s"); time.sleep(nxt)

if __name__=="__main__":
    main()
