# labarchive-integration

Electronic lab notebook API integration.

## Setup

```bash
cd labarchive-integration
python3 -m venv .venv && source .venv/bin/activate && pip install labarchivespy requests xml yaml -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/entry_operations.py --help
```

## Dependencies

- `labarchivespy`
- `requests`
- `xml`
- `yaml`
