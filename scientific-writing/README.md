# scientific-writing

Scientific manuscript writing assistant that generates IMRAD-structured scaffolds, hypothesis templates, and synthesis frameworks with support for citation styles (APA/AMA/Vancouver) and reporting guidelines (CONSORT/STROBE/PRISMA).

## What it does

This skill provides structured writing scaffolds for scientific manuscripts. It operates in three modes: **outline** generates a full IMRAD (Introduction, Methods, Results, and Discussion) manuscript template with section-by-section prompts; **hypothesis** produces a structured hypothesis template with mechanism, prediction, confirming and refuting evidence fields; and **synthesis** creates a scaffold for integrating observations into a coherent narrative with uncertainty and next-step planning.

The tool is designed as a writing utility for autonomous agent loops. It does not assert factual claims about the world -- it produces templates and scaffolds grounded only in the provided query string. Output includes machine-readable JSON with a timestamp, mode, and the generated markdown content.

The SKILL.md reference documentation covers full manuscript writing workflows including citation formatting (APA, AMA, Vancouver, Chicago, IEEE), reporting guidelines for clinical trials (CONSORT), observational studies (STROBE), and systematic reviews (PRISMA).

## Setup

```bash
cd scientific-writing
python3 -m venv .venv && source .venv/bin/activate
```

No heavy dependencies are required for the demo script (standard library only).

## Environment variables

None.

## Usage

### Input

```bash
python3 scripts/demo.py --query "CRISPR base editing efficiency" --mode outline --format json
```

### Output

```
{
  "skill": "scientific-writing",
  "status": "ok",
  "mode": "outline",
  "topic": "CRISPR base editing efficiency",
  "generated_at_utc": "2026-04-06T12:00:00Z",
  "note": "Template/scaffold only; does not assert factual claims.",
  "markdown": "## Title\nCRISPR base editing efficiency\n\n## Abstract (template)\n..."
}
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--query`, `-q` | Topic/prompt for the writing scaffold | `""` |
| `--mode`, `-m` | Scaffold type: `outline`, `hypothesis`, or `synthesis` | `outline` |
| `--format`, `-f` | Output format (`summary` or `json`) | `summary` |

## Dependencies

- None (standard library only for demo.py)

## Tested with

- **Direct script run:** pass (all three modes produce valid scaffolds)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict (excerpt)

> The agent invoked the scientific-writing skill in outline mode, received a structured IMRAD manuscript template, and confirmed the JSON output contained all expected fields including the markdown scaffold and status metadata.

## Fix notes

- Cleaned `__pycache__/` directory
- Applied ruff lint and format fixes
