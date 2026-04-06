# single-cell

CLI wrapper for the ToolUniverse scRNA-seq analysis agentic workflow — QC, clustering, differential expression, cell type annotation, batch correction, trajectory inference, and cell-cell communication analysis.

## What it does

Targets the `tooluniverse-single-cell` agentic workflow from [mims-harvard/ToolUniverse](https://github.com/mims-harvard/ToolUniverse/tree/main/skills/tooluniverse-single-cell). Covers:

1. **Core scRNA-seq**: QC → normalize → PCA → UMAP → Leiden clustering → marker genes → cell type annotation
2. **Batch correction**: Harmony integration
3. **Cell-cell communication**: Ligand-receptor interactions via OmniPath (CellPhoneDB, CellChatDB), communication strength scoring, signaling cascades
4. **Statistics**: Pearson/Spearman correlations, t-tests, ANOVA, pseudotime/trajectory inference
5. **Integration**: Gene annotation (HPA, Ensembl, MyGene, UniProt), enrichment (GSEA, PANTHER, STRING)

## ⚠️ Current status

Same gap as variant-interpretation/variant-analysis: the pip-published `tooluniverse` doesn't bundle agentic workflows from the upstream repo's `skills/` directory. Script detects this and reports honestly.

## Setup

```bash
cd single-cell
python3 -m venv .venv && source .venv/bin/activate && pip install tooluniverse pyyaml -q
```

## Environment variables

None for `--list-workflows`. Full workflow may require data-source API keys.

## Usage

### Input
```bash
python3 scripts/run.py --list-workflows
```

### Output
```json
{
  "total_tools_loaded": 214,
  "target_workflow": "tooluniverse-single-cell",
  "target_workflow_available": false,
  "sample_tools": ["CallAgent", "Finish", "Tool_RAG", ...]
}
```

## Dependencies

- `tooluniverse`, `pyyaml`

## Tested with

- **`--help`:** ✅
- **`--list-workflows`:** ✅ (via Agno, reports gap)
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Described all 5 capability areas, BixBench coverage (18+ questions across 5 projects), and data integration points

### Agno agent verdict (excerpt)
> Production-ready scRNA-seq platform built on scanpy/anndata/ToolUniverse. Covers: core scRNA-seq (QC → UMAP → clustering → DE), batch correction (Harmony), cell-cell communication (CellPhoneDB/CellChatDB via OmniPath with communication strength scoring), trajectory analysis (pseudotime), and statistical methods (t-tests, ANOVA, correlations). Multi-format support: h5ad, 10X, CSV/TSV. Integration with HPA, MyGene, Ensembl, UniProt for annotation and PANTHER, STRING, Reactome for enrichment.

## Fix notes

- Merged duplicate YAML frontmatter blocks
- Upgraded description from "ToolUniverse workflow — Single Cell" to detailed capability summary
- Rewrote `run.py` with `--list-workflows` and gap detection
- Created `references/workflow_reference.md`
- Removed `__pycache__/`
