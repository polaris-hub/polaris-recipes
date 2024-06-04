![pkis2](https://storage.googleapis.com/polaris-public/icons/icons8-fox-60-kinases.png)

## Backgroud:
 Kinases play a crucial role in cellular signalling, making them important targets for drug development. Dysregulation of kinases is frequently implicated in diseases like cancer, inflammation, and neurodegenerative disorders. Therefore, targeting kinases with specific drugs has emerged as a crucial strategy in modern drug discovery. Kinase-related task includes inhibition prediction, selectivity prediction, or kinase-ligand binding affinity prediction. In the early release version of Polaris, benchmarks were established for kinases such as EGFR, KIT, and RET, along with their respective mutations, as well as for LOK and SLK.


## Description of readout 
- **Readouts**: `EGFR`, `KIT`, `RET`, `LOK`, `SLK`
- **Bioassay readout**: Percentage of inhibition (%).
- **Optimization objective**: Higher potency (higher %inhibition).
- **Number of molecules after curation**: 640

## Data resource:
PKIS2: A second chemogenomics set of kinase inhibitors from GSK, Takeda, and Pfizer was assembled as PKIS2. This set contained 645 inhibitors and included many additional chemotypes that were not represented in the original set.

**Reference**: https://www.ncbi.nlm.nih.gov/pubmed/28767711

## Data curation
To **maintain consistency** with other benchmarks in the Polaris Hub, a thorough data curation process is carried out to ensure the accuracy of molecular presentations.

The full curation and creation process is documented [here](https://github.com/polaris-hub/polaris-recipes/tree/main/org-Polaris/drewry2017_pkis2_subset/01_pkis2_kinase_data_curation.ipynb).
