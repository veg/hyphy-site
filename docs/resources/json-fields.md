Understanding the content of JSON output files
===============

Most standard analyses in HyPhy output results in [JSON format](https://en.wikipedia.org/wiki/JSON), essentially a nested dictionary. This page describes the contents of each method's JSON output.

We note that these files are easily parsed for downstream use with standard scripting languages, e.g. using the `json` package in Python or `jsonlite` package in R.

### Bookkeeping fields

There are several fields which appear in JSONs that are used strictly for displaying results in [HyPhy Vision](vision.hyphy.org) and have no scientific meaning. These fields, which you can safely ignore, include the following:
	+ **`display order`**, in all analyses
	+ <od mashhu>
	
### Shared fields

All standard selection analyses will have the following top-level fields:

#### **`analysis`** 

This field contains information about the analysis method of interest and is comprised of the following keys:

+ **`info`**, Gives method name a brief statement of its intended use
+ **`version`**, Method version
+ **`citation`**, Method reference
+ **`authors`**, names of primary authors of method
+ **`contact`**, primary author to contact
+ **`requirements`**, Data required in order to execute method

#### **`input`** 

This field contains information about the inputted dataset being analyzed and is comprised of the following keys:

+ **`file name`**, Full path to the name of user-inputted alignment file
+ **`number of sequences`**, The number of sequences in the user-inputted alignment
+ **` number of sites`**, The number of sites in the user-inputted alignment
+ **`partition count`**, The number of user-specified data partitions to be used in the given analysis
+ **`trees`**, The inputted trees (with user-supplied branch lengths, if applicable). This field is itself a dictionary containing all provided trees in newick format. The key for each tree corresponds to the data partition to which it belongs, starting from 0. For example, if there is one specified partition, this field might look like the following:
			
			
			trees":{
    			"0":"((taxon1: 0.5, taxon2: 0.5):0.5),taxon3:0.5)"
    			}
    	
    	Alternatively, for two specified partitions, this field might look like the following:
    	
    		   "trees":{
		     "0":"((taxon1: 0.5, taxon2: 0.5):0.5),taxon3:0.5)",
		     "1":"((taxon1: 0.1, taxon2: 0.1):0.1),taxon3:0.1)"
		    	}


#### **`fits`** 

This field will contain information about each fitted model in the given analysis, and as such each method will return different fits. Most fit fields will contain the following fields:

