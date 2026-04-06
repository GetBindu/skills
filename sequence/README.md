# sequence

Analyze biological sequences using Biopython — translate, align, parse FASTA/GenBank.

## What it does

CLI tool for biological sequence analysis: translate DNA to protein, reverse complement, parse FASTA/GenBank files, perform pairwise alignments, compute GC content, and search for motifs. Built on Biopython.

## Setup

```bash
cd sequence
python3 -m venv .venv && source .venv/bin/activate && pip install biopython -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/sequence_tools.py --help
```

## Dependencies

- `biopython`

## Tested with

- **Direct script run:** pass (graceful error when biopython not installed)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict

> Agent loaded the skill and described sequence translation, alignment, and FASTA/GenBank parsing capabilities.

## Fix notes

- Cleaned `__pycache__/`, 6 ruff lint fixes
