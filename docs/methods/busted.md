# BUSTED (Branch-Site Unrestricted Statistical Test for Episodic Diversification)

!!! question "What question does this method answer?"
    Is there evidence that some sites in the alignment have been subject to positive diversifying selection, either pervasive (throughout the evolutionary tree) or episodic (only on some lineages)? In other words, BUSTED asks whether a given gene has been subject to positive, diversifying selection at any site, at any time.
    
    If a priori information about lineages of interest is available (e.g., due to migration, change in the environment, etc.), then BUSTED can be restricted to test for selection only on a subset of tree lineages, potentially boosting power.

!!! info "Recommended Applications"

    1. **Alignment Screening/Annotation:** Annotating a collection of alignments with a binary attribute: has this alignment been subject to positive diversifying selection (yes/no)?
    2. **Low-divergence / Small datasets:** Testing small or low-divergence alignments (i.e. ~30 sequences) for evidence of positive diversifying selection, where neither branch nor site-level methods have sufficient power.

BUSTED (**B**ranch-**S**ite **U**nrestricted **S**tatistical **T**est for **E**pisodic **D**iversification) provides a gene-wide (*not site-specific*) test for positive selection by asking whether a gene has experienced positive selection at at least one site on at least one branch. 

When running BUSTED, users can either specify a set of foreground branches on which to test for positive selection (remaining branches are designated "background"), or users can test the entire phylogeny for positive selection. In the latter case, the entire tree is effectively treated as foreground, and the test for positive selection considers the entire phylogeny.

### How it Works
For each phylogenetic partition (foreground and background branch sites), BUSTED fits a codon model with three rate classes, constrained as $\omega_1 \leq \omega_2 \leq 1 \leq \omega_3$. As in other methods, BUSTED simultaneously estimates the proportion of sites per partition belonging to each $\omega$ class. This model, used as the alternative model in selection testing, is referred to as the *Unconstrained* model. 

BUSTED then tests for positive selection by comparing this model fit to a null model where $\omega_3 = 1$ (i.e. disallowing positive selection) on the foreground branches. This null model is also referred to as the *Constrained* model. If the null hypothesis is rejected, then there is evidence that at least one site has, at least some of the time, experienced positive selection on the foreground branches. Importantly, a significant result *does not* mean that the gene evolved under positive selection along the entire foreground.

### Site-level Evidence Ratios
BUSTED additionally calculates "Evidence Ratios" (ERs) for each site. The ER gives the likelihood ratio (reported on a log-scale) that the alternative model was a better fit to the data compared to the null model. The ER for each site thus provides *descriptive information* about whether a given site could have evolved under positive selection. 

> [!IMPORTANT]
> The ERs *should not* be interpreted as statistical evidence for positive selection at individual sites (instead, methods like [MEME](meme.md), [FEL](fel.md), or [FUBAR](fubar.md) should be used for detecting selection at individual sites). 

For each site, two ERs are reported:
* **Constrained Model ER**: Calculates the evidence ratio using model parameters inferred from the Constrained model. 
* **Optimized Null Model ER**: Re-optimizes parameters inferred using the Constrained model for the given site of interest. These optimized parameter values are then used to calculate the site's ER.

---

### Citation
If you use BUSTED in your analysis, please cite the following:
> Murrell, B et al. ["Gene-wide identification of episodic selection."](https://doi.org/10.1093/molbev/msv035) *Mol. Biol. Evol.* 32, 1365–1371 (2015).
