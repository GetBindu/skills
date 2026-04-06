# USDA NASS Query Examples

Practical examples for common agricultural data queries using the USDA NASS QuickStats API.

## Basic Queries

### Query corn yield for Iowa
```python
import requests

params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'CORN',
    'statisticcat_desc': 'YIELD',
    'state_name': 'IOWA',
    'year': 2023,
    'format': 'JSON'
}

response = requests.get('https://quickstats.nass.usda.gov/api/api_GET/', params=params)
data = response.json()
```

### Query soybean production (national total)
```python
params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'SOYBEANS',
    'statisticcat_desc': 'PRODUCTION',
    'state_name': 'US TOTAL',
    'year': 2023,
    'format': 'JSON'
}
```

### Query wheat prices for Kansas
```python
params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'WHEAT',
    'statisticcat_desc': 'PRICE RECEIVED',
    'state_name': 'KANSAS',
    'reference_period_desc': 'MARKETING YEAR',
    'year': 2023,
    'format': 'JSON'
}
```

## Time Series Queries

### Historical corn yield trend (2010-2023)
```python
years = range(2010, 2024)
yield_data = []

for year in years:
    params = {
        'key': 'YOUR_API_KEY',
        'commodity_desc': 'CORN',
        'statisticcat_desc': 'YIELD',
        'state_name': 'IOWA',
        'year': year,
        'format': 'JSON'
    }
    response = requests.get('https://quickstats.nass.usda.gov/api/api_GET/', params=params)
    yield_data.append(response.json())
```

### Monthly price tracking
```python
months = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 
          'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']

for month in months:
    params = {
        'key': 'YOUR_API_KEY',
        'commodity_desc': 'CORN',
        'statisticcat_desc': 'PRICE RECEIVED',
        'state_name': 'ILLINOIS',
        'reference_period_desc': month,
        'year': 2023,
        'format': 'JSON'
    }
```

## Geographic Comparisons

### Compare yields across Corn Belt states
```python
corn_belt_states = ['IOWA', 'ILLINOIS', 'NEBRASKA', 'MINNESOTA', 'INDIANA']
state_yields = {}

for state in corn_belt_states:
    params = {
        'key': 'YOUR_API_KEY',
        'commodity_desc': 'CORN',
        'statisticcat_desc': 'YIELD',
        'state_name': state,
        'year': 2023,
        'format': 'JSON'
    }
    response = requests.get('https://quickstats.nass.usda.gov/api/api_GET/', params=params)
    state_yields[state] = response.json()
```

### County-level yield data
```python
params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'CORN',
    'statisticcat_desc': 'YIELD',
    'state_name': 'IOWA',
    'county_name': 'STORY',
    'year': 2023,
    'format': 'JSON'
}
```

## Production Practice Comparisons

### Organic vs. Conventional production
```python
# Organic
organic_params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'CORN',
    'statisticcat_desc': 'AREA PLANTED',
    'prodn_practice_desc': 'ORGANIC',
    'state_name': 'IOWA',
    'year': 2023,
    'format': 'JSON'
}

# Conventional (all production practices)
conventional_params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'CORN',
    'statisticcat_desc': 'AREA PLANTED',
    'prodn_practice_desc': 'ALL PRODUCTION PRACTICES',
    'state_name': 'IOWA',
    'year': 2023,
    'format': 'JSON'
}
```

### Irrigated vs. Non-irrigated yields
```python
# Irrigated
irrigated_params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'CORN',
    'statisticcat_desc': 'YIELD',
    'prodn_practice_desc': 'IRRIGATED',
    'state_name': 'NEBRASKA',
    'year': 2023,
    'format': 'JSON'
}

# Non-irrigated
dryland_params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'CORN',
    'statisticcat_desc': 'YIELD',
    'prodn_practice_desc': 'NON-IRRIGATED',
    'state_name': 'NEBRASKA',
    'year': 2023,
    'format': 'JSON'
}
```

## Livestock Queries

### Cattle inventory
```python
params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'CATTLE',
    'statisticcat_desc': 'INVENTORY',
    'state_name': 'TEXAS',
    'year': 2023,
    'format': 'JSON'
}
```

### Hog production
```python
params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'HOGS',
    'statisticcat_desc': 'PRODUCTION',
    'state_name': 'IOWA',
    'year': 2023,
    'format': 'JSON'
}
```

## Specialty Crop Queries

