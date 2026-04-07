---
name: landsat
description: Query Landsat satellite imagery with 50+ year archive from NASA/USGS
---
# Landsat Satellite Imagery

Access the longest continuous satellite record of Earth's surface for agricultural analysis.

## Overview

Landsat provides 30m spatial resolution multispectral imagery with a 50+ year archive (1972-present). Essential for long-term land use change analysis, historical crop pattern analysis, and climate change impact assessment.

## Usage

### Query by bounding box:
```bash
python3 {baseDir}/scripts/query.py --north 42.1 --south 42.0 --east -93.5 --west -93.7 --start 2023-06-01 --end 2023-09-30
```

### Query by path/row:
```bash
python3 {baseDir}/scripts/query.py --path 26 --row 31 --start 1990-01-01 --end 1990-12-31 --collection landsat-5
```

### Query historical data:
```bash
python3 {baseDir}/scripts/query.py --north 42.1 --south 42.0 --east -93.5 --west -93.7 --start 1985-06-01 --end 1985-09-30 --collection landsat-5
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--north` | Northern latitude | - |
| `--south` | Southern latitude | - |
| `--east` | Eastern longitude | - |
| `--west` | Western longitude | - |
| `--path` | Landsat path | - |
| `--row` | Landsat row | - |
| `--start` | Start date (YYYY-MM-DD) | Required |
| `--end` | End date (YYYY-MM-DD) | Required |
| `--collection` | Landsat collection | landsat-8 |
| `--cloud-max` | Max cloud cover % | 20 |
| `--username` | USGS username | USGS_USER env var |
| `--password` | USGS password | USGS_PASSWORD env var |
| `--format` | Output format: summary, json | json |

## Collections

- **landsat-5** - 1984-2013
- **landsat-7** - 1999-present
- **landsat-8** - 2013-present
- **landsat-9** - 2021-present

## Examples

### Historical yield trend analysis:
```bash
# Compare 1990s vegetation patterns against current data
python3 {baseDir}/scripts/query.py --path 26 --row 31 --start 1990-06-01 --end 1990-09-30 --collection landsat-5
```

### Land use change detection:
```bash
# Track conversion of natural areas to agriculture
python3 {baseDir}/scripts/query.py --north 42.1 --south 42.0 --east -93.5 --west -93.7 --start 1985-01-01 --end 2024-12-31
```

## Use Cases

**Historical Yield Trend Analysis**: Correlate long-term vegetation indices with yield trends

**Land Use Change Detection**: Track conversion of natural areas to agriculture over decades

**Climate Impact Assessment**: Analyze how agricultural regions have changed over 50+ years

## Notes

- Registration required: https://ers.cr.usgs.gov/register/
- Set `USGS_USER` and `USGS_PASSWORD` environment variables
- 30m resolution (multispectral), 15m (panchromatic)
- 16-day revisit time
- Historical archive: 1972-present
- Free access
- Longest satellite record available
