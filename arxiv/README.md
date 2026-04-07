# arxiv

Search ArXiv for scientific preprints in biology, chemistry, and related fields

## Setup

```bash
cd arxiv
python3 -m venv .venv && source .venv/bin/activate && pip install requests xml -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/arxiv_search.py --help
```

## Dependencies

- `requests`
- `xml`
