# spatial-omics-analysis

Spatial multi-omics interpretation via ToolUniverse — pathway enrichment, cell-cell interactions, druggable targets, immune microenvironment, and multi-modal integration for spatial transcriptomics/proteomics (10x Visium, MERFISH, DBiT-seq, SLIDE-seq).

## What it does

Targets `tooluniverse-spatial-omics-analysis` agentic workflow. Covers 8 analysis domains: pathway enrichment, cell-cell interaction inference, druggable target identification, immune microenvironment characterization, spatial domain annotation, transcription factor activity, immune checkpoint analysis, and literature validation. Produces domain-by-domain reports with Spatial Omics Integration Score (0-100) and evidence grading (T1-T4 tiers).

## ⚠️ Current status

Same gap as other ToolUniverse wrappers: pip `tooluniverse` doesn't bundle agentic workflows. Script detects and reports this honestly.

## Setup

```bash
cd spatial-omics-analysis
python3 -m venv .venv && source .venv/bin/activate && pip install tooluniverse pyyaml -q
```

## Environment variables

None for `--list-workflows`.

## Usage

```bash
python3 scripts/run.py --help
python3 scripts/run.py --list-workflows
python3 scripts/run.py --query "Analyze tumor microenvironment from Visium data"
```

## Dependencies

`tooluniverse`, `pyyaml`

## Tested with

- **`--help`:** ✅
- **Agno agent (Claude Haiku 4.5):** ✅ Described all 8 analysis domains, SOIS scoring, supported platforms

### Agno verdict
> Produces comprehensive markdown reports with evidence grading (T1-T4 tiers), calculates Spatial Omics Integration Score (0-100), supports 10x Visium, MERFISH, DBiT-seq, SLIDE-seq. NOT suitable for raw spatial data processing, image analysis, or deconvolution.
