#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
exp-004 — Sensibilidad del largo del canal (384 / 512 / 640).

Pregunta pre-registrada (exp-004/PREREG.md): ¿el largo 512 es una MESETA
(edge estructural robusto al lookback) o un PICO aislado (sobreajuste)?
Test de ROBUSTEZ, NO de optimizacion: 512 NO se cambia pase lo que pase.

Motor: copia congelada de exp-002 (run_cesta_map, lab 2026-06-25). UNICO cambio
frente a exp-002: en vez de variar el riesgo, se varia ENTRY_LEN/EXIT_LEN
(exit escalado ÷2). Riesgo FIJO uniforme 0.001 (config validada = base 1.353).

Paridad: la corrida 512/256 debe reproducir FRONTIER 0.10%-off (FULL: NET ~+24,
maxDD ~-17.8, Sharpe ~0.42). Sin paridad, el experimento es INVALIDO.

Criterio por capas (PRE-ESCRITO, en FULL, sobre cada vecino 384 y 640):
  MATA H-001     : net <= 0  o  alpha <= 0
  FRAGIL         : Calmar < 50% del 512
  MESETA         : ambos con Calmar >= 70% del 512  y  Sharpe >= base-0.10  y net,alpha>0
  INTERMEDIA     : resto -> caveat documentado

