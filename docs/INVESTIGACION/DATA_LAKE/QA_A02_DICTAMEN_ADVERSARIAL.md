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

---

# Dictamen adversarial — Contrato QA/A-02 (v3)

> 3er pase, sesión independiente (dieta: alcance v2 + QA/A-02 v3 + DATA.md) el 2026-07-29. Append-only. **Resultado: NO CONFORME.** Convergencia de 3 pases: sin fuente externa genuinamente independiente, el survivorship no se CONTROLA, solo se DECLARA/ACOTA — y la cota es solo sobre ausentes-conocidos. El revisor expone; no corrige.

```
DICTAMEN ADVERSARIAL — Contrato QA/A-02 v3
VECTOR 1 "material/cota razonable": VULNERABLE — §11 confiesa que no fija valores ("los ubica y les asigna dueño"). Placeholders de v2 con nombres nuevos; el dueño fija el umbral sin anclaje externo.
VECTOR 2 APTO-ACOTADO puerta de escape: VULNERABLE — el puente §2 colapsa 4 estados a binario: APTO y APTO-ACOTADO pasan. La frontera ACOTADO↔NO APTO usa "cota razonable" (indefinida) y "sigue mostrando evidencia" (sin umbral estadístico → cualquier edge no-nulo pasa). Casi todo lo defectuoso entra como ACOTADO.
VECTOR 3 test de cota (§3): VULNERABLE (fatal) — (a) "plausible" elegible a gusto; (b) AUTODESTRUCCIÓN: para un ausente ilíquido, −100% sin liquidez = no operable = PnL≈0 → el edge sobrevive trivialmente; el peor caso es benigno para justo los símbolos más sospechosos; (c) enumerar ausentes exige censo completo que §8 admite que puede fracasar → cota solo sobre ausentes-conocidos, presentada como cota del universo.
VECTOR 4 censo medible: VULNERABLE/circular — denominador Binance-derivado; 99% de un denominador sesgado sigue sesgado. Criterio de fracaso circular: medir "fracción faltante" exige conocer el universo verdadero, que es lo que el censo incompleto no da.
VECTOR 5 wash-trading (§4): VULNERABLE — solo se MENCIONA, no se GATEA. La tabla de estados §2 no tiene condición de wash; el template lo imprime informativo. Dataset con wash masivo pasa QA (wash no es control QA), sobrevive §3, y obtiene APTO con edge inflado por trades falsos.
VECTOR 6 caducidad/responsable: VULNERABLE — "responsable nombrado" sin exigir independencia; la parte que promueve puede fijar "material/cota" y renovar la revisión → juez y parte por la puerta de gobernanza.
VECTOR 7 estados↔compuerta: VULNERABLE — mapeo por prosa holística, no función total. Solo integridad tiene regla dura, pero nada mapea "INTEGRIDAD NO CONFORME"→NO APTO global; un 🔴 puede convivir con APTO-ACOTADO global.
VECTOR 8 survivorship de selección (§5): VULNERABLE por admisión — se nombra, no se controla; ungated por diseño (caso vivo: BTC/ETH/SOL elegidos entre majors vivos).
VECTOR 9 circularidad residual: VULNERABLE — §3←§8-censo←raw(binance.vision)←mismo origen que las fuentes del censo (anuncios Binance, exchangeInfo). Único ancla externa = Tardis, OPCIONAL/condicional; sin comprarlo, lazo cerrado sin ancla externa.
ADICIONALES: 1 certificación depende de estrategia (APTO = propiedad dato+estrategia, no dato → certification-shopping); 2 fracaso del censo se vuelve vía de promoción (§8→§3 sobre censo incompleto); 3 "suficientemente verificado" sin % mínimo; 4 restatement depende de anclas opcionales; 5 "nivel de confianza" del censo sin escala.
SOBRE-BLOQUEO SIMÉTRICO: dataset completo con proveniencia única y sin Tardis → CONDICIONADO injusto (reintroduce el over-blocking de v2); edge legítimo pequeño puede morir bajo −100% no representativo → NO APTO injusto.
VEREDICTO: NO CONFORME
Firma: Revisor adversarial · 2026-07-29 · sesión independiente
```

## Convergencia de los tres pases (nota para el IP)
v1 (circularidades) → v2 (rediseño de anclas) → v3 (censo + cota + 4 estados) → **los tres NO CONFORME por la misma raíz**: no existe ancla externa a Binance en datos gratuitos. La cota de survivorship (el escape "inteligente") es autodestructiva para los símbolos que importan. Decisión estratégica pendiente del IP: **comprar el ancla externa (Tardis) o aceptar el survivorship como limitación declarada+acotada de alcance, no controlada.** No es un problema de redacción de v4.

---

# Dictamen adversarial — Contrato QA/A-02 (v4, alcance B)

