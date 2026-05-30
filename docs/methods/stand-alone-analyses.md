# Standard, Stand-alone, & Ecosystem Analyses

HyPhy is designed as a modular, extensible evolutionary analysis engine. While selection analyses are its most famous application, the platform supports a wide array of built-in CLI standard analyses, community batch files (`hyphy-analyses`), and direct integration with web platforms like Galaxy.

---

## 1. Built-in CLI Standard Analyses

When running HyPhy from the command line, you can execute a wide variety of standard analyses directly. Running `hyphy -i` launches an interactive prompt, or you can run any analysis headlessly by passing its command name (viewable via `hyphy --help`).

Below is an overview of the core built-in analyses:

| Command | Analysis Name | Description |
|:---|:---|:---|
| **busted** | BUSTED | Test for episodic gene-wide selection. |
| **busted-ph** | BUSTED-Phenotype | Test if episodic selection is associated with phenotype/foreground branches. |
| **absrel** | aBSREL | Test for lineage-specific episodic positive selection using an adaptive branch-site model. |
| **fel** | FEL | Identify individual sites subject to pervasive selection using a maximum likelihood approach. |
| **fubar** | FUBAR | High-power Bayesian method for detecting site-level pervasive selection on large alignments. |
| **meme** | MEME | Mixed Effects Model of Evolution to find site-level episodic and pervasive positive selection. |
| **slac** | SLAC | Counting-based site-level selection test using joint maximum likelihood ancestral reconstruction. |
| **relax** | RELAX | Test for selection relaxation or intensification along a designated set of branches. |
| **prime** | PRIME | Property-Informed Models of Evolution to test if selection preserves or alters amino acid properties. |
| **gard** | GARD | Heuristic search for recombination breakpoints and partitioned tree reconstruction. |
| **contrast-fel** | Contrast-FEL | Test for site-level differences in selective pressures between predefined clades. |
| **contrast-meme** | Contrast-MEME | Mixed-effects test for site-level selective differences between clades. |
| **bgm** | BGM | Apply Bayesian Graphical Models to detect coevolutionary interactions between codon positions. |
| **fmm** | FitMultiModel | Fit models permitting double or triple instantaneous nucleotide substitutions. |
| **fst** | F_ST | Compute population genetic differentiation measures with permutation testing. |
| **sm** | Slatkin-Maddison | Test for gene flow and estimate migration events across populations. |
| **leisr** | LEISR | Infer relative evolutionary rates on nucleotide/protein alignments (similar to Rate4Site). |
| **sw** / **spl** | Sliding Window / SimPlot | Map genetic similarity/distance along alignments using a sliding window. |
| **cln** | Clean Names | Sanitize sequence headers and replace stop codons with gaps. |
| **conv** | Convert Codons | Translate an in-frame codon multiple sequence alignment to proteins. |
| **label-tree** | Label Branches | Annotate branches in a Newick tree for downstream partition analyses. |

---

## 2. Galaxy Ecosystem Integration

