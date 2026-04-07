---
name: ssurgo
description: Query detailed US soil survey data from USDA NRCS with ground-measured soil properties
---
# USDA SSURGO Soil Survey

Access detailed, ground-measured soil data from the USDA Natural Resources Conservation Service soil survey.

## Overview

SSURGO (Soil Survey Geographic Database) is the most detailed soil survey in the United States. Unlike ML-predicted data, SSURGO is based on ground surveys by soil scientists, laboratory analysis, and field observations.

## Usage

### Query soil data for a location:
```bash
python3 {baseDir}/scripts/query.py --lat 42.0308 --lon -93.6319 --properties ph om clay
```

### Get detailed soil profile:
```bash
python3 {baseDir}/scripts/query.py --lat 36.1 --lon -95.9 --format json
```

### Query specific properties:
```bash
python3 {baseDir}/scripts/query.py --lat 39.7 --lon -104.9 --properties ph om clay sand awc
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--lat` | Latitude (US locations only) | Required |
| `--lon` | Longitude (US locations only) | Required |
| `--properties` | Soil properties to query | ph om clay |
| `--format` | Output format: summary, json | json |

## Available Properties

- **ph** - Soil pH
- **om** - Organic matter (%)
- **clay** - Clay content (%)
- **sand** - Sand content (%)
- **awc** - Available water capacity

## Examples

### Soil contradiction finding (MVP use case):
```bash
# Query SSURGO for Iowa field
python3 {baseDir}/scripts/query.py --lat 42.0308 --lon -93.6319 --properties ph om clay

# Compare against SoilGrids and OpenLandMap
# SSURGO: pH 6.1 (Ground survey, 2009)
# SoilGrids: pH 6.8 ± 0.3 (ML-predicted, 2020)
# Difference: 0.7 pH units → $15,000-50,000 impact on lime application
```

### Precision agriculture validation:
```bash
python3 {baseDir}/scripts/query.py --lat 40.5 --lon -88.2 --properties ph om clay sand
```

## Use Cases

**Ground Truth Validation**: Compare SSURGO ground surveys against ML-predicted soil data (SoilGrids, OpenLandMap)

**Temporal Change Detection**: Compare old SSURGO surveys against recent satellite-derived estimates

**Precision Agriculture**: Validate variable-rate prescriptions against ground-measured data

## Notes

- Free API access, no key required
- US coverage only
- Resolution: 1:12,000 to 1:24,000 scale (much finer than SoilGrids 250m)
- Survey dates vary by location (1950s to present)
- Updates are infrequent (10-30 years between surveys)
- Ground-measured, not predicted
- Perfect for contradiction finding when compared against ML predictions
