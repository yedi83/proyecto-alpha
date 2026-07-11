# Changelog

## 2026-07-10

- **ADR-0004 — Moratoria de diseño hasta cerrar C-001:** toda idea/mejora → ADR pendiente para C-002; únicas excepciones, las ya definidas (defecto fatal, violación metodológica). Criterio de éxito del ciclo incorporado al acta: decisiones metodológicas respaldadas por evidencia, aun contra las expectativas. Último acto de diseño de la fase de arquitectura.
- **Cierre de la fase de arquitectura:** ADR-0003 "Nunca optimizar antes de medir" (mejoras exigen evidencia operativa del ciclo; se aplican en el siguiente); F0 §8 instrumentación del propio ciclo (latencias, bloqueos, fricciones) inaugurando la métrica de latencia del conocimiento; acta de apertura del C-001 en borrador (texto del IP), pendiente de sellado tras dictamen A-04.
- **Operacionalización del flujo del Banco:** A-04 con modo VALIDADOR ESTRICTO (dieta de insumos mínima, verificación literal, plantilla fija de dictamen, calidad fuera del alcance — la juzga el IP); regla 9 artefactos estructurados (JSONL fuente de verdad + Markdown como vista, un objeto por edge enriquecido fase a fase); regla 10 compuertas objetivas (dictamen + artefacto + aprobación IP, nunca juicio informal); F1 como ejecutor puro.
- **Auditoría anual de Creencias** (regla 9 de TEORIA.md, mismo día que la de Simplicidad): ¿qué damos por cierto que hace un año era hipótesis? Todo ascenso de estatus debe citar su veredicto del pipeline; ascenso sin veredicto trazable se revierte de oficio. Contra el riesgo humano de "esta vez ya sabemos la respuesta".
- **Regla de Inmutabilidad del Ciclo + apertura administrativa:** F0 inmutable durante el ciclo tras CONFORME de A-04 (problemas → ADR pendiente → F0 del ciclo siguiente; defecto fatal → aborto con acta); ciclos identificados (C-001…) con checklist de apertura de 6 puntos y tag de git; hipótesis trazables a su ciclo de origen.
- **F0 del Banco de Mecanismos cerrada (pendiente dictamen A-04):** ciclo 1 piloto por mecanismos (persistencia/carry/reversión/microestructura/régimen-como-filtro), rúbrica 35/30/20/10/5 con anclas y sensibilidad obligatoria, resiliencia como compuerta (no puntaje), salida 0-5 protocolos sin mínimo, niveles de evidencia I-VII.
- **Principio 16 — Costo de Gobernanza** (absorbe tres propuestas en una pieza, aplicándose a sí mismo): toda regla nueva justifica qué error evita, qué cuesta y qué elimina; los componentes del laboratorio son hipótesis de diseño; Auditoría de Simplicidad anual (primera 2027-07). TEORIA.md: entradas como "estado actual de la evidencia" con confianza en bandas (no porcentajes de precisión falsa). Banco renombrado a **Banco de Mecanismos** (estrategias = implementaciones). Dormidos con disparador: Cementerio Científico (~50 hipótesis), Curador del Conocimiento (~2027-01, en backlog de agentes).
- **`docs/TEORIA.md` fundada (v0.1):** Teoría del Laboratorio — documento vivo de creencias sobre mecanismos con estados epistémicos (✓/△/✗/⊘), cada una con su linaje de evidencia; las rechazadas alimentan con el mismo peso; no normativo (nada se opera desde ahí). Sembrada con lo ya aprendido de H-001: rotación de contribuyentes ✓, convexidad no consistencia ✓, crisis-alpha-por-shorts falsada ✗, persistencia mayor en alts △, funding ⊘.
- **Principios 14 y 15 en la Constitución:** separación explícita generación-de-conocimiento / producción-de-evidencia (Banco genera, Pipeline evidencia, Registro conserva, A-04 vigila, humano decide — nadie invade a nadie) y ADR de primera clase con las 5 preguntas, incluida la obligatoria condición de revisión futura. Plantilla ADR v2.
- **Banco v3 + A-04** (segunda ronda de correcciones del investigador): niveles de evidencia I-VII en F0 (sin promediar entre niveles), F2 elevada a árbol genealógico enraizado en MECANISMOS con herencia de evidencia, falsabilidad económica popperiana obligatoria en F4, versionado científico H-XXX.vN formalizado en PROTOCOLO, y **A-04 Árbitro de Metodología** creado (agents/): audita cumplimiento del proceso en todo el laboratorio, dictamen VIOLACIÓN bloqueante, sin opinión sobre trading.
- **Banco v2** (mismo día, correcciones del investigador aceptadas): F2 deduplicación por edge subyacente (nueva), auditoría de robustez fusionada en evidencia (audita, no calcula), transferibilidad como cadena mecanismo→ingredientes→veredicto, F6 diseño experimental en dos sesiones (diseñador/adversarial separados), mapa de complementariedad sin pesos, y principio rector reformulado: "el banco entrega el diseño experimental del pipeline" — protocolos pre-registrables, umbrales ratificados por el humano.
- **Banco de Estrategias** (`docs/INVESTIGACION/BANCO/`): orquestador F0–F6 creado desde el borrador del investigador, con cirugía documentada — F4 redefinida a "traducibilidad" (un LLM no mide robustez), F7-portafolio eliminada (requiere estrategias validadas; es el componente Asignación de Capital), F8 absorbida en las fichas. Reglas duras: fuentes verificadas, prohibido inventar métricas, producto final = fichas candidatas para el REGISTRO.

