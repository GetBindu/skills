# venue-templates

LaTeX templates, formatting requirements, and submission guidelines for major scientific publication venues, conferences, posters, and grant proposals.

## What it does

Provides a registry of venue-specific templates and a helper script to look them up, view their requirements, and search by keyword. Covers:

- **Journals**: Nature, Science, PLOS ONE, IEEE, ACM, Cell Press
- **Conferences**: NeurIPS, ICML, CVPR, CHI
- **Posters**: Beamerposter academic format
- **Grants**: NSF Standard Grant, NIH Specific Aims Page

Ships with 11 reference documents covering: `nature_science_style`, `cell_press_style`, `ml_conference_style`, `cs_conference_style`, `journals_formatting`, `conferences_formatting`, `medical_journal_styles`, `posters_guidelines`, `grants_requirements`, `reviewer_expectations`, and `venue_writing_styles`. Plus `.tex` template files under `assets/`.

## Setup

No pip dependencies — the helper scripts use Python stdlib only. For actually compiling templates you'll need LaTeX separately.

## Environment variables

None.

## Usage

### Input — list all templates
```bash
python3 scripts/query_template.py --list-all
```

### Output
```
=== AVAILABLE TEMPLATES ===


JOURNALS:
  • Nature
    File: nature_article.tex
    Description: Top-tier multidisciplinary science journal
  • NeurIPS (Neural Information Processing Systems)
    File: neurips_article.tex
    Description: Top-tier machine learning conference
  • PLOS ONE
    File: plos_one.tex
    Description: Open-access multidisciplinary journal


POSTERS:
  • Beamerposter Academic
    File: beamerposter_academic.tex
    Description: Classic academic conference poster using beamerposter


GRANTS:
  • NSF Standard Grant
    File: nsf_proposal_template.tex
    Description: National Science Foundation research proposal
  • NIH Specific Aims Page
    File: nih_specific_aims.tex
    Description: Most critical page of NIH proposals
```

### Other input modes
```bash
# Get formatting requirements for a specific venue
python3 scripts/query_template.py --venue "NeurIPS" --requirements

# Search by keyword
python3 scripts/query_template.py --keyword "machine learning"

# Filter by type
python3 scripts/query_template.py --list-all --type journals
python3 scripts/query_template.py --list-all --type grants
```

## Helper scripts

| Script | Purpose |
|--------|---------|
| `query_template.py` | Search, list, and view venue template metadata + requirements |
| `customize_template.py` | Auto-populate a template with author information |
| `validate_format.py` | Check a document against venue-specific formatting requirements |

## CLI flags (`query_template.py`)

| Flag | Description |
|------|-------------|
| `--venue` | Venue name (e.g., "Nature", "NeurIPS") |
| `--type` | `journals`, `posters`, `grants`, or `all` |
| `--keyword` | Search keyword across template descriptions |
| `--list-all` | List every available template |
| `--requirements` | Show formatting requirements for the selected venue |

## Dependencies

Python stdlib only.

## Tested with

- **Direct script run (`--list-all`):** ✅ Returns 3 categories (Journals, Posters, Grants) with 6 venue templates
- **`--venue "NeurIPS" --requirements`:** ✅ 8 pages + unlimited refs, two-column, numbered citations, double-blind anonymization required
- **`--keyword "machine learning"`:** ✅ Finds NeurIPS, shows full metadata and template file path
- **Agno agent (Claude Haiku 4.5 via OpenRouter, 11.9s):** ✅ Agent loaded instructions, listed all templates, explained the 3 helper scripts and the reference documentation

### Agno agent verdict (excerpt)
> The venue-templates skill is a comprehensive resource for academic publishing: 50+ publication templates (LaTeX) for major journals, conferences, and institutions; venue-specific requirements covering page limits, fonts, citation styles, figure/table requirements, and anonymization policies; three helper scripts (query_template.py for search, customize_template.py for author info, validate_format.py for compliance); writing style guides (Nature accessible storytelling vs NeurIPS contribution bullets); and reference docs covering journals, conferences, posters, grants, medical journals, ML conferences, and reviewer expectations.
