# clinvar-database

Query NCBI ClinVar for variant clinical significance.

## Setup

```bash
cd clinvar-database
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/query.py --help
```

## Dependencies

- `requests`
