# Estado del Proyecto

> Única fuente de verdad del estado. Última actualización: 2026-07-01.

## Fase actual

Reestructuración del proyecto sobre esta base documental + validación operativa de H-001 (Canal de Donchian).

## Componentes

| Componente | Estado | Notas |
|---|---|---|
| Motor de backtesting | 🔄 Existe — pendiente de migración | Código funcional en repo/carpeta anterior. Migrar a `backtester/` con tests. |
| Bot de ejecución | 🔄 Existe — pendiente de migración | Migrar a `bot/`. Documentar en RUNBOOK.md durante la migración. |
| Dashboard de auditoría | 🔄 Existe — pendiente de migración | Migrar a `dashboard/`. |
| Data Lake | 📋 Planificado | Ver ROADMAP. Prerrequisito de toda investigación futura. |
| QA / validación de datos | 📋 Planificado | Incluye tratamiento de pares delistados. |
| Motor de régimen | 📋 Planificado | Solo investigación descriptiva en los próximos 12 meses. |
| Asignación de capital / portafolio | 📋 Planificado | Necesario a partir de la segunda estrategia validada. |
| Capa de abstracción de exchange | 📋 Planificado | Hoy el bot está acoplado a Binance. |

Leyenda: ✅ operativo y verificado en este repo · 🔄 existe fuera de este repo, pendiente de migración · 📋 planificado, no existe.

**Regla:** ningún componente se marca ✅ sin enlace a su evidencia (tests en verde, informe de validación, o log auditado).

## Hipótesis en el pipeline

| ID | Nombre | Etapa | Veredicto |
|---|---|---|---|
| [H-001](INVESTIGACION/hipotesis/H-001-canal-donchian.md) | Canal de Donchian (perp USDT Binance) | Validación operativa — Fase A (dry run) | ⏳ En validación |

## Deuda documental abierta

- [ ] Completar los números de `RISK_POLICY.md` (hoy tiene campos PENDIENTE).
- [ ] Completar los criterios cuantitativos de `VALIDACION/CRITERIOS_FASES.md` **antes de evaluar la Fase A**.
- [ ] Escribir el informe honesto de H-001: datos usados, cómo se eligieron los parámetros, cuántas variantes se probaron.
- [ ] Documentar fuentes y sesgos de datos en `DATA.md`.
- [ ] Migrar código existente con sus tests.
