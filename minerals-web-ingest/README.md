# minerals-web-ingest

Ingest and normalize web pages for critical-minerals intelligence, with optional Firecrawl fetching, deduplication manif

## Setup

```bash
cd minerals-web-ingest
python3 -m venv .venv && source .venv/bin/activate && pip install bs4 requests -q
```

## Environment variables

- `FIRECRAWL_API_KEY`

## Usage

```bash
python3 scripts/web_ingest.py --help
```

## Dependencies

- `bs4`
- `requests`
