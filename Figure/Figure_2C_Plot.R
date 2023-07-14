library(ggplot2)
library(dplyr)
library(ggrepel)
library(gridExtra)
library(RColorBrewer)
library(ggpubr)
rm(list=ls())

df=read.table("Data28.txt", sep="\t", header=T)
df$UniqueID <- factor(df$UniqueID, levels=rev(c("LUSC_KRAS_M","LUSC_KRAS_F","STAD_4EBP1_M","STAD_4EBP1_F","LUAD_KEAP1_M","LUAD_KEAP1_F","BLCA_CNTN6_M","BLCA_CNTN6_F","KIRC_FZD9_M","KIRC_FZD9_F","KIRP_FZD9_M","KIRP_FZD9_F","LUSC_FZD9_M","LUSC_FZD9_F","KIRC_CDKN2A_M","KIRC_CDKN2A_F","KIRP_CDKN2A_M","KIRP_CDKN2A_F","THCA_CBL_M","THCA_CBL_F","HNSC_CBL_M","HNSC_CBL_F","KIRC_NOTCH1_M","KIRC_NOTCH1_F","KIRP_NOTCH1_M","KIRP_NOTCH1_F","BRCA_NOTCH1_M","BRCA_NOTCH1_F")))
head(df)

############################################################
ratio<-ggplot(data=df, aes(x=UniqueID, y=Ratio, fill=uniqid2)) +
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
  scale_fill_manual(values=rep(c("#ffe4e1","grey90","#6ca6cd","grey90"),15))+
  labs(title="Transcriptome",
       x="",
       y="Frequency (%)")+
  scale_y_continuous(expand = c(0,0))
############################################################
svg(filename="ratio.svg", width=10, height=10)
grid.arrange(ratio, ncol = 1)
dev.off()
