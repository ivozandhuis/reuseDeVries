# reuseDeVries

This project is reusing De Vries' dataset on social mobility in Amsterdam (https://doi.org/10.17026/dans-xez-eqdv) in order to experiment with reusing data as Linked Data. We hook up the data to other data available on the Web of Data.

## data
Containing data.

## dataQueries
SPARQL-queries on the results.

## dataHarvesting
Scripts and SPARQL-queries for collecting the necessary data.

## dataTransformation
Scripts for dataTransformation. In R en Python3.

# What does this stuf do?
Convert data.

Preconditions:
- mapping of functionnames for occupations in the dataset onto HISCO in file data/hisco/bdv_occupations_hisco.csv
- districts/neighbourhoods by AdamLink in file data/districts/wijkindeling1853.csv
- eXcel-sheet with mappings between various address-systems in Amsterdam by Fryske Akademy in file [not there]
- GIS shape file with points on the Amsterdam map for every location which had one or more addresses in file [not there]

## Result 0: adressenconcordans.ttl
This file contains the LOD representation of the Fryske Akademy HISGIS data

### Steps
In:		[eXcel-sheet not there]
Tool:	[eXcel - save as csv]
Out:	data/addresses/cc-1909-1876-1853-1832.csv

In:		data/addresses/cc-1909-1876-1853-1832.csv,
		data/districts/wijkindeling1832.csv
Tool:	dataTransformation/fryskeConcordance2AdamlinkURI1832.R
Out:	data/addresses/adressenconcordans.csv

In:		data/addresses/adressenconcordans.csv,
		data/addresses/adressenconcordans.csv-metadata.json
Tool:	http://cattle.datalegend.net/
Out:	data/addresses/adressenconcordans.ttl

## Result 1: locatiepunten.ttl
This file contains the geographical location of a "thing" that has an address.

### Steps
In:		[GIS shape-file not there]
Tool:	[QGIS - save as csv with WKT]
Out:	data/addresses/locatiepunten.csv

In:		data/addresses/locatiepunten.csv
		data/addresses/locatiepunten.csv-metadata.json
Tool:	http://cattle.datalegend.net/
Out:	locatiepunten.ttl

## Result 2: p1223a.ttl/p1223b.ttl
These files contain the original De Vries data in LOD format.

### Steps
In: 	data/org/p1223a.por
Tool:	[SPSS - save as csv with labels]
Out:	data/org/p1223a.csv

In:		data/org/p1223a.csv
		data/org/p1223a.csv-metadata.json
Tool:	http://cattle.datalegend.net/
Out:	data/p1123a.ttl

### Steps
In: 	data/org/p1223b.por
Tool:	[SPSS - save as csv with labels]
Out:	data/org/p1223b.csv

In:		data/org/p1223b.csv, 
		data/org/p1223b.csv-metadata.json
Tool:	http://cattle.datalegend.net/
Out:	data/p1123b.ttl

With cow and rapper installed you can do (TEST THIS!):
from /reuseDeVries
> cow_tool convert data/org/p1223a.csv
> rapper data/org/p1223a.csv.nq -i nquads -o turtle > data/p1223a.ttl


## Result 3: p1123a_standardization.ttl/p1123b_standardization.ttl
This file contains URI's for some of the values in the original files, in addition to p1223a.ttl and p1223b.ttl

### Steps
In:		data/org/p1223a.csv, 
		data/hisco/p1223a_occupations_hisco.csv,
		data/districts/wijkindeling1853.csv,
		data/addresses/adressenconcordans.csv
Tool:	dataTransformation/combineData1223a.py
Out:	data/p1223a_standardization.ttl

### Steps
In:		data/org/p1223b.csv, 
		data/hisco/p1223b_occupations_hisco.csv,
		data/districts/wijkindeling1853.csv,
Tool:	dataTransformation/combineData1223b.py
Out:	data/p1223b_standardization.ttl

# Interesting additional data
## Census data on Amsterdam
in data/volkstelling. Mapped on the Amsterdam neighbourhoods with the same Adamlink URI for districts.
