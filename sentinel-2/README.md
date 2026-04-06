# sentinel-2

Query Sentinel-2 multispectral satellite imagery at 10m resolution from ESA Copernicus.

## What it does

Searches the Copernicus Open Access Hub for Sentinel-2 scenes by bounding box, date range, and cloud cover percentage. Returns scene metadata including product IDs, acquisition dates, cloud cover, and download links. Useful for agricultural monitoring, land use mapping, vegetation indices (NDVI), and environmental change detection.

## Setup

```bash
cd sentinel-2
python3 -m venv .venv && source .venv/bin/activate && pip install sentinelsat -q
```

## Environment variables

| Variable | Description |
|----------|-------------|
| `COPERNICUS_USER` | Copernicus Open Access Hub username |
| `COPERNICUS_PASSWORD` | Copernicus Open Access Hub password |

Register at https://scihub.copernicus.eu/dhus/#/self-registration

## Usage

```bash
python3 scripts/query.py --north 42.1 --south 42.0 --east -93.5 --west -93.7 --start 2023-06-01 --end 2023-09-30
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--north` | North latitude | (required) |
| `--south` | South latitude | (required) |
| `--east` | East longitude | (required) |
| `--west` | West longitude | (required) |
| `--start` | Start date (YYYY-MM-DD) | (required) |
| `--end` | End date (YYYY-MM-DD) | (required) |
| `--cloud` | Max cloud cover % | `30` |
| `--format` | Output format (summary/json) | `summary` |

## Dependencies

- `sentinelsat`

## Tested with

- **Direct script run:** pass (graceful error when sentinelsat not installed)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict

> Agent loaded the skill and described Sentinel-2 capabilities, bounding box queries, and cloud cover filtering.

## Fix notes

- Enhanced description with use cases and platform details
- Added license, metadata, and requires-env fields
