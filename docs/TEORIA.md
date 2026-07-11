# Teoría del Laboratorio

> Documento VIVO. Responde una sola pregunta: **¿qué creemos hoy sobre cómo funcionan los mercados que operamos?** Solo mecanismos — no estrategias, no parámetros, no indicadores. Fundado 2026-07-10 por decisión del Investigador Principal; se puebla al ritmo de la evidencia, no del calendario.

## Reglas del documento

1. **Cada creencia cita su evidencia** (IDs de hipótesis, experimentos o informes del registro). Una creencia sin linaje no entra.
2. **Nunca se escribe una verdad; se escribe el estado actual de la evidencia.** Formato de toda entrada: *"la evidencia del laboratorio es [consistente / parcialmente consistente / inconsistente] con la hipótesis de que [mecanismo], en [condiciones]"* + confianza subjetiva declarada **en bandas** (alta ≳70% · media 40-70% · baja ≲40% — bandas, no porcentajes de dos cifras: la precisión falsa es dogma disfrazado) + última revisión + basado en [IDs] + refutaciones [IDs].
3. **Estados abreviados** (mapean a las bandas): ✓ evidencia consistente, confianza alta · △ parcial, confianza media/baja · ✗ inconsistente o falsada · ⊘ sin investigar. La v0.1 usa la abreviatura; desde v0.2 las entradas nuevas llevan el formato completo del punto 2.
4. **Las hipótesis rechazadas alimentan este documento con el mismo peso que las validadas.** "¿Qué aprendimos al rechazar?" es pregunta obligatoria de cada cierre.
5. **No es normativo:** nadie opera desde este documento. Toda idea derivada de una creencia ✓ sigue entrando al pipeline como hipótesis completa. La Teoría orienta la búsqueda; no sustituye la prueba.
6. Se versiona (v0.1, v0.2, …) y nunca se edita destructivamente: cada versión nueva declara qué creencia cambió, por qué evidencia, y qué versión reemplaza. Las degradaciones (✓→△, △→✗) son tan publicables como los ascensos.
7. Actualización: tras cada veredicto de hipótesis, cada cierre de Fase C, y revisión trimestral aunque no haya cambios ("sin cambios" también se registra).
8. La taxonomía de mecanismos es la del árbol del Banco (F2): persistencia, sobre-reacción, prima de riesgo/carry, liquidez, microestructura, convexidad.

---

## Versión 0.1 — 2026-07-10

*Sembrada únicamente con lo que la investigación de H-001 ya produjo. Casi todo está, honestamente, en △ — el laboratorio tiene una semana de vida formal.*

### Persistencia (tendencia)

- △ **Existen tendencias multi-día en perpetuos cripto explotables por ruptura de canal, netas de costes.** Evidencia: H-001 in-sample + ventana no vista 2021-23 + lockbox; alfa +11.6%/año pero t=0.94 (no significativa); ~5 trades efectivos cargan todo el neto. Plausible, no probado. [VEREDICTO, ROBUSTEZ, ALFABETA]
- △ **La persistencia es mayor donde el flujo es menos institucional:** alfa en alts (ETH/SOL/DOGE), no en BTC. Consistente con subreacción minorista; predicción P1 de la hipótesis económica, verificable en más pares/tiempo. [VEREDICTO, HIPOTESIS_ECONOMICA P1-P2]
- ✓ **Los contribuyentes de una cesta de tendencia ROTAN por régimen; seleccionar activos por rendimiento pasado anti-predice** (Spearman -0.90). De las creencias mejor establecidas del laboratorio. [ROBUSTEZ, VEREDICTO_CONSOLIDADO]
- ✗ **"El edge de tendencia en cripto es crisis-alpha que cobra shorteando bears":** falsado por atribución — el beneficio sale entero de los longs; los shorts son prima de neutralidad (beta≈0), no motor. Corrección de narrativa registrada. [ALFABETA, REGIMEN_VEREDICTO]

### Estructura de retornos del estilo

- ✓ **El retorno del trend following aquí es convexidad, no consistencia:** win rate 19-27%, top-5 trades >100% del neto, sangrado prolongado entre pagos. No es bug del sistema: es la naturaleza del estilo, y dimensiona el sizing y la paciencia exigible. [ROBUSTEZ, TOP_TRADES]
- ✓ **El valor real frente a buy&hold no es Sharpe (igual, ~0.42) sino drawdown** (-18/-32% vs -88%) **más descorrelación** (beta 0.006). Diversificador, no generador. [VEREDICTO_CONSOLIDADO, ALFABETA]
- ✗ **El vol-targeting como mejora general del Sharpe:** el lift (0.42→0.58) resultó artefacto del bear 2022; en régimen reciente, plano. Amplifica convexidad de crisis, no crea edge. [FRONTIER_VEREDICTO]

### Prima de riesgo / carry (funding)

- ⊘ **Funding como fuente de carry cobrable:** sin investigar como estrategia (candidata natural H-002 vía Banco). Lo único establecido: como COSTE, el funding real es la mayor incógnita de magnitud del laboratorio — puede llevar el edge de tendencia 2024-26 a ≈0. [FUNDING_REAL_VEREDICTO, DATA.md]

### Microestructura / datos

- ✓ **Los feeds difieren de forma material:** velas atrasadas ~0.9/día/símbolo en mainnet vs ~1.5 testnet y ~2.2 demo; señales distintas entre feeds sobre el mismo período. Toda validación debe declarar su feed. [resumen_instancias_2026-07-10]
- △ **Las cascadas de liquidación amplifican tendencias** (mecanismo 2 de la hipótesis económica): predicción P3, requiere open interest del Data Lake para verificarse. [HIPOTESIS_ECONOMICA]

### Sobre-reacción / reversión · Liquidez · Convexidad de opciones

- ⊘ Sin investigar. En alcance futuro del Banco.

---

*Próxima revisión programada: al cierre de la Fase A de H-001 (¿qué aprendimos, apruebe o repruebe?).*
