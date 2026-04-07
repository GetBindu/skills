#!/usr/bin/env python3
"""
TileDB-VCF Variant Query Tool

Query genomic variants from a TileDB-VCF dataset.

Usage:
    python query_variants.py --uri path/to/variants.tdb --regions chr1:1-100000
    python query_variants.py --uri s3://bucket/variants/ --regions chr17:7571720-7590868 --samples SAMPLE_001
    python query_variants.py --uri path/to/variants.tdb --regions chr7:117559590-117559600 --format json
"""

import argparse
import json


def query_variants(uri: str, regions: list, samples: list = None, attrs: list = None) -> dict:
    """Query variants from a TileDB-VCF dataset."""
    try:
        import tiledbvcf
    except ImportError:
        return {
            "error": "tiledbvcf not installed",
            "install": "conda install -c conda-forge -c tiledb tiledb-vcf",
            "alt_install": "pip install tiledb-vcf (limited functionality)",
            "docker": "docker pull tiledb/tiledb-vcf:latest",
        }

    if attrs is None:
        attrs = ["sample_name", "contig", "pos_start", "pos_end", "alleles", "fmt_GT"]

    try:
        ds = tiledbvcf.Dataset(uri, mode="r")
        df = ds.read(
            attrs=attrs,
            regions=regions,
            samples=samples,
        )
        records = df.to_dict(orient="records")
        # Convert non-serializable types
        for rec in records:
            for k, v in rec.items():
                if hasattr(v, "tolist"):
                    rec[k] = v.tolist()
                elif isinstance(v, (list, tuple)):
                    rec[k] = [str(x) for x in v]

        return {
            "status": "ok",
            "uri": uri,
            "regions": regions,
            "total_records": len(records),
            "records": records[:1000],  # Cap at 1000 for output
            "truncated": len(records) > 1000,
        }
    except Exception as e:
        return {"error": str(e), "uri": uri, "regions": regions}


def main():
    parser = argparse.ArgumentParser(description="Query TileDB-VCF variants")
    parser.add_argument("--uri", required=True, help="TileDB-VCF dataset URI (local path or s3://)")
    parser.add_argument("--regions", required=True, nargs="+", help="Genomic regions (e.g., chr1:1-100000)")
    parser.add_argument("--samples", nargs="+", default=None, help="Sample names to filter")
    parser.add_argument(
        "--attrs",
        nargs="+",
        default=["sample_name", "contig", "pos_start", "pos_end", "alleles", "fmt_GT"],
        help="Attributes to return",
    )
    parser.add_argument("--format", "-f", default="json", choices=["json", "summary"])
    args = parser.parse_args()

    result = query_variants(args.uri, args.regions, args.samples, args.attrs)

    if args.format == "json":
        print(json.dumps(result, indent=2, default=str))
    else:
        if "error" in result:
            print(f"Error: {result['error']}")
        else:
            print("TileDB-VCF Query Results")
            print(f"URI: {result['uri']}")
            print(f"Regions: {', '.join(result['regions'])}")
            print(f"Total records: {result['total_records']}")
            for rec in result.get("records", [])[:10]:
                print(
                    f"  {rec.get('contig', '?')}:{rec.get('pos_start', '?')} "
                    f"{rec.get('alleles', '?')} GT={rec.get('fmt_GT', '?')} "
                    f"[{rec.get('sample_name', '?')}]"
                )


if __name__ == "__main__":
    main()
