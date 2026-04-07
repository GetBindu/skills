# modis

Query daily global vegetation indices and land surface data from NASA MODIS

## Setup

```bash
cd modis
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
