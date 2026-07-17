#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
exp-008 — cesta H-001 con FUNDING REAL histórico (PREREG.md de esta carpeta).

COMPUERTA: no correr sin dictamen APTO de A-02 sobre datalake/funding/ (regla del PREREG).

Método congelado: motor de exp-002/003/004 con UN cambio — el funding se aplica
en la vela que contiene cada timestamp real (long paga rate positivo; short al
revés), en lugar del rate/32 uniforme por vela. Paridad obligatoria: la corrida
base uniforme debe reproducir NET +24.03 / maxDD -17.8 / Sharpe 0.42 / Calmar 1.35.
Umbrales R0/R1/R2: sellados en PREREG.md — este script solo los evalúa.
"""
import os, json
from datetime import datetime, timezone
from pathlib import Path
from functools import reduce
import numpy as np, pandas as pd

CACHE = Path(os.getenv("DONCHIAN_CACHE", r"D:\ESTRATEGIA_ALEX\crypto_iid_rango\backtest\cache"))
FUND  = Path(os.getenv("FUNDING_DIR", str(Path(__file__).resolve().parent.parent.parent.parent.parent / "datalake" / "funding")))
OUT = Path(__file__).resolve().parent
BASKET = ["BTCUSDT","ETHUSDT","SOLUSDT","BCHUSDT","DOGEUSDT"]
ENTRY_LEN, EXIT_LEN, ATR_LEN, ATR_MULT, MAXLEV, TAKER = 512, 256, 14, 3.0, 3.0, 0.0006
SLIP = {"BTCUSDT":0.0001,"ETHUSDT":0.0001,"BCHUSDT":0.0002,"SOLUSDT":0.0003,"DOGEUSDT":0.0004}
WINDOWS = {"full":("2021-07-22","2026-06-21"),"2123":("2021-07-22","2023-06-30"),"2426":("2024-07-05","2026-06-21")}
FUNDING_8H_UNIFORME = 0.0001
RISK = 0.001

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

def load_funding(master):
    """Por símbolo: array n con el rate aplicable en cada vela (0 si ninguno).
    El timestamp real de funding se asigna a la vela cuyo open lo contiene
    (floor a 15m). Master es tz-aware UTC."""
    pos_idx = {t:i for i,t in enumerate(master)}
    F={}
    for s in BASKET:
        tick=s.replace("USDT","")
        arr=np.zeros(len(master))
        f=pd.read_csv(FUND/f"{tick}_funding.csv")
        ts=pd.to_datetime(f["ts_utc"], utc=True, format="ISO8601").dt.floor("15min")
        for t,r in zip(ts, f["rate"].astype(float)):
            i=pos_idx.get(t)
            if i is not None: arr[i]+=r   # += por si hubiera dos tramos en la misma vela
        F[s]=arr
    return F

def run(master, ind, px, modo, F=None, equity0=10000.0, entry_pen=0.0005, stop_pen=0.0010):
    """modo: 'base' (uniforme 0.01%/8h prorrateado) | 'real' (timestamps exactos de F)."""
    CS={s:TAKER+SLIP[s] for s in BASKET}
    n=len(master); fb=FUNDING_8H_UNIFORME/32; eq=equity0
    pos={s:0 for s in BASKET}; entry={s:0.0 for s in BASKET}
    units={s:0.0 for s in BASKET}; satr={s:0.0 for s in BASKET}
    pv=np.full(n,equity0); start=max(ENTRY_LEN,ATR_LEN)+1
    fund_acum={}  # (sym, año, lado) -> $
    for i in range(start,n):
        for s in BASKET:
            if pos[s]!=0:
                if modo=="base":
                    eq-=units[s]*px[s][i]*fb
                else:
                    r=F[s][i]
                    if r!=0.0:
                        pago=pos[s]*units[s]*px[s][i]*r   # long paga r>0; short cobra
                        eq-=pago
                        k=(s, master[i].year, "long" if pos[s]==1 else "short")
                        fund_acum[k]=fund_acum.get(k,0.0)-pago  # negativo = pagado
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
                u=min((eq*RISK)/sd, eq*MAXLEV/c[i])
                p=c[i]*(1+(SLIP[s]+entry_pen)*d_); eq-=u*p*cs
                pos[s]=d_; entry[s]=p; units[s]=u; satr[s]=atr[i]
        op=sum(units[s]*(px[s][i]-entry[s])*pos[s] for s in BASKET if pos[s]!=0)
        pv[i]=eq+op
    pv[:start]=equity0
    netv=pv[-1]/equity0-1
    ec=pd.Series(pv,index=master); dd=(ec/ec.cummax()-1).min(); rr=ec.pct_change().dropna()
    sh=(rr.mean()/rr.std()*np.sqrt(96*365)) if rr.std()>0 else 0.0
    calmar=netv/abs(dd) if dd<0 else float("nan")
    return dict(net=netv,maxdd=dd,sharpe=sh,calmar=calmar), fund_acum

HASHES = {  # congelados por DICTAMEN_A02 (2026-07-17); el APTO cubre EXACTAMENTE estos bytes
 "BTC_funding.csv":"801133db36c95488723264569af1a6ac05c01e885d80eaa145f5f3f0f86dda7a",
 "ETH_funding.csv":"76c6a5187e42008157dbe5eb3954f3a1ee28c9244176449254ad10231d3b61a2",
 "SOL_funding.csv":"590d760f9e8c57f737c91df2adbbec482e2760438e8837a1f99ca6901b13c8f7",
 "BCH_funding.csv":"98239ab8b16f17f79e1494f763db6e11fc1ed07bc8ac653f29235f8c71564c87",
 "DOGE_funding.csv":"1fd25d55144784514ee6d2cc28627b3717887224dfba7b1122856236395f3ad8"}

def verificar_integridad():
    import hashlib
    for f, h in HASHES.items():
        real = hashlib.sha256((FUND/f).read_bytes()).hexdigest()
        assert real == h, f"ABORTADO: {f} no coincide con el hash auditado por A-02 ({real[:12]}... != {h[:12]}...). El APTO no cubre estos bytes."
    print("Integridad del dataset verificada contra DICTAMEN_A02: 5/5 OK")

def main():
    verificar_integridad()
    res={}; fund_full={}
    for w,(a,b) in WINDOWS.items():
        master, ind, px = load_window(pd.Timestamp(a,tz="UTC"), pd.Timestamp(b,tz="UTC"))
        F = load_funding(master)
        for modo in ("base","real"):
            m,fa = run(master, ind, px, modo, F)
            res[f"{w}/{modo}"]=m
            if w=="full" and modo=="real": fund_full=fa
            print(f"{w:5s} {modo:5s} NET {m['net']*100:7.2f}%  maxDD {m['maxdd']*100:6.1f}%  Sharpe {m['sharpe']:.2f}  Calmar {m['calmar']:.2f}", flush=True)
    # paridad
    fb_=res["full/base"]
    paridad = abs(fb_["net"]-0.2403)<0.005 and abs(fb_["maxdd"]+0.178)<0.005 and abs(fb_["sharpe"]-0.42)<0.02
    # veredicto R2->R1->R0 (PREREG sellado)
    fr=res["full/real"]; r26=res["2426/real"]
    if fr["net"]<=-0.05 or (fr["net"]<=0 and r26["net"]<0): ver="R2 — LETAL"
    elif (0<fr["net"]<0.10) or fr["net"]<=0 or fr["sharpe"]<0.30 or r26["net"]<0: ver="R1 — ADVERTENCIA"
    else: ver="R0 — ACEPTABLE"
    L=[f"# exp-008 — funding real — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC\n",
       f"Paridad full/base vs referencia: {'✅ OK' if paridad else '🔴 FALLA — EXPERIMENTO INVÁLIDO'}\n",
       "| ventana | funding | NET% | maxDD% | Sharpe | Calmar |","|---|---|---|---|---|---|"]
    for k,m in res.items():
        w,mo=k.split("/")
        L.append(f"| {w} | {'uniforme 0.01%/8h' if mo=='base' else 'REAL'} | {m['net']*100:.2f} | {m['maxdd']*100:.1f} | {m['sharpe']:.2f} | {m['calmar']:.2f} |")
    L.append(f"\n## VEREDICTO (umbral pre-escrito): **{ver}**\n")
    L.append(f"- FULL real: NET {fr['net']*100:.2f}% (R0 exige ≥ +10%) · Sharpe {fr['sharpe']:.3f} (R0 exige ≥ 0.30) · 2426 real NET {r26['net']*100:.2f}% (R1 si < 0)")
    if not paridad: L.append("\n🔴 SIN PARIDAD nada de lo anterior es evidencia.")
    L.append("\n## Funding neto por símbolo/año/lado (FULL, $; − = pagado, + = cobrado)\n")
    L.append("| símbolo | año | lado | $ |"); L.append("|---|---|---|---|")
    for (s,y,lado),v in sorted(fund_full.items()):
        L.append(f"| {s.replace('USDT','')} | {y} | {lado} | {v:+.2f} |")
    (OUT/"RESULTADO.md").write_text("\n".join(L), encoding="utf-8")
    (OUT/"metricas.json").write_text(json.dumps({"paridad":bool(paridad),"veredicto":ver,"res":res}, indent=1, default=float))
    print("\n".join(L[:14])); print(f"\nVEREDICTO: {ver}\nGuardado en {OUT}")

if __name__=="__main__":
    main()
