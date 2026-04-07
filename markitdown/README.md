# markitdown

Convert files and office documents to Markdown.

## Setup

```bash
cd markitdown
python3 -m venv .venv && source .venv/bin/activate && pip install concurrent markitdown openai -q
```

## Environment variables

- `OPENROUTER_API_KEY`

## Usage

```bash
python3 scripts/convert_literature.py --help
```

## Dependencies

- `concurrent`
- `markitdown`
- `openai`
