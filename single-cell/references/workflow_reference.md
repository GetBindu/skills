# Single-Cell Analysis Workflow Reference

## Upstream workflow
`tooluniverse-single-cell` from [mims-harvard/ToolUniverse](https://github.com/mims-harvard/ToolUniverse/tree/main/skills/tooluniverse-single-cell)

## Capabilities (from upstream skill definition)

### Core scRNA-seq analysis
- QC filtering (gene count, total counts, mitochondrial %)
- Normalization and log-transformation
- Highly variable gene selection
- PCA + neighborhood graph construction
- UMAP/t-SNE dimensionality reduction
- Leiden/Louvain clustering
- Differential expression (Wilcoxon, t-test, DESeq2)
- Cell type annotation with known marker genes

### Advanced features
- **Batch correction** via Harmony integration
- **Trajectory inference** for developmental trajectories
- **Cell-cell communication** analysis:
  - Ligand-receptor interactions via OmniPath (CellPhoneDB, CellChatDB)
  - Communication strength scoring between cell types
  - Signaling cascade identification
  - Multi-subunit receptor complex handling

### Integration with ToolUniverse ecosystem
- Gene annotation: HPA, Ensembl, MyGene, UniProt
- Enrichment: gseapy (GSEA), PANTHER, STRING

### Supported input formats
- `.h5ad` (AnnData native)
- 10X Genomics `.mtx` directories
- CSV/TSV count matrices
- Pre-annotated datasets with cell type labels

## Note on local availability
The pip-published `tooluniverse` package does NOT include this agentic workflow — it only ships data-source tool clients. The workflow definition lives in the upstream repo's `skills/` directory.
