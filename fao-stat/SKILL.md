---
name: fao-stat
description: Query global agricultural statistics from UN FAO covering 245 countries and territories
---
# FAO STAT Global Agriculture Database

Access comprehensive global food and agriculture statistics from the United Nations Food and Agriculture Organization.

## Overview

FAO STAT is the world's most comprehensive database of food and agriculture statistics. Query production, trade, consumption, and price data for 245 countries across all major agricultural commodities.

## Usage

### Query wheat production in India:
```bash
python3 {baseDir}/scripts/query.py --domain "Production" --country "India" --item "Wheat" --element "Production"
```

### Query trade data with time series:
```bash
python3 {baseDir}/scripts/query.py --domain "Trade" --country "Brazil" --item "Soybeans" --year-start 2020 --year-end 2023
```

### Query food prices:
```bash
python3 {baseDir}/scripts/query.py --domain "Prices" --country "United States" --item "Maize"
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--domain` | Data domain | Required |
| `--country` | Country name or ISO code | Required |
| `--item` | Commodity or item name | Required |
| `--element` | Data element | - |
| `--year-start` | Start year for time series | - |
| `--year-end` | End year for time series | - |
| `--format` | Output format: summary, json | json |

## Data Domains

- **Production** - Crop and livestock production
- **Trade** - Import/export flows
- **Prices** - Agricultural commodity prices
- **Food Balance** - Production, consumption, waste
- **Land Use** - Agricultural land and irrigation
- **Fertilizers** - Fertilizer consumption

## Elements

Common elements for Production domain:
- **Production** - Total production (tonnes)
- **Yield** - Crop yield (tonnes/hectare)
- **Area harvested** - Harvested area (hectares)

## Examples

### Cross-country comparison:
```bash
python3 {baseDir}/scripts/query.py --domain "Production" --country "China" --item "Rice" --element "Yield"
```

### Track trade flows:
```bash
python3 {baseDir}/scripts/query.py --domain "Trade" --country "Argentina" --item "Soybeans" --year-start 2015 --year-end 2024
```

### Food security analysis:
```bash
python3 {baseDir}/scripts/query.py --domain "Food Balance" --country "Kenya" --item "Maize"
```

## Use Cases

**Global Trade Analysis**: Track agricultural commodity movements between countries

**Food Security Assessment**: Analyze production vs. consumption gaps

**Climate Impact Studies**: Correlate agricultural production with climate data across regions

## Notes

- Free API access, no key required
- Data updated annually with monthly updates for some indicators
- Historical data available back to 1961 for most commodities
- Data quality varies by country (developed countries more reliable)
- Country-reported data may conflict with satellite-derived estimates
