# openalex-database

Query and analyze scholarly literature using the OpenAlex database.

## Setup

```bash
cd openalex-database
python3 -m venv .venv && source .venv/bin/activate && pip install openalex_client requests -q
```

## Environment variables

- `NCBI_EMAIL`
- `OPENALEX_EMAIL`

## Usage

```bash
python3 scripts/query_helpers.py --help
```

## Dependencies

- `openalex_client`
- `requests`
