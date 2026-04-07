---
name: noaa-climate-data
description: Query historical weather and climate data from NOAA Climate Data Online
---
# NOAA Climate Data Online

Access historical weather and climate data from NOAA for agricultural analysis.

## Overview

NOAA Climate Data Online provides access to daily temperature, precipitation, and other meteorological data from thousands of weather stations globally, with best coverage in the United States.

## Usage

### Query weather data for growing season:
```bash
python3 {baseDir}/scripts/query.py --lat 42.0308 --lon -93.6319 --start-date 2023-04-01 --end-date 2023-10-31
```

### Query by station ID:
```bash
python3 {baseDir}/scripts/query.py --station-id GHCND:USW00014933 --start-date 2023-01-01 --end-date 2023-12-31
```

### Query specific data types:
```bash
python3 {baseDir}/scripts/query.py --lat 28.5 --lon 77.2 --start-date 2023-06-01 --end-date 2023-09-30 --data-types TMAX TMIN PRCP
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--lat` | Latitude coordinate | - |
| `--lon` | Longitude coordinate | - |
| `--station-id` | NOAA station ID | - |
| `--start-date` | Start date (YYYY-MM-DD) | Required |
| `--end-date` | End date (YYYY-MM-DD) | Required |
| `--data-types` | Data types to query | All |
| `--api-key` | NOAA API key | NOAA_API_KEY env var |
| `--format` | Output format: summary, json | json |

## Data Types

- **TMAX** - Maximum temperature
- **TMIN** - Minimum temperature
- **PRCP** - Precipitation
- **SNOW** - Snowfall
- **SNWD** - Snow depth
- **AWND** - Average wind speed

## Examples

### Yield prediction validation:
```bash
# Query weather data for Iowa growing season
python3 {baseDir}/scripts/query.py --lat 42.0308 --lon -93.6319 --start-date 2023-04-01 --end-date 2023-10-31 --data-types TMAX TMIN PRCP

# Compare crop yield models using NOAA weather against satellite-derived estimates
```

### Climate trend analysis:
```bash
python3 {baseDir}/scripts/query.py --station-id GHCND:USW00014933 --start-date 2020-01-01 --end-date 2024-12-31
```

## Use Cases

**Yield Prediction Validation**: Compare crop yield models using NOAA weather data against satellite-derived estimates

**Climate Trend Analysis**: Analyze long-term temperature and precipitation trends affecting agriculture

**Growing Season Characterization**: Calculate growing degree days and frost dates for crop planning

## Notes

- API key required: Register at https://www.ncdc.noaa.gov/cdo-web/token
- Set `NOAA_API_KEY` environment variable
- Global coverage (best in US)
- Historical data: 1763-present (varies by station)
- Daily updates
- Free access with rate limits
