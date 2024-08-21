# Polaris Recipes

The Polaris datasets and benchmarks recipes.

This repository is a central hub for the storage, organization, and collaboration of notebooks essential for data curation and design benchmarking tasks listed in the [Polaris Hub](https://polarishub.io). The [Auroris](https://github.com/polaris-hub/auroris) package was used to curate the data.

## Datasets 101 - Basic Checks
A little bit of effort spent on dataset curation can go a long way to improving your models performance in real-world settings. Below, we outline some high level checks that you should be applying to any dataset you work with in drug discovery.

**Step 1** - Check that the dataset is representative of applications in real-world drug discovery.
  - Creators of the dataset must be able to explain the data generation process and describe the specific applications of this dataset in drug discovery.
  - Take for example the FreeSolv dataset in MoleculeNet mentioned in [Pat Walter’s blog](https://practicalcheminformatics.blogspot.com/2023/08/we-need-better-benchmarks-for-machine.html). Although the dataset was designed to evaluate molecular dynamics methods, it has turned into a generic property prediction task for the free energy of solvation. However, this quantity used in isolation is not particularly useful.

**Step 2** - Check that the dataset stems from a consistent, original source
  - Creators of the dataset must share references to where the dataset was originally sourced from. If data is aggregated from multiple sources or preprocessed in some way, this process needs to be transparent and the rationale should be well documented. Blindly combining datasets can [introduce significant noise](https://pubs.acs.org/doi/10.1021/acs.jcim.4c00049).
  -  Some examples that violate this rule include datasets like [tdcommons/solubility-aqsoldb](https://polarishub.io/datasets/tdcommons/solubility-aqsoldb) and [tdcommons/bbb-martins](https://polarishub.io/datasets/tdcommons/bbb-martins). In both cases, data has been collected from multiple sources yet there are no references to primary literature.


**Step 3** - Check that the dataset does not contain obvious errors or ambiguous data
  - Creators of the dataset should check for obvious duplicates, invalid data, or ambiguous data. You should also visualize the data distributions to highlight potential outliers.
  - For example, [tdcommons/bbb-martins](https://polarishub.io/datasets/tdcommons/bbb-martins) violates this rule as it contains many duplicate structures. 

## Example notebooks
If you're looking for examples of curated datasets, we recommended checking out the notebooks for the [adme-fang](https://github.com/polaris-hub/polaris-recipes/blob/disclaimer/org-Biogen/fang2023_ADME/01_polaris_adme-fang_data_curation.ipynb) and [pkis2](https://github.com/polaris-hub/polaris-recipes/tree/disclaimer/org-Polaris/drewry2017_pkis2_subset) datasets.
