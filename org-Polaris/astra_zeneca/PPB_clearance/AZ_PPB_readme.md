## Background
This is part of a release of experimental data determined at AstraZeneca on a set of compounds in the following assays: pKa, lipophilicity (LogD7.4), aqueous solubility, plasma protein binding (human, rat, dog , mouse and guinea pig), intrinsic clearance (human liver microsomes, human and rat hepatocytes). 

## Assay Information:
During a trip through the circulatory system, a drug can bind to many different proteins within the blood plasma. This can affect a drug's efficacy - only the unbound fraction of the drug will exert pharmacological effects. Equilibrium dialysis places a semi-permeable barrier between a drug + plasma sample and a buffer, and after a certain time we measure how much drug is present in the buffer. The membrane lets the drug pass through but drugs bound to proteins are too big to pass across the membrane. Image is from [here](https://www.sciencedirect.com/science/article/abs/pii/S0079646822000029).

![image.png](attachment:image.png)

## Description of readout:
- **PPB**: Percent plasma-bound. % bound to plasma by equilibrium dialysis. Compound is incubated with whole human plasma at 37C for >5hrs. Method described in B. Testa et al (Eds.), Pharmacokinetic Profiling in Drug Research: Biological, Physicochemical, and Computational Strategies, Wiley-VCH, Weinheim, 2006, pp.119-141. Experimental range 10% to 99.95% bound. Typically, the log transformation on %unbound to plasma proteins is used for machine learning. 
Interpretation of %unbound PPB in value ranges:
- good : >1
- medium: 0- 1
- bad: <0

## Data resource

**Reference**: https://www.ebi.ac.uk/chembl/document_report_card/CHEMBL3301361/

**Raw data**: https://www.ebi.ac.uk/chembl/assay_report_card/CHEMBL3301365/

## Curation reproducibility
The curation process in this notebook can be reproduced by command line:

```shell
auroris curate org-Polaris/astra_zeneca/PPB_clearance/curation_config.json org-Polaris/astra_zeneca/PPB_clearance
```