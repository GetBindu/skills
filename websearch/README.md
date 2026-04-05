# websearch

Search the web for scientific information via DuckDuckGo. No API key required.

## What it does

Scrapes DuckDuckGo's HTML search endpoint (`html.duckduckgo.com/html/`) and returns structured results. Supports three output formats (`summary`, `detailed`, `json`) and a `--science` mode that appends scientific-context terms to the query. Intended as a lightweight alternative to paid search APIs (Serper, Brave, etc.) for small numbers of queries where authentication and rate limits should be avoided.

## Setup

```bash
cd websearch
python3 -m venv .venv && source .venv/bin/activate && pip install requests beautifulsoup4 -q
```

## Environment variables

None. DuckDuckGo HTML endpoint is unauthenticated.

## Usage

### Input
```bash
python3 scripts/web_search.py --query "CRISPR gene editing" --max-results 3 --format json
```

### Output
```json
[
  {
    "title": "What Is CRISPR Gene Editing and How Does It Work?",
    "url": "https://health.clevelandclinic.org/crispr-gene-editing",
    "display_url": "health.clevelandclinic.org/crispr-gene-editing",
    "snippet": "Learn how CRISPR works as a gene editing tool..."
  },
  {
    "title": "What Is CRISPR? - National Institute of General Medical Sciences",
    "url": "https://nigms.nih.gov/biobeat/2024/10/what-is-crispr",
    "display_url": "nigms.nih.gov/biobeat/2024/10/what-is-crispr",
    "snippet": "CRISPR gene editing has many possible applications..."
  },
  {
    "title": "CRISPR gene editing - Wikipedia",
    "url": "https://en.wikipedia.org/wiki/CRISPR_gene_editing",
    "display_url": "en.wikipedia.org/wiki/CRISPR_gene_editing",
    "snippet": "CRISPR-Cas9 CRISPR gene editing is a genetic engineering technique..."
  }
]
```

### Other input modes
```bash
# Science-focused (adds "research" OR "scientific" OR "study")
python3 scripts/web_search.py --query "protein folding" --science

# Larger result set
python3 scripts/web_search.py --query "AlphaFold" --max-results 20

# Human-readable summary
python3 scripts/web_search.py --query "transformer architecture" --format summary
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--query` | Search query (required) | — |
| `--max-results` | Maximum results to return | 10 |
| `--science` | Append scientific-context terms to query | false |
| `--format` | `summary`, `detailed`, or `json` | `summary` |

## Dependencies

- `requests`
- `beautifulsoup4`

## Known limitations

- **HTML scraping is fragile** — breaks if DuckDuckGo changes their HTML layout
- **Rate limiting / UA filtering** — the default User-Agent is the script's identifier; DuckDuckGo may return empty results from certain subprocess environments. Running from a direct terminal shell works reliably
- **No pagination** — only returns what DDG serves on page 1
- **Not for heavy use** — for production or high-volume workloads, use Serper, Brave Search API, or similar

## Tested with

- **Direct script run:** ✅ `--query "CRISPR gene editing" --max-results 3 --format json` returned 3 real results (Cleveland Clinic, NIH, Wikipedia)
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions and executed successfully (return code 0), but DuckDuckGo returned empty results from the Agno subprocess environment — likely a UA/rate-limiting quirk. Agent correctly diagnosed the empty response and suggested using `--science` mode or a simpler query

### Agno agent verdict (excerpt)
> Purpose: Search the web for scientific information using DuckDuckGo (no API key required). Key features: no authentication, flexible output formats (summary/detailed/json), science-focused option, configurable results. The script executed successfully (return code 0), but returned an empty results array — could indicate DuckDuckGo returned no results for this specific query or a network/UA issue during execution.
