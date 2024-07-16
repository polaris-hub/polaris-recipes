import numpy as np
import datamol as dm
from auroris.visualization._chemspace import visualize_chemspace


def load_readme(path: str):
    """Load a readme file from local/remote url."""
    with dm.fs.fsspec.open(path) as f:
        readme = f.read()
    return readme


def visualize_split_chemspace(mols, train_test_dict):
    with dm.without_rdkit_log():
        X = dm.utils.parallelized(
            fn=dm.to_fp, inputs_list=mols, n_jobs=-1, progress=True
        )

    splits = []
    labels = []
    for k, v in train_test_dict.items():
        split = np.tile(np.nan, (len(X),)).astype(str)
        split[v[0]] = "train"
        split[v[1]] = "test"
        splits.append(split)
        labels.append(k)

    figs = visualize_chemspace(
        X=X,
        y=splits,
        labels=labels,
        umap_kwargs={},
        plot_kwargs={
            "hue_order": [
                "nan",
                "train",
                "test",
            ],
            "alpha": 0.9,
            "edgecolor": "none",
            "palette": "Set2",
        },
    )

    return figs
