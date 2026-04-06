# scholar-search

Search Google Scholar for academic papers via the SerpAPI service, returning citation counts, metadata, and links.

## What it does

This skill queries Google Scholar through the SerpAPI backend to find academic papers matching a given search query. It returns structured results including titles, authors, venues, publication years, citation counts, snippets, and URLs (including PDF links when available).

Results can be filtered by year range, sorted by relevance or citation count, and output in summary, detailed, or JSON format. The skill is designed for critical minerals research but works with any academic search query.

The underlying client comes from the proprietary `cmm_data` package, which wraps SerpAPI's Google Scholar endpoint with additional parsing and normalization.

## Setup

```bash
cd scholar-search
python3 -m venv .venv && source .venv/bin/activate && pip install serpapi cmm_data -q
```

Note: `cmm_data` is a proprietary package and must be available on the system path or installed separately.

## Environment variables

| Variable | Description | Required |
|----------|-------------|----------|
| `SERPAPI_KEY` | SerpAPI key for Google Scholar access | Yes |

## Usage

### Input

```bash
python3 scripts/scholar_search.py --query "lithium extraction brine"
python3 scripts/scholar_search.py --query "rare earth separation" --year-from 2020 --sort-by citations
python3 scripts/scholar_search.py --query "critical minerals policy" --format json
```

### Output

```
Found 10 Google Scholar results:

--------------------------------------------------------------------------------

1. Lithium Extraction from Brine: A Review
   Smith J, Doe A
   Journal of Mining Science (2023) [142 citations]

2. Novel Methods for Lithium Recovery
   Lee K, Park S
   Chemical Engineering Journal (2022) [89 citations]

--------------------------------------------------------------------------------
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--query`, `-q` | Search query (required) | -- |
| `--year-from` | Start year filter | None |
| `--year-to` | End year filter | None |
| `--num-results`, `-n` | Number of results (max 20) | `10` |
| `--sort-by`, `-s` | Sort order: `relevance` or `citations` | `relevance` |
| `--format`, `-f` | Output format: `summary`, `detailed`, or `json` | `summary` |

## Dependencies

- `serpapi`
- `cmm_data` (proprietary)

## Tested with

- **Direct script run:** requires `cmm_data` (proprietary); not smoke-testable without it
- **Agno agent (Claude Haiku 4.5):** pass (dry-run)

### Agno agent verdict (excerpt)

> The skill loaded successfully in dry-run mode. The frontmatter and directory structure are valid. Full execution requires the proprietary cmm_data package and a SERPAPI_KEY.

## Fix notes

- Restructured openclaw frontmatter to Agno-compatible format
- Cleaned `__pycache__/` directories
