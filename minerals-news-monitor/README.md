# minerals-news-monitor

Discover critical-minerals and materials signals from newspapers, blogs, and industry media using web search, with norma

## Setup

```bash
cd minerals-news-monitor
python3 -m venv .venv && source .venv/bin/activate && pip install bs4 requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/news_monitor.py --help
```

## Dependencies

- `bs4`
- `requests`
