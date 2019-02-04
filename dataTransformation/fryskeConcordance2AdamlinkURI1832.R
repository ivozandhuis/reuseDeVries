# R-script to link adam-link 1853 'Buurt' uri's to Fryske Akademy concordance table
# author: richard.zijdeman@iisg.nl

# set working directory
setwd("~/git/reuseDeVries/")

# read in adamlink 1853 data
dfAL <- read.csv("data/districts/wijkindeling1853.csv", stringsAsFactors = FALSE, sep = ",")
dfAL <- dfAL[,2:3] # just the uri as key (omitting polygons, if they are ever updated)

# read in Fryske data and fix label consistency
# file cc1909-1876-1853-1832 was ripped from `concordans 1909 - 1876 - 1853 - 1832 compleet 30jan2019.xlsx`
dfFR <- read.csv("data/addresses/cc1909-1876-1853-1832.csv", stringsAsFactors = FALSE, sep = ",")
dfFR$buurt1853 <- toupper(dfFR$buurt1853)
dfFR$buurt1876 <- toupper(dfFR$buurt1876)

# write out the result as a new file to preserve original file
write.csv(dfFR, file = "data/addresses/cc1909-1876-1853-1832-2.csv")

# merge file and rename URI-variable
dfCOM <- merge(dfFR, dfAL, by.x = "buurt1853", by.y = "label", all.x = TRUE)
names(dfCOM)[17] <- "adamBUri1853"
names(dfCOM)
names(dfCOM)[14] <- "sectie1832"

# write out result
write.csv(dfCOM, file = "./data/addresses/adressenconcordans.csv")

# EOF