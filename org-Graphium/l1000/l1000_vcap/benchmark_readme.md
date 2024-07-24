## Background
The LINCS L1000 is a database of high-throughput transcriptomics that screened more than 30,000 perturbations on a set of 978 landmark genes [4] from multiple cell lines. VCAP and MCF7 are, respectively, prostate cancer and human breast cancer cell lines. In L1000, most of the perturbagens are chemical, meaning that small drug-like molecules are added to the cell lines to observe how the gene expressions change. This allows to generate biological signatures of the molecules, which are known to correlate with drug activity and side effects.

## Assay information
L1000 is a gene-expression profiling assay based on the direct measurement of a reduced representation of the transcriptome and computational inference of the portion of the transcriptome not explicitly measured. The number of landmark transcripts whose abundance is measured directly is approximately one thousand. Eighty additional invariant transcripts are also explicitly measured to enable quality control, scaling and normalization. Measurements of transcript abundance are made with a combination of a coupled ligase detection and polymerase chain reaction, optically-addressed microspheres, and a flow-cytometric detection system. 

For more information, see the [LINCS User Guide](https://docs.google.com/document/d/1q2gciWRhVCAAnlvF2iRLuJ7whrGP6QjpsCMq1yWz7dU/edit#heading=h.usef9o7fuux3).

## Benchmarking
**The goal** of this benchmark is to have the best predictive model for L1000 genomic signature, for each gene. MSE (mean squared error) measures how far the predicted gene signature is from the actual.

## Description of readout:
- Readouts: MSE
- Optimization objective: Lower value