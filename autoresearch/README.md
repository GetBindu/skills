# autoresearch

Autonomous AI agent that modifies and iteratively improves a GPT language model training setup, running experiments within a 5-minute time budget to optimize validation bits-per-byte.

## Setup

```bash
cd autoresearch
python3 -m venv .venv && source .venv/bin/activate && pip install requests scientia -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/autoresearch_client.py --help
```

## Dependencies

- `requests`
- `scientia`
