HyPhy v2.3 Quick Start
======================

> **CAUTION:** This tutorial is for the development branch of HyPhy only! Please see [this tutorial](selection/README.md) for information on using the current HyPhy release.


This tutorial outlines how to prepare data and execute analyses for use in the following methods:

* [aBSREL](../methods/selection-methods/#absrel)
* [BUSTED](../methods/selection-methods/#busted)
* [FEL](../methods/selection-methods/#fel)

Note that you can additional use these methods via [Datamonkey](http://test.datamonkey.org).


If you do not have a dataset to work with, you might find it convenient to
download this [zip file](https://github.com/veg/hyphy-tutorials/blob/master/docs/selection/data/files.zip?raw=true) with some example datasets.

------------------------------------------------------------------
Installation
------------------------------------------------------------------

> *Warning : This is for the development branch of HyPhy!* 


### Dependencies
  - [cmake](https://cmake.org/download/) > 3.0

### Commands

Install the development branch of HyPhy on your system by issuing the following commands:

```
git clone https://github.com/veg/hyphy.git
cd hyphy
git checkout v2.3-dev
cmake .           # Requires version > 3.0
make HYPHYMP      # openMP should be installed in your system for optimal performance
```

Check that the HyPhy installation was successful using the following command:
```
./HYPHYMP LIBPATH=`pwd`/res ./tests/hbltests/libv3/math.bf
```

If HyPhy is working correctly, you should see the following output:
```
{
 "Count":4,
 "Mean":2.25,
 "Median":2,
 "Min":1,
 "Max":4,
 "2.5%":1,
 "97.5%":4,
 "Sum":9,
 "Std.Dev":1.089724735885168,
 "Variance":1.1875,
 "COV":0.4843221048378527,
 "Skewness":0.6520236646847543,
 "Kurtosis":2.096952908587258,
 "Sq. sum":18,
 "Non-negative":4
}
```



## RELAX

>RELAX is a method described in [Wertheim et al](http://www.ncbi.nlm.nih.gov/pubmed/25540451). It is based on the [BS-REL model](http://www.ncbi.nlm.nih.gov/pubmed/21670087) branch site framework, but the tree is partitioned (a priori) into non-overlapping sets of branches. Separate distributions of $\omega$ are fitted to each set and compared for relative _relaxation_ ($\omega$ values contract to 1) or _intensification_ ($\omega$ values move away from 1) of selection pressure.

<!--
* Please visit Dr. Pond's [tutorial](selection/README/#use-relax-to-compare-selective-pressures-on-different-parts-of-the-tree) for an in-depth overview of conducting an analysis.
-->

**1.** RELAX requires that branches be *a priori* partitioned into two sets of non-overlapping branches: The *reference* branch set and the *test* branch set. The RELAX test for relaxation/intensification of selection pressure will be run on the *test* branches relative to the baseline *reference* branches. The easiest way to partition your newick tree is using the web-based [phylotree application](http://veg.github.io/phylotree.js/), as demonstrated:

![relax-selection](./rsrc/relax.gif)


**2.** From *within* the HyPhy directory, issue the following command to run RELAX and respond to the prompts:
```
./HYPHYMP LIBPATH=`pwd`/res res/TemplateBatchFiles/SelectionAnalyses/RELAX.bf
```
> Be sure to provide absolute paths for all file names prompted.

Alternatively, you can pipe the arguments directly into the HyPhy call to RELAX.

```
(echo 1; echo <path to sequence file>; echo <path to tree file>; echo 3; echo 2;echo 1) | ./HYPHYMP LIBPATH=`pwd`/res res/TemplateBatchFiles/SelectionAnalyses/RELAX.bf
```
In the above example, the piped arguments correspond to the following:

1. `1` - Select the Universal Code
2. `<path to sequence file>` - the *absolute path*/filename of the multiple sequence alignment
3. `<path to sequence file>` - the *absolute path*/filename of the labeled newick tree
4. `3` - Selects tagged partition for testing relaxed selection
5. `2` - Selects tagged partition for reference branches
6. `1` - Fits descriptive models and run the relax test (4 models) as opposed to a minimal RELAX test (2 models)

> NOTE: In general, HyPhy assumes that the provided alignment (e.g. NEXUS, FASTA) file does not contain a defined tree. If there is a tree in the alignment file, HyPhy will use the defined tree and not prompt for an additional file.

**3.** Once the RELAX job is completed, there will be a file that is generated in the
same directory *as the sequence file* (not the working directory) named `<sequence file>.RELAX.json`.
The file is standard JSON, and can be parsed with any programming language. To visualize your results in a bit more human-readable format, visit [HyPhy Vision](http://veg.github.io/hyphy-vision/pages/relax/) to upload and view your results.


------------------------------------------------------------------
Use BUSTED to test for alignment-wide episodic diversification.
------------------------------------------------------------------

>[BUSTED](../methods/selection-methods/#busted) is a method described in [Murrell et al](http://www.ncbi.nlm.nih.gov/pubmed/25701167). It has been extensively tested and shows better power and accuracy than either ["branch-site" models in PAML](http://mbe.oxfordjournals.org/content/24/5/1219.short), or the ["covarion" style models](http://mbe.oxfordjournals.org/content/early/2013/10/16/molbev.mst198). 

Note that you can use BUSTED via [Datamonkey](http://test.datamonkey.org/busted), or follow [this tutorial](current-release-tutorial/#use-busted-to-test-for-alignment-wide-episodic-diversification) to use BUSTED in the current version of HyPhy. Otherwise, follow these directions to run BUSTED in the development branch of HyPhy:


1. If you would like to use BUSTED to test specific foreground branches for episodic selection, you must prepare your newick phylogeny with annotated branches. To accomplish this, we recommend using the web-based [phylotree widget](http://veg.github.io/phylotree.js/), as demonstrated below. Export and save this annotated tree for use in BUSTED. Alternatively, you can analyze the entire tree for episodic diversification, in which case branch annotation is not needed and a "regular" newick tree will be fine.
![busted-selection](./rsrc/busted.gif) 
2. Open a terminal session and navigate to the HyPhy directory. Issue the following command:
```
./HYPHYMP LIBPATH=`pwd`/res res/TemplateBatchFiles/SelectionAnalyses/BUSTED.bf
``` 
and answer the prompts:

and answer the prompts


Alternatively, you couple pipe the arguments into HyPhy

```
(echo 1; echo <path to sequence file>; echo <path to tree file>; echo 4; echo d) | ./HYPHYMP LIBPATH=`pwd`/res res/TemplateBatchFiles/SelectionAnalyses/RELAX.bf
```

Explanation

* `1` - Selects the [Universal Genetic Code](http://www.datamonkey.org/help/geneticcodes.html).
* `<path to sequence file>` - the filename of the multiple sequence alignment
* `<path to sequence file>` - the filename of the newick tree
* `4` - Sets Foreground to test on all branches labeled with {Foreground} jointly
* `d` - Completes the selection

> Please note that if there is a tree defined within the NEXUS file, HyPhy will use the defined tree and not prompt for an additional file.

Once the BUSTED job is completed, there will be a file that is generated in the
same directory as the sequence file named `<sequence file>.BUSTED.json`.

The file is standard JSON, and can be parsed with any programming language. For
something a bit more human readable, you can visit [this
page](http://veg.github.io/hyphy-vision/pages/busted/) to view your results.

------------------------------------------------------------------
FEL - Fixed Effects Model for detecting site-wise selective pressure
------------------------------------------------------------------
>[FEL](../methods/selection/#fel) is described in [Pond and Frost](https://doi.org/10.1093/molbev/msi105). FEL estimates
site-wise synonymous ($\alpha$) and non-synonymous ($\beta$) rates, and uses a
likelihood ratio test to determine if $\beta \neq \alpha$ at each site. The estimates
aggregate information over all branches, so the signal is derived from
pervasive diversification or conservation.

* You can try FEL via [Datamonkey](http://datamonkey.org/)

```
./HYPHYMP LIBPATH=`pwd`/res res/TemplateBatchFiles/SelectionAnalyses/FEL.bf
```

and answer the prompts


Alternatively, you couple pipe the arguments into HyPhy

```
(echo 1; echo <path to sequence file>; echo <path to tree file>; echo 1; echo 0.1) | ./HYPHYMP LIBPATH=`pwd`/res res/TemplateBatchFiles/SelectionAnalyses/FEL.bf
```

Explanation

* `1` - Selects the [Universal Genetic Code](http://www.datamonkey.org/help/geneticcodes.html).
* `<path to sequence file>` - the filename of the multiple sequence alignment
* `<path to sequence file>` - the filename of the newick tree
* `1` - Include all branches in the analysis
* `0.1` - The p-value threshold

> Please note that if there is a tree defined within the NEXUS file, HyPhy will use the defined tree and not prompt for an additional file.

> Please note that FEL is an MPI-aware script. You are free to use HYPHYMPI in conjunction with mpirun on computing clusters for improved performance.


