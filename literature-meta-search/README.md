# literature-meta-search

Unified search across OSTI, Google Scholar, ArXiv, and corpus-search with deduplication and reciprocal rank fusion

## Setup

```bash
cd literature-meta-search
python3 -m venv .venv && source .venv/bin/activate && pip install difflib httpx xml -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/meta_search.py --help
```

## Dependencies

- `difflib`
- `httpx`
- `xml`
