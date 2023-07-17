import os
from lifelines import CoxPHFitter
import pandas as pd
from lifelines.statistics import logrank_test

all_types = ["ACC","BLCA","BRCA","CHOL","COADREAD","DLBC","ESCA","GBM","HNSC","KICH","KIRC","KIRP","LAML","LGG","LIHC","LUAD","LUSC","MESO","PAAD","PCPG","SARC","SKCM","STAD","THCA","THYM","UVM"]


inputfile = open("Data.txt")


def getClinical(tumortype, gendertype):
	# clinicalfile = open("C:/Data/06.On-Working/LAB_05_Gender.Genomics/Data/Results/"+tumortype+"/"+tumortype+"_Clinical.txt")
	clinicalfile = open("Data/"+tumortype+"/"+tumortype+"_Clinical.txt")


	gender_OS = {}
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

		tcgaid = tumortype+"_"+elms[header.index("Tumor_Sample_Barcode")]
		gender = elms[header.index("SEX")]
		OS_STATUS = elms[header.index("OS_STATUS")]
		OS_MONTHS = elms[header.index("OS_MONTHS")]

		if OS_STATUS == "NA" or OS_MONTHS == "NA":
				pass
		else:
			if gender.lower() == gendertype:
				elms_to_write = gender,OS_STATUS, OS_MONTHS
				finalline = "_".join(elms_to_write)
				gender_OS[tcgaid] = finalline
				# print(finalline)
				
	return gender_OS


def getMutation(tumortype, genesymbol):
	# mutationfile = open("C:/Data/06.On-Working/LAB_05_Gender.Genomics/Data/Results/"+tumortype+"/"+tumortype+"_Mutation.txt")
	mutationfile = open("Data/"+tumortype+"/"+tumortype+"_Mutation.txt")
	header = mutationfile.readline().strip().split("\t")

	mutation_tcgaid = []
	for line in mutationfile:
		elms = line.strip().split("\t")
		if elms[0] == genesymbol:
			if elms[header.index("Variant_Classification")] != "Silent":
				pts_id = elms[header.index("Tumor_Sample_Barcode")]
				mutation_tcgaid.append(pts_id)


	return list(set(mutation_tcgaid))


def OneHotMutation(OX):
	if OX == True:
		return 1

	elif OX == False:
		return 0

def Selection_DominantGender(OddsRatio):
    if OddsRatio < 1:
        dominant_gender = "female"

    elif OddsRatio > 1:
        dominant_gender = "male"

    return dominant_gender

# def getFinalline(domi_gender_dict, Mutation_pts):


resultfile = open("Result.txt",'w')
resultheader = "TumorType","Gene","DominantGender","pvalue","zvalue"
resultfile.write("\t".join(resultheader)+"\n")


header = inputfile.readline().strip().split("\t")
for line in inputfile:
	tempfile = open("temp.txt",'w')
	tempfile_header = "OS_status", "OS_followup", "var"
	tempfile.write("\t".join(tempfile_header)+"\n")


	elms = line.strip().split("\t")
	tumortype = elms[0]
	mutgene = elms[1]
	oddsratio = float(elms[5])
	pval = float(elms[4])

	dominant_gender = Selection_DominantGender(oddsratio)
	domi_gender_dict = getClinical(tumortype, dominant_gender)

	Mutation_pts = getMutation(tumortype, mutgene)
	# print(Mutation_pts, len(Mutation_pts))
	
	# Mut
	T1 = []
	E1 = []

	# No Mut
	T2 = []
	E2 = []

	for pts in domi_gender_dict.keys():
		# print(domi_gender_dict)
		tumortype1 = pts.split("_")[0]
		ptsid = pts.split("_")[1]
		Mut_or_WT = OneHotMutation(ptsid in Mutation_pts)
		key_clinical = tumortype1+"_"+ptsid
		gender = domi_gender_dict[key_clinical].split("_")[0]
		OS_event = int(domi_gender_dict[key_clinical].split("_")[1].split(":")[0])
		OS_time = float(domi_gender_dict[key_clinical].split("_")[2])
		# finalline = tumortype, ptsid, str(Mut_or_WT), gender, str(OS_event), str(OS_time)
		# print(finalline)
		
		if Mut_or_WT == 1:
			T1.append(OS_time)
			E1.append(OS_event)

		elif Mut_or_WT == 0:
			T2.append(OS_time)
			E2.append(OS_event)

	
	results = logrank_test(T1, T2, event_observed_A = E1, event_observed_B=E2)

	finalline = tumortype, mutgene, dominant_gender, str(results.p_value), str(results.test_statistic)
	print(finalline)
	resultfile.write("\t".join(finalline)+"\n")



	
