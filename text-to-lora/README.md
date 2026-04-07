# text-to-lora

Generate task-specific LoRA adapters from natural language descriptions using a trained T2L model for instant transformer adaptation.

## Setup

```bash
cd text-to-lora
python3 -m venv .venv && source .venv/bin/activate && pip install requests scientia -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/text_to_lora_client.py --help
```

## Dependencies

- `requests`
- `scientia`
