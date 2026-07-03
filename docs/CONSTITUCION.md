# Constitución de Proyecto Alpha

Estos principios son innegociables. Cualquier decisión que los contradiga requiere modificar primero este documento mediante un ADR.

## Principios epistemológicos

1. **Los datos tienen prioridad sobre las opiniones.** Ninguna convicción sobrevive a la evidencia en contra.
2. **Toda idea es una hipótesis hasta que el pipeline diga lo contrario.** Nada se llama "estrategia" sin haber completado la validación definida en `INVESTIGACION/PROTOCOLO.md`.
3. **Toda hipótesis debe intentar refutarse antes de aceptarse.** El trabajo del investigador es destruir su propia idea; si no lo consigue, quizá sirva.
4. **Los criterios de decisión se escriben antes de ver los resultados.** Umbrales de aprobación, reprobación y parada se fijan por escrito antes de iniciar cada fase. Un criterio escrito después del resultado no es un criterio: es una excusa.
5. **Los experimentos fallidos se documentan.** El registro de hipótesis conserva las rechazadas con el mismo detalle que las validadas. Un proceso sin cementerio tiene sesgo de supervivencia.
6. **El lockbox se consume una sola vez.** Cada apertura queda registrada con fecha e hipótesis pre-registrada. Un lockbox consultado dos veces deja de ser lockbox.

## Principios operativos

7. **Ninguna estrategia se modifica durante una fase de validación.** Si hay que tocarla, la validación se reinicia desde cero.
8. **Producción e investigación permanecen completamente separadas.** El código en producción está congelado; la investigación no despliega nada directamente.
9. **Toda posición viva está bajo límites de riesgo escritos** (`RISK_POLICY.md`). El kill switch no es opcional ni negociable.
10. **Cada mejora debe beneficiar a la plataforma, no a una estrategia.** Si una mejora solo sirve a una estrategia concreta, es sospechosa de sobreajuste.
11. **Toda decisión importante queda documentada** como ADR, con contexto, alternativas consideradas y consecuencias.
12. **Una sola fuente de verdad por tema.** El estado vive en `ESTADO.md`, los criterios en `CRITERIOS_FASES.md`, las hipótesis en su registro. La duplicación de información es un bug documental.
13. **La IA no toma decisiones de trading.** Ningún agente de IA decide comprar, vender ni asignar capital. La IA investiga, audita, clasifica y documenta; los veredictos los emite el proceso y las decisiones se basan en evidencia cuantitativa. La ejecución es siempre código determinista, nunca un modelo generativo. (Ver `AGENTES.md` y ADR-0002.)

## Regla de asignación de tiempo

Mientras exista una validación operativa abierta (fases A/B/C), la validación es prioritaria: la investigación de nuevas hipótesis recibe como máximo el 30% del tiempo disponible. Esta regla existe porque el desarrollador es uno solo y la investigación es más divertida que esperar datos de un bot congelado.
