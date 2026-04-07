# landsat

Query Landsat satellite imagery with 50+ year archive from NASA/USGS

## Setup

```bash
cd landsat
python3 -m venv .venv && source .venv/bin/activate && pip install landsatxplore -q
```

## Environment variables

- `USGS_PASSWORD`
- `USGS_USER`

## Usage

```bash
python3 scripts/query.py --help
```

## Dependencies

- `landsatxplore`
