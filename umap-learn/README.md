# umap-learn

UMAP (Uniform Manifold Approximation and Projection) dimensionality reduction for visualization and clustering preprocessing.

## What it does

UMAP is a nonlinear dimensionality reduction technique that projects high-dimensional data into 2D or 3D while preserving both local and global structure. It scales better than t-SNE, supports supervised/semi-supervised variants, and is ideal for visualizing embeddings, preprocessing for HDBSCAN clustering, and exploring high-dimensional feature spaces.

The included `demo.py` accepts a `--query` topic, generates a synthetic 12-dimensional clustered dataset whose cluster labels reflect the query domain (e.g., protein structures → alpha-helical / beta-sheet / membrane / …), runs UMAP to project to 2D, and reports cluster separation and per-cluster statistics.

## Setup

```bash
cd umap-learn
python3 -m venv .venv && source .venv/bin/activate && pip install umap-learn scikit-learn numpy -q
```

## Environment variables

None. Pure local library.

## Usage

### Input
```bash
python3 scripts/demo.py --query "protein structures" --format summary
```

### Output
```
============================================================
UMAP — 2D Embedding: 'protein structures'
============================================================
Samples     : 120  (12D → 2D)
Clusters    : 5  (alpha-helical, beta-sheet, disordered, membrane, soluble)
Avg cluster separation: 21.9925
Cluster stats:
  alpha-helical             n=24  spread=0.466
  beta-sheet                n=24  spread=0.422
  disordered                n=24  spread=0.463
  membrane                  n=24  spread=0.468
  soluble                   n=24  spread=0.444
============================================================
```

### Other input modes
```bash
# Different query domain
python3 scripts/demo.py --query "scientific topics"

# JSON output
python3 scripts/demo.py --query "gene expression" --format json

# Upstream input (pipe real vectors via --input-json)
python3 scripts/demo.py --input-json '{"vectors": [[...], [...]], "labels": ["a", "b"]}'
```

## CLI flags

| Flag | Description |
|------|-------------|
| `--query` / `-q` | Topic used to seed synthetic cluster names |
| `--input-json` | JSON string with `vectors` (2D array) and `labels` (string list) for real data |
| `--format` / `-f` | `summary` or `json` |

## Dependencies

- `umap-learn`
- `scikit-learn`
- `numpy`

## Tested with

- **Direct script run:** ✅ Embedded 120 samples (12D → 2D), 5 protein-structure clusters, avg separation 21.99
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions, executed `demo.py --query "scientific topics" --format summary`, captured real output (120 samples, 4 clusters, avg separation 24.33), and explained UMAP's key advantages: preserves local+global structure, scales better than t-SNE, supports supervised learning, works with various distance metrics, sklearn-compatible. (First Agno run hit a 30s timeout; agent self-corrected by increasing timeout.)

### Agno agent verdict (excerpt)
> UMAP is a dimensionality reduction technique that reduces high-dimensional data into 2D/3D for visualization or lower dimensions for ML preprocessing. Preserves both local and global structure better than t-SNE, scales efficiently to large datasets, supports supervised/semi-supervised learning, works with various distance metrics, and follows sklearn conventions. The demo transformed 120 samples from 12 dimensions → 2 dimensions, identified 4 clusters with avg separation 24.33, balanced (30 samples each) with tight spread (0.55-0.64), demonstrating UMAP's ability to organize scientific data into interpretable 2D clusters while preserving meaningful structure.

## See also

- [`references/api_reference.md`](references/api_reference.md) — full UMAP API reference (parameters, metrics, supervised mode)

## Fix notes

- Removed stray `__pycache__/`
- Script was already functional — no code changes needed
