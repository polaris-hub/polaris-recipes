## Background
The PoseBusters dataset set is a new set of carefully-selected publicly-available crystal complexes from the PDB. It is a diverse set of recent high-quality protein–ligand complexes which contain drug-like molecules. It only contains complexes released since 2021 and therefore does not contain any complexes present in the PDBbind General Set v2020 used to train many of the methods. 


[Buttenschoen et al.](https://pubs.rsc.org/en/content/articlehtml/2024/sc/d3sc04185a) lists the steps used to select the 308 unique proteins and 308 unique ligands in the PoseBusters dataset set. The complexes were downloaded from the PDB as MMTF files and PyMOL was used to remove solvents and all occurrences of the ligand of interest before saving the proteins with the cofactors in PDB files and the ligands in SDF files. 


## Data source
- Orignial: https://zenodo.org/records/8278563
- Polaris: gs://polaris-public/polaris-recipes/org-polaris/posebusters/posebusters_paper_data/posebusters_benchmark_set

## Other links
- Github: https://github.com/maabuu/posebusters/tree/main