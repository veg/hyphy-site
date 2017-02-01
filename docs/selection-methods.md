## Choosing a method for selection inference

HyPhy provides a suite of diverse phylogenetic methodologies for testing specific hypotheses about selection in protein-coding sequence alignment. Which method you select will depend on your specific question:

### Are individual sites subject to *pervasive* (across the whole phylogeny) positive or purifying selection?
* [FEL](selection-methods/#FEL) (**F**ixed **E**fects **L**ikelihood) is suitable for small-to-medium sized data sets
* [FUBAR](selection-methods/#fubar) (**F**ast, **U**nconstrained **B**ayesian **A**pp**R**oximation) is suitable for medium-to-large data sets and is expected to have more power than FEL for detecting pervasive selection at sites.

### Are individual sites subject to *episodic* positive or purifying selection?
* [MEME](selection-methods/#MEME) tests for episodic (e.g. at a subset of branches) selection at individual sites. **MEME is the preferred approach for inferring site-specific selection** and does not accept *a priori* branch specifications.
* [aBSREL](selection-methods/#aBSREL) is an improved version of the common "branch-site" class of models. aBSREL allows either for *a priori* specification of branch(es) to test for selection, or can test each lineage for selection in an exploratory fashion. Note that the exploratory approach will sacrifice power.


### Has a gene experienced positive selection at any site on a particular branch or set of branches?
* [BUSTED](selection-methods/#BUSTED) will test for gene-wide selection at pre-specified lineages. This method is particularly useful for relatively small datasets (fewer than 10 taxa) where other methods may not have sufficient power to detect selection. **This method is not suitable for identifying specific sites subject to positive seleciton.**

### Has gene-wide selection pressure been relaxed or intensified along a certain subset of branches?
* [RELAX](selection-methods/#RELAX) tests for a relaxation (e.g. where purifying selection has become less stringent) or an intensification (e.g. where purifying selection has become stronger) of selection pressures along a specified set of "test" branches. **This method is not suitable for the detection of positive selection.**




<!--------------------------------------------------------------------------------------->
## FEL


<!--------------------------------------------------------------------------------------->
## FUBAR


<!--------------------------------------------------------------------------------------->
## MEME


<!--------------------------------------------------------------------------------------->
## aBSREL


<!--------------------------------------------------------------------------------------->
## BUSTED


<!--------------------------------------------------------------------------------------->
## RELAX


