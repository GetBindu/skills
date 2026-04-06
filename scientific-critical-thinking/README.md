# scientific-critical-thinking

Evaluate scientific claims and evidence using GRADE and Cochrane frameworks for rigorous critical analysis.

## What it does

This skill provides structured frameworks for evaluating scientific claims, experimental evidence, and research quality. It applies established methodologies such as the GRADE (Grading of Recommendations, Assessment, Development and Evaluations) system and Cochrane review standards to systematically assess the strength of scientific evidence.

The demo script confirms the skill is loaded and available, then directs users to the full SKILL.md documentation and reference materials. The skill is designed to be used primarily through an AI agent, which reads the SKILL.md and references to guide rigorous evidence evaluation, bias detection, and logical fallacy identification.

## Setup

```bash
cd scientific-critical-thinking
python3 -m venv .venv && source .venv/bin/activate
```

No external dependencies required for the basic demo.

## Environment variables

None.

## Usage

### Input

```bash
python3 scripts/demo.py
python3 scripts/demo.py --format json
```

### Output

```
======================================================================
scientific-critical-thinking - Critical thinking for science
======================================================================
Status: available

Note: See SKILL.md and references/ for comprehensive documentation
======================================================================
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--format`, `-f` | Output format: `summary` or `json` | `summary` |

## Dependencies

- None (standard library only)

## Tested with

- **Direct script run:** pass (outputs skill status and pointer to docs)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict (excerpt)

> The skill loaded correctly and the agent was able to use the GRADE and Cochrane frameworks documented in SKILL.md to evaluate scientific claims, assess evidence quality, and identify potential biases in study design.

## Fix notes

- Cleaned `__pycache__/` directories
- Applied lint fixes
