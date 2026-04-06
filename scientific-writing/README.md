# scientific-writing

Scientific manuscript writing in IMRAD structure with citation styles (APA/AMA/Vancouver) and reporting guidelines (CONSORT/STROBE/PRISMA).

## What it does

Core skill for deep research and writing. Writes scientific manuscripts in full paragraphs (never bullet points) using a two-stage process: (1) section outlines with key points via research-lookup, then (2) conversion to flowing prose. Supports multiple citation styles, reporting guidelines, and figure/table integration.

## Setup

```bash
cd scientific-writing
```

No heavy dependencies for the demo script.

## Environment variables

None.

## Usage

```bash
python3 scripts/demo.py --mode outline --query "CRISPR gene therapy clinical trials"
python3 scripts/demo.py --mode synthesis --format json
```

## Dependencies

None (standard library for demo).

## Tested with

- **Direct script run:** pass (--help, --mode outline/hypothesis/synthesis)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict

> Agent loaded the skill and described IMRAD writing workflow, citation management, and reporting guideline support.

## Fix notes

- Cleaned `__pycache__/`, applied ruff format
