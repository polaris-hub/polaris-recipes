## Background
The LINCS L1000 is a database of high-throughput transcriptomics that screened more than 30,000 perturbations on a set of 978 landmark genes [4] from multiple cell lines. VCAP and MCF7 are, respectively, prostate cancer and human breast cancer cell lines. In L1000, most of the perturbagens are chemical, meaning that small drug-like molecules are added to the cell lines to observe how the gene expressions change. This allows to generate biological signatures of the molecules, which are known to correlate with drug activity and side effects.

To process the data into our two datasets comprising the VCAP and MCF7 cell lines, we used their "level 5" data composed of the cleanup data converted to z-scores, and filtered to keep only chemical perturbagens. However, we were left with multiple data points per molecule since some variables could change (e.g., incubation time) and generate a new measure. Given our objective of generating a single signature per molecule, we decided to take the measurements with the strongest global activity such that the variance over the 978 genes is maximal. Then, since these signatures are generally noisy, we binned them into five classes corresponding to z-scores based on the thresholds.

The cell lines VCAP and MCF7 were selected since they have a higher number of unique molecule perturbagens than other cell lines. They also have a relatively lower data imbalance, with ~92% falling in the "neutral class" when the z-score was between -2 and 2.


## Assay information
L1000 is a gene-expression profiling assay based on the direct measurement of a reduced representation of the transcriptome and computational inference of the portion of the transcriptome not explicitly measured. The number of landmark transcripts whose abundance is measured directly is approximately one thousand. Eighty additional invariant transcripts are also explicitly measured to enable quality control, scaling and normalization. Measurements of transcript abundance are made with a combination of a coupled ligase detection and polymerase chain reaction, optically-addressed microspheres, and a flow-cytometric detection system. 

For more information, see the [LINCS User Guide](https://docs.google.com/document/d/1q2gciWRhVCAAnlvF2iRLuJ7whrGP6QjpsCMq1yWz7dU/edit#heading=h.usef9o7fuux3).

Reference: https://www.cell.com/cell/fulltext/S0092-8674(17)31309-0

## Description of readout:
"Level 5" data composed of the cleaned-up data converted to z-scores, and filtered to keep only chemical perturbagens.

