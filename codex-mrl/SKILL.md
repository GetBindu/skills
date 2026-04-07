---
name: codex-mrl
description: Query international Maximum Residue Limits for pesticides from Codex Alimentarius (WHO/FAO)
---
# Codex Alimentarius MRL Database

Access internationally harmonized pesticide Maximum Residue Limits from the Codex Alimentarius Commission.

## Overview

Codex Alimentarius sets international food safety standards including Maximum Residue Limits (MRLs) for pesticides. Codex MRLs serve as the international baseline and are used in WTO dispute resolution.

## Usage

### Query MRLs for pesticide-crop combination:
```bash
python3 {baseDir}/scripts/query.py --pesticide "glyphosate" --commodity "soybeans"
```

### Query all MRLs for a pesticide:
```bash
python3 {baseDir}/scripts/query.py --pesticide "chlorpyrifos" --format json
```

### Check international standards:
```bash
python3 {baseDir}/scripts/query.py --pesticide "imidacloprid" --commodity "wheat"
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--pesticide` | Pesticide active ingredient | Required |
| `--commodity` | Food commodity | - |
| `--format` | Output format: summary, json | json |

## Examples

### Cross-jurisdiction MRL comparison (Use Case #2):
```bash
# Query Codex baseline
python3 {baseDir}/scripts/query.py --pesticide "glyphosate" --commodity "soybeans"

# Codex MRL: 20 mg/kg (international baseline)
# EU MRL: 0.05 mg/kg (800x stricter!)
# US MRL: 40 mg/kg (2x more permissive)
# Japan MRL: 30 mg/kg
# 
# Same chemical, same crop, 800x range
# Creates massive export compliance challenges
```

### Trade compliance analysis:
```bash
python3 {baseDir}/scripts/query.py --pesticide "chlorpyrifos" --commodity "wheat"
```

## Use Cases

**Cross-Jurisdiction MRL Comparison**: Compare Codex vs EU vs US vs Japan MRLs for same pesticide-crop combination

**Trade Compliance Analysis**: Identify crops where national MRLs are stricter than Codex (export barriers)

**Regulatory Divergence Tracking**: Monitor when countries deviate from international standards

## Notes

- No official API (requires web scraping)
- 200+ pesticides, 300+ commodities
- Updated annually by Codex Committee on Pesticide Residues
- Adopted by 120+ countries
- Used in WTO dispute resolution
- National MRLs often differ dramatically from Codex
- Perfect for systematic contradiction detection across jurisdictions
