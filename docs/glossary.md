This glossary provides definitions for terms in the HyPhy-Vision reports for each method. See [here](./selection-methods) for descriptions of each method. 

## aBSREL Glossary

<!-- I think the following has been removed from vision
### Summary Statistics **\\\\ has this info since been removed?**
* **number of sequences** - the number of sequences present in the input file
* **number of variants** - the number of variants present in the input file
* **number of branches** - the number of branches in the phylogeny
--> 

### Summary: Tree Table
The Tree Table reports a summary of the inferred the number of rate classes across branches.

* **ω rate classes** - Number of rate classes inferred, where ω represents the ratio of nonsynonymous to synonymous substitution rates
* **\# of branches** - The number of branches inferred to have the respective number of ω rate classes 
* **% of branches** - The proportion of branches inferred to have the respective number of ω rate classes 
* **% of tree length** - The percent of the total tree length inferred to have the respective number of ω rate classes 
* **\# under selection** - The number of branches inferred to have undergone positive selection (a rate class of ω>1) at the designated p-value threshold, after correction for multiple testing

### Summary: Model Fits Table

The Model Fits Table reports a summary of the models fit to the data.

* **Model** - The model fit.
    * **MG94** - Refers to the baseline model fit, using the standard [Must-Gaut 1994](https://www.ncbi.nlm.nih.gov/labs/articles/7968485/) model (specifically the [MG94-REV](https://www.ncbi.nlm.nih.gov/pubmed/15703242) formulation), where a single ω rate category is inferred per branch. 
    * **Full Model** - Refers to the full aBSREL model fit to the tree, with the number of ω categories per branch inferred using the adaptive algorithm.
* ***log* L** - The log likelihood estimate of the respective model fit.
* **\# par.** - The number of estimated parameters in the respective model.
* **Time to fit** - Total **TYPE** time, in seconds, to fit the respective model.
* **AIC<sub>c</sub>**  - Resulting small-sample Akaike Information Criterion [(Sugiura, 1978, Commun. Stat. Theory Methods, A7:13)](http://www.tandfonline.com/doi/abs/10.1080/03610927808827599) score, calculated when inferring the optimal number of ω rate categories at each branch in the phylogeny.
* **L<sub>tree</sub>** - The tree length under the respective model, where tree length represents the expected number of substitutions per site.


### Full Table
The full Results Table reports inferences of positive selection for each branch.

* **Name** - Branch of interest, where bolded rows refer to branches inferred to have experienced position selection at the designated p-value threshold  
* **B** - **Branch length for the branch of interest -- CURRENTLY EMPTY IN THE TABLE**
* **LRT** - Likelihood ratio test statistic for selection 
* **Test p-value** - P-value corrected for multiple testing using the Holm-Bonferroni correction [(Holm, 1979, Scand. J. Statist., 6:65)](https://www.jstor.org/stable/4615733)
* **Uncorrected p-value** - Raw p-value before correction for multiple testing
* **ω distribution over sites** - Inferred ω estimates and respective proportion of sites along the respective branch


<!------------------------------------------------------------------------------------->


## RELAX Glossary

### Summary: Model Fits Table

The Model Fits Table reports a summary of the models fit to the data. Corresponding plots of ω distributions display inferred ω values, and when applicable, how selection intensity compares across ω categories between test and reference branches.

* **Model** - The model fit. For a more thorough description of these models, see [this fake link](http://thislinkisalie.com).
    * **Partitioned MG94xREV** - This baseline model fits a single rate category, respectively, for each of the two branch sets (reference and test).
    * **General Descriptive** - This model fits a single ω distribution shared across all branches (single partition analysis), but wherein a selection intensity parameter *k* is inferred for each branch.  an overall description of the data, fits a three ω rate categories to all branches as a single partition.
    * **Null** - This model represents the null model used to test for selection, where the selection intensity parameter *k* is set to 1 for both branch sets (reference and test).
    * **Alternative** - This model represents the alternative model used to test for selection, where the selection intensity parameter *k* is allowed for vary on the "test" partition of branches. Note that all test branches will share the value for *k*.
    * **Partitioned Descriptive** - This model infers ω distributions for each partition, without using the selection intensity parameter *k* (e.g. k=1). 



<!------------------------------------------------------------------------------------->



## BUSTED Glossary

### Summary: Model Fits Table

The Model Fits Table reports a summary of the models fit to the data.

* **Model** - The model fit.
    * **Unconstrained model** - Refers to the alternative model fit to the data where the ω rate category used to test for selection is permitted to exceed 1 on the foreground branches.  
    * **Constrained model** - Refers to a baseline model fit to the data where the background and foreground branches share all ω rate categories, specifically where the ω rate category used to test for selection is constrained to equal 1.
* ***log* L** - The log likelihood estimate of the respective model fit.
* **\# par.** - The number of estimated parameters in the respective model.
* **Time to fit** - Total **TYPE** time, in seconds, to fit the respective model.
* **AIC<sub>c</sub>**  - Resulting small-sample Akaike Information Criterion [(Sugiura, 1978, Commun. Stat. Theory Methods, A7:13)](http://www.tandfonline.com/doi/abs/10.1080/03610927808827599) score.
* **L<sub>tree</sub>** - The tree length under the respective model, where tree length represents the expected number of substitutions per site.
* **Branch Set** - ** I think this should go: The specified name for the set of branches with inferred rates under this model**
* **ω<sub><1,2,3></sub>** - The inferred ω value for the given rate category (1, 2, or 3) with the respective proportion of sites inferred to belong to this category.


### Summary: Model Evidence Ratios Per Site

This plot shows the "Evidence Ratio", displayed as the scaled likelihood ratio test statistic, indicating evidence for whether a given site experienced positive selection each model (**HELP, MODELS UNCLEAR**). **Importantly, These values should not be interpreted as definitive estimates of selection at individual sites.** 

### Summary: Model Evidence Ratios Per Site Table

This table provides site-specific inference information.

* **Site Index** - The codon site of interest.
* **Unconstrained likelihood** - The log likelihood score for the codon site of interest, calculated for the unconstrained model fit.
* **Constrained likelihood** - The log likelihood score for the codon site of interest, calculated for the Constrained Model fit.
* **Optimized Null Likelihood** - TBD
* **Constrained Evidence Ratio** - Evidence ratio for selection at the given codon site under the **Constrained Model**
* **Optimized Null Evidence Ratio** - Evidence ratio for selection at the given codon site under the **mystery model**





