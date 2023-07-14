library(dndscv)

rm(list=ls())
df=read.table("maf_male_maftools.maf_dndscv.txt", sep="\t", header=T)
head(df)
dndsout = dndscv(df)
sel_cv = dndsout$sel_cv
print(head(sel_cv), digits = 3)
signif_genes = sel_cv[sel_cv$pglobal_cv<=1, c("gene_name","pglobal_cv","qglobal_cv")]
rownames(signif_genes) = NULL
write.table(signif_genes, file="sig_male.txt", sep="\t", col.names = NA)


rm(list=ls())
df=read.table("maf_female_maftools.maf_dndscv.txt", sep="\t", header=T)
head(df)
dndsout = dndscv(df)
sel_cv = dndsout$sel_cv
head(sel_cv)
print(head(sel_cv), digits = 3)
signif_genes = sel_cv[sel_cv$pglobal_cv<=1, c("gene_name","pglobal_cv","qglobal_cv")]
rownames(signif_genes) = NULL
write.table(signif_genes, file="sig_female.txt", sep="\t", col.names = NA)
