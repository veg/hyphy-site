## Overview

HyPhy (**Hy**pothesis Testing using **Phy**logenies) is an open-source software package for the analysis of genetic sequences (in particular the inference of natural selection) using techniques in phylogenetics, molecular evolution, and machine learning. It features a rich scripting language for limitless customization of analyses. Additionally, HyPhy features support for parallel computing environments (via message passing interface). HyPhy has over 10000 registered users and has been cited in over 1800 peer-reviewed publications ([Google Scholar](https://scholar.google.com/scholar?hl=en&as_sdt=5,39&cites=17874163875017617061,8555001991860797787&scipsc=&q=&scisbd=1)). 

## Brief history

HyPhy grew out of the collaboration between [Spencer Muse](http://www4.stat.ncsu.edu/~muse/) and [Sergei Kosakovsky Pond](http://hyphy.org/sergei) that commenced in 1997 and continues to this day, with many additional collaborators, including [Art Poon](https://www.schulich.uwo.ca/pathol/people/bios/faculty/poon_art.html), [Simon Frost](http://www.vet.cam.ac.uk/directory/sdf22@cam.ac.uk), [Steven Weaver](http://stevenweaver.org), [Stephanie Spielman](http://sjspielman.org), [Lance Hepler](https://github.com/nlhepler), [Martin Smith](https://www.linkedin.com/in/martin-smith-371a7717/), [Konrad Scheffler](https://www.linkedin.com/in/konrad-scheffler-b185943/), [Wayne Delport](https://www.linkedin.com/in/wayne-delport-5195b545/), [Ben Murrell](http://profiles.ucsd.edu/benjamin.murrell), and [Joel Wertheim](http://id.ucsd.edu/faculty/wertheim.shtml). HyPhy was originally released in 2000, is currently at version 2.3, and is presently undergoing a major rewrite, with version v3.0 planned for release in 2018. 

## Design philosophy
 
HyPhy was designed to allow the specification and fitting of a very broad class of continuous time discrete space Markov models of sequence evolution. To implement these models, HyPhy provides its own scripting language - **HBL**, or **HyPhy Batch Language** (see [an example](#example-hbl-script)), which can be used to develop custom analyses or modify existing ones, but it is not necessary to learn or even be aware of it in order to use the package. This is because most common models and analyses have been implemented in a "push-button" type of analyses. Once the model is defined, it can be fitted to data (using a fixed tree), its parameters can be constrained in almost arbitrary ways to test various hypotheses (e.g. is rate1 > rate2), and simulate data from. While HyPhy by and large implements **maximum likelihood** methods, it can also be used to perform some forms of Bayesian inference (e.g. [FUBAR](/methods/selection-methods.md#fubar)), fit Bayesian Graphical Models to the data, run Genetic Algorithms to perform complex model selection, etc.

## Features

1. Support for arbitrary sequence data, including nucleotide, amino-acid, codon, binary, count (microsattelite) data, including multiple partitions mixing differen data types. 
2. Complex models of rate variation, including site-to-site, branch-to-branch, hidden markov model (autocorrelated rates), between/within partions, co-varion type models.
3. Fast numerical fitting routines, supporting parallel and distributed execution.
4. A very broad collection of pre-defined evolutionary models. 
5. The ability to specify very flexible constraints on model parameters and estimate confidence intervals on MLEs.
6. Ancestral sequence reconstruction and sampling. 
7. Simulate data from any model that can be defined and fitted in the language.
8. Apply unique (for this domain) machine learning methods to discover patterns in the data, e.g. genetic algorithms, stochastic context free grammars, Bayesian Graphical models.
9. Script analyses completely in HBL including flow control, I/O, parallelization, etc.
10. (v2.3) Modern web-applications for interactive result visualization.



## Example HBL Script
```js
/* 
   This is an example HY-PHY Batch File.
   It reads in a MEGA format nucleotide dataset from data/hiv.nuc 
   and fits the F81 model using the tree inclded in the file usig maximum likelihood
   Output is printed out as a Newick Style tree with branch lengths
   representing the number of expected substitutions per branch
*/

// 1. Read in the data and store the result in a DataSet variable

DataSet 		nucleotideSequences = ReadDataFile ("data/hiv.nuc");

// 2. Filter the data, specifying that all of the data is to be used
//  and that it is to be treated as nucleotides.*/
	 
DataSetFilter	filteredData = CreateFilter (nucleotideSequences,1);

// Collect observed nucleotide frequencies from the filtered data. observedFreqs will
// store receieve the vector of frequencies. 

HarvestFrequencies (observedFreqs, filteredData, 1, 1, 1);

// Define the F81 substitution matrix. '*' is defined to be -(sum of off-diag row 
// elements); mu is the rate*time parameter 

F81RateMatrix = 
		{{*,mu,mu,mu}
		 {mu,*,mu,mu}
		 {mu,mu,*,mu}
		 {mu,mu,mu,*}};

//  Define the F81 models, by combining the substitution matrix with the vector of observed (equilibrium) frequencies.
	  
Model 	F81 = (F81RateMatrix, observedFreqs);

// Now we can define the tree variable, using the tree string read from the data file, 
// and, by default, assigning the last defined model (F81) to all tree branches.

Tree	givenTree = DATAFILE_TREE;

// Since all the likelihood function ingredients (data, tree, equilibrium frequencies)
// have been defined we are ready to construct the likelihood function.

LikelihoodFunction  LF = (filteredData, givenTree);

// Maximize the likelihood function, storing parameter values in the matrix paramValues 

Optimize (paramValues, LF);

// Print the tree with optimal branch lengths to the console. 

fprintf  (stdout, LF);

```
