# Dictamen adversarial — Contrato QA/A-02 (v1)

> Producido en sesión independiente (dieta cerrada: `DATA_LAKE_ALCANCE_ESQUEMA.md` v2 + `QA_A02_CONTRATO.md` + `DATA.md`) el 2026-07-29. Archivado verbatim, append-only. **Resultado: NO CONFORME.** El revisor identificó vulnerabilidades; NO propuso correcciones (regla del C-001). Las correcciones las decide el IP; luego un segundo pase adversarial.

```
DICTAMEN ADVERSARIAL — Contrato QA/A-02
Artefactos: QA_A02_CONTRATO.md (atacado) + DATA_LAKE_ALCANCE_ESQUEMA.md v2 (contexto).
──────────────
ATAQUE 1 (universo): VULNERABLE — A02-DATA-005 solo detecta el delta "censo → recolectado". Un activo que existió pero NO figura en el censo externo es invisible al control: no está en el denominador, luego no puede aparecer como faltante. §6 nunca exige verificar la completitud del censo contra la realidad, y sus seis buckets de clasificación absorben cualquier ausencia sin que ninguno sea BLOQUEANTE por regla. Un símbolo puede desaparecer silenciosamente si desaparece a la vez del lago y del censo. "Clasificar la ausencia" no es "demostrar cobertura": el survivorship se declara "controlado" con solo haber etiquetado los huecos.

ATAQUE 2 (point-in-time): VULNERABLE — A02-DATA-004 coteja "dato vs metadatos" (listing_date/delisting_date). Pero esos metadatos son la MISMA fuente que define el point-in-time y NO están certificados por ningún control: en §4 del alcance la Integridad de "Metadatos listado/delisting" es "—" (sin .CHECKSUM), y A02-DATA-001 solo hashea archivos con .CHECKSUM del origen. Un listing_date erróneamente temprano hace que el dato "conforme" a un metadato falso pase trivialmente. El control valida el point-in-time contra el propio artefacto que lo define, sin ancla independiente.

ATAQUE 3 (cobertura): VULNERABLE — El censo (§6/§5) es de fuente única opcional ("anuncios Binance / símbolos Tardis / CoinGecko", el "/" admite una sola). No se exige multi-fuente, ni que el censo sea point-in-time, ni que se audite su completitud. Si el censo es un subconjunto sesgado, la cobertura puede dar 100% de un denominador truncado. Peor: Tardis figura como fuente de datos Y de censo — pueden compartir origen, rompiendo la "independencia" que §6 presume.

ATAQUE 4 (reproducibilidad): VULNERABLE — A02-META-012 caduca el dictamen SOLO al cambiar hash de raw. Pero los controles corren sobre normalized/, generada por script. Si cambia el parser y el raw no, los datos evaluados cambian y el dictamen NO caduca. Además el censo externo (mutable) no está hash-pineado en el manifest ni cubierto por §9: un dictamen de COBERTURA puede seguir "vigente" sobre un censo que ya cambió. A02-META-011 solo compara dos corridas con el MISMO código: no detecta no-determinismo entre versiones.

ATAQUE 5 (independencia): VULNERABLE — §10 exige independencia recolector↔A-02, pero deja dos puertas: (a) §7/§10 entregan el UMBRAL de cobertura al "consumidor" (F0/C-002), justo quien necesita un CONFORME para promover. El que quiere aprobar fija la vara. (b) La construcción del censo (denominador) no tiene requisito de independencia; si el equipo recolector arma el censo, la parte certificada controla su propio denominador.
──────────────
VULNERABILIDADES ADICIONALES:
1. Sin regla de agregación al veredicto global. No hay función que mapee combinaciones 🔴/🟠/🟡 a CONFORME / CON LIMITACIONES / NO CONFORME. Varios 🟠 pueden totalizarse como "CON LIMITACIONES" sin criterio que fuerce NO CONFORME.
2. Metadatos sin control de integridad propio. 003/004/005 dependen de listing/delisting, pero ningún control certifica esa metadata (sin checksum, "POR DEFINIR").
3. "Explicado/documentado" sin validador ni autor definido (002 duplicados, 003 gaps). El propio recolector puede escribir "mantenimiento" y neutralizar el bloqueo.
4. Censo no versionado ni pineado. No entra en MANIFEST.json ni en la vigencia §9; el dictamen de cobertura es irreproducible por construcción.
5. Determinismo auto-certificado. A02-META-011 hace que A-02 certifique su propia determinación sin verificación externa.
6. Falso-rechazo por checksum ausente en origen. A02-DATA-001 exige 100% vs .CHECKSUM; §9 admite que binance.vision puede no publicar checksum. Un archivo válido sin .CHECKSUM → 🔴 injusto.
7. Categorías de ausencia degradadas a limitación por decreto (§2 OI). Un dataset hueco se etiqueta "CONFORME CON LIMITACIONES".
8. Frontera "outlier vs absurdo" indefinida (A02-DATA-009). Un salto ×10^n puede clasificarse como outlier no bloqueante.

UMBRALES ARBITRARIOS / INDEFINIDOS:
- Cobertura: "declarado por el consumidor" sin piso mínimo.
- "Materialidad" 🟠 vs 🔴 en cobertura: sin definir ni juez.
- "Tasas absurdas" de funding: sin cota.
- Frontera outlier / absurdo lógico: sin definir.
- "Explicado/documentado" (002/003): sin definir.
- "N delistados" del spot-check: sin fijar.
- Regla de agregación al veredicto global: inexistente.

DEPENDENCIAS CIRCULARES:
1. Point-in-time (004) se valida contra la metadata que él mismo debería auditar; metadata no certificada → circularidad sin ancla externa.
2. Cobertura (005) mide contra un censo cuya completitud nunca se valida.
3. Determinismo (A02-META-011): A-02 certifica su propia determinación.
4. Umbral de cobertura fijado por el consumidor que se beneficia del CONFORME → juez y parte.

RUTAS DE FALSO CONFORME:
- Defectuoso→CONFORME: (a) consumidor declara umbral bajo → survivorship masivo obtiene COBERTURA CONFORME. (b) censo incompleto → cobertura 100% de denominador truncado. (c) metadata con listing_date temprano-pero-consistente → 004 pasa, look-ahead sobrevive. (d) recolector auto-documenta gaps/duplicados como "mantenimiento" → 🔴 degradado a 🟡. (e) sin regla de agregación, varios 🟠 → "CON LIMITACIONES" en vez de NO CONFORME. (f) cambio de parser sin cambio de hash raw → normalized distinto, dictamen no caduca.
- Válido→rechazado: (g) archivo correcto sin .CHECKSUM en origen → imposible 100% → 🔴. (h) delisting_date truncado → dato real marcado como violación post-delisting → 🔴 injusto.
──────────────
Observaciones de dieta: Respetada (solo los 3 archivos). Contexto de sistema fuera de dieta ignorado. Sin web ni código.
VEREDICTO: NO CONFORME
Firma: Revisor adversarial · 2026-07-29 · sesión independiente
```

