# QA / A-02 — Contrato de validación del Data Lake (v5, alcance B — enforcement)

> **Fecha: 2026-07-29 · v5 · Autor: Opus (Claude) sobre la decisión del IP · Estado: PROPUESTA para el 5º pase adversarial (bajo regla de parada §10).**
> **v1–v4 → NO CONFORME** (archivadas en `QA_A02_DICTAMEN_ADVERSARIAL.md`; bifurcación en `QA_A02_v3_NO_CONFORME_FORK.md`). v4 acertó el alcance (B) pero falló en ENFORCEMENT. v5 cierra los dientes.

## 0. MANDATO de v5 (el límite auto-impuesto — condición del IP)

**A-02 NO intenta demostrar que el survivorship esté controlado. No lo demuestra, no lo afirma, no lo grada.** Respecto al survivorship, el único deber de A-02 es que **la limitación declarada NO pueda:**
- **(a)** ser **ignorada** en la ruta de promoción,
- **(b)** ser **eludida** por re-etiquetado,
- **(c)** ser **malinterpretada** como control.

Todo lo **alcanzable** con proveniencia única (integridad, calidad, reproducibilidad) se **certifica**. Lo **no demostrable** (survivorship, wash sutil, restatement no observado) se **declara**. v5 solo añade **dientes de enforcement** a esa frontera; no mueve la frontera.

## 1. Dos salidas + la compuerta que las obliga

- **(A) Veredicto de calidad** — `CONFORME` / `NO CONFORME` (binario; ver §4). Solo integridad + calidad + reproducibilidad.
- **(B) Declaración** — survivorship + wash residual + restatement: **divulgación, no grado** (§7).
- **Compuerta de promoción (los dientes):** promover exige **las TRES**, no una:
  1. Veredicto de calidad **CONFORME**;
  2. **Declaración pineada + acuse explícito** de quien promueve;
  3. **Dictamen de dependencia-de-cola firmado por parte independiente del promotor** (§2).
  Falta cualquiera → **no promueve**. La compuerta **consume la Declaración**, no solo el grado — cierra (a) "decorativa".

## 2. Dependencia-de-cola: screen mecánico + default conservador + independencia

Cierra (b) elusión y el juez-y-parte de v4.

- **Screen mecánico** (a fijar en implementación): ¿el universo elegible incluye instrumentos en las bandas de **liquidez baja / vida corta** donde se concentra el delisting? ¿**Remover la cohorte delisting-elegible** mueve la señal materialmente?
- **Default conservador: TAIL-DEPENDIENTE** salvo **evidencia positiva** en contra. La **carga de la prueba** recae en quien quiere el carril barato; la aserción no basta.
- **Independencia:** el dictamen de dependencia lo firma/revisa **alguien independiente del promotor**. **F0-promotor ≠ evaluador-de-dependencia** para su propia hipótesis (§8).
- **Tail-dependiente → NO se certifica con este contrato** (requiere Opción A / fuente point-in-time externa). No re-etiquetable por aserción.

## 3. Wash: de grado a DECLARACIÓN (aplica el principio de B, que v4 violó)

- **"Wash detectable" SALE del grado de calidad.** El grado ya no comunica ninguna garantía de wash.
- **WASH-FLAG:** solo un umbral **grueso concreto** (número, §implementación) marca el dataset **en la Declaración**; **no abre ni cierra el grado**.
- El wash **sub-umbral** se **declara** como punto ciego que **alimenta la decisión de dependencia/tamaño**, no un pase.

## 4. Veredicto de calidad: binario, con acumulación, sin fugas de mapeo

- Solo propiedades **alcanzables**. **Cualquier 🔴 → NO CONFORME.**
- **`CONFORME CON OBSERVACIONES` NO satisface la compuerta** por sí solo (§1): las 🟠 deben **resolverse** o ser **aceptadas explícitamente por la parte independiente** (§8), no por el promotor.
- **Acumulación:** N observaciones graves → **NO CONFORME** (N a fijar en implementación). Ningún montón de 🟠 promueve.
- **Todo control mapea a severidad** — incluido el marcador de survivorship-de-contrato (§6). Sin controles sin mapear.

## 5. Reproducibilidad con dientes

- **Pin completo:** `raw + parser_version + a02_version + valores de umbrales (dentro de a02_version) + snapshot del censo + hash de la Declaración`. **Caducidad si cambia cualquiera** (cierra el hueco de v4: umbral o censo mutan sin caducar).
- **Reproducible por re-corrida independiente**, no auto-atestada.

## 6. Controles de calidad (lo alcanzable — mapeos cerrados)

- **INT:** SHA-256 vs `.CHECKSUM` de origen; ruta alternativa (cross-read / 2º espejo) si no hay checksum. Se **declara** que byte-identidad prueba transporte, **no** corrección de contenido.
- **QUAL:** OHLCV lógico; funding interval real por evento; `perp→spot→multiplicador`; escala ms/µs; continuidad. **Duplicados/gaps:** una "explicación" degrada 🔴→🟠 **solo con artefacto independiente DEFINIDO** (aviso oficial de venue **o** ≥2º registro independiente), **validado por parte ≠ recolector ≠ promotor**.
- **WASH-FLAG:** §3 — a la Declaración, no al grado.
- **Survivorship-de-contrato** (spec/liquidación/coin-m→USDT): **marcado con severidad** (no solo "en metadatos").
- **REPRO:** §5.

## 7. La Declaración (divulgación honesta — sin cifra-evidencia)

- Reporta el censo como **conteo de MISMA PROVENIENCIA que NO acota el universo verdadero** — explícito. **Se elimina toda "% de cobertura" presentada como evidencia** (corrige la recaída de v4).
- **Puntos ciegos declarados:** ausentes de raw **Y** censo (invisibles); sesgo de momento-de-consulta; delistados pre-captura.
- **Wash residual** y **restatement no observado** declarados.
- **Frase fija:** *"Esto es una DECLARACIÓN basada en datos de proveniencia única; NO es un control de survivorship. Una cota completa requiere una fuente point-in-time externa (Opción A)."*
- La Declaración se **pinea** (hash en manifest, §5) y es de **consumo obligatorio** en la compuerta (§1).

## 8. Independencia (mecanismo, no aspiración)

- Roles mutuamente independientes con separación verificable: **recolector · certificador A-02 · evaluador-de-dependencia-de-cola · responsable de observaciones**. **El F0-promotor NO puede ocupar ninguno de estos roles para su propia hipótesis.**
- **Honestidad de lab pequeño:** si la independencia es temporal/rotatoria por tamaño del equipo, **se declara cómo se logra** (p.ej. rotación, sesión aislada tipo A-04) — no se finge una separación que no existe.

## 9. Lo que v5 NO hace (por mandato §0)

NO demuestra survivorship controlado; NO gradúa wash; NO presenta cobertura como evidencia; NO certifica hipótesis tail-dependientes (Opción A). **Solo cierra las vías por las que una limitación declarada se ignora (§1), se elude (§2) o se malinterpreta (§3, §7).**

## 10. Regla de parada (acordada con el IP)

5º pase adversarial independiente de v5. **Si CONFORME o CONFORME CON OBSERVACIONES** (solo quedan umbrales numéricos de implementación) → **congelar** y registrar observaciones. **Si NO CONFORME por un hueco arquitectónico NUEVO** → **parar** y reconsiderar si A-02 tal como se concibió es el instrumento correcto — no seguir puliendo. El revisor expone, no corrige.
