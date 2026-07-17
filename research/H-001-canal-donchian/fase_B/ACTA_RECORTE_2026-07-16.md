# Acta de RE-CORTE de Fase B — 2026-07-16

> El corte del 2026-07-14 (15:13:16 UTC) quedó **comprometido** por un incidente de
> contaminación. Esta acta lo documenta con honestidad, registra la remediación y sella
> un **nuevo inicio limpio** de Fase B. No se ocultan los datos malos: se anulan y se
> explica por qué. La Fase A (APROBADA 6/6 el 2026-07-14) NO se toca — cerró limpia.

## 1. Qué pasó (incidente de contaminación)

Entre el 2026-07-14 y el 2026-07-15, **dos bots operaron simultáneamente la MISMA cuenta demo**:

- el **bot oficial de Fase B** (`donchian512_lab/bot/`, código de frontera, EQUITY_CAP=750), y
- el **ensayo de Fase B** (`proyecto-alpha/ensayo_faseB/bot/`), que debía haberse detenido el día D.

El diario del 07-14 afirmaba *"ensayo detenido y su cuenta aplanada"*. Fue la **intención**, pero
no se cumplió: el ensayo siguió (o se reactivó tras un reinicio del PC) y **compartía las mismas
posiciones**, porque uno abría y el otro las "adoptaba" en su reconciliación.

## 2. Causa raíz (concreta, verificada)

Las API keys del ensayo eran **idénticas** a las del bot oficial de Fase B:

| Instancia | Config | API_KEY |
|---|---|---|
| Fase B oficial | `donchian512_lab/bot/config.env` | `6rw4a9…GpdbT` |
| Ensayo | `ensayo_faseB/bot/config.env` | `6rw4a9…GpdbT` (la misma) |

El comentario del config del ensayo decía *"cuenta DEMO de la fontanería — jamás la del bot del
lab"*, pero **nunca se cambiaron las keys a una segunda cuenta demo**. Resultado: una sola cuenta,
dos bots peleándola → desincronización bot↔exchange (que es criterio de aborto del PREREG).

Síntoma capturado: el estado del ensayo mostraba BTC id 18 a 64754.6 con `fee=0.0` (adoptado),
exactamente la posición que el bot oficial abrió (BTC id 27, 64754.6, fee real 0.031); y el ensayo
había abierto por su cuenta ETH y BCH que el bot oficial no conocía.

Un factor secundario (no causa, sí ruido): cada bot venv generaba un proceso hijo `python` del
sistema; al matar solo el hijo, el padre lo revivía. Se resolvió matando el árbol completo
(`taskkill /T`) y con el guardián nuevo (ver §4).

## 3. Remediación aplicada (2026-07-16)

1. **Máquina esterilizada:** cero procesos python vivos (verificado). H8A retirado; vigía y
   ensayo deshabilitados.
2. **Keys del ensayo neutralizadas:** `ensayo_faseB/bot/config.env` con `API_KEY`/`API_SECRET`
   **vacías** + banner RETIRADO. Aunque alguien lo arranque, no conecta → no puede colisionar.
   Si alguna vez se reactiva, DEBE usar una cuenta demo DISTINTA.
3. **Arranque desplegado (lo que realmente quedó en producción):** la **tarea del Programador
   `faseB_donchian` ejecuta el python del venv DIRECTAMENTE** sobre `live_bot.py` (Execute=python,
   Argument=ruta del script, WorkingDirectory=bot), trigger `AtLogOn`, `MultipleInstances=IgnoreNew`,
   `ExecutionTimeLimit=0`, `RestartCount=5`/1 min. Es el mismo invocador que ya había arrancado sano.
   - *Descartado en el camino, con honestidad:* el guardián por PowerShell/WMI en `lanzar_bot.bat`
     hacía que el `.bat` saliera sin arrancar bajo el Programador; el candado por socket
     (`run_faseB.py`) salía de inmediato (bind bloqueado en la máquina). Ambos se abandonaron por
     frágiles. El `.bat` queda como opción manual, no es la vía de despliegue.
4. **Anti-duplicados efectivo:** `MultipleInstances=IgnoreNew` (el Programador no lanza dos) +
   keys del ensayo neutralizadas (elimina la colisión real). Si en el futuro se quiere un candado
   duro adicional, se añade uno limpio (lockfile) sin bloquear el arranque.

## 4. Datos anulados

Todo lo registrado por el bot oficial de Fase B entre **2026-07-14 15:13:16 UTC** y el nuevo corte
de esta acta queda **ANULADO como evidencia** (cuenta contaminada por doble bot). El estado
`bot_state.json` de ese periodo se respalda como `bot_state.pre_recorte_2026-07-16.json` y NO se usa
para el informe de fase. Los CSV de ese tramo se marcan como contaminados en el informe.

## 5. Nuevo corte limpio (rellenar al arrancar)

- **Fecha/hora del corte (nuevo):** **2026-07-16 15:27:33 UTC** — primer `CICLO` del bot bajo la
  tarea `faseB_donchian` (arranque limpio: demo=True, DRY_RUN=false, eq=750, abiertas=0). Segundo
  ciclo 15:30:07 confirmado sano. El reloj de 1 mes de Fase B cuenta desde aquí.
- **Fase A:** cerró APROBADA 6/6 el 2026-07-14 (`informe_cierre_faseA.md`). Sin cambios.
- **Frontera aplicada:** idéntica a la ENMIENDA 1 (F0 demo trading, B-fix1 fill vía fetch_order,
  B-fix2 fees de fills, B-fix3 riesgo BTC 0.125% por exp-003, B-fix4 omisión simulada, EQUITY_CAP=750,
  DRY_RUN=false). **Sin cambios de lógica, señales ni gestión** respecto al corte del 07-14.
- **Cuenta demo:** aplanada (0 posiciones) por `aplanar_cuenta.py` antes del arranque; estado del
  bot reiniciado limpio.
- **Instancia única:** garantizada por el guardián (§3).
- **Reloj de Fase B:** 1 mes desde este nuevo corte.

## 6. Verificación de arranque (día D bis)

1. [x] Cuenta demo aplanada: `aplanar_cuenta.py` → "Posiciones restantes: 0".
2. [x] Estado viejo respaldado (`bot_state.pre_recorte_2026-07-16.json`); bot arrancó con estado limpio (0 pos, next_id 1).
3. [x] Instancia viva bajo la tarea (`LastTaskResult=267009` corriendo).
4. [x] Primer ciclo limpio: 15:27:33 UTC — demo=True, DRY_RUN=false, eq=750, abiertas=0; 2º ciclo 15:30:07 sano.
5. [ ] Primer trade end-to-end auditado a mano cuando ocurra: fill ≠ None, fee > 0, funding al cierre. **(PENDIENTE)**
6. [x] Sellada la fecha del corte en §5 y fila de reinicio en `DIARIO_FASE_B`.
