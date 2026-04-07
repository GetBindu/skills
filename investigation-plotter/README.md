# investigation-plotter

Generate investigation-specific figures from the local artifact graph (post-run plotting agent).

## Setup

```bash
cd investigation-plotter
python3 -m venv .venv && source .venv/bin/activate && pip install matplotlib numpy -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/run.py --help
```

## Dependencies

- `matplotlib`
- `numpy`
