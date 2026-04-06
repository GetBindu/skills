---
name: usda-nass
description: Query US agricultural statistics from USDA NASS including crop yields, production, acreage, and prices. Primary source for US agricultural data with historical records back to 1866. Essential for yield gap analysis, market intelligence, and agricultural contradiction finding.
license: Public Domain
metadata:
    skill-author: K-Dense Inc.
---

# USDA NASS Agricultural Statistics

## Overview

USDA NASS (National Agricultural Statistics Service) is the official source for US agricultural statistics. Access crop production, yields, planted acreage, prices received by farmers, and livestock data for all US states and commodities via the QuickStats API.

## When to Use This Skill

This skill should be used when:
- Querying official US crop yields, production, or acreage data
- Comparing reported agricultural statistics against satellite-derived estimates
- Tracking commodity prices received by farmers
- Analyzing historical agricultural trends (1866-present for some commodities)
- Performing yield gap analysis between reported and predicted values
- Validating crop insurance claims or loss adjustments
- Conducting market intelligence for agricultural commodities
- Finding contradictions between survey data and ground truth measurements

## Core Capabilities

### 1. Querying Crop Statistics

Query production, yield, and acreage data for major field crops.

**Common query patterns:**
```python
# Corn yield for Iowa
commodity = "CORN"
data_item = "YIELD"
state = "IOWA"
year = 2023

# Soybean production (national)
commodity = "SOYBEANS"
data_item = "PRODUCTION"
state = "US TOTAL"

# Wheat prices for Kansas
commodity = "WHEAT"
data_item = "PRICE RECEIVED"
state = "KANSAS"
```

Use the API endpoint: `https://quickstats.nass.usda.gov/api/api_GET/?key={key}&commodity_desc={commodity}&statisticcat_desc={data_item}&state_name={state}`

**Supported commodities:** CORN, SOYBEANS, WHEAT, COTTON, RICE, HAY, and 500+ others

**Supported data items:** YIELD, PRODUCTION, AREA PLANTED, AREA HARVESTED, PRICE RECEIVED, SALES, INVENTORY

### 2. Geographic Filtering

Query data at multiple geographic levels.

**Geographic levels:**
- **National**: `state_name=US TOTAL`
- **State**: `state_name=IOWA`
- **County**: `state_name=IOWA&county_name=STORY`
- **Agricultural Statistics District**: `asd_desc=NORTHWEST`
- **Region**: `region_desc=MIDWEST`

**Example:** County-level corn yield
```bash
python3 {baseDir}/scripts/query.py --commodity "CORN" --data-item "YIELD" --state "IOWA" --county "STORY" --year 2023
```

### 3. Time Series Analysis

Query historical data for trend analysis.

**Temporal coverage:**
- Annual data: Most commodities, 1866-present
- Monthly data: Prices, livestock production
- Weekly data: Crop progress, condition ratings

**Example:** Historical yield trend
```python
for year in range(2010, 2024):
    query_nass(commodity="CORN", data_item="YIELD", state="IOWA", year=year)
```

### 4. Production Practice Comparisons

Compare organic vs. conventional, irrigated vs. non-irrigated.

**Production practices:**
- `ALL PRODUCTION PRACTICES` - All farming methods
- `ORGANIC` - Certified organic production
- `IRRIGATED` - Irrigated cropland
- `NON-IRRIGATED` - Dryland/rainfed cropland

**Example:** Organic vs. conventional acreage
```bash
python3 {baseDir}/scripts/query.py --commodity "CORN" --data-item "AREA PLANTED" --state "IOWA" --production-practice "ORGANIC" --year 2023
```

### 5. Livestock and Specialty Crops

Query livestock inventory, production, and specialty crop data.

**Livestock commodities:**
- CATTLE, HOGS, CHICKENS, SHEEP, TURKEYS

**Specialty crops:**
- Vegetables: POTATOES, TOMATOES, LETTUCE
- Fruits: APPLES, ORANGES, GRAPES
- Nuts: ALMONDS, WALNUTS, PECANS

See `references/api_parameters.md` for complete commodity list.

## Python Implementation

For programmatic access, use the provided helper script `scripts/query.py` which implements:

- `query_nass(commodity, data_item, state, year)` - Query NASS QuickStats API
- `format_summary(data)` - Format results as human-readable summary
- `format_json(data)` - Format results as JSON

