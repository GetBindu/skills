# arboreto

Infer gene regulatory networks (GRNs) from gene expression data using scalable algorithms (GRNBoost2, GENIE3).

## Setup

```bash
cd arboreto
python3 -m venv .venv && source .venv/bin/activate && pip install arboreto pandas -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/basic_grn_inference.py --help
```

## Dependencies

- `arboreto`
- `pandas`
