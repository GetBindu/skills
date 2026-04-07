---
name: eu-pesticide-database
description: Query EU pesticide approval status and Maximum Residue Limits from European Commission
---
# EU Pesticide Database

Access EU pesticide approval status and Maximum Residue Limits for agricultural export compliance.

## Overview

The EU Pesticide Database provides approval/ban status of active substances and Maximum Residue Limits (MRLs) for pesticides on food crops. The EU has the strictest pesticide regulations globally, creating significant export compliance challenges.

## Usage

### Query pesticide approval and MRLs:
```bash
python3 {baseDir}/scripts/query.py --pesticide "glyphosate" --crop "soybeans"
```

### Check approval status:
```bash
python3 {baseDir}/scripts/query.py --pesticide "neonicotinoids" --query-type approval_status
```

### Query MRLs for export compliance:
```bash
python3 {baseDir}/scripts/query.py --pesticide "atrazine" --crop "maize" --query-type mrl
```

## Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| `--pesticide` | Pesticide active substance | Required |
| `--crop` | Crop name for MRL query | - |
| `--query-type` | approval_status, mrl, or both | both |
| `--format` | Output format: summary, json | json |

## Query Types

- **approval_status** - EU approval/ban status
- **mrl** - Maximum Residue Limits by crop
- **both** - Both approval and MRL data

## Examples

### Export compliance risk assessment (Use Case #2):
```bash
# Check if Brazilian soybeans can be exported to EU
python3 {baseDir}/scripts/query.py --pesticide "glyphosate" --crop "soybeans"

# Codex MRL: 20 mg/kg
# EU MRL: 0.05 mg/kg (effectively a ban)
# US MRL: 40 mg/kg
# 800x range between jurisdictions!
```

### Track regulatory changes:
```bash
python3 {baseDir}/scripts/query.py --pesticide "chlorpyrifos" --query-type approval_status
```

## Use Cases

**Export Compliance Risk Assessment**: Check if crops treated with specific pesticides can be exported to EU

**MRL Contradiction Finding**: Compare EU MRLs against Codex, US EPA, and other jurisdictions

**Regulatory Tracking**: Monitor pesticide approval/ban decisions affecting agricultural trade

## Notes

- No official API (requires web scraping)
- Continuous regulatory updates
- EU MRLs often 10-1000x stricter than other jurisdictions
- Single shipment rejection costs $500K-2M
- Critical for multinational crop traders (Cargill, ADM, Bunge, Louis Dreyfus)
