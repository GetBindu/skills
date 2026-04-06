# scikit-survival

Survival analysis and time-to-event modeling — Cox models, Random Survival Forests, Gradient Boosting, Survival SVMs.

## What it does

Comprehensive toolkit for survival analysis using scikit-survival. Covers Cox proportional hazards, Random Survival Forests, Gradient Boosted survival models, Survival SVMs, concordance index evaluation, Brier score, competing risks, and Kaplan-Meier estimation. Designed for clinical trials, reliability engineering, and customer churn modeling.

## Setup

```bash
cd scikit-survival
python3 -m venv .venv && source .venv/bin/activate && pip install scikit-survival numpy pandas -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/demo.py --format summary
```

## Dependencies

- `scikit-survival`, `numpy`, `pandas`

## Tested with

- **Direct script run:** pass (--help works)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict

> Agent loaded the skill and described Cox models, RSF, gradient boosting survival models, evaluation metrics, and clinical trial use cases.

## Fix notes

- Cleaned `__pycache__/`, 1 ruff lint fix