### Vegetable production
```python
params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'POTATOES',
    'statisticcat_desc': 'PRODUCTION',
    'state_name': 'IDAHO',
    'year': 2023,
    'format': 'JSON'
}
```

### Fruit production
```python
params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'APPLES',
    'statisticcat_desc': 'PRODUCTION',
    'state_name': 'WASHINGTON',
    'year': 2023,
    'format': 'JSON'
}
```

## Use Case: Yield Gap Analysis

### Compare NASS reported yield vs. satellite-derived estimate
```python
# Step 1: Get NASS reported yield
nass_params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'CORN',
    'statisticcat_desc': 'YIELD',
    'state_name': 'IOWA',
    'year': 2023,
    'format': 'JSON'
}

nass_response = requests.get('https://quickstats.nass.usda.gov/api/api_GET/', params=nass_params)
nass_yield = float(nass_response.json()['data'][0]['Value'])

# Step 2: Get satellite-derived yield (from Sentinel-2/MODIS analysis)
satellite_yield = 192.0  # Example: derived from NDVI time series

# Step 3: Calculate yield gap
yield_gap = nass_yield - satellite_yield
yield_gap_percent = (yield_gap / nass_yield) * 100

print(f"NASS Reported Yield: {nass_yield} bu/acre")
print(f"Satellite Derived Yield: {satellite_yield} bu/acre")
print(f"Yield Gap: {yield_gap} bu/acre ({yield_gap_percent:.1f}%)")

# Output:
# NASS Reported Yield: 205.0 bu/acre
# Satellite Derived Yield: 192.0 bu/acre
# Yield Gap: 13.0 bu/acre (6.3%)
```

## Use Case: Price Trend Analysis

### Track commodity price changes over marketing year
```python
import pandas as pd
import matplotlib.pyplot as plt

# Get monthly prices for marketing year
months = ['SEP', 'OCT', 'NOV', 'DEC', 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG']
prices = []

for month in months:
    params = {
        'key': 'YOUR_API_KEY',
        'commodity_desc': 'CORN',
        'statisticcat_desc': 'PRICE RECEIVED',
        'state_name': 'ILLINOIS',
        'reference_period_desc': month,
        'year': 2023,
        'format': 'JSON'
    }
    response = requests.get('https://quickstats.nass.usda.gov/api/api_GET/', params=params)
    if response.json()['data']:
        price = float(response.json()['data'][0]['Value'])
        prices.append({'month': month, 'price': price})

df = pd.DataFrame(prices)
df.plot(x='month', y='price', kind='line', title='Corn Prices - Illinois Marketing Year 2023')
plt.ylabel('Price ($/bu)')
plt.show()
```

## Use Case: Regional Production Analysis

### Calculate state's share of national production
```python
# Get state production
state_params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'SOYBEANS',
    'statisticcat_desc': 'PRODUCTION',
    'state_name': 'IOWA',
    'year': 2023,
    'format': 'JSON'
}

state_response = requests.get('https://quickstats.nass.usda.gov/api/api_GET/', params=state_params)
state_production = float(state_response.json()['data'][0]['Value'])

# Get national production
national_params = {
    'key': 'YOUR_API_KEY',
    'commodity_desc': 'SOYBEANS',
    'statisticcat_desc': 'PRODUCTION',
    'state_name': 'US TOTAL',
    'year': 2023,
    'format': 'JSON'
}

national_response = requests.get('https://quickstats.nass.usda.gov/api/api_GET/', params=national_params)
national_production = float(national_response.json()['data'][0]['Value'])

# Calculate share
state_share = (state_production / national_production) * 100

print(f"Iowa Soybean Production: {state_production:,.0f} BU")
print(f"US Total Soybean Production: {national_production:,.0f} BU")
print(f"Iowa's Share: {state_share:.1f}%")
```

## Error Handling

### Handle missing data gracefully
```python
def safe_query(params):
    try:
        response = requests.get('https://quickstats.nass.usda.gov/api/api_GET/', params=params, timeout=30)
        response.raise_for_status()
        data = response.json()
        
        if 'data' not in data or not data['data']:
            print(f"No data found for query: {params}")
            return None
        
        return data['data']
    
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Error parsing response: {e}")
        return None
```

## Resources

- **API Documentation**: https://quickstats.nass.usda.gov/api
- **QuickStats Web Interface**: https://quickstats.nass.usda.gov/ (test queries visually)
- **NASS Reports**: https://www.nass.usda.gov/Publications/ (official reports)
- **Data Dictionary**: Use `get_param_values` endpoint to discover valid values
