# diffdock

Diffusion-based molecular docking.

## Setup

```bash
cd diffdock
python3 -m venv .venv && source .venv/bin/activate && pip install esm pandas rdkit torch -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/analyze_results.py --help
```

## Dependencies

- `esm`
- `pandas`
- `rdkit`
- `torch`
