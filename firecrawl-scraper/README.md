# firecrawl-scraper

Web scraping of JavaScript-rendered scientific websites using Firecrawl API

## Setup

```bash
cd firecrawl-scraper
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

- `FIRECRAWL_API_KEY`

## Usage

```bash
python3 scripts/firecrawl_scrape.py --help
```

## Dependencies

- `requests`
