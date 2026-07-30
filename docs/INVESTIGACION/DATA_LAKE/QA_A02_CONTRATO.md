# QA / A-02 — Contrato de validación del Data Lake (v4, alcance B)

> **Fecha: 2026-07-29 · v4 · Autor: Opus (Claude) sobre la decisión del IP · Estado: PROPUESTA para 4º pase adversarial.**
> **v1, v2, v3 → NO CONFORME** (archivadas en `QA_A02_DICTAMEN_ADVERSARIAL.md`; decisión en `QA_A02_v3_NO_CONFORME_FORK.md`). v4 recorta el alcance a **B**: A-02 certifica **lo alcanzable con datos de proveniencia única** (binance.vision) y **DECLARA** el survivorship en vez de afirmar controlarlo.

## 0. Principio de alcance (lo que vuelve al contrato inmune)

**Certificar lo detectable; DECLARAR lo que no.** A-02 certifica **integridad, calidad y reproducibilidad** —propiedades alcanzables con proveniencia única— y **gatea lo detectable** (incl. wash-trading grueso). Lo que un solo origen **no puede demostrar** (cota completa de survivorship, wash sutil de venue, restatement no observado) **no se certifica: se declara con evidencia y límites explícitos.**

> **La propiedad "survivorship controlado / cota completa" está FUERA de alcance** y requiere una fuente point-in-time externa (Tardis — Opción A, expansión futura). **Un ataque no puede disolver una afirmación que el contrato no hace.** Ahí murieron v1–v3; v4 no la hace.

## 1. Dos salidas independientes de A-02

- **(A) Veredicto de calidad del dato** — CONFORME / CONFORME CON OBSERVACIONES / NO CONFORME, sobre integridad + calidad + reproducibilidad + wash-trading detectable. **Es un grado.**
- **(B) Declaración de survivorship** — un **documento de divulgación**, NO un grado: evidencia (censo binance-derivado + raw), cobertura observada, y los **puntos ciegos declarados**. F0 la usa para decidir; A-02 no la convierte en pase/bloqueo.

## 2. Regla de promoción (disciplina C) — dónde se decide el survivorship

A-02 **no decide** si el survivorship es tolerable; lo hace **F0/metodología** leyendo la Declaración (§4). Regla dura:

- Hipótesis cuyo edge **NO depende de la cola ausente** → veredicto de calidad CONFORME **basta** para promover.
- Hipótesis que **SÍ dependen de una cota completa de survivorship** → **NO se certifican con este contrato**; requieren fuente point-in-time externa (Opción A). Se difieren.

Esto **elimina** la puerta APTO-ACOTADO y la cota autodestructiva de v3: no hay grado de survivorship que gamear; hay una **dependencia de hipótesis** que F0 juzga contra una Declaración honesta.

## 3. Controles de calidad del dato (lo alcanzable — gateado de verdad)

Severidad 🔴 BLOQUEANTE · 🟠 OBSERVACIÓN · 🟢 CONFORME. **Agregación TOTAL y DETERMINISTA** (no prosa): cualquier 🔴 en cualquier familia → **veredicto de calidad = NO CONFORME**; ≥1 🟠 sin 🔴 → **CONFORME CON OBSERVACIONES** (cada una con ID + responsable independiente + fecha de revisión); solo 🟢 → **CONFORME**.

- **INT (integridad):** SHA-256 vs `.CHECKSUM` de origen; ruta alternativa (cross-read / 2º espejo) si el origen no publica checksum. **Se declara** que byte-identidad prueba transporte, no corrección.
- **QUAL (calidad):** OHLCV lógico (`high≥max(o,c)`, `low≤min(o,c)`, `vol≥0`); funding **interval real por evento** (no 8h asumido); mapeo `perp→spot→multiplicador` (`1000SHIB`…); escala temporal ms vs µs; duplicados (**degradan 🔴→🟠 solo con artefacto corroborante independiente**, no nota del recolector); continuidad.
- **WASH (wash-trading) — GATEADO:** heurísticas definidas (volumen/nº-trades anómalo, patrones precio-tiempo, proxies de self-trade). Wash **grueso detectable → 🔴**. **Se declara** el límite: el wash **sutil** de venue no lo detecta *ninguna* fuente — es un punto ciego residual **divulgado**, no "controlado".
- **REPRO:** pin de `raw + parser_version + a02_version`; determinismo por corrida repetida registrada; caducidad si cambia **cualquier** insumo.
- **PIT (calidad de ventana, NO control de survivorship):** coherencia de ventana viva; un **hueco de borde → OBSERVACIÓN declarada**, nunca una afirmación de listing/delisting (corrige el colapso de v3).

