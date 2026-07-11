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
14. **Separación entre generación de conocimiento y producción de evidencia.** El Banco genera hipótesis y protocolos; el Pipeline produce la evidencia; el Registro conserva el historial íntegro (versionado, append-only); el Árbitro (A-04) vigila el cumplimiento del método; el Investigador Principal — humano — resuelve los conflictos metodológicos mediante ADR. Ningún rol invade a otro: quien genera no valida, quien valida no registra su propio veredicto sin traza, quien arbitra no diseña. Mientras esta separación se mantenga, el sistema resiste el sesgo de confirmación y la tentación de ajustar el método al resultado deseado. (Añadido 2026-07-10.)
15. **Toda decisión metodológica relevante se registra como ADR** con las cinco preguntas de la plantilla — incluida la quinta, obligatoria: qué evidencia futura justificaría revisarla. Las decisiones, como las hipótesis, deben ser falsables. (Añadido 2026-07-10; extiende el principio 11.)
16. **Costo de Gobernanza.** Toda regla, agente, documento o fase nuevos debe responder ANTES de nacer: ¿qué error concreto evita? ¿cuánto cuesta mantenerlo? ¿qué pieza existente podría eliminar o absorber? Los componentes del laboratorio — agentes, reglas, ADRs, esta Constitución, la Teoría — son **hipótesis de diseño**: sujetas a revisión, simplificación o eliminación si dejan de pagar su coste. Mecanismo de aplicación: **Auditoría de Simplicidad anual** (primera: 2027-07) con una sola pregunta — *¿qué eliminaríamos si tuviéramos que reducir el laboratorio a la mitad?* — cuyo resultado se registra como ADR. Los sistemas científicos mueren más por burocracia que por error; la madurez de esta arquitectura se medirá por aprender más con menos complejidad, no por crecer. (Añadido 2026-07-10.)

## Regla de asignación de tiempo

Mientras exista una validación operativa abierta (fases A/B/C), la validación es prioritaria: la investigación de nuevas hipótesis recibe como máximo el 30% del tiempo disponible. Esta regla existe porque el desarrollador es uno solo y la investigación es más divertida que esperar datos de un bot congelado.
