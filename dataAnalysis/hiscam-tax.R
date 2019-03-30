rm(list=ls())
setwd("~/git/reuseDeVries/")

elite1854 <- read.csv("dataAnalysis/hiscam-tax-1854.csv")
elite1884 <- read.csv("dataAnalysis/hiscam-tax-1884.csv")

plot(elite1854$hiscam ~ elite1854$tax)
plot(elite1884$hiscam ~ elite1884$tax)

lm1854 <- lm(elite1854$hiscam ~ elite1854$tax)
lm1884 <- lm(elite1884$hiscam ~ elite1884$tax)

summary(lm1854)
summary(lm1884)
