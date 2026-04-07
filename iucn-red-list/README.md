# iucn-red-list

Query species conservation status from IUCN Red List of Threatened Species

## Setup

```bash
cd iucn-red-list
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

- `IUCN_API_KEY`

## Usage

```bash
python3 scripts/query.py --help
```

## Dependencies

- `requests`
