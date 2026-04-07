#!/usr/bin/env python3
"""
Google Scholar Search via SerpAPI.

Searches Google Scholar for academic papers and returns title, authors,
snippet, citations, venue, year, and links.

Usage:
    python scholar_search.py --query "CRISPR delivery" --num-results 5
    python scholar_search.py --query "lithium extraction" --year-from 2020 --format json

Requires: SERPAPI_KEY env var (get one at https://serpapi.com)
"""

import argparse
import json
import os
import sys
from typing import Optional

try:
    import requests
except ImportError:
    print(json.dumps({"error": "requests required. Install: pip install requests"}))
    sys.exit(1)

SERPAPI_URL = "https://serpapi.com/search"


def search_scholar(
    query: str,
    num_results: int = 10,
    year_from: Optional[int] = None,
    year_to: Optional[int] = None,
    api_key: Optional[str] = None,
):
    """Search Google Scholar via SerpAPI."""
    key = api_key or os.environ.get("SERPAPI_KEY")
    if not key:
        return {"error": "SERPAPI_KEY env var not set. Get one at https://serpapi.com"}

    params = {
        "engine": "google_scholar",
        "q": query,
        "api_key": key,
        "num": min(num_results, 20),
    }
    if year_from:
        params["as_ylo"] = year_from
    if year_to:
        params["as_yhi"] = year_to

    try:
        r = requests.get(SERPAPI_URL, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
    except Exception as e:
        return {"error": f"SerpAPI request failed: {e}"}

    results = []
    for item in data.get("organic_results", []):
        results.append(
            {
                "title": item.get("title"),
                "snippet": item.get("snippet"),
                "link": item.get("link"),
                "citation_count": item.get("inline_links", {}).get("cited_by", {}).get("total"),
                "year": item.get("publication_info", {}).get("summary", "").split(",")[-1].strip()
                if item.get("publication_info")
                else None,
                "authors": [a.get("name") for a in item.get("publication_info", {}).get("authors", [])],
                "venue": item.get("publication_info", {}).get("summary", "").split(" - ")[0]
                if item.get("publication_info")
                else None,
            }
        )

    return {
        "query": query,
        "total_results": data.get("search_information", {}).get("total_results"),
        "results": results,
    }


def main():
    parser = argparse.ArgumentParser(description="Search Google Scholar via SerpAPI")
    parser.add_argument("--query", "-q", required=True, help="Search query")
    parser.add_argument("--num-results", "-n", type=int, default=10, help="Number of results (max 20)")
    parser.add_argument("--year-from", type=int, help="Start year filter")
    parser.add_argument("--year-to", type=int, help="End year filter")
    parser.add_argument("--api-key", help="SerpAPI key (or set SERPAPI_KEY env)")
    parser.add_argument("--format", "-f", choices=["json", "summary"], default="json")
    args = parser.parse_args()

    result = search_scholar(args.query, args.num_results, args.year_from, args.year_to, args.api_key)

    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        if "error" in result:
            print(f"Error: {result['error']}")
            return
        print(f"Google Scholar: '{args.query}' ({result.get('total_results', '?')} results)")
        for i, r in enumerate(result.get("results", []), 1):
            cite = f" [{r['citation_count']} citations]" if r.get("citation_count") else ""
            print(f"\n  {i}. {r['title']}{cite}")
            if r.get("authors"):
                print(f"     Authors: {', '.join(r['authors'][:3])}")
            if r.get("snippet"):
                print(f"     {r['snippet'][:120]}...")


if __name__ == "__main__":
    main()
