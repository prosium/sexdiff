import os
from scipy import stats

# No Survival information
# 
all_types = ["ACC","BLCA","BRCA","CHOL","COADREAD","DLBC","ESCA","GBM","HNSC","KICH","KIRC","KIRP","LAML","LGG","LIHC","LUAD","LUSC","MESO","PAAD","PCPG","SARC","SKCM","STAD","THCA","THYM","UVM"]
# all_types = ["ACC"]


def getClinical(tumortype):
	clinicalfile = open("../../../Data/Results/"+tumortype+"/"+tumortype+"_Clinical.txt")
	# clinicalfile = open("Data/"+tumortype+"/"+tumortype+"_Clinical.txt")

	age_male = []
	age_female = []
	header = clinicalfile.readline().strip().split("\t")
	
	for line in clinicalfile:
		elms = line.strip().split("\t")
		if elms[header.index("SEX")] == "Male":
			age_male.append(elms[0]+"_"+elms[4])

		if elms[header.index("SEX")] == "Female":
			age_female.append(elms[0]+"_"+elms[4])

	return age_male, age_female


resultsfile = open("age.txt",'w')
results_header = "TumorType", "Gender","TCGAID", "Age"
resultsfile.write("\t".join(results_header)+"\n")

for tumortype in all_types:
	# print("start....", tumortype)
	age_male, age_female = getClinical(tumortype)
	

	malebag = []
	femalebag = []

	for i in age_male:
		tcgaid = i.split("_")[0]
		gender = "Male"
		age = i.split("_")[1]
		if age != "":
			final = tumortype, gender, tcgaid, age
			# print("\t".join(final)+"\n")
			resultsfile.write("\t".join(final)+"\n")
			malebag.append(int(age))
		
	for i in age_female:
		tcgaid = i.split("_")[0]
		gender = "Female"
		age = i.split("_")[1]
		if age != "":
			final = tumortype, gender, tcgaid, age
			# print("\t".join(final)+"\n")
			resultsfile.write("\t".join(final)+"\n")
			femalebag.append(int(age))

	# print(malebag, femalebag)
	t_stat, p_val = stats.ttest_ind(malebag, femalebag, equal_var=False, alternative='two-sided')
	print(tumortype, p_val)

