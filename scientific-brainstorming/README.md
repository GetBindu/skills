# scientific-brainstorming

Creative research ideation assistant for generating novel scientific hypotheses and experimental approaches.

## What it does

This skill provides a framework for scientific brainstorming and creative research ideation. It helps researchers generate novel hypotheses, identify unexplored research directions, and propose experimental approaches by combining knowledge from multiple scientific domains.

The demo script confirms the skill is loaded and available, then directs users to the full SKILL.md documentation and reference materials for comprehensive usage. The skill is designed to be used primarily through an AI agent, which reads the SKILL.md and reference documents to provide structured ideation support.

## Setup

```bash
cd scientific-brainstorming
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
scientific-brainstorming - Scientific ideation assistant
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

> The skill loaded and executed correctly. The agent was able to read the SKILL.md and reference materials to provide structured scientific brainstorming guidance covering hypothesis generation and experimental design.

## Fix notes

- Cleaned `__pycache__/` directories
- Applied lint fixes
