## Background

Cytochrome P450 (CYP) enzymes are membrane-bound hemeproteins that play a key role in metabolism of drugs and xenobiotics. Assaying the effect of chemicals on CYP isozymes is useful to minimize the adverse drug reactions and toxicities in drug development process. CYP2D6, CYP3A4, CYP2C9 are in the significant enzymes responsible for metabolizing commonly used drugs. These CYP enzymes affect the metabolism of a significant portion of drugs in clinical use.

## Assay Information
Chemical compounds were tested for their effect on CYP enzyme activities by using P450-Glo (TM) screening systems (Promega Corporation, Madison, WI). These systems provide a luminescent method containing proluciferin substrates and are converted to luciferin products by CYP isozymes. The luciferin products formed are detected with a luciferin detection reagent, and the amount of light produced is proportional to CYP activity. P450-Glo (TM) CYP screening system (Catalog. No. V9890) was used to detect the compounds that interfere in CYP activity. The positive control compound used for CYP assay is quinidine (Sigma-Aldrich, St. Louis, MO).

## Description of readouts
- CYP2C9_SCORE: Average activity score of 5 replicates for CYP2C9.
- CYP2C9_OUTCOME: Binarized label based on the phenotype observed, active antagonism (class = 1) if CYP2C9_SCORE between 40-100, Inactive (class = 0) if 0. 
- CYP2D6_SCORE: Average activity score of 5 replicates for CYP2D6.
- CYP2D6_OUTCOME: Binarized label based on the phenotype observed, active antagonism (class = 1) if CYP2D6_SCORE between 40-100, Inactive (class = 0) if 0.
- CYP3A4_SCORE: Average activity score of 5 replicates for CYP3A4.
- CYP3A4_OUTCOME: Binarized label based on the phenotype observed, active antagonism (class = 1) if CYP3A4_SCORE between 40-100, Inactive (class = 0) if 0.

## Data resource
Reference: https://opendata.ncats.nih.gov/adme/data

Raw data: 
- CYP2D6: https://pubchem.ncbi.nlm.nih.gov/bioassay/1645840
- CYP3A4: https://pubchem.ncbi.nlm.nih.gov/bioassay/1645841
- CYP2C9: https://pubchem.ncbi.nlm.nih.gov/bioassay/1645842