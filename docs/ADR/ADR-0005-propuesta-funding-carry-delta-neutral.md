# ADR-0005 — Propuesta: Funding carry delta-neutral (mecanismo candidato)

- **Fecha:** 2026-07-16
- **Estado:** Propuesta (en cola por moratoria ADR-0004; revisión en el F0 del C-002 o al cumplirse el disparador de §5, lo que ocurra primero)
- **Alcance:** Metodología / Investigación (mecanismo candidato, NO desplegado)

> Se registra la idea sin decidir, según ADR-0004. No es una aprobación ni un compromiso de recursos.

## 1. ¿Qué problema intentábamos resolver?

Existe un mecanismo candidato — **funding carry delta-neutral** (long spot + short perp del mismo notional, que cobra el funding sin exposición direccional) — con código de exploración (`crypto-scanner/backtest_funding_carry*.py`) y un **centinela de régimen ya operando** (`funding_regime_sentinel.py`, corrida diaria, paper, sin dinero). Surgió la pregunta de diseño: ¿trabajarlo **individual** (por símbolo, donde haya funding rico) o **condicionado a régimen** (desplegar según el APR medio del mercado)? Hay que dejar la idea anotada y evaluada sin violar la moratoria.

## 2. ¿Qué se evaluó (datos actuales)?

- **Diseño:** delta-neutral — la dirección del precio está cubierta; se cobra la prima estructural del funding (los longs apalancados pagan). Persistencia del funding lag-1 ≈ 0.62.
- **Train (2024-11 → 2025-05, 199 días):** regla ganadora `u_in=0.0002 / u_out=5e-05` → mediana **+10.9%/año neto**; portafolio **+4.45%/año, maxDD −0.28%, Sharpe ≈ 14.79**, ~19 símbolos activos. Top en majors creíbles (BNB +15%, SOL +14.8%, DOGE +18%); colas altas en alts finos (ONDO +26%, WLD, SEI, NEIRO, PNUT) invertidos poco tiempo.
- **Individual vs régimen:** al ser delta-neutral, el "estallido direccional" del carry (el largo masificado que se desploma) está **cubierto por el hedge**. Conclusión provisional: se puede **cosechar individual** donde el funding esté rico y **escalar con el régimen**; el régimen sirve a la **defensiva** (seguridad de margen/basis de la pata corta), no como luz verde ofensiva.

## 3. ¿Por qué se aplaza (no se decide ahora)?

1. **Los números son cota superior, no edge real.** El propio código lista sus trampas: asume **basis (tracking error spot-perp) = 0** ("optimista"), **ignora costo de capital del lado spot y préstamos**, y no modela **margen/liquidación de la pata corta** ni slippage. Un Sharpe ≈ 15 y maxDD 0.28% son la firma de lo que el backtest ignora, no de una prima robusta.
2. **Holdout NO corrido.** Ambos resultados guardados dicen "solo train"; la validación OOS (jun25-may26) no se ha ejecutado. Por la constitución del laboratorio, no es evidencia hasta pasar el holdout una vez con la regla congelada.
3. **Datos insuficientes del régimen que importa.** El centinela solo ha observado **FRÍO** (APR medio máx. +4.34% en el período registrado); el **retorno Y el riesgo** del carry viven en TEMPLADO/CALIENTE, aún no observados. Decidir hoy sería adivinar.
4. **Moratoria ADR-0004.** Toda idea nueva durante el C-001 → ADR pendiente → C-002.

## 4. ¿Qué consecuencias aceptamos?

La idea espera semanas o meses. El **centinela sigue registrando** a diario (construye el track record del régimen caliente sin arriesgar dinero) — es la acción barata correcta. Nada se despliega. La cola de ADR pendientes crece (diseño funcionando, no fallando).

## 5. ¿Qué evidencia futura podría justificar revisarla?

**Obligatoria y específica.** Se reabre cuando ocurra **lo primero** de:

- **(a) Datos del régimen no observado:** el centinela registra un régimen **TEMPLADO o superior** (APR medio majors **> 5.5%**) sostenido **≥ 10 días consecutivos**, aportando por fin track record en papel del régimen donde vive el edge y el riesgo; o
- **(b) Cierre del C-001:** se levanta la moratoria y la propuesta entra al F0 del C-002.

**Al reabrir**, el paso honesto es pre-registrar y correr el **holdout UNA vez** con la regla congelada, esta vez añadiendo: haircut de **basis**, **costo de capital/préstamo**, y modelo de **slippage/liquidación de la pata corta**. Juzgar por la **cola (Calmar / maxDD real)**, no por el carry medio. Umbral de interés declarado: que un neto delta-neutral **realista** (p. ej. +4–6%/año) sobreviva OOS; si el +10.9% se evapora al meter las fricciones, se archiva.
