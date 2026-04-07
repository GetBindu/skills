#!/usr/bin/env python3
"""
GBIF Biodiversity Database Query Script

Query species occurrence records from Global Biodiversity Information Facility.

Usage:
    python query.py --species "Apis mellifera" --country "US"
    python query.py --species "Bombus" --lat 42.0 --lon -93.6 --radius 50
"""

import argparse
import json
import sys
from typing import Dict, Optional

try:
    import requests
except ImportError:
    print("Error: requests is required. Install with: pip install requests")
    sys.exit(1)

GBIF_API = "https://api.gbif.org/v1"


def query_gbif(
    scientific_name: Optional[str] = None,
    country: Optional[str] = None,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
    radius_km: Optional[int] = None,
    year_start: Optional[int] = None,
    year_end: Optional[int] = None,
    limit: int = 20,
) -> Dict:
    """
    Query GBIF occurrence database.

    Args:
        scientific_name: Species scientific name
        country: Country code (e.g., 'US', 'IN')
        latitude: Latitude for geographic search
        longitude: Longitude for geographic search
        radius_km: Search radius in kilometers
        year_start: Start year
        year_end: End year
        limit: Maximum results

    Returns:
        Dictionary with occurrence data
    """
    occurrence_url = f"{GBIF_API}/occurrence/search"

    params = {"limit": limit}

    if scientific_name:
        params["scientificName"] = scientific_name

    if country:
        params["country"] = country.upper()

    if latitude is not None and longitude is not None:
        params["decimalLatitude"] = f"{latitude - 0.5},{latitude + 0.5}"
        params["decimalLongitude"] = f"{longitude - 0.5},{longitude + 0.5}"

    if year_start:
        params["year"] = f"{year_start},{year_end or year_start}"

    try:
        response = requests.get(occurrence_url, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        occurrences = []
        for result in data.get("results", []):
            occurrences.append(
                {
                    "species": result.get("species", ""),
                    "scientific_name": result.get("scientificName", ""),
                    "latitude": result.get("decimalLatitude"),
                    "longitude": result.get("decimalLongitude"),
                    "country": result.get("country", ""),
                    "year": result.get("year"),
                    "month": result.get("month"),
                    "basis_of_record": result.get("basisOfRecord", ""),
                    "dataset": result.get("datasetName", ""),
                    "gbif_id": result.get("key"),
                }
            )

        return {
            "query": {
                "scientific_name": scientific_name,
                "country": country,
                "location": {"latitude": latitude, "longitude": longitude} if latitude else None,
            },
            "occurrences": occurrences,
            "total": data.get("count", 0),
            "source": "GBIF - Global Biodiversity Information Facility",
        }

    except requests.RequestException as e:
        print(f"Error querying GBIF API: {e}", file=sys.stderr)
        return {"error": str(e)}


def format_summary(result: Dict) -> str:
    """Format GBIF data as summary."""
    if "error" in result:
        return f"Error: {result['error']}"

    lines = ["\nGBIF Occurrence Search"]
    if result["query"].get("scientific_name"):
        lines.append(f"Species: {result['query']['scientific_name']}")
    if result["query"].get("country"):
        lines.append(f"Country: {result['query']['country']}")
    lines.append(f"Total occurrences: {result['total']}\n")
    lines.append("-" * 80)

    if result.get("occurrences"):
        lines.append(f"\nShowing {len(result['occurrences'])} records:")
        for i, occ in enumerate(result["occurrences"][:10], 1):
            loc = f"({occ['latitude']:.4f}, {occ['longitude']:.4f})" if occ.get("latitude") else "No coordinates"
            year = occ.get("year", "Unknown year")
            lines.append(f"\n{i}. {occ['scientific_name']}")
            lines.append(f"   Location: {loc}, {occ.get('country', '')}")
            lines.append(f"   Year: {year}, Basis: {occ.get('basis_of_record', '')}")

    lines.append("\n" + "-" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query GBIF biodiversity database",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --species "Apis mellifera" --country "US"
  %(prog)s --species "Bombus" --lat 42.0 --lon -93.6
  %(prog)s --species "Monarch butterfly" --year-start 2020 --year-end 2023
        """,
    )

    parser.add_argument("--species", "-s", help="Species scientific name")
    parser.add_argument("--country", "-c", help="Country code (e.g., US, IN, BR)")
    parser.add_argument("--lat", "--latitude", type=float, help="Latitude for geographic search")
    parser.add_argument("--lon", "--longitude", type=float, help="Longitude for geographic search")
    parser.add_argument("--year-start", type=int, help="Start year")
    parser.add_argument("--year-end", type=int, help="End year")
    parser.add_argument("--limit", "-l", type=int, default=20, help="Maximum results (default: 20)")
    parser.add_argument(
        "--format", "-f", default="json", choices=["summary", "json"], help="Output format (default: json)"
    )

    args = parser.parse_args()

    try:
        result = query_gbif(
            scientific_name=args.species,
            country=args.country,
            latitude=args.lat,
            longitude=args.lon,
            year_start=args.year_start,
            year_end=args.year_end,
            limit=args.limit,
        )

        if args.format == "json":
            print(json.dumps(result, indent=2))
        else:
            print(format_summary(result))

    except Exception as e:
        print(f"Error: {e!s}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
