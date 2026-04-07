# reactome-database

Query Reactome REST API for pathway analysis, enrichment, gene-pathway mapping, disease pathways, molecular interactions, expression analysis, for systems biology studies.

## Setup

```bash
cd reactome-database
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/reactome_query.py --help
```

## Dependencies

- `requests`
