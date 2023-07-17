library(fmsb)
library(ggplotify)

create_beautiful_radarchart <- function(data, color = "#00AFBB", 
                                        vlabels = colnames(data), vlcex = 0.7,
                                        caxislabels = NULL, title = NULL, ...){
  radarchart(
    data, axistype = 1,
    # Customize the polygon
    pcol = color, pfcol = scales::alpha(color, 0.5), plwd = 2, plty = 1,
    # Customize the grid
    cglcol = "#808080", cglty = 1, cglwd = 0.8,
    # Customize the axis
    axislabcol = "grey", 
    # Variable labels
    vlcex = vlcex, vlabels = vlabels,
    caxislabels = caxislabels, title = title, ...
  )
}

df=read.table("test.txt", sep="\t", header=T, row.names = 1)
head(df)
# Create the radar charts

svg(filename="blank_plot.svg", width=5, height=5)
create_beautiful_radarchart(
  data = df, caxislabels = c("", "", "", "", ""),
  color = c("#FF5238","#517C9A", "#CCB6B4"), title="zz")



alltumortypes = c("ACC","BLCA","BRCA","CHOL","COADREAD","DLBC","ESCA","GBM","HNSC","KICH","KIRC","KIRP","LAML","LGG","LIHC","LUAD","LUSC","MESO","PAAD","PCPG","SARC","SKCM","STAD","THCA","THYM","UVM")


svg(filename="All_plot.svg", width=30, height=30)
par(mar = c(0, 0, 0, 0))
par(mfrow = c(4, 7))
for (tumortype in alltumortypes){
  
  outputfigure = paste(tumortype,"fig",sep="")
  filename = paste(tumortype,".txt",sep="")
  df=read.table(filename, sep="\t", header=T, row.names = 1)
  #svg(filename=paste(tumortype,"_plot.svg",sep=""), width=6, height=6)
  create_beautiful_radarchart(
    data = df, caxislabels = c("", "", "", "", ""),
    color = c("#FF5238","#517C9A", "#CCB6B4"), vlabels=NA)
  
  #dev.off()

}
dev.off()  
