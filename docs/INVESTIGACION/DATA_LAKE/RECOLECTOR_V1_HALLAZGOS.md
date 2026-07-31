# Recolector V1 — Hallazgos empíricos (el dato que reescribe A-02)

> **Fecha: 2026-07-30 · Fuente: run `20260730T133848Z`** (5426 archivos OK, 1546 ausencias; 22 símbolos, klines 1d/1h/15m + funding + spot + metadata). Este es el resultado del redirect: los modos de falla REALES, no propiedades hipotéticas. Reordena las prioridades de todo el diseño abstracto de A-02.

## 1. La cola del deslistado NO está censurada — está completa
`binance.vision` retiene la historia completa de los perps delistados, **incluida la cola**:

| Símbolo | 1d meses | Rango | Nota |
|---|---|---|---|
| SRMUSDT | 73 | 2020-08 → 2024-05 | historia completa hasta delisting |
| ANCUSDT | 15 | 2022-01 → 2022-12 | vida corta, ventana completa |
| COCOSUSDT | 61 | 2019-09 → 2024-05 | desde el mes 1 de Binance futures |

**Implicación:** el bloqueo "cola censurada por survivorship" (F6/AC-8) es, para la *retención*, empíricamente exagerado. La cola se puede bajar gratis.

## 2. HALLAZGO CENTRAL (nuevo): reuso de ticker = identidad de activo rota
`LUNAUSDT` = `2020-08 → 2026-06` (88 meses) **bajo un solo string** — pero abarca **dos activos distintos**: el LUNA viejo (colapsó a ~0 en 2022-05) y el LUNA nuevo (Terra 2.0, relistado con el mismo ticker). No hay gap visible en la serie de archivos: los empalma.

- Un backtest ingenuo trata `LUNAUSDT` como serie continua → **empalma un crash a cero con un token nuevo** → contaminación catastrófica y silenciosa.
- Es **look-ahead / identidad de activo**, NO censura de cola. Ningún pase adversarial abstracto lo anticipó; solo el dato real lo reveló.
- **CONFIRMADO con las klines crudas (2026-07-30):** `LUNAUSDT` futuros 1d cae 05-may $82.28 → 09-may $30.11 → 11-may $1.09 → **12/13-may $0.008**, y el archivo termina en 2022-05 (sin 2022-06 → delistado tras el crash). El **futuro viejo tiene cola limpia hasta el delisting** — el peor caso exacto de AC-8, recuperable con precio real. En paralelo, el ticker `LUNAUSDT` (sobre todo spot) se extiende hasta 2026-06 = **Terra 2.0 relistado bajo el mismo string**. Empalmar futuro-viejo con spot-nuevo mezcla dos activos (riesgo directo para la descomposición AC-9).
- **Regalo colateral:** que la cola del crash esté con precio real hace que la **cota de daño de survivorship (R3) se calcule sobre datos**, no se declare — para el caso LUNA, al menos.

## 3. La fuente es limpia y fiable — el control de integridad es trivial
- **Checksum:** 5424/5427 archivos con `.CHECKSUM` de origen, **todos verifican, 0 mismatch.** Los 3 sin checksum = metadata.
- **Errores:** los 1546 son **100% `not_found_404`** — 0 http-error, 0 zip corrupto, 0 checksum-mismatch. El log de errores **no es un log de problemas: es un mapa limpio del borde listado/delisting** de cada símbolo.
- **Implicación:** el miedo del adversarial a "archivo válido sin checksum → falso-rechazo" es ~0.06% (solo metadata). No sobre-ingenierar integridad.

## 4. Mapeo multiplicador↔spot: funciona
`1000LUNCUSDT → LUNCUSDT` (2022-09→2026-06) y `1000SHIBUSDT → SHIBUSDT` (2021-05→2026-06): spot presente y alineado. La descomposición funding/base (F6 AC-9) es tratable con el mapeo correcto.

## 5. Correcciones que el dato me hizo
- `FTTUSDT` **NO está delistado** (sigue vivo, 121 meses hasta 2026-06). Asunción errada.
- `COCOSUSDT` **no era un delistado antiguo** de vida corta: corrió 2019-09→2024-05.
- La cola de los delistados **se retiene**, no se censura (contra la hipótesis dominante del hilo).

## 6. Qué debe ser el A-02 definitivo (según el dato, no el diseño)
El aparato abstracto de survivorship se encoge; **el reuso de ticker crece** al centro. Controles reales de A-02:

1. **Detección de reuso de ticker / discontinuidad de identidad de activo** (nuevo, prioritario): salto de precio anómalo (~±100%) + relisting bajo el mismo símbolo → marcar el símbolo como **multi-activo**, partir la serie en `symbol@periodo`, nunca empalmar.
2. **El log de errores como censo empírico del borde** (barato, limpio): las ventanas con datos definen listado/delisting observado por símbolo.
3. **Integridad = checksum del origen** (trivial, fiable): 100% verifica; ruta alternativa solo para el ~0.06% sin checksum.
4. Survivorship: sigue siendo DECLARACIÓN (ruleset R2/R3) — pero la cola conocida es recuperable, así que la cota de daño (R3) se puede calcular sobre datos reales, no solo declararse.

**Regla de parada del A-02 sigue en pie:** no re-diseñar en abstracto. El siguiente paso es descomprimir un puñado de series (LUNA, SRM, un small cap) y ver los datos crudos — de ahí sale el detector de reuso y los umbrales de calidad.
