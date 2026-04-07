# adaptyv

Cloud laboratory platform for automated protein testing and validation.

## Setup

```bash
cd adaptyv
python3 -m venv .venv && source .venv/bin/activate && pip install dotenv requests -q
```

## Environment variables

- `ADAPTYV_API_KEY`

## Usage

```bash
python3 scripts/get_status.py --help
```

## Dependencies

- `dotenv`
- `requests`
