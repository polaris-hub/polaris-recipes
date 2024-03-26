import os
from tempfile import NamedTemporaryFile
from typing import Literal

import warnings
warnings.filterwarnings("ignore")

from scipy import stats

import numpy as np
from gcloud import storage
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import umap

from sklearn.manifold import TSNE
import datamol as dm
import medchem
from medchem.catalogs._catalogs import NamedCatalogs

def display_chemspace(
    data: pd.DataFrame,
    mol_col: str,
    split: tuple = None,
    split_name: str = None,
    data_cols: list = None,
    method: Literal["tsne", "umap"] = "tsne",
    nrows:int = 2,
):
    """ Show chemical space of molecule, optionally between traint/test split """
    mols = data[mol_col].apply(dm.to_mol)
    features = np.array([dm.to_fp(mol) for mol in mols])
    if method == "umap":
        embedding = umap.UMAP().fit_transform(features)
    elif method == "tsne":
        embedding = TSNE(n_components=2).fit_transform(features)
    else:
        raise ValueError("Specify the embedding method")
    data[f"{method}_0"], data[f"{method}_1"] = embedding[:, 0], embedding[:, 1]
    if split is not None and split_name is not None:
        data.loc[split[0], split_name] = "train"
        data.loc[split[1], split_name] = "test"
    
    ncols = 1
    nrows = 1 if data_cols is None else nrows
    
    if data_cols is not None:
        if split_name is not None:
            ncols += len(data_cols)
        else:
           ncols = len(data_cols)
        ncols = np.ceil(ncols/nrows).astype(int)
    fig, axes = plt.subplots(ncols=ncols, nrows=nrows, figsize=(ncols * 6, 5*nrows))
    if data_cols is not None:
        axes = axes.flatten()
        for i, col in enumerate(data_cols):
            print()
            sns.scatterplot(
                data=data,
                x=f"{method}_0",
                y=f"{method}_1",
                hue=data[data_cols[i]].values,
                ax=axes[i],
                s=20,
            )
            axes[i].set_title(f"{method} embedding\n{col}")
        ax = axes[-1]
    else:
        ax = axes
    if split_name is not None:
        sns.scatterplot(
            data=data,
            x=f"{method}_0",
            y=f"{method}_1",
            hue=data[split_name].values,
            ax=ax,
            s=20,
        )
        ax.set_title(f"{method} embedding of compounds for {split_name}")
    fig.tight_layout() 
    return fig


def load_readme(path: str):
    """Load a readme file from local/remote url."""
    with dm.fs.fsspec.open(path) as f:
        readme = f.read()
    return readme


def save_figure(fig, remote_path:str, local_path:str=None):
    """Save figure to both remote google could url and/or local path"""
    if not local_path:
        temp = NamedTemporaryFile()
        local_path = temp.name
    fig.savefig(local_path)

    client = storage.Client()
    bucket_name = remote_path.split("/")[2]
    blob_name = "/".join(remote_path.split("/")[3:])
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(local_path)