> 4º pase, sesión independiente (dieta: alcance v2 + QA/A-02 v4 + DATA.md) el 2026-07-29. Append-only. **Resultado: NO CONFORME.** Naturaleza DISTINTA a v1–v3: v4 acertó el ALCANCE (B, no afirma controlar survivorship) pero falla en ENFORCEMENT — la arquitectura honesta no se auto-obliga. El revisor expone; no corrige.

```
DICTAMEN ADVERSARIAL — Contrato QA/A-02 v4
FLANCO 1 (Declaración honesta vs fuga):
 1 Declaración decorativa — VULNERABLE: nada obliga a F0 a leer/actuar la Declaración; la compuerta dura (ALCANCE §0.9/regla 5) solo exige "calidad CONFORME + manifiesto", no acuse ni acción sobre §4. Dataset con calidad CONFORME y puntos ciegos enormes promueve igual.
 2 "depende de la cola ausente" sin criterio — VULNERABLE (núcleo): §2 hace descansar la disciplina C en esa distinción, sin definición/test/umbral. La arbitrariedad no salió; se RELOCALIZÓ de "material/plausible" (v1–v3) a "depende de la cola ausente", igual de indefinida y ahora load-bearing (§7 falsamente dice que se eliminó).
 3 Re-etiquetado tail→no-dependiente — VULNERABLE: F0 juzga la dependencia (§2) Y promueve, pero NO está en la tríada de independencia §5. Juez-y-parte sobre la clasificación que abre el carril barato; re-etiquetar "no depende" es trivial y no policiado.
 4 Declaración incompleta/optimista — VULNERABLE: v4 degradó silenciosamente el censo de EXTERNO (ALCANCE §5) a binance-derivado (§1B/§4) y cruza censo↔raw de misma proveniencia. No revela símbolos que Binance nunca publicó → el punto ciego (a) es sistemáticamente mayor que lo que "cobertura observada" sugiere. Sin control de completitud.
FLANCO 2 (calidad realmente gateada):
 5 WASH no gateado — VULNERABLE (clave): heurísticas sin un solo valor (§3/§7 placeholder); "grueso" indefinido; y el sub-grueso se declara punto ciego. Un wash calibrado bajo el umbral indefinido que INFLA el edge no dispara → 🟢 → CONFORME → promueve. El gate no gatea justo el wash que importa.
 6 Agregación — VULNERABLE: sin tope/escalado por acumulación (N 🟠 graves nunca suman 🔴); y no se define si "CONFORME CON OBSERVACIONES" cuenta como "CONFORME" para la compuerta. PIT solo emite 🟠 (nunca bloquea).
 7 "artefacto independiente" (duplicados) — VULNERABLE parcial: excluye la nota del recolector pero no define qué SÍ vale ni quién valida su independencia → discreción del certificador reabre juez-y-parte.
 8 REPRO — VULNERABLE: el pin (raw+parser+a02) no consta que cubra los VALORES de umbrales ni el censo de la Declaración; umbral cambia sin bump → veredicto no caduca. Determinismo "por corrida repetida" es auto-certificación.
 9 Independencia §5 — VULNERABLE: enuncia sin mecanismo; y omite a F0 (que juzga dependencia y promueve) de la tríada.
 10 Recaída residual — VULNERABLE parcial: (i) "cobertura observada vs censo" binance-derivado presentada como evidencia = optimismo residual (regresión vs ALCANCE §5); (ii) grado CONFORME anunciado "incluyendo wash detectable" comunica una garantía de wash insostenible. PIT (borde→observación) SÍ resiste.
RECAÍDAS v1–v3: cifra de "cobertura" de proveniencia única como evidencia (§4); etiqueta "wash detectable" en el grado (§0/§8).
RUTAS DE PROMOCIÓN INDEBIDA: (1) tail-dependiente re-etiquetada "no depende" por F0 juez-y-parte → CONFORME basta → promueve; (2) wash bajo umbral indefinido infla edge → CONFORME → promueve; (3) 🟠 graves acumulados → CONFORME CON OBSERVACIONES → si la compuerta lo lee como CONFORME → promueve.
VEREDICTO: NO CONFORME (por (b) Declaración eludible + F0 juez-y-parte de la tail-dependencia; (c) wash no gateado; (a) parcial: residuos optimistas).
Firma: Revisor adversarial · 2026-07-29 · sesión independiente
```

## Lectura (nota para el IP): converge, no hace loop
v1→v3 fallaban por la MISMA raíz (survivorship no controlable) = loop sobre un imposible. v4→ falla por raíz DISTINTA: el alcance B es correcto, pero la arquitectura honesta **no se auto-obliga**. Todos los fallos son de ENFORCEMENT y fixables SIN sobre-afirmar: (1) la Declaración no tiene dientes; (2) "depende de la cola" es el nuevo término indefinido load-bearing, juzgado por quien promueve; (3) el wash se grada en vez de declararse; (4) huecos de mapeo (OBSERVACIONES vs CONFORME, acumulación); (5) cifra de cobertura optimista. Decisión del IP: v5 con dientes, o congelar con observaciones.

