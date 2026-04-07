# pubchem-database

Query PubChem via PUG-REST API/PubChemPy (110M+ compounds).

## Setup

```bash
cd pubchem-database
python3 -m venv .venv && source .venv/bin/activate && pip install pubchempy requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/bioactivity_query.py --help
```

## Dependencies

- `pubchempy`
- `requests`
