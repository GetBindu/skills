#!/usr/bin/env python3
"""
gnomAD Database Query — Population variant frequency lookup

Query the Genome Aggregation Database (gnomAD) via GraphQL API.
No API key required.

Usage:
    python query.py --gene BRCA1
    python query.py --variant "1-55051215-G-A" --genome GRCh38
    python query.py --gene TP53 --format json
"""

import argparse
import json
import sys

try:
    import requests
except ImportError:
    print(json.dumps({"error": "requests required. Install: pip install requests"}))
    sys.exit(1)

GNOMAD_API = "https://gnomad.broadinstitute.org/api"


def query_gene(gene_symbol: str, dataset: str = "gnomad_r4", genome: str = "GRCh38") -> dict:
    """Query gnomAD for gene constraint metrics and variant summary."""
    query = """
    query GeneQuery($gene: String!, $dataset: DatasetId!, $referenceGenome: ReferenceGenomeId!) {
      gene(gene_symbol: $gene, reference_genome: $referenceGenome) {
        gene_id
        symbol
        name
        gnomad_constraint {
          pLI
          oe_lof
          oe_lof_upper
          oe_mis
          oe_mis_upper
        }
        variants(dataset: $dataset) {
          variant_id
          pos
          ref
          alt
          exome {
            ac
            an
            af
          }
          genome {
            ac
            an
            af
          }
        }
      }
    }
    """
    variables = {"gene": gene_symbol, "dataset": dataset, "referenceGenome": genome}

    try:
        resp = requests.post(GNOMAD_API, json={"query": query, "variables": variables}, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        if "errors" in data:
            return {"error": data["errors"][0].get("message", "Unknown API error"), "gene": gene_symbol}

        gene_data = data.get("data", {}).get("gene")
        if not gene_data:
            return {"error": f"Gene '{gene_symbol}' not found", "gene": gene_symbol}

        constraint = gene_data.get("gnomad_constraint") or {}
        variants = gene_data.get("variants", [])

        return {
            "status": "ok",
            "gene": gene_data.get("symbol"),
            "gene_id": gene_data.get("gene_id"),
            "name": gene_data.get("name"),
            "constraint": {
                "pLI": constraint.get("pLI"),
                "LOEUF": constraint.get("oe_lof_upper"),
                "oe_lof": constraint.get("oe_lof"),
                "oe_mis": constraint.get("oe_mis"),
            },
            "total_variants": len(variants),
            "top_variants": [
                {
                    "id": v.get("variant_id"),
                    "exome_af": v.get("exome", {}).get("af") if v.get("exome") else None,
                    "genome_af": v.get("genome", {}).get("af") if v.get("genome") else None,
                }
                for v in variants[:20]
            ],
            "dataset": dataset,
            "reference_genome": genome,
        }
    except Exception as e:
        return {"error": str(e), "gene": gene_symbol}


def query_variant(variant_id: str, dataset: str = "gnomad_r4", genome: str = "GRCh38") -> dict:
    """Query a specific variant by ID (e.g., 1-55051215-G-A)."""
    query = """
    query VariantQuery($variantId: String!, $dataset: DatasetId!, $referenceGenome: ReferenceGenomeId!) {
      variant(variantId: $variantId, dataset: $dataset, reference_genome: $referenceGenome) {
        variant_id
        chrom
        pos
        ref
        alt
        exome {
          ac
          an
          af
          populations {
            id
            ac
            an
            af
          }
        }
        genome {
          ac
          an
          af
          populations {
            id
            ac
            an
            af
          }
        }
      }
    }
    """
    variables = {"variantId": variant_id, "dataset": dataset, "referenceGenome": genome}

    try:
        resp = requests.post(GNOMAD_API, json={"query": query, "variables": variables}, timeout=30)
        resp.raise_for_status()
        data = resp.json()

        if "errors" in data:
            return {"error": data["errors"][0].get("message", "Unknown"), "variant": variant_id}

        v = data.get("data", {}).get("variant")
        if not v:
            return {"error": f"Variant '{variant_id}' not found", "variant": variant_id}

        return {
            "status": "ok",
            "variant_id": v.get("variant_id"),
            "chrom": v.get("chrom"),
            "pos": v.get("pos"),
            "ref": v.get("ref"),
            "alt": v.get("alt"),
            "exome": v.get("exome"),
            "genome": v.get("genome"),
            "dataset": dataset,
        }
    except Exception as e:
        return {"error": str(e), "variant": variant_id}


def main():
    parser = argparse.ArgumentParser(description="gnomAD Database Query")
    parser.add_argument("--gene", "-g", help="Gene symbol (e.g., BRCA1, TP53)")
    parser.add_argument("--variant", "-v", help="Variant ID (e.g., 1-55051215-G-A)")
    parser.add_argument("--dataset", default="gnomad_r4", choices=["gnomad_r4", "gnomad_r3", "gnomad_r2_1"])
    parser.add_argument("--genome", default="GRCh38", choices=["GRCh38", "GRCh37"])
    parser.add_argument("--format", "-f", default="json", choices=["json", "summary"])
    args = parser.parse_args()

    if not args.gene and not args.variant:
        parser.error("Provide --gene or --variant")

    if args.gene:
        result = query_gene(args.gene, args.dataset, args.genome)
    else:
        result = query_variant(args.variant, args.dataset, args.genome)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        if "error" in result:
            print(f"Error: {result['error']}")
        elif args.gene:
            c = result.get("constraint", {})
            print(f"gnomAD — {result['gene']} ({result.get('name', '')})")
            print(f"  pLI: {c.get('pLI', 'N/A')} | LOEUF: {c.get('LOEUF', 'N/A')}")
            print(f"  Variants: {result.get('total_variants', 0)}")
        else:
            print(f"gnomAD — {result.get('variant_id', 'unknown')}")
            exome = result.get("exome") or {}
            print(f"  Exome AF: {exome.get('af', 'N/A')}")


if __name__ == "__main__":
    main()
