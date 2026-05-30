# Publications & Manuscripts

This page lists recent papers on new HyPhy methods and research groups, compiling the latest methodological developments, software workflows, and biological applications. Each publication is presented with its summary, implementation details, key findings, and references.

---

## Evolutionary Methods & Workflows

These papers introduce novel statistical models, hierarchical Bayesian frameworks, and workflow automations integrated into the HyPhy ecosystem.

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> Method / Web Platform</span>
    <span>v3.datamonkey.org</span>
  </div>
  <div class="about-dialog-title"><a href="datamonkey3/">Datamonkey 3: Browser-native molecular evolution analysis</a></div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Steven Weaver, Ben Murrell, Anton Nekrutenko, Sergei L. Kosakovsky Pond</div>
  <div style="margin-top: 10px; display: flex; gap: 15px; align-items: flex-start;">
    <img src="../images/papers/Datamonkey_3-2_preview.png" width="100" style="border: 1px solid #000000; box-shadow: 1px 1px 0px #000000;" alt="" />
    <p style="font-size: 11px; margin-bottom: 0;">Compiles the HyPhy analysis engine to WebAssembly to run selection and recombination tests serverlessly in the user's browser, preserving data privacy and bypassing server queues.</p>
  </div>
</div>

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> Method / Model</span>
    <span>PRIME Selection</span>
  </div>
  <div class="about-dialog-title"><a href="prime/">Characterizing Physicochemical Selection in Protein Evolution with Property-Informed Models (PRIME)</a></div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Hannah Kim, Konrad Scheffler, Anton Nekrutenko, Darren P. Martin, Steven Weaver, Ben Murrell, Sergei L. Kosakovsky Pond</div>
  <div style="margin-top: 10px; display: flex; gap: 15px; align-items: flex-start;">
    <img src="../images/papers/2026.03.09.710461v1.full_preview.png" width="100" style="border: 1px solid #000000; box-shadow: 1px 1px 0px #000000;" alt="" />
    <p style="font-size: 11px; margin-bottom: 0;">Integrates biophysical properties (volume, charge, hydrophobicity) into codon substitution models (G-PRIME, E-PRIME, and S-PRIME) to resolve the physical basis of evolutionary constraints.</p>
  </div>
</div>

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> Method / Model</span>
    <span>BUSTED-PH Phenotypes</span>
  </div>
  <div class="about-dialog-title"><a href="busted-ph/">BUSTED-PH: Isolating the genomic signatures of convergent phenotypes</a></div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Avery Selberg, Nathan Clark, Anton Nekrutenko, Maria Chikina, Sergei L. Kosakovsky Pond</div>
  <div style="margin-top: 10px; display: flex; gap: 15px; align-items: flex-start;">
    <img src="../images/papers/2026.01.29.702612v1.full_preview.png" width="100" style="border: 1px solid #000000; box-shadow: 1px 1px 0px #000000;" alt="" />
    <p style="font-size: 11px; margin-bottom: 0;">Introduces a branch-site codon test to identify phenotype-associated episodic diversifying selection, contrasting foreground (phenotype-positive) against background lineages.</p>
  </div>
</div>

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> Method / Model</span>
    <span>B-STILL Stasis</span>
  </div>
  <div class="about-dialog-title"><a href="b-still/">Beyond Invariable Sites: Using Evolutionary Stasis to Map Multi-Layered Constraints on the Evolution of Viral and Mammalian Genomes</a></div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Sergei L. Kosakovsky Pond, Hannah Verdonk, Steven Weaver, Gallean Brown, Danielle Callan, Anton Nekrutenko, Darren P. Martin</div>
  <div style="margin-top: 10px; display: flex; gap: 15px; align-items: flex-start;">
    <img src="../images/papers/2026.04.09.717527v1.full_preview.png" width="100" style="border: 1px solid #000000; box-shadow: 1px 1px 0px #000000;" alt="" />
    <p style="font-size: 11px; margin-bottom: 0;">A hierarchical Bayesian framework (B-STILL) that analyzes invariant sites to distinguish stochastic stasis from extreme purifying selection, mapping Evolutionary Stasis Anchors (ESAs).</p>
  </div>
</div>

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> Method / Model</span>
    <span>BUSTED+MSS Synonymous Correction</span>
  </div>
  <div class="about-dialog-title"><a href="busted-mss/">Correcting for Global Synonymous Selection Improves the Accuracy of Episodic Positive Selection Inference</a></div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Hannah Verdonk, Alyssa Pivirotto, Jody Hey, Sergei L. Kosakovsky Pond</div>
  <div style="margin-top: 10px; display: flex; gap: 15px; align-items: flex-start;">
    <img src="../images/papers/BUSTED_MSS_preview.png" width="100" style="border: 1px solid #000000; box-shadow: 1px 1px 0px #000000;" alt="" />
    <p style="font-size: 11px; margin-bottom: 0;">Corrects BUSTED for global purifying selection acting on synonymous sites (Multiclass Synonymous Substitution, MSS) to prevent false positives in positive selection inference.</p>
  </div>
