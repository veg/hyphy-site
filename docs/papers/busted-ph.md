# BUSTED-PH: Phenotype-associated selection

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> About This Paper</span>
    <span>Method</span>
  </div>
  <div class="about-dialog-title">BUSTED-PH: Isolating the genomic signatures of convergent phenotypes</div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Avery Selberg, Nathan Clark, Anton Nekrutenko, Maria Chikina, Sergei L. Kosakovsky Pond</div>
  <div class="about-dialog-meta"><strong>Reference:</strong> <em>bioRxiv preprint</em>, 2026. DOI: <a href="https://doi.org/10.1101/2026.01.29.702612" target="_blank">10.1101/2026.01.29.702612</a></div>
</div>

## Method Summary

**BUSTED-PH** (Branch-site Unrestricted Statistical Test for Episodic Diversification – Phenotype) is a codon-substitution model designed to identify positive selection associated with specific convergent traits. 

Convergent evolution—such as the independent emergence of echolocation in bats and dolphins, or gigantism in whales and elephants—offers a natural test for genetic adaptation. However, identifying which genes underlie these phenotypes is challenging because current methods are either too strict (demanding identical mutations) or suffer from high false-positive rates driven by background adaptation. 

BUSTED-PH solves this by partitioning the phylogeny into **phenotype-positive (foreground)** and **phenotype-negative (background)** branches, and running a likelihood ratio test to determine if the foreground branches experience distinct episodic diversifying selection relative to the background.


## What It Does
*   **Contrasts Selection Regimes**: Explicitly compares $\omega$ ($dN/dS$) distributions between phenotype-positive foreground branches and background branches.
*   **Filters Out Background Noise**: Disentangles general evolutionary rate changes from phenotype-specific adaptations, preventing false positives from genes that are highly variable across all lineages.
*   **Identifies Episodic Selection**: Can detect selection even if it only affects a subset of sites along a subset of foreground branches.

## How to Use It in HyPhy
BUSTED-PH is fully integrated into the standard **HyPhy** BUSTED template.

1.  **Prepare Input**: You need a codon alignment and a phylogenetic tree where branches corresponding to the phenotype of interest are labeled (e.g., labeled with `{Foreground}`).
2.  **Execute the Analysis**:
    Run BUSTED-PH via the HyPhy command line:
    ```bash
    hyphy busted --alignment data.fas --tree tree.nwk --branches Foreground
    ```
3.  **Interpret Results**: HyPhy compares a model where foreground branches are allowed to undergo selection against a null model where they are constrained to background-like parameters. A significant p-value ($p < 0.05$) indicates phenotype-associated positive selection.

## Key Findings & Significance
*   **Echolocation Scan**: Applied BUSTED-PH to a dataset of 120 mammals. Identified 72 genes associated with echolocation. Recovered classic auditory genes (*Prestin*, *TMC1*) and discovered novel candidates in lipid homeostasis and neural development.
*   **Mammalian Gigantism**: Identified 91 genes associated with gigantism, involved in skeletal reinforcement, organ size regulation, and genomic integrity (necessary to avoid cancer at large body sizes).
*   **Strict Control**: Demonstrated high statistical power and tight false-positive control under both simulated and empirical conditions.
