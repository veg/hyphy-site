# News and Releases

The HyPhy project actively updates and maintains the software package, releasing new features, performance improvements, and bug fixes on GitHub.

To view the absolute latest real-time release logs, source code, and pre-compiled binaries, please visit the official GitHub Releases page:

!!! tip "View Latest Releases on GitHub"
    **[HyPhy GitHub Releases (https://github.com/veg/hyphy/releases)](https://github.com/veg/hyphy/releases)**

---

<!-- START_LATEST_RELEASE -->
## <img src="images/logo.png" width="16" height="16" style="vertical-align: middle; margin-right: 6px;" alt="" /> Latest Release: v2.5.100 (2.5.100)

# HyPhy Version Update: 2.5.100

This release introduces major performance optimizations to HyPhy's hybrid optimization engine, modernizes several core analysis scripts to `libv3` standards, and implements a generic interface for tuning dynamic passes.

## Core Optimization Enhancements

### 1. Refined Coordinate Descent & Line Search
- **Adaptive Precision & Dampening:** Brent 1D line search precision has been relaxed to `1e-4` in early passes, dramatically speeding up initial convergence.
- **Pass Direction Tuning:** Optimized the first coordinate descent pass to run in direct order, improving early parameter search.
- **Tolerances & Bracketing:** Restored correct Brent search tolerances and refined momentum-aware search bracketing.

### 2. Intelligent Parameter Blocking & CG Logic
- **Full-Pass Accounting:** Dynamically blocked Simplex and Conjugate Gradient searches now register as complete optimization passes immediately upon execution, ensuring correct convergence tracking.
- **Skip Heuristics:** Implemented advanced CG-skip heuristics for BUSTED, avoiding redundant, computationally expensive gradient computations.
- **Unchanged Variable Exclusion:** The coordinate descent loop now tracks and skips variables that did not change in the previous sweep.

### 3. Contribution-Aware Coordinate Heuristics
- **90% Contribution Threshold:** Enforced a contribution threshold check where the subset of variables identified for "large-change-only" optimization must account for at least 90% of the cumulative parameter movement. This prevents entering unproductive large-change-only optimization cycles when changes are minor or highly distributed.

## Generic Tuning Settings

### 1. Flexible Optimization Flags
- **Generic Simplex Control:** Introduced `FORCE_DYNAMIC_SIMPLEX` as a generic environment and likelihood option variable in the C++ optimization backend. This replaces the hardcoded code checks (previously tied directly to `_Genetic_Code_ID` matching `"mtDNA"`), allowing scripts to generically force dynamic passes to only run SimplexMethod rather than ConjugateGradientDescent.

## Analysis Script Modernization

### 1. libv3 Migration
- **Standardized Scripts:** Modernized several long-standing analysis templates to `libv3` standards:
  - `AnalyzeDiNucData.bf`
  - `AnalyzeNucDataFreq.bf`
  - `AnalyzeNucProtData.bf`
- **TwoSequenceTest.bf:** Cleaned and aligned `TwoSequenceTest.bf` to standard APIs.
- **Non-Interactive Keyword Arguments:** Refactored standard codon models, `defineGamma.mdl`, and `defineHM.mdl` to support non-interactive HBL execution via `KeywordArguments`.

### 2. Model & Diagnostics
- **Yokoyama Analysis Report:** Created a Yokoyama codon model analysis report with comparative charts and custom GTR HMM rate variation.

## System & Infrastructure
- **CI Release Automation:** Added a GitHub Action workflow to automatically notify `hyphy-site` of release tags.
- **Documentation:** Created comprehensive codon models help guides and cleaned LaTeX formatting from markdown documents.


For full details, visit the [GitHub Release Page](https://github.com/veg/hyphy/releases/tag/2.5.100).

---
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
