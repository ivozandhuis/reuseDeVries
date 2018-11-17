setwd("/home/ivo/Gitrepositories/reuseDeVries/")

# read data 1854
deVriesData1854 <- read.csv("data/csv/p1223a.csv")

# merge standardizations
## occupations
occupations <- read.csv("dataTransformation/bdv_occupations_hisco.csv")
deVriesData1854 <- merge(deVriesData1854, occupations, by.x = "berpmy",  by.y = "occupationalTitleDeVries",  all.x = TRUE)

## districts
districts <- read.csv("data/districts/wijkindeling1853.csv")
deVriesData1854 <- merge(deVriesData1854, districts, by.x = "buurty",  by.y = "label",  all.x = TRUE)

## addresses
adressenconcordans <- read.csv("data/addresses/adressenconcordans_20181114.csv")
locatiepunten      <- read.csv("data/addresses/locatiepunten_20181114.csv")

### concatenate buurt and nummer in deVriesData1854
deVriesData1854$concat1854 <- paste(deVriesData1854$buurty, deVriesData1854$huisnry, sep = "")

### merge
deVriesData1854 <- merge(deVriesData1854, adressenconcordans, by.x = "concat1854",  by.y = "concat1853",  all.x = TRUE)
deVriesData1854 <- merge(deVriesData1854, locatiepunten, by.x = "locatiepunt",  by.y = "nummer",  all.x = TRUE)

# write CSV
write.table(deVriesData1854, "data/deVriesData1854.csv", sep = ",", row.names = FALSE)

# create triples
# ???
