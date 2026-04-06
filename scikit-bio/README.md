# scikit-bio

Biological data toolkit — sequence analysis, alignments, phylogenetic trees, diversity metrics, ordination, and PERMANOVA.

## What it does

Wraps scikit-bio for microbiome and bioinformatics workflows: alpha/beta diversity (Shannon, Simpson, UniFrac), ordination (PCoA, NMDS), PERMANOVA statistical testing, sequence alignment, phylogenetic tree construction, and FASTA/Newick I/O.

## Setup

```bash
cd scikit-bio
python3 -m venv .venv && source .venv/bin/activate && pip install scikit-bio numpy -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/demo.py --format summary
```

## Dependencies

- `scikit-bio`, `numpy`

## Tested with

- **Direct script run:** pass (--help works)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict

> Agent loaded the skill and described diversity analysis, sequence processing, and phylogenetic capabilities.

## Fix notes

- Cleaned `__pycache__/`, 1 ruff lint fix
