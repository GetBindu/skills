# Spatial Multi-Omics Analysis — ToolUniverse Workflow Reference

## Upstream

- **Repo**: https://github.com/mims-harvard/ToolUniverse
- **Skill def**: https://github.com/mims-harvard/ToolUniverse/tree/main/skills/tooluniverse-spatial-omics-analysis

## Workflow overview

The `tooluniverse-spatial-omics-analysis` agentic workflow performs 9 analysis phases:

1. **Spatial domain characterization** — annotate spatial clusters with cell type composition
2. **Pathway enrichment** — GSEA / ORA on spatially variable genes per domain
3. **Cell-cell interaction inference** — CellPhoneDB / CellChatDB ligand-receptor analysis
4. **Druggable target identification** — map SVGs to druggable gene databases
5. **Immune microenvironment** — deconvolute immune infiltration patterns
6. **Metabolic profiling** — spatial metabolomics integration
7. **Multi-modal integration** — combine RNA + protein + metabolite layers
8. **Validation recommendations** — suggest smFISH, IHC, spatial ATAC-seq follow-ups
9. **Report generation** — Spatial Omics Integration Score (0-100) + domain-by-domain summary

## Supported platforms

- 10x Visium / Visium HD
- MERFISH
- DBiT-seq / DBiT-plus
- SLIDE-seq / SLIDE-seq V2
- seqFISH / seqFISH+
- STARmap
- Stereo-seq

## pip vs upstream gap

The pip-published `tooluniverse` package bundles ~400 data-source tool clients (gene lookup, pathway queries, etc.) but does **not** include the agentic skill workflow definitions. The `run.py` script detects this gap and exits with a structured error pointing to the upstream repo.

## Key tools used (subset)

- `gene_ontology_search` — GO term enrichment
- `pathway_enrichment` — KEGG / Reactome pathways
- `cellphonedb_query` — ligand-receptor pairs
- `drug_target_lookup` — druggability assessment
- `immune_deconvolution` — CIBERSORT-style deconvolution
- `spatial_variable_genes` — SVG detection utilities
