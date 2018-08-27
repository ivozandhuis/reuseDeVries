setwd("/home/ivo/Gitrepositories/reuseDeVries/")

adressenConcordans <- read.csv("data/adressenconcordans_20180611.csv")
puntlocaties <- read.csv("data/puntlocaties_20180611.csv")
deVriesData1854 <- read.csv("data/p1223a_labels.csv")

adressenConcordans$adres1853 <- paste(adressenConcordans$X1853_buurt, adressenConcordans$X1853_buurtnr, adressenConcordans$X1853_tvg, sep = "")
deVriesData1854$adres1854 <- paste(deVriesData1854$buurty, deVriesData1854$huisnry, sep = "")

df <- merge(adressenConcordans, deVriesData1854, by.x = "adres1853", by.y = "adres1854", all.y = TRUE)
df <- merge(df, puntlocaties, by.x = "locatiepunt", by.y = "nummer", all.x = TRUE)

# write
write.table(df, "data/constructs/df.csv", sep = ",", row.names = FALSE)
