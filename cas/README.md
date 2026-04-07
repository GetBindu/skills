# cas

Look up chemicals in CAS Common Chemistry (name, CAS RN, SMILES, InChI; ~500k compounds)

## Setup

```bash
cd cas
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

- `CAS_API_KEY`

## Usage

```bash
python3 scripts/cas_search.py --help
```

## Dependencies

- `requests`