</div>

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> Method / Workflow</span>
    <span>CAPHEINE Automation</span>
  </div>
  <div class="about-dialog-title"><a href="capheine/">CAPHEINE, or everything and the kitchen sink: a workflow for automating selection analyses using HyPhy</a></div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Hannah Verdonk, Danielle Callan, Sergei L. Kosakovsky Pond</div>
  <div style="margin-top: 10px; display: flex; gap: 15px; align-items: flex-start;">
    <img src="../images/papers/2026.02.23.707482v3.full-2_preview.png" width="100" style="border: 1px solid #000000; box-shadow: 1px 1px 0px #000000;" alt="" />
    <p style="font-size: 11px; margin-bottom: 0;">An automated, scalable pipeline that streamlines sequence curation, codon alignment, tree building, and the execution of multiple selection analyses in HyPhy.</p>
  </div>
</div>

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> Method / Workflow</span>
    <span>AOC Workflow</span>
  </div>
  <div class="about-dialog-title"><a href="aoc/">AOC: A Snakemake workflow for the characterization of natural selection in protein-coding genes</a></div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Alexander G. Lucaci, Sergei L. Kosakovsky Pond</div>
  <div style="margin-top: 10px; display: flex; gap: 15px; align-items: flex-start;">
    <img src="../images/papers/10.21105.joss.09872_preview.png" width="100" style="border: 1px solid #000000; box-shadow: 1px 1px 0px #000000;" alt="" />
    <p style="font-size: 11px; margin-bottom: 0;">A Snakemake-based workflow automating data preparation and multi-model HyPhy runs, compiling results into interactive HTML dashboards for research sharing.</p>
  </div>
</div>

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> Method / Substitution Models</span>
    <span>Non-Reversible Matrix</span>
  </div>
  <div class="about-dialog-title"><a href="non-reversible/">Viral genome sequence datasets display pervasive evidence of strand-specific substitution biases...</a></div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Rita Sianga-Mete, Penelope Hartnady, Wimbai Caroline Mandikumba, Kayleigh Rutherford, Christopher Brian Currin, Florence Phelanyane, Sabina Stefan, Steven Weaver, Sergei L. Kosakovsky Pond, Darren P. Martin</div>
  <div style="margin-top: 10px; display: flex; gap: 15px; align-items: flex-start;">
    <img src="../images/papers/elife-87361-v1_preview.png" width="100" style="border: 1px solid #000000; box-shadow: 1px 1px 0px #000000;" alt="" />
    <p style="font-size: 11px; margin-bottom: 0;">Introduces non-reversible models NREV6 and NREV12 to represent strand-specific mutational asymmetry, demonstrating substantial improvements in viral phylogenetic trees.</p>
  </div>
</div>

---

## Biological Applications

These studies utilize HyPhy evolutionary methodologies to resolve specific biological questions in virology and genomics.

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> Application / Virology</span>
    <span>Epidemics & Pandemics</span>
  </div>
  <div class="about-dialog-title"><a href="viral-selection/">Dynamics of natural selection preceding human viral epidemics and pandemics</a></div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Jennifer L. Havens, Sergei L. Kosakovsky Pond, Jordan D. Zehr, Joel O. Wertheim, Kristian G. Andersen, Michael Worobey, Joel O. Wertheim, etc.</div>
  <div style="margin-top: 10px; display: flex; gap: 15px; align-items: flex-start;">
    <img src="../images/papers/PIIS0092867426001716-2_preview.png" width="100" style="border: 1px solid #000000; box-shadow: 1px 1px 0px #000000;" alt="" />
    <p style="font-size: 11px; margin-bottom: 0;">Cell study utilizing HyPhy's RELAX, aBSREL, and MEME models to demonstrate that viral adaptation in host reservoirs is not a prerequisite for epidemics, while identifying clear evolutionary signatures of lab passage.</p>
  </div>
</div>

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> Application / Genomics</span>
    <span>Human Y Chromosome</span>
  </div>
  <div class="about-dialog-title"><a href="human-y/">How and why ampliconic genes survive on the human Y chromosome</a></div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Karol Pal, Aleksandra Greshnova, Sukhwan Park, Byung June Ko, Hana Palova, Martin Steinegger, Sergei L. Kosakovsky Pond, Stefan Canzar, Kateryna D. Makova</div>
  <div style="margin-top: 10px; display: flex; gap: 15px; align-items: flex-start;">
    <img src="../images/papers/2024.04.02.587783v2.full_preview.png" width="100" style="border: 1px solid #000000; box-shadow: 1px 1px 0px #000000;" alt="" />
    <p style="font-size: 11px; margin-bottom: 0;">Uses HyPhy purifying selection tests to explore the survival of multicopy ampliconic fertility genes on the non-recombining human Y chromosome, highlighting gene conversion repair mechanisms.</p>
  </div>
</div>
