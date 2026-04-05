# vaex

Out-of-core DataFrame processing for tabular datasets that don't fit in RAM — billions of rows at hundreds of millions of rows per second.

## What it does

Vaex is a Python library for lazy, out-of-core DataFrames. Unlike pandas which loads everything into memory, Vaex memory-maps the data and computes expressions lazily, enabling fast aggregations, filtering, grouping, and visualization on datasets that are gigabytes to terabytes in size.

The included `demo.py` builds a synthetic DataFrame (configurable row count), then exercises:
- Aggregations (mean, std, sum, max)
- Boolean filtering
- Group-by with per-group aggregations
- Optional HDF5 export

## Setup

```bash
cd vaex
python3 -m venv .venv && source .venv/bin/activate && pip install vaex -q
```

## Environment variables

None. Pure local library.

## Usage

### Input
```bash
python3 scripts/demo.py --rows 1000000
```

### Output
```
============================================================
Vaex Demo (v4.19.0)
============================================================
  Rows: 1,000,000
  Columns: x, y, category, value

  Timings:
    build           0.02s
    aggregations    0.027s
    filter          0.003s
    groupby         0.028s

  Stats:
    row_count       1,000,000
    x_mean          0.0001
    x_std           1.0005
    y_mean          0.0010
    value_sum       99,917,957.4894
    value_max       1,444.9443

  Filtered rows (x > 0 AND value > 50): 303,158

  Group-by (category), first 3:
    category=0: value_mean=100.24, n=99848
    category=1: value_mean=99.50, n=99878
    category=2: value_mean=100.13, n=100203
```

### Other input modes
```bash
# Larger dataset
python3 scripts/demo.py --rows 100000000

# Machine-readable
python3 scripts/demo.py --rows 5000000 --format json

# Persist to HDF5
python3 scripts/demo.py --rows 1000000 --save /tmp/demo.hdf5
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--rows` | Number of synthetic rows to build | 10,000,000 |
| `--save` | Export to HDF5 at this path | — |
| `--format` / `-f` | `summary` or `json` | `summary` |

## Dependencies

- `vaex` (depends on numpy, pyarrow, pandas as transitive deps)

## Tested with

- **Direct script run (1M rows):** ✅ Full demo in ~80ms total (build 20ms, aggregations 27ms, filter 3ms, groupby 28ms)
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions, ran `demo.py --rows 500000`, captured real metrics (12ms build, 24ms aggregations, 151,269 filtered rows), and explained all 7 Vaex capabilities

### Agno agent verdict (excerpt)
> Vaex is a high-performance library for processing massive datasets that don't fit in RAM. Key capabilities: out-of-core processing (billions of rows without loading into memory), lightning-fast operations (billion rows/sec with lazy evaluation), memory efficiency via virtual columns, fast aggregations and groupby, visualization for large datasets, ML pipeline integration (scikit-learn, XGBoost, CatBoost), format support (HDF5, CSV, Arrow, Parquet). The demo demonstrated how Vaex excels at rapid aggregations and filtering on half-a-million rows in milliseconds — perfect for interactive data analysis on datasets that would cripple traditional pandas DataFrames.

## See also

Reference docs under `references/`:
- `core_dataframes.md` — creating, opening, and manipulating DataFrames
- `data_processing.md` — expressions, filters, virtual columns
- `io_operations.md` — HDF5, CSV, Arrow, Parquet I/O
- `machine_learning.md` — ML pipelines with Vaex
- `performance.md` — benchmarks and tuning
- `visualization.md` — plotting and heatmaps

## Fix notes

- Replaced the previous placeholder `demo.py` (static JSON dict) with a real functional demo that imports Vaex and exercises aggregations, filtering, groupby, and optional HDF5 export
- Fixed Python 3.9 compat: `str | None` → `Optional[str]`
- Fixed ugly version display: Vaex 4.x returns a dict from `__version__`, now extracts just the core version string
- Removed stray `__pycache__/`
