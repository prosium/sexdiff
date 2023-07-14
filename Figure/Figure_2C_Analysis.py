import os
import numpy as np
import pandas as pd
import scipy.stats as stats
from scipy.stats import chi2_contingency
import math



# No Survival information
# 
all_types = ["ACC","BLCA","BRCA","CHOL","COADREAD","DLBC","ESCA","GBM","HNSC","KICH","KIRC","KIRP","LAML","LGG","LIHC","LUAD","LUSC","MESO","PAAD","PCPG","SARC","SKCM","STAD","THCA","THYM","UVM"]
onc_genes = ["CCND1","CCND2","CCND3","CCNE1","CDK2","CDK4","CDK6","E2F1","E2F3","YAP1","WWTR1","TEAD1","TEAD2","TEAD3","TEAD4","HIPK2","AJUBA","LIMD1","WTIP","TAZ","MLXIP","MLXIPL","MYC","MYCL","MYCN","MYCL1","ARRDC1","KDM5A","NRARP","HDAC1","NFE2L2","NRF2","EIF4EBP1","AKT1","AKT2","AKT3","AKT1S1","DEPTOR","MAPKAP1","MLST8","MTOR","PDK1","PIK3CA","PIK3CB","PIK3R2","RHEB","RICTOR","RPTOR","RPS6","RPS6KB1","AKTS1","4EBP1","MDM2","MDM4","RPS6KA3","LEF1","LGR4","LGR5","LRP5","LRP6","PORCN","RSPO1","CTNNB1","DVL1","DVL2","DVL3","FRAT1","FRAT2","FZD1","FZD10","FZD2","FZD3","FZD4","FZD5","FZD6","FZD7","FZD8","FZD9","WNT1","WNT10A","WNT10B","WNT11","WNT16","WNT2","WNT3A","WNT4","WNT5A","WNT5B","WNT6","WNT7A","WNT7B","WNT8A","WNT8B","WNT9A","WNT9B","ABL1","EGFR","ERBB2","ERBB3","ERBB4","PDGFRA","PDGFRB","MET","FGFR1","FGFR2","FGFR3","FGFR4","FLT3","ALK","RET","ROS1","KIT","IGF1R","NTRK1","NTRK2","NTRK3","SOS1","GRB2","PTPN11","KRAS","HRAS","NRAS","RIT1","ARAF","BRAF","RAF1","RAC1","MAP2K1","MAP2K2","MAPK1","JAK2","IRS2"]
ts_genes = ["CDKN1A","CDKN1B","CDKN2A","CDKN2B","CDKN2C","RB1","STK4","STK3","SAV1","LATS1","LATS2","MOB1A","MOB1B","PTPN14","NF2","WWC1","TAOK1","TAOK2","TAOK3","CRB1","CRB2","CRB3","LLGL1","LLGL2","HMCN1","FAT1","FAT2","FAT3","FAT4","DCHS1","DCHS2","CSNK1E","CSNK1D","KIBRA","MST1","MST2","MAX","MGA","MLX","MNT","MXI1","CNTN6","CREBBP","EP300","HES1","HES2","HES3","HES4","HES5","HEY1","HEY2","HEYL","KAT2B","NOTCH1","NOTCH2","NOTCH3","NOTCH4","NOV","PSEN2","SPEN","FBXW7","CUL1","NCOR1","NCOR2","JAG2","MAML3","DNER","HES-1","HES-2","HES-3","HES-4","HES-5","HEY-1","HEY-2","KEAP1","CUL3","INPP4B","NPRL2","NPRL3","PIK3R1","PIK3R3","PPP2R1A","PTEN","STK11","TSC1","TSC2","TP53","ATM","CHEK2","SFRP1","SFRP2","SFRP4","SFRP5","SOST","TCF7L1","TLE1","TLE2","TLE3","TLE4","WIF1","ZNRF3","AMER1","APC","AXIN1","AXIN2","DKK1","DKK2","DKK3","DKK4","GSK3B","RNF43","TCF7","TCF7L2","TGFBR1","TGFBR2","ACVR2A","ACVR1B","SMAD2","SMAD3","SMAD4","NF1","RASA1","CBL","ERRFI1","ERF"]
outputfile = open("oncogene.txt",'w')



def getClinical(tumortype):
	clinicalfile = open("C:/Data/06.On-Working/LAB_05_Gender.Genomics/Data/Results/"+tumortype+"/"+tumortype+"_Clinical.txt")
	# clinicalfile = open("Data/"+tumortype+"/"+tumortype+"_Clinical.txt")

	malebag = []
	femalebag = []
	header = clinicalfile.readline().strip().split("\t")
	for line in clinicalfile:
		elms = line.strip().split("\t")
		if elms[header.index("SEX")] == "Male":
			malebag.append(elms[0])

		elif elms[header.index("SEX")] == "Female":
			femalebag.append(elms[0])


	return malebag, femalebag

for gene in ts_genes:
	targetgene = gene
	print(targetgene, "is processing as tsg")

	for tumortype in all_types:
		# print("start....", tumortype)
		malebag, femalebag = getClinical(tumortype)



		inputfile = open("C:/Data/06.On-Working/LAB_05_Gender.Genomics/Data/Results/"+tumortype+"/"+tumortype+"_CNV.txt")
		
		header = inputfile.readline().strip().split("\t")

		male_idx = [header.index(i) for i in header if i in malebag]
		female_idx = [header.index(i) for i in header if i in femalebag]

		# print(male_idx, female_idx)
		for line in inputfile:
			elms = line.strip().split("\t")

			genename = elms[0]
			values = elms[1:]
			# print(values)
			# print(genename, targetgene)
			if str(targetgene) == str(genename):
				if len(values) == len(header):
					
					male_cnv_values = [elms[i+1] for i in male_idx]
					female_cnv_values = [elms[i+1] for i in female_idx]

					male_amp = male_cnv_values.count("2")+male_cnv_values.count("1")
					male_neu = male_cnv_values.count("0")
					male_del = male_cnv_values.count("-2")+male_cnv_values.count("-1")

					female_amp = female_cnv_values.count("2")+female_cnv_values.count("1")
					female_neu = female_cnv_values.count("0")
					female_del = female_cnv_values.count("-2")+female_cnv_values.count("-1")

					male, female = [male_del, len(malebag)-male_del], [female_del, len(femalebag)-female_del]
					test_df = pd.DataFrame([male, female], columns=["del","All"], index=["Male", "Female"])
					f, p = stats.fisher_exact(test_df)
					line_to_write = tumortype, genename, "tsg", str(male_del), str(female_del), str(len(malebag)), str(len(femalebag)), str(p), str(round(male_del*100/len(malebag),2)), str(round(female_del*100/len(femalebag),2))
					outputfile.write("\t".join(line_to_write)+"\n")
					if p < 0.01:
						print(tumortype, targetgene, str(p), test_df)


					
