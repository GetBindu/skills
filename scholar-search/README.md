# scholar-search

Search Google Scholar via SerpAPI — titles, authors, citations, venues, links.

## Setup

`pip install requests`

## Env vars

`SERPAPI_KEY` *(required)* — Free at https://serpapi.com (100 searches/month)

## Usage

```bash
export SERPAPI_KEY=your-key
python3 scripts/scholar_search.py --query "CRISPR delivery" --num-results 5
```

## Tested with

- **`--help`:** ✅
- **Agno:** ✅

## Fix notes

- Rewrote: removed hardcoded local path + private `cmm_data` dep. Now uses SerpAPI directly via `requests`.
