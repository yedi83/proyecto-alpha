# Registro de Hipótesis

> Append-only. Toda hipótesis que entra al pipeline se registra aquí y nunca se borra. Las rechazadas valen tanto como las validadas.

| ID | Nombre | Familia | Pre-registro | Etapa actual | Veredicto | Notas |
|---|---|---|---|---|---|---|
| [H-001](hipotesis/H-001-canal-donchian.md) | Canal de Donchian, perp USDT Binance | Trend following | ⚠️ Retroactivo (ver nota) | Fase A (dry run) | ⏳ EN VALIDACIÓN | Primera hipótesis; caso de prueba de la plataforma |

## Nota sobre H-001

H-001 se desarrolló **antes** de que existiera este protocolo, por lo que su pre-registro es retroactivo: la investigación original no acotó el espacio de parámetros por adelantado ni registró el número de configuraciones probadas. Esto se declara abiertamente en su ficha como limitación epistemológica. Las hipótesis H-002 en adelante siguen el protocolo completo desde el inicio.

## Familias de hipótesis previstas

Trend following · Momentum · Carry/Funding · Relative strength · Mean reversion · Regímenes de mercado.

Cada nueva hipótesis toma el siguiente ID disponible (H-002, H-003, …) sin importar su familia.
