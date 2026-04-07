# bgs-production

Query BGS World Mineral Statistics for production, imports, and exports by commodity, country, and year

## Setup

```bash
cd bgs-production
python3 -m venv .venv && source .venv/bin/activate && pip install asyncio cmm_data -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/bgs_query.py --help
```

## Dependencies

- `asyncio`
- `cmm_data`
