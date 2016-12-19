## aBSREL Glossary

### Summary Statistics
* **number of sequences** - the number of sequences present in the input file
* **number of variants** - the number of variants present in the input file
* **number of branches** - the number of branches in the phylogeny

### aBSREL results summary
* **LRT** - likelihood ratio test implemented as described in Smith et al., 2015 (Mol. Biol. Evol. 32:1342).
* **multiple testing correction** - as the number of multiple statistical inferences or comparisons that are considered simultaneously increase, by chance, an increasing number of comparisons will result in a significant p-value that represent false positives. To offset this problem, multiple test corrections such as the Holm-Bonferroni correction (Holm, 1979, Scand. J. Statist., 6:65) are applied.

### Model Fits Table

* **MG94** - the standard Muse-Gaut 94 model estimates a single ω for each branch 

* **Full model** - the aBSREL model estimates up to ten ω rate classes for each branch

* ***log* L** - log likelihood estimate of the respective model

* **\# par.** - the number of parameters in the model

* **AIC<sub>c</sub>**  - small-sample Akaike Information Criterion (Sigiura, 1978, Commun. Stat. Theory Methods, A7:13) is used to infer the optinal number of rate categories to be used for each branch in the phylogeny.

* **L<sub>tree</sub>** - [[add in definition]]


### Tree Table

* **ω rate classes** - the number of inferred rate classes. ω represents the ratio of nonsynonymous to synonymous substitution
* **\# of branches** - the number of branches inferred to have the respective number of ω rate classes 
* **% of branches** - the proportion of branches in the phylogeny inferred to have the respective number of ω rate classes 
* **% of tree length** - the proportion of the total tree length inferred to have the respective number of ω rate classes 
* **\# under selection** - the number of branches inferred to have a non neutral ω rate class at the designated p-value threshold
 
 
### Full Table
* **B LRT** - branch length likelihood ratio test statistic
* **Test p-value** - multiple testing corrected p-value (Holm, 1979, Scand. J. Statist., 6:65)
* **Uncorrected p-value** - raw p-value
* **ω distribution over sites** - inferred ω branch rates and respective proportion of branch sites
 



