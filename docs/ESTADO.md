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
| [H-001](INVESTIGACION/hipotesis/H-001-canal-donchian.md) | Canal de Donchian 512 (perp USDT) | Fase A dry run — iniciada 2026-07-02 con acta, gobernada por su PREREG (mín. 10 días) | ⏳ En validación |

## Deuda documental abierta

- [ ] Completar los números de `RISK_POLICY.md` (hoy tiene campos PENDIENTE).
- [x] Criterios de Fase A: resuelto por enmienda de gobernanza — la fase en curso se rige por el PREREG original del lab (ver `CRITERIOS_FASES.md`).
- [x] Informe honesto de H-001: las 5 preguntas respondidas con evidencia en la ficha (2026-07-02, tras inventario del lab).
- [x] Inventario del código existente: `docs/MIGRACION.md`.
- [ ] Completar `DATA.md` con lo aprendido del inventario (fuente de velas, funding modelado vs. real).
- [ ] Copiar scripts de investigación y CSV pequeños a `research/H-001-canal-donchian/` (sin tocar el sistema vivo).
- [ ] Completar los números de `RISK_POLICY.md` antes de Fase C.
- [ ] Migrar bot y observabilidad al repo **solo al cerrar la Fase A** (regla maestra de MIGRACION.md).
- [ ] Verificar si el test de sensibilidad 384/512/640 se ejecutó; si no, decidir si se hace antes de Fase C.
