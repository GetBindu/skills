# ACMG Clinical Variant Interpretation Workflow

## What this skill delegates to

This skill is a thin CLI wrapper around the [ToolUniverse](https://github.com/mims-harvard/ToolUniverse) `tooluniverse-variant-interpretation` agentic workflow. The local script is a stdlib-only argparse shim; all the heavy lifting happens upstream.

## Evidence sources aggregated by the upstream workflow

| Database | Role | Evidence type |
|----------|------|---------------|
| **ClinVar** | Clinical significance assertions | Prior classifications (P/LP/VUS/LB/B) |
| **gnomAD** | Population frequencies | Ancestry-stratified allele frequencies, pLI, LOEUF |
| **CIViC** | Cancer variant interpretation | Therapeutic/diagnostic/prognostic evidence |
| **UniProt** | Protein functional annotation | Domain info, functional regions, PTMs |
| **PDB** | Experimental protein structures | Residue positions in known structures |
| **AlphaFold2** | Predicted structures | Structural impact of missense variants (pLDDT, pLDDT deltas) |
| **ClinGen** | Gene-disease validity | Curation status, actionability |

## ACMG/AMP 2015 criteria applied

**Pathogenic evidence:**
- PVS1 — Null variant in gene where LoF is known mechanism
- PS1/PS3 — Same amino acid change as known pathogenic / functional studies
- PM1/PM2/PM5 — Mutational hot spot / absent from gnomAD / different missense at same residue
- PP2/PP3/PP5 — Missense in gene with low benign rate / multiple computational lines / reputable source

**Benign evidence:**
- BA1 — Allele frequency > 5% in any population
- BS1/BS2/BS3/BS4 — Allele frequency greater than expected / observed in healthy / no functional impact / lack of segregation
- BP1/BP2/BP3/BP4/BP6/BP7 — Missense in gene where truncating is mechanism / in trans with pathogenic / in-frame indel in repeat / multiple computational benign / reputable benign source / silent w/o splicing impact

## Output format

The workflow produces:
- **Pathogenicity score** (0-100)
- **ACMG classification** (Pathogenic / Likely Pathogenic / VUS / Likely Benign / Benign)
- **Evidence codes applied** with justification
- **Clinical recommendation** (testing cascade, counseling, therapy implications)
- **Structural impact summary** (when structure is available)

## Local script usage

```bash
# Requires: pip install tooluniverse (heavy dep — pulls API clients for all upstream sources)
python3 scripts/run.py --query "BRCA1 c.5266dupC in Ashkenazi Jewish patient with breast cancer family history"
python3 scripts/run.py --query "TP53 R175H in Li-Fraumeni context" --format summary
```

## Notes

- The upstream `tooluniverse` package bundles API clients for all listed sources. Some endpoints (CIViC, ClinVar REST) are public; others may require free registration for higher rate limits.
- ACMG classification requires at minimum a gene symbol + variant description in HGVS or cDNA notation. Context (disease, family history, ancestry) improves classification quality.
- VUS resolution rate depends heavily on how often the variant has been seen: novel variants typically land in VUS; recurrent ones get P/LP/LB/B based on accumulated evidence.
