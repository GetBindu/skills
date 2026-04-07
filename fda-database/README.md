# fda-database

Query openFDA API for drugs, devices, adverse events, recalls, regulatory submissions (510k, PMA), substance identification (UNII), for FDA regulatory data analysis and safety research.

## Setup

```bash
cd fda-database
python3 -m venv .venv && source .venv/bin/activate && pip install fda_query requests -q
```

## Environment variables

- `FDA_API_KEY`

## Usage

```bash
python3 scripts/fda_examples.py --help
```

## Dependencies

- `fda_query`
- `requests`
