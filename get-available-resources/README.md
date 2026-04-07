# get-available-resources

This skill should be used at the start of any computationally intensive scientific task to detect and report available system resources (CPU cores, GPUs, memory, disk space).

## Setup

```bash
cd get-available-resources
python3 -m venv .venv && source .venv/bin/activate && pip install platform psutil -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/detect_resources.py --help
```

## Dependencies

- `platform`
- `psutil`
