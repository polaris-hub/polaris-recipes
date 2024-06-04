## Background
ADME@NCATS is a resource developed by NCATS to host in silico prediction models for various ADME (Absorption, Distribution, Metabolism and Excretion) properties. The resource serves as an important tool for the drug discovery community with potential uses in compound optimization and prioritization. The models were retrospectively validated on a subset of marketed drugs which resulted in very good accuracies.

Data that were used for developing the models are made publicly accessible by depositing them into PubChem database. In some instances, when complete data cannot be made public, a subset of the data are deposited into PubChem. Links to the PubChem assays can be found in the individual model pages. The users are highly encouraged to use these data for development and validation of QSAR models.

## Assay Information
Cytochrome P450 (CYP) enzymes are membrane-bound hemeproteins that play a key role in metabolism of drugs and xenobiotics. Assaying the effect of chemicals on CYP isozymes is useful to minimize the adverse drug reactions and toxicities in drug development process. Chemical compounds were tested for their effect on CYP enzyme activities by using P450-Glo (TM) screening systems (Promega Corporation, Madison, WI). These systems provide a luminescent method containing proluciferin substrates and are converted to luciferin products by CYP isozymes. The luciferin products formed are detected with a luciferin detection reagent, and the amount of light produced is proportional to CYP activity. P450-Glo (TM) CYP2D6 screening system (Catalog. No. V9890) was used to detect the compounds that interfere in CYP2D6 activity. The positive control compound used for CYP2D6 assay is quinidine (Sigma-Aldrich, St. Louis, MO).

## Description of readout:
- **PUBCHEM_ACTIVITY_OUTCOME**: Corresponds to PUBCHEM_ACTIVITY_SCORE. For all inactive compounds, PUBCHEM_ACTIVITY_SCORE is 0. For all active compounds, a score range was given for each curve class type given above. Active antagonist compounds have PUBCHEM_ACTIVITY_SCORE between 40 and 100. Inconclusive compounds had PUBCHEM_ACTIVITY_SCORE between 1 and 39, and were removed in processing. 
- **PUBCHEM_ACTIVITY_SCORE**: Average of 5 experimental replicates. Fit_LogAC50 was used for determining relative score and was scaled to each curve class' score range.

## Data resource

**Raw data**: 
- CYP2D6: https://pubchem.ncbi.nlm.nih.gov/bioassay/1645840
- CYP3A4: https://pubchem.ncbi.nlm.nih.gov/bioassay/1645841
- CYP2C9: https://pubchem.ncbi.nlm.nih.gov/bioassay/1645842