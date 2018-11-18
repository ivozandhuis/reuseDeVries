#! /usr/bin/env python3

import pandas
import rdflib

# initialization
basedir = "/home/ivo/Gitrepositories/reuseDeVries/"
g = rdflib.Graph()

# read data 1854
deVriesData1854 = pandas.read_csv(basedir + "data/csv/p1223a.csv")

# merge standardizations
## occupations
### merge standard to dataframe
occupations     = pandas.read_csv(basedir + "dataTransformation/bdv_occupations_hisco.csv")
deVriesData1854 = pandas.merge(deVriesData1854, occupations, how='left', left_on='berpmy', right_on='occupationalTitleDeVries')

### create triples
for index, row in deVriesData1854.iterrows():
   s = rdflib.URIRef("https://iisg.amsterdam/resource/bdv/" + str(row['volgnr1y']))
   p = rdflib.URIRef("http://purl.org/linked-data/sdmx/2009/dimension#occupation")
   o = rdflib.URIRef("https://socialhistory.org/nl/hisco/code/hisco/" + str(row['hisco']))
   g.add((s,p,o))

## districts
### merge standard to dataframe
districts       = pandas.read_csv(basedir + "data/districts/wijkindeling1853.csv")
deVriesData1854 = pandas.merge(deVriesData1854, districts, how='left', left_on="buurty", right_on="label")

### create triples
for index, row in deVriesData1854.iterrows():
   s = rdflib.URIRef("https://iisg.amsterdam/resource/bdv/" + str(row['volgnr1y']))
   p = rdflib.URIRef("http://dbpedia.org/ontology/residence")
   o = rdflib.URIRef(str(row['district']))
   g.add((s,p,o))

## addresses
### concatenate buurt and nummer in deVriesData1854 into one new field concat1854
deVriesData1854["concat1854"] = deVriesData1854["buurty"].map(str) + deVriesData1854["huisnry"].map(str)

### read adressenconcordans and locatiepunten
adressenconcordans = pandas.read_csv(basedir + "data/addresses/adressenconcordans_20181114.csv")
adressenconcordans["concat1853"] = adressenconcordans["concat1853"].str.upper()
adressenconcordans["concat1853"] = adressenconcordans["concat1853"].str.replace('I','J')
locatiepunten      = pandas.read_csv(basedir + "data/addresses/locatiepunten_20181114.csv")

### merge
deVriesData1854 = pandas.merge(deVriesData1854, adressenconcordans, how='left', left_on='concat1854', right_on='concat1853')
deVriesData1854 = pandas.merge(deVriesData1854, locatiepunten, how='left', left_on='locatiepunt', right_on='nummer')

### create triples
for index, row in deVriesData1854.iterrows():
   s = rdflib.URIRef("https://iisg.amsterdam/resource/bdv/" + str(row['volgnr1y']))
   p = rdflib.URIRef("http://rdfs.co/juso/address")
   o = rdflib.URIRef("https://temporary.hisgis.nl/address/amsterdam/" + str(row['concat1853']))
   g.add((s,p,o))

# write CSV
outfile = basedir + "data/deVriesData1854_combination.csv"
deVriesData1854.to_csv(outfile, encoding='utf-8')

# write RDF turtle
outfile = basedir + "data/deVriesData1854_standardization.ttl"
s = g.serialize(format='turtle')
f = open(outfile,"wb")
f.write(s)
f.close()
