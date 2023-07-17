import os

"""
<inputfile>
	TumorType	Gene	tcgaid	Gender
	ACC	CLDN17	TCGA-OR-A5KB	Female
	ACC	WWP2	TCGA-OR-A5KP	Female
	ACC	GIMAP8	TCGA-OR-A5KB	Female
	ACC	FATE1	TCGA-OR-A5K5	Female
	ACC	SGIP1	TCGA-OR-A5LJ	Female
	ACC	RBM27	TCGA-PK-A5HB	Male
"""
pathway1_cellcycle = ["CCND1","CCND2","CCND3","CCNE1","CDK2","CDK4","CDK6","E2F1","E2F3","CDKN1A","CDKN1B","CDKN2A","CDKN2B","CDKN2C","RB1"]
pathway2_Hippo = ["YAP1","WWTR1","TEAD1","TEAD2","TEAD3","TEAD4","HIPK2","AJUBA","LIMD1","WTIP","STK4","STK3","SAV1","LATS1","LATS2","MOB1A","MOB1B","PTPN14","NF2","WWC1","TAOK1","TAOK2","TAOK3","CRB1","CRB2","CRB3","LLGL1","LLGL2","HMCN1","FAT1","FAT2","FAT3","FAT4","DCHS1","DCHS2","CSNK1E","CSNK1D","SCRIB"]
pathway3_MYC = ["MLXIP","MLXIPL","MYC","MYCL","MYCN","MAX","MGA","MLX","MNT","MXI1","MXD1","MXD3","MXD4"]
pathway4_NOTCH = ["ARRDC1","KDM5A","NRARP","HDAC1","CNTN6","CREBBP","EP300","HES1","HES2","HES3","HES4","HES5","HEY1","HEY2","HEYL","KAT2B","NOTCH1","NOTCH2","NOTCH3","NOTCH4","NOV","PSEN2","SPEN","FBXW7","CUL1","NCOR1","NCOR2","JAG2","MAML3","DNER","LFNG","ITCH","NCSTN","JAG1","APH1A","FHL1","THBS2","HDAC2","MFAP2","RFNG","MFAP5","NUMB","MFNG","CIR1","CNTN1","MAML1","MAML2","NUMBL","PSEN1","PSENEN","RBPJ","RBPJL","RBX1","SAP30","SKP1","SNW1","CTBP1","CTBP2","ADAM10","APH1B","ADAM17","DLK1","DLL1","DLL3","DLL4","DTX1","DTX2","DTX3","DTX3L","DTX4","EGFL7"]
pathway5_NRF2 = ["NFE2L2","KEAP1","CUL3"]
pathway6_PI3K = ["EIF4EBP1","AKT1","AKT2","AKT3","AKT1S1","DEPTOR","MAPKAP1","MLST8","MTOR","PDK1","PIK3CA","PIK3CB","PIK3R2","RHEB","RICTOR","RPTOR","RPS6","RPS6KB1","INPP4B","NPRL2","NPRL3","PIK3R1","PIK3R3","PPP2R1A","PTEN","STK11","TSC1","TSC2","DEPDC5"]
pathway7_RTKRAS = ["CBLB","CBLC","INSR","INSRR","IRS1","SOS2","SHC1","SHC2","SHC3","SHC4","RASGRP1","RASGRP2","RASGRP3","RASGRP4","RAPGEF1","RAPGEF2","RASGRF1","RASGRF2","FNTA","FNTB","RCE1","ICMT","MRAS","PLXNB1","MAPK3","ARHGAP35","RASA2","RASA3","RASAL1","RASAL2","RASAL3","SPRED1","SPRED2","SPRED3","DAB2IP","SHOC2","PPP1CA","SCRIB","PIN1","KSR1","KSR2","PEBP1","PEA15","ABL1","EGFR","ERBB2","ERBB3","ERBB4","PDGFRA","PDGFRB","MET","FGFR1","FGFR2","FGFR3","FGFR4","FLT3","ALK","RET","ROS1","KIT","IGF1R","NTRK1","NTRK2","NTRK3","SOS1","GRB2","PTPN11","KRAS","HRAS","NRAS","RIT1","ARAF","BRAF","RAF1","RAC1","MAP2K1","MAP2K2","MAPK1","JAK2","IRS2","NF1","RASA1","CBL","ERRFI1","ERF"]
pathway8_TGFbeta = ["TGFBR1","TGFBR2","ACVR2A","ACVR1B","SMAD2","SMAD3","SMAD4"]
pathway9_TP53 = ["MDM2","MDM4","RPS6KA3","TP53","ATM","CHEK2"]
pathway10_WNT = ["CHD8","LZTR1","NDP","LEF1","LGR4","LGR5","LRP5","LRP6","PORCN","RSPO1","CTNNB1","DVL1","DVL2","DVL3","FRAT1","FRAT2","FZD1","FZD10","FZD2","FZD3","FZD4","FZD5","FZD6","FZD7","FZD8","FZD9","WNT1","WNT10A","WNT10B","WNT11","WNT16","WNT2","WNT3A","WNT4","WNT5A","WNT5B","WNT6","WNT7A","WNT7B","WNT8A","WNT8B","WNT9A","WNT9B","SFRP1","SFRP2","SFRP4","SFRP5","SOST","TCF7L1","TLE1","TLE2","TLE3","TLE4","WIF1","ZNRF3","AMER1","APC","AXIN1","AXIN2","DKK1","DKK2","DKK3","DKK4","GSK3B","RNF43","TCF7","TCF7L2","CHD4"]


