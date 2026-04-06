# scientific-slides

Build research presentations with AI-generated slide images, supporting both PDF and PowerPoint workflows.

## What it does

This skill generates presentation slides and visuals using Nano Banana Pro AI via OpenRouter. It supports two modes: full-slide generation (complete slides with title, content, and visuals for a PDF-based workflow) and visual-only generation (just the image or figure, for embedding into PowerPoint slides).

The skill also includes utilities for converting between formats. `slides_to_pdf.py` compiles slide images into a PDF presentation, `pdf_to_images.py` extracts pages from an existing PDF into individual images, and `validate_presentation.py` checks a set of slide images for consistency and quality. Reference images can be attached for context-aware generation.

Five scripts are provided: `generate_slide_image.py` (main CLI), `generate_slide_image_ai.py` (AI engine), `pdf_to_images.py`, `slides_to_pdf.py`, and `validate_presentation.py`.

## Setup

```bash
cd scientific-slides
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
# Generate a full slide (PDF workflow)
python3 scripts/generate_slide_image.py "Title: Introduction\nKey points: AI, ML, Deep Learning" -o slide_01.png

# Generate visual only (PPT workflow)
python3 scripts/generate_slide_image.py "Neural network diagram" -o figure.png --visual-only

# With reference images attached
python3 scripts/generate_slide_image.py "Create a slide about this data" -o slide.png --attach chart.png

# Convert slides to PDF
python3 scripts/slides_to_pdf.py slides/ -o presentation.pdf
```

### Output

```
Generating slide: Title: Introduction
Mode: full slide
Iteration 1: quality score 7.8/10 - PASS
Saved to: slide_01.png
```

## CLI flags

### generate_slide_image.py

| Flag | Description | Default |
|------|-------------|---------|
| `prompt` | Description of the slide or visual (positional) | -- |
| `-o`, `--output` | Output file path (required) | -- |
| `--attach` | Attach reference image(s) as context (repeatable) | None |
| `--visual-only` | Generate just the visual/figure (for PPT workflow) | off |
| `--iterations` | Maximum refinement iterations (max 2) | `2` |
| `--api-key` | OpenRouter API key (alternative to env var) | None |
| `-v`, `--verbose` | Verbose output | off |

## Dependencies

- None (standard library only; uses subprocess to invoke AI backend)

## Tested with

- **Direct script run:** requires `OPENROUTER_API_KEY`; generates PNG output
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict (excerpt)

> The skill loaded correctly and the agent understood both the full-slide and visual-only workflows. It correctly described how to generate multiple slides and compile them into a PDF presentation.

## Fix notes

- Cleaned `__pycache__/` directories
- Applied lint fixes (19 issues fixed)
