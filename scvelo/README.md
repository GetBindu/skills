# scvelo

RNA velocity analysis — estimate cell state transitions from unspliced/spliced mRNA dynamics in scRNA-seq data.

## What it does

Prompt-only skill (no scripts) providing LLM instructions for scVelo RNA velocity analysis: dynamical modeling of splicing kinetics, latent time inference, velocity embedding on UMAP/t-SNE, driver gene identification, and trajectory direction estimation. Complements scanpy and scvi-tools for trajectory inference workflows.

## Setup

```bash
pip install scvelo scanpy
```

## Environment variables

None.

## Dependencies

- `scvelo`, `scanpy`, `anndata`

## Tested with

- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict

> Agent loaded the skill and described RNA velocity concepts, dynamical modeling, and driver gene identification workflows.

## Fix notes

- No code changes needed (prompt-only skill with clean frontmatter)
