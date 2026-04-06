---
name: sentinel-2
description: Query Sentinel-2 multispectral satellite imagery at 10m resolution from ESA Copernicus. Search by bounding box, date range, and cloud cover. Returns scene metadata with download links. Requires Copernicus Open Access Hub credentials. Use for agricultural monitoring, land use mapping, vegetation indices (NDVI), and environmental change detection.
license: MIT license
metadata:
    skill-author: K-Dense Inc.
    source: https://scihub.copernicus.eu
    requires-env: COPERNICUS_USER, COPERNICUS_PASSWORD
---

# Sentinel-2 Satellite Imagery

Access high-resolution multispectral satellite imagery for agricultural monitoring.

## Overview

Sentinel-2 provides 10m spatial resolution multispectral imagery with 5-day revisit time. Essential for vegetation index calculation, crop type classification, yield estimation, and crop stress detection.

## Usage

### Query imagery for growing season:
```bash
python3 {baseDir}/scripts/query.py --north 42.1 --south 42.0 --east -93.5 --west -93.7 --start 2023-06-01 --end 2023-09-30
```

### Query with cloud filter:
```bash
python3 {baseDir}/scripts/query.py --north 28.6 --south 28.4 --east 77.3 --west 77.1 --start 2023-01-01 --end 2023-12-31 --cloud-max 10
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--north` | Northern latitude | Required |
| `--south` | Southern latitude | Required |
| `--east` | Eastern longitude | Required |
| `--west` | Western longitude | Required |
| `--start` | Start date (YYYY-MM-DD) | Required |
| `--end` | End date (YYYY-MM-DD) | Required |
| `--cloud-max` | Max cloud cover % | 20 |
| `--username` | Copernicus username | COPERNICUS_USER env var |
| `--password` | Copernicus password | COPERNICUS_PASSWORD env var |
| `--format` | Output format: summary, json | json |

## Examples

### Yield contradiction finding (Use Case #3):
```bash
# Query Sentinel-2 for Iowa cornfield during growing season
python3 {baseDir}/scripts/query.py --north 42.1 --south 42.0 --east -93.5 --west -93.7 --start 2023-06-01 --end 2023-09-30 --cloud-max 10

# Calculate NDVI from imagery
# Derive yield estimate from NDVI time series
# Compare against USDA NASS reported yield
# 
# USDA NASS: 205 bu/acre (ground-reported)
# Sentinel-2 derived: 192 bu/acre (satellite estimate)
# Difference: 13 bu/acre → significant yield gap
```

### Crop monitoring:
```bash
python3 {baseDir}/scripts/query.py --north 36.1 --south 36.0 --east -120.5 --west -120.6 --start 2023-04-01 --end 2023-10-31
```

## Use Cases

**Yield Contradiction Finding**: Compare satellite-derived yield estimates against USDA NASS reported yields

**Soil Moisture Validation**: Derive soil moisture from Sentinel-2 and compare against ground sensors

**Crop Monitoring**: Track vegetation indices (NDVI, EVI, NDRE) throughout growing season

## Notes

- Registration required: https://scihub.copernicus.eu/
- Set `COPERNICUS_USER` and `COPERNICUS_PASSWORD` environment variables
- 10m resolution (visible/NIR), 20m (red edge/SWIR)
- 5-day revisit time (with both satellites)
- Historical archive: 2015-present
- Free access
- 13 spectral bands
