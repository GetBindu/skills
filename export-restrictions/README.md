# export-restrictions

Query OECD export restriction policies on critical raw materials with corpus-search enrichment

## Setup

```bash
cd export-restrictions
python3 -m venv .venv && source .venv/bin/activate && pip install cmm_data -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/restrictions_query.py --help
```

## Dependencies

- `cmm_data`
