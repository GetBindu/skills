# write-review-paper

Generate structured templates for academic literature reviews and survey papers — reading plans, comparison matrices, writing outlines, and note-taking scaffolds.

## What it does

Helps organize the workflow of writing a literature review from **pre-collected** research materials. The tool does NOT find new papers or generate research ideas — it creates structured JSON templates that scaffold the four phases of a review:

1. **Reading Strategy** — triage papers into P1 (must-read) / P2 (should-read) / P3 (skim) with a standardized note template
2. **Synthesis & Organization** — comparison matrices across papers, timeline analyses, taxonomy structures
3. **Writing Structure** — survey paper or thesis chapter outlines with section recommendations
4. **Writing Tips** — citation density guidelines (intro: 10-20 citations; main survey: 50-100+), transition phrases, anti-patterns

Templates can be generated individually or written as a set of JSON files to an output directory.

## Setup

No setup required — uses only Python stdlib.

```bash
cd write-review-paper
python3 scripts/generate_template.py --help
```

## Environment variables

None.

## Usage

### Input — generate a reading plan
```bash
python3 scripts/generate_template.py --type reading-plan --papers 20
```

### Output
```json
{
  "topic": "[Your Topic]",
  "templates": {
    "reading_plan": {
      "phase": "1_reading_strategy",
      "triage_levels": {
        "P1_must_read": {
          "count": 5,
          "criteria": "Foundational papers, highly cited, directly relevant",
          "action": "Full read with detailed notes"
        },
        "P2_should_read": {
          "count": 10,
          "criteria": "Important context, methodological contributions",
          "action": "Abstract + key sections + notes"
        },
        "P3_skim": {
          "count": 5,
          "criteria": "Peripheral relevance, background context",
          "action": "Abstract + conclusions only"
        }
      },
      "note_template": {
        "paper_id": "[BibTeX key]",
        "title": "",
        "authors_year": "",
        "main_contribution": "",
        "methodology": "",
        "key_findings": [],
        "limitations": "",
        "relevance_to_review": "",
        "connections_to_other_papers": []
      },
      "total_papers": 20
    }
  }
}
```

### Other input modes
```bash
# Comparison matrix
python3 scripts/generate_template.py --type comparison-matrix --topic "CRISPR delivery"

# Writing outline (survey paper format)
python3 scripts/generate_template.py --type writing-outline --format survey

# All templates written as JSON files
python3 scripts/generate_template.py --type all --topic "protein folding" --output-dir ./review
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--type` | `reading-plan`, `comparison-matrix`, `writing-outline`, or `all` | required |
| `--papers` | Total paper count (for reading-plan) | 20 |
| `--topic` | Review topic (for context in output) | "[Your Topic]" |
| `--format` | `survey` or `thesis` (for writing-outline) | `survey` |
| `--output-dir` | Directory to save JSON files (for `--type all`) | stdout only |

## Dependencies

Python stdlib only.

## Tested with

- **Direct script run:** ✅ `--type reading-plan --papers 20` returns 5/10/5 P1/P2/P3 split with note template
- **`--type all`:** ✅ Writes 3 JSON files (reading_plan.json, comparison_matrix.json, writing_outline.json) to output dir
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions, executed script with `--papers 12`, got correct 3/6/3 split, explained the 4-phase workflow

### Agno agent verdict (excerpt)
> The write-review-paper skill is a structured guide for writing academic literature reviews and survey papers. The generated reading plan template shows how to distribute 12 papers across priority levels (3 must-read, 6 should-read, 3 skim) with specific reading actions for each tier and a standardized note template. The script requires no external dependencies and can generate various templates for your literature review workflow.
