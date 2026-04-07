# epa-comptox

Query chemical toxicity data from EPA CompTox Dashboard for 880,000+ chemicals

## Setup

```bash
cd epa-comptox
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/query.py --help
```

## Dependencies

- `requests`
