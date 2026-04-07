# simpy

Process-based discrete-event simulation — queues, resources, time-based events for manufacturing, logistics, networks, and service operations.

## Setup

```bash
cd simpy && python3 -m venv .venv && source .venv/bin/activate && pip install simpy -q
```

## Usage

```bash
python3 scripts/basic_simulation_template.py --help
python3 scripts/resource_monitor.py --help
```

## Dependencies

`simpy`

## Scripts

| Script | Lines | Purpose |
|--------|-------|---------|
| `basic_simulation_template.py` | 191 | Configurable simulation template |
| `resource_monitor.py` | 338 | Monitor resource utilization + generate reports |

## Tested with

- **Agno (dry-run):** ✅
