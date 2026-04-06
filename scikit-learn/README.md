# scikit-learn

Machine learning in Python — classification, regression, clustering, dimensionality reduction, pipelines, and hyperparameter tuning.

## What it does

Comprehensive scikit-learn reference skill covering supervised learning (SVM, Random Forest, Gradient Boosting, logistic regression), unsupervised learning (K-Means, DBSCAN, PCA, t-SNE), model evaluation (cross-validation, GridSearchCV), preprocessing (scaling, encoding, imputation), and pipeline construction. Includes working scripts for classification pipelines and clustering analysis.

## Setup

```bash
cd scikit-learn
python3 -m venv .venv && source .venv/bin/activate && pip install scikit-learn numpy pandas -q
```

## Environment variables

None.

## Scripts

- `demo.py` — Quick demo with --format summary/json
- `classification_pipeline.py` — Full classification workflow
- `clustering_analysis.py` — Optimal K-finding, silhouette analysis, multiple algorithms

## Dependencies

- `scikit-learn`, `numpy`, `pandas`

## Tested with

- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict

> Agent described all ML algorithm families, preprocessing techniques, pipeline construction, and hyperparameter tuning workflows. Noted this is ideal for classical ML on structured/tabular data.

## Fix notes

- Fixed mutable `range()` defaults in clustering_analysis.py (B008)
- Cleaned `__pycache__/`, 8 ruff lint fixes
