# A-02 — Reglas destiladas (producto de 5 pases adversariales)

> **Fecha: 2026-07-29 · Estado: PROVISIONAL (regla R8).** Esto **NO es un contrato**: es la destilación de lo que sobrevivió a cinco pases adversariales (v1–v5, todas NO CONFORME). Los cinco dictámenes (`QA_A02_DICTAMEN_ADVERSARIAL.md`) y las cinco versiones del contrato son **anexo, no producto**.
>
> **Aclaración de ejes (la lección que casi ocultamos):** *honestidad* y *enforcement* son variables distintas. A escala de lab pequeño/solo, A-02 = **certificación mecánica de calidad + divulgación honesta**; el enforcement **no** es un árbitro independiente (coordina a un equipo que no existe), sino **precompromiso** (R6).

## R1 — Calidad mecánica (lo alcanzable, sin independencia). Esto SÍ se certifica.
Integridad (sha256 vs origen), OHLCV lógico, funding interval real por evento, `perp→spot→multiplicador`, escala ms/µs, continuidad, duplicados. **Determinista, binario, reproducible por re-corrida.** Cualquier 🔴 → NO CONFORME.

## R2 — Taxonomía CERRADA de sesgos, con estado (auditar por omisión, no prosa libre).
Catálogo fijo; cada clase con estado `medido / acotado / desconocido / no aplica`:
`survivorship de símbolo · survivorship de contrato · restatement de klines · look-ahead de funding/mark · wash trading · realismo de fills · sesgo de selección del investigador`.
Una casilla vacía **es** un hallazgo. La completitud de una lista en prosa es incertificable; la de un catálogo fijo se audita.

## R3 — Cota de survivorship = CONDENA, no absolución.
Reconstruido el censo, peor caso plausible sobre los ausentes **conocidos** → medir el daño al edge (p.ej. Sharpe 1.4→0.3). **Si mata el edge → decisivo (NO APTO). Si sobrevive → no certifica nada** (ciega a los ausentes de raw *y* censo; benigna por construcción para ilíquidos: −100% sin liquidez = no operable = aporte ~0). Reportar como **cota de daño con signo**, nunca como sello de robustez.

## R4 — Fecha de captura ≠ periodo cubierto (campo obligatorio).
Un snapshot tomado hoy sobre 2019 ≠ uno tomado en 2019; **esa diferencia ES el survivorship.** Sin este campo, "honesto" sigue escondiendo el dato relevante. (Por eso Tardis vale: captura ≈ periodo.)

## R5 — Toda limitación aceptada lleva condición de revocación FALSABLE.
No "acepto y justifico" (coartada) sino **"esta aceptación queda nula si [censo reconstruido muestra >N deslistados en el periodo / el lockbox la contradice / …]"**. Es F4 (falsabilidad Popperiana) aplicado a la aceptación, no a la hipótesis. Justificación que no puede resultar falsa no es decisión.

## R6 — Enforcement de lab solo = precompromiso, no árbitro.
Los **hashes del slice de datos se clavan dentro del PREREG sellado** (timestamp inmutable) y la **sensibilidad al survivorship se evalúa sobre lockbox/OOS**. Eso protege del autoengaño **sin un segundo humano** — y ya existe en la práctica del lab (H-002.v2, H-001). El aparato de árbitro independiente se descarta a esta escala.

## R7 — Trip-wire de independencia (para que "futuro" no signifique "nunca").
Enforcement con parte independiente solo se activa por disparador explícito: **primer despliegue de capital REAL**, o **primer tercero con exposición económica**. Sin disparador, no se promete.

## R8 — REDIRECT (la regla que gobierna a las demás).
**Estas reglas son una hipótesis, no un contrato.** Se construye el **recolector V1**, se corre **~2 semanas**, y los **modos de falla reales reescriben esto**. Cinco pases no cerraron en abstracto lo que el archivo real resuelve en días, porque las preguntas abiertas son **empíricas, no lógicas**: ¿`binance.vision` retiene la cola completa del deslistado o se corta antes? ¿el censo es reconstruible y hasta dónde? Ningún diseño responde eso; solo el dato.
