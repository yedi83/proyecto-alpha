#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Recolector V1 del Data Lake — ver docs/INVESTIGACION/DATA_LAKE/RECOLECTOR_V1_SPEC.md
y A02_REGLAS_DESTILADAS.md.

Baja de data.binance.vision el RAW original (klines/funding/spot) del universo V1 CONGELADO,
calcula SHA-256 por archivo, escribe un manifiesto inmutable y un log de errores. NO transforma
el raw, NO borra símbolos que "no aparecieron", NO interpreta ni certifica survivorship.
Recolecta y deja evidencia. Solo librería estándar.

Uso:
    python recolector_v1.py                # run completo (1d universo + 1h estudio + 15m mínimo)
    python recolector_v1.py --smoke        # prueba rápida: solo 1d, últimos 3 meses + LUNA completo
"""
import sys, os, io, json, time, hashlib, urllib.request, urllib.error
from pathlib import Path
from datetime import datetime, timezone

BASE = "https://data.binance.vision/data"
EXCHANGE_INFO = "https://fapi.binance.com/fapi/v1/exchangeInfo"
START = (2019, 9)                                   # arranque de Binance USD-M futures
DATA_ROOT = Path(__file__).resolve().parent.parent / "data"
RUN_ID = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")

# ---------- UNIVERSO V1 CONGELADO (2026-07-29) ----------
UNIVERSO = [
    "BTCUSDT","ETHUSDT","SOLUSDT","BCHUSDT","DOGEUSDT",      # H-001
    "BNBUSDT","XRPUSDT",                                      # large extra
    "LINKUSDT","LTCUSDT","ATOMUSDT","AVAXUSDT",               # mid
    "CVCUSDT","FLMUSDT","DENTUSDT","STMXUSDT",                # small / baja-liq
    "LUNAUSDT","FTTUSDT","SRMUSDT","ANCUSDT",                 # delistados
    "1000LUNCUSDT","1000SHIBUSDT",                            # multiplicador
    "COCOSUSDT",                                              # delistado antiguo (sonda)
]
SUB_1H = ["BTCUSDT","ETHUSDT","SOLUSDT","BCHUSDT","DOGEUSDT","LUNAUSDT","FLMUSDT","DENTUSDT"]
SUB_15M = ["BTCUSDT","FLMUSDT"]
# mapeo perp->spot (multiplicadores). None = no se intenta spot.
SPOT_MAP = {s: s for s in UNIVERSO}
SPOT_MAP["1000SHIBUSDT"] = "SHIBUSDT"
SPOT_MAP["1000LUNCUSDT"] = "LUNCUSDT"
# perps que NO tienen par spot obvio → no intentar (se registrará como decisión, no como error)
NO_SPOT = {"FTTUSDT","SRMUSDT","ANCUSDT","COCOSUSDT","LUNAUSDT"}  # se intenta igual; si 404 va a errors

# raw -> data/ (fuera de git, regla 4); manifiesto+errores -> datalake/manifests/ (trackeado: son evidencia)
MAN_DIR = Path(__file__).resolve().parent / "manifests"
def now_iso(): return datetime.now(timezone.utc).isoformat()

def _get(url, timeout=60):
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, None
    except Exception as e:
        return -1, str(e).encode()

def meses(desde=START):
    y, m = desde
    now = datetime.now(timezone.utc)
    while (y, m) <= (now.year, now.month):
        yield f"{y:04d}-{m:02d}"
        m += 1
        if m == 13: y, m = y+1, 1

class Recolector:
    def __init__(self, smoke=False):
        self.smoke = smoke
        MAN_DIR.mkdir(parents=True, exist_ok=True)
        self.man = open(MAN_DIR / f"manifest_{RUN_ID}.jsonl", "a", encoding="utf-8")
        self.err = open(MAN_DIR / f"errors_{RUN_ID}.jsonl", "a", encoding="utf-8")
        self.n_ok = self.n_err = 0

    def _log_man(self, o): self.man.write(json.dumps(o, ensure_ascii=False)+"\n"); self.man.flush()
    def _log_err(self, o): self.err.write(json.dumps(o, ensure_ascii=False)+"\n"); self.err.flush()

    def _man(self, rel_dir, fname, url, symbol, itype, dtype, interval, period, cap, sha, nbytes, present, verified, resumed):
        self.n_ok += 1
        self._log_man({"run_id":RUN_ID,"file_path":str((Path("raw/binance_vision")/rel_dir/fname)),
                       "symbol":symbol,"instrument_type":itype,"data_type":dtype,"interval":interval,
                       "period_yyyymm":period,"source_url":url,"capture_date_utc":cap,
                       "sha256":sha,"bytes":nbytes,"origin_checksum_present":bool(present),
                       "checksum_verified":verified,"resumed":resumed})

    def bajar(self, rel_dir, fname, url, symbol, itype, dtype, interval, period):
        """Baja url -> DATA_ROOT/raw/rel_dir/fname (bytes crudos, sin descomprimir). RESUME: si ya existe y verifica, no re-descarga."""
        cap = now_iso()
        dest = DATA_ROOT / "raw" / "binance_vision" / rel_dir / fname
        # --- RESUME: saltar lo ya bajado (un apagón no cuesta la descarga entera) ---
        if dest.exists() and dest.stat().st_size > 0:
            b = dest.read_bytes(); sha = hashlib.sha256(b).hexdigest()
            cs_s, cs = _get(url + ".CHECKSUM")
            if cs_s == 200 and cs:
                if cs.decode(errors="replace").split()[0].strip().lower() == sha.lower():
                    self._man(rel_dir,fname,url,symbol,itype,dtype,interval,period,cap,sha,len(b),True,True,True); return True
                # mismatch -> archivo parcial/corrupto del apagón: re-descargar (cae abajo)
            else:
                self._man(rel_dir,fname,url,symbol,itype,dtype,interval,period,cap,sha,len(b),False,None,True); return True
        # --- descarga normal ---
        status, data = _get(url)
        if status != 200 or data is None:
            self.n_err += 1
            self._log_err({"run_id":RUN_ID,"symbol":symbol,"data_type":dtype,"interval":interval,
                           "period_yyyymm":period,"reason":"not_found_404" if status==404 else "http_error",
                           "http_status":status,"capture_date_utc":cap})
            return False
        cs_status, cs = _get(url + ".CHECKSUM")
        origin_present = cs_status == 200 and cs
        sha = hashlib.sha256(data).hexdigest(); verified = None
        if origin_present:
            verified = (cs.decode(errors="replace").split()[0].strip().lower() == sha.lower())
            if not verified:
                self.n_err += 1
                self._log_err({"run_id":RUN_ID,"symbol":symbol,"data_type":dtype,"interval":interval,
                               "period_yyyymm":period,"reason":"checksum_mismatch","http_status":200,"capture_date_utc":cap})
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)                                    # RAW inmutable, SIN transformar
        self._man(rel_dir,fname,url,symbol,itype,dtype,interval,period,cap,sha,len(data),bool(origin_present),verified,False)
        return True

    def klines(self, root, itype, symbol, interval, ms):
        base = f"{BASE}/{root}/monthly/klines/{symbol}/{interval}"
        rel = f"{root}/klines/{symbol}/{interval}"
        for p in ms:
            f = f"{symbol}-{interval}-{p}.zip"
            self.bajar(rel, f, f"{base}/{f}", symbol, itype, "klines", interval, p)
            time.sleep(0.05)

    def funding(self, symbol, ms):
        base = f"{BASE}/futures/um/monthly/fundingRate/{symbol}"
        rel = f"futures/um/fundingRate/{symbol}"
        for p in ms:
            f = f"{symbol}-fundingRate-{p}.zip"
            self.bajar(rel, f, f"{base}/{f}", symbol, "futures_um", "fundingRate", None, p)
            time.sleep(0.05)

    def metadata(self):
        status, data = _get(EXCHANGE_INFO)
        cap = now_iso()
        if status != 200 or not data:
            self._log_err({"run_id":RUN_ID,"symbol":"__exchangeInfo__","data_type":"metadata",
                           "reason":"http_error","http_status":status,"capture_date_utc":cap}); return
        outdir = DATA_ROOT / "raw" / "binance_vision" / "metadata"; outdir.mkdir(parents=True, exist_ok=True)
        fn = f"exchangeInfo_{RUN_ID}.json"; (outdir/fn).write_bytes(data)
        sha = hashlib.sha256(data).hexdigest()
        # qué símbolos del universo están vivos hoy (los delistados NO estarán → señal, no error)
        try:
            info = json.loads(data); vivos = {s["symbol"] for s in info.get("symbols",[])}
        except Exception: vivos = set()
        self._log_man({"run_id":RUN_ID,"file_path":f"raw/binance_vision/metadata/{fn}","symbol":"__exchangeInfo__",
                       "instrument_type":"futures_um","data_type":"metadata","interval":None,"period_yyyymm":None,
                       "source_url":EXCHANGE_INFO,"capture_date_utc":cap,"sha256":sha,"bytes":len(data),
                       "origin_checksum_present":False,"checksum_verified":None,
                       "universo_vivo_hoy":sorted([s for s in UNIVERSO if s in vivos]),
                       "universo_no_vivo_hoy":sorted([s for s in UNIVERSO if s not in vivos])})

    def run(self):
        print(f"[recolector V1] run_id={RUN_ID}  smoke={self.smoke}  data_root={DATA_ROOT}")
        self.metadata()
        ms_full = list(meses())
        ms_1d = ms_full[-3:] if self.smoke else ms_full
        for sym in UNIVERSO:
            print(f"  {sym} ...")
            # 1d: universo completo (en smoke, LUNA lleva historia completa igual)
            self.klines("futures/um","futures_um",sym,"1d", ms_full if (self.smoke and sym=="LUNAUSDT") else ms_1d)
            self.funding(sym, ms_1d)
            if not self.smoke:
                if sym in SUB_1H:  self.klines("futures/um","futures_um",sym,"1h", ms_full)
                if sym in SUB_15M: self.klines("futures/um","futures_um",sym,"15m", ms_full)
                spot = SPOT_MAP.get(sym)
                if spot:
                    self.klines("spot","spot",spot,"1d", ms_full)
                    if sym in SUB_1H: self.klines("spot","spot",spot,"1h", ms_full)
        self.man.close(); self.err.close()
        print(f"[fin] archivos OK={self.n_ok}  errores/ausencias={self.n_err}")
        print(f"      manifiesto: manifests/manifest_{RUN_ID}.jsonl")
        print(f"      errores:    manifests/errors_{RUN_ID}.jsonl  <- ESTE es el primer censo empírico de huecos")

if __name__ == "__main__":
    Recolector(smoke="--smoke" in sys.argv).run()
