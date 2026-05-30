# AOC: Snakemake selection workflow

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> About This Paper</span>
    <span>Method / Workflow</span>
  </div>
  <div class="about-dialog-title">AOC: A Snakemake workflow for the characterization of natural selection in protein-coding genes</div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Alexander G. Lucaci, Sergei L. Kosakovsky Pond</div>
  <div class="about-dialog-meta"><strong>Reference:</strong> <em>Journal of Open Source Software (JOSS)</em>, 2026. DOI: <a href="https://doi.org/10.21105/joss.09872" target="_blank">10.21105/joss.09872</a></div>
</div>

## Method Summary

The **Analysis of Orthologous Collections (AOC)** is an automated Snakemake workflow that streamlines the process of detecting natural selection in large sets of protein-coding genes. Traditionally, running phylogenetic selection tests requires multiple manual steps: sequence quality control, codon alignment, phylogenetic tree reconstruction, and formatting input files for statistical inference engines. 

AOC coordinates all of these steps into a single, reproducible pipeline. It integrates standard bioinformatic tools (such as MAFFT for alignment and FastTree for phylogenies) and automates the execution of multiple advanced evolutionary models in **HyPhy**. Finally, it compiles these results into interactive html reports.


## What It Does
*   **Automates Data Prep**: Handles quality control, cleans stop codons, performs codon-aware alignment, and infers tree topologies.
*   **Runs HyPhy Analyses**: Automatically executes:
    *   **BUSTED**: To test for gene-wide positive selection.
    *   **MEME**: To find individual sites subject to episodic diversifying selection.
    *   **FUBAR**: To identify sites under pervasive positive or negative purifying selection.
    *   **RELAX**: To detect relaxation or intensification of selection pressure.
*   **Generates Visualizations**: Creates interactive, web-based visual summaries of site-level and lineage-level selection, linking results to functional or structural hypotheses.

## How to Use It
AOC is run as a Snakemake workflow, meaning it scales from a local laptop to high-performance computing clusters:

1.  **Install AOC**:
    Clone the repository and install dependencies using Conda:
    ```bash
    git clone https://github.com/veg/AOC.git
    cd AOC
    conda env create -f environment.yml
    conda activate aoc
    ```

2.  **Configure input data**:
    Place your unaligned orthologous fasta files into a designated input folder and specify them in the config file `config.yaml`.

3.  **Run the pipeline**:
    ```bash
    snakemake --cores 8
    ```
    This command will automatically run alignments, trees, and all HyPhy models in parallel, outputting final reports into the `results/` folder.

## Key Findings & Significance
*   **Closes the Research Gap**: Automating these complex analyses makes it easier for domain biologists to investigate underexplored genes rather than focusing solely on a few highly-studied biomedical targets.
*   **Standardizes Selection Inference**: Eliminates custom script errors and manual file conversions, ensuring high reproducibility in evolutionary studies.
