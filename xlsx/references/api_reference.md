# xlsx Extract API Reference

## Supported formats
- `.xlsx` — via `openpyxl` (primary) or `pandas` (fallback)
- `.xls` — via `pandas` (`openpyxl` doesn't support `.xls`, needs `xlrd`)
- `.csv` — via `pandas`

## Dependency chain
1. For `.xlsx`/`.xls`: try `openpyxl` first, fall back to `pandas` if not installed
2. For `.csv`: always uses `pandas`
3. If neither is available, returns clean JSON error with install instructions

## Output schema

```json
{
  "file": "/path/to/file.xlsx",
  "sheets": ["Sheet1", "Sheet2"],
  "data": {
    "Sheet1": [
      ["header1", "header2", "header3"],
      ["row1col1", "row1col2", "row1col3"]
    ]
  },
  "shape": {"rows": 1250, "cols": 8},
  "extractor": "openpyxl"
}
```

## Fields
| Field | Type | Description |
|-------|------|-------------|
| `file` | string | Absolute path of input file |
| `sheets` | string[] | All sheet names in the workbook |
| `data` | object | Map of sheet name → 2D array (first `--head` rows only) |
| `data[sheet][0]` | string[] | Header row (when pandas extractor) / first row (openpyxl) |
| `shape.rows` | int | Total row count across all sheets |
| `shape.cols` | int | Max column count across all sheets |
| `extractor` | string | Which backend was used: `openpyxl` or `pandas` |

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--file` | Path to `.xlsx`, `.xls`, or `.csv` file (required) | — |
| `--sheet` | Sheet name to extract from (Excel only) | all sheets |
| `--head` | Number of rows to preview per sheet | 20 |

## Error responses

All errors return JSON on stdout with `{"error": "...", "file": "..."}` and exit code 1:
- File not found
- Unsupported extension
- Missing `openpyxl` AND `pandas`
- Parsing errors inside the file
