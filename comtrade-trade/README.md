# comtrade-trade

Query UN Comtrade bilateral trade flows (USD, kg) for critical minerals by HS code, country, and year

## Setup

```bash
cd comtrade-trade
python3 -m venv .venv && source .venv/bin/activate && pip install asyncio uncomtrade_mcp -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/comtrade_query.py --help
```

## Dependencies

- `asyncio`
- `uncomtrade_mcp`
