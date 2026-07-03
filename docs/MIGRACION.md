# Inventario y Plan de Migración — donchian512_lab → proyecto-alpha

> Inventario del laboratorio original (`D:\ESTRATEGIA_ALEX\crypto_iid_rango\donchian512_lab`), realizado 2026-07-02 (tarea 1.1 del PLAN_TRABAJO).

## ⚠️ Regla maestra de esta migración

**El bot está corriendo la Fase A desde esa carpeta. NO se mueve, NO se renombra, NO se toca nada de lo que el proceso vivo usa** (`bot/`, `paper/`, `vigia.py`, `auditoria.py`, tareas programadas de Windows) hasta que la Fase A cierre. Toda migración durante la fase es **copia de solo lectura** hacia el repo. Mover el bot a mitad de fase rompería rutas de tareas programadas, el estado y la comparabilidad — y violaría el PREREG.

## Inventario

| Grupo | Contenido | Estado de migración |
|---|---|---|
| **Pre-registros** | README original (prereg 2026-06-24), PREREG_FASE_AB.md, ESPECIFICACION_OPERATIVA.md | ✅ Copiados a `research/H-001-canal-donchian/prereg/` |
| **Veredictos e informes** (17 .md) | VEREDICTO*, RESULTADO*, ROBUSTEZ, FRONTIER, FUNDING*, REGIMEN, ALFABETA, TOP_TRADES, TRANSFERENCIA, INDEPENDENCIA, MATRICES, INFORME_EJECUTIVO | ✅ Copiados a `research/H-001-canal-donchian/report/legacy/` |
| **Scripts de investigación** (~20 .py) | backtest_donchian512, backtest_cesta, grid_frontier, robustez_boot, robustez_attr, alfa_beta, regimen_estudio, funding_apply, matrices, diag_*, test_*, export_trades, top_trades_estructura, analisis_cartera | 🔄 Copiar a `research/H-001-canal-donchian/analysis/` (no urgente; congelados de facto) |
| **Resultados CSV/PNG** | frontier_resultados, cesta_*, trades_*, resultados_donchian512, bootstrap.png, matrices.png | 🔄 Copiar los CSV pequeños a `experiments/`; los grandes (>1 MB) se regeneran por script, no se versionan |
| **Bot vivo** | bot/live_bot.py (15.7 KB), bot_state.json, lanzar_bot.bat, check_sizing.py, logs/bot.log | ⛔ NO tocar hasta cerrar Fase A. Después: migrar a `bot/` del repo adaptándolo a contratos + tests |
| **Observabilidad viva** | paper/ (dashboard.py, eventos.csv, registro_live.csv), vigia.py, auditoria.py, MONITOREO.md, DIARIO_FASE_A.md | ⛔ NO tocar hasta cerrar Fase A. Después: migrar a `dashboard/` |
| **Secretos** | `bot/config.env` contiene `API_KEY` y `API_SECRET` (testnet) | 🔒 **JAMÁS entra al repo.** Añadido `config.env` al .gitignore. Al migrar el bot: variables de entorno según `SECURITY.md` |
| **Docs operativos** | ARRANQUE.md, GUIA_OPERACION.md, DIARIO_FASE_A.md, MONITOREO.md | 🔄 Al cerrar Fase A → base del `RUNBOOK.md` del repo (el runbook real ya existe en la práctica) |

## Hallazgos del inventario (impactan a otros docs — ya aplicados)

1. **La Fase A ya estaba pre-registrada e iniciada** (acta 2026-07-02 03:53 UTC) → enmienda de gobernanza en `CRITERIOS_FASES.md`: el PREREG original gobierna la fase en curso.
2. **H-001 tenía pre-registro real del 2026-06-24** (parámetros congelados antes de correr, predicción registrada y falsada honestamente) → ficha H-001 reescrita: ya no es "pre-registro retroactivo".
3. **El rigor metodológico existente supera lo que la documentación inicial transmitía**: OOS por ventana no vista (2021-23), lockbox, jackknife por trade y por tiempo, bootstrap por bloques, regresión alfa/beta, corte por regímenes, análisis de independencia.
4. Puntos que siguen abiertos y quedan en la ficha: funding real (mayor incógnita), survivorship del universo, sensibilidad 384/512/640 (verificar si se ejecutó), sizing elegido post-hoc sobre la misma muestra (declarado).
5. Discrepancia documentada: backtest inicial a riesgo 0.5%/trade; live a 0.10% — justificado por la frontera de riesgo (0.5% era sobreapuesta) y declarado en la ficha.

## Orden de migración restante

1. (Ahora, sin riesgo) Scripts de investigación y CSV pequeños → `research/H-001-canal-donchian/`.
2. (Al cerrar Fase A) Bot → `bot/` con contratos + tests; observabilidad → `dashboard/`; guías → `RUNBOOK.md`.
3. (Al cerrar Fase A) Redirigir el lanzador y las tareas programadas a las rutas del repo, con acta de corte nueva si aplica.
