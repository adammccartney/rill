rill (erosion)
==============

For ensemble (4 Flutes, 1 Bb Clarinet, 1 Vibraphone, 8 Violins, 1 Viola)

Written by [Adam McCartney](https://admccartney.mur.at/), eroded by [Thomas Grill](http://grrrr.org)

A commission of the [Rotting sounds](http://rottingsounds.org) project of artistic research at the mdw – University of Music and Performing Arts Vienna, 2020–2021. 
Funded by the [Austrian Science Fund](http://www.fwf.ac.at), project number AR445-G24.

For more detailed information on the score and how the "erosion" process works,
see the paper presented at the ICMC 2022.[^1]


Instructions:
-------------

The recommended way to build the score and generate "erosions" is to use
the docker environments provided. There are two targets specified in the
makefile:

## Generate original score

`make docker-score` will run a once-off command inside a container that will result
in a generated pdf of the original score.

## Start a long running process to generate a series of "eroded" scores

`make docker-erosion` will launch a long running job that performs a
binary erosion of the source files that are used to create the typeset
score. The idea of this erosion process is that new editions of the
score are produced and committed to a dedicated branch in the git
repository. Note that each successful erosion will flip a single bit.

### Keep changes locally on custom branch

```
EROSION_BRANCH=erosion_secunda make docker-erosion
```

### Push changes to remote branch

Assumes push access to remote, this will create and push to a branch
called "erosion_prima" by default.

```
PUSH_REMOTE=TRUE make docker-erosion
```

## Development setup (legacy)

+ This project uses [uv](https://github.com/astral-sh/uv) for Python package management.

+ Set up the virtual environment and install dependencies:
  ```
  uv sync
  ```

+ For development/editable install:
  ```
  uv sync --dev
  ```

+ Alternatively, using pip:
  ```
  pip install .
  ```
  Or for editable install:
  ```
  pip install -e .
  ```

+ Building the score: From the top-level folder, run `make`.

+ Erosion process: 
	- Create and checkout a new branch by running, e.g., `git switch -c erosion_666`.
	
	- From the top-level folder, run `./erosion.sh`.
	
	- On each successful build, a new `score.pdf` will be placed in the subfolder `rill/builds/letter-portrait`.


[^1]: McCartney, Adam; Grill, Thomas: The effects of binary erosion on music composition expressed as a notated score. In: Torre, Giuseppe (Hg.): Proceedings of the ICMC. San Francisco, USA: International Computer Music Association, Inc 2022, S. 200-205 <https://www.fulcrum.org/epubs/8910jx22c?page=212>.
