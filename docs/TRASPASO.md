# Traspaso de Sesión — Plan de Trabajo para Próximas Sesiones

> Escrito 2026-07-03 al cierre del sprint con Fable 5. Este documento es el punto de entrada para CUALQUIER sesión futura (Opus, Sonnet, Haiku o humano solo). Protocolo de arranque de sesión: leer `ESTADO.md` → `CHANGELOG.md` → este documento → la tarea que toque.

## Estado en una frase

H-001 está en Fase A (dry run, acta 2026-07-02, mínimo 10 días → cierre elegible 2026-07-12), gobernada por su PREREG original; toda la Etapa 0 está cerrada (criterios, riesgo, datos, contratos, hipótesis económica); el instrumento de cierre (`replay_offline.py`) está validado; la Fase B tiene paquete completo, bot de frontera staged y compilado, decisión M1 cerrada por experimentos (exp-002 RECHAZA 0.15%, exp-003 ACEPTA 0.125%), y un ensayo general aislado listo para correr en paralelo.

## Guardarraíles (leer antes de CUALQUIER tarea — violan esto y el trabajo no vale)

1. **El sistema vivo del lab (`donchian512_lab`) NO se toca hasta cerrar la Fase A.** Ni el bot, ni sus CSVs, ni vigia/auditoria, ni el diario (el diario lo escribe el humano).
2. La Fase A/B se gobierna por `research/H-001-canal-donchian/prereg/PREREG_FASE_AB.md`. Cambios solo por ENMIENDA fechada, nunca tras acumular datos de la fase afectada.
3. "Casi pasa = no pasa." Los umbrales pre-escritos no se renegocian después de ver resultados.
4. Experimentos: siempre carpeta `experiments/exp-NNN/` con PREREG escrito ANTES de correr, N de pruebas múltiples declarado, y resultados copiados (RESULTADO.md, metricas.json, DATOS.md). exp-001 está RESERVADO para reproducibilidad.
5. Registros append-only. Secretos jamás en git (`config.env` está ignorado; verificar antes de cada commit).
6. Para revisiones, usar los prompts de `agents/` (A-01 valida experimentos, A-02 audita datos, A-03 investiga con restricciones).
7. Toda sesión termina con `.\scripts\tanda.ps1 "mensaje"` (push obligatorio).

## Tareas, en orden

### YA (humano, minutos)
- [ ] Push de las tandas pendientes de hoy (ensayo + exp-002/003 + bot frontera) si no se hizo.
- [x] Vigía registrado y verificado (2026-07-04): tarea `vigia_donchian` (schtasks, cada 15 min, ruta completa al `pythonw` del venv para evitar fallo silencioso por PATH). `bot/logs/vigia.log` escribe `OK` a cadencia de 15 min. **H2 cerrado**; el hallazgo estaba desactualizado (el vigía ya corría antes de la sesión).
- [x] Ensayo de Fase B arrancado (2026-07-04): montaje hecho, keys demo corregidas (−2014 formato → −1022 firma → OK), conecta a demo con `eq=750`, una sola instancia. Auto-reinicio en `ensayo_faseB/bot/lanzar_ensayo.bat` y tarea `ensayo_faseB_lanzador` (arranque al iniciar sesión, runtime ilimitado, probada). Pendiente: validar el primer trade (entry_price_fill real, fees>0, BTC ~$113).
- [ ] Fila del diario del lab con lo de hoy (plantilla en `research/H-001-canal-donchian/fase_A/checklist_2026-07-03_linea_base.md`).

### DIARIO hasta el cierre de fase (humano + cualquier modelo)
- Revisar la salida de `auditoria.py` (9:05) y mantener el diario al día ("sin incidencias" también se anota).
- Vigilar el ensayo: primer trade con `entry_price_fill` real y `fees > 0` ✓ (validado 07-10: 10/10 con fees, 0 fills sin precio, 0 `precio_aprox`); si aparece `precio_aprox`, investigar. Bugs del ensayo → corregir en `bot/live_bot_faseB.py` del repo + commit (jamás en caliente).
- **paper_real** (tercera instancia, mainnet paper — ver su README y PREREG): heartbeat en su `bot/logs/bot.log`; revisión MENSUAL (equity paper vs buy&hold de la cesta), no diaria. Pendiente del humano: erratum en su PREREG (riesgo 0.1% declarado vs RISK_MAP corriendo).

### DOMINGO 2026-07-05 y siguientes — checklist semanal (Haiku/Sonnet basta)
- Seguir `MONITOREO.md` §Nivel 3 (7 puntos). Informe fechado en `research/H-001-canal-donchian/fase_A/` usando como plantilla el de línea base. Recordar: el lector remoto puede ver archivos vivos con caché de >1h — las verificaciones de frescura se hacen en la máquina, no desde la sesión.

