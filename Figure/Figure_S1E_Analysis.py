import os

tumortype = "UVM"
female = open("female.txt")
male = open("male.txt")

male.readline()
for line in male:
	elms = line.strip().split("\t")


	ti = int(elms[4])+int(elms[5])
	tv = int(elms[2])+int(elms[3])+int(elms[6])+int(elms[7])

	print(tumortype, "Male", elms[1].replace("\"",""), ti, tv)



female.readline()
for line in female:
	elms = line.strip().split("\t")


	ti = int(elms[4])+int(elms[5])
	tv = int(elms[2])+int(elms[3])+int(elms[6])+int(elms[7])

	print(tumortype, "Female", elms[1].replace("\"",""), ti, tv)
