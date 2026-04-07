# solublempnn

Solubility-optimized protein sequence design using SolubleMPNN (ProteinMPNN variant from LigandMPNN). 72% soluble expression in E. coli vs 54% for standard ProteinMPNN.

## What it does

Redesigns protein sequences to improve aqueous solubility while preserving structure. Based on the LigandMPNN architecture from dauparas/LigandMPNN. Includes post-design filtering (GRAVY, instability index, liability scanning) and multi-chain complex support.

## Setup

Requires cloning the upstream [LigandMPNN repo](https://github.com/dauparas/LigandMPNN):

```bash
git clone https://github.com/dauparas/LigandMPNN.git && cd LigandMPNN
conda create -n solublempnn python=3.9 pytorch -c pytorch
conda activate solublempnn && pip install prody numpy
bash get_model_params.sh
```

## Environment variables

None. GPU recommended but CPU works for small designs.

## Usage

```bash
python3 scripts/info.py --info                # setup instructions
python3 scripts/info.py --check-deps          # check torch/numpy/prody
# After upstream setup:
python run.py --model_type soluble_mpnn --pdb_path input.pdb --out_folder output/
```

## Dependencies

PyTorch, NumPy, ProDy (info script: stdlib only)

## Tested with

- **`info.py --info`:** ✅
- **`info.py --check-deps`:** ✅
- **Agno (Claude Haiku 4.5):** ✅ "72% soluble expression rate in E. coli vs 54% standard ProteinMPNN"
