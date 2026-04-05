# variant-analysis

CLI wrapper for the ToolUniverse VCF analysis / variant annotation / structural-variant interpretation agentic workflow.

## What it does

Targets the `tooluniverse-variant-analysis` agentic workflow from [mims-harvard/ToolUniverse](https://github.com/mims-harvard/ToolUniverse/tree/main/skills/tooluniverse-variant-analysis). The upstream workflow handles:

1. **VCF parsing** — SNVs, indels, and structural variants (SVs); VCF 4.x + gzipped multi-sample files
2. **Mutation classification** — missense / nonsense / synonymous / frameshift / splice / intronic / intergenic / UTR, extracted from SnpEff ANN, VEP CSQ, or GATK Funcotator fields
3. **Filtering** — VAF, depth, genotype quality, consequence type, population frequency, SV size
4. **SV/CNV interpretation** — ClinGen dosage sensitivity scoring (HI/TS), gnomAD SV frequencies, ACMG/ClinGen guidelines
5. **Annotation & statistics** — Ti/Tv ratio, per-sample VAF/depth distributions, ClinVar / dbSNP / gnomAD / CADD annotation

## ⚠️ Current status

Same gap as `variant-interpretation`: the pip-published `tooluniverse` package bundles ~214 data-source tool clients but does NOT bundle the agentic skill workflows from the upstream repo's `skills/` directory. Script handles this by:
- `--list-workflows` reporting whether the target workflow is loaded
- `--query` returning a clear JSON gap message with the upstream skill definition link

## Setup

```bash
cd variant-analysis
python3 -m venv .venv && source .venv/bin/activate && pip install tooluniverse pyyaml -q
```

## Environment variables

None for `--list-workflows`. Full workflow execution may require data-source API keys depending on which upstream tools are invoked.

## Usage

### Input — check workflow availability
```bash
python3 scripts/run.py --list-workflows
```

### Output
```json
{
  "total_tools_loaded": 214,
  "upstream_repo": "https://github.com/mims-harvard/ToolUniverse",
  "target_workflow": "tooluniverse-variant-analysis",
  "target_workflow_available": false,
  "sample_tools": [
    "CallAgent",
    "Finish",
    "Tool_RAG",
    "drug_pharmacogenomics_data",
    "get_HPO_ID_by_phenotype",
    "..."
  ]
}
```

### Input — real query attempt
```bash
python3 scripts/run.py --query "What fraction of variants in /path/file.vcf with VAF < 0.3 are missense?"
```

### Output (current gap message)
```json
{
  "error": "Workflow 'tooluniverse-variant-analysis' not available in current tooluniverse install",
  "reason": "The pip-published tooluniverse package bundles data-source tool clients but not the agentic skill workflows from the upstream repo's skills/ directory.",
  "upstream_skill_definition": "https://github.com/mims-harvard/ToolUniverse/tree/main/skills/tooluniverse-variant-analysis",
  "workaround": "Clone the upstream repo and load skills from skills/ directory, or wait for the skill workflow to be published to PyPI.",
  "tools_loaded": 214,
  "query": "What fraction of variants in /path/file.vcf with VAF < 0.3 are missense?"
}
```

## CLI flags

| Flag | Description |
|------|-------------|
| `--query` / `-q` | VCF analysis question or task |
| `--format` / `-f` | `json` (default) or `summary` |
| `--list-workflows` | Report tool count + target workflow availability |
| `--no-cache` | Disable result caching (if supported by tooluniverse version) |

## Dependencies

- `tooluniverse`
- `pyyaml` (transitive dep not declared by tooluniverse)

## Tested with

- **Direct script run (`--list-workflows`):** ✅ Loads 214 ToolUniverse tools, correctly reports that the target workflow is not registered
- **Direct script run (`--query`):** ✅ Returns clear JSON gap message with upstream pointer
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions, executed `--list-workflows`, and correctly explained all 5 capability areas (VCF parsing, mutation classification, filtering, SV/CNV interpretation, annotation & statistics)

### Agno agent verdict (excerpt)
> The skill is a production-ready VCF processing system with these core capabilities: VCF parsing (SNVs, indels, SVs/CNVs), mutation classification (missense/nonsense/synonymous/frameshift/splice/intronic/intergenic), filtering (VAF, depth, consequence, population frequency, SV size), structural variant & CNV interpretation (annotates with gnomAD SV frequencies, queries ClinGen HI/TS dosage sensitivity, classifies pathogenicity via ACMG/ClinGen guidelines), and annotation & statistics (Ti/Tv ratio, VAF/depth distributions, ClinVar/dbSNP/gnomAD/CADD annotation via ToolUniverse). Designed for bioinformatics questions like "What fraction of variants with VAF < 0.3 are missense?" or "Which dosage-sensitive genes overlap this CNV?"

## See also

- [`references/vcf_analysis.md`](references/vcf_analysis.md) — mutation type & SV/CNV reference, filter criteria, annotation sources
- Upstream skill: https://github.com/mims-harvard/ToolUniverse/tree/main/skills/tooluniverse-variant-analysis

## Fix notes

- Upgraded weak description ("ToolUniverse workflow — Variant Analysis") to VCF-focused summary
- Added `--list-workflows` flag and honest gap-detection in `run.py`
- Added compat shim for ToolUniverse `use_cache` kwarg removed in newer versions
- Created `references/vcf_analysis.md` with mutation classification + SV/CNV reference
- Removed stray `__pycache__/`
