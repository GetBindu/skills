---
name: iucn-red-list
description: Query species conservation status from IUCN Red List of Threatened Species
---
# IUCN Red List Database

Access species conservation status data for agricultural biodiversity assessment.

## Overview

The IUCN Red List provides comprehensive assessments of species conservation status including threat categories, population trends, major threats, and conservation actions needed.

## Usage

### Query species conservation status:
```bash
python3 {baseDir}/scripts/query.py --species "Bombus affinis"
```

### Query by category:
```bash
python3 {baseDir}/scripts/query.py --category "CR" --region "North America"
```

### Check pollinator status:
```bash
python3 {baseDir}/scripts/query.py --species "Apis mellifera"
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--species` | Species scientific name | - |
| `--category` | Conservation category | - |
| `--region` | Geographic region | - |
| `--api-key` | IUCN API key | IUCN_API_KEY env var |
| `--format` | Output format: summary, json | json |

## Conservation Categories

- **CR** - Critically Endangered
- **EN** - Endangered
- **VU** - Vulnerable
- **NT** - Near Threatened
- **LC** - Least Concern
- **DD** - Data Deficient

## Examples

### Pollinator conservation:
```bash
# Check rusty patched bumble bee status
python3 {baseDir}/scripts/query.py --species "Bombus affinis"
# Returns: Critically Endangered, population decreasing
```

### Crop wild relatives:
```bash
# Identify threatened wild relatives of major crops
python3 {baseDir}/scripts/query.py --species "Zea diploperennis"
```

### Ecosystem services assessment:
```bash
# Evaluate biodiversity supporting agricultural production
python3 {baseDir}/scripts/query.py --category "EN" --region "North America"
```

## Use Cases

**Pollinator Conservation**: Track conservation status of bee, butterfly, and other pollinator species

**Crop Wild Relatives**: Identify threatened wild relatives of major crops (genetic resources)

**Ecosystem Services Assessment**: Evaluate biodiversity supporting agricultural production

## Notes

- API key required: Register at https://apiv3.iucnredlist.org/
- Set `IUCN_API_KEY` environment variable
- 150,000+ species assessed
- Species reassessed every 5-10 years
- Free access
