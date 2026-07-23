# Expediente — Dictamen A-04 NO CONFORME sobre F2 (Ciclo C-001)

> Abierto 2026-07-20. Append-only. Reúne los hechos para que el IP decida el tratamiento de V-001. **No decide** — el tratamiento es del IP. Sigue la secuencia acordada: identificar → norma literal → qué falta → dictamen → confirmar si es solo el JSONL → **auditar si F2 puede expresarse en el esquema JSONL** → recomendación.

## 1. Identificación inequívoca del artefacto

| Ítem | Valor |
|---|---|
| Archivo | `docs/INVESTIGACION/BANCO/fases/F2_ARBOL.md` |
| SHA-256 | `f610b4938447a94f0ec83435bd6d6a6ecbe4b55404550cec9781b0742773e088` |
| Estado en git | **No commiteado aún** (working tree; F2 se ejecutó tras el commit `c50c9d6` de cierre de F1) |
| Fecha de contenido | 2026-07-20 · Ejecutor: Opus |
| Dictamen A-04 | `F2_DICTAMEN_A04.md` (SHA-256 `22c0109230934fdcb705a4da4ce1f562ef58b919a640a1725c53e14cbefab0fd`) |
| Norma auditada | `ORQUESTADOR.md` (SHA-256 `f75e9e76975694490ccf8b7872de45e45a8690634a96229f56ff7d6c3f38cee7`) |

## 2. Norma aplicable (texto literal)

**Regla dura 9 (ORQUESTADOR L23) — la que se incumple:**
> "**Artefactos estructurados, no solo narrativos:** desde F1, **cada fase produce su registro en formato estructurado (JSONL: un objeto por entrada) más una vista Markdown generada a partir de él — nunca al revés.** Esquema del registro de F1: `{id, mecanismo, familia, variante, nombre, mecanismo_economico_1frase, mercados_documentados, fuente:{...}, nivel_evidencia_preliminar, reproducibilidad, observaciones}`. Las fases posteriores AÑADEN campos al mismo registro (F3: nivel_evidencia_final, robustez_reportada[]; F4: fundamento, falsacion[]; F5: transferibilidad; F7: puntuaciones) — **un solo objeto por edge, enriquecido fase a fase.**"

**Las tres cláusulas que la contradicen (contradicción C-001 del dictamen):**
- (b) Tabla de Fases, fila F2 (L62): *"| F2 | Árbol genealógico por mecanismos | Opus | `F2_ARBOL.md`: mecanismo → familia → variante, con herencia de evidencia |"* — nombra **solo el .md**.
- (c) La enumeración de la propia regla 9 sobre qué fases AÑADEN campos (F3/F4/F5/F7) **OMITE a F2**.
- (d) Prompt F2 (L95): *"Producto: el árbol completo + tabla de herencia de evidencia."* — **no menciona JSONL**.

## 3. Qué exige la norma y qué falta

Regla 9 exige, para toda fase desde F1: **(i)** un registro estructurado JSONL (un objeto por entrada) como **fuente de verdad**, y **(ii)** una vista Markdown **generada a partir de él**. F2 entregó **solo (ii)** (`F2_ARBOL.md`), sin (i). **Artefacto faltante: el JSONL de F2.**

## 4. El dictamen A-04

Resultado **NO CONFORME**, una sola violación:
- **V-001:** ausencia del artefacto estructurado JSONL de F2 (regla 9). Única violación.
- **C-001 (contradicción reportada, no resuelta):** las cuatro cláusulas de §2 en tensión (¿F2 lleva JSONL o no?).
- **O-1/O-2/O-3:** observaciones no bloqueantes (lenguaje "el caso más fuerte" roza priorización; referencias a H-001 fuera de dieta; compuertas administrativas downstream).

## 5. ¿El problema es SOLO el JSONL, o hay algo más?

**Solo el JSONL.** El dictamen verifica CONFORME todo el fondo de F2: estructura de árbol mecanismo→familia→variante, agrupamiento por ineficiencia (no por indicador), herencia de evidencia + tabla, evidencia específica de variante anotada, casos frontera con doble ubicación sin forzar, asignación provisional (F4 confirma), **fidelidad a F1 (las 30 entradas ubicadas, ninguna inventada)**, auditar-no-calcular, sin priorización/ranking/veredictos, documento fechado y ejecutor declarado, cierre no autodeclarado. **El bloqueo es exclusivamente de FORMATO (falta el JSONL), no de contenido.**

## 6. Auditoría: ¿puede F2 expresarse legítimamente en el esquema JSONL? (paso 2 del IP)

**Sí, sin forzar.** Demostración:

1. **El árbol ya está codificado por-registro en el JSONL de F1.** El esquema de F1 incluye `mecanismo`, `familia` y `variante` en cada objeto. Es decir, la jerarquía MECANISMO→FAMILIA→VARIANTE **ya es un atributo de cada entrada**; el "árbol" es la agrupación de esos campos. No hay estructura de F2 que no quepa en "un objeto por entrada".
2. **Lo que F2 añade es enriquecimiento por-registro**, exactamente el modelo de regla 9 ("un solo objeto por edge, enriquecido fase a fase"): a cada una de las 30 entradas se le añaden campos F2 — p.ej. `mecanismo_confirmado_prov` (provisional, F4 confirma), `tipo` (edge/teoría/método), `nivel_consolidado_mecanismo`, `frontera:{es_frontera:bool, ubicaciones:[...]}`.
3. **La "tabla de herencia" es una VISTA (agregado) del JSONL**, no un objeto suelto: es un `GROUP BY mecanismo` sobre los registros enriquecidos. Encaja perfectamente en "vista Markdown generada a partir del JSONL — nunca al revés".

**Conclusión de la auditoría:** no hay obstáculo estructural. El JSONL de F2 es **obligatorio** (regla 9, cláusula superior) **y expresable** (el árbol es enriquecimiento por-registro; la tabla de herencia es la vista/agregado). Por tanto, por la propia regla de decisión del IP —*"si el JSONL es obligatorio → producirlo; si la estructura de F2 no puede expresarse legítimamente en el esquema → estudiar modificación normativa"*— corresponde **producirlo**, no una exención.

## 7. Recomendación (no decisión)

- **Levantar V-001 produciendo el JSONL de F2** (`F2_arbol.jsonl`): 30 objetos, cada uno = una entrada de F1 enriquecida con los campos F2 (mecanismo provisional, tipo edge/teoría/método, nivel consolidado del mecanismo, frontera). Regenerar `F2_ARBOL.md` como su vista declarada. Luego **re-arbitraje A-04**.
- **La contradicción C-001 del ORQUESTADOR** (fases-tabla y prompt nombran solo el .md; la enumeración omite F2) NO se parchea a mitad de ciclo: se registra como **ADR pendiente para el F0 del C-002** (regla de inmutabilidad, regla 8) — que aclare que F2 sí produce JSONL y lo añada a la enumeración de la regla 9.
- **Descartada la exención ad-hoc** (opción 2): la auditoría muestra que F2 sí es expresable, así que una exención no está justificada.

La decisión final es del IP.
