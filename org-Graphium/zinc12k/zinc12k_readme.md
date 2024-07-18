## Background
ZINC is a free database of commercially-available compounds for virtual screening. ZINC contains over 230 million purchasable compounds in ready-to-dock, 3D formats. ZINC also contains over 750 million purchasable compounds that can be searched for analogs. ZINC12K contains a 12,000 sample subset of ZINC molecular graphs.

## Assay information
ZINC was loaded from 134 commercial supplier catalogs and 36 annotated catalogs (Table 1). If a salt, the largest organic component is taken, and molecules containing an atom other than H, C, N, O, F, S, P, Si, Cl, Br, or I are removed, a limitation due to the use of the Merck Forcefield MMFF94. Only molecules passing the primary filtering rules are loaded. Filtering rules are implemented in OpenEye’s OEChem (19) and are listed in text and graphical form (20) at filtering.docking.org. Molecules are prepared and physical properties calculated according to the protocol detailed in the [ZINC paper](https://pubs.acs.org/doi/10.1021/ci3001277).

## Description of readout:
- SA: Synthetic accessibility score.
- LogP: Log P, octanol-water partition coefficient.
- Score: constrained solubility which is the term logP − SA − cycle (octanol-water partition coefficients, logP, penalized by the synthetic accessibility score, SA, and number of long cycles, cycle).

## Data resource
References: 
- [ZINC: A Free Tool to Discover Chemistry for Biology](https://pubs.acs.org/doi/10.1021/ci3001277)
- [Benchmarking Graph Neural Networks](https://arxiv.org/pdf/2003.00982)
