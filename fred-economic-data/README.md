# fred-economic-data

Query FRED (Federal Reserve Economic Data) API for 800,000+ economic time series from 100+ sources.

## Setup

```bash
cd fred-economic-data
python3 -m venv .venv && source .venv/bin/activate && pip install fred_query requests -q
```

## Environment variables

- `FRED_API_KEY`

## Usage

```bash
python3 scripts/fred_examples.py --help
```

## Dependencies

- `fred_query`
- `requests`
