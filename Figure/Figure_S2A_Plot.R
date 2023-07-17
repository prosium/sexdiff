library(ggplot2)
library(reshape2)
library(dplyr)
library(ggrepel)
library(gridExtra)
library(RColorBrewer)
library(pheatmap)
library(reshape2)
library(ggpubr)
rm(list=ls())

df=read.table("Data10.txt", sep="\t", header=T)
head(df)

df$TumorType = factor(df$TumorType, levels=c(
  "BLCA_ANO9_Male","BLCA_ANO9_Female",
  "STAD_ANO9_Male","STAD_ANO9_Female",
  "LGG_ANO9_Male","LGG_ANO9_Female",
  "SARC_LRP1B_Male","SARC_LRP1B_Female",
  "SKCM_LRP1B_Male","SKCM_LRP1B_Female",
  "STAD_LRP1B_Male","STAD_LRP1B_Female",
  "LUAD_EGFR_Male","LUAD_EGFR_Female",
  "STAD_EGFR_Male","STAD_EGFR_Female",
  "LIHC_TP53_Male","LIHC_TP53_Female",
  "ESCA_TP53_Male","ESCA_TP53_Female",
  "BRCA_TP53_Male","BRCA_TP53_Female"))
############################################################
ratio<-ggplot(data=df, aes(x=TumorType, y=Ratio, fill=Mut_or_WT)) +
  geom_bar(stat="identity", color="black")+
  theme(panel.background = element_rect(fill = "white", colour = "black"),
        panel.grid.major =element_blank(), panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        legend.position = "none",
        plot.title = element_text(hjust=0.5, face = "bold", size=20),
        axis.text.x = element_text(size=15, angle = 90, face = "bold"),
        axis.text.y = element_text(size=15, angle = 90, face = "bold"),
        axis.ticks.x = element_blank(),
        axis.title.y = element_text(size=17, face="bold"),
        axis.title.x = element_text(size=17, face="bold"))+
  scale_fill_manual(values=c("#AFABAB","white"))+
  labs(title="Transcriptome",
       x="",
       y="Frequency (%)")+
  scale_y_continuous(expand = c(0,0))
############################################################
svg(filename="ratio.svg", width=10, height=9)
grid.arrange(ratio, ncol = 1)
dev.off()
