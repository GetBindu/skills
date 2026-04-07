# Chai-1 API Reference

## Chai Discovery API
- **URL**: https://api.chaidiscovery.com/v1/predictions
- **Auth**: Bearer token (API key from chaidiscovery.com)
- **Method**: POST to submit, GET to poll status

## Quality Thresholds

| Metric | Marginal | Good | Excellent |
|--------|----------|------|-----------|
| Mean pLDDT | <60 | 60-80 | >80 |
| ipTM (complex) | <0.5 | 0.5-0.75 | >0.75 |
| Interface PAE | >20 A | 10-20 A | <10 A |

## Output Files
| File | Contents |
|------|----------|
| pred.model_idx_0.cif | Top-ranked structure (CIF) |
| pred.model_idx_0.npz | Confidence arrays (pLDDT, PAE, pDE) |
| scores.json | Aggregate scores per model |

## FASTA Input Format
- `>protein|A` — protein chain A
- `>ligand|L` — small molecule (SMILES in sequence)
- `>rna|R` — RNA sequence

## Local Requirements
- Python 3.10+, 16GB GPU VRAM (A10G+)
- `pip install chai-lab`
