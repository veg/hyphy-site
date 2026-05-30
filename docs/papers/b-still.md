# B-STILL: Evolutionary stasis constraints

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> About This Paper</span>
    <span>Method</span>
  </div>
  <div class="about-dialog-title">Beyond Invariable Sites: Using Evolutionary Stasis to Map Multi-Layered Constraints on the Evolution of Viral and Mammalian Genomes</div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Sergei L. Kosakovsky Pond, Hannah Verdonk, Steven Weaver, Gallean Brown, Danielle Callan, Anton Nekrutenko, Darren P. Martin</div>
  <div class="about-dialog-meta"><strong>Reference:</strong> <em>Preprint</em>, 2026. DOI: <a href="https://doi.org/10.1101/2026.04.09.717527" target="_blank">10.1101/2026.04.09.717527</a></div>
</div>

## Method Summary

**B-STILL** (Bayesian Significance Test of Invariant Low Likelihoods) is a hierarchical Bayesian framework designed to map extreme purifying selection at **invariant (unchanging)** sites in protein-coding genomes.

Standard phylogenetic tools rely on amino acid and nucleotide variation to estimate evolutionary rates. Consequently, whenever a site is completely invariant across an alignment, these tools face a resolution gap. They cannot distinguish between:
1.  **Stochastic Stasis**: The site has not mutated simply due to chance or low divergence.
2.  **Functional Constraint**: The site is biologically incapable of tolerating mutations.

B-STILL solves this by estimating a site-specific "stasis radius" and calibrating it against the gene's overall evolutionary rate and tree-level mutational opportunities. It identifies statistically anomalous invariant sites, labeling them as **Evolutionary Stasis Anchors (ESAs)**.


## What It Does
*   **Identifies Stasis Anchors**: Maps sites where mutations are actively suppressed, revealing deep purifying selection.
*   **Tackles Invariant Resolution Gap**: Computes the probability that a site's invariance is driven by biological constraint rather than a lack of evolutionary time.
*   **Scalable to Large Alignments**: Operates efficiently on coding alignments containing thousands of sequences, making it suitable for modern genomic datasets.

## How to Use It in HyPhy
B-STILL is implemented in HyPhy and can be executed via HBL scripts:

1.  **Prepare Input**: You need a coding sequence alignment and a corresponding phylogenetic tree.
2.  **Run the Analysis**:
    Execute the B-STILL script in HyPhy:
    ```bash
    hyphy bstill --alignment data.fas --tree tree.nwk
    ```
3.  **Analyze Outputs**: The output JSON provides site-specific Bayes factors and probabilities. Sites with high significance support are flagged as Evolutionary Stasis Anchors (ESAs).

## Key Findings & Significance
*   **Biological Fitness Predictor**: Validation against clinical databases and pathogen experimental datasets confirms that ESAs are strong predictors of viral fitness and clinical disease potential.
*   **Footprints Protein Domains**: Automatically maps and footprints functional protein domains and currently uncharacterized structural motifs in mammalian and viral genomes.
*   **Transforms Formerly Ignored Data**: Salvages invariant sites—traditionally discarded or treated as background noise in phylogenetic trees—into useful markers of extreme purifying selection.
