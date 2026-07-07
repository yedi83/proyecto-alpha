#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
exp-005 — Fuera de muestra por activo + descomposicion largo/corto.

Pregunta pre-registrada (exp-005/PREREG.md): ¿el edge del 512 generaliza a
monedas que el diseno NUNCA toco? Regla congelada, aplicada standalone a 7
monedas, en 3 modos (combinado/largo/corto), sobre 'full' propio y '2426' comun.

  HYPE = LIMPIO (nunca mirado) -> el juez.
  NEAR = CONTAMINADO (probado y rechazado) -> contexto.
  BTC/ETH/SOL/BCH/DOGE = referencia dentro de muestra.

Criterio (FULL/2426, HYPE combinado): net>0 y alpha>0 = generaliza (buena senal);
net<=0 o alpha<=0 = bandera. Limite: n=1 moneda, ~2 anios -> orientativo.

Motor: identico a exp-002/004, con ENTRY_LEN=512/EXIT_LEN=256 congelado y un
filtro de lado (both/long/short) que solo bloquea las ENTRADAS del lado excluido.
"""
import os, json
from datetime import datetime, timezone
from pathlib import Path
import numpy as np, pandas as pd

CACHE = Path(os.getenv("DONCHIAN_CACHE", r"D:\ESTRATEGIA_ALEX\crypto_iid_rango\backtest\cache"))
OUT = Path(__file__).resolve().parent
ENTRY_LEN, EXIT_LEN, ATR_LEN, ATR_MULT, MAXLEV, TAKER = 512, 256, 14, 3.0, 3.0, 0.0006
BARS_8H = 32
FUNDING_8H = 0.0001
RISK = 0.001
# symbol: (sufijo_archivo, slippage, etiqueta)
SYMS = {
    "BTCUSDT": ("60m", 0.0001, "IS"),
    "ETHUSDT": ("60m", 0.0001, "IS"),
    "SOLUSDT": ("60m", 0.0003, "IS"),
    "BCHUSDT": ("60m", 0.0002, "IS"),
    "DOGEUSDT":("60m", 0.0004, "IS"),
    "NEARUSDT":("60m", 0.0004, "CONTAM"),
    "HYPEUSDT":("24m", 0.0004, "OOS-LIMPIO"),
}
W2426 = ("2024-07-05", "2026-06-21")

def indicators(df):
    h=df["high"].values; l=df["low"].values; c=df["close"].values
    upper=pd.Series(h).rolling(ENTRY_LEN).max().shift(1).values
    lower=pd.Series(l).rolling(ENTRY_LEN).min().shift(1).values
    exit_low=pd.Series(l).rolling(EXIT_LEN).min().shift(1).values
    exit_high=pd.Series(h).rolling(EXIT_LEN).max().shift(1).values
    tr=np.maximum.reduce([h[1:]-l[1:],np.abs(h[1:]-c[:-1]),np.abs(l[1:]-c[:-1])])
    atr=pd.Series(np.concatenate([[np.nan],tr])).rolling(ATR_LEN).mean().values
    return h,l,c,upper,lower,exit_low,exit_high,atr

def load_one(sym, suf, w0=None, w1=None):
    df=pd.read_csv(CACHE/f"{sym}_15m_{suf}.csv",parse_dates=["dt"]).set_index("dt").sort_index()
    if w0 is not None: df=df.loc[w0:w1]
    return df

def run_single(ind, close, slip, sides, equity0=10000.0, entry_pen=0.0005, stop_pen=0.0010):
    """Motor de exp-002 para UNA moneda, con filtro de lado en la ENTRADA."""
    cs=TAKER+slip; n=len(close); fb=FUNDING_8H/BARS_8H; eq=equity0
    pos=0; entry=0.0; units=0.0; satr=0.0
    pv=np.full(n,equity0); start=max(ENTRY_LEN,ATR_LEN)+1
    h,l,c,up,lo,exlo,exhi,atr=ind
    for i in range(start,n):
        if pos!=0: eq-=units*close[i]*fb
        if up[i]!=up[i] or atr[i]!=atr[i]:
            pv[i]=eq+(units*(close[i]-entry)*pos if pos!=0 else 0.0); continue
        if pos==1:
            stop=max(entry-ATR_MULT*satr, exlo[i] if exlo[i]==exlo[i] else -1e18)
            if l[i]<=stop:
                p=stop*(1-slip-stop_pen); eq+=units*(p-entry)-units*p*cs; pos=0
        elif pos==-1:
            stop=min(entry+ATR_MULT*satr, exhi[i] if exhi[i]==exhi[i] else 1e18)
            if h[i]>=stop:
                p=stop*(1+slip+stop_pen); eq+=units*(entry-p)-units*p*cs; pos=0
        lsig=c[i]>up[i]; ssig=c[i]<lo[i]
        if pos==1 and ssig:
            p=c[i]*(1-slip); eq+=units*(p-entry)-units*p*cs; pos=0
        elif pos==-1 and lsig:
            p=c[i]*(1+slip); eq+=units*(entry-p)-units*p*cs; pos=0
        if pos==0 and (lsig or ssig):
            d_=1 if lsig else -1
            if not ((sides=="both") or (sides=="long" and d_==1) or (sides=="short" and d_==-1)):
                pv[i]=eq; continue
            sd=ATR_MULT*atr[i]
            if sd<=0: pv[i]=eq; continue
            u=min((eq*RISK)/sd, eq*MAXLEV/c[i])
            p=c[i]*(1+(slip+entry_pen)*d_); eq-=u*p*cs
            pos=d_; entry=p; units=u; satr=atr[i]
        pv[i]=eq+(units*(close[i]-entry)*pos if pos!=0 else 0.0)
    pv[:start]=equity0
    netv=pv[-1]/equity0-1
    bh=close[-1]/close[start]-1
    ec=pd.Series(pv); dd=(ec/ec.cummax()-1).min(); rr=ec.pct_change().dropna()
    sh=(rr.mean()/rr.std()*np.sqrt(96*365)) if rr.std()>0 else 0.0
    calmar=netv/abs(dd) if dd<0 else float("nan")
    return dict(net=netv,bh=bh,alpha=netv-bh,maxdd=dd,sharpe=sh,calmar=calmar)

def main():
    res={}
    for sym,(suf,slip,tag) in SYMS.items():
        for wname in ("full","2426"):
            df = load_one(sym, suf, *( (None,None) if wname=="full" else (pd.Timestamp(W2426[0],tz="UTC"),pd.Timestamp(W2426[1],tz="UTC")) ))
            if len(df) < max(ENTRY_LEN,ATR_LEN)+50:
                continue
            ind=indicators(df); close=df["close"].values
            for sides in ("both","long","short"):
                m=run_single(ind, close, slip, sides)
                res[f"{sym}|{wname}|{sides}"]=m
                print(f"{tag:11s} {sym:9s} {wname:4s} {sides:5s} NET {m['net']*100:8.2f}%  "
                      f"maxDD {m['maxdd']*100:6.1f}%  Sharpe {m['sharpe']:6.2f}  alpha {m['alpha']*100:7.2f}%", flush=True)
    # ---- veredicto sobre HYPE (limpio), combinado ----
    def g(sym,w,s): return res.get(f"{sym}|{w}|{s}")
    hy = g("HYPEUSDT","full","both") or g("HYPEUSDT","2426","both")
    if hy is None:
        ver="SIN DATOS de HYPE — revisar cache"
    elif hy["net"]>0 and hy["alpha"]>0:
        ver="GENERALIZA (HYPE net>0 y alpha>0) — buena señal, pero n=1"
    else:
        ver="BANDERA (HYPE net<=0 o alpha<=0) — no generaliza en este único caso"
    # ---- informe ----
    L=[f"# exp-005 — OOS por activo + largo/corto — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC\n",
       "Regla congelada 512/256, riesgo 0.001, standalone por moneda. HYPE = limpio; NEAR = contaminado; 5 majors = dentro de muestra.\n",
       "| etiqueta | moneda | ventana | lado | NET% | maxDD% | Sharpe | alpha% |","|---|---|---|---|---|---|---|---|"]
    for k,m in res.items():
        sym,w,s=k.split("|"); tag=SYMS[sym][2]
        L.append(f"| {tag} | {sym} | {w} | {s} | {m['net']*100:.2f} | {m['maxdd']*100:.1f} | {m['sharpe']:.2f} | {m['alpha']*100:.2f} |")
    L.append(f"\n## VEREDICTO (criterio pre-escrito, HYPE combinado): **{ver}**\n")
    if hy: L.append(f"- HYPE combinado: net {hy['net']*100:.2f}% · alpha {hy['alpha']*100:.2f}% · Sharpe {hy['sharpe']:.2f} · maxDD {hy['maxdd']*100:.1f}%")
    L.append("- Límite: n=1 moneda, ~2 años. Orientativo, NO cierra H-001. El árbitro limpio final es forward sobre precios reales.")
    L.append("- Largo/corto: descriptivo. NO se decide quitar ningún lado a partir de esto.")
    (OUT/"RESULTADO.md").write_text("\n".join(L), encoding="utf-8")
    (OUT/"metricas.json").write_text(json.dumps({"veredicto":ver,"res":res}, indent=1, default=float))
    print("\n".join(L))

if __name__=="__main__":
    main()