all_types = ["ACC","BLCA","BRCA","CHOL","COADREAD","DLBC","ESCA","GBM","HNSC","KICH","KIRC","KIRP","LAML","LGG","LIHC","LUAD","LUSC","MESO","PAAD","PCPG","SARC","SKCM","STAD","THCA","THYM","UVM"]
# all_types = ["ACC"]
gender = ["Male","Female"]




def DivideGender(tumortype):
	malebag = []
	femalebag = []

	for line in inputfile:
		elms = line.strip().split("\t")
		if elms[0] == tumortype:
			if elms[3] == "Male":
				malebag.append(elms[1])

			elif elms[3] == "Female":
				femalebag.append(elms[1])
	list(set(malebag))
	list(set(femalebag))
	inputfile.seek(0)
	return malebag, femalebag


def pathwaycount(pathwayno):
	pathway1_cellcycle = ["CCND1","CCND2","CCND3","CCNE1","CDK2","CDK4","CDK6","E2F1","E2F3","CDKN1A","CDKN1B","CDKN2A","CDKN2B","CDKN2C","RB1"]
	pathway2_Hippo = ["YAP1","WWTR1","TEAD1","TEAD2","TEAD3","TEAD4","HIPK2","AJUBA","LIMD1","WTIP","STK4","STK3","SAV1","LATS1","LATS2","MOB1A","MOB1B","PTPN14","NF2","WWC1","TAOK1","TAOK2","TAOK3","CRB1","CRB2","CRB3","LLGL1","LLGL2","HMCN1","FAT1","FAT2","FAT3","FAT4","DCHS1","DCHS2","CSNK1E","CSNK1D","SCRIB"]
	pathway3_MYC = ["MLXIP","MLXIPL","MYC","MYCL","MYCN","MAX","MGA","MLX","MNT","MXI1","MXD1","MXD3","MXD4"]
	pathway4_NOTCH = ["ARRDC1","KDM5A","NRARP","HDAC1","CNTN6","CREBBP","EP300","HES1","HES2","HES3","HES4","HES5","HEY1","HEY2","HEYL","KAT2B","NOTCH1","NOTCH2","NOTCH3","NOTCH4","NOV","PSEN2","SPEN","FBXW7","CUL1","NCOR1","NCOR2","JAG2","MAML3","DNER","LFNG","ITCH","NCSTN","JAG1","APH1A","FHL1","THBS2","HDAC2","MFAP2","RFNG","MFAP5","NUMB","MFNG","CIR1","CNTN1","MAML1","MAML2","NUMBL","PSEN1","PSENEN","RBPJ","RBPJL","RBX1","SAP30","SKP1","SNW1","CTBP1","CTBP2","ADAM10","APH1B","ADAM17","DLK1","DLL1","DLL3","DLL4","DTX1","DTX2","DTX3","DTX3L","DTX4","EGFL7"]
	pathway5_NRF2 = ["NFE2L2","KEAP1","CUL3"]
	pathway6_PI3K = ["EIF4EBP1","AKT1","AKT2","AKT3","AKT1S1","DEPTOR","MAPKAP1","MLST8","MTOR","PDK1","PIK3CA","PIK3CB","PIK3R2","RHEB","RICTOR","RPTOR","RPS6","RPS6KB1","INPP4B","NPRL2","NPRL3","PIK3R1","PIK3R3","PPP2R1A","PTEN","STK11","TSC1","TSC2","DEPDC5"]
	pathway7_RTKRAS = ["CBLB","CBLC","INSR","INSRR","IRS1","SOS2","SHC1","SHC2","SHC3","SHC4","RASGRP1","RASGRP2","RASGRP3","RASGRP4","RAPGEF1","RAPGEF2","RASGRF1","RASGRF2","FNTA","FNTB","RCE1","ICMT","MRAS","PLXNB1","MAPK3","ARHGAP35","RASA2","RASA3","RASAL1","RASAL2","RASAL3","SPRED1","SPRED2","SPRED3","DAB2IP","SHOC2","PPP1CA","SCRIB","PIN1","KSR1","KSR2","PEBP1","PEA15","ABL1","EGFR","ERBB2","ERBB3","ERBB4","PDGFRA","PDGFRB","MET","FGFR1","FGFR2","FGFR3","FGFR4","FLT3","ALK","RET","ROS1","KIT","IGF1R","NTRK1","NTRK2","NTRK3","SOS1","GRB2","PTPN11","KRAS","HRAS","NRAS","RIT1","ARAF","BRAF","RAF1","RAC1","MAP2K1","MAP2K2","MAPK1","JAK2","IRS2","NF1","RASA1","CBL","ERRFI1","ERF"]
	pathway8_TGFbeta = ["TGFBR1","TGFBR2","ACVR2A","ACVR1B","SMAD2","SMAD3","SMAD4"]
	pathway9_TP53 = ["MDM2","MDM4","RPS6KA3","TP53","ATM","CHEK2"]
	pathway10_WNT = ["CHD8","LZTR1","NDP","LEF1","LGR4","LGR5","LRP5","LRP6","PORCN","RSPO1","CTNNB1","DVL1","DVL2","DVL3","FRAT1","FRAT2","FZD1","FZD10","FZD2","FZD3","FZD4","FZD5","FZD6","FZD7","FZD8","FZD9","WNT1","WNT10A","WNT10B","WNT11","WNT16","WNT2","WNT3A","WNT4","WNT5A","WNT5B","WNT6","WNT7A","WNT7B","WNT8A","WNT8B","WNT9A","WNT9B","SFRP1","SFRP2","SFRP4","SFRP5","SOST","TCF7L1","TLE1","TLE2","TLE3","TLE4","WIF1","ZNRF3","AMER1","APC","AXIN1","AXIN2","DKK1","DKK2","DKK3","DKK4","GSK3B","RNF43","TCF7","TCF7L2","CHD4"]

	if pathwayno == 1: pathwayname = "Cell_Cycle"; pathway = pathway1_cellcycle
	if pathwayno == 2: pathwayname = "Hippo";pathway = pathway2_Hippo
	if pathwayno == 3: pathwayname = "MYC";pathway = pathway3_MYC
	if pathwayno == 4: pathwayname = "Notch";pathway = pathway4_NOTCH
	if pathwayno == 5: pathwayname = "NRF2";pathway = pathway5_NRF2
	if pathwayno == 6: pathwayname = "PI3K";pathway = pathway6_PI3K
	if pathwayno == 7: pathwayname = "RTKRAS";pathway = pathway7_RTKRAS
	if pathwayno == 8: pathwayname = "TGF-beta";pathway = pathway8_TGFbeta
	if pathwayno == 9: pathwayname = "TP53";pathway = pathway9_TP53
	if pathwayno == 10: pathwayname = "WNT";pathway = pathway10_WNT

	maleno = 0
	femaleno = 0
	
	for gene in pathway:
		if gene in malebag:
			maleno += 1

		if gene in femalebag:
			femaleno += 1

	return pathwayname, maleno, femaleno

inputfile = open("results.txt")
outputfile = open("trim.txt",'w')
for tumortype in all_types:
	print(tumortype, "....start")
	malebag, femalebag = DivideGender(tumortype)
	

	for i in range(1, 10+1):
		pathway, maleno, femaleno = pathwaycount(i)
		final = tumortype, pathway, str(maleno), str(femaleno)
		outputfile.write("\t".join(final)+"\n")
