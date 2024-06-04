**Benchmarking goal:** 

Single tasks for the six endpoints: As the original paper, author established regression tasks for each ADME endpoints with predefined train-test set for the model training. In this benchmark set, the same train/test sets in the fang2023 paper were used for the 6 endpoints human and rat liver microsomal stability, MDR1-MDCK efflux ratio, solubility, and human and rat plasma protein binding, respectively. 

## Benchmarking
*The goal** of this benchmark is to perform a single task, which is to the best predictive model for human liver microsomal stability. 


## Description of readout 
- **Readouts**: `LOG RPPB (mL/min/kg)`
- **Bioassay readout**: Rat plasma protein binding 
- **Optimization objective**: Lower value


## Molecule data resource:
**Reference**: https://doi.org/10.1021/acs.jcim.3c00160

## Train/test split
In this benchmark set, the same train/test sets in the fang2023 paper were used for the 6 endpoints human and rat liver microsomal stability, MDR1-MDCK efflux ratio, solubility, and human and rat plasma protein binding, respectively. 
See more details at https://github.com/molecularinformatics/Computational-ADME/tree/main/MPNN.

**Distribution of the train/test in the chemical space**
![image](https://storage.googleapis.com/polaris-public/datasets/ADME/fang2023/figures/fang2023_ADME_public_v1_hPPB_tsne_fang2023split.png)

## Related links
The full curation and creation process is documented [here](https://github.com/polaris-hub/polaris-recipes/blob/main/01_ADME).
