invgain
=======

[CASA](http://casa.nrao.edu/) task to invert solutions in a gain calibration table.

The application in mind is direction-dependent calibration, e.g. for peeling.

Latest version: 1.3 ([download here](https://github.com/chrishales/invgain/releases/latest))

Tested with: CASA Version 4.7.0

invgain is released under a BSD 3-Clause License (open source, commercially useable); refer to LICENSE for details.

Feedback regarding invgain is always welcome.

Installation
======

Download the latest version of the source files from [here](https://github.com/chrishales/invgain/releases/latest).

Place the source files into a directory containing your measurement set. Without changing directories, open CASA and type
```
os.system('buildmytasks')
```
then exit CASA. A number of files should have been produced, including ```mytasks.py```. Reopen CASA and type
```
execfile('mytasks.py')
```
To see the parameter listing, type
```
inp invgain
```
For more details on how invgain works, type
```
help invgain
```
Now set some parameters and press go!

For a more permanent installation, place the source files into a dedicated invgain code directory and perform the steps above. Then go to the hidden directory ```.casa``` which resides in your home directory and create a file called ```init.py```. In this file, put the line
```
execfile('/<path_to_invgain_directory>/mytasks.py')
```
invgain will now be available when you open a fresh terminal and start CASA within any directory.

Acknowledging use of invgain
======

invgain is provided in the hope that it (or elements of its code) will be useful for your work. If you find that it is, I would appreciate your acknowledgement by citing [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.163000.svg)](https://doi.org/10.5281/zenodo.163000) as follows (note the [AAS guidelines for citing software](http://journals.aas.org/policy/software.html)):
```
Hales, C. A. 2016, invgain, v1.3, doi:10.5281/zenodo.163000, as developed on GitHub
```
