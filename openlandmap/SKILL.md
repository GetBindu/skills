---
name: openlandmap
description: Query ML-predicted global soil properties from EnvirometriX using different algorithms than SoilGrids
---
# OpenLandMap Soil Properties

Access ML-predicted global soil data using different algorithms than SoilGrids for three-way contradiction detection.

## Overview

OpenLandMap provides global soil property predictions at 250m resolution using different machine learning algorithms, training datasets, and spatial covariates than SoilGrids. This makes it a third independent data source for robust soil contradiction finding.

## Usage

### Query soil properties:
```bash
python3 {baseDir}/scripts/query.py --lat 42.0308 --lon -93.6319 --properties ph soc clay
```

### Query specific depth:
```bash
python3 {baseDir}/scripts/query.py --lat 28.5 --lon 77.2 --depth "0-5cm" --format json
```

### Compare with other sources:
```bash
python3 {baseDir}/scripts/query.py --lat -23.5 --lon -46.6 --properties ph soc clay bdod
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--lat` | Latitude (-90 to 90) | Required |
| `--lon` | Longitude (-180 to 180) | Required |
| `--properties` | Soil properties to query | ph soc clay |
| `--depth` | Depth layer | 0-5cm |
| `--format` | Output format: summary, json | json |

## Available Properties

- **ph** - Soil pH
- **soc** - Soil Organic Carbon
- **clay** - Clay content
- **bdod** - Bulk density

## Examples

### Three-way soil contradiction pattern:
```bash
# Query all three sources for same location
# SoilGrids: pH 6.8 ± 0.3 (ML algorithm A)
# OpenLandMap: pH 6.6 ± 0.2 (ML algorithm B)
# SSURGO: pH 6.1 (Ground survey)
# 
# Pattern analysis:
# - All three disagree → high uncertainty
# - Two agree, one differs → investigate outlier
# - All three agree → high confidence
```

## Use Cases

**Three-Way Contradiction Detection**: Compare SoilGrids vs SSURGO vs OpenLandMap for robust uncertainty quantification

**Algorithm Sensitivity Analysis**: Understand how different ML approaches affect soil predictions

**Uncertainty Quantification**: Use disagreement between sources as proxy for prediction uncertainty

## Notes

- Free access (WCS protocol implementation pending)
- Global coverage
- 250m resolution
- ML-predicted, not ground-measured
- Different methodology than SoilGrids
- Ideal third data source for contradiction finding
