# eu-pesticide-database

Query EU pesticide approval status and Maximum Residue Limits from European Commission

## Setup

```bash
cd eu-pesticide-database
python3 -m venv .venv && source .venv/bin/activate && pip install bs4 requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/query.py --help
```

## Dependencies

- `bs4`
- `requests`
