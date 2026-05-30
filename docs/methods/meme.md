# Mixed Effects Model of Evolution (MEME)

!!! question "What question does this method answer?"
    Which site(s) in a gene are subject to pervasive or *episodic* (only on a single lineage or subset of lineages) diversifying selection?

!!! info "Recommended Applications"

    * **Episodic and Pervasive Selection:** Ideally suited to identify candidate sites subject to selective pressures across the entire phylogeny or only on parts of the phylogeny.
    * **Maximum Power:** MEME is the sole method in HyPhy for detecting selection at individual sites that considers both pervasive and episodic selection, and is therefore the recommended method if maximum power is desired.

## Description

The Mixed Effects Model of Evolution (MEME) is used to identify individual codon sites subject to episodic or pervasive positive selection. Unlike traditional methods (such as FEL) that assume selection pressure at a site is constant across all branches of a phylogeny, MEME allows the selection pressure (measured as $dN/dS$) to vary from branch to branch at a given site. This makes it highly powerful for detecting selection that is restricted to a subset of branches (episodic selection).

## Statistical Method

MEME employs a mixed-effects maximum likelihood framework to model site-specific rates of nonsynonymous ($\beta$) and synonymous ($\alpha$) substitutions.

For each site, MEME infers a single synonymous rate ($\alpha$) and two separate nonsynonymous rates: $\beta^+$ and $\beta^-$, which are shared across branches but distributed with site-specific weights:
* $\beta^-$ represents a rate class under purifying or neutral selection ($\beta^- \leq \alpha$).
* $\beta^+$ represents a rate class that can be under positive selection ($\beta^+$ is unrestricted).

For each branch at a given site, the nonsynonymous rate is assumed to be $\beta^-$ with probability $1 - q$ and $\beta^+$ with probability $q$.

**Alternative Model Constraints**
$$ \alpha \text{ unrestricted}, \quad \beta^+ \text{ unrestricted}, \quad \beta^- \leq \alpha $$

**Null Model Constraints**
$$ \alpha \text{ unrestricted}, \quad \beta^+ \leq \alpha, \quad \beta^- \leq \alpha $$

The $\beta^+$ parameter is the key difference between the null and alternative models. In the null model, both $\beta^+$ and $\beta^-$ are constrained, whereas $\beta^+$ is unrestricted in the alternative model. 

Positive selection for each site is inferred when $\beta^+ > \alpha$ and shown to be statistically significant using a likelihood ratio test (LRT) comparing the null and alternative models.

## Publication

[Murrell, B., Wertheim, J. O., Moola, S., Weighill, T., Scheffler, K., & Kosakovsky Pond, S. L. "Detecting Individual Sites Subject to Episodic Diversifying Selection." *PLoS Genetics*, 8(7), e1002764 (2012).](https://doi.org/10.1371/journal.pgen.1002764)

## Visualization

The JSON output from MEME can be interactively visualized at [vision.hyphy.org/MEME](http://vision.hyphy.org/MEME). Uploading your results file (e.g., `lysozyme.meme.json`) allows you to explore:
*   A plot of $p$-values and dN/dS ratios across all sites to locate episodic selection.
*   The estimated distribution of selection parameters ($\beta^+$, $\beta^-$, and weights) at each site.
*   An interactive table summarizing site-by-site results.

## Published Applications

*   **Host-Adaptation in Pathogens:** [Long, J. S., et al. (2019). Species specific differences in ANP32A, B and E determining influenza A virus polymerase activity. *eLife*, 8: e45066.](https://doi.org/10.7554/eLife.45066)

    This study investigated the host-specific adaptations of the Influenza A virus polymerase complex, focusing on its interaction with ANP32 proteins in birds versus mammals. The researchers used the MEME method to identify individual amino acid sites in the viral polymerase subunit (PB2) that are under episodic diversifying selection across host species. The analysis pinpointed adaptive changes required for host range transition, validating the molecular mechanism of influenza transmission between avian and mammalian species.

*   **SARS-CoV-2 Spike Evolution:** [MacLean, O. A., et al. (2021). Natural selection in the evolution of SARS-CoV-2 in coronavirus hosts. *PLoS Biology*, 19(3): e3001115.](https://doi.org/10.1371/journal.pbio.3001115)

    This study analyzed selection pressures acting on SARS-CoV-2 and related bat and pangolin sarbecoviruses. The MEME method was employed to identify codon sites in the Spike gene that experienced episodic positive selection during the virus's history. The findings revealed that while the early pandemic was characterized by relative evolutionary stability, episodic diversifying selection at specific Spike residues drove the virus's adaptation to host cell receptors and immune evasion.
