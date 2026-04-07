# scientific-visualization

Publication-ready scientific figure generation with multi-panel layouts, significance annotations, colorblind-safe palettes, and journal-specific formatting (Nature/Science/Cell/PLOS/ACS/IEEE).

## What it does

This skill produces publication-quality figures suitable for journal submission. It includes a demo CLI that generates histogram plots from synthetic or upstream data, a figure export module that saves figures in multiple formats (PDF, PNG, EPS, SVG, TIFF) with journal-specific DPI and size requirements, and a style presets module with pre-configured matplotlib styles for Nature, Science, Cell, and other journals.

The style presets provide colorblind-friendly palettes (Okabe-Ito, Wong, Paul Tol variants), journal-compliant figure dimensions, font sizes, and axis formatting. The figure export module can check figure size compliance against journal specifications and save with the correct resolution for line art, photos, or combination figures.

The demo script accepts a `--query` topic, generates a distribution snapshot histogram, and exports it via the figure export pipeline. It also supports upstream data injection via `--input-json` for integration with other skills in agent workflows.

## Setup

```bash
cd scientific-visualization
python3 -m venv .venv && source .venv/bin/activate && pip install matplotlib seaborn numpy -q
```

## Environment variables

None.

## Usage

### Input

```bash
python3 scripts/demo.py --query "SSTR2 NETs DOTATATE uptake" --format json
```

### Output

```
{
  "topic": "SSTR2 NETs DOTATATE uptake",
  "data_source": "synthetic",
  "n": 200,
  "output_base": "/Users/you/.scienceclaw/figures/sviz_3281047263",
  "files": [
    "/Users/you/.scienceclaw/figures/sviz_3281047263.png",
    "/Users/you/.scienceclaw/figures/sviz_3281047263.pdf"
  ],
  "formats": ["png", "pdf"]
}
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--query`, `-q` | Topic to visualize | `"scientific figure"` |
| `--format`, `-f` | Output format (`summary` or `json`) | `summary` |
| `--output` | Output base path (no extension) | `~/.scienceclaw/figures/` |
| `--title` | Figure title override | derived from query |
| `--input-json` | JSON with upstream data `{"data": [...]}` | `""` |
| `--describe-schema` | Print expected input-json schema and exit | off |

## Scripts

| Script | Purpose |
|--------|---------|
| `demo.py` | CLI entrypoint -- generates histogram and exports via figure_export |
| `figure_export.py` | Save figures in multiple formats, journal-specific export, size compliance checks |
| `style_presets.py` | Pre-configured matplotlib styles and colorblind-friendly palettes |

## Dependencies

- `matplotlib`
- `seaborn`
- `numpy`

## Tested with

- **Direct script run:** pass (generates PNG + PDF to `~/.scienceclaw/figures/`)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict (excerpt)

> The agent successfully invoked the scientific-visualization skill, generated a distribution snapshot figure for the given query, and returned valid JSON with file paths to the exported PNG and PDF outputs.

## Fix notes

- Fixed mutable default argument in `figure_export.py` (`formats` parameter)
- Cleaned `__pycache__/` directory
- Applied ruff lint and format fixes
