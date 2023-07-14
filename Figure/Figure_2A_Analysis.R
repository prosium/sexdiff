library(maftools)

male = read.maf(maf = "male.maf")
female = read.maf(maf = "female.maf")

sexdiff <- mafCompare(m1 = male, m2 = female, m1Name = 'M', m2Name = 'F', minMut = 3)
print(sexdiff)