### 2026-07-12 (o cuando se cumplan 10 días + criterios) — CIERRE DE FASE A (Opus recomendado)
1. Correr `python research/H-001-canal-donchian/fase_A/replay_offline.py` (en la máquina del bot).
2. Evaluar los 6 criterios del PREREG con el informe del replay + bot.log + vigia.log + diario. C3 y C6 son manuales.
3. Escribir el informe de cierre en `fase_A/` (aprobada/reprobada por criterio, con evidencia enlazada) y registrar la decisión en la tabla de `docs/VALIDACION/CRITERIOS_FASES.md` y en el diario.
4. Si REPRUEBA: causa raíz, corrección documentada, decidir reinicio de reloj según PREREG. No pasar a B.

### DÍA D (solo si A aprueba) — ARRANQUE DE FASE B (Opus recomendado)
Seguir al pie de la letra el checklist de 9 pasos de `research/H-001-canal-donchian/fase_B/PAQUETE_FASE_B.md` §5: detener el ensayo y aplanar su cuenta; ENMIENDA al PREREG (demo trading, riesgo BTC 0.125% con exp-003, métrica de omisión simulada); copiar `bot/live_bot_faseB.py` (ya depurado por el ensayo) sobre el `live_bot.py` del lab; keys demo en el config.env del lab; `EQUITY_CAP=750`; commit con tag `H001-faseB-frontera`; acta sellada; primer trade auditado end-to-end.

### DURANTE LA FASE B (1 mes) — rutina (Haiku/Sonnet)
- Checklist semanal (ahora con TE ±5%, slippage, y la métrica "señal BTC con notional < $100 = omisión simulada de producción").
- Al cierre: informe final de Fase B contra criterios del PREREG (Opus para el juicio).

### PARALELO, ≤30% del tiempo (regla constitucional) — delegable con receta
- **Banco de Estrategias** (`docs/INVESTIGACION/BANCO/ORQUESTADOR.md`): pipeline F0–F6 que alimenta la cola de hipótesis. Empezar por F0 (protocolo, Opus + humano); una fase por sesión; F1 exige búsqueda web. Regla de oro: su producto son fichas candidatas, jamás validaciones ni números inventados.
- **exp-001 (reproducibilidad):** re-correr `backtest_donchian512.py` y verificar que reproduce `VEREDICTO.md` — misma mecánica de paridad que usó exp-002 (ver su script como plantilla). Informe en `experiments/exp-001/`.
- **Copiar scripts/CSV pequeños del lab** a `research/H-001-canal-donchian/analysis/` (inventario y reglas en `docs/MIGRACION.md` — copias, no movimientos).
- **Data Lake (Etapa 3 del PLAN_TRABAJO):** solo tras cerrar Fase A. Prioridades confirmadas por los hallazgos: funding histórico completo, open interest (lo exige la predicción P3), pares delistados.
- **Sensibilidad 384/512/640 (pre-Fase C):** pre-registrar como exp-00X (umbral: se busca meseta, no optimizar; el PREREG del experimento debe decir qué resultado mataría a H-001) y correr con la plantilla de exp-002.

### DORMIDOS CON DISPARADOR (no construir antes de tiempo — principio 16)
- **Cementerio Científico** (documento vivo: por qué murió cada hipótesis, qué señales se ignoraron, qué se reutilizó): se crea al llegar a ~50 hipótesis en el registro. Hasta entonces, la regla 4 de TEORIA.md y el registro append-only cubren la función.
- **Curador del Conocimiento** (agente, ver backlog en AGENTES.md): primera corrida ~2027-01.
- **Auditoría de Simplicidad** (principio 16): anual, primera 2027-07 — ¿qué eliminaríamos si hubiera que reducir el laboratorio a la mitad? Resultado en ADR.

### ANTES DE FASE C (no urgente, no olvidar)
- Completar los PENDIENTE de Fase C en `RISK_POLICY.md`: criterio de retiro numérico, kill duro vs. blando, stop residente en exchange, checklist de `SECURITY.md` (keys reales con retiros deshabilitados).
- Revisar las señales de retiro conceptual de `HIPOTESIS_ECONOMICA.md` §5 e instrumentar las medibles.

## Qué tarea exige qué modelo

| Tarea | Modelo mínimo |
|---|---|
| Checklists, diario, copias, correr scripts existentes, git | Haiku |
| Informes semanales, fixes menores del bot staged, exp-001 con receta | Sonnet |
| Cierre de Fase A (juicio sobre criterios), arranque de Fase B, análisis de divergencias del replay, nuevos experimentos con prereg, cualquier decisión metodológica | Opus |
| Revisión adversarial de código nuevo, diseño de contratos/arquitectura, hipótesis nuevas (H-002) | El mejor disponible |