## 4. La Declaración de survivorship (el corazón de B — divulgación, no grado)

Documento estructurado, verificable y **honesto sobre lo que NO se ve**:

- **Censo observado** (fuentes binance-derivadas listadas) + **cobertura observada** vs ese censo.
- **Ausentes conocidos** (en censo y no en raw, y viceversa por cruce censo↔raw).
- **Puntos ciegos DECLARADOS** (lo indetectable): (a) símbolos ausentes de raw **Y** censo → invisibles; (b) sesgo de **momento-de-consulta** (REST retroactivo); (c) delistados **antes** del inicio de captura → invisibles sin fuente point-in-time externa.
- **Frase fija obligatoria:** *"Esto es una DECLARACIÓN basada en datos de proveniencia única (binance.vision); NO es un control de survivorship. Una cota completa requiere una fuente point-in-time externa (p.ej. Tardis)."*

No hay umbral aquí que decida promoción. La Declaración es **insumo para F0**.

## 5. Independencia y gobernanza (cierra juez-y-parte)

Mutuamente independientes: **recolector · certificador A-02 · responsable de observaciones/caducidad**. Toda 🟠 lleva **fecha de revisión + responsable nombrado independiente de quien promueve**. El pase adversarial de este contrato: sesión independiente (patrón A-04/F6b).

## 6. Survivorship de selección y de contrato

- **De selección** (BTC/ETH/SOL elegidos entre majors vivos): responsabilidad de **F0**; se **declara** como contexto en la Declaración (§4), no lo gatea A-02.
- **De contrato** (cambios de spec, tiers de liquidación, migración coin-margined→USDT): **A-02 lo marca** en los metadatos del instrumento.

## 7. Umbrales — ahora SÍ fijables (porque ya no deciden survivorship)

Sin "material/razonable/plausible" decidiendo promoción, los umbrales restantes son de **calidad** y son concretos: rangos OHLCV, cota numérica de funding, heurísticas de wash (valores), tolerancia de duplicados, unidad temporal. Se fijan con justificación en implementación. **Ninguno decide survivorship** — esa palanca salió del contrato.

## 8. Entregables + dictamen

```
A02_REPORT.md/.json · MANIFEST.json (raw+parser+a02) · SURVIVORSHIP_DECLARATION.md ·
ANOMALIES.csv · WASH_FLAGS.csv · HASHES.sha256
```
```
A-02 DICTAMEN
Dataset / Versión / Manifest / a02_version / parser_version / Fecha
──────────────
VEREDICTO DE CALIDAD:  CONFORME / CONFORME CON OBSERVACIONES / NO CONFORME   (función total §3)
  OBSERVACIONES: [ID · responsable independiente · fecha de revisión]
DECLARACIÓN DE SURVIVORSHIP:  adjunta (§4) — divulgación, NO grado
──────────────
Nota: este contrato NO certifica "survivorship controlado". Hipótesis tail-dependientes → fuente externa (Opción A).
Firma: A-02 · <fecha> · <a02_version>
```

## 9. Lo que este contrato NO hace / NO afirma

**NO** afirma survivorship controlado; **NO** afirma detectar todo el wash; **NO** certifica hipótesis tail-dependientes (van a Opción A); **NO** reemplaza a F0 en juzgar dependencia de cola. Afirma **solo** lo que un origen único puede sostener, y **declara** el resto. **No está congelado:** debe pasar el 4º pase adversarial — cuyo ataque válido ahora es *"¿la Declaración es honesta y completa en sus límites, y los controles de calidad están realmente gateados?"*, no *"¿está controlado el survivorship?"* (que v4 ya no afirma).

## 10. Orden + 4º pase adversarial

1. Spike de censo (para poblar la Declaración, no para "probar cobertura") con su time-box. 2. Fijar los umbrales de calidad (§7). 3. **4º pase adversarial independiente de v4.** 4. Si sobrevive → congelar; si no → v5. El revisor expone, no corrige.
