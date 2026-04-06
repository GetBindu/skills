# usfiscaldata

Query US Treasury Fiscal Data API — national debt, federal spending, revenue, exchange rates, savings bonds, and interest rates. 54 datasets, 182+ tables, free, no auth.

## What it does

Dynamic query engine for the [US Treasury Fiscal Data API](https://fiscaldata.treasury.gov/api-documentation/). No API key required. Supports filtering, sorting, field selection, pagination, endpoint discovery, and schema introspection. Covers data going back to the 1970s-1990s depending on the dataset.

## Setup

```bash
cd usfiscaldata
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

None. Free public API, no authentication.

## Usage

### Input — national debt (debt to the penny)
```bash
python3 scripts/fiscal_data.py --endpoint "v2/accounting/od/debt_to_penny" --page-size 3 --output-format summary
```

### Output
```json
{
  "summary": {
    "endpoint": "v2/accounting/od/debt_to_penny",
    "count": 3,
    "latest_date": "1993-04-01",
    "sample_records": [
      {
        "record_date": "1993-04-01",
        "tot_pub_debt_out_amt": "4225873987843.44",
        "record_fiscal_year": "1993"
      }
    ]
  }
}
```

### Key endpoints

| Endpoint | Description | Update frequency |
|----------|-------------|------------------|
| `v2/accounting/od/debt_to_penny` | Total public debt (precise daily) | Daily |
| `v2/accounting/od/debt_outstanding` | Debt outstanding summary | Daily |
| `v1/accounting/mts/mts_table_1` | Monthly receipts and outlays | Monthly |
| `v1/accounting/mts/mts_table_5` | Budget categories | Monthly |
| `v1/accounting/od/rates_of_exchange` | Treasury exchange rates | Quarterly |
| `v2/accounting/od/avg_interest_rates` | Average interest on US debt | Monthly |
| `v2/accounting/od/savings_bonds_pcs` | I-bond and EE bond rates | Varies |

### Other input modes
```bash
# Discover all available tables
python3 scripts/fiscal_data.py --discover

# Get schema for an endpoint
python3 scripts/fiscal_data.py --endpoint "v2/accounting/od/avg_interest_rates" --schema

# Filter + field selection
python3 scripts/fiscal_data.py --endpoint "v2/accounting/od/debt_to_penny" \
  --filter "record_date:gte:2024-01-01" --fields "record_date,tot_pub_debt_out_amt" --page-size 10
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--endpoint` | API endpoint path | — |
| `--fields` | Comma-separated field list | all |
| `--filter` | Filter expression (e.g., `record_date:gte:2024-01-01`) | — |
| `--sort` | Sort field | — |
| `--page-size` | Results per page (1-10000) | API default |
| `--page-number` | Page number | 1 |
| `--format` | `json` or `csv` | `json` |
| `--discover` | List all available tables | — |
| `--schema` | Get schema for endpoint | — |
| `--output-format` | `json` or `summary` | `json` |

## Dependencies

- `requests`

## Tested with

- **Direct script run (debt_to_penny):** ✅ Returns real debt data ($4.2T in 1993, first 3 records)
- **`--discover`:** ⚠️ Returns 404 — discovery endpoint path needs verification against current API docs. Individual endpoints work.
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions, executed query, listed 5 endpoint categories (debt, spending/revenue, exchange rates, interest rates, savings bonds), correctly identified 54 datasets / 182+ tables / free / no auth

### Agno agent verdict (excerpt)
> The usfiscaldata skill provides access to the US Treasury Fiscal Data API — free, no-authentication-required with 54 datasets and 182+ tables covering national debt, federal spending, revenue, exchange rates, savings bonds, and interest rates. Historical data going back to 1970s-1990s depending on dataset. Daily updates for debt data, monthly for spending/revenue, quarterly for exchange rates. Note: All numeric values are returned as strings and must be explicitly converted.

## See also

- SKILL.md contains the full endpoint catalog with all 54 datasets
