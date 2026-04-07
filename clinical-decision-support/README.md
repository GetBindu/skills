# clinical-decision-support

Generate professional clinical decision support (CDS) documents for pharmaceutical and clinical research settings, including patient cohort analyses (biomarker-stratified with outcomes) and treatment recommendation reports (evidence-based guidelines with decision algorithms).

## Setup

```bash
cd clinical-decision-support
python3 -m venv .venv && source .venv/bin/activate && pip install lifelines matplotlib numpy pandas scipy -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/generate_survival_analysis.py --help
```

## Dependencies

- `lifelines`
- `matplotlib`
- `numpy`
- `pandas`
- `scipy`