---

# Dictamen adversarial — Contrato QA/A-02 (v5, enforcement)

> 5º pase (final bajo regla de parada), sesión independiente (dieta: alcance v2 + QA/A-02 v5 + DATA.md) el 2026-07-29. Append-only. **Resultado: NO CONFORME.** Los huecos restantes son de DOS clases: (A) coordinación entre documentos (la compuerta con dientes de v5 no está cableada en el ALCANCE frozen), y (B) gobernanza de independencia (el contrato asume roles independientes que un lab pequeño puede no tener). El revisor expone; no corrige.

```
DICTAMEN ADVERSARIAL — Contrato QA/A-02 v5
DIENTES:
 (a) IGNORAR — ABIERTO: §1 (3 requisitos) NO deroga la COMPUERTA DURA frozen del ALCANCE §0.9 ("solo CONFORME+pin") ni DATA.md regla 5 ("APTO"). Coexisten 2-3 compuertas y vale la más laxa; se puede promover con solo CONFORME+pin, saltándose Declaración/acuse y dictamen de dependencia. Además "acuse" (§1.2) es auto-emitido por el promotor, sin firma ni testigo → no verificable.
 (b) ELUDIR — ABIERTO: "evidencia positiva" que voltea el default TAIL-DEPENDIENTE (§2) sin criterio; screen mecánico sin umbral de "materialidad" ni de "superado"; nadie tiene autoridad asignada para NOMBRAR al evaluador → reciprocidad cruzada (A evalúa a B, B a A) no prohibida. Independencia "declarada", no forzada.
 (c) MALINTERPRETAR — ABIERTO (residual): internamente v5 lo cierra (§7 sin %, §3 wash fuera del grado), pero el ALCANCE §5/§2 frozen SIGUE exigiendo "cobertura X% demostrada" como entregable; v5 no enmienda el frozen → la cifra-evidencia sobrevive aguas abajo.
CONTROLES ALCANZABLES:
 4 Calidad/acumulación — CON HUECO: "N observaciones graves → NO CONFORME" con N indefinido = placeholder que decide promoción; "🟠 aceptadas por parte independiente" sin criterio de aceptación.
 5 Reproducibilidad — CON HUECO: el pin no cubre el dictamen de dependencia (§1.3) ni las aceptaciones de 🟠 (§4) → promoción no reproducible.
 6 Duplicados/gaps — GATEADO con observación (artefacto definido + separación triple; residual: suficiencia de la explicación es discreción del validador).
 7 Independencia — CON HUECO: F0-promotor excluido es verificable, pero "lab pequeño/rotatoria/se declara cómo se logra" es divulgación, no enforcement; admite back-scratching sin autoridad de nombramiento.
UMBRALES PENDIENTES: N de acumulación [ARQUITECTÓNICO]; criterio de "evidencia positiva" [ARQUITECTÓNICO]; screen mecánico + materialidad [ARQUITECTÓNICO]; criterio de aceptación de 🟠 [ARQUITECTÓNICO]; WASH-FLAG número [implementación]; cutpoints QUAL [implementación].
HUECOS ARQUITECTÓNICOS: (1) §1 sin precedencia sobre §0.9 frozen / DATA.md regla 5; (2) "cobertura % demostrada" reinstalada por el frozen no enmendado; (3) "evidencia positiva" sin criterio + nombramiento del evaluador sin autoridad; (4) N y aceptación de 🟠 sin criterio; (5) pin no cubre dictamen de dependencia ni aceptaciones; (6) "acuse" auto-emitido no verificable.
VEREDICTO: NO CONFORME
Firma: Revisor adversarial · 2026-07-29 · sesión independiente
```

## Aplicación de la regla de parada (nota para el IP)
Los huecos de v5 se agrupan en: **(A) coordinación de documentos** — la compuerta con dientes de v5 no está cableada en el ALCANCE §0.9 frozen, y el frozen aún pide "cobertura % demostrada" (FIXABLE: enmendar el ALCANCE en nueva versión con justificación); y **(B) gobernanza de independencia** — evaluador independiente, autoridad de nombramiento, acuse verificable, aceptación de 🟠: todos asumen ≥2-3 partes independientes que un lab pequeño puede no tener. **(B) no se arregla con redacción** — es el hallazgo de la regla de parada: A-02 fue concebido como compuerta de enforcement con árbitro independiente; si el lab no puede dotar árbitros independientes, A-02 debe reconcebirse como instrumento de DIVULGACIÓN + certificación mecánica de calidad, cuyo enforcement es el juicio documentado del IP + el proceso adversarial, honestamente etiquetado como tal — no fingir una independencia que no se tiene. Decisión estratégica del IP pendiente; no v6.
