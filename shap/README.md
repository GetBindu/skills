# shap

Model interpretability using SHAP (SHapley Additive exPlanations) — feature importance, waterfall/beeswarm/bar plots, bias analysis.

## Setup

```bash
cd shap && python3 -m venv .venv && source .venv/bin/activate && pip install shap numpy scikit-learn -q
```

## Usage

```bash
python3 scripts/demo.py --help
python3 scripts/demo.py --example tree --format json
```

## Dependencies

`shap`, `numpy`, `scikit-learn`

## Tested with

- **Agno (dry-run):** ✅
