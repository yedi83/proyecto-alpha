#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Go/no-go del camino gratis para el Data Lake (ver docs/INVESTIGACION/DATA_LAKE/FUENTES_DELISTADOS.md).

Descarga de data.binance.vision el funding rate + klines de uno o varios perpetuos YA DELISTADOS,
verifica el .CHECKSUM (sha256) y muestra la COLA de la serie para responder:
  ¿la historia del delistado esta disponible y hasta que fecha/precio llega antes del delisting?

Solo libreria estandar (urllib, zipfile, hashlib, csv). No instala nada.
Uso:
    python verificar_delistado.py
    python verificar_delistado.py LUNAUSDT:2022-04,2022-05  RAYUSDT:2024-01
El default verifica LUNAUSDT (colapso Terra, mayo 2022) en klines 1d + fundingRate.
NO escribe nada en el repo: baja a una carpeta temporal y solo imprime. Crudo inmutable = otra etapa.
"""
import sys, io, csv, hashlib, zipfile, tempfile, urllib.request, urllib.error
from datetime import datetime, timezone

BASE = "https://data.binance.vision/data/futures/um/monthly"
INTERVAL = "1d"   # klines: 1d es compacto y deja ver el colapso dia a dia; cambia a 15m/1h si quieres fino

def _get(url):
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        return ("HTTP %s" % e.code)
    except Exception as e:
        return ("ERR %s" % e)

def _ts(ms):
    try:
        return datetime.fromtimestamp(int(ms)/1000, tz=timezone.utc).strftime("%Y-%m-%d %H:%M")
    except Exception:
        return str(ms)

def _descargar_y_verificar(url):
    """Baja el .zip y su .CHECKSUM; verifica sha256; devuelve (filas_csv, nota)."""
    data = _get(url)
    if isinstance(data, str):
        return None, "no disponible (%s)" % data
    chk = _get(url + ".CHECKSUM")
    nota_chk = "sin .CHECKSUM"
    if not isinstance(chk, str):
        esperado = chk.decode(errors="replace").split()[0].strip().lower()
        real = hashlib.sha256(data).hexdigest().lower()
        nota_chk = "CHECKSUM OK" if esperado == real else "CHECKSUM *MISMATCH*"
    # descomprimir el primer csv del zip
    try:
        zf = zipfile.ZipFile(io.BytesIO(data))
        name = zf.namelist()[0]
        raw = zf.read(name).decode(errors="replace")
    except Exception as e:
        return None, "zip ilegible (%s)" % e
    filas = [r for r in csv.reader(io.StringIO(raw)) if r]
    return filas, nota_chk

def verificar_klines(symbol, mes):
    url = "%s/klines/%s/%s/%s-%s-%s.zip" % (BASE, symbol, INTERVAL, symbol, INTERVAL, mes)
    filas, nota = _descargar_y_verificar(url)
    print("  KLINES %s %s  [%s]" % (symbol, mes, nota))
    if not filas:
        return None
    # saltar cabecera si la hay (algunos dumps recientes la traen)
    if filas and not filas[0][0].isdigit():
        filas = filas[1:]
    if not filas:
        print("    (vacio)"); return None
    prim, ult = filas[0], filas[-1]
    print("    filas=%d  desde=%s  hasta=%s" % (len(filas), _ts(prim[0]), _ts(ult[0])))
    print("    primer close=%s   ULTIMO close=%s" % (prim[4], ult[4]))
    return (_ts(ult[0]), ult[4])

def verificar_funding(symbol, mes):
    url = "%s/fundingRate/%s/%s-fundingRate-%s.zip" % (BASE, symbol, symbol, mes)
    filas, nota = _descargar_y_verificar(url)
    print("  FUNDING %s %s  [%s]" % (symbol, mes, nota))
    if not filas:
        return
    if filas and not filas[0][0].isdigit():
        print("    cols:", ",".join(filas[0])); filas = filas[1:]
    if not filas:
        print("    (vacio)"); return
    print("    filas=%d  desde=%s  hasta=%s" % (len(filas), _ts(filas[0][0]), _ts(filas[-1][0])))
    print("    ultima fila cruda:", ",".join(filas[-1]))

def main():
    # objetivos: "SYMBOL:mes,mes"  (default LUNAUSDT abril+mayo 2022)
    args = sys.argv[1:] or ["LUNAUSDT:2022-04,2022-05"]
    print("== VERIFICACION DE DELISTADOS EN data.binance.vision ==")
    print("intervalo klines:", INTERVAL, "| base:", BASE)
    for a in args:
        sym, _, meses = a.partition(":")
        meses = meses.split(",") if meses else ["2022-05"]
        print("\n### %s" % sym)
        for mes in meses:
            verificar_klines(sym, mes)
            verificar_funding(sym, mes)
    print("\n== VEREDICTO (leelo tu) ==")
    print("- Si aparecen filas y CHECKSUM OK -> la historia del delistado SI esta en la fuente gratis.")
    print("- Mira 'ULTIMO close' y 'hasta=': ¿la serie llega al colapso (p.ej. LUNA ~mayo 2022, precio en centavos),")
    print("  o se corta ANTES? Eso decide si la cola del carry-crash esta completa o censurada por el delisting.")

if __name__ == "__main__":
    main()
