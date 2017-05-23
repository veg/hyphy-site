# Methods for Inferring Selection Pressure

HyPhy distributes a variety of methods for inferring the strength of natural selection in your data using the *dN/dS* metric. Here, we provide an overview of each method. For help determining which method best suits your specific needs, follow [these guidelines](../getting-started/#characterizing-selective-pressures).



## aBSREL

aBSREL (**a**daptive **B**ranch-**S**ite **R**andom **E**ffects **L**ikelihood) is an improved version of the commonly-used "branch-site" models, which are used to test if positive selection has occurred on a proportion of branches. As such, aBSREL models both site-level and branch-level $\omega$  heterogeneity. aBSREL, however, does not test for selection at specific sites. Instead, aBSREL will test, for each branch (or branch of interest) in the phylogeny, whether a proportion of sites have evolved under positive selection. 

aBSREL differs from other branch-site model implementations by inferring the optimal number of $\omega$  classes for each branch. For example, the earlier HyPhy branch-site approach (BS-REL) assumed three $\omega$  rate classes for each branch and assigned each site, with some probability, to one of these classes. aBSREL, by contrast, acknowledges that different branches may feature more or less complex evolutionary patterns and hence may be better modeled by more or fewer $\omega$ classes. Specifically, aBSREL uses AIC<sub>c</sub> (small sample AIC) to infer the optimal number of $\omega$ rate classes for each branch. 

After aBSREL fits the full adaptive model, the Likelihood Ratio Test is performed at each branch and compares the full model to a null model where branches are not allowed to have rate classes of $\omega>1$. 

aBSREL can be run in two modes:

* Test a specific hypothesis by *a priori* selecting a set of "foreground" branches to test for positive selection. 
* Perform an exploratory analysis where all branches are tested for positive selection. In this scenario, p-values at each branch must be corrected for multiple testing (using the Holm-Bonferroni correction). Due to multiple testing, the exploratory approach *has much lower power* compared to the other approach. 


**If you use aBSREL in your analysis, please cite the following:** [`Smith, MD et al. "Less is more: an adaptive branch-site random effects model for efficient detection of episodic diversifying selection." Mol. Biol. Evol. 32, 1342–1353 (2015).`](https://doi.org/10.1093/molbev/msv022)

<!--------------------------------------------------------------------------------------->

## BUSTED

BUSTED (**B**ranch-**S**ite **U**nrestricted **S**tatistical **T**est for **E**pisodic **D**iversification) provides a gene-wide (*not site-specific*) test for positive selection by asking whether a gene has experienced positive selection at at least one site on at least one branch. When running BUSTED, users can either specify a set of foreground branches on which to test for positive selection (remaining branches are designated "background"), or users can test the entire phylogeny for positive selection. In the latter case, the entire tree is effectively treated as foreground, and the test for positive selection considers the entire phylogeny.

For each phylogenetic partition (foreground and background branch sites), BUSTED fits a codon model with three rate classes, constrained as $\omega_1 < \omega_2 < 1 < \omega_3$. As in other methods, BUSTED simultaneously estimates the proportion of sites per partition belonging to each $\omega$  class. This model, used as the alternative model in selection testing, is referred to as the *Unconstrained* model. BUSTED then tests for positive selection by comparing this model fit to a null model where $\omega_3 = 1$ (i.e. disallowing positive selection) on the foreground branches. This null model is also referred to as the *Constrained* model. If the null hypothesis is rejected, then there is evidence that at least one site has, at least some of the time, experienced positive selection on the foreground branches. Importantly, a significant result *does not* mean that the gene evolved under positive selection along the entire foreground.

BUSTED additionally calculates "Evidence Ratios" (ERs) for each site. The ER gives the likelihood ratio (reported on a log-scale) that the alternative model was a better fit to the data compared to the null model. The ER for each site thus provides *descriptive information* about whether a given site could have evolved under positive selection. The ERs *should not* be interpreted as statistical evidence for positive selection at individual sites (instead, methods like [MEME](selection-methods/#meme), [FEL](selection-methods/#fel), or [FUBAR](selection-methods/#fubar) should be used for detecting selection at individual sites). 

For each site, two ERs are reported: the *Constrained Model* ER and the *Optimized Null* Model ER. The Constrained Model ER calculates the evidence ratio using model parameters inferred from the Constrained model. By contrast, the Optimized Null model ER re-optimizes parameters inferred using the Constrained model for the given site of interest. These optimized parameter values are then used to calculate the site's ER. Again, while these ERs may be helpful descriptors of selection in the data set, they do not provide statistically valid evidence for positive selection at a site.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

**If you use BUSTED in your analysis, please cite the following:** [`Murrell, B et al. "Gene-wide identification of episodic selection." Mol. Biol. Evol. 32, 1365–1371 (2015).`](https://doi.org/10.1093/molbev/msv035)


<!--------------------------------------------------------------------------------------->

<!--
## FADE


[forthcoming]
-->

<!--------------------------------------------------------------------------------------->
## FEL


FEL (**F**ixed **E**fects **L**ikelihood) uses a maximum-likelihood (ML) approach to infer nonsynoymous (dN) and synonymous (dS) substitution rates on a per-site basis for a given coding alignment and corresponding phylogeny. This method assumes that the selection pressure for each site is constant along the entire phylogeny. 

After optimizing branch lengths and nucleotide substitution parameters, FEL fits a MG94xREV model to each codon site to infer site-specific nonsynonymous and synonymous (dN and dS, respectively) substitution rates. Hypothesis testing is then conducted on a site-specific basis, using the Likelihood Ratio Test, to ascertain if dN is significantly greater than dS.


**If you use FEL in your analysis, please cite the following:** [`Kosakovsky Pond, SL and Frost, SDW. "Not So Different After All: A Comparison of Methods for Detecting Amino Acid Sites Under Selection." Mol. Biol. Evol. 22, 1208--1222 (2005).`](https://doi.org/10.1093/molbev/msi105)


<!--------------------------------------------------------------------------------------->
## FUBAR 

FUBAR (**F**ast, **U**nconstrained **B**ayesian **A**pp**R**oximation) uses a Bayesian approach to infer nonsynoymous (dN) and synonymous (dS) substitution rates on a per-site basis for a given coding alignment and corresponding phylogeny. This method assumes that the selection pressure for each site is constant along the entire phylogeny.

Although FUBAR produces similar information to FEL, it has several key differences:

* FUBAR employs a Bayesian algorithm to infer rates, and therefore it reports evidence for positive selection using *posterior probabilities* (which range from 0-1), not p-values. Generally, posterior probabilities > 0.9 are strongly suggestive of positive selection. 
* FUBAR runs extremely quickly and is well-suited for analyzing large alignments, with hundreds or thousands of sequences. This speed-up results from the novel strategy of employing a pre-specified discrete grid of dN and dS values to be applied across sites. This approach contrasts with the time-consuming FEL strategy of fitting a new MG94xREV model at each site.
* FUBAR may have more power than FEL, in particular when positive selection is present but relatively weak (i.e. low values of $\omega>1$).

**If you use FUBAR in your analysis, please cite the following:** [`Murrell, B et al. "FUBAR: A Fast, Unconstrained Bayesian AppRoximation for inferring selection." Mol. Biol. Evol. 30, 1196–1205 (2013).`](https://doi.org/10.1093/molbev/mst030)





<!--------------------------------------------------------------------------------------->
## GARD 

GARD (**G**enetic **A**lgorithm for **R**ecombination **D**etection) is a method to screen a multiple sequence analysis for the presence of recombination and is extremely useful as a *pre-processing step for selection inference*. Because recombinant sequences cannot be adequately described with a single phylogenetic history, selection inference on recombinant data often leads to a significant increase in false positives. GARD alleviates this concern by comprehensively screening an alignment for recombination breakpoints and inferring a unique phylogenetic history for each detected recombination block.

If GARD detects recombination in your dataset, it will provide you with an updated *partitioned* dataset, where each partition corresponds to a recombination block with its own corresponding phylogeny. This partitioned dataset can then be used as input (instead of your original data) for the selection inference method of interest.

<!--
Methods which accept data processed by GARD include the following: 

+ [FEL](./selection-methods/#fel)
+ [FUBAR](./selection-methods/#fubar)
+ [SLAC](./selection-methods/#slac)
+ ...more...
-->

**If you use GARD in your analysis, please cite the following:** [`Kosakovsky Pond, SL et al. "Automated Phylogenetic Detection of Recombination Using a Genetic Algorithm." Mol. Biol. Evol. 23, 1891–1901 (2006).`](https://doi.org/10.1093/molbev/msl051)



<!--------------------------------------------------------------------------------------->
## MEME

MEME (**M**ixed **E**ffects **M**odel of **E**volution) employs a mixed-effects maximum likelihood approach to test the hypothesis that individual sites have been subject to episodic positive or diversifying selection. 
In other words, MEME aims to detect sites evolving under positive selection under a *proportion* of branches.


For each site, MEME infers two $\omega$ rate classes and corresponding weights representing the probability that the site evolves under $\omega$ rate class, at a given branch. Importantly, to infer $\omega$ rates, MEME infers a single $\alpha$ (dS) value and two separate $\beta$ (dN) values, $\beta^-$ and $\beta^+$, which share the same $\alpha$, per site. For both the null and alternative model, MEME enforces the constraint $\beta^- \leq \alpha$. The $\beta^+$ parameter is therefore the key difference between null and alternative models: In the null model, $\beta^+$ is constrained as in the null model: $\beta^+ \leq \alpha$, but $\beta^+$ is not constrained in the alternative model. Ultimately, positive selection for each site is inferred when $\beta^+ > \alpha$ and shown to be significant using the likelihood ratio test. 
 

**If you use MEME in your analysis, please cite the following:** [`Murrell, B et al. "Detecting individual sites subject to episodic diversifying selection." PLoS Genetics 8, e1002764 (2012).`](http://dx.doi.org/10.1371/journal.pgen.1002764)



<!--------------------------------------------------------------------------------------->
## RELAX

RELAX is a hypothesis testing framework that asks whether the strength of natural selection has been relaxed or intensified along a specified set of test branches. RELAX is therefore *not* a suitable method for explicitly testing for positive selection. Instead, RELAX is most useful for identifying trends and/or shifts in the stringency of natural selection on a given gene.

RELAX requires a specified set of "test" branches to compare with a second set of "reference" branches (note that all branches do not have to be assigned, but one branch is required the test and reference set each). RELAX begins by fitting a codon model with three $\omega$  classes to the entire phylogeny (null model). RELAX then tests for relaxed/intensified selection by introducing the parameter **k** (where $k \geq 0$), serving as the *selection intensity parameter*, as an exponent for the inferred $\omega$  values: $\omega^k$. Specifically, RELAX fixes the inferred $\omega$ values (all $\omega_{<1,2,3>}$) and infers, for the test branches, a value for *k* which modifies the rates to $\omega_{<1,2,3>}^k$ (alternative model). RELAX then conducts a Likelihood Ratio Test to compare the alternative and null models. 

A significant result of **k>1 indicates that selection strength has been intensified** along the test branches, and a significant result of **k<1 indicates that selection strength has been relaxed** along the test branches.

In addition to this pair of null/alternative models, RELAX fits three other models meant as complementary descriptors for the data, but are not suitable for hypothesis testing. These additional models include the following:

* *Partitioned MG94xREV* - This model fits a single $\omega$ value, i.e. shared for all sites, to each branch partition (reference and test). Here, a total of two $\omega$ rates are inferred.
* *Partitioned Descriptive* - This model, like a more standard branch-site model, fits three $\omega$  classes separately to each branch partition (reference and test, producing a total of six estimated $\omega$ rates estimated). The selection intensity parameter *k* is not included.
* *General Descriptive* - This model fits three $\omega$  classes to the full data set, ignoring the specified test and reference partition division (three total $\omega$ rates estimated). It subsequently fits a *k* parameter at each branch, ultimately tailoring the three $\omega$  class values to this branch. This model may serve as a useful description of how selection intensity fluctuates over the whole tree.


**If you use RELAX in your analysis, please cite the following:** [`Wertheim, JO et al. "RELAX: detecting relaxed selection in a phylogenetic framework." Mol. Biol. Evol. 32, 820–832 (2015).`](https://doi.org/10.1093/molbev/msu400)



<!--------------------------------------------------------------------------------------->
## SLAC

SLAC (**S**ingle-**L**ikelihood **A**ncestor **C**ounting) uses a combination of maximum-likelihood (ML) and counting approaches to infer nonsynonymous (dN) and synonymous (dS) substitution rates on a per-site basis for a given coding alignment and corresponding phylogeny. Like FEL, this method assumes that the selection pressure for each site is constant along the entire phylogeny. 

SLAC begins by optimizing branch lengths and nucleotide substitution parameters under the MG94xREV model. However, rather than using ML to fit site-specific dN and dS parameters, SLAC instead uses ML to infer the most likely ancestral sequence at each node of the phylogeny. SLAC then employs a modified version of the [Suzuki-Gojobori counting method](https://doi.org/10.1093/oxfordjournals.molbev.a026042) to directly count the total number of nonsynonymous and synonymous changes which have occurred at each site. Significance is ascertained at each site using an extended binomial distribution. Importantly, due to its counting-based approach, SLAC may not be accurate for data sets with high divergence levels.

**If you use SLAC in your analysis, please cite the following:** [`Kosakovsky Pond, SL and Frost, SDW. "Not So Different After All: A Comparison of Methods for Detecting Amino Acid Sites Under Selection." Mol. Biol. Evol. 22, 1208--1222 (2005).`](https://doi.org/10.1093/molbev/msi105)


