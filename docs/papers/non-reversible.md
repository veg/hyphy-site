# Non-reversible nucleotide models

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> About This Paper</span>
    <span>Method / Application</span>
  </div>
  <div class="about-dialog-title">Viral genome sequence datasets display pervasive evidence of strand-specific substitution biases that are best described using non-reversible nucleotide substitution models</div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Rita Sianga-Mete, Penelope Hartnady, Wimbai Caroline Mandikumba, Kayleigh Rutherford, Christopher Brian Currin, Florence Phelanyane, Sabina Stefan, Steven Weaver, Sergei L. Kosakovsky Pond, Darren P. Martin</div>
  <div class="about-dialog-meta"><strong>Reference:</strong> <em>eLife</em>, 2023. DOI: <a href="https://doi.org/10.7554/eLife.87361" target="_blank">10.7554/eLife.87361</a></div>
</div>

## Method & Application Summary

The vast majority of molecular phylogenetic trees are inferred using **time-reversible** evolutionary models (like GTR). These models assume that the rate of nucleotide substitution from $A \to B$ is identical to $B \to A$ when weighted by nucleotide frequencies. 

However, there is no biochemical reason to assume that mutational processes are symmetrical, particularly in viral genomes. For single-stranded (ss) DNA and RNA viruses, the single strand is exposed to different mutational insults (such as cytidine deamination) than its complementary strand, creating significant **strand-specific mutational asymmetry**.

This study introduces two non-reversible nucleotide substitution models:
1.  **NREV6**: A 6-rate non-reversible model where complementary substitutions occur at identical rates (applicable to double-stranded genomes).
2.  **NREV12**: A 12-rate non-reversible model where all 12 substitution types are free to occur at different rates (applicable to single-stranded genomes).


## What It Does
*   **Captures Mutational Asymmetry**: Allows substitution rates to differ depending on the direction of mutation (e.g. $C \to T$ rate can differ from $T \to C$).
*   **Improves Tree Topology & Branch Lengths**: Accounts for strand-specific substitution bias, producing more accurate phylogenetic trees.
*   **Identifies Biochemical Mutational Biases**: Directly estimates asymmetrical rate parameters to reconstruct historical mutational footprints (such as host APOBEC deamination).

## How to Use It in HyPhy
Non-reversible models are implemented in HyPhy and can be selected for standard nucleotide alignments:

1.  **Prepare Input**: You need a nucleotide sequence alignment.
2.  **Run in HyPhy**:
    Define a custom non-reversible substitution rate matrix in HBL or call standard analysis scripts that support non-reversible model selection. In HyPhy:
    ```hbl
    // Example of defining NREV12 rate matrix in HBL
    NREV12RateMatrix = [
      [*, rAB, rAC, rAD]
      [rBA, *, rBC, rBD]
      [rCA, rCB, *, rCD]
      [rDA, rDB, rDC, *]
    ];
    ```
    Standard HyPhy model-fitting scripts will test non-reversible matrices against GTR to confirm if they improve model fit.

## Key Findings & Significance
*   **Strand Bias is Pervasive**: Evaluation of a broad benchmark of real-world viral datasets showed that **NREV12** provided a significantly better fit than standard reversible GTR models for single-stranded genomes.
*   **APOBEC Footprints**: Shows that asymmetrical models are critical to capture host-mediated editing (like APOBEC deamination in HIV/HBV or ADAR deamination in influenza), which strongly biases substitutions in a non-reversible fashion.
*   **Phylogenetic Correction**: Standard GTR models often suffer from systematic artifacts and branch length distortions when applied to asymmetric single-stranded datasets. NREV12 corrects these distortions.
