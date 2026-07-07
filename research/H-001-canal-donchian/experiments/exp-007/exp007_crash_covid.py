#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
exp-007 — Comportamiento en el crash de covid (aislado). P3.

Pregunta pre-registrada (exp-007/PREREG.md): ¿la estrategia PROTEGE durante el
flash crash del covid (marzo 2020), o queda atrapada? Un trend-follower lento
protege bien en bears lentos; el covid fue de un dia.

Requiere *_15m_84m.csv (descargar_historia.py). BTC/ETH/BCH (los que existian).
Warmup desde 2019-12; se MIDE solo la ventana del crash (calendario, no peeking).

Criterio: PROTEGE si ret_estrategia >> B&H y maxDD_estrategia <= 1/3 del B&H
(idealmente exposicion neta <=0 en los dias del desplome). NO PROTEGE si cae
parecido al B&H. Ilustrativo del mecanismo, no prueba estadistica.
"""
import os, json
from datetime import datetime, timezone
from pathlib import Path
from functools import reduce
import numpy as np, pandas as pd

CACHE = Path(os.getenv("DONCHIAN_CACHE", r"D:\ESTRATEGIA_ALEX\crypto_iid_rango\backtest\cache"))
OUT = Path(__file__).resolve().parent
ENTRY_LEN, EXIT_LEN, ATR_LEN, ATR_MULT, MAXLEV, TAKER = 512, 256, 14, 3.0, 3.0, 0.0006
BARS_8H = 32; FUNDING_8H = 0.0001; RISK = 0.001; SUF = "84m"
SLIP = {"BTCUSDT":0.0001,"ETHUSDT":0.0001,"BCHUSDT":0.0002}
BASKET = list(SLIP.keys())
DATA_HASTA = pd.Timestamp("2020-07-01", tz="UTC")
CRASH = (pd.Timestamp("2020-02-14",tz="UTC"), pd.Timestamp("2020-04-30",tz="UTC"))
FLASH = (pd.Timestamp("2020-03-08",tz="UTC"), pd.Timestamp("2020-03-20",tz="UTC"))

def indicators(df):
    h=df["high"].values; l=df["low"].values; c=df["close"].values
    upper=pd.Series(h).rolling(ENTRY_LEN).max().shift(1).values
    lower=pd.Series(l).rolling(ENTRY_LEN).min().shift(1).values
    exit_low=pd.Series(l).rolling(EXIT_LEN).min().shift(1).values
    exit_high=pd.Series(h).rolling(EXIT_LEN).max().shift(1).values
    tr=np.maximum.reduce([h[1:]-l[1:],np.abs(h[1:]-c[:-1]),np.abs(l[1:]-c[:-1])])
    atr=pd.Series(np.concatenate([[np.nan],tr])).rolling(ATR_LEN).mean().values
    return h,l,c,upper,lower,exit_low,exit_high,atr

def run_cesta(master, ind, px, basket, slipm, equity0=10000.0, entry_pen=0.0005, stop_pen=0.0010):
    CS={s:TAKER+slipm[s] for s in basket}
    n=len(master); fb=FUNDING_8H/BARS_8H; eq=equity0
    pos={s:0 for s in basket}; entry={s:0.0 for s in basket}
    units={s:0.0 for s in basket}; satr={s:0.0 for s in basket}
    pv=np.full(n,equity0); expo=np.zeros(n); start=max(ENTRY_LEN,ATR_LEN)+1
    for i in range(start,n):
        for s in basket:
            if pos[s]!=0: eq-=units[s]*px[s][i]*fb
            h,l,c,up,lo,exlo,exhi,atr=ind[s]
            if up[i]!=up[i] or atr[i]!=atr[i]: continue
            cs=CS[s]; sl=slipm[s]
            if pos[s]==1:
                stop=max(entry[s]-ATR_MULT*satr[s], exlo[i] if exlo[i]==exlo[i] else -1e18)
                if l[i]<=stop:
                    p=stop*(1-sl-stop_pen); eq+=units[s]*(p-entry[s])-units[s]*p*cs; pos[s]=0
            elif pos[s]==-1:
                stop=min(entry[s]+ATR_MULT*satr[s], exhi[i] if exhi[i]==exhi[i] else 1e18)
                if h[i]>=stop:
                    p=stop*(1+sl+stop_pen); eq+=units[s]*(entry[s]-p)-units[s]*p*cs; pos[s]=0
            lsig=c[i]>up[i]; ssig=c[i]<lo[i]
            if pos[s]==1 and ssig:
                p=c[i]*(1-sl); eq+=units[s]*(p-entry[s])-units[s]*p*cs; pos[s]=0
            elif pos[s]==-1 and lsig:
                p=c[i]*(1+sl); eq+=units[s]*(entry[s]-p)-units[s]*p*cs; pos[s]=0
            if pos[s]==0 and (lsig or ssig):
                d_=1 if lsig else -1; sd=ATR_MULT*atr[i]
                if sd<=0: continue
                u=min((eq*RISK)/sd, eq*MAXLEV/c[i])
                p=c[i]*(1+(sl+entry_pen)*d_); eq-=u*p*cs
                pos[s]=d_; entry[s]=p; units[s]=u; satr[s]=atr[i]
        signed=sum(units[s]*px[s][i]*pos[s] for s in basket if pos[s]!=0)
        op=sum(units[s]*(px[s][i]-entry[s])*pos[s] for s in basket if pos[s]!=0)
        pv[i]=eq+op; expo[i]= signed/pv[i] if pv[i]>0 else 0.0
    pv[:start]=equity0
    return pv, expo, start

def win(series, master, w0, w1):
    idx=np.where((master>=w0)&(master<=w1))[0]
    if len(idx)<2: return None,None,idx
    seg=np.asarray(series)[idx]
    ret=seg[-1]/seg[0]-1
    dd=(pd.Series(seg)/pd.Series(seg).cummax()-1).min()
    return ret, dd, idx

def main():
    raw={}
    for s in BASKET:
        f=CACHE/f"{s}_15m_{SUF}.csv"
        if not f.exists():
            print(f"[!] falta {f.name} — corre descargar_historia.py"); return
        df=pd.read_csv(f,parse_dates=["dt"]).set_index("dt").sort_index()
        raw[s]=df[df.index < DATA_HASTA]
    master=reduce(lambda a,b:a.intersection(b),[d.index for d in raw.values()])
    ind={}; px={}
    for s in BASKET:
        d=raw[s].reindex(master); ind[s]=indicators(d); px[s]=d["close"].values
    pv, expo, start = run_cesta(master, ind, px, BASKET, SLIP)
    bh_curve=np.mean([px[s]/px[s][start] for s in BASKET], axis=0)
    sret,sdd,cidx = win(pv, master, *CRASH)
    bret,bdd,_    = win(bh_curve, master, *CRASH)
    _,_,fidx = win(pv, master, *FLASH)
    expo_flash = float(np.mean(expo[fidx])) if len(fidx) else float("nan")
    protege = (sret>bret) and (abs(sdd) <= abs(bdd)/3.0)
    if protege: ver="PROTEGE (crisis alpha en crash rápido)"
    elif abs(sdd) >= 0.7*abs(bdd): ver="NO PROTEGE el flash crash (cobertura solo para bears lentos)"
    else: ver="PARCIAL (protege algo, no del todo)"
    # trayectoria semanal en la ventana del crash (normalizada a 100)
    traj=["", "Trayectoria (100 = inicio ventana):", "| fecha | estrategia | buy&hold |","|---|---|---|"]
    p0=pv[cidx[0]]; b0=bh_curve[cidx[0]]
    seen=set()
    for i in cidx:
        wk=master[i].strftime("%Y-%m-%d")
        if master[i].weekday()==0 and wk not in seen:  # lunes
            seen.add(wk); traj.append(f"| {wk} | {pv[i]/p0*100:.1f} | {bh_curve[i]/b0*100:.1f} |")
    L=[f"# exp-007 — crash covid aislado — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC\n",
       f"Basket: **{', '.join(BASKET)}**. Warmup desde {master[start]:%Y-%m-%d}. Ventana crash {CRASH[0]:%Y-%m-%d}→{CRASH[1]:%Y-%m-%d}.\n",
       "| métrica | estrategia | buy&hold equipond. |","|---|---|---|",
       f"| retorno en la ventana% | {sret*100:.2f} | {bret*100:.2f} |",
       f"| maxDD en la ventana% | {sdd*100:.1f} | {bdd*100:.1f} |",
       f"\n- Exposición neta media en los días del desplome ({FLASH[0]:%m-%d}→{FLASH[1]:%m-%d}): **{expo_flash:+.2f}** (>0 largo, <0 corto, ~0 plano)",
       f"\n## VEREDICTO (pre-escrito): **{ver}**\n",
       f"- ret estrategia > B&H: {'SÍ' if sret>bret else 'NO'} ({sret*100:.1f}% vs {bret*100:.1f}%)",
       f"- maxDD estrategia <= 1/3 del B&H: {'SÍ' if abs(sdd)<=abs(bdd)/3 else 'NO'} ({sdd*100:.1f}% vs {bdd*100:.1f}%)",
       "- Límite: un crash, 3 monedas. Ilustra el MECANISMO (protege/atrapado), no prueba edge."]
    L+=traj
    (OUT/"RESULTADO.md").write_text("\n".join(L), encoding="utf-8")
    (OUT/"metricas.json").write_text(json.dumps(
        {"veredicto":ver,"ret_estrategia":sret,"dd_estrategia":sdd,"ret_bh":bret,"dd_bh":bdd,"expo_flash":expo_flash}, indent=1, default=float))
    print("\n".join(L))

if __name__=="__main__":
    main()
