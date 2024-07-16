
![molprop](https://storage.googleapis.com/polaris-public/icons/icons8-bear-100-Molprop.png)

## Background

Molecular representations are crucial for understanding molecular structure, predicting properties, QSAR studies, toxicology and chemical modeling and other aspects in drug discovery tasks. Therefore, benchmarks for molecular representations are critical tools that drive progress in the field of computational chemistry and drug design. In recent years, many large models have been trained for learning molecular representation. The aim is to evaluate large pretrained models are capable of predicting various “easy-to-compute” molecular properties. 

## Description of readout
The computed properties are molecular weight, fraction of sp3 carbon atoms (fsp3), number of rotatable bonds, topological polar surface area, computed logP, formal charge, number of charged atoms, refractivity and number of aromatic rings. These properties are widely used in molecule design and molecule prioritization.

**Number of molecules after curation**: 249455

## Data resource
ZINC is a widely utilized public access database and tool set, playing a crucial role in various applications including virtual screening, ligand discovery, pharmacophore screens, benchmarking, and force field development. The **MolProp250K** dataset consists of 250,000 compounds randomly selected from ZINC15.

**Reference**: https://pubs.acs.org/doi/10.1021/acs.jcim.5b00559 

**Raw data**: https://raw.githubusercontent.com/aspuru-guzik-group/chemical_vae/master/models/zinc_properties/250k_randm_zinc_drugs_clean_3.csv \


## Data curation
To **maintain consistency** with other benchmarks in the Polaris Hub, a thorough data curation process is carried out to ensure the accuracy of molecular presentations.

The full curation and creation process is documented [here](https://github.com/polaris-hub/polaris-recipes/blob/main/02_MolProp).

## Related benchmarks
- [molprop250kleadlike_reg_v1](https://polarishub.io/benchmarks/polaris/molprop250k-multitask-reg-v1)
- [molprop250kleadlike_multitask_reg_v1](https://polarishub.io/benchmarks/polaris/molprop250kleadlike-multitask-reg-v1)
> Note: It's recommanded to evaluate your methods agaisnt all the benchmarks related to this dataset. 
