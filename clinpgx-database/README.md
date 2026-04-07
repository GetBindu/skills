# clinpgx-database

Access ClinPGx pharmacogenomics data (successor to PharmGKB).

## Setup

```bash
cd clinpgx-database
python3 -m venv .venv && source .venv/bin/activate && pip install pandas requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/query_clinpgx.py --help
```

## Dependencies

- `pandas`
- `requests`
