## FEL-contrast

|   |   |
|---|---|
| HyPhy version required   |  &geq; 2.3.4 |
| Parallel support | MP and/or MPI |
| File path | `LIB/TemplateBatchFiles/SelectionAnalyses/FEL-contrast.bf` |
| Standard analysis menu | `Evolutionary Hypothesis Testing > FEL-contrast` |


### What biological question is the method designed to answer?

Which sites in a gene may be associated with adaptation to a different environment. You need a tree with branches partitioned (a priori) into two sets: reference and test.

### What are the recommended applications?

Suppose you have a gene which was sampled from different selective environments.
The specific example for which this tool was developed is evolution of HIV in different
hosts or different compartments (blood vs brain) in the host. Similar situations arise
when the gene is sampled from species living in different environment, eating different food,
having different wavelength eye sensitivity. This division has to be binary, however, so
that any branch in the tree is either in the **reference** environment, or the **test** environment.

FEL-contrast then allows you to examine selective pressures (measured as dN/dS) at each site
in the gene individually, and test whether or not they are different between environments.

Armed with a list of such sites, you could then attempt to explore if evolution at these sites
is associated with adaptation to the environment.

### What is the statistical procedure and statistical test is used to establish significance for this method?

For each site, three rates are inferred, with other parameters (frequencies, branch lengths) inferred jointly and held at

- &alpha; : synonymous substitution rate
- &beta; <sub>r</sub> : non-synonymous substitution rate along **reference** branches
- &beta; <sub>p</sub> : non-synonymous substitution rate along **test** branches

Two models are compared using a likelihood ratio test

- H<sub>A</sub>: &alpha;, &beta; <sub>r</sub>, and &beta; <sub>t</sub> are inferred by maximum likelihood as free parameters

- H<sub>0</sub>: The &beta; <sub>r</sub> := &beta; <sub>t</sub> constraint is enforced.

The models are nested and differ by one degree of freedom. p-values are computed using the limit &chi;<sup>2</sup> distribution with one degree of freedom.


### How should one interpret positive and negative test results?

A significant result at a site means that dN/dS (&beta;/&alpha) is **different** between the two sets of branches, with either an **increase** or a **decrease** on the test branches _relative_ to the reference branches. A significant finding does **not** make any claims about positive (dN/dS > 1) or negative (dN / dS < 1), just that dN/dS differ among sets of branches, i.e., a difference need not change the **mode** of selection.

Negative results do not mean that there is no difference, rather that whatever difference there may be does not rise to the level of statistical significance/

###  Rules of thumb for when this method is likely to work well, and when it is not.

 - Generally, you need 10 or more branches in each set to be able to have any statistical power.
 - Too little divergence is also likely to severely throttle statistical power.


### Example

We will analyze partial HIV-1 env sequences from a transmission pair: sequences are isolated from the putative source individual and the putative recipient individual from the 2005 study by [Frost et al](https://www.ncbi.nlm.nih.gov/pubmed/15858036).

First, partition the tree into the source and recipient (here we include the transmission branch with the source sequences), for example as described [here](/resources/#labeling-branches-with-phylotree)