**Example usage:**
```bash
python3 {baseDir}/scripts/query.py --commodity "CORN" --data-item "YIELD" --state "IOWA" --year 2023 --format json
```

## Query Examples

### Basic Queries
```bash
# Iowa corn yield
python3 {baseDir}/scripts/query.py --commodity "CORN" --data-item "YIELD" --state "IOWA" --year 2023

# National soybean production
python3 {baseDir}/scripts/query.py --commodity "SOYBEANS" --data-item "PRODUCTION" --state "US TOTAL" --year 2023

# Kansas wheat prices
python3 {baseDir}/scripts/query.py --commodity "WHEAT" --data-item "PRICE RECEIVED" --state "KANSAS" --year 2023
```

### Advanced Queries
```bash
# County-level data
python3 {baseDir}/scripts/query.py --commodity "CORN" --data-item "YIELD" --state "IOWA" --county "STORY" --year 2023

# Organic production
python3 {baseDir}/scripts/query.py --commodity "SOYBEANS" --data-item "AREA PLANTED" --state "ILLINOIS" --production-practice "ORGANIC" --year 2023

# Irrigated vs. non-irrigated yields
python3 {baseDir}/scripts/query.py --commodity "CORN" --data-item "YIELD" --state "NEBRASKA" --production-practice "IRRIGATED" --year 2023
```

See `references/query_examples.md` for comprehensive examples in Python, R, JavaScript, and curl.

## Use Case: Yield Gap Contradiction Finding

**Scenario**: Compare NASS reported yields against satellite-derived estimates to identify systematic discrepancies.

**Workflow:**
1. Query NASS reported yield for Iowa corn (2023)
2. Calculate satellite-derived yield from Sentinel-2 NDVI time series
3. Compare values and quantify yield gap

**Example:**
```python
# NASS reported yield
nass_yield = 205.0  # bu/acre (from QuickStats API)

# Satellite-derived yield
satellite_yield = 192.0  # bu/acre (from NDVI analysis)

# Calculate yield gap
yield_gap = nass_yield - satellite_yield  # 13.0 bu/acre
yield_gap_pct = (yield_gap / nass_yield) * 100  # 6.3%

# Interpretation: NASS yields are 6.3% higher than satellite estimates
# Potential causes:
# - Survey sample bias toward better-managed farms
# - Farmer optimism in yield estimates
# - Harvest losses not captured in satellite data
# - Timing differences (survey vs. satellite observation)
```

**Impact**: 13 bu/acre difference × $4.50/bu = $58.50/acre revenue impact

See `references/data_quality.md` for detailed discussion of NASS data quality and contradiction opportunities.

## Best Practices

1. **Check data quality indicators**: Review CV (Coefficient of Variation) values; CV > 25% indicates high uncertainty
2. **Handle suppressed data**: County-level data often suppressed to protect individual operations (flagged as "(D)")
3. **Use appropriate geographic level**: State-level data more reliable than county-level
4. **Account for survey timing**: Annual data published February-March for previous year
5. **Compare multiple sources**: Cross-validate NASS data against satellite, FAO, or other sources
6. **Filter by review status**: Survey data vs. Census data (Census every 5 years, more comprehensive)
7. **Understand methodology changes**: Historical data may not be directly comparable due to methodology changes

## Resources

### scripts/
`query.py` - Python client for USDA NASS QuickStats API with support for commodity queries, geographic filtering, time series analysis, and formatted output.

### references/
- `api_parameters.md` - Complete list of API parameters, commodities, states, and data items
- `query_examples.md` - Comprehensive query examples in Python, R, JavaScript, and curl
- `data_quality.md` - Data quality indicators, limitations, and contradiction finding opportunities
- `api_examples.md` - Code examples in multiple languages with complete workflows

## Additional Resources

- **API Documentation**: https://quickstats.nass.usda.gov/api
- **Register for API Key**: https://quickstats.nass.usda.gov/api (free)
- **QuickStats Web Interface**: https://quickstats.nass.usda.gov/ (test queries visually)
- **NASS Reports**: https://www.nass.usda.gov/Publications/
- **Methodology**: https://www.nass.usda.gov/Education_and_Outreach/Understanding_Statistics/
