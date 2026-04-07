# blast

Search NCBI BLAST for sequence homology and find similar sequences in biological databases

## Setup

```bash
cd blast
python3 -m venv .venv && source .venv/bin/activate && pip install threading -q
```

## Environment variables

- `NCBI_EMAIL`

## Usage

```bash
python3 scripts/blast_search.py --help
```

## Dependencies

- `threading`
