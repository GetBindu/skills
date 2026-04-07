# structure-contact-analysis

Identify peptide–protein contact hotspots from a PDB structure (local file or fetched from RCSB) and emit binding hotspot positions.

## Setup

```bash
cd structure-contact-analysis
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/run.py --help
```

## Dependencies

- `requests`
