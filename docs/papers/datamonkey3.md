# Datamonkey 3: Browser-native analysis

<div class="about-dialog">
  <div class="about-dialog-header">
    <span> About This Paper</span>
    <span>Method / Web Platform</span>
  </div>
  <div class="about-dialog-title">Datamonkey 3: Browser-native molecular evolution analysis</div>
  <div class="about-dialog-meta"><strong>Authors:</strong> Steven Weaver, Ben Murrell, Anton Nekrutenko, Sergei L. Kosakovsky Pond</div>
  <div class="about-dialog-meta"><strong>Reference:</strong> <em>Preprint</em>, 2026. Web server: <a href="https://v3.datamonkey.org" target="_blank">v3.datamonkey.org</a></div>
</div>

## Method Summary

**Datamonkey 3** is a browser-native, serverless implementation of the popular Datamonkey web platform for molecular evolutionary analysis. 

For two decades, the Datamonkey server (datamonkey.org) has provided public access to HyPhy selection analyses by running jobs on remote high-performance computing (HPC) clusters. However, this centralized model faces challenges: users must upload sequences and wait in queues, data sovereignty and privacy are compromised, and maintaining centralized servers is expensive.

Datamonkey 3 solves this by compiling the **HyPhy** C++ analysis engine into **WebAssembly (Wasm)**. The browser loads this Wasm module and executes selection analyses (such as MEME, BUSTED, or FEL) directly on the user's local CPU. No genomic data ever leaves the user's computer.


## What It Does
*   **Local Execution via Wasm**: Runs full HyPhy maximum likelihood and Bayesian analyses entirely client-side.
*   **Guarantees Data Sovereignty**: Ideal for clinical, proprietary, or privacy-sensitive sequence data, as files are processed locally and never uploaded to remote servers.
*   **Zero Queue Times**: Eliminates HPC queue latency; analyses start instantly.
*   **Interactive Curation & Validation**: Leverages local JS scripting to format, clean, and validate alignments, catching formatting errors before launching calculations.
*   **Data-Driven Run Estimation**: Employs statistical estimators to predict runtimes locally.

## How to Use It
Datamonkey 3 is open and serverless.

1.  **Open the Web App**:
    Go to **[v3.datamonkey.org](https://v3.datamonkey.org)** in any modern web browser.
2.  **Upload Data**:
    Drag-and-drop a codon sequence alignment (Fasta or Nexus format).
3.  **Configure Analysis**:
    Select your desired HyPhy method (e.g. MEME, BUSTED, FEL, or GARD) and options.
4.  **Run**:
    Click "Run Analysis." Your browser will run the WebAssembly engine, utilizing local CPU threads.
5.  **Visualize**:
    Once complete, the page immediately renders interactive results, which can also be exported as JSON files for visualization on [vision.hyphy.org](https://vision.hyphy.org).

## Key Findings & Significance
*   **Scalability**: Offloading compute to the client creates a sustainable model that scales infinitely with the user base, requiring zero server maintenance.
*   **Generalizable Bioinformatic Blueprint**: Demonstrates that complex, resource-heavy bioinformatic command-line engines can be safely and effectively deployed in serverless browser environments.
