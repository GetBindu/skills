# minerals-gov-monitor

Monitor government and regulator releases relevant to critical minerals and materials via domain-targeted web discovery 

## Setup

```bash
cd minerals-gov-monitor
python3 -m venv .venv && source .venv/bin/activate && pip install bs4 requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/gov_monitor.py --help
```

## Dependencies

- `bs4`
- `requests`
