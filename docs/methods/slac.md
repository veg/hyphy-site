# Single-Likelihood Ancestor Counting (SLAC)

!!! question "What question does this method answer?"
    Which specific sites in a gene show evidence of positive diversifying or purifying selection that has been maintained throughout the evolutionary history of the analyzed sequences (pervasive selection)?

!!! info "Recommended Applications"

    * **Pathogen Evolution & Arms Races:** Identify candidate sites subject to strong selective pressures across the entire phylogeny (e.g. adaptive immune escape by viruses).
    * **Legacy / Interpretability:** SLAC provides legacy counting-based functionality. It is generally the least statistically robust method (compared to FEL or FUBAR), but it is the most directly interpretable.

## Description

The Single-Likelihood Ancestor Counting (SLAC) method is used to identify individual codon sites subject to pervasive diversifying or purifying selection. SLAC is a counting-based method that is computationally faster than FEL, making it suitable for larger datasets, though it can be less accurate for highly divergent sequences.

## Statistical Method

SLAC combines maximum-likelihood (ML) estimation and heuristic counting:
1. **Global Fit**: It first optimizes branch lengths and nucleotide substitution parameters under the MG94xREV model across the entire alignment.
2. **Ancestral Reconstruction**: Under these optimized parameters, SLAC uses joint maximum-likelihood to reconstruct ancestral sequences at each internal node of the phylogeny.
3. **Counting**: For each site, it counts the numbers of synonymous and nonsynonymous substitutions along each branch using a modified Suzuki-Gojobori counting procedure. It also calculates the expected numbers of synonymous and nonsynonymous sites to determine expected rates under neutral evolution.
4. **Hypothesis Testing**: A two-tailed binomial test is used to determine whether the observed number of substitutions significantly deviates from the null hypothesis of neutrality ($dN = dS$).
   - **Positive selection** is inferred when the observed nonsynonymous rate is significantly higher than expected ($dN > dS$).
   - **Purifying selection** is inferred when the observed nonsynonymous rate is significantly lower than expected ($dN < dS$).

## Publication

[Kosakovsky Pond, S. L., and Frost, S. D. W. "Not So Different After All: A Comparison of Methods for Detecting Amino Acid Sites Under Selection." *Mol. Biol. Evol.* 22, 1208–1222 (2005).](https://doi.org/10.1093/molbev/msi105)

## Visualization

The JSON output from SLAC can be interactively visualized at [vision.hyphy.org/SLAC](http://vision.hyphy.org/SLAC). You can upload the `lysozyme.slac.json` file to the visualizer. This will generate:

*   A plot of dN and dS estimates for each site.
*   A table of the site-by-site results.

This interactive visualization is a powerful tool for exploring the results and identifying key sites of interest.

## Published Applications

*   **Viral Evolution:** [Frost, S. D. W., et al. (2005). Characterization of selective pressures on the gp120 envelope gene of HIV-1 in vivo. *Journal of Virology*, 79(10): 6523–6527.](https://pubmed.ncbi.nlm.nih.gov/15858036/)

    This study investigated the selective pressures on the gp120 envelope gene of HIV-1 within and between patients. The SLAC method was used to identify specific codon sites in gp120 under positive selection to analyze how the virus adapts to host immune responses.

*   **Mammalian Neuropeptide Receptors:** [Bakiu, R., Korro, K., & Santovito, G. (2015). Positive selection effects on the biochemical properties of mammal pyroglutamylated RFamide peptide receptor (QRFPR). *Italian Journal of Zoology*, *82*(3), 309-326.](https://pubmed.ncbi.nlm.nih.gov/26018900/)

    This study explored the evolution of the QRFPR gene, which encodes a receptor for neuropeptides involved in regulating various physiological processes in mammals. The SLAC method, along with other methods, was used to detect sites under positive selection in the QRFPR gene across different mammal species. The analysis identified several sites under positive selection, suggesting that the QRFPR gene has been subject to adaptive evolution in mammals. The key contribution of the SLAC method was to identify specific amino acid changes that may have altered the function of the QRFPR receptor, potentially contributing to the diversification of physiological traits in mammals.
