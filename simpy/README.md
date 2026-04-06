# simpy

Discrete-event simulation for manufacturing lines, queuing systems, and logistics using the SimPy framework.

## What it does

This skill provides templates and utilities for building discrete-event simulations with SimPy. The `basic_simulation_template.py` script implements a configurable queuing simulation where customers arrive at random intervals, wait for a shared resource (server/machine), get served, and depart. It collects statistics on wait times, service times, throughput, and queue lengths.

The `resource_monitor.py` module provides reusable monitoring classes that track queue lengths over time, resource utilization, wait times, and request/release events. These can be attached to any SimPy resource to collect detailed performance metrics during a simulation run.

Together, these scripts serve as a starting point for modeling manufacturing lines, call centers, hospital patient flows, supply chain logistics, and other systems where entities compete for limited resources.

## Setup

```bash
cd simpy
python3 -m venv .venv && source .venv/bin/activate && pip install simpy -q
```

## Environment variables

None.

## Usage

### Input

```bash
python3 scripts/basic_simulation_template.py
```

### Output

```
==================================================
SIMULATION STATISTICS
==================================================
Total customers: 10
Average wait time: 2.45
Max wait time: 6.12
Min wait time: 0.00
Average service time: 3.01
Throughput: 0.15 customers/time unit
==================================================
```

## CLI flags

The template uses a `SimulationConfig` class for configuration rather than CLI flags. Edit the config parameters in the script:

| Parameter | Description | Default |
|-----------|-------------|---------|
| `random_seed` | Random seed for reproducibility | `42` |
| `num_resources` | Number of shared resources (servers) | `2` |
| `num_processes` | Number of customer processes | `10` |
| `sim_time` | Total simulation time | `100` |
| `arrival_rate` | Average time between arrivals | `5.0` |
| `service_time_mean` | Average service time | `3.0` |
| `service_time_std` | Service time standard deviation | `1.0` |

## Dependencies

- `simpy`

## Tested with

- **Direct script run:** pass (ran successfully with default parameters, produced statistics)
- **Agno agent (Claude Haiku 4.5):** pass

### Agno agent verdict (excerpt)

> The skill loaded and executed correctly. The agent understood the discrete-event simulation framework, described how to customize the template for different scenarios (manufacturing, queuing, logistics), and correctly interpreted the simulation output statistics.

## Fix notes

- Cleaned `__pycache__/` directories
- Applied lint fixes (6 issues fixed)
