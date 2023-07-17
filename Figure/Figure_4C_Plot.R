library(ggplot2)
library(reshape2)
library(dplyr)
library(ggrepel)
library(gridExtra)
library(RColorBrewer)
library(reshape2)
library(ggpubr)
rm(list=ls())
setwd("C:/Data/06.On-Working/LAB_05_Gender.Genomics/Figures/025/Plot/")

df=read.table("COADREAD_Female_COL7A1.txt", sep="\t", header=T)
head(df)


############################################################
my_comparisons <- list( c("Male", "Female"), c("Female","Female_mutation"),
                        c("Male", "Female_mutation"))
df$Gender <- factor(df$Gender, levels=c("Male","Female","Female_mutation"))
position_y = c(1.0, 1.0, 1.1)

############################################################
ggboxplot(df, x="Gender", y="SBS38", add="jitter", color = "black",
                 palette =c("#00AFBB", "#00AFBB", "#B38F00"), add.params = list(color="Gender"))+
  ylim(-0.01,1.2)+stat_compare_means(comparisons = my_comparisons, label.y = position_y, method="t.test")+
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

svg(filename="DMG.svg", width=15, height=5)
grid.arrange(plot1, plot2,
             ncol = 3)
dev.off()
