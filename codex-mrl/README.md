# codex-mrl

Query international Maximum Residue Limits for pesticides from Codex Alimentarius (WHO/FAO)

## Setup

```bash
cd codex-mrl
python3 -m venv .venv && source .venv/bin/activate && pip install bs4 requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/query.py --help
```

## Dependencies

- `bs4`
- `requests`
