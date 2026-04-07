# askcos

Retrosynthetic template relevance prediction using a locally deployed ASKCOS TorchServe service.

## Setup

```bash
cd askcos
python3 -m venv .venv && source .venv/bin/activate && pip install rdkit requests selenium -q
```

## Environment variables

- `ASKCOS_BASE_URL`
- `ASKCOS_MODEL`

## Usage

```bash
python3 scripts/askcos_retro.py --help
```

## Dependencies

- `rdkit`
- `requests`
- `selenium`
