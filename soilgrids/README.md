# soilgrids

Query ISRIC SoilGrids for ML-predicted global soil properties at 250m resolution. Clay, sand, silt, organic carbon, pH, bulk density, CEC, nitrogen, soil water content at 6 depth layers (0-200cm).

## Setup

```bash
pip install requests
```

## Env vars

None. Free public API.

## Usage

```bash
python3 scripts/query.py --lat 52.0 --lon 5.0 --properties clay --format summary
```

## Output

```
SoilGrids Data for (52.0, 5.0)
Source: ISRIC SoilGrids v2.0, Resolution: 250m

Clay content (g/kg):
  0-5cm: 475 ± 19
  5-15cm: 488 ± 18
  15-30cm: 480 ± 19
  30-60cm: 458 ± 23
  60-100cm: 461 ± 20
  100-200cm: 471 ± 20
```

## Dependencies

`requests`

## Tested with

- **Direct run (clay at 52°N, 5°E):** ✅ Real ISRIC data returned with uncertainty bounds
- **Agno (dry-run):** ✅
