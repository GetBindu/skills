# nistwebbook

Look up chemical data from NIST Chemistry WebBook (thermochemistry, spectra, properties)

## Setup

```bash
cd nistwebbook
python3 -m venv .venv && source .venv/bin/activate && pip install nistchempy requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/nistwebbook_search.py --help
```

## Dependencies

- `nistchempy`
- `requests`
