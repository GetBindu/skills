# opentargets-database

Query Open Targets Platform for target-disease associations, drug target discovery, tractability/safety data, genetics/omics evidence, known drugs, for therapeutic target identification.

## Setup

```bash
cd opentargets-database
python3 -m venv .venv && source .venv/bin/activate && pip install requests -q
```

## Environment variables

None.

## Usage

```bash
python3 scripts/query_opentargets.py --help
```

## Dependencies

- `requests`
