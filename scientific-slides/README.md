# scientific-slides

Build slide decks for research talks — PowerPoint and LaTeX Beamer. Structure, design, timing, and visual validation.

## What it does

5 scripts: `generate_slide_image.py` (template-based), `generate_slide_image_ai.py` (AI-powered), `slides_to_pdf.py` (PPTX→PDF), `pdf_to_images.py` (PDF→PNG), `validate_presentation.py` (check compliance). Covers conference talks, seminar presentations, thesis defense, research updates.

## Setup

```bash
cd scientific-slides
python3 -m venv .venv && source .venv/bin/activate && pip install python-pptx pillow -q
```

## Env vars

`GEMINI_API_KEY` — for AI-powered slide image generation (optional)

## Usage

```bash
python3 scripts/validate_presentation.py --help
python3 scripts/slides_to_pdf.py presentation.pptx
```

## Tested with

- **`--help`:** ✅
- **Agno (dry-run):** ✅ Loads successfully
