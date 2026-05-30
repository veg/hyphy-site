# News and Releases

The HyPhy project actively updates and maintains the software package, releasing new features, performance improvements, and bug fixes on GitHub.

To view the absolute latest real-time release logs, source code, and pre-compiled binaries, please visit the official GitHub Releases page:

!!! tip "View Latest Releases on GitHub"
    **[HyPhy GitHub Releases (https://github.com/veg/hyphy/releases)](https://github.com/veg/hyphy/releases)**

---

<!-- START_LATEST_RELEASE -->
<!-- END_LATEST_RELEASE -->

## <img src="images/logo.png" width="16" height="16" style="vertical-align: middle; margin-right: 6px;" alt="" /> Major Version Highlights

### HyPhy v2.5.x (Active Release Series)
The v2.5 series of HyPhy represents the current stable release sequence, introducing major performance upgrades, optimized MPI scaling, and deep integration with **Datamonkey** and **HyPhy Vision**.

Key features in this series include:
* **Standard JSON Formats**: Uniform, structured, and descriptive machine-readable JSON result outputs.
* **Analysis Speedups**: Optimizations to MEME, FEL, BUSTED, and aBSREL, significantly reducing execution times.
* **Conda & Homebrew Integration**: Fast package management installs via Bioconda (`conda install -c bioconda hyphy`) or Homebrew (`brew install hyphy`).
* **PRIME Integration**: Selection-model variants (G-PRIME, E-PRIME, and S-PRIME) mapping biophysical property constraints.

### HyPhy v2.3 / v2.4 (Legacy Series)
* Introduced episodic selection testing at individual sites (MEME).
* Improved branch selection methods and added Likelihood Ratio Tests.
* Established foundation for JSON-based results parsing.

---

## <img src="images/logo.png" width="16" height="16" style="vertical-align: middle; margin-right: 6px;" alt="" /> Recent Publications & Preprints

Keep up to date with the latest methodological developments, applications, and workflows built around the HyPhy platform. Click on any title to read the detailed summary, method capabilities, key findings, and representative figures:

### Methods & Workflows
*   **[Datamonkey 3 (2026)](papers/datamonkey3/)**: "Datamonkey 3: Browser-native molecular evolution analysis" &mdash; Compiles the HyPhy analysis engine to WebAssembly to run selection analyses entirely serverless in your local browser.
*   **[PRIME Selection (2026)](papers/prime/)**: "Characterizing Physicochemical Selection in Protein Evolution with Property-Informed Models (PRIME)" &mdash; Parametric selection models incorporating physical property changes (volume, charge, hydrophobicity).
*   **[BUSTED-PH Phenotypes (2026)](papers/busted-ph/)**: "BUSTED-PH: Isolating the genomic signatures of convergent phenotypes" &mdash; A branch-site model comparing phenotype-positive foreground lineages with background noise to isolate adaptive convergence.
*   **[B-STILL Stasis (2026)](papers/b-still/)**: "Beyond Invariable Sites: Using Evolutionary Stasis to Map Multi-Layered Constraints on the Evolution of Viral and Mammalian Genomes" &mdash; A Bayesian framework resolving stasis constraints at invariant genome sites.
*   **[BUSTED+MSS Synonymous Correction (2026)](papers/busted-mss/)**: "Correcting for Global Synonymous Selection Improves the Accuracy of Episodic Positive Selection Inference" &mdash; Accounts for global synonymous constraints to minimize positive selection false positives.
*   **[CAPHEINE Workflow (2026)](papers/capheine/)**: "CAPHEINE, or everything and the kitchen sink: a workflow for automating selection analyses using HyPhy" &mdash; A reproducible high-throughput selection analysis pipeline.
*   **[AOC Snakemake (2026)](papers/aoc/)**: "AOC: A Snakemake workflow for the characterization of natural selection in protein-coding genes" &mdash; Standardized pipeline from raw homologous sequences to interactive reports.
*   **[Non-Reversible Models (eLife, 2023)](papers/non-reversible/)**: "Viral genome sequence datasets display pervasive evidence of strand-specific substitution biases that are best described using non-reversible nucleotide substitution models" &mdash; Symmetrical-violating evolutionary models for asymmetric single-stranded genomes.

### Biological & Educational Applications
*   **[Zoonotic Outbreaks (Cell, 2026)](papers/viral-selection/)**: "Dynamics of natural selection preceding human viral epidemics and pandemics" &mdash; Evolutionary analysis of reservoir spillover and detection of laboratory selection signatures.
*   **[Human Y Chromosome (2026)](papers/human-y/)**: "How and why ampliconic genes survive on the human Y chromosome" &mdash; Dynamic copy number maintenance and purifying selection on ampliconic fertility genes.

---

## <img src="images/logo.png" width="16" height="16" style="vertical-align: middle; margin-right: 6px;" alt="" /> How to Install the Latest Version

For most environments (Linux, macOS), we recommend installing the latest version via package managers to automatically handle dependencies:

### macOS (via Homebrew)
```bash
brew install hyphy
```

### Linux / macOS (via Conda)
```bash
conda install -c bioconda hyphy
```

### Build from Source
If you are compiling on high-performance clusters (with MPI or OpenMP support), please fetch the latest source code from GitHub:
```bash
git clone https://github.com/veg/hyphy.git
cd hyphy
cmake .
make -j
```
