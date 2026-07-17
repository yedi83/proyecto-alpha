#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RECOLECTOR DE FUNDING HISTÓRICO REAL — Data Lake, pieza 1 (Propuesta 1, 2026-07-17).

Descarga el funding rate histórico COMPLETO por símbolo desde el endpoint
público de Binance mainnet (fapi/v1/fundingRate vía ccxt, paginado) y lo guarda
como CSV por símbolo con un informe de QA integrado. Insumo del exp-008 (su
PREREG exige después el dictamen APTO de A-02 sobre este dataset).

- Solo endpoints PÚBLICOS: no necesita API keys. No toca ningún bot.
- Idempotente: si el CSV existe, retoma desde el último timestamp guardado.
- Correr en la máquina del investigador (el sandbox no llega a Binance):
    python "D:\\PIC\\Proyecto Investigación cuantitativa PIC\\proyecto-alpha\\datalake\\funding\\recolector_funding.py"
Salida: {SYM}_funding.csv (ts_utc ISO, rate) + QA_REPORT.md en esta carpeta.
"""
import time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
SYMBOLS = ["BTC/USDT:USDT", "ETH/USDT:USDT", "SOL/USDT:USDT", "BCH/USDT:USDT", "DOGE/USDT:USDT"]
DESDE = datetime(2021, 7, 1, tzinfo=timezone.utc)      # cubre la ventana FULL del backtest
PASO_8H_MS = 8 * 3600 * 1000

def iso(ms): return datetime.fromtimestamp(ms / 1000, timezone.utc).isoformat()

def recolectar(ex, sym):
    tick = sym.split("/")[0]
    out = HERE / f"{tick}_funding.csv"
    since = int(DESDE.timestamp() * 1000)
    rows = []
    if out.exists():  # idempotencia: retomar
        last = out.read_text(encoding="utf-8").strip().splitlines()
        if len(last) > 1:
            prev = last[1:]
            rows = [tuple(l.split(",")) for l in prev]
            since = int(datetime.fromisoformat(rows[-1][0]).timestamp() * 1000) + 1
    nuevos = 0
    while True:
        lote = ex.fetch_funding_rate_history(sym, since=since, limit=1000)
        if not lote:
            break
        for f in lote:
            rows.append((iso(f["timestamp"]), repr(float(f["fundingRate"]))))
        nuevos += len(lote)
        nxt = lote[-1]["timestamp"] + 1
        if nxt <= since:
            break
        since = nxt
        if lote[-1]["timestamp"] >= ex.milliseconds() - PASO_8H_MS:
            break
        time.sleep(0.3)
    # dedup por timestamp conservando el último, orden ascendente
    dd = {}
    for ts, r in rows:
        dd[ts] = r
    filas = sorted(dd.items())
    out.write_text("ts_utc,rate\n" + "\n".join(f"{t},{r}" for t, r in filas), encoding="utf-8")
    return filas, nuevos

def qa(sym, filas):
    """QA: cadencia 8h, huecos, rangos. Devuelve dict para el informe."""
    tick = sym.split("/")[0]
    if not filas:
        return {"sym": tick, "n": 0, "error": "SIN DATOS"}
    ts = [datetime.fromisoformat(t) for t, _ in filas]
    rates = [float(r) for _, r in filas]
    huecos = []
    for a, b in zip(ts, ts[1:]):
        d = (b - a).total_seconds()
        if d > 8 * 3600 * 1.5:  # tolerancia 12h: hueco real
            huecos.append((a.isoformat(), b.isoformat(), round(d / 3600, 1)))
    n = len(filas)
    esperado = int((ts[-1] - ts[0]).total_seconds() / (8 * 3600)) + 1
    media_anual = sum(rates) / n * 3 * 365 * 100  # % anualizado aproximado
    return {"sym": tick, "n": n, "desde": ts[0].isoformat(), "hasta": ts[-1].isoformat(),
            "esperado": esperado, "cobertura_pct": round(100 * n / max(esperado, 1), 2),
            "huecos": huecos, "rate_min": min(rates), "rate_max": max(rates),
            "media_anualizada_pct": round(media_anual, 2),
            "extremos_pos": sum(1 for r in rates if r > 0.003),   # >0.3%/8h
            "extremos_neg": sum(1 for r in rates if r < -0.003)}

def main():
    import ccxt
    ex = ccxt.binance({"enableRateLimit": True, "options": {"defaultType": "future"}})
    ex.load_markets()
    L = [f"# QA — funding histórico Binance mainnet — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC\n",
         "| símbolo | n tramos | desde | hasta | cobertura | huecos>12h | rate min/max | media anualizada |",
         "|---|---|---|---|---|---|---|---|"]
    detalles = []
    for sym in SYMBOLS:
        print(f"{sym}: descargando...", flush=True)
        filas, nuevos = recolectar(ex, sym)
        q = qa(sym, filas)
        print(f"  {q.get('n',0)} tramos ({nuevos} nuevos), cobertura {q.get('cobertura_pct','—')}%, huecos {len(q.get('huecos',[]))}")
        L.append(f"| {q['sym']} | {q.get('n',0)} | {q.get('desde','—')[:10]} | {q.get('hasta','—')[:10]} | "
                 f"{q.get('cobertura_pct','—')}% | {len(q.get('huecos',[]))} | "
                 f"{q.get('rate_min',0):.5f} / {q.get('rate_max',0):.5f} | {q.get('media_anualizada_pct','—')}% |")
        if q.get("huecos"):
            detalles.append(f"\n### Huecos {q['sym']}\n" + "\n".join(f"- {a} → {b} ({h} h)" for a, b, h in q["huecos"][:20]))
        detalles.append(f"\n{q['sym']}: tramos extremos (+>0.3%/8h): {q.get('extremos_pos',0)} · (−<−0.3%/8h): {q.get('extremos_neg',0)}")
    L.append("\nNota: SOL/DOGE pueden empezar después de 2021-07 (listing); eso es cobertura real, no hueco.")
    L.append("Siguiente paso obligatorio (PREREG exp-008): dictamen A-02 sobre este dataset ANTES de correr el experimento.")
    L += detalles
    rep = HERE / "QA_REPORT.md"
    rep.write_text("\n".join(L), encoding="utf-8")
    print("\n".join(L[:12])); print(f"\nGuardado: {rep}")

if __name__ == "__main__":
    main()
