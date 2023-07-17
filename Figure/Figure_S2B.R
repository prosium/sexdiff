library(survival) 
library(survminer)
library(dplyr)

df = read.csv("F.csv", header = T, sep=",")

head(df)
target = df$Group



df$Group <- factor(df$Group, levels=c("WT","Mutation"))
df$AGE <- factor(df$AGE, levels=c("young","old"))
df$AJCC_STAGE <- factor(df$AJCC_STAGE, levels=c("EARLY","LATE","NOSTAGE"))


surv_object_os <- Surv(time=df$OS_follow, event = df$OS)
fit.coxph<-coxph(surv_object_os ~ Group + AGE + AJCC_STAGE, data=df)
ggforest(fit.coxph, data=df, cpositions = c(0.02, 0.22, 0.37))


fit.coxph<-coxph(surv_object_os ~ Group+AGE+AJCC_STAGE, data=df)
summary(fit.coxph)

svg(filename="results.svg", width=9, height=5) # 6 * ea
ggforest(fit.coxph, data=df, cpositions = c(0.02, 0.22, 0.33))
dev.off()



summary(fit.coxph)
