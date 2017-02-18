Using HyPhy to detect selection.
=================================


These tutorials outline how to prepare data and execute analyses in HyPhy's suite of methods for detecting natural selection in protein-coding alignments. Specifically, this tutorial explains how to use the [current release](https://github.com/veg/hyphy/releases) of HyPhy from the **command line**.

__Before you begin__


1. Install the current release of HyPhy on your computer, as needed, using [these instructions].
2. This tutorial employs example datasets, available for download as a  [zip file](https://github.com/veg/hyphy-tutorials/blob/master/docs/selection/data/files.zip?raw=true). Unpack this zip file on your machine for use and **remember the absolute path to this directory**.
3. This tutorial assumes you are specifically using the HyPhy executable `HYPHYMP`. If you have installed a different executable (e.g. `HYPHYMPI`), you may need to alter some commands.
4. This tutorial uses the interactive HyPhy menu prompt to perform analyses. If you wish to automate many analyses instead of using HyPhy interactively, see the section [Automating Analyses](./current-release-tutorial/#automating-analyses) for modified instructions.

<!--
__Notation__

Throughout the tutorial, we will use the following notation:

1. `filename` refers to a file on your computer and/or local file system. In general, HyPhy requires that *absolute paths* be specified for files.
2. **Option** refers to an analysis option that you will select when prompted by HyPhy.
3. *Menu item* refers to a menu option you will select in the Mac OS X or Windows GUI (Graphical User Interface) version of HyPhy,
or a command line you will supply in terminal with the command line version of HyPhy.
4. <tt>X</tt> refers to a model parameter X.
5. The following formatting denotes text output to the screen by HyPhy.

```
[BUSTED] Selected 35 branches as the test (foreground) set: RABENSBURG_ISOLATE,WNFCG,SPU116_89,Node11,Node9,KUNCG,Node8,..
[BUSTED] Obtaining initial branch lengths under the GTR model
[BUSTED] Log(L) = -7745.475588071066
[BUSTED] Fitting the unconstrained branch-site model
```
-->

<!---------------------------------------------------------------------------------------------------->

## Estimate a single alignment-wide &omega;.


For this example, we will use HyPhy to estimate a single alignment-wide $\omega$ for the example dataset `WestNileVirus_NS3.fas`. You can examine the contents of this file in a text editor. It contains a FASTA-formatted multiple sequence alignment followed by a corresponding newick-formatted tree.
    
1. Launch HyPhy from the command line by entering `HYPHYMP`. Provide the following options to the menu prompts:
    1. Enter `1` to select `Basic Analyses`.
    2. Enter `1` to select `Analyze codon data with a variety of standard models using a given tree.`
    3. Enter `1` to select the Universal genetic code.
    4. Enter the **absolute path** to your alignment file: `/path/to/downloaded/example/files/WestNileVirus_NS3.fas`.      
    5. This screen shows a variety of model options to fit to this dataset. We will use HyPhy's preferred model [MG94xREV](../methods/general.md). Select this option by entering `MG94CUSTOMCF3X4`.
    6. Enter `2`, which tells HyPhy that the estimated $\omega$ should be shared across the entire alignment tree.
    7. Enter the string `012345`, which tells HyPhy to use the GTR mutation model in the MG94 model.
    8. Enter `Y` to confirm that HyPhy should use the tree provided in the alignment file.
    9. Enter `Estimate` to tell HyPhy to use maximum likelihood to estimate and optimize branch lengths on the provided tree.
    
2. HyPhy will now perform your analysis, which should take several minutes (depending on your computer). 
    
3. Once the analysis has completed, output that looks like this will appear:
```
______________RESULTS______________
Log Likelihood = -6413.50468184347;
Shared Parameters:
R=0.008557848966878849
GT=0.2303600815210618
CT=1.979989664067556
CG=0.02076764883647483
AC=0.2428440082030551
AT=0.3056061615274677

Tree givenTree=((((((HNY1999:0.001101787189557129,NY99_EQHS:0.00108698796444847)Node6:0,NY99_FLAMINGO:0)Node5:0,MEX03:0.003274397587748566)Node4:0.001043699094072735,IS_98:0.002238969679775947)Node3:0.0108106327401535,PAH001:0.009947231998139823)Node2:0.006480815229843424,AST99:0.01679372620666718,((((RABENSBURG_ISOLATE:1.05102590132809,(WNFCG:0.01053193289945618,SPU116_89:0.00569613982107767)Node19:0.507068944265484)Node17:0.5772661357618611,KUNCG:0.08756311980263866)Node16:0.06947527827356371,(ETHAN4766:0.02385184540957046,(CHIN_01:0.01206163326344818,EG101:0.01506055273715259)Node25:0.007681688497219724)Node23:0.003442808476468687)Node15:0.01851421610241251,(((ITALY_1998_EQUINE:0.009037431851104481,PAAN001:0.007872553578665653)Node30:0.002694356278175029,(RO97_50:0.001642931262019352,VLG_4:0.00108305411902561)Node33:0.002794580801147744)Node29:0.0007243769694723316,KN3829:0.003058011972423634)Node28:0.01097965849521703)Node14:0.00929314901848397);
```
The **R** parameter represents your alignment-wide $\omega$. **Your result for this analysis is &omega; = 0.00856.**

Additional information reported here includes the following:

* **Log Likelihood** is the log likelihood of the model fit to your dataset.
* Parameters named **GT**, **CT**, etc. represent the nucleotide exchangeability rates inferred for the GTR mutation model component of the MG94 codon model.
* **Tree givenTree** is your provided tree with branch lengths have been optimized under the fitted MG94xREV model.
<!---------------------------------------------------------------------------------------------------->


<!---------------------------------------------------------------------------------------------------->
## Use BUSTED to test for alignment-wide episodic diversification.
------------------------------------------------------------------

>[BUSTED](../methods/selection-methods/#busted) is a method described in [Murrell et al](http://www.ncbi.nlm.nih.gov/pubmed/25701167). It has been extensively tested and shows better power and accuracy than either ["branch-site" models in PAML](http://mbe.oxfordjournals.org/content/24/5/1219.short), or the ["covarion" style models](http://mbe.oxfordjournals.org/content/early/2013/10/16/molbev.mst198). 

For this example, we will run BUSTED on the dataset `HIV.nex`, which includes partial clonal HIV-1 env sequences from epidemiologically linked partners (source/donor and recipient). We will run BUSTED in two ways:

* Run BUSTED to test for selection across the entire tree.
* Run BUSTED to test for selection on specific *a priori* selection of foreground branches.

### BUSTED: Full tree analysis

1. Launch HyPhy from the command line by entering `HYPHYMP`. Provide the following options to the menu prompts:
    1. Enter `10` to select `Positive Selection`.
    2. Enter `4` to select `Run the Branch-site Unrestricted Statistical Test for Episodic Diversification to test for evidence of episodic alignment-wide selective pressure.`
    3. Enter `1` to select the Universal genetic code.
    4. Enter the **absolute path** to your dataset (in this case, a NEXUS file): `/path/to/downloaded/example/files/HIV.nex`.      
    5. Enter `Y` to confirm that HyPhy should use the tree provided in the dataset file.
    6. Enter `1` to select `All` branches to test for selection with BUSTED.
    7. Enter `d` to indicate that your branch selection is complete. 

2. BUSTED will now run for a few minutes, outputting various status indicators as it proceeds. Once BUSTED completes, the total output will look like this:

```
[BUSTED] Selected 26 branches as the test (foreground) set: R20_239,R20_245,Node5,R20_240,R20_238,R20_242,Node4,R20_241,Node3,R20_243,Node2,R20_244,Node1,D20_233,D20_235,D20_236,D20_232,Node17,D20_234,D20_237,Node21,Node16,D20_230,D20_231,Node24,Node15 
[BUSTED] Obtaining initial branch lengths under the GTR model 
[BUSTED] Log(L) = -2114.132335772669 
[BUSTED] Fitting the unconstrained branch-site model 
[BUSTED] Log(L) = -2039.992959126133. Unrestricted class omega = 104.6591567580357 (weight = 0.02032866068122922) 
[BUSTED] Fitting the branch-site model that disallows omega > 1 among foreground branches 
[BUSTED] Log(L) = -2076.666683221396 
[BUSTED] Likelihood ratio test for episodic positive selection, p = 1.110223024625157e-16 
```

This result tells us a few things:

* A proportion of sites ($\sim 0.02032$) is evolving with $\omega > 1$ a subset of the branches, although we do not know which branches specifically.
* The performed Likelihood ratio test returned a P-value$=1.11\times10^{-16}$. This result means that disallowing positive selection results in a *significantly worse fit* to the data. **We therefore reject the null hypothesis that there is no episodic positive selection the alignment.**  

In addition to this output, HyPhy has also generated a [JSON](http://json.org) containing a more detailed analysis output. The JSON will be written to same directory as the *input alignment file*, with `BUSTED.json` appended to the file name. In this example the JSON file is named `/path/to/downloaded/example/files/HIV.nex.BUSTED.json`. You can visualize, explore, and obtain plots from this JSON file using the [HyPhy Vision web application](http://veg.github.io/hyphy-vision/pages/busted/).

### BUSTED: Test a subset of branches for selection

To test for a specific selection of branches, you can modify step **1.6** from the previous BUSTED example to instead select one or more branches of interest to define as the foreground set. 

Alternatively, you can directly annotate your tree with the flag `{FG}` at specific nodes to indicate foreground branches. The most convenient way to annotate your tree is with the web-based [phylotree widget](http://veg.github.io/phylotree.js/), as demonstrated:

![busted-selection](./rsrc/busted.gif).


If you label your tree in this manner, the branch selection prompt (step 1.6 above) will show a new menu where option `4` now tests only the foreground branches, rather than the full tree. All other aspects of the analysis will remain the same.

Example results for such an *a priori* analysis might look like the following:
 
<!--
1. Navigate to http://test.datamonkey.org, selected _BUSTED_ from the _Methods and Tools_ menu.
2. Choose the file to analyze on the next screen.
3. Use the analysis setup screen to select all the `source/donor` branches as the foreground (shift-click on the branches to add them to selection)
![BUSTED datamonkey](images/busted-datamonkey.png)
4. As the analysis runs, you will see a progress page looking something  like this
![BUSTED datamonkey progess](images/busted-datamonkey-progress.png)
5. When the analysis finishes, you will be directed to a results page, which is very similar to the web app referenced above

### Testing for selection on an *a priori* specified set of branches

The tree in the `HIV.nex` is annotated with {} to indicate the set of test ("foreground") branches (e.g. you can use this [widget](http://veg.github.io/phylotree.js/) to select foreground
branches and then export them to Newick using the *Newick:Export* menu dialog).

in this case the branch being tested is the *transmission* branch, i.e. the one separating the source/donor and the recipient in the phylogenetic tree.
BUSTED will only constrain &omega; < 1 on these branches (allowing the rest of the tree to have its own &omega; distribution) during testing.

An annotated Newick string looks like this (a single branch):

>((((((R20_239:0.001179071552709126,R20_245:0.003569393318767422):0.002373643652152119,R20_240:0.00354445225954759,
>R20_238:0,R20_242:0.007143686359514547):0.001169032517101171,R20_241:0.003555888002841892):0.001829250056707198,
>R20_243:0.006486065374683752):0.003845820830922537,R20_244:0.02113434306810657)**{Test}**:0.03269082780807394,
>D20_233:0.02550919363771013,(((D20_235:0,D20_236:0,D20_232:0):0.006433904687642939,
>(D20_234:0,D20_237:0):0.005843978498632621):0.01022675723558638,
>(D20_230:0.02979851732996924,D20_231:0.006905678660095517):0.02444611465196596):0.005946252173834307);

Repeat the analysis from the previous section, choosing option 4 (**Set Test**) in step 5.
Note that you could also manually select the set of branches to test in the same dialog.

The results of this *a priori* analysis are
-->

```
[BUSTED] Selected 1 branches as the test (foreground) set: Node1 
[BUSTED] Obtaining initial branch lengths under the GTR model 
[BUSTED] Log(L) = -2114.13233621422 
[BUSTED] Fitting the unconstrained branch-site model 
[BUSTED] Log(L) = -2031.302017161514. Unrestricted class omega = 524.9720891747666 (weight = 0.07815647810018292) 
[BUSTED] Fitting the branch-site model that disallows omega > 1 among foreground branches 
[BUSTED] Log(L) = -2050.101940483789 
[BUSTED] Likelihood ratio test for episodic positive selection, p = 6.843795752331516e-09 
```

Running BUSTED to test this specified branch set for selection tells us the following information:

* A proportion of sites ($\sim 0.078$) is evolving with $\omega > 1$ on the *specified* set of foreground branch(es).
* The performed Likelihood ratio test returned a P-value$=6.84\times10^{-9}$. This result means that disallowing positive selection results in a *significantly worse fit* to the data. **We therefore reject the null hypothesis that there is no episodic positive selection on the specified foreground branch(es).**  

<!--
#### Questions.

0. Use the [web app](http://veg.github.io/hyphy-vision/pages/busted/) to visualize the JSON result file from this analysis and
compare the inferred &omega; distributions for the foreground and background branches.
1. Explain why the log-likelihood for the unconstrained model is higher for the case when *a priori* branches are tested?
2. Do these results suggest that the transmission branch is evolving differently from the rest of the tree?
3. If the *a priori* analysis had a negative result (no selection along the transmission branch), might it still be possible to
find evidence of selection in the **All** branches analysis?
-->
<!---------------------------------------------------------------------------------------------------->


<!---------------------------------------------------------------------------------------------------->
## Use aBSREL to find lineages which have experienced episodic diversification.

>[aBSREL](../methods/selection-methods/#absrel) is a method described in [Smith et al](http://www.ncbi.nlm.nih.gov/pubmed/25697341). It is an extension of our popular [BS-REL model](http://www.ncbi.nlm.nih.gov/pubmed/21670087), which performs a complexity analysis and model selection prior to doing hypothesis testing. It runs much faster than BS-REL and has better statistical properies.

For this example, we will run aBSREL on the dataset `HIV.nex`, which includes partial clonal HIV-1 env sequences from epidemiologically linked partners (source/donor and recipient). Note that this analysis differs from the BUSTED example described above because aBSREL will scan the phylogeny
for all the branches where selection may have operated. As with BUSTED, we will run aBSREL in two ways:

* Run aBSREL to test for selection by scanning all branches in the tree.
* Run BUSTED to test for selection by testing only an *a priori* selection of branches. This approach of analysis will have increased power to detect lineage-specific selection.

### aBSREL: Full tree analysis

1. Launch HyPhy from the command line by entering `HYPHYMP`. Provide the following options to the menu prompts:
    1. Enter `10` to select `Positive Selection`.
    2. Enter `1` to select `Use the random effects branch-site model (2010) to find lineages subject to episodic selection.`
    3. Enter `1` to select the Universal genetic code.
    4. Enter `1` to use the aBSREL method (instead of the older BS-REL method) 
    5. Enter `2` to assume that synonymous rates (*dS*) do not vary across sites (only *dN* will vary). You may select option `1`, although aBSREL will run much more slowly without substantial benefit. 
    6. Enter the **absolute path** to your dataset (in this case, a NEXUS file): `/path/to/downloaded/example/files/HIV.nex`.      
    7. Enter `Y` to confirm that HyPhy should use the tree provided in the dataset file. 
        * **Importantly**, if you have modified the tree in this NEXUS file for use with BUSTED or RELAX (e.g. branch annotations), **enter** `N` and instead provide the tree file `/path/to/downloaded/example/files/HIV.nwk` (a clean newick tree file) at the next menu prompt. 
    8. Enter `2` to select `All` branches to test for selection with aBSREL.
    9. Enter `d` to indicate that your branch selection is complete. 
    10. Enter an **absolute path** to a file where aBSREL output should be saved, for example `/path/to/downloaded/example/files/HIV.nex.aBSREL`.

2. The analysis will now run for several (many) minutes and produce a lot of diagnostic output while running, corresponding to aBSREL analysis stages:
    1. `[PHASE 0]`: As the initial phase, aBSREL fits the standard [MG94xREV](../methods/general.md) model to estimate a single $\omega$ for each branch and prints out model fit statistics. This is the simplest model that can be selected by aBSREL.
    2. `[PHASE 1]`: aBSREL then sorts all the branches by length (longest first), and tries to greedily add $\omega$ categories to one branch at a time, until the addition is no longer justified by AIC<sub>c</sub> scores.
    3. `[INFERRED MODEL COMPLEXITY]`: When aBSREL has determined the optimal number of $\omega$ categories at each branch, a summary of inferred model complexity will be printed to the screen.
    4. `[PHASE 2]`: Next, aBSREL optimizes all model parameters for the branch models determined in `[PHASE 1]`.
    5. Next, aBSREL will test all the branches selected in step 1.8 above (in this example, *All* branches) to see if there is a proportion of sites
with $\omega > 1$ along that branch. aBSREL further assesses, using branch-specific Likelihood ratio tests, whether disallowing any categories of $\omega>1$ would result in a significantly worse fit to the data. Note that, as a shortcut, aBSREL will only perform the LRT for a branch if it indeed contained sites with $\omega > 1$. **This is the most time consuming phase of the analysis.** aBSREL prints a running tally to the screen as tests proceed, including the rate distribution inferred for a particular branch under the null model (e.g. $\omega \leq 1$) the branch's **uncorrected** p-value. Branches not tested will show p-value=0.5.

3. Once the analysis completes, aBSREL will print out the list of all branches with p-values below 0.05 **after** 
applying the [Holm-Bonferroni multiple testing correction](http://en.wikipedia.org/wiki/Holm–Bonferroni_method), and a CPU time report indicating how long each step of the analysis took:

```
Summary of branches under episodic selection (26 were tested, of which 14 required optimizations) :
	Node1 p = 2.143165644952205e-10
	Node16 p = 0.0002007962489750659
	D20_233 p = 0.0006790829268799037


 === CPU TIME REPORT === 
	MG94 model fit : 00:00:52
	Rate class complexity analysis : 00:04:58
	aBSREL model fit : 00:01:46
	Individual branch selection testing : 00:12:02
	Total time : 00:28:26
```

Our aBSREL analysis determined that **three** branches with evidence of episodic diversifying selection were identified: Node1, D20_233, and Node16. aBSREL will have generated four additional files named as `PREFIX.extension` where PREFIX is the file name chosed in step 10 above (here, PREFIX is `/path/to/downloaded/example/files/HIV.nex.aBSREL`):

* `PREFIX.json`: a JSON file storing all the relevant analysis output. You can visualize, explore, and obtain plots from this JSON file using the [HyPhy Vision web application](http://veg.github.io/hyphy-vision/pages/absrel/). 
* `PREFIX`: a CSV file containing branch-by-branch output (similar to what is shown in the _Table_ tab of the HyPhy Vision web application).
* `PREFIX.mglocal.fit` : A HyPhy batch file containing the model fit (including all parameter estimates) of `[PHASE 0]` (only branch variation). This is a NEXUS file with a private NEXUS HyPhy block.
* `PREFIX.fit` : A HyPhy batch file containing the model fit (including all parameter estimates) of `[PHASE 2]` (unconstrained branch-site model). This is a NEXUS file with a private NEXUS HyPhy block.


### aBSREL: Test a subset of branches for selection


To test for a specific selection of branches, you can modify step **1.8** from the previous aBSREL example to instead select one or more branches of interest to test for selection. All other aspects of analysis will remain the same, except runtime will be faster because fewer tests are performed.
<!---------------------------------------------------------------------------------------------------->




<!---------------------------------------------------------------------------------------------------->
## Use FUBAR to find sites which have experienced pervasive diversification.


>[FUBAR](../methods/selection/#fubar) is described in [Murrell et al.](http://mbe.oxfordjournals.org/content/30/5/1196) which is intended to supersede (owing to its remarkable speed and statistical performance), previous REL, SLAC, and and FEL methods (although note SLAC and FEL may still be used). Because of its exceptionally fast runtime, FUBAR is particularly useful for extremely large datasets.


For this example, we will run FUBAR on the dataset `WestNileVirus_NS3.fas` to identify sites which have experienced pervasive diversification over the entire tree. For reference, an analysis by [Brault et al.](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2291521/) using our older counting method [SLAC](../methods/selection/#slac) found a single site (249) subject to pervasive positive selection.


1. Launch HyPhy from the command line by entering `HYPHYMP`. Provide the following options to the menu prompts:
    1. Enter `13` to select `Selection/Recombination`.
    2. Enter `1` to select `Detect site-specific pervasive diversifying and purifying selection using the FUBAR (Fast Unbiased Bayesian AppRoximate) method on a multiple partition data set, e.g. produced by GARD.`  Note that, as suggested by the text, FUBAR can account for the confounding effect of recombination, although it is not necessary to run GARD if recombination is not suspected.
    3. Enter `1` to select the Universal genetic code.
    4. Enter `1` to specify that a single dataset is being analyzed. Note that more could be specified, for example as outputted by GARD in the event of detected recombination.
    5. Enter the **absolute path** to your dataset (in this case, a FASTA file with embedded tree): `/path/to/downloaded/example/files/WestNileVirus_NS3.fas`.      
    6. Enter `Y` to confirm that HyPhy should use the tree provided in the dataset file. 

2. At this point, FUBAR will begin to run interactively. Analysis phases will be performed with intermittent prompts asking for additional instructions.
    * `[FUBAR PHASE 1]`: FUBAR wherein a nucleotide GTR model is fit to the data. Results from the GTR model fit are saved in the indicated file.
3. Once `[FUBAR PHASE 1]` is complete, enter `20` as the default grid size. This is the default FUBAR setting, meaning that a 20x20 grid of discrete *dN* and *dS* values will be used during selection inference. `[FUBAR PHASE 2]` will now proceed.
4. Once `[FUBAR PHASE 2]` is complete, respond to the following prompts:
    1. Enter `5` as the default number of MCMC chains to run. 
    2. Enter `2000000` as the default length for each MCMC chain.
    3. Enter `1000000` as the default number of MCMC samples to discard as burnin.
    4. Enter `100` as the default number of samples to draw from each MCMC chain.
    5. Enter `0.5` as the default concentration parameter of the Dirichlet prior. `[FUBAR PHASE 3]` will now proceed to run the MCMC chains using these specified parameters. 

5. Finally, FUBAR will finish and provide a report of sites it identified under pervasive selection:

```
[RESULTS] At posterior probability >= 0.9 there were 1 sites under diversifying positive selection, of which  0.01 [0 - 0] are expected to be false positives.

Codon	Prob[dN/dS>1]	EBF[dN/dS]>1	PSRF	N_eff
249	0.9884428021898912	595.8810841395058	1.023623280459778	90.63329322769367
```

This output tells us that a single site, codon 249, has experienced diversifying positive selection (note that this is the same site as previously found by [Brault et al.](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2291521/). FUBAR will have generated several additional files named `PREFIX.extension`, where PREFIX is the name of your datafile (here, PREFIX is `/path/to/downloaded/example/files/WestNileVirus_NS3.fas`):

* `PREFIX.fubar.csv`: **The primary result file** is a CSV of site-specific inferences, including inferences rates (where `alpha` is *dS* and `beta` is *dN*), and the column `Prob[alpha<beta]` gives the posterior probability that this site is under positive diversifying selection.
* `PREFIX.gtr_fit`: A HyPhy batch file containing the nucleotide GTR model fit during `[FUBAR PHASE 1]`. This is a NEXUS file with a private NEXUS HyPhy block.
* `PREFIX.codon_fit`: A HyPhy batch file containing the [MG94xREV](../methods/general.md) model fit during `[FUBAR PHASE 2]`. This is a NEXUS file with a private NEXUS HyPhy block.
* `PREFIX.samples*`: Text files containing information pertaining to MCMC samples. Generally you will not need these files.
* `PREFIX.grid_info`: A text file containing information pertaining to the 20x20 rate grid. Generally you will not need this file.


<!--
### Questions

1. Try the same analysis with different grid sizes (5,10,30).
  * How do the run times change?
  * Are the results robust to the choice of N?
2. Run FUBAR with using the same settings on a large HIV RT dataset (>400 sequences) `HIV_RT.nex`, which was previously analyzed by us using a [dedicated method for finding directional selection, MEDS] (http://www.ploscompbiol.org/article/info%3Adoi%2F10.1371%2Fjournal.pcbi.1002507).
  * How does FUBAR time scale with the number of sequences?
  * How does the list of sites found by FUBAR compare with the MEDS paper?
  * And with the list of sites known for their as resistance associated for [NNRTI](http://hivdb.stanford.edu/DR/NNRTIResiNote.html) and [NRTI](http://hivdb.stanford.edu/DR/NRTIResiNote.html)?
3. Explore the effect of correcting for recombination with partitioning, by running FUBAR on `CVV_G.fas` [no partitioning] and `CVV_G_GARD.nex` [partitioning into non-recombinant fragments using GARD]. How different are the lists of sites produced by the analyses?
-->
<!---------------------------------------------------------------------------------------------------->


<!---------------------------------------------------------------------------------------------------->
## Use MEME to find sites which have experienced episodic diversification.

>[MEME](../methods/selection/#meme) is described in [Murrell et al.](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1002764) and is our default recommendation for finding individual sites under selection. It is MUCH slower than FUBAR, however, so there's room for both.

For this example, we will run MEME on the dataset `WestNileVirus_NS3.fas` to identify sites which have experienced episodic positive selection. Analyzing this data with MEME will find sites where selection operated along a subset of branches, while the rest of the tree may have been strongly conserved (in **addition** to the type of sites found by FUBAR). MEME tests each individual site separately; it runs quite slowly on a desktop, but very quickly on a cluster. You may also run MEME on [datamonkey](www.datamonkey.org) to speed up the process. MEME requires a lot of user input (this is a legacy issue and will be addressed in the upcoming HyPhy v3 release).


1. Launch HyPhy from the command line by entering `HYPHYMP`. Provide the following options to the menu prompts:
    1. Enter `10` to select `Positive Selection`.
    2. Enter `9` to select `Quickly test for positive selection using several approaches`.
    3. Enter `1` to select the Universal genetic code.
    4. Enter `1` to indicate a New Analysis is being performed.
    5. Enter the **absolute path** to your dataset (in this case, a FASTA file with embedded tree): `/path/to/downloaded/example/files/WestNileVirus_NS3.fas`.  
    6. Enter `2` to specify a Custom nucleotide model.
    7. Enter the string `012345`, which tells HyPhy to use the GTR mutation model as its custom nucleotide model (resulting in an [MG94xREV](../methods/general) fit.
    8. Enter `Y` to confirm that HyPhy should use the tree provided in the dataset file. 
    9. Enter a file name to save the (intermediate) GTR mutation model fit. For example, `/path/to/downloaded/example/files/WestNileVirus_NS3.fas.nuc_fit` is a good option. Generally, you will not need this file but it will be provided in case you wish to restart/repeat an analysis (Enter `2` in step 1.4 above).
    10. Enter `5` for `Estimate dN/dS only` 
    11. Enter `11` to specify the MEME method. Note that, if you were to want to run the methods [FEL](../methods/selection/#fel) or [SLAC](../methods/selection/#fel), you could instead enter `5` (FEL without *dS* variation), `6` (FEL with *dS* variation), or `1` (SLAC) at this prompt instead.
2. HyPhy will now proceed to fit an initial nucleotide and global codon model, producing the following output:

        ______________READ THE FOLLOWING DATA______________
            19 species:{RABENSBURG_ISOLATE,WNFCG,SPU116_89,KUNCG,ITALY_1998_EQUINE,PAAN001,KN3829,RO97_50,VLG_4,AST99,PAH001,MEX03,IS_98,HNY1999,NY99_EQHS,NY99_FLAMINGO,ETHAN4766,CHIN_01,EG101};
            Total Sites:1857;
            Distinct Sites:357

            Phase 1:Nucleotide Model (010010) Model Fit

            -7842.44514029565

            Phase 2:MG94x(010010) Model Fit

            Phase 3:Estimating dN/dS

            Nuc->codon scaling factor:3.363225425621389
            Raw scaling factor:3.363225425621389
            Tree scaling factor(S): 1

            Using dN/dS=0.02413010970256795
            Codon model:-6578.11643060985


3. You will then see two additional prompts:
    1. Enter `0.1` (or any other reasonable threshold) as the Significance Level. Here, the default is 0.1 (rather than perhaps more traditional 0.05) because MEME is a conservative test on small alignments and 0.05 may be too stringent a threshold.
    2. Enter `N` to not save fit files for individual codons. These many files will generally not be needed.
4. MEME will now run to completion and will print site-specific inferences to screen as they are completed, for example:

        [RETUNING BRANCH LENGTHS AND NUCLEOTIDE RATES UNDER THE CODON MODEL]
        IMPROVED Log(L) BY 125.2787507415687 POINTS
        | Codon:    1| Beta1:       0.00| P(Beta1):  0.93| Beta2:       0.00| P(Beta2):  0.07| alpha:       0.18| LRT:   0.00| p:  1.00| Log(L): -5.91
        | Codon:    2| Beta1:       0.00| P(Beta1):  0.93| Beta2:       0.00| P(Beta2):  0.07| alpha:       2.13| LRT:   0.00| p:  1.00| Log(L): -16.18
        | Codon:    3| Beta1:       0.00| P(Beta1):  0.93| Beta2:       0.00| P(Beta2):  0.07| alpha:       0.37| LRT:   0.00| p:  1.00| Log(L): -7.96
        | Codon:    4| Beta1:       0.00| P(Beta1):  0.93| Beta2:       0.00| P(Beta2):  0.07| alpha:       1.88| LRT:   0.00| p:  1.00| Log(L): -19.68


5. When finished, MEME issues a final prompt for a CSV file name in which this site-specific information will be saved. For example, `/path/to/downloaded/example/files/WestNileVirus_NS3.fas.MEME.csv` is a good option to provide here. 
    
6. You should now see the final output printed to the screen, corresponding to the codon(s) that MEME identified as under selection:
```
| Codon:  249| Beta1:       0.86| P(Beta1):  0.00| Beta2:       2.50| P(Beta2):  1.00| alpha:       0.00| LRT:   7.62| p:  0.01| Log(L): -33.85 *P
```

This information, along with information for all other codon sites, will be in the final CSV file whose name you specified in step 3. Provided information in this output and in the CSV files includes the following columns:

* `alpha`: The estimate for the synonymous rate at the given site (*dS*). This value is shared across all branches.
* `Beta1`: The estimate for the first nonsynonymous rate (*dN*) category at the given site. By definition, this parameter is constrained as Beta1 &le; alpha.
* `P(Beta1)`: The proportion of branches at the given site which MEME estimated to evolve with the rate Beta1.
* `Beta2`: The estimate for the second nonsynonymous rate (*dN*) category at the given site. By definition, this parameter is unconstrained (can be any value).
* `P(Beta2)`: The proportion of branches aat the given site which MEME estimated to evolve with the rate Beta2.
* `LRT` is the likelihood ratio test statistic obtained by testing the relative fit of the full model to the null model which constrains Beta2 &le; alpha
* `p` is the p-value for positive selection at this site. if `*P` is displayed at the end of the line, the p-value is at or below the selected threshold for positive selection.


<!--
### Questions

1. Find sites detected as selected by MEME, but not by FUBAR. What makes them different from those which are detected by both methods?
2. Using R (or another data analysis package), plot how LRT (or p-value) varies over sites.
3. Is `(1-p)` [p-value] of MEME correlated with the posterior probability of positive selection derived by FUBAR (use a non-parametric association test, e.g. rank correlation)? Use the CSV files generated by each analysis to import the results into a statistical package for analysis.
-->
<!---------------------------------------------------------------------------------------------------->

<!---------------------------------------------------------------------------------------------------->
## Use FEL or SLAC to find sites which have experienced pervasive diversification.

>[FEL](../methods/selection/#fel) and [SLAC](../methods/selection/#slac) are described in [Pond and Frost]( https://doi.org/10.1093/molbev/msi105). These are the original HyPhy methods for detecting individual sites under selection across the entire phylogeny. We strongly recommend using MEME or FUBAR instead of either of these methods, but they remain available if you still wish to use them.

Running FEL and SLAC require almost identical steps as MEME (see above). Therefore, you should begin a FEL/SLAC analysis by following menu prompt instructions 1.1-1.10, as described in the MEME tutorial. At step 1.11, you will be prompted to select a specific method for positive selection inference:

### Running FEL
1. To run FEL, enter either `5` (One-rate FEL, i.e. without *dS* variation) or `6` (Two-rate FEL, i.e. with *dS* variation) when you see the prompt `Ancestor Counting Options`. For selection inference, we strongly recommend running a two-rate FEL (option `6`).
2. HyPhy will proceed to fit the initial nucleotide and global codon models. You will then see a prompt for the Significance level, for which you may enter a preferred p-value threshold (default is `0.1`).
3. If you have selected option `6` for a two-rate FEL, you will see an additional prompt asking about `Branch Options`. To test the whole tree for selection, enter `1` here for `All branches`. If you selected option `5` for a one-rate FEL, this prompt will not appear.
4. FEL will now run to completion. As it runs, FEL will print site-specific inferences to the screen, for example:

        [RETUNING BRANCH LENGTHS AND NUCLEOTIDE RATES UNDER THE CODON MODEL]
        IMPROVED Log(L) BY 125.2787507415687 POINTS
        | Codon:    1| dN/dS:       0.00| dN:  0.00| dS:  0.18| dS(=dN):  0.05| Log(L):      -5.91| LRT:  2.38| p:  0.12
        | Codon:    2| dN/dS:       0.00| dN:  0.00| dS:  2.13| dS(=dN):  0.18| Log(L):     -16.18| LRT:  8.75| p:  0.00 *N
        | Codon:    3| dN/dS:       0.00| dN:  0.00| dS:  0.37| dS(=dN):  0.06| Log(L):      -7.96| LRT:  2.89| p:  0.09 *N
        | Codon:    4| dN/dS:       0.00| dN:  0.00| dS:  1.88| dS(=dN):  0.33| Log(L):     -19.68| LRT:  9.43| p:  0.00 *N


5. When finished, FEL issues a final prompt for a CSV file name in which this site-specific information will be saved. For example, `/path/to/downloaded/example/files/WestNileVirus_NS3.fas.FEL.csv` is a good option to provide here.

This final FEL results file will have several columns:

* `Codon`: The codon site. 
* `dN/dS`: The resulting $\omega$ estimate for this site.
* `dN`: The estimated *dN* parameter at this site. 
* `dS`: The estimated *dS* parameter at this site. 
* `dS=dN`: The rate estimate under the null model of evolution where the constraint $dS=dN$ is enforced. Generally this is not needed. 
* `LRT`: The likelihood ratio test statistic for comparing null and alternative models to test for selection.
* `p-value`: The resulting p-value from the LRT used to test for selection. If this row shows a value $dN/dS > 1$ and a p-value below your specified threshold, then the site is positively selected.
* `Full Log(L)`: The log likelihood for the alternative model fit. 

Note that one-rate FEL result files will only contain these columns:

* `dN/dS`
* `LRT`
* `p-value`
* `Log(L)`. This column is the same as `Full Log(L)`, except with a different name.


### Running SLAC
1. To run SLAC, enter `1` when you see the prompt `Ancestor Counting Options`, to select the option `Single Ancestor Counting`.
2. HyPhy will proceed to fit the initial nucleotide and global codon models. You will then see a prompt for `SLAC Options`, for which you should enter `1` for `Full tree`. The other choice, `Tips vs Internals`, is mostly useful for certain viral sequence, e.g. influenza, analyses but is usually not relevant.
3. Enter `1` to select `Averaged` treatment of ambiguities.
4. Enter `1` for the `Approximate` test statistic.
5. Provide the Significance level of `0.1`.
6. SLAC will now run to completion, very quickly, and print site-specific information about selection inference. At the top of this printed information is a summary about sites determined to be under positive/negative selection. The top portion of this information should look like this:

        ******* FOUND NO POSITIVELY SELECTED SITES ********


        ******* FOUND 175 NEGATIVELY SELECTED SITES ********


        +--------------+--------------+--------------+--------------+
        | Index        | Site Index   | dN-dS        | p-value      | 
        +--------------+--------------+--------------+--------------+
        |            1 |     2.000000 |    -3.000000 |     0.037037 |
        +--------------+--------------+--------------+--------------+
        |            2 |     4.000000 |    -2.571328 |     0.073792 |
        +--------------+--------------+--------------+--------------+

7. Finally, You will then see a prompt for `Output Options` where more detailed result information. Select option `2` to export result to file. You will then be prompted for a file name for this output (tab-delimited file). For example, `/path/to/downloaded/example/files/WestNileVirus_NS3.fas.SLAC.txt` is a good option to provide here.

This final SLAC results file will have several columns, where rows are ordered as codon sites in your alignment:

* `Observed S Changes`: The total *count* of synonymous changes at this site
* `Observed NS Changes`: The total *count* of nonsynonymous changes at this site
* `E[S Sites]`: The expected number of "synonymous sites" (i.e. opportunities for synoynymous change) at this site. This quantity is used to normalize synonymous substitution counts to obtain a *dS* value.
* `E[NS Sites]`: The expected number of "nonsynonymous sites" (i.e. opportunities for nonsynoynymous change) at this site. This quantity is used to normalize nonsynonymous substitution counts to obtain a *dN* value.
* `Observed S. Prop.`: The proportion of observed changes which were synonymous.
* `P{S}`: The proportion of substitutions expected to be synonymous under neutral evolutuion.
* `dS`: The estimated (by counting) dS value at this site.
* `dN`: The estimated (by counting) dN value at this site.
* `dN-dS`: The difference between dN and dS values.
* `P{S leq. observed}`: The probability of getting as many or *fewer* synonymous changes observed at this site, under a binomial distribution.
* `P{S geq. observed}`: The probability of getting as many or *more* synonymous changes observed at this site, under a binomial distribution.
* `Scaled(dN-dS)`: The difference between dN and dS values, normalized by the total tree length (sum of optimized branch lengths).
<!---------------------------------------------------------------------------------------------------->



<!---------------------------------------------------------------------------------------------------->
## Use RELAX to compare selective pressures on different parts of the tree

>[RELAX](../methods/selection/#relax) is a method described in [Wertheim et al](http://www.ncbi.nlm.nih.gov/pubmed/25540451). It is based on the [BS-REL model](http://www.ncbi.nlm.nih.gov/pubmed/21670087) branch site framework, but the tree is partitioned (a priori) into non-overlapping sets of branches, and the separate distributions of &omega; are fitted to each set and compared for relative _relaxation_ (&omega; values contract to 1) or _intensification_ (&omega; values move away from 1).

For this example, we will run RELAX on the dataset `HIV.nex`, which includes partial clonal HIV-1 env sequences from epidemiologically linked partners (source/donor and recipient). We will specifically test if natural selection in the recipient (`R` branches) and in the source/donor (`D` branches) operate at different intensities. Importantly, this analysis will **not** use the tree provided in `HIV.nex`, but instead a different tree available in the example file `HIV-relax.nwk`. This file contains a newick phylogeny whose branches have been annotated as either `{Recipient}` or `{Donor}`. These labels were applied using this web-based [phylotree widget](http://veg.github.io/phylotree.js/).

1. Launch HyPhy from the command line by entering `HYPHYMP`. Provide the following options to the menu prompts:
    1. Enter `10` to select `Positive Selection`.
    2. Enter `10` to select ` Test whether selected branches are under relaxed or intensified selection against reference branches`.
    3. Enter `1` to select the Universal genetic code.
    4. Enter the **absolute path** to your dataset (in this case, a NEXUS file): `/path/to/downloaded/example/files/HIV.nex`.
    5. Enter `N` to opt **not** to use the tree found in the data file.
    6. Enter the **absolute path** to the newick tree file which has been annotated for use in RELAX: `/path/to/downloaded/example/files/HIV-relax.nwk`.
    7. Enter `3` to select the branches labeled `Recipient` as your test set of branches ("T set").
    8. Enter `2` to select the branches labeled `Donor` as your reference set of branches ("R set").
    9. Enter `2` to execute only the `Minimal` analysis type. Note that entering `1` for `All` tests will additionally run additional descriptive models described [here](../methods/selection/#relax).
2. RELAX will now begin to run and output information to the screen as it proceeds to completion:
        
        [RELAX] Obtaining branch lengths under the GTR model 
        [RELAX] Log(L) = -2114.132338088236 
        [RELAX] Obtaining omega and branch length estimates under the partitioned MG94xGTR model 
        [RELAX] Log(L) = -2076.093223041783 
        [RELAX] Fitting the RELAX null model 
        [RELAX] Log(L) = -2031.204697143867 
        [RELAX] Fitting the RELAX alternative model 
        [RELAX] Log(L) = -2024.075837744705. Relaxation parameter K = 0.4389230603260226 
        [RELAX] Likelihood ratio test for relaxation on Test branches, p = 0.0001594057084282063 

    The output provides several pieces of information:
    
    * The alternative model that selection was relaxed/intensified along the "test" branches significantly outperformed the null model with a P-value=$1.59\times10^{-4}$, as assessed with the likelihood ratio test. **We therefore reject the null hypothesis that selection intensity has not shifted from the reference to the test branches.**
    * RELAX estimated the *selection intensity parameter* value of **K=0.439** (note that K=1 is RELAX's null hypothesis). Because K is *less than 1*, we can infer that selection **was relaxed/was weaker** along the test than on the reference branches. In other words, $\omega$ rates "shrank" towards 1 on the test branches compared to the reference branches. 


Like in other analyses, HyPhy will generate a JSON file, in this case called `HIV.nex.RELAX.json`, in the same directory where the original dataset `HIV.nex` is located. This JSON file contains all the relevant analysis output, and can visualize, explore, and obtain plots from this JSON file using the [HyPhy Vision web application](http://veg.github.io/hyphy-vision/pages/relax/). 
<!---------------------------------------------------------------------------------------------------->



<!---------------------------------------------------------------------------------------------------->
## Automating analyses

All above examples use HyPhy interactively. This approach, however, may be exceptionally tedious if you have many datasets to analyze (or if you don't want to use HyPhy interactively). In this case, it would be better to automate analyses in HyPhy. The best way to accomplish this goal is by **piping** arguments (`|` symbol) into HyPhy. 

For example, if you look through the BUSTED tutorial above, you will see these options provided to the interactive HyPhy session, in order:

1. `10` 
2. `4`
3. `1` 
4. `/path/to/downloaded/example/files/HIV.nex`  
5. `Y`
6. `1`
7. `d`

You can combine all of these input options in a single HyPhy call:
```
echo `(echo "10"; echo "4"; echo "1"; echo "/path/to/downloaded/example/files/HIV.nex"; echo "Y"; echo "1"; echo "d") | HYPHYMP`
```

If you have several datasets to analyze, a for-loop may come in handy:
```
# Path to files of interest
FILEPATH=/absolute/path/to/directory/with/all/your/files/

# Run BUSTED on all files $FILEPATH/*.fas
for FILE in `ls $FILEPATH/*.fas`; do
    echo "Running BUSTED on $FILE"
    echo `(echo "10"; echo "4"; echo "1"; echo $FILE; echo "Y"; echo "1"; echo "d") | HYPHYMP`
done
```


