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

df=read.table("data.txt", sep="\t", header=T)
head(df)

############################################################
dmg<-ggplot(data=df, aes(x=SignedLog2OR, y=log10P, color=TumorType)) +
  geom_point()+
  xlim(-5.5,5.5)+ylim(1.2,7)+
  geom_hline(yintercept=1.3, linetype='dashed', color='grey', size=1)+
  geom_text_repel(aes(label=uniqid))+
  theme(panel.background = element_rect(fill = "white", colour = "black"),
        panel.grid.major =element_blank(), panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        #legend.position = "none",
        plot.title = element_text(hjust=0.5, face = "bold", size=20),
        axis.text.x = element_text(size=15, angle = 0, face = "bold"),
        axis.text.y = element_text(size=15, angle = 0, face = "bold"),
        axis.title.y = element_text(size=17, face="bold"),
        axis.title.x = element_text(size=17, face="bold"))

#labs(title="Transcriptome",
#     x="",
#     y="Frequency (%)")+
############################################################
svg(filename="DMG.svg", width=7, height=6)
grid.arrange(dmg, ncol = 1)
dev.off()
