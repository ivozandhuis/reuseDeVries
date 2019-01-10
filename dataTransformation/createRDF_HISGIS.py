#! /usr/bin/env python3

import pandas
import rdflib

# initialization
basedir = "/home/ivo/Gitrepositories/reuseDeVries/"
g = rdflib.Graph()

# addresses
## read adressenconcordans and locatiepunten
adressen      = pandas.read_csv(basedir + "data/addresses/adressenconcordans_20181114.csv")
locatiepunten = pandas.read_csv(basedir + "data/addresses/locatiepunten_20181114.csv")
straten       = pandas.read_csv(basedir + "data/addresses/adressen1876-met-straaturi.csv")
adressen["concat1853"] = adressen["concat1853"].str.upper()
adressen["concat1853"] = adressen["concat1853"].str.replace('I','J')

## merge
adressen = pandas.merge(adressen, locatiepunten, how='left', left_on='locatiepunt', right_on='nummer')
adressen = pandas.merge(adressen, straten, how='left', left_on='locatiepunt', right_on='lp')

## create triples
for index, row in adressen.iterrows():
   address = str(row['concat1853'])
   if (address != "nan"):

       s = rdflib.URIRef("https://ivotmp.hisgis.nl/address/amsterdam/" + str(row['concat1853']))
       p = rdflib.URIRef("http://www.opengis.net/ont/geosparql#asWKT")
       o = rdflib.Literal(str(row['WKT']))
       g.add((s,p,o))

       s = rdflib.URIRef("https://ivotmp.hisgis.nl/address/amsterdam/" + str(row['concat1853']))
       p = rdflib.URIRef("http://rdf.histograph.io/liesIn")
       o = rdflib.URIRef(str(row['straaturi']))
       g.add((s,p,o))

# write CSV
outfile = basedir + "data/addresses/adressen.csv"
adressen.to_csv(outfile, encoding='utf-8', index=False)

# write RDF turtle
outfile = basedir + "data/addresses/adressen.ttl"
s = g.serialize(format='turtle')
f = open(outfile,"wb")
f.write(s)
f.close()
