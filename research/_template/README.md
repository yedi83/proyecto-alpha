# H-XXX — Nombre de la hipótesis

- **Ficha (pre-registro y veredicto):** ../../docs/INVESTIGACION/hipotesis/H-XXX-nombre.md
- **Estado:** EN VALIDACIÓN | VALIDADA | RECHAZADA

## Contenido

- `config/` — espacio de parámetros pre-registrado (se congela al crear la hipótesis)
- `experiments/` — append-only: exp-001/, exp-002/… con config exacta + resultados + fecha. Nunca se borra ni se sobrescribe.
- `analysis/` — notebooks y scripts exploratorios (no son evidencia)
- `report/` — informe final con números y veredicto

## Cómo se creó esta carpeta

1. Copiar `research/_template/` → `research/H-XXX-nombre/`
2. Crear la ficha en `docs/INVESTIGACION/hipotesis/`
3. Añadir fila en `docs/INVESTIGACION/REGISTRO_HIPOTESIS.md`
