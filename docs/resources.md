Resources
===================

* [Tutorials](./tutorials/current-release-tutorial) for using HyPhy to infer selection with various methods. Detailed descriptions of these methods are available [here](./getting-started/#choosing-a-method-for-selection-inference).

* Book chapters and Powerpoints detailing HyPhy usage:
      * [Quantifying Natural Selection in Coding Sequences (2016)](resources-files/slides-selection-2016.pdf) 
      * [HyPhy Book: Estimating selection pressures on alignments of
coding sequences (2007)](resources-files/hyphybook2007.pdf)
      * [Introduction: Compartmentalization Detection](resources-files/compartmentalization_detection_ppt.pdf) 

* Getting help
      * See the current [Github Issues](https://www.github.com/veg/hyphy/issues) page for posting questions or searching queries from other users.
      * The retired (as of 2014) user forum is also available for viewing [here](http://www.hyphy.org/cgi-bin/hyphy_forums/YaBB.pl).
      * You can also tweet us at [@hyphy_software](https://www.twitter.com/hyphy_software) with quick questions.


### Labeling branches with phylotree
Labeling phylogenies is critical for branch-level analyses such as RELAX and BUSTED. These instructions detail the most basic usage of the [phylotree.js](http://veg.github.io/phylotree.js/) widget branch labeling functionality. 

1. Upload your phylogeny.
	+ Click the `Newick` dropdown menu at the top left of the site and choose your newick-formatted phylogeny to upload. Once uploaded, the phylogeny will load in the widget for labeling and/or manipulation.
2. In the text box next to the `Tag` dropdown menu, create all of your labels **before selecting/highlighting any branches**. 
	+ By default, the first label will always be named `Foreground`. This can be renamed with `Tag->Rename selection set` as desired. Be sure to click `Save` when finished renaming!
	+ To additional more labels, click `Tag->New selection set`. Each new selection set will be named, by default, `new_selection_name`. You can change this name now by directly typing the new name into the text field next to the `Tag` button. Again, click `Save` when finished renaming.
3. After all labels have been created, they will be visible in differently-colored text under the `Tag` dropdown menu. To select branches for a label, follow these steps:
	+ Click the label of interest in the `Tag` dropdown menu. The name of your chosen label will now be shown in the text box to the right of `Tag`. 
	+ Highlight and select any branches for this label. 
	+ When finished, navigate back to `Tag` to select the next label of interest, and select branches accordingly. Proceed until all selections are complete.

4. Export your labeled phylogeny by clicking the `Newick` dropdown menu and then `Export`. A text box with your labeled newick tree will appear. Copy and paste this newick tree as needed.


 