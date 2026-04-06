# Spatial Transcriptomics — ToolUniverse Workflow Reference

## Upstream

- **Repo**: https://github.com/mims-harvard/ToolUniverse
- **Skill def**: https://github.com/mims-harvard/ToolUniverse/tree/main/skills/tooluniverse-spatial-transcriptomics

## Workflow overview

The `tooluniverse-spatial-transcriptomics` agentic workflow maps gene expression in tissue architecture context:

1. **Spatial clustering** — identify spatial domains/regions from expression data
2. **Domain identification** — annotate clusters with cell type and tissue context
3. **Cell-cell proximity analysis** — quantify spatial relationships between cell types
4. **Spatially variable gene detection** — identify genes with significant spatial patterns
5. **Tissue architecture mapping** — reconstruct tissue organization from expression + coordinates
6. **scRNA-seq integration** — combine spatial data with single-cell reference atlases

## Supported platforms

- 10x Visium / Visium HD
- MERFISH
- seqFISH / seqFISH+
- Slide-seq / Slide-seq V2
- Imaging-based spatial transcriptomics (osmFISH, STARmap)

## pip vs upstream gap

The pip-published `tooluniverse` package bundles ~214 data-source tool clients but does **not** include the agentic skill workflow definitions. The `run.py` script detects this gap and exits with a structured error pointing to the upstream repo.

## Difference from spatial-omics-analysis

- **spatial-transcriptomics**: Focuses on expression mapping, spatial clustering, domain identification, and scRNA-seq integration
- **spatial-omics-analysis**: Broader scope — adds pathway enrichment, druggable targets, immune microenvironment, metabolomics, and multi-modal integration on top of spatial data
