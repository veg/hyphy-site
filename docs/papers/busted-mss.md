# BUSTED+MSS: Synonymous rate corrections

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> About This Paper</span>
    <span>Method</span>
  </div>
  <div class="about-dialog-title">Correcting for Global Synonymous Selection Improves the Accuracy of Episodic Positive Selection Inference</div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Hannah Verdonk, Alyssa Pivirotto, Jody Hey, Sergei L. Kosakovsky Pond</div>
  <div class="about-dialog-meta"><strong>Reference:</strong> <em>Preprint</em>, 2026.</div>
</div>

## Method Summary

Standard codon-based tests for natural selection, including **BUSTED**, operate on the assumption that synonymous substitutions (mutations that do not alter the amino acid) are selectively neutral and occur at a uniform background rate ($dS$). 

This assumption is increasingly challenged by evidence of purifying selection acting on synonymous sites to optimize translation efficiency, preserve mRNA secondary structure, or control folding kinetics. When models fail to account for this synonymous selection, the background rate ($dS$) is underestimated, inflating the $dN/dS$ ($\omega$) ratio and leading to **false positive inferences of positive selection**.

This paper introduces **BUSTED+S+MSS**, which incorporates Multiclass Synonymous Substitution (MSS) models into the BUSTED framework. It partitions synonymous rates into multiple empirically derived classes, correcting for global synonymous selection constraints.


## What It Does
*   **Models Synonymous Variation**: Replaces the single background $dS$ rate with a multiclass distribution, capturing site-to-site variation in synonymous selection.
*   **Reduces False Positives**: Minimizes spurious positive selection signals caused by unmodeled purifying selection on synonymous sites.
*   **Integrates an "Error Sink"**: Combines synonymous rate classes with an error-sink parameter to absorb alignment artifacts, preventing them from biasing biological selection tests.

## How to Use It in HyPhy
The MSS synonymous selection correction is fully integrated into the standard HyPhy BUSTED package.

1.  **Prepare Input**: You need a coding sequence alignment and phylogenetic tree.
2.  **Execute the Analysis**:
    Select the synonymous rate variation option when running BUSTED via the CLI:
    ```bash
    hyphy busted --alignment data.fas --tree tree.nwk --syn-rate-classes 3
    ```
    Specifying `--syn-rate-classes 3` enables the Multiclass Synonymous Substitution (MSS) model, splitting synonymous rates into three distinct categories.

## Key Findings & Significance
*   **Empirical Validation**: Applied to datasets across five diverse clades—Drosophila, Caenorhabditis, Enterobacteria, Saccharomyces, and Primates. The inclusion of MSS consistently improved model fit.
*   **Fewer False Positives**: MSS corrections reduced the number of genes falsely inferred to be under positive selection, particularly in highly divergent alignments.
*   **Dual Correction**: Information-theoretic analyses show that while site-specific synonymous rate variation (SRV) provides the primary correction, global synonymous rate variation (MSS) acts as a crucial second-order correction.
