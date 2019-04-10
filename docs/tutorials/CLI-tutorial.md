Using HyPhy from the Command Line
=================================

As of version 2.4.0 HyPhy is a bonified command line tool.
An executable with key-word arguments, relative paths to files and sane defaults.
No more echoing in arguments from bash scripts.
Yes... We're excited too!

Like any command line tool, to see the available options simply run `hyphy --help`.

Once you've [installed hyphy](../installation.md) run the method of your choice like so (we'll use SLAC for demonstration purposes):

`hyphy slac --alignment CD2.nex`

If you're tree is in a seperate file (not the same file as the alignment) add a `--tree` flag.

`hyphy slac --alignment CD2.fasta --tree CD2.newick`

Most methods require only an alignment and a tree.
Default values are used for any other options.
To see a list of the available options for a method run `hyphy <method_name> --help` (`hyphy slac --help` in our example)

Markdown formatted status indicators will be printed to stdout as the analysis runs.
Final results will be saved in a JSON-formatted file (saved in the same directory as the alignment file unless a `--output` argument is provided). This JSON results file can be uploaded at [vision.hyphy.org](http://vision.hyphy.org) for an interactive visualization of the results.

To see a list of the methods that can be run with a command line invocation run `hyphy --help`.