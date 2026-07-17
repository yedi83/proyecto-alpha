# SECURITY.md

## Objetivo

Establecer los controles mínimos de seguridad para cualquier despliegue en producción (Fase C, capital real). Complementa `RISK_POLICY.md` (límites de riesgo) y el `PREREG_FASE_C` (criterios de fase). Este checklist debe estar **completo y verificado ANTES del día 1 de Fase C**.

> Estado: redactado 2026-07-16. Ver §11 (Estado de implementación) para qué controles ya ejecuta el bot congelado y cuáles son requisitos a construir/validar antes de C — para que este documento no liste protección que el código no hace.

---

## 1. API Keys

### Producción
- API Key **exclusiva para trading** (una por propósito).
- Permisos:
  - ✅ Spot/Futures Trading
  - ❌ Withdrawals (retiros)
  - ❌ Universal Transfer (si no es indispensable)
  - ❌ Gestión de usuarios
- Rotación periódica de credenciales, y rotación inmediata ante cualquier sospecha de exposición.

### Desarrollo
- API Keys completamente separadas por entorno (demo/testnet y producción **nunca** comparten credenciales).
- Nunca reutilizar credenciales de producción.

---

## 2. Restricción de IP

Toda API Key de producción debe estar restringida por **lista blanca (IP Whitelist)**. No se permiten API Keys abiertas a Internet.

---

## 3. Gestión de secretos

**Nunca** almacenar API Keys, Secret Keys, tokens ni passwords en: Git, GitHub, README ni código fuente.

Utilizar: variables de entorno, gestor de secretos, o archivo `.env` **fuera del repositorio**. `.env` debe estar en `.gitignore`, y se verifica antes de cada commit.

**Repositorio (heredado del control previo, se mantiene):**
- El repositorio es privado. Antes de cualquier cambio de visibilidad, **auditar el historial completo** en busca de secretos.
- Si una credencial llega a un commit (aunque el repo sea privado): **se revoca inmediatamente en el exchange y LUEGO se limpia el historial. Revocar primero, limpiar después.**

---

## 4. Principio de mínimo privilegio

Cada componente recibe solo los permisos estrictamente necesarios:
- Bot de ejecución → Trading únicamente.
- Dashboard → Solo lectura.
- Backtester → Sin acceso a APIs privadas.

---

## 5. Registro y auditoría

Registrar (con timestamp, logs inmutables): inicio y cierre del sistema, creación de órdenes, cancelaciones, errores de API, reconexiones, **activación del Kill Switch**, y **activación del Disyuntor Técnico** (§10).

---

## 6. Validaciones antes de enviar órdenes

Verificar, y si **cualquiera** falla NO enviar la orden:
- API disponible.
- Hora sincronizada.
- Símbolo habilitado.
- Balance suficiente.
- Tamaño mínimo permitido.
- Riesgo máximo por operación (RISK_POLICY).
- Kill Switch inactivo.
- Disyuntor Técnico inactivo (§10).

---

## 7. Recuperación

Ante reinicio del sistema, antes de continuar operando:
- Reconciliar posiciones abiertas.
- Reconciliar órdenes pendientes.
- Verificar balances.
- Recalcular el estado interno.

**Nunca asumir que el estado en memoria es correcto.**

---

## 8. Despliegue

Antes de operar con dinero real: backtest aprobado, walk-forward aprobado, paper trading aprobado, checklist de seguridad completado, y todas las pruebas críticas en verde. **Solo entonces** habilitar producción.

---

## 9. Prohibición de intervención manual no registrada

Si un operador modifica una posición directamente desde el exchange (cerrarla, reducirla, mover órdenes), el bot debe **detectarlo, registrarlo, y reconciliar su estado antes de seguir operando**. Ninguna divergencia entre el estado local y el del exchange se ignora ni se sobrescribe en silencio: se registra como evento y se reconcilia. (Es la lección directa del incidente de contaminación 2026-07-14/15.)

---

## 10. Parada por anomalía operacional (Disyuntor Técnico)

Además del drawdown (que gobierna la **suspensión de estrategia**, RISK_POLICY / PREREG_FASE_C §3), el sistema debe **detenerse por síntomas de fallo técnico** — es el "disyuntor catastrófico técnico, no de precio" de PREREG_FASE_C §4. Dispara ante:

- Varios **rechazos consecutivos de órdenes** (propuesta: ≥ 3 seguidos).
- **Diferencia persistente** entre la posición local y la del exchange (propuesta: mismatch que sobrevive a > 2 ciclos de reconciliación).
- **Pérdida prolongada de datos de mercado** (propuesta: sin vela actualizada por > 2 velas esperadas, o > 30 min).
- **Latencia o deslizamiento por encima del umbral** definido (propuesta: usar el p95 de slippage/latencia medido en Fase B como techo).

Al dispararse: cerrar de forma segura o congelar la operativa, registrar el evento (§5), y **exigir intervención + reconciliación manual antes de reanudar**. Los umbrales marcados "propuesta" se confirman al sellar el PREREG_FASE_C.

---

## 11. Estado de implementación (honesto — qué hace hoy el bot vs. qué falta)

Para que este documento no sea teatro: distinción entre controles **ya operativos** en el bot congelado y **requisitos a construir + validar antes de C**.

**Ya operativo en el bot (`live_bot_faseB.py`):**
- Reconciliación de posiciones **al arranque** (§7) + estado persistente (`bot_state.json`).
- Kill switch **blando** diario (§5, `DAILY_LOSS_KILL`).
- Secretos fuera de git (§3); validaciones de tamaño/riesgo/`halted`/max concurrentes antes de abrir (§6, parcial).

**A construir y VALIDAR antes de Fase C (no van en el bot de Fase B, que está congelado):**
- §9 detección de intervención manual **durante** la operación (hoy la reconciliación es solo al arranque, no continua).
- §10 Disyuntor Técnico (contador de rechazos, mismatch persistente, gap de datos, umbral latencia/slippage).
- §1-2 configuración de la **cuenta Binance de producción**: keys sin retiros + IP whitelist (se setea en el exchange, no en código).

**Decisión abierta (análoga al stop en exchange, PREREG_FASE_C §5):** implementar §9/§10 antes de C implica un **bot nuevo que hay que validar** (no se puede tocar el de Fase B en curso). Alternativa: diferir §9/§10 a C-002 y correr C con los controles actuales + vigilancia manual reforzada. **Se decide al sellar el PREREG_FASE_C**, con ADR; no se asume aquí.

---

## 12. Referencias

- `RISK_POLICY.md` — límites de riesgo y kill switch blando.
- `research/H-001-canal-donchian/fase_C/PREREG_FASE_C_BORRADOR.md` — criterios de Fase C (capital, suspensión-y-revisión a −27%, kill, stop).
- `HIPOTESIS_ECONOMICA.md §5` — señales de retiro conceptual.
