# USDA NASS Data Quality and Limitations

Understanding data quality, coverage, and limitations of USDA NASS agricultural statistics.

## Data Sources

### Survey Data
- **Collection Method**: Statistical surveys of farmers and ranchers
- **Sample Size**: Varies by commodity and state (typically 10,000-50,000 respondents)
- **Response Rate**: 60-80% depending on survey
- **Frequency**: Weekly, monthly, quarterly, annual depending on commodity
- **Coverage**: All US states and territories

### Census Data
- **Collection Method**: Complete enumeration (Census of Agriculture every 5 years)
- **Last Census**: 2022 (published 2024)
- **Coverage**: All farms with $1,000+ in annual sales
- **Detail Level**: County-level data available
- **Historical**: Available back to 1840

## Data Quality Indicators

### Coefficient of Variation (CV)
- **Definition**: Measure of relative variability (standard error / estimate × 100)
- **Interpretation**:
  - CV < 10%: Reliable estimate
  - CV 10-25%: Moderately reliable
  - CV > 25%: Use with caution
  - CV > 50%: Unreliable, often suppressed

### Data Flags
- **(D)** - Withheld to avoid disclosing data for individual operations
- **(Z)** - Less than half the unit shown
- **(NA)** - Not available
- **(X)** - Not applicable

## Coverage and Limitations

### Geographic Coverage

**Excellent Coverage (County-level data available):**
- Major field crops: Corn, soybeans, wheat, cotton
- Major livestock: Cattle, hogs, chickens
- States: All major agricultural states

**Limited Coverage (State-level only):**
- Specialty crops in minor production states
- Organic production (limited historical data)
- Small-scale operations

**No Coverage:**
- Individual farm-level data (confidential)
- Sub-county geographic detail
- Real-time data (surveys have lag time)

### Temporal Coverage

**Annual Data:**
- Most field crops
- Livestock inventory
- Published: February-March (previous year)

**Monthly Data:**
- Prices received by farmers
- Livestock production
- Published: End of month + 1-2 weeks

**Weekly Data:**
- Crop progress
- Condition ratings
- Published: Monday afternoons

**Historical Data:**
- Available back to 1866 for some commodities
- Methodology changes over time (not always comparable)
- County-level data: 1997-present (Census years earlier)

## Known Data Quality Issues

### 1. Survey Non-Response Bias
**Issue**: Farmers who don't respond may differ systematically from respondents

**Impact**: 
- Larger operations more likely to respond
- May overestimate yields in some cases
- Undercount small/part-time operations

**Mitigation**: NASS uses statistical adjustments for non-response

### 2. Reporting Lag
**Issue**: Data published weeks to months after reference period

**Example**:
- 2023 crop year data published February 2024
- Monthly prices published 2-3 weeks after month end

**Impact**: Not suitable for real-time decision making

### 3. County-Level Suppression
**Issue**: Data withheld if fewer than 3 operations or would disclose individual data

**Impact**:
- Many counties have suppressed data
- Particularly affects specialty crops
- Limits spatial analysis

### 4. Methodology Changes
**Issue**: Survey methods, definitions, and coverage change over time

**Examples**:
- Organic data collection began 2008
- County-level data standardized 1997
- Acreage estimation methods improved with satellite data

**Impact**: Long-term trends may not be directly comparable

### 5. Yield Estimation Challenges
**Issue**: Yields are estimated from surveys, not measured

**Sources of Error**:
- Farmer estimates may be optimistic or pessimistic
- Harvest losses not always accounted for
- Weather impacts during harvest season

**Comparison with Satellite Data**:
- NASS yields often 5-15% higher than satellite-derived estimates
- Differences vary by state and year
- Perfect for contradiction finding!

## Data Validation Best Practices

### 1. Check CV Values
```python
if 'CV (%)' in data and float(data['CV (%)']) > 25:
    print("Warning: High variability in estimate")
```

### 2. Verify Data Flags
```python
if data['Value'] in ['(D)', '(Z)', '(NA)', '(X)']:
    print("Warning: Data suppressed or not available")
```

### 3. Compare Multiple Sources
```python
# Compare NASS survey vs. Census data
survey_value = get_nass_survey_data(2023)
census_value = get_nass_census_data(2022)

if abs(survey_value - census_value) / census_value > 0.10:
    print("Warning: >10% difference between survey and census")
```

### 4. Check for Outliers
```python
# Compare against historical range
historical_yields = get_historical_data(2010, 2023)
current_yield = get_current_data(2024)

mean = np.mean(historical_yields)
std = np.std(historical_yields)

if abs(current_yield - mean) > 2 * std:
    print("Warning: Current value is >2 standard deviations from mean")
```

## Contradiction Finding Opportunities

### 1. NASS vs. Satellite-Derived Yields
**Pattern**: NASS reported yields often 5-15% higher than satellite estimates

**Example**:
- NASS: 205 bu/acre (Iowa corn, 2023)
- Sentinel-2 derived: 192 bu/acre
- Difference: 13 bu/acre (6.3%)

**Causes**:
- Farmer optimism in estimates
- Survey timing (before harvest losses)
- Sample bias toward better-managed farms
- Satellite algorithm limitations

### 2. Survey vs. Census Data
**Pattern**: Survey estimates may differ from Census counts

**Example**:
- 2023 Survey: 85.5M acres corn planted
- 2022 Census: 83.2M acres corn planted
- Difference: 2.3M acres (2.8%)

**Causes**:
- Survey sample vs. complete enumeration
- Definition differences
- Timing differences

### 3. State vs. County Aggregation
**Pattern**: Sum of county data ≠ state total (due to suppression)

**Example**:
- Iowa state total: 13.5M acres corn
- Sum of county data: 12.8M acres (5.2% missing due to suppression)

**Impact**: County-level analysis incomplete

### 4. Organic vs. Conventional Reporting
**Pattern**: Organic acreage underreported in early years

**Example**:
- NASS organic corn: 250K acres (2010)
- USDA certified organic: 310K acres (2010)
- Difference: 60K acres (24% undercount)

**Causes**:
- Survey coverage gaps
- Certification vs. production timing
- Small operation undercount

## Using NASS Data for Contradiction Detection

### Recommended Workflow

1. **Query NASS Data**
   ```python
   nass_yield = query_nass(commodity='CORN', state='IOWA', year=2023)
   ```

2. **Query Alternative Source** (Satellite, FAO, etc.)
   ```python
   satellite_yield = query_sentinel2_derived_yield(location, year=2023)
   ```

3. **Calculate Discrepancy**
   ```python
   discrepancy = abs(nass_yield - satellite_yield)
   discrepancy_pct = (discrepancy / nass_yield) * 100
   ```

4. **Assess Significance**
   ```python
   if discrepancy_pct > 10:
       print(f"Significant contradiction: {discrepancy_pct:.1f}% difference")
       print(f"NASS: {nass_yield} bu/acre")
       print(f"Satellite: {satellite_yield} bu/acre")
   ```

5. **Investigate Causes**
   - Check CV values (high variability?)
   - Check timing (survey vs. satellite date)
   - Check geographic match (state vs. pixel)
   - Check methodology differences

## Resources

- **NASS Methodology**: https://www.nass.usda.gov/Education_and_Outreach/Understanding_Statistics/
- **Survey Methods**: https://www.nass.usda.gov/Surveys/
- **Data Quality**: https://www.nass.usda.gov/Publications/Methodology_and_Data_Quality/
- **Census Methodology**: https://www.nass.usda.gov/AgCensus/Methodology/
