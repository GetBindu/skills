# USDA NASS API Examples

Code examples in multiple languages for querying the USDA NASS QuickStats API.

## Python Examples

### Basic Query with requests
```python
import requests
import json

API_KEY = 'YOUR_API_KEY'
BASE_URL = 'https://quickstats.nass.usda.gov/api/api_GET/'

params = {
    'key': API_KEY,
    'commodity_desc': 'CORN',
    'statisticcat_desc': 'YIELD',
    'state_name': 'IOWA',
    'year': 2023,
    'format': 'JSON'
}

response = requests.get(BASE_URL, params=params)
data = response.json()

if 'data' in data and data['data']:
    for record in data['data']:
        print(f"{record['commodity_desc']} {record['statisticcat_desc']}: {record['Value']} {record['unit_desc']}")
else:
    print("No data found")
```

### Reusable Query Function
```python
def query_nass(commodity, data_item, state=None, year=None, api_key=None):
    """Query USDA NASS QuickStats API"""
    import os
    import requests
    
    if not api_key:
        api_key = os.environ.get('NASS_API_KEY')
    
    if not api_key:
        raise ValueError("API key required")
    
    params = {
        'key': api_key,
        'commodity_desc': commodity.upper(),
        'statisticcat_desc': data_item.upper(),
        'format': 'JSON'
    }
    
    if state:
        params['state_name'] = state.upper()
    if year:
        params['year'] = year
    
    response = requests.get(
        'https://quickstats.nass.usda.gov/api/api_GET/',
        params=params,
        timeout=30
    )
    response.raise_for_status()
    
    return response.json()

# Usage
data = query_nass('CORN', 'YIELD', 'IOWA', 2023)
```

### Pandas DataFrame Integration
```python
import pandas as pd
import requests

def nass_to_dataframe(commodity, data_item, states, years):
    """Query NASS and return pandas DataFrame"""
    all_data = []
    
    for state in states:
        for year in years:
            params = {
                'key': 'YOUR_API_KEY',
                'commodity_desc': commodity,
                'statisticcat_desc': data_item,
                'state_name': state,
                'year': year,
                'format': 'JSON'
            }
            
            response = requests.get(
                'https://quickstats.nass.usda.gov/api/api_GET/',
                params=params
            )
            
            if response.json().get('data'):
                all_data.extend(response.json()['data'])
    
    df = pd.DataFrame(all_data)
    return df

# Usage
corn_belt = ['IOWA', 'ILLINOIS', 'NEBRASKA', 'MINNESOTA', 'INDIANA']
years = range(2010, 2024)

df = nass_to_dataframe('CORN', 'YIELD', corn_belt, years)
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')

# Analyze
print(df.groupby('state_name')['Value'].mean())
```

## curl Examples

### Basic Query
```bash
curl "https://quickstats.nass.usda.gov/api/api_GET/?key=YOUR_API_KEY&commodity_desc=CORN&statisticcat_desc=YIELD&state_name=IOWA&year=2023&format=JSON"
```

### Pretty Print JSON
```bash
curl "https://quickstats.nass.usda.gov/api/api_GET/?key=YOUR_API_KEY&commodity_desc=CORN&statisticcat_desc=YIELD&state_name=IOWA&year=2023&format=JSON" | jq '.'
```

### Save to File
```bash
curl "https://quickstats.nass.usda.gov/api/api_GET/?key=YOUR_API_KEY&commodity_desc=SOYBEANS&statisticcat_desc=PRODUCTION&state_name=US TOTAL&year=2023&format=JSON" > soybean_production.json
```

### Get Parameter Values
```bash
curl "https://quickstats.nass.usda.gov/api/get_param_values/?key=YOUR_API_KEY&param=commodity_desc" | jq '.commodity_desc[]' | head -20
```

## R Examples

### Basic Query with httr
```r
library(httr)
library(jsonlite)

API_KEY <- "YOUR_API_KEY"
BASE_URL <- "https://quickstats.nass.usda.gov/api/api_GET/"

params <- list(
  key = API_KEY,
  commodity_desc = "CORN",
  statisticcat_desc = "YIELD",
  state_name = "IOWA",
  year = 2023,
  format = "JSON"
)

response <- GET(BASE_URL, query = params)
data <- fromJSON(content(response, "text"))

if (!is.null(data$data)) {
  print(data$data)
}
```

### Create Data Frame
```r
library(httr)
library(jsonlite)
library(dplyr)

query_nass <- function(commodity, data_item, state = NULL, year = NULL) {
  params <- list(
    key = Sys.getenv("NASS_API_KEY"),
    commodity_desc = toupper(commodity),
    statisticcat_desc = toupper(data_item),
    format = "JSON"
  )
  
  if (!is.null(state)) params$state_name <- toupper(state)
  if (!is.null(year)) params$year <- year
  
  response <- GET("https://quickstats.nass.usda.gov/api/api_GET/", query = params)
  data <- fromJSON(content(response, "text"))
  
  if (!is.null(data$data)) {
    return(as.data.frame(data$data))
  } else {
    return(NULL)
  }
}

# Usage
corn_yield <- query_nass("CORN", "YIELD", "IOWA", 2023)
print(corn_yield)
```

