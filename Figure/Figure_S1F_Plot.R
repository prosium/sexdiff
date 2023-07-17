library(ggplot2)
library(dplyr)
library(ggrepel)
library(gridExtra)
library(RColorBrewer)
library(ggpubr)
rm(list=ls())


df=read.table("Data.txt", sep="\t", header=T)
head(df)


mycomparison <- list(
  c("ACC_Male","ACC_Female"),
  c("BLCA_Male","BLCA_Female"),
  c("BRCA_Male","BRCA_Female"),
  c("CHOL_Male","CHOL_Female"),
  c("COADREAD_Male","COADREAD_Female"),
  c("DLBC_Male","DLBC_Female"),
  c("ESCA_Male","ESCA_Female"),
  c("GBM_Male","GBM_Female"),
  c("HNSC_Male","HNSC_Female"),
  c("KICH_Male","KICH_Female"),
  c("KIRC_Male","KIRC_Female"),
  c("KIRP_Male","KIRP_Female"),
  c("LAML_Male","LAML_Female"),
  c("LGG_Male","LGG_Female"),
  c("LIHC_Male","LIHC_Female"),
  c("LUAD_Male","LUAD_Female"),
  c("LUSC_Male","LUSC_Female"),
  c("MESO_Male","MESO_Female"),
  c("PAAD_Male","PAAD_Female"),
  c("PCPG_Male","PCPG_Female"),
  c("SARC_Male","SARC_Female"),
  c("SKCM_Male","SKCM_Female"),
  c("STAD_Male","STAD_Female"),
  c("THCA_Male","THCA_Female"),
  c("THYM_Male","THYM_Female"),
  c("UVM_Male","UVM_Female"))


symnum.args <- list(cutpoints = c(0, 0.0001, 0.001, 0.01, 0.05, 1), 
                    symbols = c("", "", "", "", ""))


plot<-ggboxplot(df, x="UniqueID", y="Age",add="jitter",color="UniqueID",
          palette = rep(c("#ffe4e1", "#6ca6cd"),26),
          legend="None", alpha=3)+
  ylim(0,110)+
  stat_compare_means(comparisons = mycomparison, label.y=93,
                     method = "t.test")+
  theme(panel.background = element_rect(fill = "white", colour = "black"),
        panel.grid.major =element_blank(), panel.grid.minor = element_blank(),
        panel.border = element_blank(),
    legend.position = "none",
    plot.title = element_text(hjust=0.5, face = "bold", size=20),
    axis.text.x = element_text(size=15, angle = 90, face = "bold"),
    axis.text.y = element_text(size=15, angle = 90, face = "bold"),
    axis.title.y = element_text(size=17, face="bold"),
    axis.title.x = element_text(size=17, face="bold"))

?stat_compare_means

svg(filename="age.svg", width=15, height=7)
grid.arrange(plot, ncol = 1)
dev.off()
