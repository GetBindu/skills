# RNA-seq DESeq2 Workflow Reference

## Required Packages
```bash
pip install pydeseq2 gseapy pandas numpy scipy anndata
```

## Core Workflow Steps

1. **Question Parsing** — Identify data files, thresholds, design, contrast, direction
2. **Data Loading** — Load count matrix + metadata (CSV/TSV/H5AD)
3. **Validation** — Check matching sample IDs, non-negative integers, design factors present
4. **DESeq2 Pipeline** — DeseqDataSet → deseq() → DeseqStats → summary()
5. **Result Filtering** — Apply padj, log2FC, baseMean thresholds
6. **Enrichment** (optional) — GO/KEGG/Reactome via gseapy

## Default Thresholds
| Parameter | Default |
|-----------|---------|
| padj | 0.05 |
| log2FC | 0 (any fold change) |
| baseMean | 0 (any expression) |

## Key PyDESeq2 API
```python
from pydeseq2.dds import DeseqDataSet
from pydeseq2.ds import DeseqStats

dds = DeseqDataSet(counts=count_df, metadata=meta_df, design_factors="condition")
dds.deseq2()

stat = DeseqStats(dds, contrast=["condition", "treated", "control"])
stat.summary()
results_df = stat.results_df
```
