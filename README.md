rill (erosion)
==============
[![Build Status](https://travis-ci.org/adammccartney/rill.svg?branch=master)](https://travis-ci.org/adammccartney/rill)

For ensemble (4 Flutes, 1 Bb Clarinet, 1 Vibraphone, 8 Violins, 1 Viola)

Written by [Adam McCartney](https://admccartney.mur.at/), eroded by [Thomas Grill](http://grrrr.org)

A commission of the [Rotting sounds](http://rottingsounds.org) project of artistic research at the mdw – University of Music and Performing Arts Vienna, 2020–2021. 
Funded by the [Austrian Science Fund](http://www.fwf.ac.at), project number AR445-G24.


Instructions:
-------------

+ Install Python package `rill` and its dependencies, by running `python setup.py install` or `pip install .`. If an erosion process shall be started, install as editable instead: `pip install -e .`

+ Building the score: From the top-level folder, run `make`.

+ Erosion process: 
	- Create and checkout a new branch by running, e.g., `git branch erosion_666 && git checkout erosion_666`.
	
	- From the top-level folder, run `erosion.sh`.
	
	- On each successful build, a new `score.pdf` will be placed in the subfolder `rill/builds/letter-portrait`.
