## Analysis list

> This is not a complete list, but the new analyses will be described here.
> Other places to look are [manuscript associated analyses](https://github.com/spond/pubs/),
> and the [GitHub boards](https://github.com/veg/hyphy/issues?q=)

### Contrast-FEL

For each site in a codon alignment, estimate whether or not dN/dS ratios
differ between sets of branches defined _a priori_. If the branches are associated with
different selective environments, this could be used to generate a list of sites that may
be evolving at different rates (under different selective pressures) in these environments.

- Outputs a list of sites where `test` branches have a statistically detectable difference
    in dN/dS from `reference` branches.
- Could be used to test for **differential** selection pressures, for example between
    host and recipient or individual anatomical compartments in HIV-1, or in between species
    with different phenotypes/traits.

[Further information](contrast-fel.md)

### FitMultiModel

For each alignment, FitMulti model fits five models, all extenstions of the Muse and Gaut (1994) codon model allowing for multiple instantaneous nucleotide changes within a codon to occur. Then pairwise likelihood ratio tests are performed between the models. This requires a codon alignment and a tree. 

- Output includes the rate estimates for each model, the LRT p values, and a list of sites that show strong preference for multiple hit models. 
- Can be used to determine the extent of multiple hits present in a data set.

[Further information](FitMultiModel.md)
