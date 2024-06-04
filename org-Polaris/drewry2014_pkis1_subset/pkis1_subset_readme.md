![kinase](https://storage.googleapis.com/polaris-public/icons/icons8-fox-60-kinases.png)

## Background:
 Kinases play a crucial role in cellular signalling, making them important targets for drug development. Dysregulation of kinases is frequently implicated in diseases like cancer, inflammation, and neurodegenerative disorders. Therefore, targeting kinases with specific drugs has emerged as a crucial strategy in modern drug discovery. Kinase-related task includes inhibition prediction, selectivity prediction, or kinase-ligand binding affinity prediction. In the early release version of Polaris, benchmarks were established for kinases such as EGFR, KIT, and RET, along with their respective mutations.


## Description of readout 
- **Readouts**:
    - `EGFR`, `EGFR_L858R`, `EGFR_L861Q`, `EGFR_T790M`, `EGFR_T790M-L858R`
    - `KIT`, `KIT_D816V`, `KIT_T6701`, `KIT_V560G`
    - `RET`, `RET_V804L`, `RET_Y791F`
- **Bioassay readout**: Percentage of inhibition (%).
- **Optimization objective**: Higher potency (higher %inhibition).


## Data resource:
PKIS 1: A set of 364 unique small-molecule ATP-competitive kinase inhibitors that was screened by the set in activity assays with 224 recombinant kinases and 24 G protein-coupled receptors and in cellular assays of cancer cell proliferation and angiogenesis.

**Reference**: https://pubmed.ncbi.nlm.nih.gov/26501955

