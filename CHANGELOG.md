# Changelog

## 2026-07-03

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
