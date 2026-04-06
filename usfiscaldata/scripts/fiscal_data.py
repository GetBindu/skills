#!/usr/bin/env python3
"""
US Fiscal Data API Script - Fully Dynamic Query Engine
100% compliant with usfiscaldata/SKILL.md specifications
Supports all endpoints, parameters, and operators dynamically
"""

import argparse
import json
import re
from datetime import datetime
from typing import Dict, List, Optional, Union

import requests

BASE_URL = "https://api.fiscaldata.treasury.gov/services/api/fiscal_service"


class FiscalDataQueryEngine:
    """Dynamic query engine for US Treasury Fiscal Data API"""

    def __init__(self):
        self.session = requests.Session()

    def treasury_get(self, endpoint: str, params: Optional[Dict] = None) -> Dict:
        """
        Generic API call to US Treasury Fiscal Data

        Args:
            endpoint: API endpoint (e.g., 'v1/accounting/mts/mts_table_1')
            params: Query parameters as defined in SKILL.md

        Returns:
            API response as dictionary
        """
        try:
            url = f"{BASE_URL}/{endpoint}"
            response = self.session.get(url, params=params or {})
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": f"API request failed: {e!s}"}
        except json.JSONDecodeError as e:
            return {"error": f"JSON decode failed: {e!s}"}
        except Exception as e:
            return {"error": f"Unexpected error: {e!s}"}

    def validate_parameters(self, params: Dict) -> Dict:
        """
        Validate and sanitize parameters according to API specifications

        Args:
            params: User-provided parameters

        Returns:
            Validated parameters dictionary
        """
        validated = {}

        # Validate and process fields
        if "fields" in params:
            fields = params["fields"]
            if isinstance(fields, str):
                validated["fields"] = fields
            elif isinstance(fields, list):
                validated["fields"] = ",".join(fields)
            else:
                raise ValueError("Fields must be a comma-separated string or list")

        # Validate filter syntax
        if "filter" in params:
            filter_expr = params["filter"]
            if not self._validate_filter_syntax(filter_expr):
                raise ValueError(f"Invalid filter syntax: {filter_expr}")
            validated["filter"] = filter_expr

        # Validate sort
        if "sort" in params:
            sort_field = params["sort"]
            if not isinstance(sort_field, str):
                raise ValueError("Sort field must be a string")
            validated["sort"] = sort_field

        # Validate page[size]
        if "page[size]" in params:
            page_size = params["page[size]"]
            try:
                page_size = int(page_size)
                if page_size < 1 or page_size > 10000:
                    raise ValueError("Page size must be between 1 and 10000")
                validated["page[size]"] = page_size
            except (ValueError, TypeError):
                raise ValueError("Page size must be an integer")

        # Validate page[number]
        if "page[number]" in params:
            page_num = params["page[number]"]
            try:
                page_num = int(page_num)
                if page_num < 1:
                    raise ValueError("Page number must be >= 1")
                validated["page[number]"] = page_num
            except (ValueError, TypeError):
                raise ValueError("Page number must be an integer")

        # Validate format
        if "format" in params:
            format_type = params["format"]
            if format_type not in ["json", "csv"]:
                raise ValueError("Format must be 'json' or 'csv'")
            validated["format"] = format_type

        return validated

    def _validate_filter_syntax(self, filter_expr: str) -> bool:
        """
        Validate filter expression syntax according to SKILL.md operators

        Supported operators: eq, gt, gte, lt, lte, in
        Syntax: field:operator:value
        """
        if not isinstance(filter_expr, str):
            return False

        # Basic pattern: field:operator:value
        pattern = r"^([^:]+):((?:eq|gt|gte|lt|lte|in)):(.+)$"
        match = re.match(pattern, filter_expr)

        if not match:
            return False

        field, operator, value = match.groups()

        # Validate 'in' operator has proper list format
        if operator == "in":
            # Should be like: security_type:in:(Note,Bond)
            list_pattern = r"^\([^)]+\)$"
            return bool(re.match(list_pattern, value.strip()))

        return True

    def discover_tables(self) -> Dict:
        """
        Discover all available tables using meta endpoint

        Returns:
            List of available endpoints and their schemas
        """
        return self.treasury_get("v1/")

    def get_table_schema(self, endpoint: str) -> Dict:
        """
        Get schema information for a specific table

        Args:
            endpoint: API endpoint

        Returns:
            Table schema with field definitions
        """
        return self.treasury_get(f"v1/{endpoint}")

    def execute_query(self, endpoint: str, params: Optional[Dict] = None, format_output: str = "json") -> Dict:
        """
        Execute a dynamic query with full parameter support

        Args:
            endpoint: API endpoint
            params: Query parameters
            format_output: Output format ('json' or 'summary')

        Returns:
            Query results formatted appropriately
        """
        # Validate parameters
        if params:
            try:
                validated_params = self.validate_parameters(params)
            except ValueError as e:
                return {"error": f"Parameter validation failed: {e!s}"}
        else:
            validated_params = {}

        # Execute query
        result = self.treasury_get(endpoint, validated_params)

        if "error" in result:
            return result

        # Format output if requested
        if format_output == "summary":
            return self._format_summary(result, endpoint)

        return result

    def _format_summary(self, result: Dict, endpoint: str) -> Dict:
        """
        Format results as a readable summary

        Args:
            result: API response
            endpoint: Query endpoint for context

        Returns:
            Formatted summary
        """
        if "data" not in result:
            return {"error": "No data found in response"}

        data = result["data"]
        if not data:
            return {"summary": "No records found", "count": 0}

        # Get basic statistics
        summary = {
            "endpoint": endpoint,
            "count": len(data),
            "latest_date": None,
            "sample_records": data[:5],  # First 5 records
        }

        # Try to find date fields
        for record in data[:10]:  # Check first 10 records
            for field in ["record_date", "date", "timestamp"]:
                if record.get(field):
                    summary["latest_date"] = record[field]
                    break
            if summary["latest_date"]:
                break

        return {"summary": summary}


