#! /usr/bin/env python3

import pandas
import rdflib

# initialization
basedir = "/home/ivo/Gitrepositories/reuseDeVries/"
g = rdflib.Graph()

# addresses
## read adressenconcordans and locatiepunten
observaties      = pandas.read_csv(basedir + "data/volkstellingen/volkstelling1859.csv")
buurtlinks       = pandas.read_csv(basedir + "data/volkstellingen/volkstelling1859_buurtlink.csv")

## merge
observaties = pandas.merge(observaties, buurtlinks, how='left', left_on='rij', right_on='rij')

## create triples
for index, row in observaties.iterrows():
       s = rdflib.URIRef(str(row['obs']))
       p = rdflib.URIRef("http://purl.org/linked-data/sdmx/2009/dimension#refArea")
       o = rdflib.URIRef(str(row['buurt']))
       g.add((s,p,o))

# write CSV
outfile = basedir + "data/volkstellingen/volkstelling1859_plus.csv"
observaties.to_csv(outfile, encoding='utf-8', index=False)

# write RDF turtle
outfile = basedir + "data/volkstellingen/volkstelling1859_buurtlinks.ttl"
s = g.serialize(format='turtle')
f = open(outfile,"wb")
f.write(s)
f.close()
