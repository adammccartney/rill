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

# TASK: make the docker build reproducible (to some degree)
+ Make sure we are tied to a specific version of the image, ideally with a sha
  checksum

# TASK: create runtime environment to generate "erosions"


+ Analyze the "erosion.sh" script to understand the logic of an erosion.
  Do not take any other action before completing the analysis.
  Note there are specific details from the erosion.sh script that are relevant
  for the dockerfile, in particular the working directory should be derived from
  the logic in the erosion.sh script.
  Also we need to take care to set up the mount point that holds the eroded
  scores. Probably it's the easiest thing to just create a "data" directory in
  the pwd where the docker compose is run. Open to other suggestions here
  though.

+ create a `Dockerfile` that holds some key info about creating the container. 
  - image: 	docker.io/texlive/texlive@sha256:91f9d3b4bf623022432c4838940e94bf2923e6f655575c412cd3c2df1a543777 
  - environment setup (note the dependencies LaTeX, LilyPond, Python/uv, git,
    make)
```Dockerfile
RUN apt-get update && apt-get install -y curl lilypond make zip python3 python3-pip python3-venv \
 && curl -LsSf https://astral.sh/uv/install.sh | sh \
 && export PATH="$$HOME/.local/bin:$$PATH"; \
 && rm -rf .venv \
 && uv venv \
 && . .venv/bin/activate \
    uv pip install -e .; \
```

+ Create a `docker-compose.yml` to run "erosions" in a long running container

+ Note that the docker-score target was essentially serving it's function.
  That is for creating the "original" score ... before any erosion takes place
  It's working for that use case, so do not make any updates to that target.
  It's preferable to create a new target "docker-erosion"
