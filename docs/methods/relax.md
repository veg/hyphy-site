# RELAX (Detecting Relaxed or Intensified Selection)

!!! question "What question does this method answer?"
    RELAX is a hypothesis testing framework that asks whether the strength of natural selection has been relaxed or intensified in a specific set of branches (the "test" set) on a phylogenetic tree, relative to another set of branches (the "reference" set).

!!! info "Recommended Applications"

    1. **Systematic Evolutionary Shifts:** Testing for a systematic shift (relaxation / intensification) in the distribution of selection pressure associated with major biological transitions such as host switching in viruses, or lifestyle evolution in bacteria (e.g., transition from free-living to endosymbiotic lifestyle).
    2. **Comparative Selection Pressures:** Comparing selective regimes between two subsets of branches in the tree, e.g., to investigate selective differences due to an environmental or phenotypic change.

RELAX is a hypothesis testing framework that asks whether the strength of natural selection has been relaxed or intensified along a specified set of test branches. 

> [!IMPORTANT]
> RELAX is *not* a suitable method for explicitly testing for positive selection. Instead, RELAX is most useful for identifying trends and/or shifts in the stringency of natural selection on a given gene.

### How it Works
RELAX requires a specified set of "test" branches to compare with a second set of "reference" branches (note that all branches do not have to be assigned, but one branch is required for the test and reference set each). 

RELAX begins by fitting a codon model with three $\omega$ classes to the entire phylogeny (null model). RELAX then tests for relaxed/intensified selection by introducing the parameter **k** (where $k \geq 0$), serving as the *selection intensity parameter*, as an exponent for the inferred $\omega$ values: $\omega^k$. Specifically, RELAX fixes the inferred $\omega$ values (all $\omega_{1,2,3}$) and infers, for the test branches, a value for *k* which modifies the rates to $\omega_{1,2,3}^k$ (alternative model). RELAX then conducts a Likelihood Ratio Test to compare the alternative and null models. 

* **k > 1**: A significant result indicates that **selection strength has been intensified** along the test branches (i.e. $\omega$ rates pull away from 1).
* **k < 1**: A significant result indicates that **selection strength has been relaxed** along the test branches (i.e. $\omega$ rates shrink toward 1).

### Additional Models
In addition to the null/alternative hypothesis testing models, RELAX fits three other descriptive models:

* **Partitioned MG94xREV**: Fits a single $\omega$ value (shared for all sites) to each branch partition (reference and test). Here, a total of two $\omega$ rates are inferred.
* **Partitioned Descriptive**: Fits three $\omega$ classes separately to each branch partition (reference and test, producing a total of six estimated $\omega$ rates). The selection intensity parameter *k* is not included.
* **General Descriptive**: Fits three $\omega$ classes to the full data set, ignoring the test/reference partitions. It subsequently fits a *k* parameter at each branch, tailoring the three $\omega$ class values to this branch. This model serves as a description of how selection intensity fluctuates over the tree.

---

### Citation
If you use RELAX in your analysis, please cite the following:
> Wertheim, JO et al. ["RELAX: detecting relaxed selection in a phylogenetic framework."](https://doi.org/10.1093/molbev/msu400) *Mol. Biol. Evol.* 32, 820–832 (2015).
