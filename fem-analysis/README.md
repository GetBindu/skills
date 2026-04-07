# fem-analysis

Modal analysis of a membrane STL using Kirchhoff plate FEM (scipy eigensolver).

## Setup

```bash
cd fem-analysis
python3 -m venv .venv && source .venv/bin/activate && pip install matplotlib numpy scipy struct -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/modal_analysis.py --help
```

## Dependencies

- `matplotlib`
- `numpy`
- `scipy`
- `struct`
