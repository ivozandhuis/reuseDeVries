#!/bin/sh

curl -i -F "csv=@../data/p1223a_labels_semicolon_short.csv" -F "json=@../data/p1223a_labels_semicolon.csv-metadata.json" http://cattle.datalegend.net/convert -H'Accept: text/turtle' > ../data/constructs/p1223a_labels_semicolon_short.csv.ttl
