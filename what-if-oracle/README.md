# what-if-oracle

Structured scenario analysis generator for exploring uncertain futures through multi-branch possibility mapping.

## What it does

Takes a speculative "what if" question and produces a structured JSON template for multi-branch scenario analysis using the **0·IF·1 framework**. The template is a scaffold for an LLM agent to fill in with actual probabilities, narratives, assumptions, triggers, and insights.

Three operating modes:
- **quick** (Ω/α/Δ) — 3 branches: best case, likely case, worst case
- **deep** (Ω/α/Δ/Ψ/Φ/∞) — 6 branches including wild cards, contrarian, and second-order effects
- **reverse** (α/Ω/Φ) — backward mapping from a desired outcome

Each branch asks for: probability, narrative, key assumptions, trigger conditions, consequences timeline (immediate / short-term / long-term), required responses, and the "1% insight most analysis overlooks".

## Setup

No setup required — uses only Python stdlib.

## Environment variables

None.

## Usage

### Input
```bash
python3 scripts/analyze.py --question "What if oil prices double in 6 months?" --mode quick --format summary
```

### Output (summary mode)
```
======================================================================
WHAT-IF ORACLE — QUICK MODE
======================================================================
Question: What if oil prices double in 6 months?
Framework: 0·IF·1
Branches: 3

  Ω Best Case: Maximum upside scenario
  α Likely Case: Most probable path
  Δ Worst Case: Maximum downside scenario

Run with --format json for full structured template.
Feed the JSON to an LLM agent to fill in the analysis fields.
```

### Other input modes
```bash
# Deep 6-branch analysis
python3 scripts/analyze.py --question "What if we launch before Q4?" --mode deep

# Full JSON template (for feeding to an LLM)
python3 scripts/analyze.py --question "What if interest rates hit 8%?" --format json

# Reverse mode (backward from desired outcome)
python3 scripts/analyze.py --question "What if we 10x revenue?" --mode reverse
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--question` / `-q` | The what-if question (required) | — |
| `--mode` / `-m` | `quick` (3), `deep` (6), or `reverse` (3) | `quick` |
| `--format` / `-f` | `json` or `summary` | `json` |

## Framework details

**0·IF·1**
- `0` = unexpressed potential state
- `1` = expressed current reality
- `IF` = conditional transformation

**Golden ratio principle**: allocate 61.8% attention to primary scenario, 38.2% to alternatives — matching natural branching patterns.

## Dependencies

Python stdlib only.

## Tested with

- **Direct script run (quick mode):** ✅ Returns 3 branches with full JSON scaffold
- **Direct script run (deep mode summary):** ✅ Lists all 6 branches with symbols and labels
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions, executed with test question about AI replacing coding jobs, explained 4-phase process, 5 operating modes, and golden ratio principle

### Agno agent verdict (excerpt)
> The script mapped your question into three branches for quick analysis: Ω Best Case, α Likely Case, Δ Worst Case. The output shows the framework is ready to accept deeper LLM-powered analysis — you can feed the JSON template to an AI agent to flesh out probabilities, narratives, assumptions, and hidden insights. The framework allocates attention using Fibonacci proportions: 61.8% to primary scenario, 38.2% to alternatives.