### Time Series Analysis
```r
library(httr)
library(jsonlite)
library(ggplot2)

# Get historical data
years <- 2010:2023
yield_data <- data.frame()

for (year in years) {
  data <- query_nass("CORN", "YIELD", "IOWA", year)
  if (!is.null(data)) {
    yield_data <- rbind(yield_data, data)
  }
}

# Convert to numeric
yield_data$Value <- as.numeric(yield_data$Value)
yield_data$year <- as.numeric(yield_data$year)

# Plot
ggplot(yield_data, aes(x = year, y = Value)) +
  geom_line() +
  geom_point() +
  labs(title = "Iowa Corn Yield Trend",
       x = "Year",
       y = "Yield (bu/acre)") +
  theme_minimal()
```

## JavaScript/Node.js Examples

### Basic Query with axios
```javascript
const axios = require('axios');

const API_KEY = 'YOUR_API_KEY';
const BASE_URL = 'https://quickstats.nass.usda.gov/api/api_GET/';

async function queryNASS(commodity, dataItem, state, year) {
  const params = {
    key: API_KEY,
    commodity_desc: commodity.toUpperCase(),
    statisticcat_desc: dataItem.toUpperCase(),
    state_name: state ? state.toUpperCase() : undefined,
    year: year,
    format: 'JSON'
  };
  
  try {
    const response = await axios.get(BASE_URL, { params });
    return response.data;
  } catch (error) {
    console.error('Error querying NASS:', error.message);
    return null;
  }
}

// Usage
queryNASS('CORN', 'YIELD', 'IOWA', 2023)
  .then(data => {
    if (data && data.data) {
      data.data.forEach(record => {
        console.log(`${record.commodity_desc} ${record.statisticcat_desc}: ${record.Value} ${record.unit_desc}`);
      });
    }
  });
```

### Fetch API (Browser)
```javascript
const API_KEY = 'YOUR_API_KEY';

async function queryNASS(commodity, dataItem, state, year) {
  const params = new URLSearchParams({
    key: API_KEY,
    commodity_desc: commodity.toUpperCase(),
    statisticcat_desc: dataItem.toUpperCase(),
    format: 'JSON'
  });
  
  if (state) params.append('state_name', state.toUpperCase());
  if (year) params.append('year', year);
  
  const url = `https://quickstats.nass.usda.gov/api/api_GET/?${params}`;
  
  try {
    const response = await fetch(url);
    const data = await response.json();
    return data;
  } catch (error) {
    console.error('Error:', error);
    return null;
  }
}

// Usage
queryNASS('CORN', 'YIELD', 'IOWA', 2023)
  .then(data => console.log(data));
```

## Complete Workflow Example (Python)

### Yield Gap Analysis Script
```python
#!/usr/bin/env python3
"""
Complete workflow: Compare NASS yield against satellite-derived estimate
"""

import os
import requests
import pandas as pd
import matplotlib.pyplot as plt

class NASSClient:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get('NASS_API_KEY')
        self.base_url = 'https://quickstats.nass.usda.gov/api/api_GET/'
    
    def query(self, **kwargs):
        params = {'key': self.api_key, 'format': 'JSON'}
        params.update(kwargs)
        
        response = requests.get(self.base_url, params=params, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        return data.get('data', [])
    
    def get_yield(self, commodity, state, year):
        records = self.query(
            commodity_desc=commodity.upper(),
            statisticcat_desc='YIELD',
            state_name=state.upper(),
            year=year
        )
        
        if records:
            return float(records[0]['Value'])
        return None

# Initialize client
nass = NASSClient()

# Get NASS reported yield
nass_yield = nass.get_yield('CORN', 'IOWA', 2023)
print(f"NASS Reported Yield: {nass_yield} bu/acre")

# Satellite-derived yield (from Sentinel-2 NDVI analysis)
satellite_yield = 192.0  # Example value

# Calculate yield gap
yield_gap = nass_yield - satellite_yield
yield_gap_pct = (yield_gap / nass_yield) * 100

print(f"Satellite Derived Yield: {satellite_yield} bu/acre")
print(f"Yield Gap: {yield_gap:.1f} bu/acre ({yield_gap_pct:.1f}%)")

# Visualize
fig, ax = plt.subplots(figsize=(8, 6))
sources = ['NASS\nReported', 'Satellite\nDerived']
yields = [nass_yield, satellite_yield]
colors = ['#2E7D32', '#1976D2']

bars = ax.bar(sources, yields, color=colors, alpha=0.7)
ax.set_ylabel('Yield (bu/acre)', fontsize=12)
ax.set_title('Iowa Corn Yield Comparison - 2023', fontsize=14, fontweight='bold')
ax.set_ylim(0, max(yields) * 1.2)

# Add value labels
for bar, yield_val in zip(bars, yields):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2., height,
            f'{yield_val:.1f}',
            ha='center', va='bottom', fontsize=11)

# Add gap annotation
ax.annotate('', xy=(0, nass_yield), xytext=(1, satellite_yield),
            arrowprops=dict(arrowstyle='<->', color='red', lw=2))
ax.text(0.5, (nass_yield + satellite_yield)/2,
        f'Gap: {yield_gap:.1f} bu/acre\n({yield_gap_pct:.1f}%)',
        ha='center', va='center',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='red'))

plt.tight_layout()
plt.savefig('yield_gap_analysis.png', dpi=300)
plt.show()
```

## Resources

- **API Documentation**: https://quickstats.nass.usda.gov/api
- **Python requests**: https://docs.python-requests.org/
- **R httr**: https://httr.r-lib.org/
- **Node.js axios**: https://axios-http.com/