- Resumen de las 3 instancias (día 8 de Fase A): fixes de frontera validados en el ensayo (fees 10/10, 0 fills sin precio); feed mainnet cuantificado (~0.9 atrasadas/día/símbolo vs 1.5 testnet / 2.2 demo); bot_state del lab verificado OK en máquina.
- paper_real documentado con sección de gobernanza (no-evidencia de A/B; insumo de la decisión de C; keys vacías confirmadas — el hallazgo de seguridad del resumen era falso positivo). Detectada discrepancia PREREG (0.1% uniforme) vs código (RISK_MAP BTC 0.125%): erratum del investigador pendiente.
- `.gitignore`: `paper_real/bot/` fuera de git; `paper_real/paper/` (serie de comparación de feed) sí se versiona.

## 2026-07-04

- **Vigía operativo:** tarea `vigia_donchian` (schtasks cada 15 min, ruta completa al `pythonw` del venv para evitar fallo silencioso por PATH); `vigia.log` escribiendo `OK`. H2 cerrado — el hallazgo del checklist estaba desactualizado (el vigía ya corría).
- **Ensayo de Fase B arrancado:** montaje completado, keys demo corregidas (−2014 formato → −1022 firma → OK), conecta a demo con `eq=750`, una sola instancia. F0 confirmado en vivo (enable_demo_trading + assert de endpoint demo → se niega a operar si no es demo).
- **Arranque automático del ensayo:** `bot/lanzar_ensayo.bat` (auto-reinicio, sleep headless-safe con `ping`) + tarea `ensayo_faseB_lanzador` (al iniciar sesión). La ruta con espacios sin comillas daba `0x80070002` (archivo no encontrado); re-registrada con `Register-ScheduledTask` (ejecutable + directorio separados, runtime ilimitado, batería) y probada OK.
- **Rescate de git:** índice corrupto en la copia de trabajo (`bad signature`); reconstruido trasplantando el `.git` de un clon limpio, 0 pérdida de datos (working tree == HEAD, solo CRLF). `core.autocrlf=true` para cortar el conflicto CRLF Windows/Linux; pendiente `.gitattributes` commiteado (`* text=auto eol=lf`).

## 2026-07-03

