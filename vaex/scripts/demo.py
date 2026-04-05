#!/usr/bin/env python3
"""
Vaex Demo — Out-of-core DataFrames on billions of rows.

Demonstrates creating a large Vaex DataFrame, computing aggregations,
filtering, and exporting. Uses synthetic data so no external files are
needed.

Usage:
    python demo.py                              # default 10M rows
    python demo.py --rows 100000000             # 100M rows
    python demo.py --format json                # JSON output
    python demo.py --rows 5000000 --save /tmp/demo.hdf5
"""

import argparse
import json
import sys
import time
from pathlib import Path
from typing import Optional

try:
    import numpy as np

    import vaex
except ImportError as e:
    print(json.dumps({"error": f"Missing dependency: {e}. Install: pip install vaex numpy"}))
    sys.exit(1)


def demo_basic(num_rows: int, save_path: Optional[str] = None):
    """Create a Vaex DataFrame, compute stats, filter, and group-by."""
    t0 = time.perf_counter()

    # Build a synthetic dataset in-memory (stays fast even at 100M rows thanks to numpy)
    rng = np.random.default_rng(seed=42)
    data = {
        "x": rng.standard_normal(num_rows).astype("f4"),
        "y": rng.standard_normal(num_rows).astype("f4"),
        "category": rng.integers(0, 10, num_rows).astype("i4"),
        "value": rng.exponential(scale=100.0, size=num_rows).astype("f4"),
    }
    df = vaex.from_arrays(**data)
    t_build = time.perf_counter() - t0

    # Aggregations across all rows
    t1 = time.perf_counter()
    stats = {
        "row_count": int(df.count()),
        "x_mean": float(df["x"].mean()),
        "x_std": float(df["x"].std()),
        "y_mean": float(df["y"].mean()),
        "value_sum": float(df["value"].sum()),
        "value_max": float(df["value"].max()),
    }
    t_stats = time.perf_counter() - t1

    # Filtering
    t2 = time.perf_counter()
    df_hot = df[(df.x > 0) & (df.value > 50)]
    hot_count = int(df_hot.count())
    t_filter = time.perf_counter() - t2

    # Group-by
    t3 = time.perf_counter()
    grouped = df.groupby(df.category, agg={"value_mean": vaex.agg.mean("value"), "n": vaex.agg.count("value")})
    grouped_data = grouped.to_pandas_df().to_dict(orient="records")
    t_group = time.perf_counter() - t3

    # Vaex 4.x returns a dict from __version__; extract just the core version
    vv = vaex.__version__
    vaex_ver = vv.get("vaex", str(vv)) if isinstance(vv, dict) else str(vv)

    result = {
        "vaex_version": vaex_ver,
        "rows": num_rows,
        "columns": list(df.get_column_names()),
        "timings_seconds": {
            "build": round(t_build, 3),
            "aggregations": round(t_stats, 3),
            "filter": round(t_filter, 3),
            "groupby": round(t_group, 3),
        },
        "stats": stats,
        "filtered_rows": hot_count,
        "grouped_sample": grouped_data[:3],
    }

    if save_path:
        df.export_hdf5(save_path)
        result["saved_to"] = save_path
        result["saved_bytes"] = Path(save_path).stat().st_size

    return result


def main():
    parser = argparse.ArgumentParser(description="Vaex demo: out-of-core DataFrame operations on billions of rows")
    parser.add_argument("--rows", type=int, default=10_000_000, help="Number of rows (default: 10M)")
    parser.add_argument("--save", type=str, default=None, help="Export to HDF5 at this path (optional)")
    parser.add_argument("--format", "-f", default="summary", choices=["summary", "json"], help="Output format")
    args = parser.parse_args()

    result = demo_basic(args.rows, args.save)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(f"{'=' * 60}")
        print(f"Vaex Demo (v{result['vaex_version']})")
        print(f"{'=' * 60}")
        print(f"  Rows: {result['rows']:,}")
        print(f"  Columns: {', '.join(result['columns'])}")
        print()
        print("  Timings:")
        for k, v in result["timings_seconds"].items():
            print(f"    {k:15s} {v}s")
        print()
        print("  Stats:")
        for k, v in result["stats"].items():
            if isinstance(v, float):
                print(f"    {k:15s} {v:,.4f}")
            else:
                print(f"    {k:15s} {v:,}")
        print()
        print(f"  Filtered rows (x > 0 AND value > 50): {result['filtered_rows']:,}")
        print()
        print("  Group-by (category), first 3:")
        for g in result["grouped_sample"]:
            print(f"    category={g.get('category')}: value_mean={g.get('value_mean'):.2f}, n={g.get('n')}")
        if result.get("saved_to"):
            print()
            print(f"  Saved to: {result['saved_to']} ({result['saved_bytes']:,} bytes)")


if __name__ == "__main__":
    main()
