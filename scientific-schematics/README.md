# scientific-schematics

Generate publication-quality scientific diagrams and schematics using Nano Banana Pro AI with smart iterative refinement.

## What it does

This skill generates scientific diagrams from natural language descriptions using the Nano Banana Pro AI model via OpenRouter. It supports a wide range of diagram types including CONSORT flowcharts, signaling pathways, system architectures, circuit diagrams, and more.

The generation pipeline includes smart iterative refinement: it only regenerates if the quality score (evaluated by Gemini 3 Pro) falls below a threshold appropriate for the target document type. Journal papers demand the highest quality (8.5/10), while presentations accept a lower threshold (6.5/10) for faster turnaround.

Three scripts are provided: `generate_schematic.py` is the main CLI entry point, `generate_schematic_ai.py` is the underlying AI generation engine, and `example_usage.sh` demonstrates common invocations.

## Setup

```bash
cd scientific-schematics
python3 -m venv .venv && source .venv/bin/activate
```

No pip dependencies beyond standard library (uses subprocess to call the AI backend).

## Environment variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENROUTER_API_KEY` | OpenRouter API key for AI generation | Yes |

## Usage

### Input

```bash
python3 scripts/generate_schematic.py "CONSORT participant flowchart" -o flowchart.png --doc-type journal
python3 scripts/generate_schematic.py "Transformer architecture diagram" -o arch.png --doc-type poster
python3 scripts/generate_schematic.py "MAPK signaling pathway" -o pathway.png --doc-type presentation
```

### Output

```
Generating schematic: CONSORT participant flowchart
Document type: journal (threshold: 8.5/10)
Iteration 1: quality score 8.7/10 - PASS
Saved to: flowchart.png
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `prompt` | Description of the diagram to generate (positional) | -- |
| `-o`, `--output` | Output file path (required) | -- |
| `--doc-type` | Document type for quality threshold: `journal`, `conference`, `poster`, `presentation`, `report`, `grant`, `thesis`, `preprint`, `default` | `default` |
| `--iterations` | Maximum refinement iterations (max 2) | `2` |
| `--api-key` | OpenRouter API key (alternative to env var) | None |
| `-v`, `--verbose` | Verbose output | off |

## Dependencies

- None (standard library only; uses subprocess to invoke AI backend)

## Tested with

- **Direct script run:** requires `OPENROUTER_API_KEY`; generates PNG output
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict (excerpt)

> The skill loaded successfully and the agent understood how to generate scientific diagrams via natural language prompts. The document-type quality thresholds and iterative refinement system were correctly described and invoked.

## Fix notes

- Cleaned `__pycache__/` directories
- Applied lint fixes (16 issues fixed)
