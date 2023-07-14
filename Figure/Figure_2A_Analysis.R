library(maftools)
library(ggpubr)
setwd("C:/Data/06.On-Working/LAB_05_Gender.Genomics/Figures/016/")


rm(list=ls())

#GBM	HNSC	KICH	KIRC	KIRP	LAML	LGG	LIHC	LUAD	LUSC	MESO	PAAD	PCPG	SARC	SKCM	STAD	THCA	THYM	UVM

tumortype = "GBM"
maffilename = paste("../../Data/Results/",tumortype,"/",tumortype,"_Mutation.txt",sep="")
clinicalfilename = paste("../../Data/Results/",tumortype,"/",tumortype,"_Clinical.txt",sep="")

data_maf = read.maf(
  maf = maffilename,
  clinicalData = clinicalfilename)

data_Male = subsetMaf(maf = data_maf, clinQuery = "SEX %in% 'Male'")
data_Female = subsetMaf(maf = data_maf, clinQuery = "SEX %in% 'Female'")


write.mafSummary(maf = data_Male, basename = 'maf_male')
write.mafSummary(maf = data_Female, basename = 'maf_female')

sexdiff <- mafCompare(m1 = data_Male, m2 = data_Female, m1Name = 'M', m2Name = 'F', minMut = 3)
print(sexdiff)

