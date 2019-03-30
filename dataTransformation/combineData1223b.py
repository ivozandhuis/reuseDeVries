#! /usr/bin/env python3

import pandas
import rdflib

# initialization
basedir = "/home/ivo/git/reuseDeVries/"
g = rdflib.Graph()

# read data 1854
deVriesData1884 = pandas.read_csv(basedir + "data/org/p1223b.csv", dtype=object, na_filter=False)

# set refPeriod
for index, row in deVriesData1884.iterrows():
   s = rdflib.URIRef("https://iisg.amsterdam/resource/bdv/" + str(row['volgnr1z']))
   p = rdflib.URIRef("http://purl.org/linked-data/sdmx/2009/dimension#refPeriod")
   o = rdflib.Literal("1884")
   g.add((s,p,o))

# merge standardizations
## occupations
### merge standard to dataframe
occupations     = pandas.read_csv(basedir + "data/hisco/p1223b_occupations_hisco.csv", dtype=object, na_filter=False)
deVriesData1884 = pandas.merge(deVriesData1884, occupations, how='left', left_on='berpmz', right_on='occupationalTitleDeVries')

### create triples
for index, row in deVriesData1884.iterrows():
   hisco = str(row['hisco'])
   if (hisco != "nan"):
      s = rdflib.URIRef("https://iisg.amsterdam/resource/bdv/" + str(row['volgnr1z']))
      p = rdflib.URIRef("http://purl.org/linked-data/sdmx/2009/dimension#occupation")
      o = rdflib.URIRef("https://iisg.amsterdam/hisco/code/hisco/" + str(row['hisco']))
      g.add((s,p,o))

## districts
### merge standard to dataframe
districts       = pandas.read_csv(basedir + "data/districts/wijkindeling1853.csv", dtype=object, na_filter=False)
deVriesData1884 = pandas.merge(deVriesData1884, districts, how='left', left_on="buurtz", right_on="ordering")

### create triples
for index, row in deVriesData1884.iterrows():
   s = rdflib.URIRef("https://iisg.amsterdam/resource/bdv/" + str(row['volgnr1z']))
   p = rdflib.URIRef("http://dbpedia.org/ontology/residence")
   o = rdflib.URIRef(str(row['district']))
   g.add((s,p,o))

# write RDF turtle
outfile = basedir + "data/p1223b_standardization.ttl"
s = g.serialize(format='turtle')
f = open(outfile,"wb")
f.write(s)
f.close()
