# Paper-real — trading sobre precios REALES de mainnet, SIN dinero

> Forward test del **edge** sobre precios reales. Las fases A/B corren sobre testnet (falso); esto es lo primero sobre precios de verdad. Pre-registro: `PREREG.md`. Reglas congeladas del bot de frontera (512/256, cesta 5, riesgo 0.1%). **Cero riesgo:** `DRY_RUN=true` + sin API keys = no puede colocar órdenes.

## Qué mide (y qué NO)

- Mide: que la estrategia genere y capture sus señales sobre precios reales going forward. Sobre todo, que cuando llegue una tendencia grande, la capture limpio.
- NO mide: fricción de ejecución real (slippage/fills reales) — eso es Fase C (capital mínimo). Aquí los fills son simulados.
- Es **lento**: ~3 trades clave/año. Sembrar y esperar; revisar mensual. La pregunta correcta (tras la corrección de régimen): **¿aporta algo MÁS que estar largo de cripto?** → trackear vs buy&hold.

## Montaje (una vez) — PowerShell

```
cd "D:\PIC\Proyecto Investigación cuantitativa PIC\proyecto-alpha\research\H-001-canal-donchian\paper_real"
New-Item -ItemType Directory -Force -Path bot, paper | Out-Null
Copy-Item "..\..\..\bot\live_bot_faseB.py" bot\live_bot.py
Copy-Item config.example.env bot\config.env
```

(el `config.example.env` ya trae mainnet + DRY + sin keys; NO hay que editar nada)

## Verificar que arranca (una corrida)

```
& "D:\ESTRATEGIA_ALEX\crypto_iid_rango\.venv\Scripts\python.exe" bot\live_bot.py
```

Debe imprimir `BOT Donchian512 FASE-B | exchange=binance demo=False DRY_RUN=True` y un `CICLO ... eq=10000.00`. **`demo=False` = mainnet real.** Corta con Ctrl+C tras ver el primer CICLO.

## Dejarlo corriendo (tarea al iniciar sesión) — PowerShell ADMIN

```
$b="D:\PIC\Proyecto Investigación cuantitativa PIC\proyecto-alpha\research\H-001-canal-donchian\paper_real\lanzar_paper.bat"
Register-ScheduledTask -TaskName "paper_real_donchian" -Force -Action (New-ScheduledTaskAction -Execute $b -WorkingDirectory (Split-Path $b)) -Trigger (New-ScheduledTaskTrigger -AtLogOn) -Settings (New-ScheduledTaskSettingsSet -ExecutionTimeLimit ([TimeSpan]::Zero) -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries)
```

## Monitoreo

- Heartbeat: `bot\logs\bot.log` (`CICLO` cada 15 min).
- Trades cerrados: `paper\registro_live.csv`. Eventos: `paper\eventos.csv`.
- Mensual: comparar la curva de equity paper contra buy&hold de la cesta (¿aporta más que beta, con menos drawdown?).

## Gobernanza (añadido 2026-07-10, sesión de documentación)

1. **Estatus:** instancia de comparación/forward — **NO es evidencia de Fase A ni B** (esas se rigen por su PREREG propio). Sí es insumo formal de la decisión de Fase C: (a) tasa de velas atrasadas del feed real (medida al 07-10: ~0.9/día/símbolo vs ~1.5 testnet y ~2.2 demo), (b) divergencia señal-a-señal entre feeds, (c) captura de señales going-forward según su propio PREREG.
2. **Git:** `paper/` (eventos y registro) SÍ se versiona — es la serie de comparación, append-only y pequeña. `bot/` está fuera de git (config, estado, logs).
3. **ERRATUM pendiente del investigador (detectado 2026-07-10):** el PREREG dice "riesgo 0.1%/trade" uniforme, pero el código copiado es el bot de frontera con RISK_MAP (BTC 0.125%, exp-003). Las señales no dependen del sizing, así que la captura de señal no se contamina; el sizing de BTC en el registro difiere de lo pre-registrado. Añadir línea de erratum fechada al PREREG.md (la escribe el humano, con la decisión: aceptar el mapa o reiniciar con 0.1% uniforme).
4. Los bugs que revele se corrigen en `bot/live_bot_faseB.py` del repo con commit, nunca en caliente aquí.
5. Se retira solo por decisión documentada; su horizonte natural es acompañar B y C como testigo del feed real.
