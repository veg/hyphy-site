# aBSREL (Adaptive Branch-Site Random Effects Likelihood)

!!! question "What question does this method answer?"
    aBSREL (adaptive Branch-Site Random Effects Likelihood) is a powerful method for detecting episodic positive selection. It identifies instances where a proportion of sites along specific branches or lineages of a phylogeny have undergone positive selection.

!!! info "Recommended Applications"

    1. **Detecting Episodic Diversifying Selection:** Ideal for exploratory testing to find evidence of lineage-specific positive diversifying selection in alignments of various sizes.
    2. **Targeted Branch Testing:** Suitable for targeted testing of branches hypothesized to be under positive selection, even in alignments that would be computationally prohibitive for older branch-site models.

aBSREL (**a**daptive **B**ranch-**S**ite **R**andom **E**ffects **L**ikelihood) is an improved version of the commonly-used "branch-site" models, which are used to test if positive selection has occurred on a proportion of branches. As such, aBSREL models both site-level and branch-level $\omega$ heterogeneity. aBSREL, however, does not test for selection at specific sites. Instead, aBSREL will test, for each branch (or branch of interest) in the phylogeny, whether a proportion of sites have evolved under positive selection. 

aBSREL differs from other branch-site model implementations by inferring the optimal number of $\omega$ classes for each branch. For example, the earlier HyPhy branch-site approach (BS-REL) assumed three $\omega$ rate classes for each branch and assigned each site, with some probability, to one of these classes. aBSREL, by contrast, acknowledges that different branches may feature more or less complex evolutionary patterns and hence may be better modeled by more or fewer $\omega$ classes. Specifically, aBSREL uses AIC<sub>c</sub> (small sample AIC) to infer the optimal number of $\omega$ rate classes for each branch. 

After aBSREL fits the full adaptive model, the Likelihood Ratio Test is performed at each branch and compares the full model to a null model where branches are not allowed to have rate classes of $\omega>1$. 

### Run Modes
aBSREL can be run in two modes:

* **Hypothesis Testing**: Select a specific set of "foreground" branches *a priori* to test for positive selection. 
* **Exploratory Analysis**: Test all branches in the phylogeny for positive selection. In this scenario, p-values at each branch must be corrected for multiple testing (using the Holm-Bonferroni correction). Due to multiple testing corrections, the exploratory approach *has much lower power* compared to hypothesis testing.

---

### Citation
If you use aBSREL in your analysis, please cite the following:
> Smith, MD et al. ["Less is more: an adaptive branch-site random effects model for efficient detection of episodic diversifying selection."](https://doi.org/10.1093/molbev/msv022) *Mol. Biol. Evol.* 32, 1342–1353 (2015).