- `docs/TRASPASO.md`: plan de trabajo para próximas sesiones con cualquier modelo — guardarraíles, tareas fechadas (cierre Fase A 07-12, día D, rutinas), y tabla de qué tarea exige qué modelo.
- `ensayo_faseB/`: ensayo general aislado del bot de frontera (órdenes demo, EQUITY_CAP=750, reglas no-evidencia).
- `bot/live_bot_faseB.py` (staged, NO ejecutar en Fase A): versión de frontera con los 4 cambios aprobados — demo trading, fill vía fetch_order con fallback declarado, fees desde fills, riesgo por símbolo con cap por suma real. Se aplica el día D con el checklist del paquete.
- **exp-002 y exp-003 (riesgo por símbolo):** 0.15% RECHAZADO por umbral pre-escrito; 0.125% pre-registrado como intento final (N=2) y ACEPTADO con el mismo umbral. M1 cerrado: $750 + BTC 0.125%. Paridad del motor con la frontera original verificada (24.03/-17.8/0.42).
- **Fontanería ejecutada + `PAQUETE_FASE_B.md`:** BTC min demo $50 vs mainnet $100 (brecha demo/producción → métrica nueva de B); bugs pre-B descubiertos: fill price None en create_order (B-fix1) y fees solo en fills (B-fix2). Decisión M1: $750 + riesgo BTC 0.15% condicionada a exp-002. Acta borrador y checklist de arranque de B listos.
- **Hallazgo F0** (primer intento de fontanería): ccxt ≥4.5 retiró el testnet de futuros de Binance → script migrado a `enable_demo_trading` (keys de demo.binance.com); el bot necesitará la misma migración al arrancar Fase B. Registrado como bloqueante pre-B en ESTADO.
- `fontaneria_ordenes.py` (prep. Fase B, cuenta testnet separada): límites reales por símbolo (verifica M1), round-trip con inspección de fees, firma exacta del rechazo por min_notional en BTC, funding history, limpieza verificada. Decisión M1 (capital/BTC) diferida a sus resultados, registrada.
- `replay_offline.py` (cierre de Fase A): recomputa señales con fórmulas congeladas, estado dirigido por eventos reales, criterios C1/C2/C4/C5 del PREREG, clasificación de velas saltadas (M2), selftest sin red en verde.
- Revisión adversarial de código (bot vs. especificación vs. backtester): señal idéntica confirmada, 0 divergencias bloqueantes. Hallazgos M1 (omisión BTC por min_notional casi cierta con $750 — decisión pre-B desbloqueada), M2 (vela saltada invisible — requisito del replay), M3 (maxDD por activo del veredicto inicial subestimado; cifras válidas = cesta corregida). Informe en `research/H-001-canal-donchian/report/`.
- `docs/CONTRATOS.md` (tarea 0.4): vela (identidad = apertura UTC), funding (signo = contribución cobrada), señal (intención, no orden), experimento (config+datos+hash), eventos/trades (esquemas vivos adoptados tal cual). **Etapa 0 cerrada.**
- Checklist línea base de Fase A: instrumentación OK; hallazgo real (vigía sin registrar); falsa alarma de heartbeat resuelta (caché del lector remoto, lección registrada).
- `RISK_POLICY.md`: límites transcritos del sistema vivo (0.10%/trade, cap 0.60%, máx 5, kill diario -5% blando) + matiz documentado del kill switch + pendientes de Fase C.
- `DATA.md`: fuentes verificadas en código (cache 15m origen Binance; bot en testnet), sesgos con tratamiento, funding real como incógnita nº 1, requisitos del Data Lake.
- Verificado: el test de sensibilidad 384/512/640 NO se ejecutó — decisión pendiente antes de Fase C.

## 2026-07-02 (hipótesis económica H-001)

- A-03: `research/H-001-canal-donchian/HIPOTESIS_ECONOMICA.md` — mecanismo (subreacción + cascadas de liquidación + límites al arbitraje conductuales), contraparte identificada, 5 predicciones falsables (P1 ya consistente), 4 señales de retiro conceptual. Formulada ex-post y así declarada.

## 2026-07-02 (inventario del lab original)

- **Inventario de `donchian512_lab`** (`docs/MIGRACION.md`): pre-registros y 17 informes migrados a `research/H-001-canal-donchian/`. Regla maestra: el sistema vivo no se toca hasta cerrar Fase A.
- **Enmienda de gobernanza** en `CRITERIOS_FASES.md`: la Fase A en curso se rige por su PREREG original (acta 2026-07-02 03:53 UTC); la tabla del repo queda como plantilla futura.
- **Ficha H-001 reescrita**: pre-registro reconocido como original (no retroactivo), 5 preguntas respondidas con evidencia, métricas consolidadas (Sharpe ~0.42, alfa t=0.94 NS, top-5 trades = 115% del neto), corrección visible en el registro de hipótesis.
- `.gitignore`: añadido `config.env` (el lab contiene API keys que jamás deben entrar al repo).

- **Criterios de la Fase A fijados antes de evaluar** (tarea 0.1 del plan): 28 días + ≥15 señales, uptime ≥99%, coincidencia bot/backtester 100%, latencia ≤60 s, velas perdidas ≤0.1%, reconexión automática ≤2 min. Regla: todos aprueban o la fase reprueba. Ficha H-001 actualizada: 512 velas de 15m (~5.3 días), 5 pares.

- Sistema de agentes (ADR-0002): A-01 Validador Estadístico, A-02 Auditor de Datos, A-03 Investigador Cuantitativo (restringido a H-001 hasta cerrar Etapa 0). Backlog de 13 agentes con condiciones de activación en `docs/AGENTES.md`. Principio 13 añadido a la Constitución: la IA no toma decisiones de trading.
- `docs/PLAN_TRABAJO.md`: análisis de arranque, etapas 0–4 (teoría → migración → programación), contratos a diseñar, disciplina de git.
- Convención de carpetas por hipótesis: `research/_template/` copiable, `research/H-001-canal-donchian/` creada, `strategies/` (biblioteca de validadas congeladas).

## 2026-07-01

- Creación del repositorio con estructura documental completa.
- ADR-0001: adopción del proceso centrado en hipótesis.
- H-001 (Canal de Donchian) registrada como hipótesis en validación, Fase A.
- Pendiente: migración del código existente (backtester, bot, dashboard) y completar campos PENDIENTE de criterios y riesgo.
