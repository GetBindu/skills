# noaa-climate-data

Query historical weather and climate data from NOAA Climate Data Online

## Setup

```bash
cd noaa-climate-data
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

- `NOAA_API_KEY`

## Usage

```bash
python3 scripts/query.py --help
```

## Dependencies

- `requests`
