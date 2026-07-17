# exp-008 — DATOS (artefacto congelado)

- **Dataset:** `datalake/funding/{BTC,ETH,SOL,BCH,DOGE}_funding.csv` — funding histórico Binance mainnet 2021-07-01 → 2026-07-17, recolectado 2026-07-17 por `recolector_funding.py`.
- **Dictamen A-02: APTO** (2026-07-17, `datalake/funding/DICTAMEN_A02.md`) — SOL 4h/2h en episodio FTX legítimo; extremos = eventos reales (FTX, The Merge, crash 2021-09); malla UTC limpia, sin lookahead ni doble aplicación.
- **SHA-256 congelados (el APTO cubre EXACTAMENTE estos bytes; el script verifica antes de correr y aborta si no coinciden):**

| archivo | sha256 |
|---|---|
| BTC_funding.csv | 801133db36c95488723264569af1a6ac05c01e885d80eaa145f5f3f0f86dda7a |
| ETH_funding.csv | 76c6a5187e42008157dbe5eb3954f3a1ee28c9244176449254ad10231d3b61a2 |
| SOL_funding.csv | 590d760f9e8c57f737c91df2adbbec482e2760438e8837a1f99ca6901b13c8f7 |
| BCH_funding.csv | 98239ab8b16f17f79e1494f763db6e11fc1ed07bc8ac653f29235f8c71564c87 |
| DOGE_funding.csv | 1fd25d55144784514ee6d2cc28627b3717887224dfba7b1122856236395f3ad8 |

- Velas: cache `_15m_60m` del lab (mismo origen que exp-002/003/004, paridad verificada).
- Deuda de proceso registrada (crítica de A-02, aceptada): el recolector debe emitir hash y metadatos de intervalo de fábrica — mejora para la próxima pieza del datalake, no se re-toca este artefacto.
