#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Descarga historia EXTENDIDA (84 meses ~ desde 2019-09) para el test de
regimen 2020 (exp-006). Corre en TU maquina con el venv del lab (tiene ccxt).

Crea backtest/cache/{SYM}_15m_84m.csv. Las monedas cuyo perp arranco despues
(SOL, etc.) solo traeran lo que exista — NO inventan historia; el backtest
las excluira del basket 2020 si no tienen velas pre-2021.
"""
import sys
sys.path.insert(0, r"D:\ESTRATEGIA_ALEX\crypto_iid_rango")
from backtest.data_loader import load_ohlcv

MESES = 84  # ~6.9 anios -> alcanza el crash covid (mar-2020) y antes
SIMBOLOS = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "BCH/USDT", "DOGE/USDT"]

for s in SIMBOLOS:
    print(f"Descargando {s} 15m {MESES}m ...", flush=True)
    df = load_ohlcv(s, "15m", MESES, force=True)
    print(f"  {s}: {len(df)} velas | desde {df.index[0]} hasta {df.index[-1]}", flush=True)
print(f"\nListo. Archivos en backtest/cache/*_15m_{MESES}m.csv")
