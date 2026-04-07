# materials

Materials Project lookup and structure analysis (pymatgen, ASE)

## Setup

```bash
cd materials
python3 -m venv .venv && source .venv/bin/activate && pip install mp_api pymatgen requests -q
```

## Environment variables

- `MP_API_KEY`

## Usage

```bash
python3 scripts/materials_lookup.py --help
```

## Dependencies

- `mp_api`
- `pymatgen`
- `requests`
