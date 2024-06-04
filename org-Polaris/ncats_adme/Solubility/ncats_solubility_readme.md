## Background
ADME@NCATS is a resource developed by NCATS to host in silico prediction models for various ADME (Absorption, Distribution, Metabolism and Excretion) properties. The resource serves as an important tool for the drug discovery community with potential uses in compound optimization and prioritization. The models were retrospectively validated on a subset of marketed drugs which resulted in very good accuracies.

Data that were used for developing the models are made publicly accessible by depositing them into PubChem database. In some instances, when complete data cannot be made public, a subset of the data are deposited into PubChem. Links to the PubChem assays can be found in the individual model pages. The users are highly encouraged to use these data for development and validation of QSAR models.

## Assay Information
Aqueous solubility is one of the most important properties in drug discovery, as it has profound impact on various drug properties, including biological activity, pharmacokinetics (PK), toxicity, and in vivo efficacy. Both kinetic and thermodynamic solubilities are determined during different stages of drug discovery and development. One way of assessing solubility is as follows:

![image.png](https://storage.googleapis.com/polaris-public/readme/datasets/img/04_02_ADME_NCATS_Solubility_data_curation.jpeg)

Image is from [here](https://www.emdmillipore.com/CA/en/product/MultiScreenHTS-PCF-Filter-Plates-for-Solubility-Assays,MM_NF-C8875?ReferrerURL=https%3A%2F%2Fwww.google.com%2F).


## Description of readout:
- **PUBCHEM_ACTIVITY_OUTCOME**: Corresponds to the phenotype observed. For all compounds with Moderate/High phenotype, PUBCHEM_ACTIVITY_OUTCOME is "active" (class = 1). For all        compounds with Low phenotype, PUBCHEM_ACTIVITY_OUTCOME is "inactive" (class = 0).
- **PUBCHEM_ACTIVITY_SCORE**: Whole number in Solubility (ug/mL) of the compound.
- **PHENOTYPE**: Indicates type of activity observed: 0-10: Low Solubility (class = 0) >10: Moderate/High Solubility (class = 1)
- **KINETIC_AQUEOUS_SOLUBILITY**: Numerical value of the observed aqueous solubility, measured in ug/mL.

## Data resource

**Reference**: https://pubmed.ncbi.nlm.nih.gov/31176566/ 

**Raw data**: https://pubchem.ncbi.nlm.nih.gov/bioassay/1645848