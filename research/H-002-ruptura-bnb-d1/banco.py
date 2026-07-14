#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H-002 — BANCO. Reutiliza VERBATIM el motor de backtest.py del investigador
(atr_rma, backtest, metrics) para no introducir bugs de transcripcion, y corre
los tests pre-registrados (PREREG_BANCO.md): T1 vs buy&hold, T2 cruzado, T3
sensibilidad, T4 significancia, T5 OOS.

Requiere datos/*_1d.csv (crear con descargar_datos.py).
Parametros de la estrategia validada (Pine): N=20, atr_mult=2.5, sma=200, rr=2, risk=1.25%.
"""
import numpy as np, pandas as pd
from pathlib import Path
DATOS = Path(__file__).resolve().parent / "datos"
EQ0 = 10000.0
# ---- parametros base (los del Pine que se quiere operar) ----
BASE = dict(N=20, atr_mult=2.5, sma_len=200, rr=2.0, risk=0.0125, fee=0.0004, lev=2.0)

# ================== MOTOR VERBATIM (backtest.py del investigador) ==================
def atr_rma(df, n=14):
    pc = df.Close.shift(1)
    tr = pd.concat([df.High-df.Low,(df.High-pc).abs(),(df.Low-pc).abs()],axis=1).max(axis=1)
    return tr.ewm(alpha=1/n, adjust=False).mean()

def backtest(df, N=20, atr_mult=2.0, sma_len=200, rr=2.0, risk=0.0125,
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

def load_coin(sym):
    df = pd.read_csv(DATOS/f"{sym}_1d.csv").rename(columns={
        "dt":"Date","open":"Open","high":"High","low":"Low","close":"Close","volume":"Volume"})
    df["Date"]=pd.to_datetime(df["Date"], errors="coerce", utc=True)
    for c in ["Open","High","Low","Close"]: df[c]=pd.to_numeric(df[c], errors="coerce")
    df = df.dropna(subset=["Date","Open","High","Low","Close"]).sort_values("Date").drop_duplicates("Date").reset_index(drop=True)
    return df

def stats(curve, dates):
    curve=np.asarray(curve,float)
    if len(curve)<3: return dict(ret=np.nan,mdd=np.nan,sharpe=np.nan,mar=np.nan)
    ret=curve[-1]/curve[0]-1
    peak=np.maximum.accumulate(curve); mdd=((curve-peak)/peak).min()
    r=np.diff(curve)/curve[:-1]; sh=r.mean()/r.std()*np.sqrt(365) if r.std()>0 else 0.0
    yrs=(pd.Timestamp(dates[-1])-pd.Timestamp(dates[0])).days/365.25
    cagr=(curve[-1]/curve[0])**(1/yrs)-1 if yrs>0 else np.nan
    return dict(ret=ret,mdd=mdd,sharpe=sh,mar=(cagr/abs(mdd) if mdd<0 else np.nan))

def bh_stats(df, i0):
    c=df.Close.values[i0:]; d=df.Date.values[i0:]
    return stats(c/c[0]*EQ0, d)

def strat_stats(df, i0=0, i1=None, **kw):
    tr,cv=backtest(df, i0=i0, i1=(i1 if i1 else len(df)), **kw)
    warm=max(kw.get("N",20), kw.get("sma_len",200), 15)
    dts=df.Date.values[max(i0,warm):max(i0,warm)+len(cv)]
    s=stats(cv, dts); s["n"]=len(tr); s["tr"]=tr
    return s

def line(tag, s, bh=None):
    base=f"{tag:22s} n={s.get('n','-'):>4}  Ret={s['ret']*100:+9.1f}%  MDD={s['mdd']*100:6.1f}%  Sharpe={s['sharpe']:5.2f}  MAR={s['mar']:5.2f}"
    if bh is not None:
        base+=f"   | B&H: Ret={bh['ret']*100:+9.1f}%  MDD={bh['mdd']*100:6.1f}%  Sharpe={bh['sharpe']:5.2f}  MAR={bh['mar']:5.2f}"
    print(base)

def main():
    print("="*120)
    bnb=load_coin("BNBUSDT")
    warm=max(BASE["N"],BASE["sma_len"],15)
    print(f"BNB: {len(bnb)} velas | {str(bnb.Date.iloc[0])[:10]} -> {str(bnb.Date.iloc[-1])[:10]}\n")

    print("### T1 — ¿bate a comprar-y-aguantar BNB? (ajustado por riesgo, el decisivo)")
    s=strat_stats(bnb, **BASE); bh=bh_stats(bnb, warm)
    line("Estrategia BNB", s, bh)
    t1_pasa = (s["sharpe"]>bh["sharpe"]) or (s["mar"]>bh["mar"])
    print(f"    -> {'PASA' if t1_pasa else 'MATA (no mejora Sharpe ni MAR del hold = beta con pasos extra)'}\n")

    print("### T2 — ¿generaliza a otros activos? (¿fue elegido BNB?)")
    for sym in ["BTCUSDT","ETHUSDT","ADAUSDT","XRPUSDT","LTCUSDT"]:
        try:
            df=load_coin(sym); s2=strat_stats(df, **BASE); bh2=bh_stats(df, warm)
            gana = "gana-hold" if (s2["sharpe"]>bh2["sharpe"] or s2["mar"]>bh2["mar"]) else "NO-gana-hold"
            line(f"{sym[:-4]}", s2, bh2); print(f"        {gana}")
        except FileNotFoundError:
            print(f"{sym}: falta datos/{sym}_1d.csv")
    print()

    print("### T3 — sensibilidad de parametros (¿meseta o pico? sobre BNB full)")
    for N in [10,15,20,30,40]:
        row=[]
        for am in [2.0,2.5,3.0]:
            s3=strat_stats(bnb, **{**BASE,"N":N,"atr_mult":am})
            row.append(f"atr{am}:Ret{s3['ret']*100:+6.0f}%/Sh{s3['sharpe']:.2f}")
        print(f"  N={N:2d}  "+" | ".join(row))
    for sm in [100,200,300]:
        s3=strat_stats(bnb, **{**BASE,"sma_len":sm})
        print(f"  SMA={sm:3d}  Ret={s3['ret']*100:+7.1f}%  Sharpe={s3['sharpe']:.2f}  n={s3['n']}")
    print()

    print("### T4 — significancia y concentracion")
    tr=s["tr"]
    if len(tr):
        top=tr.reindex(tr.pnl.abs().sort_values(ascending=False).index)
        net=tr.pnl.sum()
        for k in (1,3,5):
            print(f"  top-{k} trades = {top.head(k).pnl.sum()/net*100:5.1f}% del neto")
        print(f"  n={len(tr)}  win rate={(tr.pnl>0).mean()*100:.1f}%")
    print()

    print("### T5 — OOS por tiempo (ultimo 30% como lockbox)")
    split=int(len(bnb)*0.70)
    soos=strat_stats(bnb, i0=split, **BASE)
    bhoos=bh_stats(bnb.iloc[split:].reset_index(drop=True), warm)
    line("Estrategia OOS", soos);
    print(f"    OOS desde {str(bnb.Date.iloc[split])[:10]}  (B&H OOS Ret={bhoos['ret']*100:+.1f}% Sharpe={bhoos['sharpe']:.2f})")

if __name__=="__main__":
    main()
