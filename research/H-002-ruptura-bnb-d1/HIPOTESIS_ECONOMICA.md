# H-002 — Hipótesis Económica

> **Declaración de honestidad:** este documento se escribe DESPUÉS de conocer el banco (veredicto 2026-07-14). Explicar lo ya visto es barato; el compromiso real son las **predicciones falsables (§4)** y las **señales de retiro (§5)**. Si esas fallan, la hipótesis falla, aunque la estrategia haya ganado.

## 1. La ineficiencia propuesta

**En los majors cripto, las tendencias alcistas de mediano plazo (semanas a meses), confirmadas por estructura (precio por encima de su media de 200 días), persisten más de lo que la ruptura inicial de 20 días incorpora.** Mismo motor conductual que H-001 —subreacción/rebaño en un mercado de flujo minorista + amplificación por apalancamiento en perpetuos— pero **filtrado al régimen alcista** y **cosechado con objetivo fijo 2R**.

Dos diferencias de diseño con H-001, y su porqué:

1. **Filtro de régimen SMA200 (solo largos en tendencia estructural).** En cripto las subidas son tendencias largas que una ruptura diaria monta bien; las caídas son crashes rápidos + rango, donde la ruptura hace *whipsaw*. El SMA200 **excluye ese terreno hostil** — de ahí viene la reducción de drawdown, no de mejores entradas.
2. **Objetivo fijo 2R (no trailing).** Recoge el **tramo medio** del movimiento sin depender de la cola gigante. Por eso el perfil de pago es **distinto al de H-001**: win rate ~49%, top-5 trades = 44% del neto (top-1 solo 9%) — **NO cuelga de la cola** (H-001 era 115% en top-5). Es un pago mucho mejor repartido.

## 2. ¿Quién está al otro lado y por qué pierde?

- **Los que hacen fade de la ruptura** (esperan el retorno al rango): en la fracción de veces que la tendencia es real, financian el tramo.
- **Los que capitulan en los crashes que la estrategia NO toca:** bajo SMA200 la estrategia está fuera; su dolor no es el nuestro.
- **El holder pasivo, en términos de riesgo:** come el **−76% de drawdown** que la estrategia esquiva (**−5.5%**). Aquí la ventaja **no es "ganar más"** —en BNB, aguantar el pump gana ~100× más— sino **participar de la tendencia con una fracción del drawdown, repartido en varios majors**.

## 3. Tensiones declaradas (lo que el banco mostró y hay que explicar honestamente)

- **T1: en BNB historia completa, la beta dimensionada la aplasta.** El valor de H-002 **no** es batir a aguantar en el activo de un pump irrepetible (el 40× de BNB 2017-21 no se puede comprar hoy). Es **reducción de drawdown + mejor retorno ajustado por riesgo OOS y multi-activo** (T2, T5). Juzgarla contra "aguantar el pump" es un test defectuoso: confunde "batir un outlier" con "tener edge".
- **Long-only ⇒ beta POSITIVA, no neutral.** A diferencia de H-001 (beta≈0, cortos como seguro), H-002 **está expuesta a la dirección del mercado**. Su "edge" es **timing de beta / gestión de drawdown**, NO alfa market-neutral. Es una tensión honesta, no un defecto oculto: cambia el benchmark correcto (retorno ajustado por riesgo y vs. beta dimensionada) y la fuente de riesgo (direccional, no descorrelacionada).
- **ETH fue el más fuerte, no las alts pequeñas.** El mecanismo generalizó fuerte en BTC y ETH (T2). Contrasta con la P1 de H-001 (alfa en alts, no en BTC). Se declara y se vigila (§4 P4).

## 4. Predicciones falsables (el compromiso)

| # | Predicción | Cómo se verifica | Estado |
|---|---|---|---|
| P1 | La ventaja de drawdown viene de estar **FLAT bajo SMA200** (crashes/rango), no de mejores entradas | Descomponer retorno y DD por régimen (sobre/bajo SMA200) sobre los datos existentes | ⏳ Verificable ya |
| P2 | El edge ajustado por riesgo **persiste fuera de muestra** | Ya consistente (T5: Sharpe 1.08 vs 0.26 de aguantar); seguir midiéndolo forward | ⏳ Paper_real lo mide |
| P3 | Al ser **long-only en tendencias alcistas**, la exposición a funding positivo es máxima → el edge neto se **comprime cuando el funding es crónicamente extremo** (misma incógnita que H-001 P4, pero MÁS expuesta) | Funding real por trade; cruzar con el centinela de funding | ⏳ Requiere datos (Data Lake) |
| P4 | A medida que los majors se institucionalizan, la **persistencia de rupturas decae** | Sharpe/edge rolling por activo | ⏳ Continuo |
| P5 | El **perfil de pago sigue bien repartido** (win ~49%, top-5 ≈ 44%, sin dependencia de cola). Si deriva a dependencia de cola o el win rate colapsa, el mecanismo cambió → sospechar régimen o bug, no celebrar | Distribución de PnL por trade forward vs. la del banco | ⏳ Continuo |

## 5. Señales de retiro conceptual (qué vigilar ANTES de que el drawdown lo diga)

1. **Muerte de la persistencia:** si las tendencias multi-día colapsan de forma sostenida, el filtro sangrará por whipsaw antes de que el equity lo grite.
2. **Institucionalización de los majors:** compresión estructural de spreads/participación profesional → decaimiento estilo BTC (P4).
3. **Funding crónicamente extremo:** más grave aquí que en H-001 — al ser **siempre larga en tendencia alcista**, si el funding se come el lado largo en los regímenes donde debería pagar, la implementación en perpetuos muere aunque el mecanismo de señal siga vivo.
4. **Divergencia del perfil forward vs. el banco** (win rate, reparto del neto, drawdown) sin causa identificada → el mecanismo o la implementación cambió.

## 6. Qué NO afirma esta hipótesis

- **No afirma edge probado** (n=57 trades → confianza **moderada**, no prueba).
- **No afirma ser market-neutral:** es **long-only, beta positiva**; su ventaja es drawdown / riesgo-ajustado, no alfa descorrelacionada.
- **No afirma batir a la beta dimensionada** en el activo de un pump único (T1).
- **No incluye la variante trailing** (más parámetros, autoflag "dudosa-favorable"): solo la **base**.
- No sustituye la validación forward en curso (`paper_real/`).

## 7. Nota meta (prueba de fuego de la plataforma)

El banco de H-002 **reutilizó el motor de backtest del investigador VERBATIM** y corrió un suite pre-registrado completo (T1-T5) en ~1 jornada (2026-07-14), frente al arco largo que costó H-001. Es evidencia —de las primeras— a favor de la tesis central del proyecto: *si la plataforma es el activo, la segunda hipótesis cuesta una fracción de la primera*. Se registra como observación, no como prueba (n=1 hipótesis).
