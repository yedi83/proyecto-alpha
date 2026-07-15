#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H-002 VARIANTE (trailing Chandelier) — BANCO. Reutiliza VERBATIM el motor
backtest_2rt del investigador. Mismos tests pre-registrados que la base
(PREREG_BANCO.md): T1 vs buy&hold, T2 cruzado, T3 sensibilidad, T4, T5 OOS.
Se juzga con MAS exigencia (mas parametros, autoflag 'dudosa-favorable').
Requiere datos/*_1d.csv."""
import numpy as np, pandas as pd
from pathlib import Path
DATOS = Path(__file__).resolve().parent / "datos"; EQ0 = 10000.0
VBASE = dict(N=20, atr_mult=2.5, sma_len=200, trigger_r=2.0, lock_r=0.5,
             ch_mult=3.0, ch_len=14, ext_max=10.0, risk=0.0125, fee=0.0004, lev=2.0)

# ================== MOTOR VERBATIM (backtest_2r_trail.py del investigador) ==================
def atr_rma(df, n=14):
    pc = df.Close.shift(1)
    tr = pd.concat([df.High-df.Low,(df.High-pc).abs(),(df.Low-pc).abs()],axis=1).max(axis=1)
    return tr.ewm(alpha=1/n, adjust=False).mean()

def backtest_2rt(df, N=20, atr_mult=2.5, sma_len=200, risk=0.0125,
                 trigger_r=2.0, lock_r=0.5, ch_mult=3.0, ch_len=14, ext_max=10.0,
                 fee=0.0004, lev=2.0, i0=0, i1=None):
    if i1 is None: i1 = len(df)
    o,h,l,c,d = df.Open.values, df.High.values, df.Low.values, df.Close.values, df.Date.values
    A14 = atr_rma(df,14).values; ACH = atr_rma(df,ch_len).values
    hh = df.High.rolling(N).max().shift(1).values
    sma = df.Close.rolling(sma_len).mean().values
    eq = EQ0; trades = []; curve = []; pos = None
    warm = max(N, sma_len, ch_len+1); i = max(i0, warm)
    def close_trade(px, when, tag):
        nonlocal eq, pos
        pnl = pos["qty"]*(px-pos["entry"]) - fee*pos["qty"]*(pos["entry"]+px)
        eq += pnl
        trades.append(dict(entry_date=pos["date"], exit_date=when, res=tag,
                           pnl=pnl, r=pnl/pos["risk_amt"], eq=eq)); pos_clear()
    def pos_clear():
        nonlocal pos; pos=None
    def update_after_close(j):
        pos["hh"] = max(pos["hh"], h[j])
        if not pos["armed"] and h[j] >= pos["trigger_px"]:
            pos["armed"] = True
            pos["stop"] = max(pos["stop"], pos["entry"] + lock_r*pos["dist"])
        if pos["armed"]:
            pos["stop"] = max(pos["stop"], pos["hh"] - ch_mult*ACH[j])
    while i < i1:
        if pos:
            if   o[i] <= pos["stop"]: close_trade(o[i], d[i], "gap")
            elif l[i] <= pos["stop"]: close_trade(pos["stop"], d[i], "stop")
            else: update_after_close(i)
        if pos is None and i+1 < i1 and not np.isnan(hh[i]+sma[i]+A14[i]):
            ok = c[i] > hh[i] and c[i] > sma[i] and A14[i] > 0 and (c[i]-sma[i])/A14[i] <= ext_max
            if ok:
                e = o[i+1]; st = e - atr_mult*A14[i]
                if st > 0:
                    dist = e-st; ra = risk*eq; q = ra/dist
                    if q*e > lev*eq: q = lev*eq/e; ra = q*dist
                    pos = dict(entry=e, stop=st, dist=dist, qty=q, risk_amt=ra, date=d[i+1],
                               hh=e, armed=False, trigger_px=e+trigger_r*dist)
                    j = i+1
                    if l[j] <= pos["stop"]: close_trade(pos["stop"], d[j], "sl")
                    else: update_after_close(j)
                    i = j
        curve.append(eq + (pos["qty"]*(c[i]-pos["entry"]) if pos else 0.0))
        i += 1
    if pos: close_trade(c[i1-1], d[i1-1], "eod")
    return pd.DataFrame(trades), np.array(curve)
# ============================================================================================

def load_coin(sym):
    df = pd.read_csv(DATOS/f"{sym}_1d.csv").rename(columns={
        "dt":"Date","open":"Open","high":"High","low":"Low","close":"Close","volume":"Volume"})
    df["Date"]=pd.to_datetime(df["Date"], errors="coerce", utc=True)
    for c in ["Open","High","Low","Close"]: df[c]=pd.to_numeric(df[c], errors="coerce")
    return df.dropna(subset=["Date","Open","High","Low","Close"]).sort_values("Date").drop_duplicates("Date").reset_index(drop=True)

def stats(curve, dates):
    curve=np.asarray(curve,float)
    if len(curve)<3: return dict(ret=np.nan,mdd=np.nan,sharpe=np.nan,mar=np.nan)
    ret=curve[-1]/curve[0]-1; peak=np.maximum.accumulate(curve); mdd=((curve-peak)/peak).min()
    r=np.diff(curve)/curve[:-1]; sh=r.mean()/r.std()*np.sqrt(365) if r.std()>0 else 0.0
    yrs=(pd.Timestamp(dates[-1])-pd.Timestamp(dates[0])).days/365.25
    cagr=(curve[-1]/curve[0])**(1/yrs)-1 if yrs>0 else np.nan
    return dict(ret=ret,mdd=mdd,sharpe=sh,mar=(cagr/abs(mdd) if mdd<0 else np.nan))

def bh_stats(df,i0):
    c=df.Close.values[i0:]; return stats(c/c[0]*EQ0, df.Date.values[i0:])

def ss(df, i0=0, i1=None, **kw):
    p={**VBASE,**kw}; tr,cv=backtest_2rt(df, i0=i0, i1=(i1 if i1 else len(df)), **p)
    warm=max(p["N"],p["sma_len"],p["ch_len"]+1)
    s=stats(cv, df.Date.values[max(i0,warm):max(i0,warm)+len(cv)]); s["n"]=len(tr); s["tr"]=tr; return s

def line(tag,s,bh=None):
    b=f"{tag:22s} n={s.get('n','-'):>4}  Ret={s['ret']*100:+9.1f}%  MDD={s['mdd']*100:6.1f}%  Sharpe={s['sharpe']:5.2f}  MAR={s['mar']:5.2f}"
    if bh is not None: b+=f"   | B&H: Ret={bh['ret']*100:+9.1f}%  MDD={bh['mdd']*100:6.1f}%  Sharpe={bh['sharpe']:5.2f}  MAR={bh['mar']:5.2f}"
    print(b)

def main():
    print("="*120); print("VARIANTE (2R->BE+colchon->trailing Chandelier)")
    bnb=load_coin("BNBUSDT"); warm=max(VBASE["N"],VBASE["sma_len"],VBASE["ch_len"]+1)
    print(f"BNB: {len(bnb)} velas | {str(bnb.Date.iloc[0])[:10]} -> {str(bnb.Date.iloc[-1])[:10]}\n")
    print("### T1 — vs aguantar BNB (decisivo)")
    s=ss(bnb); bh=bh_stats(bnb,warm); line("Variante BNB", s, bh)
    print(f"    -> {'PASA' if (s['sharpe']>bh['sharpe'] or s['mar']>bh['mar']) else 'MATA (no bate Sharpe ni MAR del hold)'}\n")
    print("### T2 — cruzado (¿generaliza?)")
    for sym in ["BTCUSDT","ETHUSDT","BNBUSDT","ADAUSDT","XRPUSDT","LTCUSDT"]:
        try:
            df=load_coin(sym); s2=ss(df); bh2=bh_stats(df,warm)
            line(sym[:-4], s2, bh2)
            print(f"        {'gana-hold' if (s2['sharpe']>bh2['sharpe'] or s2['mar']>bh2['mar']) else 'NO-gana-hold'}")
        except FileNotFoundError: print(f"{sym}: falta datos")
    print("\n### T3 — sensibilidad (parametros propios de la variante, sobre BNB)")
    for lk in [0.25,0.5,1.0]:
        s3=ss(bnb, lock_r=lk); print(f"  lock_r={lk}: Ret={s3['ret']*100:+7.1f}%  Sharpe={s3['sharpe']:.2f}  MDD={s3['mdd']*100:.1f}%")
    for ch in [2.5,3.0,3.5]:
        s3=ss(bnb, ch_mult=ch); print(f"  ch_mult={ch}: Ret={s3['ret']*100:+7.1f}%  Sharpe={s3['sharpe']:.2f}")
    for tr in [1.5,2.0,2.5]:
        s3=ss(bnb, trigger_r=tr); print(f"  trigger_r={tr}: Ret={s3['ret']*100:+7.1f}%  Sharpe={s3['sharpe']:.2f}")
    print("\n### T4 — significancia y concentracion")
    tr=s["tr"]
    if len(tr):
        top=tr.reindex(tr.pnl.abs().sort_values(ascending=False).index); net=tr.pnl.sum()
        for k in (1,3,5): print(f"  top-{k} = {top.head(k).pnl.sum()/net*100:5.1f}% del neto")
        print(f"  n={len(tr)}  win rate={(tr.pnl>0).mean()*100:.1f}%")
    print("\n### T5 — OOS (ultimo 30%)")
    split=int(len(bnb)*0.70); soos=ss(bnb, i0=split); line("Variante OOS", soos)
    bhoos=bh_stats(bnb.iloc[split:].reset_index(drop=True),warm)
    print(f"    OOS desde {str(bnb.Date.iloc[split])[:10]}  (B&H OOS Sharpe={bhoos['sharpe']:.2f} Ret={bhoos['ret']*100:+.1f}%)")

if __name__=="__main__": main()
