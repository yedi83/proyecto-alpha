#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H-002 paper-real — monitor forward DIARIO, multi-activo, SIN dinero.

Sin estado: cada corrida re-ejecuta el backtest VALIDADO (motor verbatim) sobre
datos frescos de mainnet spot (publico, SIN API keys) y registra los trades
FORWARD (entry_date >= deploy_date) como evidencia going-forward. Cero riesgo:
no coloca ordenes, no usa keys. Se programa una vez al dia (tras el cierre diario).

Basket = majors probados en el banco. Reglas congeladas: N=20, atr 2.5, SMA200,
stop 2.5xATR, objetivo 2R, riesgo 1.25%, solo largos. La variante trailing NO va.
Comparacion clave: trades forward vs 'aguantar desde deploy' por activo.
"""
import json, time
from datetime import datetime, timezone
from pathlib import Path
import numpy as np, pandas as pd, ccxt

HERE = Path(__file__).resolve().parent
EQ0 = 10000.0
BASE = dict(N=20, atr_mult=2.5, sma_len=200, rr=2.0, risk=0.0125, fee=0.0004, lev=2.0)
BASKET = ["BTC/USDT","ETH/USDT","BNB/USDT","ADA/USDT","XRP/USDT","LTC/USDT"]
EX = ccxt.binance({"enableRateLimit": True})

# ================== MOTOR VERBATIM (backtest.py del investigador) ==================
def atr_rma(df, n=14):
    pc = df.Close.shift(1)
    tr = pd.concat([df.High-df.Low,(df.High-pc).abs(),(df.Low-pc).abs()],axis=1).max(axis=1)
    return tr.ewm(alpha=1/n, adjust=False).mean()

def backtest(df, N=20, atr_mult=2.5, sma_len=200, rr=2.0, risk=0.0125,
             fee=0.0004, lev=2.0, i0=0, i1=None):
    if i1 is None: i1 = len(df)
    o,h,l,c,d = df.Open.values, df.High.values, df.Low.values, df.Close.values, df.Date.values
    A   = atr_rma(df).values
    hh  = df.High.rolling(N).max().shift(1).values
    sma = df.Close.rolling(sma_len).mean().values
    eq = EQ0; trades = []; curve = []
    pos = None
    warm = max(N, sma_len, 15)
    i = max(i0, warm)
    def close_trade(px, when, tag):
        nonlocal eq, pos
        pnl = pos["qty"]*(px-pos["entry"]) - fee*pos["qty"]*(pos["entry"]+px)
        eq += pnl
        trades.append(dict(entry_date=pos["date"], exit_date=when, res=tag,
                           pnl=pnl, r=pnl/pos["risk_amt"], eq=eq))
        pos = None
    while i < i1:
        if pos:
            if   o[i] <= pos["stop"]: close_trade(o[i], d[i], "sl_gap")
            elif l[i] <= pos["stop"]: close_trade(pos["stop"], d[i], "sl")
            elif o[i] >= pos["tp"]:   close_trade(o[i], d[i], "tp_gap")
            elif h[i] >= pos["tp"]:   close_trade(pos["tp"], d[i], "tp")
        if pos is None and i+1 < i1 and not np.isnan(hh[i]+sma[i]+A[i]):
            if c[i] > hh[i] and c[i] > sma[i] and A[i] > 0:
                e = o[i+1]; st = e - atr_mult*A[i]
                if st > 0:
                    dist = e-st; ra = risk*eq; q = ra/dist
                    if q*e > lev*eq:
                        q = lev*eq/e; ra = q*dist
                    pos = dict(entry=e, stop=st, tp=e+rr*dist, qty=q, risk_amt=ra, date=d[i+1])
                    j = i+1
                    if   l[j] <= pos["stop"]: close_trade(pos["stop"], d[j], "sl")
                    elif h[j] >= pos["tp"]:   close_trade(pos["tp"], d[j], "tp")
                    i = j
        curve.append(eq + (pos["qty"]*(c[i]-pos["entry"]) if pos else 0.0))
        i += 1
    if pos: close_trade(c[i1-1], d[i1-1], "eod")
    return pd.DataFrame(trades), np.array(curve)
# ==================================================================================

def fetch_daily(sym, dias=800):
    now = EX.milliseconds(); since = now - dias*86_400_000
    rows=[]; cur=since
    while cur < now:
        b = EX.fetch_ohlcv(sym, "1d", since=cur, limit=1000)
        if not b: break
        rows += b; cur = b[-1][0] + 86_400_000
        if len(b) < 1000 and cur >= now - 86_400_000: break
        time.sleep(EX.rateLimit/1000)
    df = pd.DataFrame(rows, columns=["ts","Open","High","Low","Close","Volume"]).drop_duplicates("ts").sort_values("ts")
    df["Date"] = pd.to_datetime(df["ts"], unit="ms", utc=True)
    df = df[df["Date"] < pd.Timestamp.now(tz="UTC").normalize()]   # solo velas CERRADAS
    for cc in ["Open","High","Low","Close"]: df[cc]=pd.to_numeric(df[cc], errors="coerce")
    return df.dropna(subset=["Open","High","Low","Close"]).reset_index(drop=True)

def main():
    HERE.mkdir(exist_ok=True)
    ef = HERE/"estado.json"
    est = json.loads(ef.read_text()) if ef.exists() else {"deploy_date": datetime.now(timezone.utc).date().isoformat()}
    deploy = pd.Timestamp(est["deploy_date"], tz="UTC")
    allrows=[]; resumen=[]
    for sym in BASKET:
        try: df = fetch_daily(sym)
        except Exception as e:
            resumen.append(f"{sym.replace('/','')}: fetch_fallo"); continue
        if len(df) < 220: resumen.append(f"{sym.replace('/','')}: pocos_datos"); continue
        tr, cv = backtest(df, **BASE)
        hold = df.Close.iloc[-1]/df.Close[df.Date>=deploy].iloc[0]-1 if (df.Date>=deploy).any() else np.nan
        if len(tr):
            tr["symbol"] = sym.replace("/","")
            tr["entry_date"] = pd.to_datetime(tr["entry_date"], utc=True)
            fwd = tr[tr["entry_date"] >= deploy]
            abierto = tr.iloc[-1]["res"] == "eod"
            resumen.append(f"{sym.replace('/','')}: fwd={len(fwd)} pnl={fwd.pnl.sum():+.0f}$ hold={hold*100:+.0f}% {'ABIERTA' if abierto else 'flat'}")
            allrows.append(tr)
        else:
            resumen.append(f"{sym.replace('/','')}: sin_trades")
    if allrows:
        full = pd.concat(allrows, ignore_index=True); full.to_csv(HERE/"trades.csv", index=False)
        full[pd.to_datetime(full["entry_date"], utc=True) >= deploy].to_csv(HERE/"forward.csv", index=False)
    est["last_run"] = datetime.now(timezone.utc).isoformat()
    ef.write_text(json.dumps(est, indent=1))
    linea = f"[{datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC] deploy={est['deploy_date']} | " + " | ".join(resumen)
    with open(HERE/"monitor.log","a",encoding="utf-8") as f: f.write(linea+"\n")
    print(linea)

if __name__ == "__main__":
    main()
