# spatial-transcriptomics

Spatial transcriptomics analysis via ToolUniverse — gene expression mapping in tissue architecture for 10x Visium, MERFISH, seqFISH, Slide-seq, and imaging-based platforms.

## What it does

Wraps the `tooluniverse-spatial-transcriptomics` agentic workflow, which maps gene expression in tissue context: spatial clustering, domain identification, cell-cell proximity analysis, spatially variable gene detection, tissue architecture mapping, and integration with single-cell RNA-seq reference data.

Compared to `spatial-omics-analysis` (which adds pathway enrichment, druggable targets, immune microenvironment, and multi-modal integration), this skill focuses on core spatial expression analysis and tissue organization.

**Note**: The pip-published `tooluniverse` package bundles ~214 data-source tool clients but does not include the agentic skill workflow definitions. The script detects this gap and provides a structured error pointing to the upstream repo.

## Setup

```bash
cd spatial-transcriptomics
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
  "target_workflow": "tooluniverse-spatial-transcriptomics",
  "target_workflow_available": false,
  "sample_tools": ["CallAgent", "Finish", "Tool_RAG", "..."]
}
```

### Run a query (requires upstream workflow)
```bash
python3 scripts/run.py --query "Map gene expression in 10x Visium breast cancer tissue"
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

> The agent loaded the spatial-transcriptomics skill, read the SKILL.md instructions, and described the full spatial analysis pipeline. It correctly identified the pip vs upstream gap and provided installation instructions for accessing the full workflow from the upstream ToolUniverse repo.

## Fix notes

- Merged duplicate YAML frontmatter blocks into one
- Upgraded weak description to detailed capability summary
- Moved `source:` under `metadata:`
- Rewrote `run.py` with `--list-workflows`, gap detection, and `use_cache` compat shim
- Removed `__pycache__/`
- Added `references/spatial_transcriptomics_workflow.md`
