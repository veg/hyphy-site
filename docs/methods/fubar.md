# FUBAR (Fast, Unconstrained Bayesian AppRoximation)

!!! question "What question does this method answer?"
    Which site(s) in a gene are subject to pervasive (consistently across the entire phylogeny) diversifying selection?

!!! info "Recommended Applications"

    * **Pervasive Selection / Pathogen Evolution:** Ideally suited to identify sites under positive selection representing candidate sites subject to strong selective pressures across the entire phylogeny, such as adaptive immune escape by viruses.
    * **Large Datasets:** FUBAR is the recommended method for detecting pervasive selection at individual sites on large datasets (> 500 sequences) for which other methods (like FEL) have prohibitive runtimes.

FUBAR (**F**ast, **U**nconstrained **B**ayesian **A**pp**R**oximation) uses a Bayesian approach to infer nonsynoymous ($dN$) and synonymous ($dS$) substitution rates on a per-site basis for a given coding alignment and corresponding phylogeny. This method assumes that the selection pressure for each site is constant along the entire phylogeny.

### Key Differences from FEL
Although FUBAR produces similar information to [FEL](fel.md), it has several key differences:

* **Posterior Probabilities**: FUBAR employs a Bayesian algorithm to infer rates, and therefore it reports evidence for positive selection using *posterior probabilities* (which range from 0 to 1), rather than p-values. Generally, posterior probabilities $\geq 0.9$ are strongly suggestive of positive selection. 
* **High Performance**: FUBAR runs extremely quickly and is well-suited for analyzing large alignments with hundreds or thousands of sequences. This speed-up results from the novel strategy of employing a pre-specified discrete grid of $dN$ and $dS$ values to be applied across sites. This approach contrasts with the time-consuming FEL strategy of fitting a new MG94xREV model at each site.
* **Higher Power**: FUBAR may have more power than FEL, in particular when positive selection is present but relatively weak (i.e., low values of $\omega > 1$).

---

### Citation
If you use FUBAR in your analysis, please cite the following:
> Murrell, B et al. ["FUBAR: A Fast, Unconstrained Bayesian AppRoximation for inferring selection."](https://doi.org/10.1093/molbev/mst030) *Mol. Biol. Evol.* 30, 1196–1205 (2013).