The [Galaxy Project](https://galaxyproject.org/) is a web-based platform for accessible, reproducible, and transparent computational biomedical research. Galaxy is a primary partner in the HyPhy ecosystem, providing a user-friendly graphical interface for high-performance clusters without requiring command-line usage.

The Galaxy Intergalactic Utilities Commission (IUC) maintains official, robust wrapper XMLs for HyPhy tools under the [tools-iuc](https://github.com/galaxyproject/tools-iuc/tree/main/tools/hyphy) repository. The local equivalents are stored in `galaxy-tools/tools-iuc/tools/hyphy`.

### Supported Galaxy XML Wrappers:
*   **Selection Tests**: `hyphy_busted.xml`, `hyphy_absrel.xml`, `hyphy_fel.xml`, `hyphy_fubar.xml`, `hyphy_meme.xml`, `hyphy_slac.xml`
*   **Clade-Specific & Property Tests**: `hyphy_cfel.xml` (Contrast-FEL), `hyphy_prime.xml` (PRIME)
*   **Recombination & Relaxation**: `hyphy_gard.xml`, `hyphy_relax.xml`
*   **Utility & Networks**: `hyphy_bgm.xml` (Coevolution), `hyphy_cln.xml` (Data prep), `hyphy_conv.xml` (Translation)

By packaging parameter validations, automatic test suites (in `/test-data`), and detailed biological guidelines directly inside these wrappers, Galaxy enables seamless integration of HyPhy into multi-tool automated workflows.

---

## 3. Community Stand-alone Analyses (`hyphy-analyses`)

For advanced pipelines, custom models, and experimental methods, the HyPhy team maintains the [hyphy-analyses](https://github.com/veg/hyphy-analyses) repository. These analyses can be run locally using the HyPhy command-line engine by passing the path to their corresponding batch file.

### Selection & Modeling Extensions
*   **[BUSTED-PH](https://github.com/veg/hyphy-analyses/tree/master/BUSTED-PH)**: Test if episodic diversifying selection is associated with a specific phenotype/trait on foreground branches.
*   **[BUSTED-MH](https://github.com/veg/hyphy-analyses/tree/master/BUSTED-MH)**: BUSTED variant supporting multiple instantaneous nucleotide substitutions.
*   **[BUSTED-SR](https://github.com/veg/hyphy-analyses/tree/master/BUSTED-SR)**: BUSTED variant incorporating synonymous rate variation.
*   **[RELAX-joint](https://github.com/veg/hyphy-analyses/tree/master/RELAX-joint)**: Joint RELAX analysis across multiple gene alignments to boost statistical power.
*   **[RELAX-scan](https://github.com/veg/hyphy-analyses/tree/master/RELAX-scan)**: Perform sliding-window scans of selection relaxation along a gene.
*   **[MulticlassSynonymousSubstitutions](https://github.com/veg/hyphy-analyses/tree/master/MulticlassSynonymousSubstitutions)**: Model codon evolution with multiple distinct classes of synonymous codons.

### Model Fitting & Emulation
*   **[FitMG94](https://github.com/veg/hyphy-analyses/tree/master/FitMG94)**: Maximum likelihood fit of a standard Muse-Gaut 94 codon model.
*   **[FitMultiModel](https://github.com/veg/hyphy-analyses/tree/master/FitMultiModel)**: Fit and compare models with single, double, and triple instantaneous mutations.
*   **[PAML-emulator](https://github.com/veg/hyphy-analyses/tree/master/PAML-emulator)**: Emulate standard PAML models (such as M0, M1a, M2a, M7, M8) directly within the HyPhy framework.
*   **[NucleotideNonREV](https://github.com/veg/hyphy-analyses/tree/master/NucleotideNonREV)**: Fit non-reversible nucleotide models of sequence evolution.

### Simulation & Synthetic Data
*   **[SimulateMG94](https://github.com/veg/hyphy-analyses/tree/master/SimulateMG94)**: Simulate synthetic codon alignments along a tree under MG94 models.
*   **[SimulateProtein](https://github.com/veg/hyphy-analyses/tree/master/SimulateProtein)**: Simulate amino acid sequence evolution under standard matrices.

### Sequence Preparation & Utilities
*   **[codon-msa](https://github.com/veg/hyphy-analyses/tree/master/codon-msa)**: A helper workflow for generating codon-aware multiple sequence alignments.
*   **[LabelTrees](https://github.com/veg/hyphy-analyses/tree/master/LabelTrees)**: Automatically annotate phylogenetic trees for downstream branch-partition analyses.
*   **[clean-names](https://github.com/veg/hyphy-analyses/tree/master/clean-names)** / **[remove-duplicates](https://github.com/veg/hyphy-analyses/tree/master/remove-duplicates)**: Sanitization scripts to clean sequence headers and prune identical taxa from trees and alignments.
*   **[extract-partitions](https://github.com/veg/hyphy-analyses/tree/master/extract-partitions)**: Extract multi-partition alignments into individual files.