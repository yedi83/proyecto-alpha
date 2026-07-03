# Arquitectura

> Distingue explícitamente entre lo que **existe** y lo que está **planificado**. Ver estado por componente en `ESTADO.md`.

## Diagrama

```
            ┌──────────────────────────────────────────────────┐
            │  OBSERVABILIDAD / AUDITORÍA  (capa transversal)   │
            └──────────────────────────────────────────────────┘
            ┌──────────────────────────────────────────────────┐
            │  GESTIÓN DE RIESGO  (transversal, dos niveles:    │
            │  por estrategia y por portafolio)                 │
            └──────────────────────────────────────────────────┘

 Data Lake ──► QA de datos ──┬─► Motor de Investigación ─► Biblioteca de Estrategias
 [plan]        [plan]        │        [existe*]                  │
     ▲                       └─► Motor de Régimen [plan]         ▼
     │                                  │            Asignación de Capital [plan]
     │                                  └──────────────────┐     │
     │                                                     ▼     ▼
     │                     Capa de Abstracción de Exchange ◄── Motor de Ejecución
     │                              [plan]                       [existe*]
     │                                                            │
     └──────── feedback: resultados live → investigación ◄────────┘
               + Reconciliación contable [plan]
```

\* "existe" = código funcional desarrollado previamente, pendiente de migración a este repo.

## Decisiones estructurales

1. **Observabilidad y riesgo son capas transversales, no etapas de un pipeline.** Observan y limitan a todos los componentes.
2. **QA de datos es un componente explícito.** Ningún dato entra a investigación o ejecución sin pasar validación (huecos, duplicados, alineación temporal, pares delistados).
3. **La asignación de capital es un componente de primer orden**, separado de la selección por régimen. Decide cuánto capital recibe cada estrategia y el riesgo agregado del portafolio. Se construye cuando exista la segunda estrategia validada.
4. **El motor de ejecución no conoce exchanges concretos**: opera contra una capa de abstracción. Hoy esto no se cumple (bot acoplado a Binance); es deuda registrada.
5. **Existe un bucle de retroalimentación**: los resultados live (tracking error, slippage, PnL vs. modelo) alimentan la investigación. La producción genera datos; no se modifica a sí misma.
6. **Riesgo en dos niveles.** Cada estrategia tiene límites propios; el portafolio tiene límites globales que dominan. El kill switch global apaga todo.

## Responsabilidades por componente

| Componente | Hace | No hace |
|---|---|---|
| Data Lake | Recolecta y almacena datos crudos versionados | Transformar o interpretar |
| QA de datos | Valida integridad, alineación, cobertura | Decidir qué datos usar en investigación |
| Motor de Investigación | Backtest, OOS, lockbox, estadísticas | Desplegar nada a producción |
| Biblioteca de Estrategias | Estrategias validadas, congeladas y versionadas | Contener hipótesis sin validar |
| Motor de Régimen | Clasificar contexto de mercado (descriptivo) | Ejecutar u ordenar trades |
| Asignación de Capital | Pesos por estrategia, riesgo agregado | Generar señales |
| Motor de Ejecución | Traducir señales en órdenes, gestionar posiciones | Decidir qué estrategia opera |
| Observabilidad | Medir, alertar, auditar todo lo anterior | Corregir automáticamente |

Los cambios a esta arquitectura se registran en `ADR/`.
