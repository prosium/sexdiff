import os
from scipy import stats
from scipy.stats import chi2_contingency
import pandas as pd


# No Survival information
all_types = ["ACC","BLCA","BRCA","CHOL","COADREAD","DLBC","ESCA","GBM","HNSC","KICH","KIRC","KIRP","LAML","LGG","LIHC","LUAD","LUSC","MESO","PAAD","PCPG","SARC","SKCM","STAD","THCA","THYM","UVM"]
# all_types = ["ACC"]


def getClinical(tumortype):
	clinicalfile = open("../../../Data/Results/"+tumortype+"/"+tumortype+"_Clinical.txt")
	# clinicalfile = open("Data/"+tumortype+"/"+tumortype+"_Clinical.txt")

	male_stage = []
	female_stage = []
	header = clinicalfile.readline().strip().split("\t")
	
	for line in clinicalfile:
		elms = line.strip().split("\t")
		if elms[header.index("SEX")] == "Male":
			ajcc_stage = elms[header.index("AJCC_PATHOLOGIC_TUMOR_STAGE")]
			if ajcc_stage != "":
				male_stage.append(ajcc_stage)

		elif elms[header.index("SEX")] == "Female":
			ajcc_stage = elms[header.index("AJCC_PATHOLOGIC_TUMOR_STAGE")]
			if ajcc_stage != "":
				female_stage.append(ajcc_stage)

	return male_stage, female_stage


resultsfile = open("stage.txt",'w')
results_header = "TumorType", "Gender","TCGAID", "Age"
resultsfile.write("\t".join(results_header)+"\n")

for tumortype in all_types:
	# print("start....", tumortype)
	male_stage, female_stage = getClinical(tumortype)
	
	male_early = male_stage.count("STAGE I") + male_stage.count("STAGE II")
	male_late = male_stage.count("STAGE III") + male_stage.count("STAGE IV")

	female_early = female_stage.count("STAGE I") + female_stage.count("STAGE II")
	female_late = female_stage.count("STAGE III") + female_stage.count("STAGE IV")

	male, female = [male_early, male_late], [female_early, female_late]
	test_df = pd.DataFrame([male, female], columns=["early","late"], index=["Male", "Female"])
	f, p = stats.fisher_exact(test_df)
	
	print(tumortype, p)
