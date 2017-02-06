## Choosing a method for selection inference

HyPhy provides a suite of diverse phylogenetic methodologies for testing specific hypotheses about selection in protein-coding multiple sequence alignments. Which method you select will depend on your specific question:

### Are individual sites subject to *pervasive* (across the whole phylogeny) positive or purifying selection?
* [FEL](selection-methods/#FEL) (**F**ixed **E**fects **L**ikelihood) is suitable for small-to-medium sized data sets
* [FUBAR](selection-methods/#fubar) (**F**ast, **U**nconstrained **B**ayesian **A**pp**R**oximation) is suitable for medium-to-large data sets and is expected to have more power than FEL for detecting pervasive selection at sites.

### Are individual sites subject to *episodic* positive or purifying selection?
* [MEME](selection-methods/#MEME) (**M**ixed **E**ffects **M**odel of **E**volution) tests for episodic (e.g. at a subset of branches) selection at individual sites. **MEME is the preferred approach for inferring site-specific selection** and does not accept *a priori* branch specifications.
* [aBSREL](selection-methods/#aBSREL) (**a**daptive **B**ranch-**S**ite **R**andom **E**ffects **L**ikelihood) is an improved version of the common "branch-site" class of models. aBSREL allows either for *a priori* specification of branch(es) to test for selection, or can test each lineage for selection in an exploratory fashion. Note that the exploratory approach will sacrifice power.


### Has a gene experienced positive selection at any site on a particular branch or set of branches?
* [BUSTED](selection-methods/#BUSTED) (**B**ranch-**S**ite **U**nrestricted **S**tatistical **T**est for **E**pisodic **D**iversification) will test for gene-wide selection at pre-specified lineages. This method is particularly useful for relatively small datasets (fewer than 10 taxa) where other methods may not have sufficient power to detect selection. **This method is not suitable for identifying specific sites subject to positive seleciton.**

### Has gene-wide selection pressure been relaxed or intensified along a certain subset of branches?
* [RELAX](selection-methods/#RELAX) tests for a relaxation (reduction in stringency) or an intensification (increase in stringency) of selection pressures along a specified set of "test" branches. **This method is not suitable for the detection of positive selection.**

<!--------------------------------------------------------------------------------------->
## MG94xREV Framework
All methods rely, to some extent, on the MG94xREV codon model, a generalized extension of the [MG94 model](https://www.ncbi.nlm.nih.gov/labs/articles/7968485/) (MG94xREV) that allows for a full GTR mutation rate matrix:

[rate matrix goes here with explanation of parameters, graphically]

As part of likelihood calculations, MG94xREV requires a specified set of "codon frequencies," which globally reflect codon frequencies which would be present in the *absence* of selection. HyPhy employs the [CF3x4](http://dx.doi.org/10.1371/journal.pone.0011230), a corrected version of the common F3x4 estimator (introduced in [Goldman and Yang 1994](https://www.ncbi.nlm.nih.gov/pubmed/7968486)) which accounts for biases in nucleotide composition induced by stop codons. 


All methods (with the partial exception of RELAX*) will perform a global MG94xREV fit to optimize branch length and nucleotide substitution parameters before proceeding to hypothesis testing. Several of these methods (FEL, FUBAR, and MEME) additionally pre-fit a GTR nucleotide model to the data, using the estimated parameters as starting values for the global MG94xREV fit, as a computational speed-up. Resulting branch length and nucleotide substitution parameters are subsequently used during model fitting for hypothesis testing.


*The global MG94xREV fit is only performed for the descriptive and/or exploratory versions of RELAX (see [below](selection-methods/#RELAX) for details).


<!--------------------------------------------------------------------------------------->
## Synonymous Rate Variation

A key component of HyPhy analyses is the inclusion of *synonymous rate variation*, meaning that dS is often allowed to vary across sites and/or branches, depending on the specific method. As such, hypothesis testing for positive selection is typically conducted by assessing whether dN is significantly greater than dS. [See this paper](https://doi.org/10.1093/molbev/msi232) for a detailed description of why incorporating synonymous rate variation into positive selection inference is likely beneficial. Importantly, this consideration of synonymous rate variation stands in contrast to methods implemented in, for example, [PAML](https://doi.org/10.1093/molbev/msm088) where dS is constrained to equal 1, and postitive selection is inferred based on whether dN () is greater than 1. 

<!--------------------------------------------------------------------------------------->
## FEL


FEL uses a maximum-likelihood (ML) approach to infer nonsynoymous (dN) and synonymous (dS) substitution rates on a per-site basis for a given coding alignment and corresponding phylogeny. This method assumes that the selection pressure for each site is constant along the entire phylogeny. 

After optimizing branch lengths and nucleotide substitution parameters, FEL fits a MG94xREV model to each codon site to infer site-specific nonsynonymous and synonymous (dN and dS, respectively) substitution rates. Hypothesis testing is then conducted on a site-specific basis, using the Likelihood Ratio Test, to ascertain if dN is significantly greater than dS.


**If you use FEL in your analysis, please cite the following:** [`Kosakovsky Pond, SL and Frost, SDW. "Not So Different After All: A Comparison of Methods for Detecting Amino Acid Sites Under Selection." Mol. Biol. Evol. 22, 1208--1222 (2005).`](https://doi.org/10.1093/molbev/msi105)


<!--------------------------------------------------------------------------------------->
## FUBAR

FUBAR uses a Bayesian approach to infer nonsynoymous (dN) and synonymous (dS) substitution rates on a per-site basis for a given coding alignment and corresponding phylogeny. This method assumes that the selection pressure for each site is constant along the entire phylogeny.

Although FUBAR produces similar information to FEL, it has several key differences:

* FUBAR employs a Bayesian algorithm to infer rates, and therefore it reports evidence for positive selection using *posterior probabilities* (which range from 0-1), not p-values. Generally, posterior probabilities > 0.9 are strongly suggestive of positive selection. 
* FUBAR runs extremely quickly and is well-suited for analyzing large alignments, with hundreds or thousands of sequences. This speed-up results from the novel strategy of employing a pre-specified discrete grid of dN and dS values to be applied across sites. This approach contrasts with the time-consuming FEL strategy of fitting a new MG94xREV model at each site.
* FUBAR may have more power than FEL, in particular when positive selection is present but relatively weak (i.e. low values of ω>1).

**If you use FUBAR in your analysis, please cite the following:** [`Murrell, B et al. "FUBAR: A Fast, Unconstrained Bayesian AppRoximation for inferring selection." Mol. Biol. Evol. 30, 1196–1205 (2013).`](https://doi.org/10.1093/molbev/mst030)

<!--------------------------------------------------------------------------------------->
## MEME

MEME employs a mixed-effects maximum likelihood approach to test the hypothesis that individual sites have been subject to episodic positive or diversifying selection. 
In other words, MEME aims to detect sites evolving under positive selection under a *proportion* of branches.

The "mixed-effects" aspect of MEME refers to its modeling strategy of allowing ω rates to vary across sites, while also allowing these ω rates to vary across branches. More specifically, MEME infers two ω rate categories (ω<sub>1</sub> and ω<sub>2</sub>), and corresponding weights, for each site, shared across all branches at that site. These two ω categories share a site-specific synonymous rate dS, but differ in their nonsynonymous rates. 
For both the null and alternative models, one rate category ω<sub>1</sub> follows the constraint ω<sub>1</sub>≤dS. The second rate category ω<sub>2</sub> is used for positive selection inference: In the null model, ω<sub>2</sub> is similarly constrained as ω<sub>2</sub>≤dS. By contrast, the alternative model places no constraints on ω<sub>2</sub>, thus representing a category of positive selection. Positive selection is inferred using the Likelihood Ratio Test between alternative and null models. 
 

**If you use MEME in your analysis, please cite the following:** [`Murrell, B et al. "Detecting individual sites subject to episodic diversifying selection." PLoS Genetics 8, e1002764 (2012).`](http://dx.doi.org/10.1371/journal.pgen.1002764)

<!--------------------------------------------------------------------------------------->
## aBSREL

aBSREL ("adaptive Branch-Site Random Effects Likelihood) is an "adaptive" version of the commonly-used "branch-site" models, which are used to test if positive selection has occurred on a proportion of branches. As such, aBSREL models both site-level and branch-level ω heterogeneity. aBSREL, however, does not test for selection at specific sites. Instead, aBSREL will test, for each branch (or branch of interest) in the phylogeny, whether a proportion of sites have evolved under positive selection. 

aBSREL differs from other branch-site implementations by inferring the optimal number of ω categories for each branch. For example, the earlier HyPhy branch-site approach (BS-REL) assumed three ω rate categories for each branch and assigned each site, with some probability, to one of these categories. aBSREL, by contrast, acknowledges that different branches may feature more or less complex evolutionary patterns and hence may be better modeled by more or fewer ω categories. aBSREL specifically uses AIC<sub>c</sub> (small sample AIC) to infer the optimal number of rate categories for each branch. 

After aBSREL fits the full adaptive model, hypothesis testing is performed for each branch by comparing, using the Likelihood Ratio Test, the full model to a null model where branches are not allowed to have categories of ω>1. 

Most importantly, aBSREL can be run in two modes:

* Test a specific hypothesis by *a priori* selecting a set of "foreground" branches to test for positive selection. 
* Perform an exploratory analysis where all branches are tested for positive selection. In this scenario, p-values at each branch must be corrected for multiple testing (using the Holh-Bonferroni correction). Due to multiple testing, the exploratory approach *has much lower power* compared to the other approach. 


**If you use aBSREL in your analysis, please cite the following:** [`Smith, MD et al. "Less is more: an adaptive branch-site random effects model for efficient detection of episodic diversifying selection." Mol. Biol. Evol. 32, 1342–1353 (2015).`](https://doi.org/:10.1093/molbev/msv022)


<!--------------------------------------------------------------------------------------->
## BUSTED

BUSTED provides a gene-wide (*not site-specific*) test for positive selection by asking whether a gene has experienced positive selection at at least one site in at least one branch. As such, BUSTED is not suitable for identifying specific sites under selection. When running BUSTED, users can either specify a set of foreground branches on which to test for positive selection (remaining branches are designated "background"), or users can test the entire phylogeny for positive selection. In the latter case, the entire tree is effectively treated as foreground, and the test for positive selection considers the entire phylogeny.

For each phylogenetic partition (foreground and background branch sites), BUSTED fits a codon model with three rate categories: ω<sub>1</sub>≤ω<sub>2</sub>≤1≤ω<sub>3</sub>, and BUSTED estimates the proportion of sites per partition belonging to each ω category. This model, used as the alternative model in selection testing, is referred to as the *Unconstrained* model. BUSTED then tests for positive selection by comparing this model fit to a null model where ω<sub>3</sub>=1 (i.e. disallowing positive selection) on the foreground branches. This null model is also referred to as the *Constrained* model. If the null hypothesis is rejected, then there is evidence that at least one site has, at least some of the time, experienced positive selection on the foreground branches. Importantly, a significant result *does not* mean that the gene evolved under positive selection along the entire foreground.

BUSTED additionally reports "Evidence Ratios" (ERs) for each site. The ER gives the likelihood ratio (reported on a log-scale) that the alternative model was a better fit to the null model. The ER for each site thus provides *descriptive information* about whether a given site could have evolved under positive selection. The ERs *should not* be interpreted as statistical evidence for positive selection at individual sites (instead, methods like [MEME](selection-methods/#MEME), [FEL](selection-methods/#FEL), or [FUBAR](selection-methods/#FUBAR) should be used for detecting selection at individual sites). 

For each site, two ERs are reported: the *Constrained Model* ER and the *Optimized Null* model ER. The Constrained model ER calculates the evidence ratio using model parameters inferred from the Constrained model. By contrast the Optimized Null model ER re-optimizes parameters inferred using the Constrained model for the given site of interest. These optimized parameter values are then used to calculate the site's ER. Again, while these ERs may be helpful descriptors of selection in the data set, they do not provide statistically valid evidence for positive selection at a site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             


**If you use BUSTED in your analysis, please cite the following:** [`Murrell, B et al. "Gene-wide identification of episodic selection." Mol. Biol. Evol. 32, 1365–1371 (2015).`](https://doi.org/10.1093/molbev/msv035)



<!--------------------------------------------------------------------------------------->
## RELAX

RELAX is a hypothesis testing framework that asks whether the strength of natural selection has been relaxed or intensified along a specified set of test branches. RELAX is therefore not a suitable method for explicitly testing for positive selection. Instead, RELAX is most useful for identifying trends and/or shifts in the stringency of natural selection on a given gene.

RELAX requires a specified set of "test" branches to compare with an additional selection of "reference" branches (note that all branches do not have to be assigned, but one branch is required the test and reference set each). RELAX begins by fitting a codon model with three ω categories to the entire phylogeny (null model). RELAX then tests for relaxed/intensified selection by introducing the parameter **k** (where k≥0), serving as the *selection intensity parameter*, as an exponent for the inferred ω values: ω<sup>k</sup>. Specifically, RELAX fixes the inferred ω values (ω<sub>1</sub>, ω<sub>2</sub>, and ω<sub>3</sub>), and infers, for the test branches, a value for *k* which modifies the rates as ω<sub>1</sub><sup>k</sup>, ω<sub>2</sub><sup>k</sup>, and ω<sub>3</sub><sup>k</sup> (alternative model). RELAX then conducts a likelihood ratio test to compare the alternative and null models. Importantly, a significant result of *k>1* indicates that selection has *been intensified* along the test branches, and a significant result of *k<1* indicates that selection has *been relaxed* along the test branches.

In addition to this pair of null/alternative models, RELAX fits three other models meant as complementary descriptors for the data, but are not suitable for hypothesis testing. These additional models include the following:

* *Partitioned MG94xREV* - This model fits a single ω value, i.e. for all sites, to each branch partition (reference and test).
* *Partitioned Descriptive* - This model, like a more standard branch-site model, fits three ω categories separately to each branch partition (reference and test). The selection intensity parameter *k* is not included.
* *General Descriptive* - This model fits three ω categories to the full data set, ignoring the specified test and reference partition division. It subsequently fits a *k* parameter at each branch, ultimately tailoring the three ω category values to this branch. This model may serve as a useful description of how selection intensity fluctuates over the whole tree.


**If you use RELAX in your analysis, please cite the following:** [`Wertheim, JO et al. "RELAX: detecting relaxed selection in a phylogenetic framework." Mol. Biol. Evol. 32, 820–832 (2015).`](https://doi.org/10.1093/molbev/msu400)


