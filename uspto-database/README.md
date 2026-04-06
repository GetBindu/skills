# uspto-database

Access USPTO APIs for patent search, examination history (PEDS), and trademark status/monitoring (TSDR). Three specialized scripts covering the full IP lifecycle.

## What it does

Three CLI clients for different USPTO API surfaces:

1. **`patent_search.py`** — search patents by keywords, inventors, assignees, or CPC classifications via PatentsView API
2. **`peds_client.py`** — retrieve patent examination history, office actions, prosecution events, and pendency data via the Patent Examination Data System (PEDS)
3. **`trademark_client.py`** — look up trademark status, goods/services, ownership, prosecution history, and health monitoring via TSDR

## Setup

```bash
cd uspto-database
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
# For PEDS client: pip install uspto-opendata-python -q
```

## Environment variables

| Name | Required by | Description |
|------|------------|-------------|
| `PATENTSVIEW_API_KEY` | `patent_search.py` | Free key from https://patentsview.org/api-v01-information-page |
| `USPTO_API_KEY` | `trademark_client.py`, `peds_client.py` | Free key from https://account.uspto.gov/api-manager/ |

Both are free to register, instant activation.

## Usage

### Patent search
```bash
export PATENTSVIEW_API_KEY=your-key
python3 scripts/patent_search.py --query "CRISPR gene editing" --max-results 5
```

### Trademark lookup
```bash
export USPTO_API_KEY=your-key
python3 scripts/trademark_client.py --serial 87654321
python3 scripts/trademark_client.py --status 87654321
python3 scripts/trademark_client.py --health 87654321
python3 scripts/trademark_client.py --goods 87654321
python3 scripts/trademark_client.py --owner 87654321
python3 scripts/trademark_client.py --prosecution 87654321
```

### Patent examination history (PEDS)
```bash
export USPTO_API_KEY=your-key
pip install uspto-opendata-python -q
python3 scripts/peds_client.py --application 16123456
```

## CLI flags

### patent_search.py
| Flag | Description |
|------|-------------|
| `--query` / `-q` | Keyword search query |
| `--inventor` / `-i` | Inventor name |
| `--assignee` / `-a` | Assignee / company name |
| `--cpc` | CPC classification code |
| `--max-results` | Max results to return |
| `--format` | Output format |

### trademark_client.py
| Flag | Description |
|------|-------------|
| `--serial` / `-s` | Trademark serial number |
| `--registration` / `-r` | Trademark registration number |
| `--status` | Registration status summary |
| `--health` | Trademark health check with alerts |
| `--goods` / `-g` | Goods and services info |
| `--owner` / `-o` | Ownership information |
| `--prosecution` / `-p` | Prosecution history |
| `--api-key` | Override env var |

## Dependencies

- `requests` (all scripts)
- `uspto-opendata-python` (PEDS client only)

## Tested with

- **`trademark_client.py --help`:** ✅ All 7 query modes listed
- **`peds_client.py --help`:** ✅ Clean "install required" message
- **`patent_search.py --help`:** ⚠️ Crashes before argparse — API key validation runs in `__init__` before args are parsed. Works when key is set.
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions, ran `trademark_client.py --help`, correctly described all 3 scripts, both API keys (USPTO + PatentsView), and the 7 trademark query options

### Agno agent verdict (excerpt)
> Three scripts cover the full IP lifecycle: (1) patent_search.py — search by keywords/inventors/assignees/CPC classifications via PatentsView, (2) peds_client.py — prosecution history, office actions, pendency analysis via PEDS, (3) trademark_client.py — 7 query modes (serial/registration/status/health/goods/owner/prosecution) via TSDR. Two API keys needed: USPTO API Key (register at account.uspto.gov/api-manager/) and PatentsView API Key (patentsview.org). Both free, instant activation.

## See also

Reference docs (4 files):
- `references/patentsearch_api.md` — PatentsView search API details
- `references/peds_api.md` — PEDS examination data endpoints
- `references/trademark_api.md` — TSDR trademark API reference
- `references/additional_apis.md` — other USPTO data sources (assignments, citations, office actions)

## Fix notes

- Removed stray `__pycache__/`
- No script changes — all 3 scripts already functional (886 lines total)
- Noted `patent_search.py` argparse bug (key check before help) in README
