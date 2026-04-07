# scikit-learn

Machine learning in Python with scikit-learn covering classification, regression, clustering, dimensionality reduction, pipelines, and hyperparameter tuning.

## What it does

This skill provides three CLI-ready scripts for common machine learning workflows. The **demo** script fits a log-log linear regression on synthetic or upstream data, returning R-squared, slope, intercept, and a scaling exponent (alpha). It accepts upstream data via `--input-json` for integration with other skills in agent pipelines.

The **classification pipeline** script demonstrates a complete supervised learning workflow: preprocessing with ColumnTransformer (numeric scaling, categorical one-hot encoding), model comparison via 5-fold cross-validation (Logistic Regression, Random Forest, Gradient Boosting), hyperparameter tuning with GridSearchCV, and full test-set evaluation with accuracy, precision, recall, F1, ROC AUC, confusion matrix, and feature importances.

The **clustering analysis** script compares K-Means, Agglomerative Clustering, Gaussian Mixture, and DBSCAN. It includes an elbow method and silhouette analysis for optimal K selection, evaluation with silhouette score, Calinski-Harabasz index, and Davies-Bouldin index, plus PCA-based 2D visualization of cluster assignments.

## Setup

```bash
cd scikit-learn
python3 -m venv .venv && source .venv/bin/activate && pip install scikit-learn numpy pandas matplotlib -q
```

## Environment variables

None.

## Usage

### Input

```bash
python3 scripts/demo.py --query "SSTR2 binding potency scaling" --format json
```

### Output

```
{
  "topic": "SSTR2 binding potency scaling",
  "model": "LinearRegression",
  "data_source": "synthetic",
  "n_observations": 40,
  "x_label": "log10(concentration)",
  "y_label": "log10(response)",
  "coefficients": {"intercept": 3.456, "slope": -1.412},
  "r2": 0.998,
  "r_squared": 0.998,
  "alpha": 1.412,
  "scaling_exponent": 1.412
}
```

## CLI flags

### demo.py

| Flag | Description | Default |
|------|-------------|---------|
| `--query`, `-q` | Topic to analyse | `"general trend"` |
| `--format`, `-f` | Output format (`summary` or `json`) | `summary` |
| `--input-json` | JSON with upstream data `{"rows": [{"x":..,"y":..}]}` | `""` |
| `--describe-schema` | Print expected input-json schema and exit | off |

### classification_pipeline.py

Run directly with `python3 scripts/classification_pipeline.py` (uses Breast Cancer Wisconsin dataset as example).

### clustering_analysis.py

Run directly with `python3 scripts/clustering_analysis.py` (uses Iris dataset and synthetic blobs as examples).

## Scripts

| Script | Purpose |
|--------|---------|
| `demo.py` | CLI entrypoint -- log-log linear regression with synthetic or upstream data |
| `classification_pipeline.py` | Full classification workflow: preprocessing, model comparison, tuning, evaluation |
| `clustering_analysis.py` | Clustering comparison: K-Means, Agglomerative, GMM, DBSCAN with evaluation |

## Dependencies

- `scikit-learn`
- `numpy`
- `pandas`
- `matplotlib` (for clustering visualization)

## Tested with

- **Direct script run:** pass (demo returns valid JSON; classification and clustering scripts run end-to-end)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict (excerpt)

> The agent invoked the scikit-learn skill with a binding potency query, received a valid regression result with R-squared and scaling exponent, and confirmed the JSON output matched the expected schema for downstream pipeline integration.

## Fix notes

- Fixed mutable `range()` default arguments in `clustering_analysis.py` (`k_range` parameter in two functions)
- Cleaned `__pycache__/` directory
- Applied 8 ruff lint fixes
