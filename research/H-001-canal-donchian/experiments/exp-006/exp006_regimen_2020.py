#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
exp-006 — Fuera de muestra por tiempo: regimen 2020 (crash covid).

Pregunta pre-registrada (exp-006/PREREG.md): ¿la firma de SEGURO de la cesta
—alfa sobre el buy&hold Y drawdown muy inferior— sobrevive en un regimen
anterior y NO visto (2020: covid + arranque del bull)?

Requiere haber corrido antes 'descargar_historia.py' (crea *_15m_84m.csv).
Usa SOLO velas ANTERIORES al corte 2021-07-22 (periodo que la estrategia nunca uso).

Corre DOS baskets (fix 2026-07-07: la interseccion de las 5 arrancaba en 2020-09
por SOL/DOGE y se perdia el covid):
  - cesta-covid: monedas con perp ANTES de 2020-06 (BTC/ETH/BCH) -> captura marzo 2020.
  - cesta-todas: todas las que tengan historia pre-2021 (ventana mas corta).

Criterio pre-escrito (basket combinado, ventana pre-corte):
  SOBREVIVE : (net>0 o alpha>0) Y maxDD <= 50% del maxDD del B&H equiponderado.
  BANDERA   : net<0 Y sin ventaja de drawdown sobre B&H.
  Limite: un regimen mas, cripto correlacionado, pocas monedas. No zanja significancia.

