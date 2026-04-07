---
name: epa-comptox
description: Query chemical toxicity data from EPA CompTox Dashboard for 880,000+ chemicals
---
# EPA CompTox Dashboard

Access comprehensive chemical toxicity and property data from the US Environmental Protection Agency.

## Overview

EPA CompTox Chemicals Dashboard provides data on 880,000+ chemicals including toxicity endpoints, physicochemical properties, bioactivity data, and regulatory status.

## Usage

### Query chemical by name:
```bash
python3 {baseDir}/scripts/query.py --chemical "glyphosate" --data-type toxicity
```

### Get chemical properties:
```bash
python3 {baseDir}/scripts/query.py --chemical "atrazine" --format json
```

### Query by CAS number:
```bash
python3 {baseDir}/scripts/query.py --chemical "1071-83-6" --data-type properties
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--chemical` | Chemical name, CAS, or DTXSID | Required |
| `--data-type` | Data type to retrieve | - |
| `--format` | Output format: summary, json | json |

## Data Types

- **toxicity** - Toxicity endpoints (LD50, LC50, NOAEL, LOAEL)
- **properties** - Physicochemical properties
- **bioactivity** - High-throughput screening data

## Examples

### Pesticide safety assessment:
```bash
python3 {baseDir}/scripts/query.py --chemical "glyphosate" --data-type toxicity
```

### Regulatory contradiction finding:
```bash
# Compare EPA toxicity data against EU EFSA assessments
python3 {baseDir}/scripts/query.py --chemical "chlorpyrifos" --data-type toxicity
# EPA values often differ from EU/international databases
```

## Use Cases

**Pesticide Safety Assessment**: Compare EPA toxicity data against EU EFSA and international assessments

**Regulatory Contradiction Finding**: Identify chemicals where toxicity values differ between jurisdictions

**Chemical Property Validation**: Cross-check physicochemical properties against manufacturer data

## Notes

- Free API access, no key required
- 880,000+ chemicals
- Continuous updates
- Toxicity values may differ from EU/international databases
- Perfect for regulatory contradiction finding
