#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H-002 — descarga OHLCV diario SPOT de Binance para el banco.
BNB (el activo) + varios majors (test cruzado T2). Spot para llegar a 2017
(los perp arrancaron ~2020). Corre en TU maquina (venv del lab, tiene ccxt).
Crea datos/{SYM}_1d.csv.
"""
import time
from pathlib import Path
import pandas as pd, ccxt

OUT = Path(__file__).resolve().parent / "datos"; OUT.mkdir(exist_ok=True)
EX = ccxt.binance({"enableRateLimit": True})   # spot por defecto
MESES = 120                                    # ~10 anios -> alcanza 2017
SIMBOLOS = ["BNB/USDT", "BTC/USDT", "ETH/USDT", "ADA/USDT", "XRP/USDT", "LTC/USDT"]

def bajar(sym, tf="1d", meses=MESES):
    now = EX.milliseconds(); since = now - meses*30*86_400_000
    rows=[]; cur=since
    while cur < now:
        b = EX.fetch_ohlcv(sym, tf, since=cur, limit=1000)
        if not b: break
        rows += b; cur = b[-1][0] + 86_400_000
        if len(b) < 1000 and cur >= now - 86_400_000: break
        time.sleep(EX.rateLimit/1000)
    df = pd.DataFrame(rows, columns=["ts","open","high","low","close","volume"]).drop_duplicates("ts").sort_values("ts")
    df["dt"] = pd.to_datetime(df["ts"], unit="ms", utc=True)
    df = df.set_index("dt")[["open","high","low","close","volume"]].astype(float)
    df.to_csv(OUT/f"{sym.replace('/','')}_1d.csv")
    print(f"{sym}: {len(df)} velas | {df.index[0].date()} -> {df.index[-1].date()}", flush=True)

for s in SIMBOLOS:
    print(f"Descargando {s} 1d ...", flush=True)
    bajar(s)
print(f"\nListo. Archivos en {OUT}")
