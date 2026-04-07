# cosmic-database

Access COSMIC cancer mutation database.

## Setup

```bash
cd cosmic-database
python3 -m venv .venv && source .venv/bin/activate && pip install download_cosmic getpass gzip requests -q
```

## Environment variables

- `COSMIC_EMAIL`
- `COSMIC_PASSWORD`

## Usage

```bash
python3 scripts/query.py --help
```

## Dependencies

- `download_cosmic`
- `getpass`
- `gzip`
- `requests`
