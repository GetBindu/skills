# bioreason_pro

Multimodal reasoning LLM for protein function prediction integrating protein embeddings with biological context to generate structured reasoning traces and functional annotations.

## Setup

```bash
cd bioreason_pro
python3 -m venv .venv && source .venv/bin/activate && pip install requests scientia -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/bioreason_pro_client.py --help
```

## Dependencies

- `requests`
- `scientia`
