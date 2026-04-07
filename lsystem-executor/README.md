# lsystem-executor

Execute L-system and shape grammars to produce visual derivations, SVG/PNG renders, and optional STL meshes

## Setup

```bash
cd lsystem-executor
python3 -m venv .venv && source .venv/bin/activate && pip install matplotlib numpy -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/lsystem_render.py --help
```

## Dependencies

- `matplotlib`
- `numpy`
