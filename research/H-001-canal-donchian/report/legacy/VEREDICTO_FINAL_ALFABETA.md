# Veredicto final — Alfa/Beta, exposicion y lado (cierre del analisis)

## 1) Regresion alfa-beta (vs cesta B&H, retornos diarios)
- beta = 0.006, R2 = 0.000, corr = 0.01  -> DESCORRELACIONADA de beta cripto.
- alpha anual = +11.6%, pero t(alpha) = 0.94 -> NO significativo.
- Sharpe estrategia 0.43 = Sharpe B&H 0.43 (similar, pero sin correlacion).

## 2) Exposicion temporal
- 79.5% del tiempo con >=1 posicion; ~2.63 posiciones a la vez.
- Direccion equilibrada: net long 51% / net short 47% -> explica beta~0.

## 3) Atribucion por lado
| lado | n | sumPnL | exp/trade | win% |
|---|---|---|---|---|
| LONGS | 982 | +11.417$ | +11.6$ | 19.2 |
| SHORTS | 902 | -1.671$ | -1.9$ | 21.5 |
El beneficio sale ENTERO de los longs. Los shorts pierden, pero aportan la
neutralidad (beta~0). Quitarlos = mas retorno pero mas beta/direccional.

## Correcciones de narrativa (registradas)
- "Crisis-alpha / shortea el bear": FALSO (gana long; estudio de regimen).
- "Beta disfrazada": FALSO (beta=0.006).
- "Fuerte-largo": matizado (exposicion equilibrada 51/47).

## Que ES, en una frase
Un trend-following market-neutral, descorrelacionado de cripto, con alfa positivo
PERO no significativo (+11.6%/año, t<1) y extremadamente concentrado (~5 trades,
todo del lado largo). Diversificador plausible, NO edge probado.

## Estado de cierre
- Robustez estadistica: BAJA (jackknife: ~5 trades; t-alpha<1). Por diseno (trend).
- Propiedad valiosa real: descorrelacion (beta~0).
- Incognita unica restante: FUNDING REAL (no medible aqui; en tu maquina).
- Seleccion de activos: DESCARTADA por datos (Spearman -0.90).
- Decision: es de asignacion, no de backtest. Mas backtest sobre esta misma
  muestra ya no aporta informacion, solo riesgo de reinterpretar.

## Si se opera (no es recomendacion, es la unica forma defendible)
Cesta completa equiponderada (sin seleccionar), sizing pequeno (0.10-0.25%),
funding real medido, 1 mes paper SOLO para validar fontaneria, capital minimo,
y aceptando que es un diversificador de baja confianza que puede no pagar en
ventanas largas. Congelar reglas/sizing/universo y NO volver a optimizar.
