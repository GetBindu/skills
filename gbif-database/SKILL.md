---
name: gbif-database
description: Query 2.4+ billion species occurrence records from Global Biodiversity Information Facility
---
# GBIF Biodiversity Database

Access global species occurrence data for agricultural biodiversity analysis.

## Overview

GBIF (Global Biodiversity Information Facility) aggregates 2.4+ billion species occurrence records from museum collections, citizen science observations, research surveys, and automated monitoring systems.

## Usage

### Query species occurrences:
```bash
python3 {baseDir}/scripts/query.py --species "Apis mellifera" --country "US"
```

### Geographic search:
```bash
python3 {baseDir}/scripts/query.py --species "Bombus" --lat 42.0 --lon -93.6
```

### Time series query:
```bash
python3 {baseDir}/scripts/query.py --species "Danaus plexippus" --year-start 2020 --year-end 2023
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--species` | Species scientific name | - |
| `--country` | Country code (e.g., US, IN) | - |
| `--lat` | Latitude for geographic search | - |
| `--lon` | Longitude for geographic search | - |
| `--year-start` | Start year | - |
| `--year-end` | End year | - |
| `--limit` | Maximum results | 20 |
| `--format` | Output format: summary, json | json |

## Examples

### Pollinator monitoring:
```bash
# Query honeybee occurrences in Iowa
python3 {baseDir}/scripts/query.py --species "Apis mellifera" --country "US" --year-start 2020 --year-end 2024
```

### Pest distribution mapping:
```bash
# Track invasive species spread
python3 {baseDir}/scripts/query.py --species "Halyomorpha halys" --country "US"
```

### Biodiversity assessment:
```bash
# Monitor pollinator populations in agricultural landscapes
python3 {baseDir}/scripts/query.py --species "Bombus" --lat 42.0 --lon -93.6 --limit 50
```

## Use Cases

**Pest Distribution Mapping**: Track the spread of agricultural pests across regions

**Pollinator Decline Analysis**: Monitor pollinator populations in agricultural landscapes

**Invasive Species Detection**: Identify new invasive species threatening crops

## Notes

- Free API access, no key required
- 2.4+ billion occurrence records
- Continuous updates
- Global coverage
- Data quality varies by source
- Includes coordinates, dates, and data sources
