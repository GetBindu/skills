# drugbank-database

Access and analyze comprehensive drug information from the DrugBank database including drug properties, interactions, targets, pathways, chemical structures, and pharmacology data.

## Setup

```bash
cd drugbank-database
python3 -m venv .venv && source .venv/bin/activate && pip install drugbank_downloader drugbank_helper xml zipfile -q
```

## Environment variables

- `DRUGBANK_VERSION`
- `DRUGBANK_XML_PATH`
- `DRUGBANK_ZIP_PATH`

## Usage

```bash
python3 scripts/drugbank_helper.py --help
```

## Dependencies

- `drugbank_downloader`
- `drugbank_helper`
- `xml`
- `zipfile`
