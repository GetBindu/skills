#!/usr/bin/env python3
"""
Monarch Initiative Database Query

Search for disease-gene-phenotype associations using the Monarch Initiative API v3.

Usage:
    python query.py --query "Marfan syndrome" --type disease
    python query.py --query "BRCA1" --type gene
    python query.py --query "HP:0001166" --type phenotype
    python query.py --query "MONDO:0007947" --type disease --format json
"""

import argparse
import json
import sys

try:
    import requests
except ImportError:
    print(json.dumps({"error": "requests required. Install: pip install requests"}))
    sys.exit(1)

BASE_URL = "https://api.monarchinitiative.org/v3/api"


def search_entity(query: str, category: str = None, limit: int = 10) -> dict:
    """Search Monarch for entities by name or ID."""
    params = {"q": query, "limit": limit}
    if category:
        params["category"] = category

    try:
        resp = requests.get(f"{BASE_URL}/search", params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        results = []
        for item in data.get("items", []):
            results.append(
                {
                    "id": item.get("id"),
                    "name": item.get("name"),
                    "category": item.get("category"),
                    "description": item.get("description", ""),
                }
            )
        return {"status": "ok", "query": query, "total": data.get("total", 0), "results": results}
    except Exception as e:
        return {"error": str(e), "query": query}


def get_associations(entity_id: str, assoc_type: str = "all", limit: int = 20) -> dict:
    """Get associations for a Monarch entity (disease, gene, phenotype)."""
    url = f"{BASE_URL}/entity/{entity_id}/associations"
    params = {"limit": limit}
    if assoc_type != "all":
        params["category"] = assoc_type

    try:
        resp = requests.get(url, params=params, timeout=15)
        resp.raise_for_status()
        data = resp.json()
        associations = []
        for item in data.get("items", []):
            associations.append(
                {
                    "subject_id": item.get("subject", {}).get("id"),
                    "subject_name": item.get("subject", {}).get("name"),
                    "predicate": item.get("predicate"),
                    "object_id": item.get("object", {}).get("id"),
                    "object_name": item.get("object", {}).get("name"),
                    "sources": [s.get("resource") for s in item.get("publications", [])[:3]],
                }
            )
        return {
            "status": "ok",
            "entity_id": entity_id,
            "total": data.get("total", 0),
            "associations": associations,
        }
    except Exception as e:
        return {"error": str(e), "entity_id": entity_id}


CATEGORY_MAP = {
    "disease": "biolink:Disease",
    "gene": "biolink:Gene",
    "phenotype": "biolink:PhenotypicFeature",
}


def main():
    parser = argparse.ArgumentParser(description="Monarch Initiative Database Query")
    parser.add_argument("--query", "-q", required=True, help="Search term (name, ID, or HPO term)")
    parser.add_argument(
        "--type", "-t", default=None, choices=["disease", "gene", "phenotype"], help="Entity type to search for"
    )
    parser.add_argument("--associations", "-a", action="store_true", help="Also fetch associations for top result")
    parser.add_argument("--limit", "-l", type=int, default=10, help="Max results (default: 10)")
    parser.add_argument("--format", "-f", default="json", choices=["json", "summary"])
    args = parser.parse_args()

    category = CATEGORY_MAP.get(args.type) if args.type else None
    result = search_entity(args.query, category, args.limit)

    if args.associations and result.get("results"):
        top_id = result["results"][0]["id"]
        result["associations"] = get_associations(top_id, limit=args.limit)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print(f"Monarch Initiative — Search: '{args.query}'")
        print(f"Found: {result.get('total', 0)} results")
        for r in result.get("results", [])[:5]:
            print(f"  [{r['id']}] {r['name']} ({r.get('category', 'unknown')})")
            if r.get("description"):
                print(f"    {r['description'][:100]}")


if __name__ == "__main__":
    main()
