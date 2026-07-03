# Ensayo General de Fase B — REGLAS

> Bot de frontera corriendo con órdenes reales en la cuenta DEMO de la fontanería, en paralelo a la Fase A y **totalmente aislado de ella**.

## Qué ES y qué NO es

- ES un banco de pruebas de integración del código de frontera (fetch_order, fees de fills, demo trading, riesgo por símbolo, reconciliación tras reinicios).
- **NO es la Fase B.** Nada de lo que produzca cuenta como evidencia de fase. La Fase B oficial arranca solo tras el cierre aprobado de la Fase A, con su acta (PAQUETE_FASE_B §4-5).
- **NO toca nada del lab** (`donchian512_lab`): ni sus CSVs, ni su estado, ni su cuenta. Escribe únicamente dentro de esta carpeta (`bot/`, `paper/` locales — ignorados por git).

## Compromisos (escritos antes de arrancar)

1. Al iniciar la Fase B oficial, este ensayo se DETIENE y su cuenta demo se aplana (o se usa una cuenta demo nueva para B).
2. Los datos del ensayo no se citan en ningún informe de fase; solo sus BUGS (que van al PAQUETE como fixes de frontera adicionales, con fecha).
3. Si el ensayo exige cambiar `bot/live_bot_faseB.py` (el staged del repo), el cambio se hace en el repo con commit — así el día D se aplica la versión ya depurada.

## Montaje (una vez)

```powershell
cd "D:\PIC\Proyecto Investigación cuantitativa PIC\proyecto-alpha\ensayo_faseB"
mkdir bot 2>$null; mkdir paper 2>$null
copy ..\bot\live_bot_faseB.py bot\live_bot.py
copy config.example.env bot\config.env    # editar: keys DEMO de la fontanería
python bot\live_bot.py                    # o crear un .bat lanzador como el del lab
```

`config.env` del ensayo: `DRY_RUN=false`, `EXCHANGE_TESTNET=true`, `EQUITY_CAP=750` (así el sizing refleja el capital previsto aunque la demo tenga ~$5,000 virtuales — y ejercita el min_notional de BTC de verdad).

## Qué observar (los objetivos del ensayo)

- Primer trade end-to-end: `entry_price_fill` ≠ None y ≠ aproximado, `fees` > 0 (de fills), funding al cierre.
- Comportamiento del min_notional con EQUITY_CAP=750: BTC debe entrar con ~$113 de notional (o omitirse con evento si el ATR sube >13%).
- Reconciliación: matar el proceso con posición abierta y relanzar → debe adoptarla sin duplicar.
- Eventos `orden/precio_aprox`: si aparecen, el fallback de precio está activándose — investigar antes del día D.
- Si el balance demo se puede ajustar/restablecer (responde la duda del checklist §5 del paquete).
