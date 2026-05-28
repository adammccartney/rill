# TASK: modernize the current python project
+ migrate from "setup.py" to "pyproject.toml" file that can be used to
  handle the project management
+ assume that a user will use "uv" for managing the project, i.e. setup of the
  virtual environment 
+ be explicit about the python version ... the requirements specify needing
  abjad==3.1, this may mean tying the project to a very specific python version,
  because python is what it is

# TASK: add a "docker-score" target to the makefile
+ In addition to the python project management above, there are a number of
  undeclared dependencies, in particular it is pretty reliant on a (presumably
  quite large) latex installation. I know that the score was previously build on
  a debian (and possibly fedora) distribution that used something like the
  "latex-full" package (deb / rpm) to handle the latex dependencies.
+ I'd like to make these dependencies explicit by declaring the build
  environment in the form of a docker container. Use something like the
  following blueprint. Also ensure that the docker container has what is
  required to run a uv based setup of the virtual environment as described
  above.

```
# --------------------------------
# go build container
# --------------------------------
docker-go:
	@echo "Building go binary inside go container..."
	docker run --rm -it \
		-v $(PWD):/src \
		-w /src \
		docker.io/golang:1.25.10-trixie \
		bash -c 'set -e; apt-get install -y make; make cvmfs-prometheus-wrapper'
```