Motor: identico a exp-002/004/005, 512/256, riesgo uniforme 0.001, funding 0.01%/8h.
"""
import os, json
from datetime import datetime, timezone
from pathlib import Path
from functools import reduce
import numpy as np, pandas as pd

CACHE = Path(os.getenv("DONCHIAN_CACHE", r"D:\ESTRATEGIA_ALEX\crypto_iid_rango\backtest\cache"))
OUT = Path(__file__).resolve().parent
ENTRY_LEN, EXIT_LEN, ATR_LEN, ATR_MULT, MAXLEV, TAKER = 512, 256, 14, 3.0, 3.0, 0.0006
BARS_8H = 32
FUNDING_8H = 0.0001
RISK = 0.001
SUF = "84m"
CUT = pd.Timestamp("2021-07-22", tz="UTC")
COVID_ANTES = pd.Timestamp("2020-06-01", tz="UTC")   # existir antes de esto = tener el crash de marzo 2020
MIN_BARS_PRE = 600
SLIP = {"BTCUSDT":0.0001,"ETHUSDT":0.0001,"SOLUSDT":0.0003,"BCHUSDT":0.0002,"DOGEUSDT":0.0004}
CANDIDATOS = list(SLIP.keys())

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
    pv=np.full(n,equity0); start=max(ENTRY_LEN,ATR_LEN)+1
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
        op=sum(units[s]*(px[s][i]-entry[s])*pos[s] for s in basket if pos[s]!=0)
        pv[i]=eq+op
    pv[:start]=equity0
    netv=pv[-1]/equity0-1
    bh=float(np.mean([px[s][-1]/px[s][start]-1 for s in basket]))
    ec=pd.Series(pv,index=master); dd=(ec/ec.cummax()-1).min(); rr=ec.pct_change().dropna()
    sh=(rr.mean()/rr.std()*np.sqrt(96*365)) if rr.std()>0 else 0.0
    calmar=netv/abs(dd) if dd<0 else float("nan")
    return dict(net=netv,bh=bh,alpha=netv-bh,maxdd=dd,sharpe=sh,calmar=calmar,n=len(master),start=start)

def bh_dd_equiponderado(px, basket, start):
    curves=[px[s][start:]/px[s][start] for s in basket]
    ec=pd.Series(np.mean(curves, axis=0)); return (ec/ec.cummax()-1).min()

def evaluar(raw, basket):
    master=reduce(lambda a,b:a.intersection(b),[raw[s].index for s in basket])
    ind={}; px={}
    for s in basket:
        d=raw[s].reindex(master); ind[s]=indicators(d); px[s]=d["close"].values
    m=run_cesta(master, ind, px, basket, {s:SLIP[s] for s in basket})
    bhdd=bh_dd_equiponderado(px, basket, m["start"])
    ventaja = abs(m["maxdd"]) <= 0.5*abs(bhdd)
    up = (m["net"]>0 or m["alpha"]>0)
    if up and ventaja: ver="SOBREVIVE (mantiene firma de seguro)"
    elif (m["net"]<0) and not ventaja: ver="BANDERA (sin cobertura en crash real)"
    else: ver="INTERMEDIO (parcial)"
    return m, bhdd, ventaja, up, ver, master

def main():
    raw={}
    for s in CANDIDATOS:
        f=CACHE/f"{s}_15m_{SUF}.csv"
        if not f.exists():
            print(f"[!] falta {f.name} — corre descargar_historia.py primero", flush=True); continue
        df=pd.read_csv(f,parse_dates=["dt"]).set_index("dt").sort_index()
        pre=df[df.index < CUT]
        if len(pre) >= MIN_BARS_PRE:
            raw[s]=pre
            print(f"{s}: {len(pre)} velas PRE-2021 (desde {pre.index[0]:%Y-%m-%d})", flush=True)
        else:
            print(f"{s}: solo {len(pre)} velas pre-2021 -> EXCLUIDA", flush=True)
    if not raw:
        print("Sin monedas con historia pre-2021. Aborta."); return
    todas=list(raw.keys())
    covid=[s for s in raw if raw[s].index[0] < COVID_ANTES]   # existian antes de marzo-2020
    L=[f"# exp-006 — regimen 2020 (OOS por tiempo) — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC\n",
       "Regla congelada 512/256, riesgo 0.001. Ventana = SOLO pre-corte (2021-07-22), no vista.\n"]
    resumen={}
    for etiqueta, basket in [("cesta-covid (BTC/ETH/BCH, captura marzo-2020)", covid),
                             ("cesta-todas (ventana corta desde la ultima moneda)", todas)]:
        if not basket:
            L.append(f"## {etiqueta}\nSin monedas para este basket.\n"); continue
        m,bhdd,ventaja,up,ver,master=evaluar(raw,basket)
        resumen[etiqueta]={"ver":ver,"m":m,"bh_maxdd":bhdd,"basket":basket}
        L += [f"## {etiqueta}",
              f"Basket: **{', '.join(basket)}** ({len(master)} velas, {master[0]:%Y-%m-%d} → {master[-1]:%Y-%m-%d})\n",
              "| metrica | estrategia | buy&hold equipond. |","|---|---|---|",
              f"| NET% | {m['net']*100:.2f} | {m['bh']*100:.2f} |",
              f"| maxDD% | {m['maxdd']*100:.1f} | {bhdd*100:.1f} |",
              f"| Sharpe | {m['sharpe']:.2f} | — |",
              f"| alpha% | {m['alpha']*100:.2f} | — |",
              f"\n**VEREDICTO: {ver}** — ventaja DD (≤50% B&H): {'SÍ' if ventaja else 'NO'} ({m['maxdd']*100:.1f}% vs {bhdd*100:.1f}%); net>0 o alpha>0: {'SÍ' if up else 'NO'}\n"]
        print(f"{etiqueta}: {ver} | net {m['net']*100:.1f}% DD {m['maxdd']*100:.1f}% (B&H {bhdd*100:.1f}%) Sharpe {m['sharpe']:.2f}", flush=True)
    L.append("Límite: cripto correlacionado, pocas monedas, un régimen más — NO zanja significancia. La **cesta-covid** (BTC/ETH/BCH) es la que prueba de verdad el crash de marzo 2020; la cesta-todas arranca en 2020-09 y NO lo incluye.")
    (OUT/"RESULTADO.md").write_text("\n".join(L), encoding="utf-8")
    (OUT/"metricas.json").write_text(json.dumps(resumen, indent=1, default=float))
    print("\n".join(L))

if __name__=="__main__":
    main()
