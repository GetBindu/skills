---
name: soilgrids
description: Query ISRIC SoilGrids for ML-predicted global soil properties at 250m resolution — clay/sand/silt content, organic carbon, pH, bulk density, CEC, nitrogen, and soil water content at 6 depth layers (0-200cm). Returns values with uncertainty bounds. Use for precision agriculture, environmental modeling, land suitability assessment, or carbon stock estimation.
license: MIT license
metadata:
    skill-author: K-Dense Inc.
    source: https://rest.isric.org
---

# SoilGrids Global Soil Data

Access machine learning-predicted global soil properties at 250m resolution from ISRIC.

## Overview

SoilGrids provides global soil property predictions using ML models trained on 240,000+ soil profiles. Query any GPS coordinate worldwide to get soil pH, organic carbon, texture, nutrients, and more at multiple depth layers.

## Usage

### Query soil properties for a location:
```bash
python3 {baseDir}/scripts/query.py --lat 42.0308 --lon -93.6319 --properties phh2o soc clay
```

### Query specific depth layers:
```bash
python3 {baseDir}/scripts/query.py --lat 28.5 --lon 77.2 --depths "0-5" "5-15" "15-30"
```

### Get all properties:
```bash
python3 {baseDir}/scripts/query.py --lat -23.5 --lon -46.6 --properties phh2o soc clay sand silt bdod cec --format json
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--lat` | Latitude (-90 to 90) | Required |
| `--lon` | Longitude (-180 to 180) | Required |
| `--properties` | Soil properties to query | phh2o soc clay |
| `--depths` | Depth layers in cm | All layers |
| `--format` | Output format: summary, json | json |

## Available Properties

- **phh2o** - Soil pH (H2O)
- **soc** - Soil Organic Carbon (g/kg)
- **clay** - Clay content (%)
- **sand** - Sand content (%)
- **silt** - Silt content (%)
- **bdod** - Bulk density (kg/dm³)
- **cec** - Cation Exchange Capacity (cmol/kg)
- **nitrogen** - Nitrogen content (g/kg)
- **cfvo** - Coarse fragments (%)

## Depth Layers

Standard depth layers (cm):
- 0-5, 5-15, 15-30, 30-60, 60-100, 100-200

## Examples

### Soil contradiction finding (MVP use case):
```bash
# Query SoilGrids for Iowa cornfield
python3 {baseDir}/scripts/query.py --lat 42.0308 --lon -93.6319 --properties phh2o om clay

# Compare against SSURGO and OpenLandMap for same location
# SoilGrids: pH 6.8 ± 0.3 (ML-predicted, 2020)
# SSURGO: pH 6.1 (Ground survey, 2009)
# Difference: 0.7 pH units → changes lime recommendation by 2 tons/acre
```

### Precision agriculture validation:
```bash
python3 {baseDir}/scripts/query.py --lat 36.1 --lon -95.9 --properties phh2o soc clay nitrogen
```

## Use Cases

**Soil Data Contradiction Finding**: Compare SoilGrids ML predictions against ground surveys (SSURGO, farmer soil tests)

**Global Coverage**: Get soil data for regions where ground surveys don't exist

**Variable-Rate Application**: Validate precision agriculture maps against multiple soil data sources

## Notes

- Free API access, no key required
- 250m spatial resolution
- ML-predicted values, not ground-measured
- Includes uncertainty estimates
- Based on data through 2018
- Version 2.0 released in 2020
- Predictions often differ from ground surveys (perfect for contradiction finding)
