# seaborn

Statistical visualization with pandas integration — distributions, relationships, categorical comparisons with attractive defaults.

## What it does

Reference skill for the seaborn library. Covers distribution plots (histplot, kdeplot, ecdfplot), relational plots (scatterplot, lineplot), categorical plots (boxplot, violinplot, swarmplot, barplot), matrix plots (heatmap, clustermap), pair plots, and FacetGrid for multi-panel layouts. Built on matplotlib with attractive defaults.

## Setup

```bash
cd seaborn
python3 -m venv .venv && source .venv/bin/activate && pip install seaborn matplotlib numpy pandas -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/demo.py --format summary
```

## Dependencies

- `seaborn`, `matplotlib`, `numpy`, `pandas`

## Tested with

- **Direct script run:** pass (graceful error when seaborn not installed)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict

> Agent loaded the skill and described all plot types, FacetGrid usage, and the distinction from plotly (interactive) and scientific-visualization (publication).

## Fix notes

- Fixed `skill_name` undefined bug in demo.py
- Cleaned `__pycache__/`, ruff lint fixes
