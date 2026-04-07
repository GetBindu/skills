# brenda-database

Access BRENDA enzyme database via SOAP API.

## Setup

```bash
cd brenda-database
python3 -m venv .venv && source .venv/bin/activate && pip install brenda_client brenda_queries matplotlib networkx numpy pandas requests scripts seaborn zeep -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/brenda_visualization.py --help
```

## Dependencies

- `brenda_client`
- `brenda_queries`
- `matplotlib`
- `networkx`
- `numpy`
- `pandas`
- `requests`
- `scripts`
- `seaborn`
- `zeep`
