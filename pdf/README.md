# pdf

Extract text, tables, and metadata from scientific PDF papers and reports

## Setup

```bash
cd pdf
python3 -m venv .venv && source .venv/bin/activate && pip install pdfplumber pypdf -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/pdf_extract.py --help
```

## Dependencies

- `pdfplumber`
- `pypdf`
