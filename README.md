# sexdiff

**1. Raw data Retrieval**
Raw data are retrieved 25 tumor type data from [cBioPortal](https://www.cbioportal.org/study/summary?id=laml_tcga_pan_can_atlas_2018%2Cacc_tcga_pan_can_atlas_2018%2Cblca_tcga_pan_can_atlas_2018%2Clgg_tcga_pan_can_atlas_2018%2Cchol_tcga_pan_can_atlas_2018%2Ccoadread_tcga_pan_can_atlas_2018%2Cdlbc_tcga_pan_can_atlas_2018%2Cesca_tcga_pan_can_atlas_2018%2Cgbm_tcga_pan_can_atlas_2018%2Chnsc_tcga_pan_can_atlas_2018%2Ckich_tcga_pan_can_atlas_2018%2Ckirc_tcga_pan_can_atlas_2018%2Ckirp_tcga_pan_can_atlas_2018%2Clihc_tcga_pan_can_atlas_2018%2Cluad_tcga_pan_can_atlas_2018%2Clusc_tcga_pan_can_atlas_2018%2Cmeso_tcga_pan_can_atlas_2018%2Cpaad_tcga_pan_can_atlas_2018%2Cpcpg_tcga_pan_can_atlas_2018%2Csarc_tcga_pan_can_atlas_2018%2Cskcm_tcga_pan_can_atlas_2018%2Cstad_tcga_pan_can_atlas_2018%2Cthym_tcga_pan_can_atlas_2018%2Cthca_tcga_pan_can_atlas_2018%2Cuvm_tcga_pan_can_atlas_2018)

**2. Analysis**
   
- 2-1. Figure2A.
   
Clinical data를 이용해서 maf file을 male과 female로 나눈후 maftools의 `mafCompare` function을 default 옵션으로 사용하였습니다. 결과는 Supplementary Table 6에 기록되어있습니다.
   
- 2-2. Figure2B.
   
R의 `survival` package를 활용하여 clinical significance를 가진 유전자를 선별하였습니다. [LINK](https://github.com/prosium/sexdiff/blob/main/Figure/Figure_2B.R)
   
- 2-3. Figure2C.
   
Copy number change를 Oncogene과 Tumor Suppressor Gene으로 나누어 Oncogene의 amplification, tumor suppressor gene의 deletion을 각각 test하였습니다. 결과는 Supplementary Table 7에 기록되어있습니다. [LINK](https://github.com/prosium/sexdiff/blob/main/Figure/Figure_2C.py)

- 2-4. Figure 2D.
   
[dNdScv](https://github.com/im3sanger/dndscv) 를 활용하여 유의미한 (FDR < 0.05) driver mutation을 male과 female 따로 선별하였습니다. 결과는 Supplementary Table 7에 기록되어있습니다. [LINK](https://github.com/im3sanger/dndscv)

- 2-5. Figure 3A.

[Sanchez-Vega et al](https://pubmed.ncbi.nlm.nih.gov/29625050/)의 논문과 같이 우리는 male과 female에서 10개의 oncogenic pathway에 대해 mutation frequency differnece를 나타내었습니다.
