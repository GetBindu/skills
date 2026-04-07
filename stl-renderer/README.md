# stl-renderer

Render publication-quality PNG views of any binary STL file — isometric (3-D perspective), top-down XY projection, and XZ cross-section at Y midpoint.

## Setup

```bash
cd stl-renderer
python3 -m venv .venv && source .venv/bin/activate && pip install matplotlib mpl_toolkits numpy struct utils -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/stl_renderer.py --help
```

## Dependencies

- `matplotlib`
- `mpl_toolkits`
- `numpy`
- `struct`
- `utils`
