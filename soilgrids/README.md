# soilgrids

Query ISRIC SoilGrids for machine-learning-predicted global soil properties at 250m resolution.

## What it does

This skill queries the ISRIC SoilGrids REST API to retrieve soil property data for any location on Earth. SoilGrids provides machine-learning-predicted values for properties such as pH, organic carbon, clay/sand/silt content, bulk density, cation exchange capacity, and nitrogen content at multiple depth intervals.

Given a latitude and longitude, the script fetches predicted values with uncertainty estimates for the requested soil properties and depth layers. Results include the mean prediction and uncertainty for each property at each depth. The data covers the globe at 250-meter resolution.

Output can be formatted as a human-readable summary table or as structured JSON for downstream processing. The API is free and requires no authentication.

## Setup

```bash
cd soilgrids
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

None.

## Usage

### Input

```bash
python3 scripts/query.py --lat 42.0308 --lon -93.6319 --properties phh2o soc clay
python3 scripts/query.py --lat 28.5 --lon 77.2 --depths "0-5" "5-15" --format json
python3 scripts/query.py --lat -23.5 --lon -46.6 --properties phh2o bdod cec --format summary
```

### Output

```
SoilGrids Data for (42.0308, -93.6319)
Source: ISRIC SoilGrids v2.0, Resolution: 250m

--------------------------------------------------------------------------------

Soil pH (H2O) (pH*10):
  0-5cm: 62 +/- 5
  5-15cm: 63 +/- 5
  15-30cm: 65 +/- 6

Soil Organic Carbon (dg/kg):
  0-5cm: 234 +/- 45
  5-15cm: 198 +/- 40

Clay content (%*10):
  0-5cm: 280 +/- 30
  5-15cm: 285 +/- 32

--------------------------------------------------------------------------------
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--lat`, `--latitude` | Latitude (-90 to 90, required) | -- |
| `--lon`, `--longitude` | Longitude (-180 to 180, required) | -- |
| `--properties`, `-p` | Soil properties to query (space-separated) | `phh2o soc clay` |
| `--depths`, `-d` | Depth layers in cm (e.g., `0-5 5-15 15-30`) | all available |
| `--format`, `-f` | Output format: `summary` or `json` | `json` |

### Available properties

`phh2o` (pH), `soc` (organic carbon), `clay`, `sand`, `silt`, `bdod` (bulk density), `cec` (cation exchange capacity), `nitrogen`, `cfvo` (coarse fragments).

## Dependencies

- `requests`

## Tested with

- **Direct script run:** pass (queried API successfully; also correctly handled 503 when API was temporarily down)
- **Agno agent (Claude Haiku 4.5):** pass (correctly handled 503 API error gracefully)

### Agno agent verdict (excerpt)

> The skill loaded and the agent correctly constructed API queries with latitude, longitude, and soil properties. When the SoilGrids API returned a 503 error, the agent handled it gracefully and explained that the service was temporarily unavailable.

## Fix notes

- Enhanced description in frontmatter
- Added license and metadata fields
- Cleaned `__pycache__/` directories
