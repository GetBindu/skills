# USDA NASS QuickStats API Parameters Reference

Complete list of available parameters for querying the USDA NASS QuickStats API.

## Usage

Add parameters to your API request:
```
https://quickstats.nass.usda.gov/api/api_GET/?key=YOUR_KEY&commodity_desc=CORN&statisticcat_desc=YIELD&state_name=IOWA
```

Parameters are case-insensitive but values are case-sensitive.

## Core Parameters

### Required
- `key` - Your NASS API key (register at https://quickstats.nass.usda.gov/api)
- `format` - Response format: JSON, CSV, XML (default: JSON)

### Commodity Selection
- `commodity_desc` - Commodity name (e.g., CORN, SOYBEANS, WHEAT, CATTLE)
- `class_desc` - Commodity class (e.g., ALL CLASSES, GRAIN, SILAGE)
- `prodn_practice_desc` - Production practice (e.g., ALL PRODUCTION PRACTICES, IRRIGATED, NON-IRRIGATED, ORGANIC)
- `util_practice_desc` - Utilization practice (e.g., ALL UTILIZATION PRACTICES, GRAIN, SILAGE)

### Statistical Categories
- `statisticcat_desc` - Statistic category:
  - `YIELD` - Crop yield (BU/ACRE, TONS/ACRE, etc.)
  - `PRODUCTION` - Total production (BU, TONS, CWT, etc.)
  - `AREA PLANTED` - Planted acreage
  - `AREA HARVESTED` - Harvested acreage
  - `PRICE RECEIVED` - Price received by farmers ($/BU, $/CWT, etc.)
  - `SALES` - Sales value ($)
  - `INVENTORY` - Inventory levels
  - `OPERATIONS` - Number of operations

### Geographic Filters
- `state_name` - State name (e.g., IOWA, ILLINOIS, KANSAS)
- `state_alpha` - State abbreviation (e.g., IA, IL, KS)
- `state_fips_code` - State FIPS code (e.g., 19 for Iowa)
- `asd_desc` - Agricultural Statistics District
- `county_name` - County name
- `county_code` - County FIPS code
- `region_desc` - Region (e.g., MIDWEST, SOUTH, WEST)
- `zip_5` - 5-digit ZIP code

### Temporal Filters
- `year` - Year (e.g., 2023, 2022)
- `reference_period_desc` - Reference period:
  - `YEAR` - Annual data
  - `MARKETING YEAR` - Marketing year
  - `SEASON` - Growing season
  - Specific months: `JAN`, `FEB`, etc.
  - Quarters: `FIRST QUARTER`, etc.
- `freq_desc` - Frequency (ANNUAL, MONTHLY, WEEKLY)
- `begin_code` - Beginning period code
- `end_code` - Ending period code

### Data Characteristics
- `unit_desc` - Unit of measurement (BU, TONS, ACRES, $, etc.)
- `domain_desc` - Domain (TOTAL, ORGANIC STATUS, NAICS CLASSIFICATION, etc.)
- `domaincat_desc` - Domain category

### Data Source
- `source_desc` - Data source (SURVEY, CENSUS)
- `sector_desc` - Sector (CROPS, ANIMALS & PRODUCTS, ECONOMICS, DEMOGRAPHICS)
- `group_desc` - Commodity group (FIELD CROPS, VEGETABLES, FRUITS & NUTS, etc.)

## Common Parameter Combinations

### Query corn yield by state
```
commodity_desc=CORN
statisticcat_desc=YIELD
state_name=IOWA
year=2023
```

### Query soybean production (all states)
```
commodity_desc=SOYBEANS
statisticcat_desc=PRODUCTION
year=2023
```

### Query wheat prices for Kansas
```
commodity_desc=WHEAT
statisticcat_desc=PRICE RECEIVED
state_name=KANSAS
reference_period_desc=MARKETING YEAR
```

### Query organic corn acreage
```
commodity_desc=CORN
statisticcat_desc=AREA PLANTED
prodn_practice_desc=ORGANIC
year=2023
```

### Query county-level data
```
commodity_desc=CORN
statisticcat_desc=YIELD
state_name=IOWA
county_name=STORY
year=2023
```

## Commodity Names

### Major Field Crops
- `CORN` - Corn (all types)
- `CORN, GRAIN` - Grain corn
- `CORN, SILAGE` - Silage corn
- `SOYBEANS` - Soybeans
- `WHEAT` - Wheat (all types)
- `WHEAT, WINTER` - Winter wheat
- `WHEAT, SPRING` - Spring wheat
- `COTTON` - Cotton
- `RICE` - Rice
- `SORGHUM` - Sorghum
- `BARLEY` - Barley
- `OATS` - Oats

### Specialty Crops
- `HAY` - Hay (all types)
- `HAY, ALFALFA` - Alfalfa hay
- `PEANUTS` - Peanuts
- `SUNFLOWER` - Sunflower
- `CANOLA` - Canola

### Vegetables
- `POTATOES` - Potatoes
- `SWEET CORN` - Sweet corn
- `TOMATOES` - Tomatoes
- `LETTUCE` - Lettuce

### Fruits & Nuts
- `APPLES` - Apples
- `ORANGES` - Oranges
- `GRAPES` - Grapes
- `ALMONDS` - Almonds

### Livestock
- `CATTLE` - Cattle (all types)
- `CATTLE, COWS` - Cows
- `HOGS` - Hogs
- `CHICKENS` - Chickens
- `SHEEP` - Sheep

## State Names

Use full state names in uppercase:
- `ALABAMA`, `ALASKA`, `ARIZONA`, `ARKANSAS`
- `CALIFORNIA`, `COLORADO`, `CONNECTICUT`
- `DELAWARE`, `FLORIDA`, `GEORGIA`
- `HAWAII`, `IDAHO`, `ILLINOIS`, `INDIANA`, `IOWA`
- `KANSAS`, `KENTUCKY`, `LOUISIANA`
- `MAINE`, `MARYLAND`, `MASSACHUSETTS`, `MICHIGAN`, `MINNESOTA`, `MISSISSIPPI`, `MISSOURI`, `MONTANA`
- `NEBRASKA`, `NEVADA`, `NEW HAMPSHIRE`, `NEW JERSEY`, `NEW MEXICO`, `NEW YORK`, `NORTH CAROLINA`, `NORTH DAKOTA`
- `OHIO`, `OKLAHOMA`, `OREGON`
- `PENNSYLVANIA`, `RHODE ISLAND`
- `SOUTH CAROLINA`, `SOUTH DAKOTA`
- `TENNESSEE`, `TEXAS`
- `UTAH`, `VERMONT`, `VIRGINIA`
- `WASHINGTON`, `WEST VIRGINIA`, `WISCONSIN`, `WYOMING`

Or use `US TOTAL` for national-level data.

## Units of Measurement

### Yield Units
- `BU / ACRE` - Bushels per acre (corn, soybeans, wheat)
- `TONS / ACRE` - Tons per acre (hay, silage)
- `CWT / ACRE` - Hundredweight per acre (potatoes, sugar beets)
- `LB / ACRE` - Pounds per acre (cotton lint)

### Production Units
- `BU` - Bushels (corn, soybeans, wheat)
- `TONS` - Tons (hay, silage)
- `CWT` - Hundredweight (potatoes)
- `LB` - Pounds (cotton)
- `$ / ACRE` - Dollars per acre (value of production)

### Price Units
- `$ / BU` - Dollars per bushel
- `$ / TON` - Dollars per ton
- `$ / CWT` - Dollars per hundredweight
- `$ / LB` - Dollars per pound

### Area Units
- `ACRES` - Acres planted or harvested

## Response Format

### JSON Response Structure
```json
{
  "data": [
    {
      "source_desc": "SURVEY",
      "sector_desc": "CROPS",
      "group_desc": "FIELD CROPS",
      "commodity_desc": "CORN",
      "class_desc": "ALL CLASSES",
      "prodn_practice_desc": "ALL PRODUCTION PRACTICES",
      "util_practice_desc": "GRAIN",
      "statisticcat_desc": "YIELD",
      "unit_desc": "BU / ACRE",
      "short_desc": "CORN, GRAIN - YIELD, MEASURED IN BU / ACRE",
      "domain_desc": "TOTAL",
      "state_name": "IOWA",
      "asd_desc": "NORTHWEST",
      "county_name": "",
      "region_desc": "",
      "zip_5": "",
      "watershed_desc": "",
      "year": 2023,
      "freq_desc": "ANNUAL",
      "begin_code": "00",
      "end_code": "00",
      "reference_period_desc": "YEAR",
      "week_ending": "",
      "load_time": "2024-01-15 08:00:00",
      "Value": "205.0",
      "CV (%)": "1.2"
    }
  ]
}
```

## Rate Limits and Best Practices

1. **API Key Required**: Register at https://quickstats.nass.usda.gov/api
2. **Rate Limits**: No official limit, but be respectful (max ~10 requests/second)
3. **Result Limits**: Maximum 50,000 records per query
4. **Wildcards**: Not supported in parameter values
5. **Case Sensitivity**: Parameter names are case-insensitive, but values are case-sensitive
6. **Multiple Values**: Cannot query multiple values for same parameter in single request
7. **Null Values**: Use empty string for "all" or "not specified"

## Discovering Available Values

Use the `get_param_values` endpoint to discover valid parameter values:

```
https://quickstats.nass.usda.gov/api/get_param_values/?key=YOUR_KEY&param=commodity_desc
```

Available params to query:
- `commodity_desc`
- `statisticcat_desc`
- `state_name`
- `county_name`
- `year`
- `reference_period_desc`
- And all other parameters listed above

## Resources

- **API Documentation**: https://quickstats.nass.usda.gov/api
- **Register for API Key**: https://quickstats.nass.usda.gov/api
- **QuickStats Web Interface**: https://quickstats.nass.usda.gov/
- **NASS Help**: https://www.nass.usda.gov/
