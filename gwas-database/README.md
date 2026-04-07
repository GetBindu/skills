# gwas-database

Query NHGRI-EBI GWAS Catalog for SNP-trait associations.

## Setup

```bash
cd gwas-database
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
