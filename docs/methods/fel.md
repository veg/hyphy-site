# Fixed Effects Likelihood (FEL)

!!! question "What question does this method answer?"
    FEL (Fixed Effects Likelihood) addresses the question: Which specific sites in a gene show evidence of positive diversifying or purifying selection that has been consistently maintained (pervasive) across the entire evolutionary phylogeny of the analyzed sequences?

!!! info "Recommended Applications"

    * **Pervasive Selection / Evolutionary Arms Races:** Ideally suited to identify candidate sites subject to strong selective pressures across the entire phylogeny, which is common in pathogen evolution and arms-race dynamics (e.g., adaptive immune escape by viruses).
    * **Small-to-Medium Datasets:** FEL is the recommended method for analyzing small-to-medium size datasets (up to ~100 sequences) when one wishes only to study pervasive selection at individual sites.

## Description

The Fixed Effects Likelihood (FEL) method is used to identify individual codons that have been subject to pervasive diversifying or purifying selection. This method is suitable for small to medium-sized datasets and assumes that selection pressure at a site is constant along the entire phylogeny. FEL directly estimates nonsynonymous (dN) and synonymous (dS) substitution rates for each site and uses a likelihood ratio test to infer selection.

## Statistical Method

FEL employs a maximum-likelihood framework to infer site-specific rates of nonsynonymous (dN or β) and synonymous (dS or α) substitutions. The method fits an MG94xREV codon model to each site in a coding sequence alignment, given a phylogenetic tree.

A key assumption of FEL is that the selective pressure for each site is constant across all branches of the phylogeny. To test for selection at a site, FEL uses a likelihood ratio test (LRT). This test compares the likelihood of a null model, where dN = dS, to an alternative model, where dN and dS are estimated independently.

If the alternative model provides a significantly better fit to the data (i.e., the LRT statistic is large and the p-value is small), then the null model of neutral evolution is rejected.
- **Positive (or diversifying) selection** is inferred when dN > dS.
- **Purifying (or negative) selection** is inferred when dN < dS.

## Publication

[Kosakovsky Pond, S. L., and Frost, S. D. W. "Not So Different After All: A Comparison of Methods for Detecting Amino Acid Sites Under Selection." *Mol. Biol. Evol.* 22, 1208–1222 (2005).](https://doi.org/10.1093/molbev/msi105)

## Visualization

The JSON output from FEL can be interactively visualized at [vision.hyphy.org/FEL](http://vision.hyphy.org/FEL). You can upload the `lysozyme.fel.json` file to the visualizer. This will generate:

*   A plot of dN/dS ratios for each site, allowing for easy identification of sites under selection.
*   Bar plots of the estimated dN and dS rates for each site.
*   A table of the site-by-site results.

This interactive visualization is a powerful tool for exploring the results and identifying key sites of interest.

## Published Applications

The FEL method has been used in a variety of studies to detect selection in genes from different organisms. Some examples include:

*   **Viral Evolution:** [Botosso, V. P., et al. (2009). Positive Selection Results in Frequent Reversible Amino Acid Replacements in the G Protein Gene of Human Respiratory Syncytial Virus. *PLoS Pathogens*, 5(1): e1000254.](https://pubmed.ncbi.nlm.nih.gov/19119418/)

    This study investigated the evolutionary dynamics of the G protein gene in Human Respiratory Syncytial Virus (HRSV), a major cause of respiratory infections. The FEL method was used to identify individual amino acid sites under positive selection in the G protein. The analysis revealed numerous positively selected sites, many of which exhibited a "flip-flop" phylogenetic pattern, suggesting frequent reversible amino acid replacements. The key contribution of the FEL method was to highlight how HRSV adapts to the host immune system through rapid evolution at specific sites, providing insights into viral immune evasion strategies.

*   **Plant Biology:** [Zamora, A., et al. (2009). Positively selected disease response orthologous gene sets in the cereals identified using Sorghum bicolor L. Moench expression profiles and comparative genomics. *Molecular Biology and Evolution*, 26(9): 2015-2030.](https://pubmed.ncbi.nlm.nih.gov/19506000/)

    This study aimed to identify disease response genes in cereals that show signs of positive selection, contributing to our understanding of plant defense mechanisms. The researchers used gene expression data from *Sorghum bicolor* and comparative genomics across several grass species. The FEL method was applied to test for positive selection in orthologous gene sets. The results indicated that several genes, including a peroxidase and a thaumatin-like protein, have evolved under positive selection. The key contribution of the FEL method was to provide evidence that these genes are involved in an evolutionary "arms race" with pathogens, confirming their importance in plant defense and adaptation.

*   **Immunology:** [Martin, K. R., Mansfield, K. L., & Savage, A. E. (2022). Adaptive evolution of major histocompatibility complex class I immune genes and disease associations in coastal juvenile sea turtles. *R. Soc. Open Sci.*, 9(2): 211190.](https://pubmed.ncbi.nlm.nih.gov/35154791/)

    This research characterized the polymorphism and adaptive evolution of Major Histocompatibility Complex (MHC) class I genes in juvenile green and loggerhead sea turtles. The FEL method was employed to detect sites under positive selection within the MHC class I genes. The analysis revealed extensive variation and trans-species polymorphism, with specific sites showing strong signatures of positive selection. The key contribution of the FEL method was to identify adaptive changes in MHC genes that are likely driven by pathogen pressure, providing insights into the genetic basis of disease resistance and susceptibility in sea turtle populations, particularly in relation to fibropapillomatosis.

