## Background
This dataset is very similar to the [OGBG-PCBA](https://arxiv.org/abs/2005.00687) dataset, but instead of being limited to 128 assays and 437k molecules, it comprises 1,328 assays and 1.56M molecules. This dataset is very interesting for pre-training molecular models since it contains information about a molecule's behavior in various settings relevant to biochemists, with evidence that it improves binding predictions. Analogous to the gene expression, we obtain a bio-assay-expression of each molecule.

To gather the data, we have looped over the PubChem index of bioassays [6] in 2022 and collected every dataset such that it contains more than 6,000 molecules annotated with either "Active" or "Inactive" flags reported by the author, and at least 10 of each. All other flags are removed. Then, we converted all the molecular IDs to canonical SMILES and used it to merge all of the bioassays into a single dataset.

## Data resource
Reference: [PubChem index of bioassays](https://pubmed.ncbi.nlm.nih.gov/26400175/)

