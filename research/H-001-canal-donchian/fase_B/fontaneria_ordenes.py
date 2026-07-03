#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FONTANERÍA DE ÓRDENES — preparación de Fase B (NO toca el bot ni su cuenta).

Prueba en testnet, con una CUENTA SEPARADA, lo que la Fase B necesita saber:
  F1. Límites reales por símbolo según ccxt: min notional (cost.min), min qty,
      precisión  -> verifica el hallazgo M1 (¿BTC exige $100?).
  F2. Round-trip real en DOGE (~$20): market buy -> inspección de la respuesta
      (average, timestamp, fee ¿poblada?) -> cierre reduce-only -> cuenta plana.
  F3. Rechazo controlado: orden de BTC por DEBAJO del mínimo -> captura el tipo
      y mensaje EXACTOS del error (la firma del "rechazo sin evento" del bot).
  F4. Funding rate history en testnet: ¿el endpoint responde? (lo usa el bot).
  F5. Latencia del round-trip (ms).

SEGURIDAD:
  - Solo corre en sandbox/testnet (se verifica; aborta si no).
  - Se NIEGA a correr si las keys coinciden con las del bot (config.env del lab).
  - Notionales mínimos; cierra todo lo que abre; verifica cuenta plana al final.

USO (ccxt >= 4.5: Binance retiró el testnet de futuros; se usa DEMO TRADING):
  1) Activar demo trading en demo.binance.com y crear API keys ahí
     (Settings > API Management del modo demo). Cuenta/keys SEPARADAS del bot.
  2) Copiar config.example.env -> config.env (misma carpeta) con esas keys.
     (config.env está en .gitignore: JAMÁS se versiona.)
  3) python fontaneria_ordenes.py
Salida: fontaneria_report_YYYY-MM-DD.md en esta carpeta.

