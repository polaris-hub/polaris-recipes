![ADME](https://pubs.acs.org/cms/10.1021/acs.chemrestox.3c00305/asset/images/medium/tx3c00305_0006.gif) 

## Background

Cytochrome P450 (CYP) enzymes are membrane-bound hemeproteins that play a key role in metabolism of drugs and xenobiotics. Most drugs are mainly metabolized by cytochrome P450 (CYP450), which can lead to drug–drug interactions (DDI). Specifically, time-dependent inhibition (TDI) of CYP3A4 isoenzyme has been associated with clinically relevant DDI. To overcome potential DDI issues, high-throughput in vitro assays were established to assess the TDI of CYP3A4 during the discovery and lead optimization phases.

## Benchmarking
**The goal** of this benchmark is to perform a single task, which is to have the best predictive model for CYP3A4 inactivation rate **log_kobs**. 


## Description of readout 
- **Readouts**: `log_kobs`
- **Bioassay readout**: CYP3A4 inactivation rate

## Molecule data resource:
**Reference**: https://pubs.acs.org/doi/10.1021/acs.chemrestox.3c00305

## Train/test split
In this benchmark set, the train/test sets in the above paper are used. 

**Distribution of the train/test in the chemical space**
![image](https://storage.googleapis.com/polaris-public/polaris-recipes/org-novartis/CYP/figures/paper_split_chemspace.png)


## Related links
The full curation and creation process is documented [here](https://github.com/polaris-hub/polaris-recipes/org-Novartis/CYP/01_CYP3A4_data_curation.ipynb).
