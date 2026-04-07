# neuropixels-analysis

Neuropixels neural recording analysis.

## Setup

```bash
cd neuropixels-analysis
python3 -m venv .venv && source .venv/bin/activate && pip install matplotlib numpy pandas probeinterface scipy spikeinterface -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/preprocess_recording.py --help
```

## Dependencies

- `matplotlib`
- `numpy`
- `pandas`
- `probeinterface`
- `scipy`
- `spikeinterface`
