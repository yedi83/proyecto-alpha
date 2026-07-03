#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REPLAY OFFLINE — cierre de Fase A (criterio 1 del PREREG_FASE_AB).

Verifica, SIN tocar el sistema vivo:
  C1: toda señal del modelo tiene evento registrado (ejecutada/omitida).
  C2: todo evento del bot (señal/salida) está respaldado por el modelo.
  C4: latencia mediana señal->registro < 30 s, medida contra el CIERRE real
      de la vela (= vela_ts + 15 min; vela_ts es APERTURA, contrato 1).
  C5: señales sin evento se cruzan contra eventos 'vela_atrasada' para
      clasificarlas como explicadas (hallazgo M2 de la revisión de código).

Diseño (ver report/revision_codigo_2026-07-03.md):
  - Señales recomputadas de forma independiente con las fórmulas CONGELADAS
    (Donchian 512/256 shift(1), ATR SMA-14, solo velas cerradas).
  - El ESTADO (posiciones) se dirige por los EVENTOS REALES del bot: si el bot
    no abrió (omitida), el replay tampoco — así los stops posteriores se
    evalúan sobre el mismo estado y una divergencia no contamina las demás.
  - Parámetros LIVE (riesgo 0.10%); las velas se bajan del MISMO feed que usó
    el bot (testnet) para no comparar contra datos distintos.

Uso (en la máquina del bot, mismo Python: ccxt, pandas, numpy):
  python replay_offline.py             -> informe de la fase hasta ahora
  python replay_offline.py --selftest  -> autoprueba sin red (validar el replay)
