# CAPHEINE: Automated selection workflow

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> About This Paper</span>
    <span>Method / Workflow</span>
  </div>
  <div class="about-dialog-title">CAPHEINE, or everything and the kitchen sink: a workflow for automating selection analyses using HyPhy</div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Hannah Verdonk, Danielle Callan, Sergei L. Kosakovsky Pond</div>
  <div class="about-dialog-meta"><strong>Reference:</strong> <em>bioRxiv preprint</em>, 2026. DOI: <a href="https://doi.org/10.64898/2026.02.23.707482" target="_blank">10.64898/2026.02.23.707482</a></div>
</div>

## Method Summary

**CAPHEINE** (Codon Analysis Pipeline for High-throughput Evolutionary Inference and Null Evaluation) is a unified, high-performance bioinformatic pipeline designed to automate and standardize natural selection analyses using the **HyPhy** engine. 

While HyPhy provides a comprehensive toolkit for molecular evolutionary inference, executing multiple models on large datasets can be complicated. Issues like sequence cleaning, alignment artifacts, tree building, and consolidating JSON files often lead researchers to write custom, error-prone wrapper scripts. 

CAPHEINE automates this entire lifecycle, handling sequence validation, translation, alignment, tree reconstruction, running standard HyPhy analyses, and aggregating the final results into clean dashboards.


## What It Does
*   **Data Curation & Alignment**: Automates translation, codon-aware alignment (using tools like MAFFT or PRANK), and checks for frame shifts or premature stop codons.
*   **Phylogenetic Reconstruction**: Infers trees using FastTree or IQ-TREE.
*   **HyPhy Automation**: Automatically executes a standard suite of selection analyses:
    *   **MEME**: For site-level episodic selection.
    *   **Contrast-FEL**: For differential selection between branch groups.
    *   **RELAX**: For selection intensity shifts (relaxation vs. intensification).
*   **Artifact Protection ("Error Sink")**: Integrates mechanisms to identify and absorb alignment anomalies that could skew evolutionary inferences.

## How to Use It
CAPHEINE is developed using modern workflow managers (such as Nextflow) for cross-platform scalability.

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/veg/capheine.git
    cd capheine
    ```

2.  **Run with Docker/Conda**:
    Prepare a sample sheet pointing to your fasta sequences and run:
    ```bash
    nextflow run main.nf --input samplesheet.csv --profile docker
    ```
    This command downloads all necessary bioinformatic dependencies, builds the alignments and trees, runs the selection models in parallel, and generates a structured summary dashboard.

## Key Findings & Significance
*   **Reduces Analysis Bottlenecks**: Speeds up genome-wide evolutionary scans by distributing computations across local cores or cluster nodes.
*   **Robustness to Errors**: Incorporates automated quality-check filters that prevent the pipeline from failing on poorly aligned sequences or translation exceptions.
