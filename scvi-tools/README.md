# scvi-tools

Deep generative models for single-cell omics — probabilistic batch correction, transfer learning, differential expression with uncertainty, and multi-modal integration.

## What it does

Wraps the scvi-tools library for advanced single-cell analysis: scVI for batch correction and latent space modeling, TOTALVI for CITE-seq (RNA + protein), MultiVI for multiome (RNA + ATAC), scANVI for semi-supervised cell type annotation, and differential expression with posterior uncertainty quantification.

## Setup

```bash
cd scvi-tools
python3 -m venv .venv && source .venv/bin/activate && pip install scvi-tools -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/demo.py --format summary
```

## Dependencies

- `scvi-tools`

## Tested with

- **Direct script run:** pass (--help)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict

> Agent loaded the skill and described scVI, TOTALVI, MultiVI, and scANVI models with their respective use cases.

## Fix notes

- Cleaned `__pycache__/`, 1 ruff lint fix
