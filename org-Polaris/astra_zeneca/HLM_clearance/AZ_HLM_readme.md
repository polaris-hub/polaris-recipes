## Background
This is part of a release of experimental data determined at AstraZeneca on a set of compounds in the following assays: pKa, lipophilicity (LogD7.4), aqueous solubility, plasma protein binding (human, rat, dog , mouse and guinea pig), intrinsic clearance (human liver microsomes, human and rat hepatocytes). 

## Assay Information
Hepatic metabolic stability is a key pharmacokinetic parameter in drug discovery. Metabolic stability is usually assessed in microsomal fractions and only the best compounds progress in the drug discovery process.

![image.png](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs00216-016-9929-6/MediaObjects/216_2016_9929_Fig1_HTML.gif)

Image is from [this paper](https://link.springer.com/article/10.1007/s00216-016-9929-6). Biologically active compounds can be transformed or destroyed by the action of enzymes in the liver. Microsomes are small membrane bubbles (vesicles) that come from a fragmented cell membrane, and can be used as a proxy for how well a drug survives a trip through the liver.

## Description of readout:
- **HLM_CLEARANCE**: Intrinsic clearance measured in human liver microsomes following incubation at 37C. Experimental range <3 to >150 microL/min/mg. Rapid Commun. Mass Spectrom. 2010, 24, 1730-1736.

## Data resource

**Reference**: https://www.ebi.ac.uk/chembl/document_report_card/CHEMBL3301361/

**Raw data**: https://www.ebi.ac.uk/chembl/assay_report_card/CHEMBL3301370/

## Curation reproducibility
The curation process in this notebook can be reproduced by command line:

```shell
auroris curate org-Polaris/astra_zeneca/AZ_HLM/curation_config.json org-Polaris/astra_zeneca/AZ_HLM
```