Salida: replay_report_YYYY-MM-DD.md (+ replay_divergencias.csv si las hay).
"""
import os, sys, argparse
from datetime import datetime, timedelta, timezone
from pathlib import Path
import numpy as np
import pandas as pd

# ---------------- CONFIG ----------------
LAB = Path(os.getenv("DONCHIAN_LAB", r"D:\ESTRATEGIA_ALEX\crypto_iid_rango\donchian512_lab"))
EVENTOS_CSV  = LAB / "paper" / "eventos.csv"
REGISTRO_CSV = LAB / "paper" / "registro_live.csv"
OUT_DIR = Path(__file__).resolve().parent

CORTE = pd.Timestamp("2026-07-02T03:53:46+00:00")          # acta de inicio (PREREG)
SYMBOLS = ["BTC/USDT:USDT","ETH/USDT:USDT","SOL/USDT:USDT","BCH/USDT:USDT","DOGE/USDT:USDT"]
TIMEFRAME = "15m"; BAR = timedelta(minutes=15)
ENTRY_LEN, EXIT_LEN, ATR_LEN, ATR_MULT = 512, 256, 14, 3.0  # CONGELADO
WARMUP = ENTRY_LEN + ATR_LEN + 10
LAT_MEDIANA_MAX_S = 30.0                                    # criterio 4 del PREREG

# Posiciones abiertas EN el corte (acta de inicio, PREREG): estado inicial del replay.
INIT_POSITIONS = {
    "BCH/USDT:USDT": {"side": "long", "entry": 204.54, "atr": 1.3492857142857093},  # trade #7
}

# ---------------- indicadores (fórmulas congeladas, idénticas a bot/backtest) ----------------
def indicators(df):
    h, l, c = df["high"].values, df["low"].values, df["close"].values
    upper = pd.Series(h).rolling(ENTRY_LEN).max().shift(1).values
    lower = pd.Series(l).rolling(ENTRY_LEN).min().shift(1).values
    exlo  = pd.Series(l).rolling(EXIT_LEN).min().shift(1).values
    exhi  = pd.Series(h).rolling(EXIT_LEN).max().shift(1).values
    tr = np.maximum.reduce([h[1:]-l[1:], np.abs(h[1:]-c[:-1]), np.abs(l[1:]-c[:-1])])
    atr = pd.Series(np.concatenate([[np.nan], tr])).rolling(ATR_LEN).mean().values
    return upper, lower, exlo, exhi, atr

# ---------------- datos ----------------
def fetch_candles(sym, since_ts, until_ts):
    """Velas 15m CERRADAS del mismo feed que usa el bot (testnet)."""
    import ccxt
    ex = ccxt.binance({"enableRateLimit": True, "options": {"defaultType": "future"}})
    if hasattr(ex, "set_sandbox_mode"):
        ex.set_sandbox_mode(True)                    # mismo endpoint que el bot
    rows, since_ms = [], int(since_ts.timestamp()*1000)
    until_ms = int(until_ts.timestamp()*1000)
    while since_ms < until_ms:
        o = ex.fetch_ohlcv(sym, TIMEFRAME, since=since_ms, limit=1500)
        if not o: break
        rows += o
        nxt = o[-1][0] + 1
        if nxt <= since_ms: break
        since_ms = nxt
    df = pd.DataFrame(rows, columns=["ts","open","high","low","close","vol"]).drop_duplicates("ts")
    df["dt"] = pd.to_datetime(df["ts"], unit="ms", utc=True)
    df = df.sort_values("ts").reset_index(drop=True)
    # descartar la vela en curso (no cerrada): cierre = dt + 15min > ahora
    now = datetime.now(timezone.utc)
    return df[df["dt"] + BAR <= now].reset_index(drop=True)

def load_eventos():
    ev = pd.read_csv(EVENTOS_CSV)
    ev["ts_utc"]  = pd.to_datetime(ev["ts_utc"], utc=True, format="ISO8601")
    ev["vela_ts"] = pd.to_datetime(ev["vela_ts"], utc=True, format="ISO8601", errors="coerce")
    return ev[ev["ts_utc"] >= CORTE].copy()

# ---------------- núcleo: replay por símbolo ----------------
def replay_symbol(sym, df, ev_sym):
    """Devuelve (esperadas, divergencias). Estado dirigido por eventos reales."""
    upper, lower, exlo, exhi, atr = indicators(df)
    dts = list(df["dt"])  # conservar tz-aware (numpy despojaría el tz)
    close = df["close"].values
    low = df["low"].values; high = df["high"].values

    # índice de eventos del bot por vela: {vela_ts: [filas]}
    ev_sen = ev_sym[ev_sym["evento"] == "senal"].set_index("vela_ts")
    ev_sal = ev_sym[ev_sym["evento"] == "salida"].set_index("vela_ts")
    ev_atr = ev_sym[ev_sym["evento"].isin(["vela","vela_atrasada"])]  # velas atrasadas

    pos = dict(INIT_POSITIONS.get(sym)) if INIT_POSITIONS.get(sym) else None
    esperadas, dive = [], []

    def bot_tiene(idx_df, vts):
        try: return idx_df.loc[[vts]]
        except KeyError: return None

    for i in range(len(df)):
        vts = pd.Timestamp(dts[i])
        if vts < CORTE:  # warmup: solo actualiza estado si hubiese eventos (no los hay pre-corte)
            continue
        if np.isnan(upper[i]) or np.isnan(atr[i]):
            continue
        c = close[i]
        # --- salida esperada (modelo) ---
        exp_salida = None
        if pos:
            if pos["side"] == "long":
                stop = max(pos["entry"] - ATR_MULT*pos["atr"], exlo[i] if not np.isnan(exlo[i]) else -np.inf)
                hit = low[i] <= stop; rev = c < lower[i]
            else:
                stop = min(pos["entry"] + ATR_MULT*pos["atr"], exhi[i] if not np.isnan(exhi[i]) else np.inf)
                hit = high[i] >= stop; rev = c > upper[i]
            if hit or rev:
                exp_salida = "stop" if hit else "reversa"
                esperadas.append((sym, vts, "salida", exp_salida))
        # --- evento real de salida en esta vela ---
        real_sal = bot_tiene(ev_sal, vts)
        if exp_salida and real_sal is None:
            dive.append((sym, vts, "C1", f"modelo espera SALIDA ({exp_salida}) y no hay evento"))
        if real_sal is not None:
            if not exp_salida:
                dive.append((sym, vts, "C2", "bot registró SALIDA que el modelo no espera"))
            pos = None  # estado = lo que hizo el bot
        elif exp_salida:
            pos = None  # tratar como cerrada para no cascada; ya quedó la divergencia C1
        # --- señal de entrada esperada (modelo) ---
        exp_side = None
        if pos is None:
            if c > upper[i]: exp_side = "long"
            elif c < lower[i]: exp_side = "short"
            if exp_side:
                esperadas.append((sym, vts, "senal", exp_side))
        real_sen = bot_tiene(ev_sen, vts)
        if exp_side and real_sen is None:
            # ¿explicada por vela atrasada? (M2: el bot pudo no ver esta vela)
            explicada = ((ev_atr["ts_utc"] >= vts) & (ev_atr["ts_utc"] <= vts + 4*BAR)).any()
            dive.append((sym, vts, "C1" if not explicada else "C5-explicada",
                         f"modelo espera SEÑAL {exp_side}" + (" [cubierta por evento vela_atrasada]" if explicada else " y no hay evento")))
        if real_sen is not None:
            r = real_sen.iloc[0]
            if not exp_side:
                dive.append((sym, vts, "C2", f"bot registró SEÑAL ({r['resultado']}/{r['motivo']}) que el modelo no espera"))
            elif str(r["motivo"]) not in (exp_side, "nan", "") and str(r["resultado"]) == "ejecutada" and str(r["motivo"]) != exp_side:
                dive.append((sym, vts, "C2", f"dirección difiere: modelo {exp_side} vs bot {r['motivo']}"))
            if str(r["resultado"]) == "ejecutada":
                px = float(r["precio"]) if str(r["precio"]) not in ("", "nan") else c
                pos = {"side": str(r["motivo"]) if str(r["motivo"]) in ("long","short") else exp_side,
                       "entry": px, "atr": float(atr[i])}
            # omitida => el bot siguió plano; el replay también (pos sigue None)
    return esperadas, dive

# ---------------- criterios 4 y 5 + registro ----------------
def latencias(ev):
    e = ev[ev["evento"].isin(["senal","salida"]) & ev["vela_ts"].notna()].copy()
    e["lat_s"] = (e["ts_utc"] - (e["vela_ts"] + BAR)).dt.total_seconds()
    return e

def check_registro(ev):
    out = []
    if not REGISTRO_CSV.exists(): return out
    tr = pd.read_csv(REGISTRO_CSV)
    for col in ("entry_time_signal","exit_time_signal"):
        tr[col] = pd.to_datetime(tr[col], utc=True, format="ISO8601", errors="coerce")
    sen = ev[(ev["evento"]=="senal") & (ev["resultado"]=="ejecutada")]
    sal = ev[ev["evento"]=="salida"]
    for _, t in tr.iterrows():
        if pd.notna(t["entry_time_signal"]) and t["entry_time_signal"] >= CORTE:
            ok = ((sen["symbol"]==t["symbol"]) & (sen["vela_ts"]==t["entry_time_signal"])).any()
            if not ok: out.append(f"trade #{t['trade_id']} {t['symbol']}: entrada sin evento de señal (C2)")
        if pd.notna(t["exit_time_signal"]) and t["exit_time_signal"] >= CORTE:
            ok = ((sal["symbol"]==t["symbol"]) & (sal["vela_ts"]==t["exit_time_signal"])).any()
            if not ok: out.append(f"trade #{t['trade_id']} {t['symbol']}: salida sin evento (C2)")
    return out

# ---------------- informe ----------------
def informe(esperadas, dive, ev, reg_issues, until):
    lat = latencias(ev)
    med = lat["lat_s"].median() if len(lat) else float("nan")
    p95 = lat["lat_s"].quantile(0.95) if len(lat) else float("nan")
    atras = ev[ev["evento"].isin(["vela","vela_atrasada"])]
    c1 = [d for d in dive if d[2]=="C1"]; c2 = [d for d in dive if d[2]=="C2"] + reg_issues
    c5e = [d for d in dive if d[2]=="C5-explicada"]
    ok = lambda cond: "✅ CUMPLE" if cond else "🔴 NO CUMPLE"
    L = []
    L.append(f"# Replay offline — Fase A (corte {CORTE.isoformat()} → {until:%Y-%m-%d %H:%M} UTC)\n")
    L.append(f"Señales/salidas esperadas por el modelo: **{len(esperadas)}** · eventos del bot: **{len(ev[ev['evento'].isin(['senal','salida'])])}**\n")
    L.append("| Criterio PREREG | Resultado | Detalle |\n|---|---|---|")
    L.append(f"| C1 señal→evento | {ok(not c1)} | {len(c1)} sin evento; {len(c5e)} explicadas por vela atrasada |")
    L.append(f"| C2 evento→modelo | {ok(not c2)} | {len(c2)} sin respaldo del modelo |")
    L.append(f"| C4 latencia | {ok(med < LAT_MEDIANA_MAX_S)} | mediana {med:.1f}s · p95 {p95:.1f}s · n={len(lat)} |")
    L.append(f"| C5 atrasadas | {'✅ 0 eventos' if len(atras)==0 else f'ℹ️ {len(atras)} eventos — revisar diario'} | por símbolo: {atras['symbol'].value_counts().to_dict() if len(atras) else '—'} |")
    L.append("\n(C3 caídas/estado y C6 diario se verifican manualmente: bot.log, vigia.log, DIARIO_FASE_A.md)\n")
    if dive or reg_issues:
        L.append("## Divergencias\n")
        for d in dive: L.append(f"- `{d[0]}` vela {d[1]:%Y-%m-%d %H:%M} [{d[2]}]: {d[3]}")
        for r in reg_issues: L.append(f"- {r}")
        pd.DataFrame(dive, columns=["symbol","vela_ts","criterio","detalle"]).to_csv(OUT_DIR/"replay_divergencias.csv", index=False)
    else:
        L.append("## Divergencias\n\nNinguna. Instrumentación coherente con el modelo en todo el período.\n")
    return "\n".join(L)

def main():
    until = datetime.now(timezone.utc)
    ev = load_eventos()
    esperadas, dive = [], []
    for sym in SYMBOLS:
        df = fetch_candles(sym, CORTE - WARMUP*BAR, until)
        e, d = replay_symbol(sym, df, ev[ev["symbol"]==sym])
        esperadas += e; dive += d
        print(f"{sym}: {len(df)} velas, {len(e)} esperadas, {len(d)} divergencias")
    reg = check_registro(ev)
    rep = informe(esperadas, dive, ev, reg, until)
    out = OUT_DIR / f"replay_report_{until:%Y-%m-%d}.md"
    out.write_text(rep, encoding="utf-8")
    print(rep); print(f"\nGuardado: {out}")

# ---------------- selftest (sin red): valida el propio replay ----------------
def selftest():
    """Escenario sintético: ruptura long en vela conocida, luego stop.
    Caso A: eventos correctos -> 0 divergencias. Caso B: falta evento -> C1."""
    n = WARMUP + 60
    ts0 = pd.Timestamp("2026-07-01T00:00:00+00:00")
    dts = pd.date_range(ts0, periods=n, freq="15min", tz="UTC")
    base = np.full(n, 100.0)
    ib, istop = WARMUP + 20, WARMUP + 30
    base[ib] = 106.0                                  # cierre rompe el máximo (señal long)
    for j in range(ib+1, istop): base[j] = 106.0      # se mantiene
    df = pd.DataFrame({"dt": dts, "open": base, "close": base,
                       "high": base + 0.5, "low": base - 0.5, "vol": 1.0})
    df.loc[istop, ["low","close","open","high"]] = [101.0, 103.0, 103.0, 106.0]  # toca stop SIN romper el canal corto
    global CORTE, INIT_POSITIONS
    CORTE_old, INIT_old = CORTE, INIT_POSITIONS
    CORTE, INIT_POSITIONS = dts[WARMUP], {}
    sym = "BTC/USDT:USDT"
    mk = lambda rows: pd.DataFrame(rows, columns=["ts_utc","modo","symbol","vela_ts","evento","resultado","motivo","precio","qty","detalle"]).assign(
        ts_utc=lambda x: pd.to_datetime(x["ts_utc"], utc=True), vela_ts=lambda x: pd.to_datetime(x["vela_ts"], utc=True))
    evA = mk([[dts[ib]+BAR+timedelta(seconds=9),"DRY",sym,dts[ib],"senal","ejecutada","long",106.0,1.0,""],
              [dts[istop]+BAR+timedelta(seconds=9),"DRY",sym,dts[istop],"salida","ejecutada","stop",103.0,1.0,""]])
    eA, dA = replay_symbol(sym, df, evA)
    assert len(eA) == 2, f"esperadas={eA}"
    assert not dA, f"caso A debía estar limpio: {dA}"
    evB = evA.iloc[[1]]                                # quitamos el evento de señal
    eB, dB = replay_symbol(sym, df, evB)
    assert any(x[2] == "C1" for x in dB), f"caso B debía dar C1: {dB}"
    # nota: sin entrada del bot, el replay queda plano y la 'salida' real produce C2 — correcto
    CORTE, INIT_POSITIONS = CORTE_old, INIT_old
    print("SELFTEST OK — señal y stop esperados detectados; evento faltante produce C1.")

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    selftest() if a.selftest else main()
