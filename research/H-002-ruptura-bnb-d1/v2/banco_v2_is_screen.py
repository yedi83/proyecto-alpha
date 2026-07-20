#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""H-002.v2 — SCREEN IN-SAMPLE (T1-IS) — ADELANTO, NO VEREDICTO.

Ejecuta SOLO la parte in-sample del PREREG v2 sellado:
  - Cesta EQUIPONDERADA de los 6 activos (BTC, ETH, BNB, ADA, XRP, LTC).
  - Datos ANTES de 2023-01-01 (in-sample de desarrollo; el tramo 2023-26 esta
    QUEMADO y el forward decisivo aun no existe).
  - Instrumento: SPOT (sin funding), consistente con el PREREG v2 sec.4 (el
    screen in-sample corre en spot; la corrida decisiva forward sera perp+funding).
  - SIN risk-match (eliminado en v2 por invariancia de escala del Sharpe).
  - Metricas: Sharpe Y MAR, estrategia vs buy&hold, a nivel CESTA.
  - Regla T1-IS (sellada): PASA si la cesta-estrategia supera a la cesta-hold en
    Sharpe Y MAR, por margen estricto > 0.

MOTOR: reutilizado VERBATIM importando ../banco.py (backtest, stats, load_coin, BASE, EQ0).
Construccion de la cesta (declarada, mecanica): por activo se normaliza la curva
de equity a 1.0 en su inicio; se alinean por fecha (union, ffill, 1.0 antes de
que el activo empiece = caja); la cesta es la MEDIA de las curvas normalizadas
(equiponderacion rebalanceada a diario). Igual para el hold.

ESTO NO ES EL VEREDICTO DE v2: es la condicion NECESARIA (no suficiente). El
veredicto exige ademas el forward OOS (>=30 trades y >=6 meses desde 2026-07-15)
y su dictamen A-01. No aprueba ni rechaza nada por si solo.
"""
import sys
from pathlib import Path
import numpy as np, pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import banco  # motor verbatim

SYMS = ["BTCUSDT", "ETHUSDT", "BNBUSDT", "ADAUSDT", "XRPUSDT", "LTCUSDT"]
IS_CUTOFF = pd.Timestamp("2023-01-01", tz="UTC")
EQ0 = banco.EQ0
BASE = banco.BASE
warm = max(BASE["N"], BASE["sma_len"], 15)


def norm_series(values, dates):
    v = np.asarray(values, float)
    if len(v) < 2 or v[0] == 0:
        return None
    return pd.Series(v / v[0], index=pd.to_datetime(dates, utc=True))


def build_basket(series_list):
    """Media de curvas normalizadas alineadas por fecha (equiponderacion diaria)."""
    df = pd.concat(series_list, axis=1).sort_index()
    df = df.ffill().fillna(1.0)   # antes de que un activo empiece: caja=1.0
    basket = df.mean(axis=1)
    return basket.values * EQ0, basket.index.values


def main():
    print("=" * 100)
    print("H-002.v2 — SCREEN IN-SAMPLE (T1-IS)  ·  cesta equiponderada 6 activos  ·  pre-2023  ·  SPOT")
    print("ADELANTO, NO VEREDICTO (condicion necesaria, no suficiente)")
    print("=" * 100)

    strat_series, hold_series, per_asset, all_trades = [], [], [], []

    for sym in SYMS:
        df = banco.load_coin(sym)
        df_is = df[df.Date < IS_CUTOFF].reset_index(drop=True)
        if len(df_is) < warm + 30:
            print(f"  {sym}: datos pre-2023 insuficientes ({len(df_is)} velas) — excluido")
            continue
        # estrategia (motor verbatim)
        tr, cv = banco.backtest(df_is, **BASE)
        dts = df_is.Date.values[warm:warm + len(cv)]
        s_strat = banco.stats(cv, dts)
        ns = norm_series(cv, dts)
        # buy & hold sobre el mismo tramo
        c = df_is.Close.values[warm:]
        d_bh = df_is.Date.values[warm:]
        s_hold = banco.stats(c / c[0] * EQ0, d_bh)
        nh = norm_series(c, d_bh)
        if ns is None or nh is None:
            continue
        strat_series.append(ns); hold_series.append(nh)
        per_asset.append((sym[:-4], s_strat, s_hold, len(tr)))
        if len(tr):
            all_trades.append(tr)
        rng = f"{str(df_is.Date.iloc[0])[:10]}->{str(df_is.Date.iloc[-1])[:10]}"
        print(f"  {sym[:-4]:4s} {rng}  n={len(tr):>3}  "
              f"estr Sh={s_strat['sharpe']:5.2f}/MAR={s_strat['mar']:5.2f}   "
              f"hold Sh={s_hold['sharpe']:5.2f}/MAR={s_hold['mar']:5.2f}")

    # ---- CESTA (T1-IS decisivo del screen) ----
    bcv, bdt = build_basket(strat_series)
    bhv, _   = build_basket(hold_series)
    B  = banco.stats(bcv, bdt)
    BH = banco.stats(bhv, bdt)

    print("-" * 100)
    print(f"CESTA estrategia :  Sharpe={B['sharpe']:6.3f}   MAR={B['mar']:6.3f}   "
          f"Ret={B['ret']*100:+7.1f}%   MDD={B['mdd']*100:6.1f}%")
    print(f"CESTA buy&hold   :  Sharpe={BH['sharpe']:6.3f}   MAR={BH['mar']:6.3f}   "
          f"Ret={BH['ret']*100:+7.1f}%   MDD={BH['mdd']*100:6.1f}%")

    pasa_sharpe = B['sharpe'] > BH['sharpe']
    pasa_mar    = B['mar']    > BH['mar']
    pasa = pasa_sharpe and pasa_mar
    print(f"\nT1-IS (regla sellada: cesta-estrategia > cesta-hold en Sharpe Y MAR, margen estricto>0):")
    print(f"   Sharpe: {B['sharpe']:.3f} {'>' if pasa_sharpe else '<='} {BH['sharpe']:.3f}   -> {'OK' if pasa_sharpe else 'NO'}")
    print(f"   MAR   : {B['mar']:.3f} {'>' if pasa_mar else '<='} {BH['mar']:.3f}   -> {'OK' if pasa_mar else 'NO'}")
    print(f"   RESULTADO SCREEN IN-SAMPLE: {'PASA (necesario, no suficiente)' if pasa else 'NO PASA'}")

    # ---- T4-style: concentracion sobre trades agrupados ----
    if all_trades:
        allt = pd.concat(all_trades, ignore_index=True)
        net = allt.pnl.sum()
        top = allt.reindex(allt.pnl.abs().sort_values(ascending=False).index)
        print(f"\nT4 (info, cap de confianza): n_total={len(allt)}  win={ (allt.pnl>0).mean()*100:.1f}%  "
              f"top-5={top.head(5).pnl.sum()/net*100:.1f}% del neto")
        print("   (Deflated Sharpe pendiente: exige el N de configuraciones de T3, no corrido aqui)")

    print("\n" + "=" * 100)
    print("RECORDATORIO: esto es el screen IN-SAMPLE. NO es el veredicto de v2.")
    print("Falta lo decisivo: forward OOS (>=30 trades y >=6 meses desde 2026-07-15) + A-01.")
    print("=" * 100)


if __name__ == "__main__":
    main()