Datos: cache 15m_60m (origen lab). Funding 0.01%/8h. stop_fill='stop'.
"""
import os, json
from datetime import datetime, timezone
from pathlib import Path
from functools import reduce
import numpy as np, pandas as pd

CACHE = Path(os.getenv("DONCHIAN_CACHE", r"D:\ESTRATEGIA_ALEX\crypto_iid_rango\backtest\cache"))
OUT = Path(__file__).resolve().parent
BASKET = ["BTCUSDT","ETHUSDT","SOLUSDT","BCHUSDT","DOGEUSDT"]
ATR_LEN, ATR_MULT, MAXLEV, TAKER = 14, 3.0, 3.0, 0.0006
SLIP = {"BTCUSDT":0.0001,"ETHUSDT":0.0001,"BCHUSDT":0.0002,"SOLUSDT":0.0003,"DOGEUSDT":0.0004}
BARS_8H = 32
WINDOWS = {"full":("2021-07-22","2026-06-21"),"2123":("2021-07-22","2023-06-30"),
           "2426":("2024-07-05","2026-06-21")}
FUNDING_8H = 0.0001                                   # 0.01%/8h
RISK = {s: 0.001 for s in BASKET}                     # uniforme = config validada (base 1.353)
LENGTHS = [(384,192),(512,256),(640,320)]             # (ENTRY_LEN, EXIT_LEN), exit escalado ÷2

def indicators(df, entry_len, exit_len):
    h=df["high"].values; l=df["low"].values; c=df["close"].values
    upper=pd.Series(h).rolling(entry_len).max().shift(1).values
    lower=pd.Series(l).rolling(entry_len).min().shift(1).values
    exit_low=pd.Series(l).rolling(exit_len).min().shift(1).values
    exit_high=pd.Series(h).rolling(exit_len).max().shift(1).values
    tr=np.maximum.reduce([h[1:]-l[1:],np.abs(h[1:]-c[:-1]),np.abs(l[1:]-c[:-1])])
    atr=pd.Series(np.concatenate([[np.nan],tr])).rolling(ATR_LEN).mean().values
    return h,l,c,upper,lower,exit_low,exit_high,atr

def load_raw(w0, w1):
    raw={s:pd.read_csv(CACHE/(s+"_15m_60m.csv"),parse_dates=["dt"]).set_index("dt").sort_index().loc[w0:w1] for s in BASKET}
    master=reduce(lambda a,b:a.intersection(b),[df.index for df in raw.values()])
    return master, {s: raw[s].reindex(master) for s in BASKET}

def build_ind(d, entry_len, exit_len):
    ind={}; px={}
    for s in BASKET:
        ind[s]=indicators(d[s], entry_len, exit_len); px[s]=d[s]["close"].values
    return ind, px

def run_cesta_map(master, ind, px, risk_map, entry_len, equity0=10000.0,
                  entry_pen=0.0005, stop_pen=0.0010):
    """Copia de run_cesta (exp-002) con ENTRY_LEN parametrico. stop_fill='stop'."""
    CS={s:TAKER+SLIP[s] for s in BASKET}
    n=len(master); fb=FUNDING_8H/BARS_8H; eq=equity0
    pos={s:0 for s in BASKET}; entry={s:0.0 for s in BASKET}
    units={s:0.0 for s in BASKET}; satr={s:0.0 for s in BASKET}
    pv=np.full(n,equity0); start=max(entry_len,ATR_LEN)+1
    for i in range(start,n):
        for s in BASKET:
            if pos[s]!=0: eq-=units[s]*px[s][i]*fb
            h,l,c,up,lo,exlo,exhi,atr=ind[s]
            if up[i]!=up[i] or atr[i]!=atr[i]: continue
            cs=CS[s]
            if pos[s]==1:
                stop=max(entry[s]-ATR_MULT*satr[s], exlo[i] if exlo[i]==exlo[i] else -1e18)
                if l[i]<=stop:
                    p=stop*(1-SLIP[s]-stop_pen); eq+=units[s]*(p-entry[s])-units[s]*p*cs; pos[s]=0
            elif pos[s]==-1:
                stop=min(entry[s]+ATR_MULT*satr[s], exhi[i] if exhi[i]==exhi[i] else 1e18)
                if h[i]>=stop:
                    p=stop*(1+SLIP[s]+stop_pen); eq+=units[s]*(entry[s]-p)-units[s]*p*cs; pos[s]=0
            lsig=c[i]>up[i]; ssig=c[i]<lo[i]
            if pos[s]==1 and ssig:
                p=c[i]*(1-SLIP[s]); eq+=units[s]*(p-entry[s])-units[s]*p*cs; pos[s]=0
            elif pos[s]==-1 and lsig:
                p=c[i]*(1+SLIP[s]); eq+=units[s]*(entry[s]-p)-units[s]*p*cs; pos[s]=0
            if pos[s]==0 and (lsig or ssig):
                d_=1 if lsig else -1; sd=ATR_MULT*atr[i]
                if sd<=0: continue
                u=min((eq*risk_map[s])/sd, eq*MAXLEV/c[i])
                p=c[i]*(1+(SLIP[s]+entry_pen)*d_); eq-=u*p*cs
                pos[s]=d_; entry[s]=p; units[s]=u; satr[s]=atr[i]
        op=sum(units[s]*(px[s][i]-entry[s])*pos[s] for s in BASKET if pos[s]!=0)
        pv[i]=eq+op
    pv[:start]=equity0
    netv=pv[-1]/equity0-1
    bh=float(np.mean([px[s][-1]/px[s][start]-1 for s in BASKET]))
    ec=pd.Series(pv,index=master); dd=(ec/ec.cummax()-1).min(); rr=ec.pct_change().dropna()
    sh=(rr.mean()/rr.std()*np.sqrt(96*365)) if rr.std()>0 else 0.0
    calmar=netv/abs(dd) if dd<0 else float("nan")
    return dict(net=netv,bh=bh,alpha=netv-bh,maxdd=dd,sharpe=sh,calmar=calmar)

def veredicto_vecino(nb, base):
    """Criterio por capas del PREREG, en FULL, para un vecino vs base(512)."""
    if nb["net"]<=0 or nb["alpha"]<=0: return "MATA"
    if nb["calmar"] < 0.50*base["calmar"]: return "FRAGIL"
    if (nb["calmar"] >= 0.70*base["calmar"] and nb["sharpe"] >= base["sharpe"]-0.10
            and nb["net"]>0 and nb["alpha"]>0): return "MESETA"
    return "INTERMEDIA"

def main():
    res={}
    for wname,(a,b) in WINDOWS.items():
        master, d = load_raw(pd.Timestamp(a,tz="UTC"), pd.Timestamp(b,tz="UTC"))
        for (el,xl) in LENGTHS:
            ind, px = build_ind(d, el, xl)
            m = run_cesta_map(master, ind, px, RISK, el)
            res[f"{wname}/{el}"] = m
            print(f"{wname:5s} L{el:<3d} NET {m['net']*100:7.2f}%  maxDD {m['maxdd']*100:6.1f}%  "
                  f"Sharpe {m['sharpe']:.2f}  Calmar {m['calmar']:.2f}", flush=True)
    # ---- paridad: full/512 debe reproducir FRONTIER 0.10%-off ----
    f=res["full/512"]
    paridad = abs(f["net"]-0.24)<0.05 and abs(f["maxdd"]+0.178)<0.03 and abs(f["sharpe"]-0.42)<0.08
    # ---- criterio por capas (FULL) ----
    base=res["full/512"]; n384=res["full/384"]; n640=res["full/640"]
    v384=veredicto_vecino(n384, base); v640=veredicto_vecino(n640, base)
    if "MATA" in (v384,v640):        ver="H-001 MATADA (edge no robusto al lookback)"
    elif "FRAGIL" in (v384,v640):    ver="FRAGILIDAD SERIA (512 es un pico)"
    elif v384=="MESETA" and v640=="MESETA": ver="MESETA ROBUSTA (H-001 sobrevive)"
    else:                            ver="INTERMEDIA (caveat documentado)"
    # ---- informe ----
    L=[f"# exp-004 — sensibilidad de lookback (384/512/640) — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC\n",
       f"Paridad full/512 vs FRONTIER 0.10%-off: {'✅ OK' if paridad else '🔴 FALLA — experimento INVÁLIDO, revisar código/datos'}\n",
       "Riesgo uniforme 0.001 fijo; único eje = largo del canal (exit escalado ÷2).\n",
       "| ventana | largo | NET% | maxDD% | Sharpe | Calmar |","|---|---|---|---|---|---|"]
    for k,m in res.items():
        L.append(f"| {k.split('/')[0]} | {k.split('/')[1]} | {m['net']*100:.2f} | {m['maxdd']*100:.1f} | {m['sharpe']:.2f} | {m['calmar']:.2f} |")
    L.append(f"\n## VEREDICTO (criterio por capas, FULL): **{ver}**\n")
    L.append(f"- Base 512 FULL: Calmar {base['calmar']:.3f} · Sharpe {base['sharpe']:.3f} · net {base['net']*100:.2f}% · alpha {base['alpha']*100:.2f}%")
    L.append(f"- Vecino 384: Calmar {n384['calmar']:.3f} ({n384['calmar']/base['calmar']*100:.0f}% del base) · Sharpe {n384['sharpe']:.3f} · net {n384['net']*100:.2f}% · alpha {n384['alpha']*100:.2f}% → **{v384}**")
    L.append(f"- Vecino 640: Calmar {n640['calmar']:.3f} ({n640['calmar']/base['calmar']*100:.0f}% del base) · Sharpe {n640['sharpe']:.3f} · net {n640['net']*100:.2f}% · alpha {n640['alpha']*100:.2f}% → **{v640}**")
    L.append(f"\nUmbrales: MESETA≥70% Calmar ({0.70*base['calmar']:.3f}) y Sharpe≥{base['sharpe']-0.10:.3f}; FRÁGIL<50% Calmar ({0.50*base['calmar']:.3f}); MATA si net≤0 o alpha≤0.")
    L.append("\n**Recordatorio:** 512 NO se cambia. Un vecino mejor = meseta, no razón para re-optimizar.")
    if not paridad: L.append("\n⚠️ SIN paridad la comparación no es evidencia. No usar.")
    (OUT/"RESULTADO.md").write_text("\n".join(L), encoding="utf-8")
    (OUT/"metricas.json").write_text(json.dumps(
        {"paridad":bool(paridad),"veredicto":ver,"v384":v384,"v640":v640,"res":res}, indent=1, default=float))
    print("\n".join(L))

if __name__=="__main__":
    main()
