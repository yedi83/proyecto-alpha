# QA/A-02 v3 NO CONFORME — Bifurcación y decisión del IP

> **Fecha: 2026-07-29 · Registro de decisión (gobernanza).** Documenta la convergencia de tres pases adversariales, el hallazgo-raíz, y la decisión del IP que reorienta el alcance de A-02. Los dictámenes verbatim viven en `QA_A02_DICTAMEN_ADVERSARIAL.md` (append-only).

## 1. La convergencia (el hallazgo real)

Tres versiones del contrato, tres NO CONFORME, **la misma raíz**:

| Versión | Enfoque | Cayó por |
|---|---|---|
| v1 | 10 controles + censo externo | 4 circularidades: cada control se validaba contra su propio insumo |
| v2 | Axioma anti-circularidad + anclas + censo de 2 rutas | La independencia de **proveniencia** no existe: todo deriva de Binance; el axioma se contradice |
| v3 | Censo verificado + cota de survivorship + 4 estados | La **cota de survivorship es autodestructiva** (−100% sin liquidez ⇒ no operable ⇒ PnL≈0 ⇒ el edge "sobrevive" trivial para los símbolos que importan); y solo cubre ausentes-**conocidos** |

**Raíz común:** no existe un ancla externa a Binance en datos gratuitos. Toda cadena (censo → raw → fuentes del censo) termina en Binance. El único ancla externa real —capturas point-in-time tipo Tardis— es de pago y quedaba opcional. **La propiedad "survivorship controlado" no es construible con datos gratuitos**, por mucho que se rediseñe el contrato.

## 2. La bifurcación (opciones)

- **A — Comprar el ancla (Tardis).** Rompe el lazo cerrado. Cuesta dinero.
- **B — Aceptar que el survivorship no se controla con datos gratis, solo se declara.** A-02 certifica lo alcanzable (integridad, calidad, reproducibilidad) + una **declaración** de survivorship con evidencia y límites; deja de prometer control.
- **C — Acotar hipótesis** a donde el survivorship no muerde; las dependientes de la cola ausente no se promueven con datos gratuitos.

## 3. Decisión del IP (2026-07-29)

**B — con C como disciplina inmediata de cartera; A documentada como expansión futura, no requisito fantasma.**

Razonamiento del IP (resumido):
- **A** es técnicamente impecable pero **prematuro**: comprar certeza para un carril de hipótesis de cola ancha que aún no es central. Se reactiva si en ~3 meses ese carril se vuelve central.
- **C** es sabia operativamente y se aplica **ya** a la cartera (tail-dependientes no se promueven con datos gratis), pero **sola** deja la puerta a colar un "casi controlado" barato. Va como disciplina de dimensionamiento, no como respuesta a la certificación.
- **B rompe el patrón:** es el equivalente honesto a la primera lección del carry (asumir el cimiento real). A-02 se vuelve sólido sobre su **verdadero perímetro** e **inmune** al ataque que disolvió las tres versiones — porque **no afirma lo que no puede cumplir sin Tardis**.

## 4. Qué cambia para A-02 (recorte de alcance)

- **Sale del alcance de A-02:** la propiedad *"survivorship controlado / cota completa de survivorship"*.
- **Entra / se consolida:** integridad del dato, calidad, reproducibilidad, **wash-trading gateado**, y una **DECLARACIÓN de survivorship** basada en censo + raw de binance.vision, con las **limitaciones documentadas explícitamente** (ausentes de raw *y* censo indetectables; sesgo de momento-de-consulta; delistados-antes-de-la-captura invisibles sin fuente point-in-time externa).
- **Regla de promoción (C):** cualquier hipótesis que requiera una **cota completa** de survivorship **no se certifica con este contrato** y debe basarse en una fuente point-in-time externa (Tardis). Las que **no** dependen de la cola ausente se promueven con A-02 CONFORME sobre lo alcanzable.
- **Tardis:** opción documentada de expansión futura (Opción A), no requisito presente.

## 5. Gobernanza

v1/v2/v3 quedan archivadas (contrato + dictámenes, append-only). **v4 es el recorte a B** y debe pasar su propio pase adversarial — pero ahora el ataque válido es *"¿la declaración es honesta y los controles alcanzables están realmente gateados?"*, no *"¿está controlado el survivorship?"* (que v4 ya no afirma).
