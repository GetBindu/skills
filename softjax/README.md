# softjax

Soft differentiable drop-in replacements for non-differentiable JAX functions (abs, relu, sort, argmax, comparison, logical operators, etc.

## Setup

```bash
cd softjax
python3 -m venv .venv && source .venv/bin/activate && pip install requests scientia -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/softjax_client.py --help
```

## Dependencies

- `requests`
- `scientia`
