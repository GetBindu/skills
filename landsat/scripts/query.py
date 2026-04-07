#!/usr/bin/env python3
"""
Landsat Satellite Imagery Query Script

Query Landsat imagery from NASA/USGS with 50+ year archive.

Usage:
    python query.py --north 42.1 --south 42.0 --east -93.5 --west -93.7 --start 2023-06-01 --end 2023-09-30
    python query.py --path 26 --row 31 --start 1990-01-01 --end 1990-12-31 --collection landsat-5
"""

import argparse
import json
import os
import sys
from typing import Dict, Optional

try:
    from landsatxplore.api import API
    from landsatxplore.earthexplorer import EarthExplorer
except ImportError:
    print("Error: landsatxplore is required. Install with: pip install landsatxplore")
    sys.exit(1)


def query_landsat(
    north: Optional[float] = None,
    south: Optional[float] = None,
    east: Optional[float] = None,
    west: Optional[float] = None,
    path: Optional[int] = None,
    row: Optional[int] = None,
    start_date: str = None,
    end_date: str = None,
    collection: str = "landsat-8",
    cloud_max: int = 20,
    username: str = None,
    password: str = None,
) -> Dict:
    """
    Query Landsat imagery via USGS Earth Explorer.

    Args:
        north, south, east, west: Bounding box coordinates
        path, row: Landsat path/row (alternative to bbox)
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        collection: Landsat collection (landsat-5, landsat-7, landsat-8, landsat-9)
        cloud_max: Maximum cloud cover percentage
        username: USGS username (or set USGS_USER env var)
        password: USGS password (or set USGS_PASSWORD env var)

    Returns:
        Dictionary with imagery metadata
    """
    if not username:
        username = os.environ.get("USGS_USER")
    if not password:
        password = os.environ.get("USGS_PASSWORD")

    if not username or not password:
        return {
            "error": "USGS credentials required",
            "note": "Register at https://ers.cr.usgs.gov/register/ and set USGS_USER and USGS_PASSWORD",
        }

    # Map collection names to dataset IDs
    dataset_map = {
        "landsat-5": "landsat_tm_c2_l2",
        "landsat-7": "landsat_etm_c2_l2",
        "landsat-8": "landsat_ot_c2_l2",
        "landsat-9": "landsat_ot_c2_l2",
    }

    dataset = dataset_map.get(collection, "landsat_ot_c2_l2")

    try:
        api = API(username, password)

        # Search for scenes
        if path and row:
            scenes = api.search(
                dataset=dataset, start_date=start_date, end_date=end_date, path=path, row=row, max_cloud_cover=cloud_max
            )
        elif all([north, south, east, west]):
            bbox = (west, south, east, north)
            scenes = api.search(
                dataset=dataset, bbox=bbox, start_date=start_date, end_date=end_date, max_cloud_cover=cloud_max
            )
        else:
            api.logout()
            return {"error": "Provide either bbox (north/south/east/west) or path/row"}

        api.logout()

        # Format results
        imagery_list = []
        for scene in scenes:
            imagery_list.append(
                {
                    "scene_id": scene.get("display_id", ""),
                    "entity_id": scene.get("entity_id", ""),
                    "date": scene.get("acquisition_date", ""),
                    "cloud_cover": scene.get("cloud_cover", ""),
                    "path": scene.get("wrs_path", ""),
                    "row": scene.get("wrs_row", ""),
                    "collection": collection,
                }
            )

        return {
            "query": {
                "area": {"north": north, "south": south, "east": east, "west": west} if north else None,
                "path_row": {"path": path, "row": row} if path else None,
                "start_date": start_date,
                "end_date": end_date,
                "collection": collection,
                "cloud_max": cloud_max,
            },
            "imagery": imagery_list,
            "total": len(imagery_list),
            "source": "Landsat (NASA/USGS)",
        }

    except Exception as e:
        return {"error": str(e)}


def format_summary(result: Dict) -> str:
    """Format Landsat query as summary."""
    if "error" in result:
        return f"Error: {result['error']}\n{result.get('note', '')}"

    lines = ["\nLandsat Imagery Query"]
    if result["query"].get("area"):
        area = result["query"]["area"]
        lines.append(f"Area: ({area['south']}, {area['west']}) to ({area['north']}, {area['east']})")
    if result["query"].get("path_row"):
        pr = result["query"]["path_row"]
        lines.append(f"Path/Row: {pr['path']}/{pr['row']}")
    lines.append(f"Period: {result['query']['start_date']} to {result['query']['end_date']}")
    lines.append(f"Collection: {result['query']['collection']}")
    lines.append(f"\nFound {result['total']} scenes\n")
    lines.append("-" * 80)

    if result.get("imagery"):
        lines.append("\nAvailable scenes:")
        for i, img in enumerate(result["imagery"][:10], 1):
            lines.append(f"\n{i}. {img['scene_id']}")
            lines.append(f"   Date: {img['date']}, Cloud: {img['cloud_cover']}%")
            lines.append(f"   Path/Row: {img['path']}/{img['row']}")

    lines.append("\n" + "-" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query Landsat satellite imagery",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --north 42.1 --south 42.0 --east -93.5 --west -93.7 --start 2023-06-01 --end 2023-09-30
  %(prog)s --path 26 --row 31 --start 1990-01-01 --end 1990-12-31 --collection landsat-5
  
Collections: landsat-5 (1984-2013), landsat-7 (1999-present), landsat-8 (2013-present), landsat-9 (2021-present)
Register at: https://ers.cr.usgs.gov/register/
        """,
    )

    parser.add_argument("--north", type=float, help="Northern latitude")
    parser.add_argument("--south", type=float, help="Southern latitude")
    parser.add_argument("--east", type=float, help="Eastern longitude")
    parser.add_argument("--west", type=float, help="Western longitude")
    parser.add_argument("--path", type=int, help="Landsat path")
    parser.add_argument("--row", type=int, help="Landsat row")
    parser.add_argument("--start", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--collection", default="landsat-8", help="Landsat collection (default: landsat-8)")
    parser.add_argument("--cloud-max", type=int, default=20, help="Max cloud cover %% (default: 20)")
    parser.add_argument("--username", help="USGS username (or set USGS_USER)")
    parser.add_argument("--password", help="USGS password (or set USGS_PASSWORD)")
    parser.add_argument("--format", "-f", default="json", choices=["summary", "json"], help="Output format")

    args = parser.parse_args()

    try:
        result = query_landsat(
            north=args.north,
            south=args.south,
            east=args.east,
            west=args.west,
            path=args.path,
            row=args.row,
            start_date=args.start,
            end_date=args.end,
            collection=args.collection,
            cloud_max=args.cloud_max,
            username=args.username,
            password=args.password,
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
