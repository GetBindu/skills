# SolubleMPNN Design Reference

## Upstream
[dauparas/LigandMPNN](https://github.com/dauparas/LigandMPNN) — SolubleMPNN is a variant of ProteinMPNN optimized for aqueous solubility.

## Key parameters

| Flag | Description |
|------|-------------|
| `--model_type soluble_mpnn` | Use the solubility-optimized model weights |
| `--pdb_path` | Input PDB structure file |
| `--out_folder` | Output directory for designed sequences |
| `--number_of_batches` | Number of design batches (default: 1) |
| `--temperature` | Sampling temperature (lower = more conservative) |

## Post-design quality filters

| Metric | Threshold | Description |
|--------|-----------|-------------|
| GRAVY score | < 0 (hydrophilic) | Grand average of hydropathicity |
| Instability index | < 40 | Protein stability prediction |
| Charge at pH 7 | -5 to +5 | Net charge at physiological pH |
| Liability scan | No flags | Check for deamidation/oxidation/cleavage motifs |

## Use cases

- Reducing inclusion bodies in E. coli expression
- Improving yields in cell-free expression systems
- Designing soluble binder variants
- Multi-chain complex design with solubility constraints
