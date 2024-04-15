import numpy as np
import pandas as pd
from typing import List
import umap
import matplotlib.pyplot as plt
import seaborn as sns
import datamol as dm


def visualize_samples(
    data,
    train_inds,
    test_inds,
    n_train_examples=8,
    n_test_examples=8,
    seed=1428,
    n_cols=4,
    mol_size=(200, 200),
):
    """
    Visualize a random subset of samples from a dataframe that has a "mol" column containing an RDKit molecule representation.
    -- Inputs --
        data: dataframe
        train_inds: list of train indices to randomly choose from
        test_inds: list of test indices to randomly choose from
        n_train_examples: int, number of training examples to pick
        n_test_examples: int, number of test examples to pick
        seed: int, random seed to set for reproducibility
        n_cols: int, number of columns in the output figure
        mol_size: tuple, size of the molecule
    -- Outputs --
        A figure with the specified number of randomly-selected molecules from train and test sets.
    """
    rng = np.random.default_rng(seed=seed)  # Initialize a random number generator
    train_subset = rng.choice(
        a=train_inds, size=n_train_examples, replace=False
    )  # Get a random subset of training samples to visualize
    test_subset = rng.choice(
        a=test_inds, size=n_test_examples, replace=False
    )  # Get a random subset of test samples to visualize

    train_mols = data.loc[train_subset][
        "mol"
    ]  # Get the corresponding molecules from the data
    test_mols = data.loc[test_subset][
        "mol"
    ]  # Get the corresponding molecules from the data
    mols_to_viz = np.concatenate(
        [train_mols, test_mols]
    )  # Combine the molecules that we want to visualize into a group to pass to the visualization
    labels = ["train" for i in range(len(train_subset))] + [
        "test" for i in range(len(test_subset))
    ]  # We just want to label whether the molecule came from the train or test set, could make this more informative

    image = dm.viz.to_image(
        mols=mols_to_viz, legends=labels, n_cols=n_cols, mol_size=mol_size
    )  # Visualize!

    return image


def visualize_chemspace(
    data: pd.DataFrame,
    split_names: List[str],
    mol_col: str = "smiles",
    size_col=None,
    seed=1428,
    umap_metric="jaccard",
):
    """
    Visualize the chemical space by doing a dimensionality reduction with UMAP.
    -- Inputs --
        data: a dataframe
        split_names: names of the types of splits, should be found in columns of the "data" dataframe
        mol_col: string column where we will look for a molecule to featurize
        size_col: used for setting the style of the resulting scatterplot
        seed: int, random seed to use for reproducibility
        umap_metric: similarity metric to use for constructing the UMAP representation
    -- Outputs --
        figs, figures for each kind of split specified in split_names
    """
    figs = plt.figure(num=3)
    features = [
        dm.to_fp(mol) for mol in data[mol_col]
    ]  # Convert molecules to fingerprint
    embedding = umap.UMAP(metric=umap_metric, random_state=seed).fit_transform(
        features
    )  # Embed the features with UMAP using a similarity metric
    data["UMAP_0"], data["UMAP_1"] = embedding[:, 0], embedding[:, 1]
    for split_name in split_names:
        plt.figure()
        fig = sns.scatterplot(
            data=data,
            x="UMAP_0",
            y="UMAP_1",
            style=size_col,
            hue=split_name,
            alpha=0.7,
            palette="colorblind",
        )
        fig.set_title(f"UMAP embedding of compounds for {split_name}")
    return figs


def preprocess_molecule(smiles: str):
    """
    Take a smiles string input and preprocess it with datamol
    """
    # Disable RDKit logs
    dm.disable_rdkit_log()

    # Convert to a mol object
    mol = dm.to_mol(smiles, ordered=True)

    # Fix common errors in the molecule
    mol = dm.fix_mol(mol)

    # Sanitize
    mol = dm.sanitize_mol(mol, sanifix=True, charge_neutral=False)

    # Standardize
    mol = dm.standardize_mol(
        mol,
        disconnect_metals=False,
        normalize=True,
        reionize=True,
        uncharge=False,
        stereo=True,
    )

    # Return a standardized smiles representation
    standard_smiles = dm.standardize_smiles(dm.to_smiles(mol))

    return standard_smiles
