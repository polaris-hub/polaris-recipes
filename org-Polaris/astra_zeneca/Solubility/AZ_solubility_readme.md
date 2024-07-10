## Background
This is part of a release of experimental data determined at AstraZeneca on a set of compounds in the following assays: pKa, lipophilicity (LogD7.4), aqueous solubility, plasma protein binding (human, rat, dog , mouse and guinea pig), intrinsic clearance (human liver microsomes, human and rat hepatocytes). 

## Assay Information
Aqueous solubility is one of the most important properties in drug discovery, as it has profound impact on various drug properties, including biological activity, pharmacokinetics (PK), toxicity, and in vivo efficacy. Both kinetic and thermodynamic solubilities are determined during different stages of drug discovery and development. One way of assessing solubility is as follows:

![image-2.png](https://www.emdmillipore.com/images/xl/170931-71[7175-ALL].jpg)

Image is from [here](https://www.emdmillipore.com/CA/en/product/MultiScreenHTS-PCF-Filter-Plates-for-Solubility-Assays,MM_NF-C8875?ReferrerURL=https%3A%2F%2Fwww.google.com%2F).


## Description of readout:
- **SOLUBILITY_74**: Solubility in pH7.4 buffer using solid starting material using the method described in J. Assoc. Lab. Autom. 2011, 16, 276-284, temperature-controlled (20 °C).

## Data resource

**Reference**: https://www.ebi.ac.uk/chembl/document_report_card/CHEMBL3301361/

**Raw data**: https://www.ebi.ac.uk/chembl/assay_report_card/CHEMBL3301364/

## Curation reproducibility
The curation process in this notebook can be reproduced by command line:

```shell
auroris curate org-Polaris/astra_zeneca/solubility/curation_config.json org-Polaris/astra_zeneca/solubility
```