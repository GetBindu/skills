# scholar-evaluation

Evaluate scholarly work using ScholarEval — 8 research quality dimensions with weighted scoring and visual reports.

## What it does

Calculates aggregate scores from dimension ratings (1-5 scale) across: problem formulation, literature review, methodology, data collection, analysis, results, writing, and citations. Default weights emphasize methodology (20%) and problem/literature/analysis (15% each).

## Setup

No dependencies — stdlib only.

## Usage

```bash
python3 scripts/calculate_scores.py --scores scores.json
python3 scripts/calculate_scores.py -i  # interactive
```

## Tested with

- **Direct run:** ✅ Visual bar chart + weighted breakdown
- **Agno:** ✅ All 8 dimensions, default weights identified
