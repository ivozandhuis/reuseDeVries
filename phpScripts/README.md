# A set of scripts to match Addresses from the Saa beeldbank to HisGis location points 

We were determined to only create *matches of which we are certain*, so all addresses that could be ambiguous (because they existed in multiple periods for instance) were stripped out. 
The `concordans2beeldbank.php` script uses the  data in `adressenconcordans.csv` as delivered by HisGis, as a starting point.

* Uses the concordans to create a list of all Amsterdam addresses that have existed in different times, is created: `adressenconcordans-combined.csv` 
* Removes all ambiguous addresses from that csv, via sorting and removing in a few steps Ithe doubles in a few steps and intermediate files. It creates a final restult in `adressenconcordans-unique.csv`

Uses the data in `saa-beeldbank-adressen.csv` containing all the addresses mentioned in the beeldbank and tries to find matches in the concordance (`adressenconcordans-unique.csv`).
Output of this is two files:
 - `link-locatiepunten-saa-beeldbank.csv` with all the matches that were linked:
 - `geen-link-locatiepunten-saa-beeldbank.csv` with beeldbank identifiers and address that could not be linked
 