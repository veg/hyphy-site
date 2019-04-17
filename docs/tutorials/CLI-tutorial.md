Using HyPhy as a standard command line tool
=================================

As of version 2.4.0 HyPhy is a bonified command line tool.
An executable with key-word arguments, relative paths to files and sane defaults.
The interactive command line prompt is still avaialible if you prefer that (simply run `hyphy -i`).
This page provides some general information about using HyPhy as a command line tool; the older [command line prompt tutorial](./CL-prompt-tutorial.md) provides more details about each method.

Like any command line tool, to see the available options simply run `hyphy --help`.

Once you've [installed hyphy](../installation.md) run the method of your choice like so (we'll use SLAC for demonstration purposes):

`hyphy slac --alignment CD2.nex`

If you're tree is in a seperate file (not the same file as the alignment) add a `--tree` flag.

`hyphy slac --alignment CD2.fasta --tree CD2.newick`

Most methods require only an alignment and a tree.
Default values are used for any other options.
To see a list of the available options for a method run `hyphy <method_name> --help` (`hyphy slac --help` in our example).

Key word arguments and interactive prompts can be mixed by including `-i` before any key word arguments.
For example:  
`hyphy -i slac --alignment CD2.fasta --code Universal`  
Will begin a slac analysis with CD2.fasta using the universal genetic code and prompt you for all the non-specified options: a tree file, branch selection, number of samples for ancesteral state reconstruction, p-value.

Markdown formatted status indicators will be printed to stdout as the analysis runs.
Final results will be saved in a JSON-formatted file (saved in the same directory as the alignment file unless a `--output` argument is provided). This JSON results file can be uploaded at [vision.hyphy.org](http://vision.hyphy.org) for an interactive visualization of the results.

To see a list of the methods that can be run with a command line invocation run `hyphy --help`.