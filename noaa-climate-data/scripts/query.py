#!/usr/bin/env python3
"""
NOAA Climate Data Online Query Script

Query historical weather and climate data from NOAA.

Usage:
    python query.py --lat 42.0308 --lon -93.6319 --start-date 2023-04-01 --end-date 2023-10-31
    python query.py --station-id GHCND:USW00014933 --start-date 2023-01-01 --end-date 2023-12-31
"""

import argparse
import json
import os
import sys
from typing import Dict, List, Optional

try:
    import requests
except ImportError:
    print("Error: requests is required. Install with: pip install requests")
    sys.exit(1)

NOAA_API = "https://www.ncdc.noaa.gov/cdo-web/api/v2"


def query_noaa_climate(
    start_date: str,
    end_date: str,
    latitude: Optional[float] = None,
    longitude: Optional[float] = None,
    station_id: Optional[str] = None,
    data_types: Optional[List[str]] = None,
    api_key: Optional[str] = None,
) -> Dict:
    """
    Query NOAA Climate Data Online API.

    Args:
        start_date: Start date (YYYY-MM-DD)
        end_date: End date (YYYY-MM-DD)
        latitude: Latitude coordinate (optional)
        longitude: Longitude coordinate (optional)
        station_id: NOAA station ID (optional)
        data_types: Data types (e.g., ['TMAX', 'TMIN', 'PRCP'])
        api_key: NOAA API key (or set NOAA_API_KEY env var)

    Returns:
        Dictionary with climate data
    """
    if not api_key:
        api_key = os.environ.get("NOAA_API_KEY")

    if not api_key:
        raise ValueError("NOAA API key required. Set NOAA_API_KEY environment variable or pass --api-key")

    headers = {"token": api_key}

    # If lat/lon provided, find nearest station
    if latitude is not None and longitude is not None and not station_id:
        station_url = f"{NOAA_API}/stations"
        station_params = {"extent": f"{latitude},{longitude},{latitude},{longitude}", "limit": 1}
        try:
            station_response = requests.get(station_url, headers=headers, params=station_params, timeout=30)
            station_response.raise_for_status()
            station_data = station_response.json()
            if station_data.get("results"):
                station_id = station_data["results"][0]["id"]
        except Exception:
            pass

    if not station_id:
        return {"error": "Could not determine station. Provide station_id or valid lat/lon coordinates"}

    # Query data
    data_url = f"{NOAA_API}/data"
    params = {
        "datasetid": "GHCND",  # Global Historical Climatology Network Daily
        "stationid": station_id,
        "startdate": start_date,
        "enddate": end_date,
        "limit": 1000,
    }

    if data_types:
        params["datatypeid"] = ",".join(data_types)

    try:
        response = requests.get(data_url, headers=headers, params=params, timeout=30)
        response.raise_for_status()
        data = response.json()

        climate_data = {
            "station_id": station_id,
            "start_date": start_date,
            "end_date": end_date,
            "data": [],
            "source": "NOAA Climate Data Online",
        }

        if data.get("results"):
            for record in data["results"]:
                climate_data["data"].append(
                    {
                        "date": record.get("date", "")[:10],
                        "datatype": record.get("datatype", ""),
                        "value": record.get("value", ""),
                        "attributes": record.get("attributes", ""),
                    }
                )

        return climate_data

    except requests.RequestException as e:
        print(f"Error querying NOAA API: {e}", file=sys.stderr)
        return {"error": str(e)}


def format_summary(climate_data: Dict) -> str:
    """Format climate data as summary."""
    if "error" in climate_data:
        return f"Error: {climate_data['error']}"

    lines = ["\nNOAA Climate Data"]
    lines.append(f"Station: {climate_data['station_id']}")
    lines.append(f"Period: {climate_data['start_date']} to {climate_data['end_date']}\n")
    lines.append("-" * 80)

    if climate_data.get("data"):
        lines.append(f"\nFound {len(climate_data['data'])} records")
        lines.append("\nSample (first 10 records):")
        for record in climate_data["data"][:10]:
            lines.append(f"  {record['date']}: {record['datatype']} = {record['value']}")
    else:
        lines.append("\nNo data found for this period")

    lines.append("\n" + "-" * 80)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Query NOAA Climate Data Online",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --lat 42.0308 --lon -93.6319 --start-date 2023-04-01 --end-date 2023-10-31
  %(prog)s --station-id GHCND:USW00014933 --start-date 2023-01-01 --end-date 2023-12-31
  %(prog)s --lat 28.5 --lon 77.2 --start-date 2023-06-01 --end-date 2023-09-30 --data-types TMAX TMIN PRCP
        """,
    )

    parser.add_argument("--lat", "--latitude", type=float, help="Latitude coordinate")
    parser.add_argument("--lon", "--longitude", type=float, help="Longitude coordinate")
    parser.add_argument("--station-id", help="NOAA station ID (e.g., GHCND:USW00014933)")
    parser.add_argument("--start-date", required=True, help="Start date (YYYY-MM-DD)")
    parser.add_argument("--end-date", required=True, help="End date (YYYY-MM-DD)")
    parser.add_argument("--data-types", nargs="+", help="Data types (e.g., TMAX TMIN PRCP)")
    parser.add_argument("--api-key", help="NOAA API key (or set NOAA_API_KEY env var)")
    parser.add_argument(
        "--format", "-f", default="json", choices=["summary", "json"], help="Output format (default: json)"
    )

    args = parser.parse_args()

    try:
        climate_data = query_noaa_climate(
            start_date=args.start_date,
            end_date=args.end_date,
            latitude=args.lat,
            longitude=args.lon,
            station_id=args.station_id,
            data_types=args.data_types,
            api_key=args.api_key,
        )

        if args.format == "json":
            print(json.dumps(climate_data, indent=2))
        else:
            print(format_summary(climate_data))

    except Exception as e:
        print(f"Error: {e!s}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
