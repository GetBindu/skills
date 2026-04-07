# fao-stat

Query global agricultural statistics from UN FAO covering 245 countries and territories

## Setup

```bash
cd fao-stat
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