HALLAZGO F0 (descubierto al primer intento): ccxt moderno lanza NotSupported con
set_sandbox_mode para futuros. El BOT usa set_sandbox_mode para la Fase B ->
habrá que migrarlo a enable_demo_trading al arrancar la B (cambio de frontera de
fase, documentado). El DRY actual no se ve afectado (solo endpoints públicos).
"""
import os, time
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
LAB = Path(os.getenv("DONCHIAN_LAB", r"D:\ESTRATEGIA_ALEX\crypto_iid_rango\donchian512_lab"))
SYMBOLS = ["BTC/USDT:USDT","ETH/USDT:USDT","SOL/USDT:USDT","BCH/USDT:USDT","DOGE/USDT:USDT"]
RT_SYMBOL = "DOGE/USDT:USDT"     # round-trip barato
RT_NOTIONAL = 20.0                # ~$20
BELOWMIN_SYMBOL = "BTC/USDT:USDT"
BELOWMIN_NOTIONAL = 50.0          # a propósito bajo el mínimo esperado ($100)

def load_env(path):
    d = {}
    if path.exists():
        for line in path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                d[k.strip()] = v.split("#")[0].strip()
    return d

def main():
    import ccxt
    cfg = load_env(HERE / "config.env")
    key = os.getenv("FONTANERIA_API_KEY", cfg.get("API_KEY", ""))
    sec = os.getenv("FONTANERIA_API_SECRET", cfg.get("API_SECRET", ""))
    assert key and sec, "Faltan keys: crea config.env (ver config.example.env)"

    # --- seguridad 1: NO usar la cuenta del bot ---
    bot_cfg = load_env(LAB / "bot" / "config.env")
    assert key != bot_cfg.get("API_KEY", "___"), \
        "ABORTADO: estas keys son las del BOT. Usa una cuenta testnet separada."

    ex = ccxt.binance({"apiKey": key, "secret": sec, "enableRateLimit": True,
                       "options": {"defaultType": "future"}})
    ex.enable_demo_trading(True)   # ccxt >= 4.5 (testnet futuros retirado)
    # --- seguridad 2: solo entorno demo ---
    api = ex.urls.get("api", {})
    fapi = str(api.get("fapiPrivate", "")) if isinstance(api, dict) else str(api)
    assert "demo" in fapi.lower(), f"ABORTADO: endpoint no parece demo trading: {fapi}"
    ex.load_markets()

    R = [f"# Fontanería de órdenes — {datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC (testnet, cuenta separada)\n"]

    # ---------- F1: límites reales ----------
    R.append("## F1 — Límites por símbolo (según ccxt/testnet)\n")
    R.append("| Símbolo | min notional (cost.min) | min qty (amount.min) | precisión qty |\n|---|---|---|---|")
    for s in SYMBOLS:
        m = ex.market(s); lim = m.get("limits", {})
        cost_min = (lim.get("cost") or {}).get("min")
        amt_min = (lim.get("amount") or {}).get("min")
        prec = m.get("precision", {}).get("amount")
        R.append(f"| {s} | {cost_min} | {amt_min} | {prec} |")
    R.append("\n**Verificación M1:** si cost.min de BTC es None, el guard del bot usa "
             "default 5.0 y el rechazo lo daría el exchange (sin evento). Si es ~100, "
             "el guard del bot omitirá BTC correctamente con equity $750.\n")

    # ---------- balance ----------
    bal = ex.fetch_balance()
    usdt = float(bal["total"].get("USDT", 0))
    R.append(f"## Balance\n\nUSDT total en la cuenta de pruebas: **{usdt:.2f}**\n")
    assert usdt > RT_NOTIONAL * 2, f"Balance insuficiente ({usdt:.2f} USDT) para el round-trip."

    # ---------- F2: round-trip DOGE ----------
    R.append("## F2 — Round-trip real (" + RT_SYMBOL + ")\n")
    px = float(ex.fetch_ticker(RT_SYMBOL)["last"])
    qty = float(ex.amount_to_precision(RT_SYMBOL, RT_NOTIONAL / px))
    t0 = time.time()
    o = ex.create_order(RT_SYMBOL, "market", "buy", qty)
    t1 = time.time()
    oid = o.get("id")
    time.sleep(1.5)
    od = ex.fetch_order(oid, RT_SYMBOL) if oid else o
    fee_inline = (od.get("fee") or {}).get("cost")
    trades = []
    try: trades = ex.fetch_my_trades(RT_SYMBOL, limit=5)
    except Exception as e: R.append(f"- fetch_my_trades falló: `{type(e).__name__}: {e}`")
    fee_trades = sum((t.get("fee") or {}).get("cost") or 0 for t in trades if t.get("order") == oid)
    R.append(f"- qty enviada: {qty} (redondeo amount_to_precision desde {RT_NOTIONAL/px:.6f})")
    R.append(f"- respuesta create_order: average={o.get('average')} price={o.get('price')} "
             f"status={o.get('status')} timestamp={o.get('timestamp')}")
    R.append(f"- fetch_order: average={od.get('average')} filled={od.get('filled')} status={od.get('status')}")
    R.append(f"- **fee inline en la orden: {fee_inline}** | fee sumada de fills (fetch_my_trades): {fee_trades}")
    R.append(f"  (si inline es None/0 y fills>0: el bot DEBE leer fees de los fills, no de la orden — bug latente del registro)")
    R.append(f"- **F5 latencia create_order→respuesta: {(t1-t0)*1000:.0f} ms**")
    # cierre reduce-only
    c = ex.create_order(RT_SYMBOL, "market", "sell", qty, None, {"reduceOnly": True})
    time.sleep(1.5)
    poss = ex.fetch_positions([RT_SYMBOL])
    open_amt = sum(abs(float(p.get("contracts") or 0)) for p in poss)
    R.append(f"- cierre reduce-only: status={c.get('status')} | contratos abiertos tras cierre: **{open_amt}**")
    flat_ok = open_amt == 0

    # ---------- F3: rechazo por debajo del mínimo (BTC) ----------
    R.append("\n## F3 — Rechazo controlado por min_notional (" + BELOWMIN_SYMBOL + f", ~${BELOWMIN_NOTIONAL:.0f})\n")
    pxb = float(ex.fetch_ticker(BELOWMIN_SYMBOL)["last"])
    qb = float(ex.amount_to_precision(BELOWMIN_SYMBOL, BELOWMIN_NOTIONAL / pxb))
    try:
        ob = ex.create_order(BELOWMIN_SYMBOL, "market", "buy", qb)
        R.append(f"- ⚠️ INESPERADO: la orden PASÓ (id={ob.get('id')}, notional≈{qb*pxb:.1f}$). "
                 "El mínimo de testnet es menor de lo asumido -> M1 debe re-evaluarse con este dato.")
        ex.create_order(BELOWMIN_SYMBOL, "market", "sell", qb, None, {"reduceOnly": True})
        time.sleep(1.5)
    except Exception as e:
        R.append(f"- rechazo capturado (la firma que el bot vería SIN generar evento):")
        R.append(f"  - tipo: `{type(e).__name__}`")
        R.append(f"  - mensaje: `{e}`")

    # ---------- F4: funding history ----------
    R.append("\n## F4 — fetch_funding_rate_history en testnet\n")
    try:
        fr = ex.fetch_funding_rate_history(RT_SYMBOL, limit=5)
        R.append(f"- OK: {len(fr)} tramos; último rate={fr[-1]['fundingRate'] if fr else '—'}")
    except Exception as e:
        R.append(f"- FALLÓ: `{type(e).__name__}: {e}` (el bot estima funding con este endpoint en DRY — anotar)")

    # ---------- limpieza final ----------
    poss = ex.fetch_positions(SYMBOLS)
    residual = {p["symbol"]: p.get("contracts") for p in poss if abs(float(p.get("contracts") or 0)) > 0}
    if residual:
        R.append(f"\n## 🔴 LIMPIEZA PENDIENTE: posiciones residuales {residual} — ciérralas a mano en testnet.")
    else:
        R.append("\n## ✅ Cuenta plana al terminar.")
    if not flat_ok and not residual:
        R.append("(la posición del round-trip tardó en reflejarse; verificar en la web de testnet)")

    out = HERE / f"fontaneria_report_{datetime.now(timezone.utc):%Y-%m-%d}.md"
    out.write_text("\n".join(R), encoding="utf-8")
    print("\n".join(R)); print(f"\nGuardado: {out}")

if __name__ == "__main__":
    main()
