# chembl-database

Query ChEMBL bioactive molecules and drug discovery data.

## Setup

```bash
cd chembl-database
python3 -m venv .venv && source .venv/bin/activate && pip install chembl_webresource_client pandas -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/example_queries.py --help
```

## Dependencies

- `chembl_webresource_client`
- `pandas`
