# ensembl-database

Query Ensembl genome database REST API for 250+ species.

## Setup

```bash
cd ensembl-database
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/ensembl_query.py --help
```

## Dependencies

- `requests`
