## What is HyPhy?

HyPhy (**Hy**pothesis Testing using **Phy**logenies) is an open-source software package for the analysis of genetic sequences (in particular the inference of natural selection) using techniques in phylogenetics, molecular evolution, and machine learning. It features a rich scripting language for limitless customization of analyses. Additionally, HyPhy features support for parallel computing environments (via message passing interface). HyPhy has over 8000 registered users and has been cited in over 1800 peer-reviewed publications ([Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=5,39&cites=17874163875017617061,8555001991860797787&scipsc=&q=&scisbd=1)). 

You can use HyPhy in two ways:

* Run HyPhy our accompanying webserver [Datamonkey](http://datamonkey.org) (or see the [development version of Datamonkey](http://test.datamonkey.org) for newer methods and a dramatically better user experience).
* Run HyPhy from the command line on your local computer/server. Follow [these instructions](installation.md) for download and installation. 

HyPhy provides its own scripting language - **HBL** or **HyPhy Batch Language**, which can be used to develop custom analyses or modify existing ones, but it is not necessary to learn or even be aware of it in order to use the package. This is because HyPhy ships with a library of **standard analyses** that implement the most popular methods from start to finish. The most popular class of analyses are those that deal with understanding how **natural selection** has shaped the evolution of extant sequences, e.g., pathogens or comparative genomic data over different time scales.

## Choosing a method for selection inference

HyPhy provides a suite of diverse phylogenetic methodologies for testing specific hypotheses about selection in protein-coding and/or amino-acid multiple sequence alignments. Which method you select will depend on your specific question. Below we recommend several methods for different purposes, linked to more in depth descriptions. Tutorials for using these methods are also available [here](tutorials/current-release-tutorial). 

> Note that you may find it useful to perform pre-processing on your dataset, specifically by screening for recombination breakpoints using our [GARD](./methods/selection-methods/#gard) (**G**enetic **A**lgorithm for **R**ecombination **D**etection) method before proceeding to selection analysis.


### Are individual sites subject to *pervasive* (across the whole phylogeny) positive or purifying selection?
* [FEL](./methods/selection-methods/#fel) (**F**ixed **E**fects **L**ikelihood) is suitable for small-to-medium sized data sets.
* [SLAC](./methods/selection-methods/#slac) (**S**ingle-**L**ikelihood **A**ncestor **C**ounting) is an approximate method with accuracy similar to FEL, but suitable for larger datasets. However, SLAC is not suitable for highly-diverged sequences.
* [FUBAR](./methods/selection-methods/#fubar) (**F**ast, **U**nconstrained **B**ayesian **A**pp**R**oximation) is suitable for medium-to-large data sets and is expected to have more power than FEL for detecting pervasive selection at sites. **FUBAR is the preferred approach for inferring pervasive selection.**


### Are individual sites subject to *episodic* (at a subset of branches) positive or purifying selection?
* [MEME](./methods/selection-methods/#meme) (**M**ixed **E**ffects **M**odel of **E**volution) tests for episodic selection at individual sites. Note that MEME does not accept *a priori* branch specifications. **MEME is the preferred approach for detecting positive selection at individual sites.**


### Are individual branches subject to *episodic* (at a subset of sites) positive or purifying selection?

* [aBSREL](./methods/selection-methods/#absrel) (**a**daptive **B**ranch-**S**ite **R**andom **E**ffects **L**ikelihood) is an improved version of the common "branch-site" class of models. aBSREL allows either for *a priori* specification of branch(es) to test for selection, or can test each lineage for selection in an exploratory fashion. Note that the exploratory approach will sacrifice power. **aBSREL is the preferred approach for detecting positive selection at individual branches.**


### Has a gene experienced positive selection at any site on a particular branch or set of branches?
* [BUSTED](./methods/selection-methods/#busted) (**B**ranch-**S**ite **U**nrestricted **S**tatistical **T**est for **E**pisodic **D**iversification) will test for gene-wide selection at pre-specified lineages. This method is particularly useful for relatively small datasets (fewer than 10 taxa) where other methods may not have sufficient power to detect selection. **This method is not suitable for identifying specific sites subject to positive seleciton.**

### Has gene-wide selection pressure been relaxed or intensified along a certain subset of branches?
* [RELAX](./methods/selection-methods/#relax) tests for a relaxation (e.g. where purifying selection has become less stringent) or an intensification (e.g. where purifying selection has become stronger) of selection pressures along a specified set of "test" branches. **This method is not suitable for detecting positive selection.**

<!--
### Are individual sites within a gene subject to *directional* selection, i.e. selection pressure to evolve towards a specific set of amino acids?
* [FADE](./methods/selection-methods/#fade) tests for directional selection at specific sites in *protein* alignments.
-->

