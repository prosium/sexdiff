import os
import pandas as pd
from scipy import stats
import numpy as np
from lifelines import CoxPHFitter
from lifelines.datasets import load_rossi
import matplotlib.pyplot as plt

# No Survival information
# 
all_types = ["ACC","BLCA","BRCA","CHOL","COADREAD","DLBC","ESCA","GBM","HNSC","KICH","KIRC","KIRP","LAML","LGG","LIHC","LUAD","LUSC","MESO","PAAD","PCPG","SARC","SKCM","STAD","THCA","THYM","UVM"]
# all_types = ["LAML"]

def getClinical(tumortype):
	clinicalfile = open("C:/Data/06.On-Working/LAB_05_Gender.Genomics/Data/Results/"+tumortype+"/"+tumortype+"_Clinical.txt")

	pts_enriched = {}
	
	header = clinicalfile.readline().strip().split("\t")
	for line in clinicalfile:
		elms = line.strip().split("\t")

		for i in range(0, len(header)):
			try:
				elms[i]
			except IndexError:
				elms.insert(i, "NA")

		for i in range(0, len(header)):
			if elms[i] == "":
				elms[i] = "NA"

		

		tcgaid = elms[header.index("Tumor_Sample_Barcode")]
		sex = elms[header.index("SEX")]
		OS_STATUS = elms[header.index("OS_STATUS")]
		OS_MONTHS = elms[header.index("OS_MONTHS")]

		if OS_STATUS == "NA" or OS_MONTHS == "NA":
				pass
		else:

			elms_to_write = sex, OS_STATUS, OS_MONTHS
			finalline = "_".join(elms_to_write)
			pts_enriched[tcgaid] = finalline
				
	return pts_enriched

def OneHotGender(gender):
	if gender == "Male":
		return 1

	elif gender == "Female":
		return 0



for tumortype in all_types:
	

	tempfile = open("temp.txt",'w')
	tempfile_header = "OS_status", "OS_followup", "var"
	tempfile.write("\t".join(tempfile_header)+"\n")


	pts_gender_OS = getClinical(tumortype)
	# print(pts_gender_OS)
	for i in list(pts_gender_OS.keys()):
		gender = pts_gender_OS[i].split("_")[0]
		OS_event = pts_gender_OS[i].split("_")[1].split(":")[0]
		OS_time = pts_gender_OS[i].split("_")[2]
		line_to_write = OS_event, OS_time, str(OneHotGender(gender))
		tempfile.write("\t".join(line_to_write)+"\n")
	
	tempfile.close()

	input_surv = pd.read_table("temp.txt", sep="\t")
	# print(input_surv)
	cph = CoxPHFitter()

	# print(input_surv)
	cph.fit(input_surv, "OS_followup", "OS_status")
	pvalue = round(cph.summary['p'].item(),5)
	zvalue = round(cph.summary['z'].item(),5)
	
	print(tumortype, pvalue, zvalue)

	
	# break




	# print(tumortype, genesymbol, enriched)

	# print(pts_enriched)


	# break
