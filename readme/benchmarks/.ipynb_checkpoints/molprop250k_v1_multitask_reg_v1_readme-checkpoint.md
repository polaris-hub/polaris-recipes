**Benchmarking goal:** 

The objective is to comprehend the proficiency of a model in predicting these 'easy' properties, gauging its effectiveness. Ideally, any pre-trained models should, at the very least, demonstrate good performance in those tasks before applying them to the downstream tasks. 

**Molecule data resource**: 
https://pubs.acs.org/doi/10.1021/acs.jcim.2c01253"

**Train/test split**:
The objective is to comprehend the proficiency of a model in predicting these 'easy' properties. In order to select the predictive models which is able to generalize to new chemical space, a scaffold split is used to generate trian/test sets. 

**Distribution of the train/test in the chemical space**
![image](https://storage.googleapis.com/polaris-public/Datasets/MolProp/figures/molprop250k_v1_umap_scaffold_split.svg)

**For more details of this benchmark** -> [notebook](https://github.com/polaris-hub/polaris-recipes/blob/mvp/02_MolProp/02_ZINC22_250K_leadlike_benchmark.ipynb)