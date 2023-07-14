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

df=read.table("Data.txt", sep="\t", header=T)
head(df)

############################################################
count<-ggplot(data=df, aes(x=TumorType, y=Count, fill=Gender)) +
  geom_bar(stat="identity", color="black")+
  theme(panel.background = element_rect(fill = "white", colour = "black"),
        panel.grid.major =element_blank(), panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        legend.position = "none",
        plot.title = element_text(hjust=0.5, face = "bold", size=20),
        axis.text.x = element_text(size=15, angle = 0, face = "bold"),
        axis.text.y = element_blank(),
        axis.title.y = element_text(size=17, face="bold"),
        axis.title.x = element_text(size=17, face="bold"))+
  scale_fill_manual(values=c("#FFE4E1","#6CA6CD"))+
  labs(title="Transcriptome",
       x="",
       y="Frequency (%)")+
  scale_y_continuous(expand = c(0,0))
############################################################

############################################################
ratio<-ggplot(data=df, aes(x=TumorType, y=Ratio, fill=Gender)) +
  geom_bar(stat="identity", color="black")+
  theme(panel.background = element_rect(fill = "white", colour = "black"),
        panel.grid.major =element_blank(), panel.grid.minor = element_blank(),
        panel.border = element_blank(),
        legend.position = "none",
        plot.title = element_text(hjust=0.5, face = "bold", size=20),
        axis.text.x = element_text(size=15, angle = 0, face = "bold"),
        axis.text.y = element_blank(),
        axis.title.y = element_text(size=17, face="bold"),
        axis.title.x = element_text(size=17, face="bold"))+
  scale_fill_manual(values=c("#FFE4E1","#6CA6CD"))+
  labs(title="Transcriptome",
       x="",
       y="Frequency (%)")+
  scale_y_continuous(expand = c(0,0))
############################################################
svg(filename="Incidence.svg", width=10, height=7)
grid.arrange(count, ratio,
             ncol = 1)
dev.off()
