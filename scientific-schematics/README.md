# scientific-schematics

Create publication-quality scientific diagrams using AI with iterative refinement. Uses Gemini 3 Pro for quality review.

## What it does

Two generation modes: `generate_schematic.py` (template-based) and `generate_schematic_ai.py` (AI-powered with Gemini quality review). Specializes in neural network architectures, system diagrams, flowcharts, biological pathways, and complex scientific visualizations.

## Setup

```bash
cd scientific-schematics
python3 -m venv .venv && source .venv/bin/activate && pip install requests pillow -q
```

## Env vars

`GEMINI_API_KEY` — for AI-powered generation + quality review (optional for template mode)

## Usage

```bash
python3 scripts/generate_schematic.py --help
python3 scripts/generate_schematic.py --type "neural-network" --description "Transformer encoder"
```

## Tested with

- **`--help`:** ✅
- **Agno (Claude Haiku 4.5):** ✅ Described 4-step workflow (describe → generate → review → output), 6 specializations
