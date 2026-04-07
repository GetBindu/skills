# spatial-transcriptomics

Spatial transcriptomics analysis via ToolUniverse — gene expression mapping in tissue architecture for 10x Visium, MERFISH, seqFISH, Slide-seq, and imaging-based platforms.

## What it does

Targets `tooluniverse-spatial-transcriptomics` agentic workflow. Performs spatial clustering, domain identification, cell-cell proximity analysis, spatially variable gene detection, tissue architecture mapping, and integration with single-cell data. Use for spatial expression patterns, tumor microenvironment spatial structure, or tissue organization studies.

## ⚠️ Current status

ToolUniverse wrapper — pip package doesn't bundle the agentic workflow. Script detects and reports this.

## Setup

```bash
cd spatial-transcriptomics
python3 -m venv .venv && source .venv/bin/activate && pip install tooluniverse pyyaml -q
```

## Environment variables

None for `--list-workflows`.

## Usage

```bash
python3 scripts/run.py --help
python3 scripts/run.py --list-workflows
python3 scripts/run.py --query "Map spatial gene expression in Visium breast cancer"
```

## Dependencies

`tooluniverse`, `pyyaml`

## Tested with

- **`--help`:** ✅
- **Agno agent (Claude Haiku 4.5):** ✅ Described spatial clustering, domain ID, cell-cell proximity, SVG detection, tissue architecture

### Agno verdict
> Perfect for understanding how cells organize in tissue and how their spatial relationships drive biological processes. Supports 10x Visium, MERFISH, seqFISH, Slide-seq, and imaging-based platforms.
