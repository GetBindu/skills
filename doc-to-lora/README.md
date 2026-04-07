# doc-to-lora

A method to instantly internalize document contexts into language models using LoRA without fine-tuning.

## Setup

```bash
cd doc-to-lora
python3 -m venv .venv && source .venv/bin/activate && pip install requests scientia -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/doc_to_lora_client.py --help
```

## Dependencies

- `requests`
- `scientia`
