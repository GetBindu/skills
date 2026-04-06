# scientific-visualization

Publication-ready scientific figures with multi-panel layouts, significance annotations, colorblind-safe palettes, and journal-specific formatting.

## What it does

Meta-skill for creating journal submission figures (Nature, Science, Cell, etc.). Orchestrates matplotlib/seaborn/plotly with publication styles. Includes figure export utilities with multi-format output (PDF/PNG/SVG/TIFF), style presets for major journals, and a demo script.

## Setup

```bash
cd scientific-visualization
python3 -m venv .venv && source .venv/bin/activate && pip install matplotlib seaborn numpy -q
```

## Environment variables

None.

## Dependencies

- `matplotlib`, `seaborn`, `numpy`

## Tested with

- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict

> Agent described journal-specific formatting requirements for 8+ publishers, the figure export pipeline, style presets, and colorblind-safe palettes.

## Fix notes

- Fixed mutable default arg in figure_export.py (B006)
- Cleaned `__pycache__/`, applied ruff lint/format
