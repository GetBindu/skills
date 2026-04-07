# pubmed-database

Direct REST API access to PubMed.

## Setup

```bash
cd pubmed-database
python3 -m venv .venv && source .venv/bin/activate && pip install requests xml -q
```

## Environment variables

- `NCBI_API_KEY`
- `NCBI_EMAIL`

## Usage

```bash
python3 scripts/query.py --help
```

## Dependencies

- `requests`
- `xml`
