#! /usr/bin/env python3

import pandas

# initialization
basedir = "/home/ivo/git/reuseDeVries/"

# read hisgis data
adressenconcordans = pandas.read_csv(basedir + "data/addresses/adressenconcordans.csv", dtype=object, na_filter=False)

# create list of addresses from adressenconcordans
adressenlijst1876 = adressenconcordans.drop(columns=["buurt1853","hisgisID","straat1909","nr1909","tvg1909","buurt1876","steeg1876","nr1853","tvg1853","sectie1832","perceel1832","tvg1832","adamBUri1853"])
adressenlijst1876.columns = ['lp', 'straat', 'nr', 'tvg']

adressenlijst1909 = adressenconcordans.drop(columns=["buurt1853","hisgisID","buurt1876","straat1876","steeg1876","nr1876","tvg1876","nr1853","tvg1853","sectie1832","perceel1832","tvg1832","adamBUri1853"])
adressenlijst1909.columns = ['lp', 'straat', 'nr', 'tvg']

adressenlijst = adressenlijst1876.copy()
adressenlijst = adressenlijst.append(adressenlijst1909)

# remove empty rows
adressenlijst = adressenlijst[adressenlijst.straat != ""]
adressenlijst = adressenlijst[adressenlijst.straat != " "]

# unique
adressenlijst = adressenlijst.drop_duplicates()

# write CSV
outfile = basedir + "data/addresses/adressenlijst.csv"
adressenlijst.to_csv(outfile, encoding='utf-8', index=False)