+ **`Log Likelihood`**, the log likelihood of the fitted model
+ **`estimated parameters`**, the number of parameters estimated during likelihood optimization (i.e., not including empirically-determined parameters)
+ **`AIC-c`**, the [small-sample AIC](https://en.wikipedia.org/wiki/Akaike_information_criterion#AICc) for the fitted model
+ **`Rate distributions`**, the inferred rate distribution under the fitted model. Depending on the model, this field can refer to different rates. See each fit description for an explanation of the rates provided.


Within **`fits`**, all methods will contain a field **`Nucleotide GTR`**, and most will contain a field for **`Global MG94xREV`** (note that this is termed **`MG94xREV with separate rates for branch sets`** in methods RELAX and BUSTED, and termed **`Baseline MG94xREV`** in aBSREL). Each of these fields will contain the following additional fields:

+ **`Nucleotide GTR`**
	+ **`Equilibrium frequencies`**, a vector of nucleotide frequencies obtained empirically, in alphabetical order (A, C, G, T)
	+ **`Rate distributions`**, a dictionary of inferred nucleotide substitution rates under the GTR model. Note that, for all inferences, the rate `A->G` (`G->A`) is constrained to equal 1. 
+ **`Global MG94xREV`** (or analogous field in RELAX, BUSTED, aBSREL)
	+ **`Equilibrium frequencies`**, a vector of codon frequencies obtained using the [CF3x4 estimator](http://dx.doi.org/10.1371/journal.pone.0011230), in alphabetical order (AAA, AAC, AAG,..., TTT)
	+ **`Rate distributions`**, inferred $\omega$ rates under the fitted model. Content in this field is method-specific.
	

#### **`data partitions`**

This field provides information about the specified partitions for a given analysis. In this context, partition refers to the case where different sites evolve according to different trees. It does not refer to branch sets.

Keys enumerate partitions (starting from 0). Each partition contains the following fields:

+ **`name`**, an automatic name determined by HyPhy for the given partition.
+ **`coverage`**, a list of the sites to which the given partition corresponds.


#### **`branch attributes`**

This field provides information branch-level inferences. It contains a field for each partition (starting from 0) as well as an **`attributes`** field. Each partition's field further contains a dictionary for each node (taxa and internal nodes) in the data containing information about the branch. For each key seen per node, the **`attributes`** field defines its meaning, either **branch length** or **node label** (indicating meta information). 

For example, consider this (fake, for explanation purposes) example **`branch attributes`** field:

	"branch attributes":{
		   "0":{
		     "Node0":{
		       "Nucleotide GTR":0,
		       "Global MG94xREV":0
		      },
		     "Node1":{
		       "Nucleotide GTR":0.1866611825064384,
		       "Global MG94xREV":0.1982719556638508
		      },
		     "taxon1":{
		       "original name": "taxon1",
				"Nucleotide GTR":0.0371579129290541,
		       "Global MG94xREV":0.03929183706601039
		      },
		     "taxon2":{
		       "original name": "taxon2",
		       "Nucleotide GTR":0.01588385857974938,
		       "Global MG94xREV":0.01711781392713551
		      }
		      "taxon3":{
       		"original name":"taxon!!!3~~",
       		"Nucleotide GTR":0.3679870611263812,
       		"Global MG94xREV":0.4073912756908664
       	  }
      		},
		   "attributes":{
		     "original name":{
		       "attribute type":"node label",
		       "display order":-1
		      },
		     "Nucleotide GTR":{
		       "attribute type":"branch length",
		       "display order":0
		      },
		     "Global MG94xREV":{
		       "attribute type":"branch length",
		       "display order":1
		      }
		    }
		}

Here, we see a single partition (0) with two internal nodes (Node0, Node1) and three tips (taxon1, taxon2, taxon3). All of these nodes contain the keys **"Nucleotide GTR"** and **"Global MG94xREV"** associated with numerical values. Looking into the **`attributes`** dictionary, we see that these keys correspond to the **`attribute type`** "branch length". Therefore, the values present in each node's dictionary represent the inferred branch length at that node under the given model. 
We also see the key **`original name`** for only nodes which are *tips*. This attribute, recorded as a "node label" in **`attributes`**, provides the original taxon name provided to HyPhy. In the event that there are forbidden characters in the provided name (i.e. for taxon3), HyPhy maps this forbidden name to an acceptable name. The original provided name will be recorded as an attribute in the node's dictionary.

#### **`timers`**

This field provides the run times, including total execution time (**`Total time`**), of different stages in model fitting. Each method will report the total time as well as times for critical fitting stages specific to the method.

### BUSTED

This section details JSON fields which are specific to BUSTED, and further clarifies the contents of shared fields as they appear in BUSTED.

#### **`background`**

This field simply contains the value **0** or **1** indicating if all nodes are considered as test ("foreground"), or if specific test/background sets have been specified. **0** indicates  that all branches are test, and **1** indicates that there are separate test and background lineages.

#### **`tested`**

This field indicates whether each node (taxon and internal node) belongs to either the "test" or "background" branch sets. If multiple partitions were specified, then there will be a dictionary for each partition, beginning from 0.

#### **`test results`**

This field reports the likelihood ratio test statistic (**`LRT`**) and P-value (**`p-value`**) obtained under the BUSTED test for gene-wide episodic selection.

#### **`fits`**

In BUSTED, this field contains either 3 or 4 model fits:

+ **`"Nucleotide GTR"`**, whose contents are described above in the section **Shared fields**
+ **`"MG94xREV with separate rates for branch sets"`**, the MG94xREV fit in BUSTED. 
	+ **`Rate Distributions`** reports the branch-set--wide inferred $\omega$ ratio. This field will contain either one or two keys (depending on if test and background were specified, or just test). For example, this field would contain the following contents for an analysis with test and background specified, where each list representes **[dN, dS]** (as BUSTED does not consider synonymous rate variation, dS=1 in all cases):

	
		    "Rate Distributions":{
	       		"non-synonymous/synonymous rate ratio for *background*":[
	        			[0.5210400433507286, 1]
	        		],
	       		"non-synonymous/synonymous rate ratio for *test*":[
	        			[0.434676603885773, 1]
	        		]
	      	 	}

+ **`"Unconstrained model"`**, the fitted BUSTED alternative model that allows for positive selection in test branches.
	+ **`Rate Distributions`** reports the three-rate $\omega$ distribution inferred for the test lineages, as well as the background lineages if they were specified. Values for each rate category (numbered 0, 1, 2) include the inferred rate (**`omega`**) and the inferred proportion of sites evolving at this rate (**`proportion`**).

+ **`"Constrained model"`**, the fitted BUSTED null model that disallows positive selection in test branches. Note that this field will only appear in the JSON **if there was evidence suggetive of selection in the earlier unconstrained model fit**. If, for example, the unconstrained model did not detect a proportion of sites with $\omega > 1$, BUSTED will skip the null fit and conclude that there is no evidence for selection in the test branches.
	+ **`Rate Distributions`** reports the three-rate $\omega$ distribution inferred for the test lineages, as well as the background lineages if they were specified. It follows the same format as does the corresponding field in **`"Unconstrained model"`**. 


#### **`branch attributes`**