# zarr-python

Create, write, read, and slice chunked N-dimensional arrays using Zarr.

## What it does

Demonstrates Zarr's core capabilities for storing large arrays: chunked layout, NumPy-style indexing, round-trip integrity checks, and partial reads. The demo creates a chunked float32 array, writes sequential data, verifies it reads back correctly, and exercises common slicing patterns (first row, first chunk, every-Nth row). Supports arbitrary array dimensions via CLI flags.

## Setup

```bash
cd zarr-python
python3 -m venv .venv && source .venv/bin/activate && pip install zarr numpy -q
```

## Environment variables

None. Pure local library, no API keys.

## Usage

### Input — default 2D array
```bash
python3 scripts/demo.py
```

### Output
```
============================================================
Zarr Demo (v2.18.2)
============================================================
  Shape: [1000, 1000]  Chunks: [100, 100]  dtype: float32
  Total chunks: 100
  Size: 4,000,000 bytes (3.81 MB)
  Write verified: True
  First 5 values: [0.0, 1.0, 2.0, 3.0, 4.0]

  Slicing demo:
    first_row: shape=[1000]
    first_chunk: shape=[100, 100]
    every_tenth: shape=[100, 1000]
```

### Other input modes
```bash
# 3D array with custom chunks
python3 scripts/demo.py --shape 300 300 300 --chunks 30 30 30

# JSON output for machine consumption
python3 scripts/demo.py --format json

# Persist the store to disk (default: tempdir, auto-cleaned)
python3 scripts/demo.py --store /tmp/my.zarr
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--shape` | Array shape (space-separated ints) | `1000 1000` |
| `--chunks` | Chunk shape (must match shape dims) | `100 100` |
| `--store` | Disk path to persist store | tempdir (cleaned) |
| `--format` / `-f` | `summary` or `json` | `summary` |

## Dependencies

- `zarr` (tested with 2.18 and 3.1)
- `numpy`

## Tested with

- **Direct script run:** ✅ 1000×1000 float32 array, 100 chunks, write verified, slicing demo works
- **3D test:** ✅ 300×300×300 array, 1000 chunks, 108 MB, write verified
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions, ran demo via `get_skill_script(execute=True)`, verified output, explained chunking/slicing behavior

### Agno agent verdict (excerpt)
> The demo script executed a practical example of Zarr's core functionality: Created a 1000×1000 float32 array with 100×100 chunks (100 total chunks), populated with sequential values, verified round-trip (Write verified: True), and demonstrated efficient partial access (first row, first chunk, every tenth row). The NumPy-style indexing makes it intuitive for scientists already familiar with NumPy. Cloud-ready: chunked arrays can be stored in S3, GCS, or local filesystems with the same API.
