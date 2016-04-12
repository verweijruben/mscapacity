## Analyse 50/10 KV Houten
library("ggplot2", lib.loc="\\\\enc-cap-vdm-01/766141$/Documents/R/R-3.1.3/library")
library("plyr", lib.loc="\\\\enc-cap-vdm-01/766141$/Documents/R/R-3.1.3/library")
library("reshape2", lib.loc="\\\\enc-cap-vdm-01/766141$/Documents/R/R-3.1.3/library")

setwd("S:/Stedin/Techniek/AM/Afdelingen/RM-PM/1.1.10 Werkmappen/Ruben Verweij/Collegas/Osisoft_MS_capaciteit/resultaten")
resultaten = read.csv("results.txt", sep="", stringsAsFactors = FALSE)




qplot(resultaten$Voltage_pu, binwidth=0.005) + xlim(1,0.85)
