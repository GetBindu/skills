# scikit-bio

Biological data toolkit for sequence analysis, alignments, phylogenetic trees, diversity metrics (alpha/beta, UniFrac), ordination (PCoA), PERMANOVA, and FASTA/Newick I/O.

## What it does

This skill wraps the scikit-bio Python library, providing a comprehensive bioinformatics toolkit for working with biological data. Core capabilities include sequence manipulation (DNA, RNA, protein) with reading and writing of FASTA, FASTQ, GenBank, EMBL, and Newick formats. It supports sequence alignment, motif searching, reverse complement, transcription, and translation operations.

For microbial ecology and community analysis, the skill provides alpha diversity metrics (Shannon, Simpson, observed OTUs, Faith's PD), beta diversity distance matrices (Bray-Curtis, UniFrac, Jaccard), ordination methods (PCoA, CCA, RDA), and statistical tests (PERMANOVA, ANOSIM, Mantel test). Phylogenetic tree construction and manipulation are also supported via Newick I/O.

The demo script serves as a lightweight CLI entrypoint that confirms scikit-bio availability and points to the SKILL.md reference documentation for detailed usage patterns and code examples.

## Setup

```bash
cd scikit-bio
python3 -m venv .venv && source .venv/bin/activate && pip install scikit-bio numpy -q
```

## Environment variables

None.

## Usage

### Input

```bash
python3 scripts/demo.py --format json
```

### Output

```
{
  "skill": "scikit-bio",
  "status": "available",
  "description": "Bioinformatics toolkit",
  "note": "See SKILL.md and references/ for comprehensive documentation"
}
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--format`, `-f` | Output format (`summary` or `json`) | `summary` |

## Dependencies

- `scikit-bio`
- `numpy`

## Tested with

- **Direct script run:** pass (reports status and points to SKILL.md documentation)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict (excerpt)

> The agent loaded the scikit-bio skill, confirmed it was available via the demo entrypoint, and successfully referenced the SKILL.md documentation for detailed bioinformatics analysis patterns covering sequence analysis, diversity metrics, and ordination.

## Fix notes

- Cleaned `__pycache__/` directory
- Applied 1 ruff lint fix
