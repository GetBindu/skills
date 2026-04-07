# supply-chain-analysis

Compute supply chain risk metrics for critical minerals — HHI concentration, net import reliance, top-3 share, and trend

## Setup

```bash
cd supply-chain-analysis
python3 -m venv .venv && source .venv/bin/activate && pip install asyncio cmm_data -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/supply_chain_metrics.py --help
```

## Dependencies

- `asyncio`
- `cmm_data`
