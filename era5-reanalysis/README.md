# era5-reanalysis

Query global atmospheric reanalysis data from ECMWF/Copernicus ERA5

## Setup

```bash
cd era5-reanalysis
python3 -m venv .venv && source .venv/bin/activate && pip install cdsapi -q
```

## Environment variables

- `CDS_API_KEY`

## Usage

```bash
python3 scripts/query.py --help
```

## Dependencies

- `cdsapi`