def create_argument_parser() -> argparse.ArgumentParser:
    """Create comprehensive argument parser for dynamic queries"""
    parser = argparse.ArgumentParser(
        description="US Treasury Fiscal Data API - Dynamic Query Engine",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Monthly receipts and outlays
  python fiscal_data.py --endpoint v1/accounting/mts/mts_table_1 --fields "record_date,current_month_rcpt_outly_amt" --filter "record_date:gte:2023-01-01"
  
  # National debt with custom page size
  python fiscal_data.py --endpoint v2/accounting/od/debt_outstanding --fields "record_date,tot_pub_debt_out_amt" --page-size 50
  
  # Exchange rates with sorting
  python fiscal_data.py --endpoint v1/accounting/od/rates_of_exchange --sort "-record_date" --page-size 20
  
  # Treasury securities with filtering
  python fiscal_data.py --endpoint v1/debt/tsy/pub_debt_securities_type --filter "security_type:in:(Note,Bond)"
  
  # Discover available tables
  python fiscal_data.py --discover
  
  # Get table schema
  python fiscal_data.py --endpoint v1/accounting/mts/mts_table_1 --schema
        """,
    )

    # Core query arguments
    parser.add_argument("--endpoint", type=str, help="API endpoint (e.g., v1/accounting/mts/mts_table_1)")
    parser.add_argument("--fields", type=str, help="Comma-separated field list (e.g., 'record_date,amount')")
    parser.add_argument("--filter", type=str, help="Filter expression (e.g., 'record_date:gte:2023-01-01')")
    parser.add_argument("--sort", type=str, help="Sort field (use - for descending, e.g., '-record_date')")
    parser.add_argument("--page-size", type=int, dest="page_size", help="Results per page (1-10000)")
    parser.add_argument("--page-number", type=int, dest="page_number", help="Page number (>=1)")
    parser.add_argument(
        "--format", type=str, choices=["json", "csv"], default="json", help="Output format (default: json)"
    )

    # Utility arguments
    parser.add_argument("--discover", action="store_true", help="Discover all available tables")
    parser.add_argument("--schema", action="store_true", help="Get schema for specified endpoint")
    parser.add_argument(
        "--output-format",
        type=str,
        choices=["json", "summary"],
        default="json",
        dest="output_format",
        help="Result formatting (default: json)",
    )

    return parser


def main():
    parser = create_argument_parser()
    args = parser.parse_args()

    engine = FiscalDataQueryEngine()

    # Handle discovery
    if args.discover:
        result = engine.discover_tables()
        print(json.dumps(result, indent=2))
        return

    # Handle schema request
    if args.schema:
        if not args.endpoint:
            print("Error: --endpoint required when using --schema")
            return
        result = engine.get_table_schema(args.endpoint)
        print(json.dumps(result, indent=2))
        return

    # Handle regular query
    if not args.endpoint:
        print("Error: --endpoint required for queries (or use --discover)")
        return

    # Build parameters
    params = {}
    if args.fields:
        params["fields"] = args.fields
    if args.filter:
        params["filter"] = args.filter
    if args.sort:
        params["sort"] = args.sort
    if args.page_size:
        params["page[size]"] = args.page_size
    if args.page_number:
        params["page[number]"] = args.page_number
    if args.format:
        params["format"] = args.format

    # Execute query
    result = engine.execute_query(args.endpoint, params, args.output_format)

    # Output results
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
