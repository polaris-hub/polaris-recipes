![CYP](https://pubs.acs.org/cms/10.1021/acs.chemrestox.3c00305/asset/images/medium/tx3c00305_0006.gif)

## Background
Cytochrome P450 (CYP) enzymes are membrane-bound hemeproteins that play a key role in metabolism of drugs and xenobiotics. Most drugs are mainly metabolized by cytochrome P450 (CYP450), which can lead to drug–drug interactions (DDI). Specifically, time-dependent inhibition (TDI) of CYP3A4 isoenzyme has been associated with clinically relevant DDI. To overcome potential DDI issues, high-throughput in vitro assays were established to assess the TDI of CYP3A4 during the discovery and lead optimization phases.

## Assay information
To assess time-dependent inhibition (TDI), inactivation rate constants (kobs values) were determined. For this purpose, test articles (10 μM) were dispensed to 96-well plates, and the preincubation was started by the addition of human liver microsomes supplemented with reduced nicotinamide adenine dinucleotide phosphate (NADPH). After 0, 7, 16, and 32 min, the residual CYP3A activity was determined by the addition of midazolam (including d4-1-hydroxy-midazolam as internal standard) and incubated for six additional minutes before being stopped by the addition of acetonitrile. The supernatants were analyzed for the CYP3A4 selective metabolites 1-hydroxymidazolam and d4-1-hydroxymidazolam using liquid chromatography–mass spectrometry (LC–MS). The time-dependent CYP3A enzyme activity was calculated using the normalized AREA-ratios of 1-hydroxymidazolam to the internal standard and plotted over the preincubation time. The first-order inactivation rate constant kobs was determined by a 1-parameter fit using a range of 80% and a background of 20%. The percentage of reversible inhibition (%inh-rev) was calculated by the AREA-ratio at a preincubation time of 0 min in relation to the AREA-ratio of the control containing dimethyl sulfoxide (DMSO) only. In the case of a strong reversible inhibition (%inh-rev >50%), no kobs values were calculated.

## Description of readout:
- **log_kobs**:  Log-transformed(base 10) inactivation rate($K_{obs}$). 

## Data resource

**Raw data**: 
- Training set: https://pubs.acs.org/doi/suppl/10.1021/acs.chemrestox.3c00305/suppl_file/- tx3c00305_si_002.xlsx 
- Test set: https://pubs.acs.org/doi/suppl/10.1021/acs.chemrestox.3c00305/suppl_file/tx3c00305_si_003.xlsx

**Processed data**: gs://polaris-public/polaris-recipes/org-novartis/CYP/data/raw/train_test.parquet