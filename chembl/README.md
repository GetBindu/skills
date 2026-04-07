# chembl

Small-molecule drug lookup by exact drug name or ChEMBL ID.

## Setup

```bash
cd chembl
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/chembl_search.py --help
```

## Dependencies

- `requests`
