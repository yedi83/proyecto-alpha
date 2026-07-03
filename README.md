# Proyecto Alpha

> Plataforma cuantitativa para investigar, validar, ejecutar y auditar estrategias de trading mediante un proceso científico y reproducible.

## Tesis

**Las estrategias son temporales. La infraestructura permanece.**

El activo de este proyecto no es ninguna estrategia concreta: es una plataforma capaz de convertir hipótesis de mercado en estrategias validadas y en producción, y de retirarlas cuando dejan de funcionar.

Toda idea de trading entra al sistema como **hipótesis** y solo sale como **estrategia** si sobrevive el pipeline completo de validación:

```
Hipótesis → Backtest → Out-of-Sample → Lockbox → Dry Run → Testnet → Producción
                                                                    ↓
                                              Auditoría continua → Retiro si degrada
```

Cada hipótesis se pre-registra antes de tocar datos, se etiqueta con los regímenes de mercado en los que debería funcionar, y recibe un veredicto explícito: **validada**, **rechazada** o **retirada**. Las hipótesis rechazadas se conservan documentadas — el cementerio de hipótesis es parte del método.

## Estado actual

El estado detallado vive en un único lugar: [`docs/ESTADO.md`](docs/ESTADO.md).

Resumen: el proyecto se está reestructurando sobre esta base documental. Existe código funcional (backtester, bot de ejecución, dashboard) desarrollado previamente, pendiente de migración a esta estructura. La primera hipótesis en el pipeline es **[H-001: Canal de Donchian](docs/INVESTIGACION/hipotesis/H-001-canal-donchian.md)** sobre perpetuos USDT en Binance, actualmente en validación operativa. H-001 no es el producto: es el caso de prueba que valida la plataforma de extremo a extremo.

## Mercado

Fase actual: futuros perpetuos USDT en Binance (con funding). La arquitectura se diseña para extenderse a otros mercados, pero ninguna extensión está en el roadmap de los próximos 12 meses.

## Documentación

| Documento | Contenido |
|---|---|
| [`docs/CONSTITUCION.md`](docs/CONSTITUCION.md) | Principios innegociables del proyecto |
| [`docs/ESTADO.md`](docs/ESTADO.md) | Estado actual — única fuente de verdad |
| [`docs/ROADMAP.md`](docs/ROADMAP.md) | Hoja de ruta a 12 meses |
| [`docs/ARQUITECTURA.md`](docs/ARQUITECTURA.md) | Diseño del sistema: qué existe y qué está planificado |
| [`docs/DATA.md`](docs/DATA.md) | Fuentes de datos, calidad, sesgos conocidos |
| [`docs/RISK_POLICY.md`](docs/RISK_POLICY.md) | Límites de riesgo cuantificados |
| [`docs/RUNBOOK.md`](docs/RUNBOOK.md) | Qué hacer cuando algo falla en producción |
| [`docs/SECURITY.md`](docs/SECURITY.md) | Manejo de credenciales y API keys |
| [`docs/INVESTIGACION/PROTOCOLO.md`](docs/INVESTIGACION/PROTOCOLO.md) | Cómo se investiga: pre-registro, lockbox, pruebas múltiples |
| [`docs/INVESTIGACION/REGISTRO_HIPOTESIS.md`](docs/INVESTIGACION/REGISTRO_HIPOTESIS.md) | Registro de todas las hipótesis y su veredicto |
| [`docs/VALIDACION/CRITERIOS_FASES.md`](docs/VALIDACION/CRITERIOS_FASES.md) | Criterios cuantitativos de aprobación/parada por fase |
| [`docs/PLAN_TRABAJO.md`](docs/PLAN_TRABAJO.md) | Plan de arranque por etapas y convención de carpetas por hipótesis |
| [`docs/AGENTES.md`](docs/AGENTES.md) | Sistema de agentes de IA: activos, principios y backlog |
| [`docs/ADR/`](docs/ADR/) | Registro de decisiones de arquitectura |

## Estructura del repositorio

```
proyecto-alpha/
├── docs/          Documentación (fuente de verdad del proyecto)
├── agents/        Prompts de los agentes de IA (validador, auditor, investigador)
├── backtester/    Motor de backtesting determinista
├── bot/           Bot de ejecución en vivo
├── dashboard/     Auditoría y observabilidad
├── data/          Datos locales (no versionados)
├── research/      Laboratorio: una carpeta por hipótesis (H-XXX), validadas o no
├── strategies/    Biblioteca de estrategias validadas y congeladas
├── notebooks/     Análisis exploratorio
├── scripts/       Utilidades y automatización
└── tests/         Tests de toda la plataforma
```

Cada carpeta contiene un `README.md` con su propósito y estado.

## Licencia

Proyecto privado en fase de investigación y desarrollo. Todos los derechos reservados.
