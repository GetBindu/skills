# scikit-survival

Survival analysis and time-to-event modeling in Python with scikit-survival covering Cox models, Random Survival Forests, Gradient Boosting, Survival SVMs, concordance index, and Brier score.

## What it does

This skill wraps the scikit-survival library, which extends scikit-learn for survival analysis -- the study of time-to-event data with censored observations. It supports Cox proportional hazards models (standard and penalized with elastic net), ensemble methods (Random Survival Forests, Gradient Boosting Survival Analysis), and Survival Support Vector Machines.

Model evaluation includes the concordance index (C-index) for discrimination, the Brier score for calibration, and time-dependent AUC curves. The library also provides Kaplan-Meier and Nelson-Aalen estimators for survival and cumulative hazard functions, as well as tools for handling competing risks and preprocessing survival data.

The demo script serves as a lightweight CLI entrypoint that confirms scikit-survival availability and points to the SKILL.md reference documentation for detailed usage patterns, model selection guidance, and code examples covering the full survival analysis workflow from data preparation through model evaluation.

## Setup

```bash
cd scikit-survival
python3 -m venv .venv && source .venv/bin/activate && pip install scikit-survival numpy pandas -q
```

## Environment variables

None.

## Usage

### Input

```bash
python3 scripts/demo.py --format json
```

### Output

```
{
  "skill": "scikit-survival",
  "status": "available",
  "description": "Survival analysis",
  "note": "See SKILL.md and references/ for comprehensive documentation"
}
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--format`, `-f` | Output format (`summary` or `json`) | `summary` |

## Dependencies

- `scikit-survival`
- `numpy`
- `pandas`

## Tested with

- **Direct script run:** pass (reports status and points to SKILL.md documentation)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict (excerpt)

> The agent loaded the scikit-survival skill, confirmed availability via the demo entrypoint, and referenced the SKILL.md documentation for survival analysis workflows including Cox regression, ensemble models, and evaluation with concordance index and Brier score.

## Fix notes

- Cleaned `__pycache__/` directory
- Applied 1 ruff lint fix
