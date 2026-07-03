#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
exp-003 — ¿La cesta tolera riesgo por símbolo (BTC 0.125%, resto 0.10%)?

Pregunta pre-registrada (PAQUETE_FASE_B §1): la decisión M1 ($750, BTC con
riesgo 0.15% para librar el min_notional de producción) modifica la cesta
validada (riesgo uniforme). Este experimento la compara contra la base en las
tres ventanas. Si degrada materialmente (Sharpe o Calmar), la decisión se revisa.

Umbral de decisión (escrito ANTES de correr):
  ACEPTA si, en FULL: Sharpe(btc0125) >= Sharpe(base) - 0.05
                  y  Calmar(btc0125) >= Calmar(base) * 0.85
  y en ninguna ventana el maxDD empeora más de 5 puntos porcentuales.

Código: copia congelada de backtest_cesta.run_cesta (lab, 2026-06-25) con UN
cambio: risk escalar -> RISK_MAP por símbolo. Chequeo de paridad: la config
base debe reproducir la fila '0.10% off' de FRONTIER_VEREDICTO (FULL: NET +24,
maxDD -17.8, Sharpe 0.42) — si no la reproduce, el experimento es inválido.

Datos: cache 15m_60m (origen lab). Funding 0.01%/8h. stop_fill='stop' (default
del análisis original, para comparabilidad).
"""
import os, json
from datetime import datetime, timezone
from pathlib import Path
from functools import reduce
import numpy as np, pandas as pd

CACHE = Path(os.getenv("DONCHIAN_CACHE", r"D:\ESTRATEGIA_ALEX\crypto_iid_rango\backtest\cache"))
OUT = Path(__file__).resolve().parent
BASKET = ["BTCUSDT","ETHUSDT","SOLUSDT","BCHUSDT","DOGEUSDT"]
ENTRY_LEN, EXIT_LEN, ATR_LEN, ATR_MULT, MAXLEV, TAKER = 512, 256, 14, 3.0, 3.0, 0.0006
SLIP = {"BTCUSDT":0.0001,"ETHUSDT":0.0001,"BCHUSDT":0.0002,"SOLUSDT":0.0003,"DOGEUSDT":0.0004}
BARS_8H = 32
WINDOWS = {"full":("2021-07-22","2026-06-21"),"2123":("2021-07-22","2023-06-30"),
           "2426":("2024-07-05","2026-06-21")}
FUNDING_8H = 0.0001                                   # 0.01%/8h
RISK_BASE   = {s: 0.001 for s in BASKET}              # cesta validada (uniforme)
RISK_BTC015 = {**{s: 0.001 for s in BASKET}, "BTCUSDT": 0.00125}  # decisión M1

def indicators(df):
    h=df["high"].values; l=df["low"].values; c=df["close"].values
    upper=pd.Series(h).rolling(ENTRY_LEN).max().shift(1).values
    lower=pd.Series(l).rolling(ENTRY_LEN).min().shift(1).values
    exit_low=pd.Series(l).rolling(EXIT_LEN).min().shift(1).values
    exit_high=pd.Series(h).rolling(EXIT_LEN).max().shift(1).values
    tr=np.maximum.reduce([h[1:]-l[1:],np.abs(h[1:]-c[:-1]),np.abs(l[1:]-c[:-1])])
    atr=pd.Series(np.concatenate([[np.nan],tr])).rolling(ATR_LEN).mean().values
    return h,l,c,upper,lower,exit_low,exit_high,atr

def load_window(w0, w1):
    raw={s:pd.read_csv(CACHE/(s+"_15m_60m.csv"),parse_dates=["dt"]).set_index("dt").sort_index().loc[w0:w1] for s in BASKET}
    master=reduce(lambda a,b:a.intersection(b),[df.index for df in raw.values()])
    ind={}; px={}
    for s in BASKET:
        d=raw[s].reindex(master); ind[s]=indicators(d); px[s]=d["close"].values
    return master, ind, px

def run_cesta_map(master, ind, px, risk_map, equity0=10000.0,
                  entry_pen=0.0005, stop_pen=0.0010):
    """Copia de run_cesta (lab) con risk por símbolo. stop_fill='stop', gross_cap=0."""
    CS={s:TAKER+SLIP[s] for s in BASKET}
    n=len(master); fb=FUNDING_8H/BARS_8H; eq=equity0
    pos={s:0 for s in BASKET}; entry={s:0.0 for s in BASKET}
    units={s:0.0 for s in BASKET}; satr={s:0.0 for s in BASKET}
    pv=np.full(n,equity0); start=max(ENTRY_LEN,ATR_LEN)+1
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

def main():
    res={}
    for wname,(a,b) in WINDOWS.items():
        master, ind, px = load_window(pd.Timestamp(a,tz="UTC"), pd.Timestamp(b,tz="UTC"))
        for cfg, rmap in (("base", RISK_BASE), ("btc0125", RISK_BTC015)):
            m = run_cesta_map(master, ind, px, rmap)
            res[f"{wname}/{cfg}"] = m
            print(f"{wname:5s} {cfg:7s} NET {m['net']*100:7.2f}%  maxDD {m['maxdd']*100:6.1f}%  "
                  f"Sharpe {m['sharpe']:.2f}  Calmar {m['calmar']:.2f}", flush=True)
    # ---- paridad con FRONTIER_VEREDICTO (0.10% off, FULL): NET≈+24, DD≈-17.8, Sharpe≈0.42 ----
    f=res["full/base"]
    paridad = abs(f["net"]-0.24)<0.05 and abs(f["maxdd"]+0.178)<0.03 and abs(f["sharpe"]-0.42)<0.08
    # ---- umbral de decisión pre-escrito ----
    fb_, fv_ = res["full/base"], res["full/btc0125"]
    dd_ok = all(res[f"{w}/btc0125"]["maxdd"] >= res[f"{w}/base"]["maxdd"] - 0.05 for w in WINDOWS)
    acepta = (fv_["sharpe"] >= fb_["sharpe"] - 0.05) and (fv_["calmar"] >= fb_["calmar"]*0.85) and dd_ok
    ver = "ACEPTA" if acepta else "RECHAZA"
    L=[f"# exp-003 — riesgo por símbolo (BTC 0.125%) — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC\n",
       f"Paridad con FRONTIER (full/base vs 0.10%-off): {'✅ OK' if paridad else '🔴 FALLA — experimento INVÁLIDO, revisar código/datos'}\n",
       "| ventana | config | NET% | maxDD% | Sharpe | Calmar |","|---|---|---|---|---|---|"]
    for k,m in res.items():
        L.append(f"| {k.split('/')[0]} | {k.split('/')[1]} | {m['net']*100:.2f} | {m['maxdd']*100:.1f} | {m['sharpe']:.2f} | {m['calmar']:.2f} |")
    L.append(f"\n## VEREDICTO (umbral pre-escrito): **{ver}**\n")
    L.append(f"- Sharpe FULL: {fb_['sharpe']:.3f} -> {fv_['sharpe']:.3f} (umbral: caída máx 0.05)")
    L.append(f"- Calmar FULL: {fb_['calmar']:.3f} -> {fv_['calmar']:.3f} (umbral: ≥85% de la base)")
    L.append(f"- maxDD por ventana dentro de +5 pp: {'sí' if dd_ok else 'NO'}")
    if not paridad: L.append("\n⚠️ SIN paridad la comparación no es evidencia. No usar.")
    out=OUT/"RESULTADO.md"; out.write_text("\n".join(L), encoding="utf-8")
    (OUT/"metricas.json").write_text(json.dumps({"paridad":bool(paridad),"veredicto":ver,"res":res}, indent=1, default=float))
    print("\n".join(L))

if __name__=="__main__":
    main()
