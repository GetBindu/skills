# minerals-viz

Generate charts (PNG/SVG) for critical minerals data — production, trade, import reliance, and time series

## Setup

```bash
cd minerals-viz
python3 -m venv .venv && source .venv/bin/activate && pip install cmm_data matplotlib -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/generate_chart.py --help
```

## Dependencies

- `cmm_data`
- `matplotlib`
