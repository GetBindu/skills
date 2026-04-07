---
name: modis
description: Query daily global vegetation indices and land surface data from NASA MODIS
---
# MODIS Satellite Data

Access daily global vegetation and land surface data from NASA MODIS.

## Overview

MODIS (Moderate Resolution Imaging Spectroradiometer) provides daily global coverage with pre-processed vegetation indices, land surface temperature, and other products at 250m-1km resolution.

## Usage

### Query vegetation indices:
```bash
python3 {baseDir}/scripts/query.py --product MOD13Q1 --lat 42.0 --lon -93.6 --start 2023-04-01 --end 2023-10-31
```

### Query land surface temperature:
```bash
python3 {baseDir}/scripts/query.py --product MOD11A1 --lat 28.5 --lon 77.2 --start 2023-01-01 --end 2023-12-31
```

### Query surface reflectance:
```bash
python3 {baseDir}/scripts/query.py --product MOD09A1 --lat 36.1 --lon -120.5 --start 2023-06-01 --end 2023-09-30
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--product` | MODIS product | Required |
| `--lat` | Latitude coordinate | Required |
| `--lon` | Longitude coordinate | Required |
| `--start` | Start date (YYYY-MM-DD) | Required |
| `--end` | End date (YYYY-MM-DD) | Required |
| `--format` | Output format: summary, json | json |

## Common Products

- **MOD13Q1** - Vegetation Indices 16-Day 250m (NDVI, EVI)
- **MOD11A1** - Land Surface Temperature Daily 1km
- **MCD43A4** - Nadir BRDF-Adjusted Reflectance Daily 500m
- **MOD09A1** - Surface Reflectance 8-Day 500m
- **MCD15A2H** - Leaf Area Index 8-Day 500m

## Examples

### Daily crop monitoring:
```bash
# Track NDVI throughout growing season
python3 {baseDir}/scripts/query.py --product MOD13Q1 --lat 42.0 --lon -93.6 --start 2023-04-01 --end 2023-10-31
```

### Drought detection:
```bash
# Monitor vegetation stress in near-real-time
python3 {baseDir}/scripts/query.py --product MOD13Q1 --lat 36.5 --lon -100.2 --start 2023-06-01 --end 2023-09-30
```

### Yield forecasting:
```bash
# Use daily NDVI time series for yield prediction models
python3 {baseDir}/scripts/query.py --product MOD13Q1 --lat 40.5 --lon -88.2 --start 2023-05-01 --end 2023-10-31
```

## Use Cases

**Daily Crop Monitoring**: Track vegetation indices throughout growing season with daily coverage

**Drought Detection**: Monitor vegetation stress in near-real-time

**Yield Forecasting**: Use daily NDVI time series for yield prediction models

## Notes

- Free API access, no key required
- Daily global coverage
- 250m-1km resolution (depending on product)
- Historical archive: 2000-present
- Pre-processed products (NDVI, EVI, LST)
- Coarser resolution than Sentinel-2/Landsat but much more frequent
