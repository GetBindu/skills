# usda-nass

Query US agricultural statistics from USDA NASS — crop yields, production, acreage, and prices received by farmers. Historical records back to 1866.

## What it does

Queries the [USDA NASS QuickStats API](https://quickstats.nass.usda.gov/api) for official US agricultural statistics. Covers all major commodities (corn, soybeans, wheat, cotton, rice, livestock, dairy, etc.), all 50 states, and historical data going back to 1866. Primary use cases: yield gap analysis, market intelligence, agricultural contradiction finding, and policy research.

## Setup

```bash
cd usda-nass
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

| Name | Required | Description |
|------|----------|-------------|
| `NASS_API_KEY` | **Yes** | Free API key from https://quickstats.nass.usda.gov/api (register, instant) |

Pass via env var or `--api-key` flag. No rate limits once registered.

## Usage

### Input
```bash
export NASS_API_KEY=your-key-here
python3 scripts/query.py --commodity "CORN" --data-item "YIELD" --state "IOWA" --year 2023 --format json
```

### Output (expected — requires API key)
```json
{
  "query": {"commodity": "CORN", "data_item": "YIELD", "state": "IOWA", "year": 2023},
  "results": [
    {"year": 2023, "state": "IOWA", "commodity": "CORN", "data_item": "YIELD", "value": "202.0", "unit": "BU / ACRE"}
  ],
  "count": 1
}
```

### Other input modes
```bash
# National soybean production (all states aggregated)
python3 scripts/query.py --commodity "SOYBEANS" --data-item "PRODUCTION" --format json

# Wheat prices received by farmers in Kansas
python3 scripts/query.py --commodity "WHEAT" --data-item "PRICE RECEIVED" --state "KANSAS"

# Human-readable summary
python3 scripts/query.py --commodity "CORN" --data-item "ACRES PLANTED" --format summary
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--commodity` / `-c` | Commodity name: CORN, SOYBEANS, WHEAT, COTTON, RICE, etc. | required |
| `--data-item` / `-d` | Statistic type: YIELD, PRODUCTION, ACRES PLANTED, PRICE RECEIVED | required |
| `--state` / `-s` | US state name (omit for national total) | all |
| `--year` / `-y` | Specific year | all years |
| `--api-key` / `-k` | NASS API key (or use env var) | `NASS_API_KEY` env |
| `--format` / `-f` | `json` or `summary` | `json` |

## Dependencies

- `requests`

## Tested with

- **`--help`:** ✅ All flags documented, 3 example queries shown
- **Without API key:** ✅ Clean error message: "NASS API key required. Set NASS_API_KEY or pass --api-key"
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions, ran `--help`, correctly identified: free API key from quickstats.nass.usda.gov/api, all 6 parameters, commodity/data-item/state/year options, and use cases (yield gap analysis, market intelligence, contradiction finding)

### Agno agent verdict (excerpt)
> NASS API provides official US agricultural statistics. Free API key required (register at quickstats.nass.usda.gov/api, unlimited free access). Key parameters: --commodity (CORN, SOYBEANS, WHEAT), --data-item (YIELD, PRODUCTION, ACRES PLANTED, PRICE RECEIVED), --state (optional, any US state), --year (optional). Essential for yield gap analysis, market intelligence, and validating contradictions between survey data and ground truth measurements.

## See also

Reference docs (4 files):
- `references/api_parameters.md` — full parameter list + valid values
- `references/api_examples.md` — detailed query examples
- `references/query_examples.md` — common research query patterns
- `references/data_quality.md` — data coverage, limitations, and revision notes
