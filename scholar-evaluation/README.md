# scholar-evaluation

Systematically evaluate scholarly work using the ScholarEval framework with quantitative scoring across 8 research quality dimensions.

## What it does

Provides structured evaluation of academic papers, research proposals, and literature reviews across 8 weighted dimensions: problem formulation (15%), literature review (15%), methodology (20%), data collection (10%), analysis (15%), results (10%), writing (10%), and citations (5%). Generates ASCII bar charts, quality level assessments, strengths/weaknesses analysis, and actionable recommendations.

Quality levels range from "Exceptional" (4.5-5.0, top-tier publication ready) to "Poor" (0-2.0, complete revision needed).

## Setup

No external dependencies — uses Python standard library only.

```bash
cd scholar-evaluation
```

## Environment variables

None required.

## Usage

### From JSON file
```bash
echo '{"problem_formulation": 4.5, "literature_review": 4.0, "methodology": 3.5, "data_collection": 4.0, "analysis": 3.5, "results": 4.0, "writing": 4.5, "citations": 4.0}' > scores.json
python3 scripts/calculate_scores.py --scores scores.json
```

### Output
```
======================================================================
SCHOLAREVAL SCORE REPORT
======================================================================

Overall Score: 3.95 / 5.00
Quality Level: Good
Assessment: Major revisions required, promising work

======================================================================
DIMENSION SCORES
======================================================================

  problem_formulation │ █████████████████████████████████████████████ 4.50
  writing             │ █████████████████████████████████████████████ 4.50
  literature_review   │ ████████████████████████████████████████ 4.00
  ...

======================================================================
RECOMMENDATIONS
======================================================================

  Good foundation. Focus on major revisions in weak dimensions.
```

### With custom weights
```bash
python3 scripts/calculate_scores.py --scores scores.json --weights custom_weights.json
```

### Interactive mode
```bash
python3 scripts/calculate_scores.py --interactive
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--scores` | Path to JSON file with dimension scores (1-5) | (required unless `--interactive`) |
| `--weights` | Path to JSON file with dimension weights | default weights |
| `--output` | Path to save report | stdout |
| `--interactive`, `-i` | Interactive score entry mode | off |

## Dependencies

None (Python standard library only).

## Tested with

- **Direct script run:** pass (--help, JSON input, report generation)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict (excerpt)

> The agent loaded the skill, ran the calculator with sample scores, and correctly interpreted the report output. It described all 4 usage modes and noted that no dependencies are required — just Python standard library.

## Fix notes

- Fixed quality level range gaps (scores like 3.95 were falling into "Unknown")
- Removed `__pycache__/`
- Applied ruff lint fixes (import sorting, unnecessary mode args, IOError→OSError)
