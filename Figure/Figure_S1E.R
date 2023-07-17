library(maftools)
library(ggpubr)

rm(list=ls())


tumortype = "UVM"
maffilename = paste("../../Data/Results/",tumortype,"/",tumortype,"_Mutation.txt",sep="")
clinicalfilename = paste("../../Data/Results/",tumortype,"/",tumortype,"_Clinical.txt",sep="")

data_maf = read.maf(
  maf = maffilename,
  clinicalData = clinicalfilename)

data_Male = subsetMaf(maf = data_maf, clinQuery = "SEX %in% 'Male'")
data_Female = subsetMaf(maf = data_maf, clinQuery = "SEX %in% 'Female'")



test_male = titv(maf = data_Male, plot = FALSE, useSyn = TRUE)
test_female = titv(maf = data_Female, plot = FALSE, useSyn = TRUE)

write.table(test_male$raw.counts,"male.txt", sep="\t", col.names = NA)
write.table(test_female$raw.counts,"female.txt", sep="\t", col.names = NA)
