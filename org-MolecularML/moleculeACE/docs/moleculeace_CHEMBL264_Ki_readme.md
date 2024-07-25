## Background
This dataset comprises collected and curated bioactivity data for the target Histamine receptor from ChEMBL assay CHEMBL264, utilized to evaluate the performance of various machine learning algorithms on activity cliffs. We employed classical machine learning methods combined with common molecular descriptors, as well as neural networks based on unstructured molecular data such as molecular graphs or SMILES strings.

Activity cliffs are molecules with small differences in structure but large differences in potency. Activity cliffs play an important role in drug discovery, but the bioactivity of activity cliff compounds are notoriously difficult to predict.

## Description of readouts
- `exp_mean [nM]`: Inhibition [Inhibitory Constant, Ki]
- `y`: Negative of log transform of the bioactivity value.
- `split`: Train-test split based on activity cliff.

## Data resource:
- [Exposing the Limitations of Molecular Machine Learning with Activity Cliffs
](https://pubs.acs.org/doi/10.1021/acs.jcim.2c01073)
- Github: https://github.com/molML/MoleculeACE