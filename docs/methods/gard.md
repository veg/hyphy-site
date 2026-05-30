# GARD (Genetic Algorithm for Recombination Detection)

!!! question "What question does this method answer?"
    This tool screens an alignment of sequences for evidence of recombination in one or more sequences. It asks whether the entire alignment is adequately described by a single phylogenetic tree or if separate trees are preferred for different segments, indicating recombination breakpoints.

!!! info "Recommended Applications"

    * **Pre-processing for Selection Inference:** Because recombinant sequences cannot be adequately described with a single phylogenetic history, selection inference on recombinant data often leads to a significant increase in false positives. GARD is highly recommended to screen alignments and generate partitioned datasets for downstream selection methods (like FEL, FUBAR, SLAC, and MEME).

GARD (**G**enetic **A**lgorithm for **R**ecombination **D**etection) is a method to screen a multiple sequence alignment for the presence of recombination and is extremely useful as a *pre-processing step for selection inference*. 

Because recombinant sequences cannot be adequately described with a single phylogenetic history, selection inference on recombinant data often leads to a significant increase in false positives. GARD alleviates this concern by comprehensively screening an alignment for recombination breakpoints and inferring a unique phylogenetic history for each detected recombination block.

### Recombination & Selection
If GARD detects recombination in your dataset, it will provide you with an updated *partitioned* dataset, where each partition corresponds to a recombination block with its own corresponding phylogeny. This partitioned dataset can then be used as input (instead of your original data) for downstream selection inference methods.

Downstream methods that natively accept and process partitioned datasets from GARD include:
* [FEL](fel.md)
* [FUBAR](fubar.md)
* [SLAC](slac.md)
* [MEME](meme.md)

---

### Citation
If you use GARD in your analysis, please cite the following:
> Kosakovsky Pond, SL et al. ["Automated Phylogenetic Detection of Recombination Using a Genetic Algorithm."](https://doi.org/10.1093/molbev/msl051) *Mol. Biol. Evol.* 23, 1891–1901 (2006).
