# PRIME: Property-Informed Models

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> About This Paper</span>
    <span>Method</span>
  </div>
  <div class="about-dialog-title">Characterizing Physicochemical Selection in Protein Evolution with Property-Informed Models (PRIME)</div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Hannah Kim, Konrad Scheffler, Anton Nekrutenko, Darren P. Martin, Steven Weaver, Ben Murrell, Sergei L. Kosakovsky Pond</div>
  <div class="about-dialog-meta"><strong>Reference:</strong> <em>bioRxiv preprint</em>, 2026. DOI: <a href="https://doi.org/10.1101/2026.03.09.710461" target="_blank">10.1101/2026.03.09.710461</a></div>
</div>

## Method Summary

**PRIME** (Property-Informed Models of Evolution) is a framework of codon-level maximum likelihood methods that explicitly model amino acid exchangeability as a function of their physicochemical properties.

Standard codon substitution models represent selection using simple rate ratios ($dN/dS$ or $\omega$). While effective at identifying *where* and *when* selection occurs, these models are blind to the biophysical forces involved. For instance, standard models treat a mutation from Alanine to Valine (similar size/properties) identically to a mutation from Alanine to Arginine (large, charged).

PRIME solves this by parameterizing substitutions based on 5 core biophysical properties:
1.  **Molecular Volume**
2.  **Hydropathy**
3.  **Isoelectric Point (pI / Charge)**
4.  **Alpha-Helix Propensity**
5.  **Beta-Sheet Propensity**

PRIME operates across three distinct levels of evolutionary resolution:
*   **G-PRIME (Global)**: Models property constraints globally across the entire alignment and phylogeny.
*   **E-PRIME (Episodic)**: Identifies lineage-specific changes in property constraints.
*   **S-PRIME (Site-Level)**: Characterizes site-specific conservation or diversifying selection for specific properties.


## What It Does
*   **Resolves Biophysical Constraints**: Identifies which specific physical properties (e.g. volume or charge) are being conserved or diversified at individual sites.
*   **Categorizes Site-Level Selection**: S-PRIME groups sites into:
    *   **Property Conserved**: Sites where amino acids are highly constrained to preserve a specific property.
    *   **Property Neutral**: Sites evolving neutrally for that property.
    *   **Property Changing**: Sites undergoing adaptive shifts in that property.
*   **Connects Evolution to Machine Learning**: Demonstrates that PRIME selection weights align with the primary semantic axes of deep learning protein representations (like ESM-2) and agree with experimental deep mutational scanning (DMS) fitness landscapes.

## How to Use It in HyPhy
PRIME is implemented as a standard analysis template in HyPhy.

1.  **Prepare Input**: You need a coding sequence alignment and an associated phylogenetic tree.
2.  **Execute PRIME**:
    Run the analysis through the HyPhy command line:
    ```bash
    hyphy prime --alignment data.fas --tree tree.nwk
    ```
3.  **Choose Properties**: The interactive prompt will allow you to select which physicochemical properties to model, or you can run with the default set of five properties.
4.  **Visualize Results**: Output JSONs can be uploaded to **HyPhy Vision** to explore property constraints interactively via custom heatmaps.

## Key Findings & Significance
*   **Biophysical Realism**: Modeling physical properties significantly improves statistical model fit compared to standard $dN/dS$ models.
*   **Biophysical Selection Hierarchy**: Episodic analyses (E-PRIME) reveal that core packing and beta-sheet scaffolds are rigidly conserved, while alpha-helix propensity and surface electrostatics serve as the primary substrates for adaptive evolutionary tuning.
*   **High Sensitivity**: The power to detect site-level property selection (S-PRIME) is governed by informational depth. It achieves $>90\%$ sensitivity in data-rich alignments.
