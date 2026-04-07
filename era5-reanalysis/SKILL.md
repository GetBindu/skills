---
name: era5-reanalysis
description: Query global atmospheric reanalysis data from ECMWF/Copernicus ERA5
---
# ERA5 Climate Reanalysis

Access global atmospheric reanalysis data from ECMWF/Copernicus for agricultural climate analysis.

## Overview

ERA5 is a global climate reanalysis dataset combining weather observations with numerical weather prediction models. Provides consistent, gridded climate data covering 1940-present at 31km resolution with hourly temporal resolution.

## Usage

### Query soil moisture for growing season:
```bash
python3 {baseDir}/scripts/query.py --variable "soil_moisture" --north 43 --south 41 --east -93 --west -95 --start 2023-04-01 --end 2023-10-31
```

### Query temperature data:
```bash
python3 {baseDir}/scripts/query.py --variable "temperature" --north 30 --south 28 --east 78 --west 76 --start 2023-01-01 --end 2023-12-31
```

### Query precipitation:
```bash
python3 {baseDir}/scripts/query.py --variable "precipitation" --north 42 --south 40 --east -88 --west -90 --start 2023-06-01 --end 2023-09-30 --time-resolution monthly
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--variable` | Climate variable | Required |
| `--north` | Northern latitude | Required |
| `--south` | Southern latitude | Required |
| `--east` | Eastern longitude | Required |
| `--west` | Western longitude | Required |
| `--start` | Start date (YYYY-MM-DD) | Required |
| `--end` | End date (YYYY-MM-DD) | Required |
| `--time-resolution` | hourly or monthly | monthly |
| `--format` | Output format: summary, json | json |

## Available Variables

- **temperature** - 2m temperature
- **precipitation** - Total precipitation
- **soil_moisture** - Volumetric soil water
- **wind** - 10m wind speed

## Examples

### Soil moisture contradiction finding:
```bash
# Query ERA5 soil moisture
python3 {baseDir}/scripts/query.py --variable "soil_moisture" --north 43 --south 41 --east -93 --west -95 --start 2023-06-01 --end 2023-09-30

# Compare three sources:
# Satellite-derived: 22%
# Ground sensor: 28%
# ERA5 reanalysis: 25%
# 
# Three independent estimates enable robust contradiction detection
```

### Climate impact assessment:
```bash
python3 {baseDir}/scripts/query.py --variable "temperature" --north 42 --south 40 --east -90 --west -92 --start 2020-01-01 --end 2024-12-31 --time-resolution monthly
```

## Use Cases

**Soil Moisture Validation**: Compare ERA5 soil moisture against satellite-derived estimates and ground sensors

**Climate Impact Assessment**: Analyze long-term climate trends affecting crop yields

**Gap Filling**: Provide weather data for regions lacking ground stations

## Notes

- CDS API key required: Register at https://cds.climate.copernicus.eu/
- Set `CDS_API_KEY` environment variable
- Global coverage
- 31km spatial resolution (~0.25° × 0.25°)
- Hourly or monthly temporal resolution
- Historical range: 1940-present
- Updated within 5 days of real-time
- Free access
