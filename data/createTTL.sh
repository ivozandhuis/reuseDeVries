#!/bin/sh

curl -i -F "csv=@/home/ivo/Gitrepositories/reuseDeVries/data/p1223a_labels_semicolon_short.csv" -F "json=@p1223a_labels_semicolon.csv-metadata.json" http://cattle.datalegend.net/convert -H'Accept: text/turtle' > p1223a_labels_semicolon_short.csv.ttl
