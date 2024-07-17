## Background
This dataset comes from the same data source as the OGBG-PCQM4M dataset, famously known for being part of the OGB large-scale challenge [7] and being one of the only graph datasets where pure Transformers have proven successful. The data source is the PubChemQC project [8] that computed DFT properties on the energy-minimized conformation of 3.8M small molecules from PubChem.

Contrarily to the OGB challenge, we aim to provide enough data for pre-training GNNs, so we do not limit ourselves to the HOMO-LUMO gap prediction [7]. Instead, we gather properties directly given by the DFT (e.g., energies) and compute other 3D descriptors from the conformation (e.g., inertia, the plane of best fit). We also gather node-level properties, the Mulliken and Lowdin charges at each atom. Furthermore, about half of the molecules have time-dependent DFT to help inform about the molecule's excited state. Looking forward, we plan on adding edge-level tasks to enable the prediction of bond properties, such as their lengths and the gradient of the charges.


## Assay information


## Description of readout:


## Data resource

