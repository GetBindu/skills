# spatial-omics-analysis

Spatial multi-omics interpretation via ToolUniverse — pathway enrichment, cell-cell interactions, druggable targets, immune microenvironment, and multi-modal integration for spatial transcriptomics/proteomics experiments.

## What it does

Wraps the `tooluniverse-spatial-omics-analysis` agentic workflow, which performs 9-phase biological interpretation of spatial omics data: domain characterization, pathway enrichment, cell-cell interaction inference (CellPhoneDB/CellChatDB), druggable target identification, immune deconvolution, metabolic profiling, multi-modal integration, validation recommendations, and report generation with a Spatial Omics Integration Score (0-100).

Supports 10x Visium, MERFISH, DBiT-seq, SLIDE-seq, seqFISH, STARmap, and Stereo-seq platforms. The SKILL.md provides detailed prompting instructions for domain-by-domain analysis, evidence grading (T1-T4), and disease-focused interpretation.

**Note**: The pip-published `tooluniverse` package bundles ~214 data-source tool clients but does not include the agentic skill workflow definitions. The script detects this gap and provides a structured error pointing to the upstream repo for the full workflow.

## Setup

```bash
cd spatial-omics-analysis
python3 -m venv .venv && source .venv/bin/activate && pip install tooluniverse pyyaml -q
```

## Environment variables

None required.

## Usage

### List available tools
```bash
python3 scripts/run.py --list-workflows
```

### Output
```json
{
  "total_tools_loaded": 214,
  "upstream_repo": "https://github.com/mims-harvard/ToolUniverse",
  "target_workflow": "tooluniverse-spatial-omics-analysis",
  "target_workflow_available": false,
  "sample_tools": ["CallAgent", "Finish", "Tool_RAG", "drug_pharmacogenomics_data", "..."]
}
```

### Run a query (requires upstream workflow)
```bash
python3 scripts/run.py --query "Analyze breast cancer spatial transcriptomics SVGs"
```

### Gap detection output
```json
{
  "error": "Workflow 'tooluniverse-spatial-omics-analysis' not available in current tooluniverse install",
  "reason": "The pip-published tooluniverse package bundles data-source tool clients but not the agentic skill workflows.",
  "upstream_skill_definition": "https://github.com/mims-harvard/ToolUniverse/tree/main/skills/tooluniverse-spatial-omics-analysis",
  "workaround": "Clone the upstream repo and load skills from skills/ directory.",
  "tools_loaded": 214
}
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--query`, `-q` | Research question or analysis task | (required unless `--list-workflows`) |
| `--format`, `-f` | Output format (`json` or `summary`) | `json` |
| `--no-cache` | Disable result caching | off |
| `--list-workflows` | List available tools and exit | off |

## Dependencies

- `tooluniverse`
- `pyyaml`

## Tested with

- **Direct script run:** pass (--help, --list-workflows, gap detection all work)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict (excerpt)

> The agent loaded the spatial-omics-analysis skill, read the SKILL.md instructions, and correctly described the 9-phase spatial omics analysis pipeline. It identified that the pip package provides ~400 individual tool clients but the agentic workflow lives in the upstream GitHub repo, accurately reporting the gap detection behavior.

## Fix notes

- Merged duplicate YAML frontmatter blocks into one
- Upgraded weak description ("ToolUniverse workflow — Spatial Omics Analysis") to detailed capability summary
- Moved `source:` under `metadata:`
- Rewrote `run.py` with `--list-workflows`, gap detection, and `use_cache` compat shim
- Removed `__pycache__/`
- Added `references/spatial_omics_workflow.md`
