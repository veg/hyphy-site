# Viral selection preceding zoonoses

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> About This Paper</span>
    <span>Application</span>
  </div>
  <div class="about-dialog-title">Dynamics of natural selection preceding human viral epidemics and pandemics</div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Jennifer L. Havens, Sergei L. Kosakovsky Pond, Jordan D. Zehr, Joel O. Wertheim, Kristian G. Andersen, Michael Worobey, Joel O. Wertheim, etc.</div>
  <div class="about-dialog-meta"><strong>Reference:</strong> <em>Cell</em>, 2026. Volume 189, Pages 2762–2775. DOI: <a href="https://doi.org/10.1016/j.cell.2026.02.006" target="_blank">10.1016/j.cell.2026.02.006</a></div>
</div>

## Research Summary

Understanding the evolutionary changes that allow animal viruses to spill over into humans is a primary goal of pandemic preparedness. This study uses comparative phylogenetic selection analyses to examine the evolutionary dynamics of several major zoonotic viruses (including SARS-CoV, SARS-CoV-2, Ebola, and H1N1 influenza) before and after their emergence in humans.

By modeling selective pressures along the ancestral branches of animal reservoirs, spillover lineages, and human outbreak branches, the authors test whether viral adaptation in the animal host is a necessary precursor to spillover, and whether laboratory passage leaves distinct, detectable evolutionary footprints.


## Key Findings & Significance
*   **Adaptation in Reservoirs is Not Required**: Zoonotic spillover and human pandemics do not always require preceding adaptive mutations in the animal reservoir. For SARS-CoV-2, selection signatures remained stable in the animal host until its direct emergence in humans, indicating that the reservoir virus was already capable of human-to-human transmission.
*   **Signatures of Laboratory Passage**: Laboratory passaging and gain-of-function experiments (which select for replication in cell cultures or model organisms) leave distinct, statistically detectable evolutionary signatures of relaxed or intensified selection across viral genes.
*   **1977 H1N1 Origin**: The reemergence of the H1N1 influenza virus in 1977 was preceded by a period of evolution showing selective signatures highly consistent with laboratory passage, rather than natural reservoir circulation, resolving a long-standing historical debate.

## Role of HyPhy in the Analysis
The analysis relied on the **HyPhy** software package:
*   **RELAX**: Specifically used to detect whether selective constraints were relaxed or intensified on target lineages (such as spillover branches or laboratory-passaged sequences) relative to reference background lineages.
