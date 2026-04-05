#!/usr/bin/env python3
"""
Zarr Demo — Chunked N-dimensional array storage.

Demonstrates creating, writing, reading, and inspecting Zarr arrays.

Usage:
    python demo.py                          # run all demos
    python demo.py --shape 1000 1000        # custom shape
    python demo.py --chunks 100 100         # custom chunks
    python demo.py --format json            # JSON output
    python demo.py --store /tmp/my.zarr     # persist to disk
"""

import argparse
import json
import shutil
import sys
import tempfile
from pathlib import Path

try:
    import numpy as np
    import zarr
except ImportError as e:
    print(json.dumps({"error": f"Missing dependency: {e}. Install: pip install zarr numpy"}))
    sys.exit(1)


def demo_basic(shape, chunks, store_path=None):
    """Create, write, and read a Zarr array."""
    cleanup = False
    if store_path is None:
        store_path = tempfile.mkdtemp(suffix=".zarr")
        cleanup = True

    try:
        z = zarr.open(
            store_path,
            mode="w",
            shape=tuple(shape),
            chunks=tuple(chunks),
            dtype="f4",
        )

        data = np.arange(int(np.prod(shape)), dtype="f4").reshape(shape)
        z[:] = data
        read_data = z[:]

        return {
            "store_path": str(store_path),
            "shape": list(z.shape),
            "chunks": list(z.chunks),
            "dtype": str(z.dtype),
            "size_bytes": int(z.nbytes),
            "num_chunks": int(np.prod([s // c for s, c in zip(z.shape, z.chunks)])),
            "write_verified": bool(np.array_equal(data, read_data)),
            "first_values": data.flat[:5].tolist(),
            "zarr_version": zarr.__version__,
        }
    finally:
        if cleanup and Path(store_path).exists():
            shutil.rmtree(store_path, ignore_errors=True)


def demo_slicing(shape, chunks):
    """Demonstrate partial reads from a chunked array."""
    tmp = tempfile.mkdtemp(suffix=".zarr")
    try:
        z = zarr.open(tmp, mode="w", shape=tuple(shape), chunks=tuple(chunks), dtype="f4")
        z[:] = np.random.rand(*shape).astype("f4")

        return {
            "full_shape": list(shape),
            "slices": {
                "first_row": list(z[0, :].shape) if len(shape) >= 2 else None,
                "first_chunk": list(z[: chunks[0], : chunks[1]].shape) if len(shape) >= 2 else None,
                "every_tenth": list(z[::10].shape) if len(shape) >= 1 else None,
            },
        }
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main():
    parser = argparse.ArgumentParser(description="Zarr demonstration: create, write, and read chunked arrays")
    parser.add_argument("--shape", type=int, nargs="+", default=[1000, 1000], help="Array shape (default: 1000 1000)")
    parser.add_argument("--chunks", type=int, nargs="+", default=[100, 100], help="Chunk shape (default: 100 100)")
    parser.add_argument(
        "--store", type=str, default=None, help="Path to persist store (default: tempdir, auto-cleaned)"
    )
    parser.add_argument(
        "--format", "-f", default="summary", choices=["summary", "json"], help="Output format (default: summary)"
    )
    args = parser.parse_args()

    if len(args.shape) != len(args.chunks):
        print("Error: --shape and --chunks must have same number of dimensions", file=sys.stderr)
        sys.exit(1)

    result = {
        "skill": "zarr-python",
        "zarr_version": zarr.__version__,
        "basic": demo_basic(args.shape, args.chunks, args.store),
        "slicing": demo_slicing(args.shape, args.chunks),
    }

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(f"{'=' * 60}")
        print(f"Zarr Demo (v{zarr.__version__})")
        print(f"{'=' * 60}")
        b = result["basic"]
        print(f"  Shape: {b['shape']}  Chunks: {b['chunks']}  dtype: {b['dtype']}")
        print(f"  Total chunks: {b['num_chunks']}")
        print(f"  Size: {b['size_bytes']:,} bytes ({b['size_bytes'] / 1024 / 1024:.2f} MB)")
        print(f"  Write verified: {b['write_verified']}")
        print(f"  First 5 values: {b['first_values']}")
        if args.store:
            print(f"  Stored at: {b['store_path']}")

        s = result["slicing"]
        print("\n  Slicing demo:")
        for k, v in s["slices"].items():
            print(f"    {k}: shape={v}")


if __name__ == "__main__":
    main()
