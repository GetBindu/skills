# corpus-search

Semantic search over critical minerals PDF corpus — rare earth, lithium, cobalt, nickel supply chain, trade policy, extr

## Setup

```bash
cd corpus-search
python3 -m venv .venv && source .venv/bin/activate && pip install pdfplumber pinecone -q
```

## Environment variables

- `PINECONE_API_KEY`

## Usage

```bash
python3 scripts/search_corpus.py --help
```

## Dependencies

- `pdfplumber`
- `pinecone`
