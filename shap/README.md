# shap

Explain machine learning model predictions using SHAP (SHapley Additive exPlanations) feature importance analysis.

## What it does

This skill computes SHAP values to identify which features most influence a model's predictions. Given a research topic via `--query`, it builds a domain-matched synthetic dataset (with recognized domains including scaling laws, drug discovery, gene analysis, and polymer science), trains a GradientBoostingRegressor, and computes SHAP values using TreeExplainer.

The skill can also accept real tabular data via `--input-json`, allowing it to run SHAP analysis on upstream pipeline output. When the `shap` library is not available, it falls back to scikit-learn's permutation importance as an approximation.

Output includes per-feature mean absolute SHAP values, importance percentages, model R-squared, and a ranked feature list. The summary view displays an ASCII bar chart of the top features.

## Setup

```bash
cd shap
python3 -m venv .venv && source .venv/bin/activate && pip install shap numpy scikit-learn -q
```

## Environment variables

None.

## Usage

### Input

```bash
python3 scripts/demo.py --query "neural scaling laws"
python3 scripts/demo.py --query "drug bioavailability" --format json
python3 scripts/demo.py --describe-schema
python3 scripts/demo.py --query "polymer degradation" --input-json '{"rows": [...], "target": "biodegradability"}'
```

### Output

```
============================================================
SHAP - Feature Importance: 'neural scaling laws'
============================================================
Model R2    : 0.9312
Train/Test  : 160/40
Top Features (by mean |SHAP|):
  log_params                      32.1%  ##########
  log_tokens                      24.8%  ########
  log_flops                       18.3%  ######
  data_quality                    12.4%  ####
  architecture_depth               7.2%  ##
============================================================
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--query`, `-q` | Research topic to analyse | `general model` |
| `--format`, `-f` | Output format: `summary` or `json` | `summary` |
| `--describe-schema` | Print expected `--input-json` schema and exit | off |
| `--input-json` | JSON with upstream tabular data (`{rows: [...], target: "col"}`) | empty |

## Dependencies

- `shap`
- `numpy`
- `scikit-learn`

## Tested with

- **Direct script run:** pass (generates SHAP analysis for synthetic domain-matched data)
- **Agno agent (Claude Haiku 4.5):** pass (described all explainer types)

### Agno agent verdict (excerpt)

> The skill executed correctly and produced SHAP feature importance analysis. The agent described all SHAP explainer types (TreeExplainer, KernelExplainer, DeepExplainer) and correctly identified the top features driving predictions in the synthetic dataset.

## Fix notes

- Cleaned `__pycache__/` directories
- Applied lint fix: replaced `dict.keys()` iteration with direct `dict` iteration
