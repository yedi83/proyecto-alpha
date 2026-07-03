# Protocolo de Investigación

> Cómo una idea se convierte (o no) en estrategia. Este protocolo es obligatorio para toda hipótesis, sin excepciones. H-001 incluida.

## Ciclo de vida de una hipótesis

```
IDEA → PRE-REGISTRO → BACKTEST → OOS → LOCKBOX → DRY RUN → TESTNET → PRODUCCIÓN
                          │        │       │         │         │          │
                          └────────┴───────┴─────────┴─────────┴──────────┘
                                    reprobación en cualquier punto
                                              ↓
                                          RECHAZADA (se documenta y se conserva)
```

Estados posibles: `EN VALIDACIÓN` · `VALIDADA` · `RECHAZADA` · `EN PRODUCCIÓN` · `RETIRADA` (estaba en producción y degradó).

## 1. Pre-registro (antes de tocar datos)

Toda hipótesis se registra en `hipotesis/H-XXX-nombre.md` **antes** de correr el primer backtest, con:

- **Hipótesis económica:** por qué debería existir esta ineficiencia y quién está al otro lado perdiendo dinero.
- **Regímenes esperados:** en qué contextos de mercado debería funcionar y en cuáles no. Esto se escribe antes, no después de ver dónde funcionó.
- **Universo y período de datos** que se usarán.
- **Espacio de parámetros** que se explorará, acotado de antemano.
- **Métricas de éxito y umbrales de rechazo**, con números.
- **Predicción falsable:** qué resultado obligaría a rechazar la hipótesis.

## 2. Backtest

- Motor determinista, con funding, comisiones y position sizing reales.
- **Todo experimento se registra**, incluido el fallido. El número total de configuraciones probadas es un dato obligatorio del informe.

## 3. Corrección por pruebas múltiples

Si se probaron N configuraciones, la métrica reportada debe corregirse (Deflated Sharpe Ratio o equivalente). Un "backtest satisfactorio" sin declarar N no significa nada.

## 4. Out-of-Sample

- La partición IS/OOS se define en el pre-registro, antes de ver los datos.
- El OOS se evalúa contra los umbrales pre-registrados, no contra la impresión visual de la curva.

## 5. Lockbox

- Segmento de datos definido en el pre-registro y **nunca consultado durante la investigación**.
- **Se abre una sola vez.** La apertura se registra: fecha, hipótesis exacta evaluada, resultado.
- Si la hipótesis se modifica después de abrir el lockbox, ese lockbox está quemado para esa familia de hipótesis: se necesita un período nuevo (normalmente, esperar a que el mercado lo genere).

## 6. Validación operativa (Fases A/B/C)

Definida en `../VALIDACION/CRITERIOS_FASES.md`. Los criterios cuantitativos de cada fase se escriben antes de iniciarla.

## 7. Producción y retiro

- La estrategia entra congelada. No se modifica: si necesita cambios, vuelve al inicio del pipeline como nueva hipótesis.
- El criterio de retiro (cuándo declararla muerta) se escribe **antes** de entrar a producción.
- La auditoría continua compara PnL live vs. modelo; el tracking error fuera de umbral dispara revisión.

## Reglas anti-autoengaño

1. Ningún parámetro se elige "porque se ve mejor la curva". Si no está en el espacio pre-registrado, no existe.
2. Los regímenes donde funciona una estrategia se predicen antes y se verifican después — nunca se descubren mirando dónde ganó.
3. Está prohibido re-correr una validación fallida con datos ligeramente distintos "para confirmar".
4. El registro de hipótesis (`REGISTRO_HIPOTESIS.md`) es append-only: nada se borra, todo se fecha.
