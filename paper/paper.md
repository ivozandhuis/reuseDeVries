# The Linked Data version of De Vries' elite-dataset on Amsterdam 1850-1895

Ivo Zandhuis & Richard Zijdeman (in alfabetische volgorde :-P)

## Journal
* Research Data Journal (https://brill.com/view/journals/rdj/rdj-overview.xml)
* https://www.tseg.nl/

## Introduction
Ever since the introduction of computers in historical research digital datasets are constructed. The current opinion is that these datasets should be archived and made available for reuse as Open Data. In The Netherlands the NHDA (now incorporated in KNAW-DANS) was the first organization in the humanities to acknowledge this task and stored the first digital datasets in their archiving system []. They are now available in EASY at KNAW-DANS [].

In this article we ask ourselves how these archived datasets could be reused. In our opinion scholars should be able to combine isolated datasets in order to ask new research questions or evaluate results. In the CLARIAH infrastructure Linked Data and its standard dataformat Resource Descripton Framework (RDF) [] is chosen as the basic technology to enable the linking of datasets through overlapping values and properties. It will result in an ecosystem for datasets, its data management and its usage. [Hoekstra etal 2017].

In order to investigate whether old datasets could be reused according to these modern principles, we did an experiment with a dataset, stored in EASY and created by B.M.A. de Vries as part of the research for her PhD-thesis, published in 1986 [De Vries 1986]. We want to know how the dataset can be
* obtained and read,
* transformed into RDF,
* linked to other data, to de-isolate the dataset, and
* published as Linked Open Data.

Finally we will evaluate the process: was it worth the trouble and what did we gain? Formally: what was the Return on Investment?

## The dataset of De Vries
https://doi.org/10.17026/dans-xez-eqdv
De Vries created a dataset with a sample of elite inhabitants of Amsterdam in 1854 and 1884. The fact that they were elite was derived from the fact that they were sampled from the electoral roles.

* the dataset De Vries
 * original research
 * original data; EASY;

## Workflow creating data as Linked data

### The horror that is called .POR
* Save as CSV
* Export including labels
* We need the codebook to know whether data is complete or added by SPSS.

## Workflow adding links to the data
### Linking the original source at Amsterdam City Archives
https://archief.amsterdam/inventarissen/inventaris/30272.nl.html

### Standardizing values to URI's
  * districts by Adamlink, linking censusdata (CEDAR)
  * addresses by HisGIS, linking pictures from SAA
  * professions (HISCO) by IISH, linking status (HISCAM)

### Creating RDF


## Archiving and publishing the new data
* archiving in dataverse (IISH and DANS) / publishing in druid

## Using the new data
  * visualisation
    * on the map
    * tables
  * links for free
    * to CEDAR (via wijken?)
    * to AdamNet CH-objects
    * to other HISCO data - eg HISCLASS
  * new analysis, like ....

## Evaluation

* the workflow
* the reuse
* the concept Linked Data