---

# Dictamen adversarial — Contrato QA/A-02 (v2)

> 2º pase, sesión independiente (dieta: alcance v2 + QA/A-02 v2 + DATA.md) el 2026-07-29. Append-only. **Resultado: NO CONFORME.** Hallazgo de fondo: la independencia de PROVENIENCIA no es alcanzable con fuentes todas derivadas de Binance; el axioma anti-circularidad §0 se contradice a sí mismo con la realidad de datos del proyecto. El revisor expone; no corrige.

```
DICTAMEN ADVERSARIAL — Contrato QA/A-02 v2
ATAQUE 1 (universo): VULNERABLE — CENSO-02 "el raw delata" es UNIDIRECCIONAL: solo detecta símbolos en raw-pero-no-censo. Un símbolo purgado en el origen que nunca dejó rastro en el raw recolectado es invisible para ambas anclas a la vez. El universo esperado puede quedar sistemáticamente incompleto sin que ningún control lo revele.
ATAQUE 2 (point-in-time): VULNERABLE — PIT-01 (intersección metadata × trade observado) toma el borde más estrecho: un hueco de recolección al inicio/fin del raw NO se lee como hueco, se COLAPSA en "aún no cotizaba / ya no cotizaba". PIT-03 solo cubre la dirección contraria. Pérdida de datos de borde absorbida como límite natural, indetectable para QUAL-02 (que evalúa gaps contra esa misma ventana).
ATAQUE 3 (cobertura): VULNERABLE — El "piso independiente" (§6/§8) es placeholder ("≥X%, a proponer y arbitrar"; §11 admite que no fija valores). No cambió CUÁNTO, solo QUIÉN lo pone. Y el % se mide contra un denominador que bajo Ruta B puede subcontar: 95% de un censo que ya omitió delistados es un 95% engañoso reportado "crudo".
ATAQUE 4 (reproducibilidad): VULNERABLE — REPRO-01 pinea raw+parser+censo_hash+a02_version, pero NO la 2ª fuente de cross-reconciliación, la fuente de muestreo (Ruta B), ni las ≥2 fuentes de PIT-02, ni las decisiones/tolerancia de reconciliación. Se pinea el hash de SALIDA del censo, no las entradas. Fuentes live pueden mutar entre corridas.
ATAQUE 5 (independencia): VULNERABLE — §7 exige independencia de ROLES, no de PROVENIENCIA. CENSO-01 verifica censo ≠ fuente OHLCV, pero NO que las dos fuentes del censo sean independientes de un upstream común. "Anuncios Binance / Tardis / CoinGecko" derivan todas de Binance (Tardis re-empaqueta, CoinGecko ingesta): dos espejos del mismo origen = independencia aparente, ceguera correlacionada.
VECTORES a-i: a VULNERABLE (Ruta A puede ser 2 derivados de Binance); b VULNERABLE (misma omisión histórica → acuerdo = falsa confianza, CENSO-02 no lo atrapa); c VULNERABLE (CENSO-02 unidireccional; víctima de survivorship sin rastro en raw es indetectable); d VULNERABLE (piso tan arbitrario como el umbral que reemplazó, solo mudó de dueño); e VULNERABLE (hueco de borde leído como listing/delisting falso); f VULNERABLE (intersección crea look-ahead nuevo: define "debía cotizar" a partir de "cotizó", circular para el gap de borde que pretende detectar); g VULNERABLE (§4 sin estado para controles NO evaluados que la precedencia §2 salta; CONDICIONADA no acumula); h VULNERABLE parcial (insumos de corroboración sin pinear); i VULNERABLE (INT-02 byte-identidad ≠ corrección: corrupción estable pasa; PIT-03 conserva colas basura post-delisting como datos reales).
PREGUNTA FUNDAMENTAL (Ruta B): PUERTA TRASERA. Con una sola fuente, A-02 solo puede afirmar "cobertura X% contra denominador de fuente única no verificable" = survivorship DECLARADO, no CONTROLADO. Ruta B pretende conservar ancla vía CENSO-02, pero es unidireccional y no revela víctimas ausentes de raw y de un censo derivado de Binance. La corroboración por muestreo es OPCIONAL y sin N. Cuando no hay 2ª fuente, Ruta B = fuente única + CENSO-02 (ancla más débil) y aún certifica CONDICIONADA. Y §4 promueve CONDICIONADA → "CONFORME CON LIMITACIONES" global, mientras la COMPUERTA DURA del alcance §0.9 y regla 5 de DATA.md exigen "A-02 CONFORME/APTO": el contrato NO mapea si "CONFORME CON LIMITACIONES" satisface la compuerta → CONDICIONADA se trata de facto como suficiente para promoción.
VULNERABILIDADES ADICIONALES: 1 independencia de proveniencia indefinida (§0b/CENSO-01); 2 CENSO-02 unidireccional; 3 §8 tabla de placeholders (piso, materialidad, cota funding, N, tolerancia PIT-02, ×10^n, muestreo Ruta B); 4 INT-02 byte-identidad≠corrección; 5 PIT-03 conserva colas basura; 6 PIT-01 colapso de huecos de borde; 7 §4 sin estado "no evaluado"; 8 CONDICIONADA no acumula (cajón de sastre); 9 desajuste "CONFORME CON LIMITACIONES" vs "A-02 APTO" sin puente; 10 insumos de corroboración sin pinear; 11 el axioma §0 usa raw como ancla "independiente" pero raw comparte origen (binance.vision) con censo Ruta B y datos → circularidad reintroducida por el propio axioma.
DEPENDENCIAS CIRCULARES: 1 L1↔L2 (ventana definida por trades, gaps evaluados contra esa ventana); 2 raw como verificador "independiente" del censo compartiendo origen Binance; 3 Ruta A de origen común = auto-confirmación disfrazada.
VEREDICTO: NO CONFORME
Firma: Revisor adversarial · 2026-07-29 · sesión independiente
```

## Nota de transición
v1 (NO CONFORME, circularidades) → v2 (rediseño de anclas, censo de dos rutas) → **v2 NO CONFORME**: el ataque de proveniencia revela un límite que no es un bug del contrato sino de la realidad de datos (todo deriva de Binance). Pendiente decisión estratégica del IP antes de v3.
