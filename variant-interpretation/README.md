# variant-interpretation

CLI wrapper for the ToolUniverse clinical variant interpretation agentic workflow. Aggregates evidence from ClinVar, gnomAD, CIViC, UniProt, PDB, and AlphaFold2 to produce ACMG-classified pathogenicity assessments.

## What it does

This skill targets the `tooluniverse-variant-interpretation` agentic workflow from [mims-harvard/ToolUniverse](https://github.com/mims-harvard/ToolUniverse/tree/main/skills/tooluniverse-variant-interpretation). It is designed to take a variant description (gene + HGVS, variant ID, or natural-language query) and return:

- **ACMG/AMP 2015 classification** (Pathogenic / Likely Pathogenic / VUS / Likely Benign / Benign)
- **Pathogenicity score** (0–100)
- **Evidence codes applied** (PVS1, PS1, PM1, PP3, BP4, etc.) with justification
- **Clinical recommendation** (cascade testing, counseling, therapy implications)
- **Structural impact summary** (when AlphaFold2 structure is available)

## ⚠️ Current status

**The pip-published `tooluniverse` package does NOT bundle this agentic workflow.** It ships ~214 data-source tool clients (OpenTargets, FDA labels, Monarch, etc.) but the `skills/` subdirectory from the upstream repo — including `tooluniverse-variant-interpretation` — is **not** installed via `pip install tooluniverse`.

The script handles this gracefully:
- `--list-workflows` reports whether the target workflow is loaded
- `--query` attempts the workflow and returns a clear JSON error message with a pointer to the upstream skill definition if it's missing

To actually run the workflow, you need to clone the upstream repo and load the skill from its `skills/` directory, or wait for the skill to be published to PyPI.

## Setup

```bash
cd variant-interpretation
python3 -m venv .venv && source .venv/bin/activate && pip install tooluniverse pyyaml -q
```

## Environment variables

None required for `--list-workflows`. Full workflow execution (when the skill becomes available) may require data-source API keys depending on which tools the upstream workflow pulls in.

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
  "target_workflow": "tooluniverse-variant-interpretation",
  "target_workflow_available": false,
  "sample_tools": [
    "CallAgent",
    "Finish",
    "Tool_RAG",
    "drug_pharmacogenomics_data",
    "get_HPO_ID_by_phenotype",
    ...
  ]
}
```

### Input — attempt a variant interpretation query
```bash
python3 scripts/run.py --query "BRCA1 c.5266dupC in Ashkenazi Jewish patient"
```

### Output (current gap message)
```json
{
  "error": "Workflow 'tooluniverse-variant-interpretation' not available in current tooluniverse install",
  "reason": "The pip-published tooluniverse package bundles data-source tool clients but not the agentic skill workflows from the upstream repo's skills/ directory.",
  "upstream_skill_definition": "https://github.com/mims-harvard/ToolUniverse/tree/main/skills/tooluniverse-variant-interpretation",
  "workaround": "Clone the upstream repo and load skills from skills/ directory, or wait for the skill workflow to be published to PyPI.",
  "tools_loaded": 214,
  "query": "BRCA1 c.5266dupC in Ashkenazi Jewish patient"
}
```

## CLI flags

| Flag | Description |
|------|-------------|
| `--query` / `-q` | Variant description or clinical question |
| `--format` / `-f` | `json` (default) or `summary` |
| `--list-workflows` | Report tool count + target workflow availability |
| `--no-cache` | Disable result caching (if supported by tooluniverse version) |

## Dependencies

- `tooluniverse`
- `pyyaml` (transitively required by tooluniverse but not declared in its requirements)

## Tested with

- **Direct script run (`--list-workflows`):** ✅ Loads 214 ToolUniverse tools, correctly reports that the target workflow is not registered
- **Direct script run (`--query`):** ✅ Returns a clear JSON gap message with upstream pointer
- **Agno agent (Claude Haiku 4.5 via OpenRouter, 15.8s):** ✅ Agent loaded instructions, executed `--list-workflows`, correctly explained the 6-phase clinical workflow design (variant identity → databases → predictions → structure → literature → ACMG), listed evidence codes (PVS1, PS1, PM1, PP3, BP4), and surfaced the current gap (workflow definition not in pip package)

### Agno agent verdict (excerpt)
> The variant-interpretation skill is a comprehensive clinical genomics workflow that transforms raw genetic variants into ACMG-classified clinical recommendations. Key problems solved: VUS classification (40-60% of clinical variants), evidence aggregation from 10+ databases (ClinVar, gnomAD, CIViC, UniProt, PDB), 3D structural context via AlphaFold2, clinical actionability. Current limitation: While tools are available in ToolUniverse, the specific variant-interpretation workflow definition hasn't been registered yet, so you'd need to orchestrate the phases manually using the available tools.

## See also

- [`references/acmg_workflow.md`](references/acmg_workflow.md) — full ACMG/AMP 2015 criteria + evidence source table
- Upstream skill definition: https://github.com/mims-harvard/ToolUniverse/tree/main/skills/tooluniverse-variant-interpretation

## Fix notes

- Merged two duplicate YAML frontmatter blocks (one was malformed — missing closing `---`)
- Upgraded weak description ("ToolUniverse workflow — Variant Interpretation") to accurate ACMG-focused description
- Added `--list-workflows` flag and graceful gap-detection in `run.py` so it produces actionable output even when the upstream workflow is missing
- Added compat shim for ToolUniverse `use_cache` kwarg which was removed in newer versions
- Created `references/acmg_workflow.md` with ACMG criteria reference
- Removed stray `__pycache__/`
