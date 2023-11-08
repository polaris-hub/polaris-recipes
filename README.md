# Polaris Recipes

The Polaris datasets and benchmarks recipes.

This repository is a central hub for the storage, organization, and collaboration of notebooks essential for data curation and design benchmarking tasks listed in the [Polaris Hub](https://polarishub.io). 

<!-- ## Collection groups:
The current Polaris hub hosts three groups of datasets and benchmarks. 
- ![ADME](https://storage.googleapis.com/polaris-public/icons/icons8-whale-96-ADME.png) ADME properties
- ![Molprop](https://storage.googleapis.com/polaris-public/icons/icons8-bear-100-Molprop.png) Molecular properties
- ![Kinase](https://storage.googleapis.com/polaris-public/icons/icons8-fox-60-kinases.png) Human kinases
 -->

## Basic steps of data curation and processing
Most of the datasets in Polaris hub were curated by the steps below:

**Step 1** - Curate the chemistry information
  - Clean the molecules by performing molecule sanitization and fixing, standardization of molecules, and salts/solvents removal.
  - Detect the stereochemistry information in the molecules. Such as undefined stereocenters and information. It's crucial in the case of the activity cliff among the stereoisomers.


**Step 2** - Curate the measured values
  - Identify the compounds which have multiple measures in the dataset. The identification of the repeated molecules is defined by `datamol.hash_mol` including stereochemistry information.
  - Verify the data resource and remove the dubious data points which are significant different or in different classes in case of categorical data. Compute the average of the rest of the duplicated molecules.
  - Detect potential outliers of the dataset. Verify the data resource and remove the dubious data points.
  - Convert the continuous values based on provided threshold values to classification tasks.
  - Detect activity cliff between the stereoisomers. Those isomers and their bioactivity values can be removed/masked from dataset if the downstream molecule representation is not able to differentiate the stereoisomers.


**Step 3** - Visual inspection
  - Assess molecular diversity and distribution in the chemical space. This can guide the decision on which splitting approach to employ. 
  - Visualize the distribution of bioactivity values. It's useful to examine whether it's meaningful to convert to classification task.
  - Check molecules that contain undesired characters.

## Related links
The data curation philosophy and guildelines can be found in [Polaris Hub](https://polarishub.io/pages/documentation)
