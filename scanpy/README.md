# scanpy

Standard single-cell RNA-seq analysis pipeline — QC, normalization, dimensionality reduction, clustering, differential expression, and visualization.

## What it does

Scanpy is the standard Python toolkit for scRNA-seq analysis built on AnnData. This skill provides two CLI scripts plus comprehensive reference docs covering the full workflow: load data → QC → normalize → select features → PCA → neighborhood graph → UMAP/t-SNE → cluster (Leiden) → find marker genes → annotate cell types → save.

## Setup

```bash
cd scanpy
python3 -m venv .venv && source .venv/bin/activate && pip install scanpy -q
```

## Environment variables

None. Pure local library.

## Usage

### Input — QC analysis (main script)
```bash
python3 scripts/qc_analysis.py input_data.h5ad --mt-threshold 5 --min-genes 200
```

### Output
Produces `qc_filtered.h5ad` with filtered cells and genes, plus QC diagnostic plots (unless `--skip-plots`).

### Help output
```
usage: qc_analysis.py [-h] [--output OUTPUT] [--mt-threshold MT_THRESHOLD]
                      [--min-genes MIN_GENES] [--min-cells MIN_CELLS]
                      [--skip-plots]
                      input

positional arguments:
  input                 Input file (h5ad, 10X mtx, csv, etc.)

optional arguments:
  --output OUTPUT       Output file name (default: qc_filtered.h5ad)
  --mt-threshold        Max mitochondrial percentage (default: 5)
  --min-genes           Min genes per cell (default: 200)
  --min-cells           Min cells per gene (default: 3)
  --skip-plots          Skip generating QC plots
```

## Scripts

| Script | Purpose |
|--------|---------|
| `qc_analysis.py` | Quality control: calculates metrics, generates diagnostic plots, filters low-quality cells/genes |
| `demo.py` | Placeholder for basic workflow demonstration (returns scanpy version info) |

## CLI flags (qc_analysis.py)

| Flag | Description | Default |
|------|-------------|---------|
| `input` | Input file: `.h5ad`, 10X `.mtx`, `.csv`, etc. | required |
| `--output` | Output filtered file path | `qc_filtered.h5ad` |
| `--mt-threshold` | Max mitochondrial gene % | 5 |
| `--min-genes` | Min genes per cell | 200 |
| `--min-cells` | Min cells per gene | 3 |
| `--skip-plots` | Skip generating QC plots | false |

## Dependencies

- `scanpy` (includes anndata, numpy, scipy, matplotlib, pandas, seaborn as transitive deps)

## Tested with

- **`demo.py --format json`:** ✅ Returns clean JSON (scanpy imported successfully)
- **`qc_analysis.py --help`:** ✅ All 5 flags documented with defaults
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions, ran `qc_analysis.py --help`, described the 9-step standard workflow (load → QC → normalize → features → PCA → UMAP → cluster → markers → annotate), both scripts' roles, and QC parameters

### Agno agent verdict (excerpt)
> Standard scRNA-seq workflow: load data (10X/h5ad/CSV) → QC (filter low-quality cells by gene count, total counts, mitochondrial %) → normalize (10K counts/cell, log-transform) → feature selection (~2K HVGs) → PCA → neighborhood graph → UMAP/t-SNE → Leiden clustering → marker gene identification → cell type annotation → save. The qc_analysis.py script automates the QC step with configurable thresholds (mt-threshold 5%, min-genes 200, min-cells 3) and diagnostic plots.

## See also

- `references/standard_workflow.md` — complete Scanpy workflow code walkthrough
- `references/api_reference.md` — key function signatures and parameters
- `references/plotting_guide.md` — visualization recipes

## Fix notes

- Fixed `skill_name` undefined bug in `demo.py` (replaced with `"scanpy"`)
- Removed stray `__pycache__/`
- `qc_analysis.py` unchanged (200 lines, already functional)
