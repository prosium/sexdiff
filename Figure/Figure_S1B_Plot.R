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
plot<-ggplot(data=df, aes(x=TumorType, y=Pvalue, fill=TumorType, color=TumorType)) +
  geom_bar(stat="identity")+
  geom_hline(yintercept=2, linetype='dashed', color='gray34', size=1)+
  #geom_vline(xintercept=1, linetype='dashed', color='grey', size=1)+
  scale_fill_manual(values=c(rep("grey",26)))+
  scale_color_manual(values=c(rep("black",26)))+
  theme(panel.background = element_rect(fill = "white", colour = "black"),
        panel.grid.major =element_blank(), panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        legend.position = "none",
        plot.title = element_text(hjust=0.5, face = "bold", size=20),
        axis.text.x = element_text(size=15, angle = 0, face = "bold"),
        axis.text.y = element_text(size=15, angle = 0, face = "bold"),
        axis.title.y = element_text(size=17, face="bold"),
        axis.title.x = element_text(size=17, face="bold"))
############################################################
svg(filename="surv_dataset.svg", width=6, height=3)
grid.arrange(plot, ncol = 1)
dev.off()
