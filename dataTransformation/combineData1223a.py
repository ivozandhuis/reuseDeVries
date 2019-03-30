#! /usr/bin/env python3

import pandas
import rdflib

# initialization
basedir = "/home/ivo/git/reuseDeVries/"
g = rdflib.Graph()

# read data 1854
deVriesData1854 = pandas.read_csv(basedir + "data/org/p1223a.csv", dtype=object, na_filter=False)

# set refPeriod
for index, row in deVriesData1854.iterrows():
   s = rdflib.URIRef("https://iisg.amsterdam/resource/bdv/" + str(row['volgnr1y']))
   p = rdflib.URIRef("http://purl.org/linked-data/sdmx/2009/dimension#refPeriod")
   o = rdflib.Literal("1854")
   g.add((s,p,o))

# merge standardizations
## occupations
### merge standard to dataframe
occupations     = pandas.read_csv(basedir + "data/hisco/p1223a_occupations_hisco.csv", dtype=object, na_filter=False)
deVriesData1854 = pandas.merge(deVriesData1854, occupations, how='left', left_on='berpmy', right_on='occupationalTitleDeVries')

### create triples
for index, row in deVriesData1854.iterrows():
   s = rdflib.URIRef("https://iisg.amsterdam/resource/bdv/" + str(row['volgnr1y']))
   p = rdflib.URIRef("http://purl.org/linked-data/sdmx/2009/dimension#occupation")
   o = rdflib.URIRef("https://iisg.amsterdam/hisco/code/hisco/" + str(row['hisco']))
   g.add((s,p,o))

## districts
### merge standard to dataframe
districts       = pandas.read_csv(basedir + "data/districts/wijkindeling1853.csv", dtype=object, na_filter=False)
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

### read adressenconcordans
### concatenate buurt and nummer in adressenconcordance into one new field concat1853
adressenconcordans = pandas.read_csv(basedir + "data/addresses/adressenconcordans.csv", dtype=object, na_filter=False)
adressenconcordans["concat1853"] = adressenconcordans["buurt1853"].map(str) + adressenconcordans["nr1853"].map(str)
adressenconcordans["concat1853"] = adressenconcordans["concat1853"].str.upper()
adressenconcordans["concat1853"] = adressenconcordans["concat1853"].str.replace('I','J')


### merge
deVriesData1854 = pandas.merge(deVriesData1854, adressenconcordans, how='left', left_on='concat1854', right_on='concat1853')

### create triples
for index, row in deVriesData1854.iterrows():
   lp = str(row['lp'])
   if (lp != "nan"):
       s = rdflib.URIRef("https://iisg.amsterdam/resource/bdv/" + str(row['volgnr1y']))
       p = rdflib.URIRef("http://rdfs.co/juso/address")
       o = rdflib.URIRef("https://hisgis.nl/resource/atm/lp-" + str(row['lp']))
       g.add((s,p,o))

# write RDF turtle
outfile = basedir + "data/p1223a_standardization.ttl"
s = g.serialize(format='turtle')
f = open(outfile,"wb")
f.write(s)
f.close()
