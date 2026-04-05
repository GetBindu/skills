# xlsx

Extract and preview data from Excel (`.xlsx`, `.xls`) and CSV spreadsheets as structured JSON.

## What it does

Parses spreadsheet files and returns a JSON summary containing the sheet names, the first N rows of each sheet, and the total row/column count. Primarily intended for previewing scientific supplementary data (publication tables, high-throughput screening results, omics datasets) before full analysis. Uses `openpyxl` for `.xlsx` and falls back to `pandas` when `openpyxl` is not installed or when processing `.csv` / `.xls` files.

## Setup

```bash
cd xlsx
python3 -m venv .venv && source .venv/bin/activate && pip install openpyxl pandas -q
```

## Environment variables

None. Purely local file processing.

## Usage

### Input
```bash
python3 scripts/xlsx_extract.py --file /path/to/supplementary.xlsx --head 3
```

### Output
```json
{
  "file": "/tmp/test_supplementary.xlsx",
  "sheets": ["Genes", "Samples"],
  "data": {
    "Genes": [
      ["Gene", "Log2FC", "pvalue", "FDR"],
      ["BRCA1", "2.4", "0.0001", "0.001"],
      ["TP53", "-1.8", "0.003", "0.02"]
    ],
    "Samples": [
      ["SampleID", "Group"],
      ["S1", "control"],
      ["S2", "treated"]
    ]
  },
  "shape": {"rows": 5, "cols": 4},
  "extractor": "openpyxl"
}
```

### Other input modes
```bash
# Preview all sheets with default 20 rows each
python3 scripts/xlsx_extract.py --file /path/to/data.xlsx

# Only one sheet
python3 scripts/xlsx_extract.py --file /path/to/data.xlsx --sheet "Table S1"

# Larger preview
python3 scripts/xlsx_extract.py --file /path/to/screening.xlsx --head 100

# CSV files
python3 scripts/xlsx_extract.py --file /path/to/results.csv
```

## CLI flags

| Flag | Description | Default |
|------|-------------|---------|
| `--file` | Path to `.xlsx`, `.xls`, or `.csv` file (required) | — |
| `--sheet` | Sheet name (Excel only; omit for all sheets) | all |
| `--head` | Number of rows to preview per sheet | 20 |

## Dependencies

- `openpyxl` (primary, for `.xlsx`)
- `pandas` (fallback + `.csv` + `.xls` support)

Either is sufficient for basic operation; install both for the fullest coverage.

## Tested with

- **Direct script run:** ✅ Extracted 2 sheets from a test xlsx fixture (Genes + Samples), returned headers and data rows correctly, reported shape `{rows: 5, cols: 4}`
- **Agno agent (Claude Haiku 4.5 via OpenRouter):** ✅ Agent loaded instructions, executed `xlsx_extract.py --file /tmp/test_supplementary.xlsx --head 3` via `get_skill_script(execute=True)`, parsed the JSON output, and explained the skill. Initially used wrong arg name (`--xlsx-file`), self-corrected to `--file`.

### Agno agent verdict (excerpt)
> The script successfully extracted data from /tmp/test_supplementary.xlsx with the --head 3 limit, returning: 2 sheets (Genes and Samples), first 3 rows from each sheet, shape info (5 total rows, 4 columns), extractor: openpyxl. This is ideal for quickly previewing scientific datasets, supplementary tables from publications, or screening results before performing detailed analysis.
