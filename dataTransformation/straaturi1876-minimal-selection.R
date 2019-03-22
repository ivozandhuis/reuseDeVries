
# directory
setwd("~/git/reuseDeVries/")

# read file
df <- read.csv("./data/addresses/adressen1876-met-straaturi.csv",
               stringsAsFactors = FALSE)
# fix hisgis id (for ATM project)
df$lp <- df$lp+100000

# add year, to indicate match
df$year <- 1876

# retain important vars
df2 <- df[, c("lp", "straaturi", "year")]

write.csv(df2, "./data/addresses/straaturis1876.csv",
          row.names = FALSE)