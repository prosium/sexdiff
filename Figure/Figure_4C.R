rm(list = setdiff(ls(), lsf.str()))
ref_genome <- "BSgenome.Hsapiens.UCSC.hg19"
library(ref_genome, character.only = TRUE)
library(MutationalPatterns)

setwd("D:/LAB/LAB_05_Gender.Genomics/Figures/024/CosineSimilarity")
inputfilename = "Female.txt"
signaturefilename = "REF_Sig_COSMICv3.txt"

mutation_matrix = read.table(inputfilename, header = TRUE, sep ="\t")
rownames(mutation_matrix) <- mutation_matrix[,1]
mutation_matrix <- mutation_matrix[,-1]
test<-mutation_matrix+0.0000000001
#######################################################
cancer_signatures = read.table(signaturefilename, sep = "\t", header = TRUE)

new_order = match(row.names(mutation_matrix), cancer_signatures$MutationType)
cancer_signatures = cancer_signatures[as.vector(new_order),]

head(cancer_signatures)
row.names(cancer_signatures) = cancer_signatures$Somatic.Mutation.Type
cancer_signatures = as.matrix(cancer_signatures[,4:ncol(cancer_signatures)]) ###### all COSMIC Signatures
mutation_matrix[,1:ncol(mutation_matrix)] = apply(mutation_matrix[,1:ncol(mutation_matrix)], 2, function(x) as.numeric(as.character(x)))
cancer_signatures[,1:ncol(cancer_signatures)] = apply(cancer_signatures[,1:ncol(cancer_signatures)], 2, function(x) as.numeric(as.character(x)))

cos_sim_samples_signatures = cos_sim_matrix(mutation_matrix, cancer_signatures)


write.table(cos_sim_samples_signatures, "Female_COSMIC.txt", sep="\t", col.names=NA)
