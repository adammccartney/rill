.PHONY: all clean docker-score

all:
	make -C rill/builds/letter-portrait

clean:
	make -C rill/builds/letter-portrait clean

# --------------------------------
# docker-score: Build score inside docker container
# --------------------------------
# This target builds the score inside a Docker container with all required
# dependencies (LaTeX, LilyPond, Python/uv). The container mounts the current
# directory and runs the make command to build the score.
docker-score:
	@echo "Building score inside docker container with full LaTeX and LilyPond..."
	docker run --rm -it \
		-v $(PWD):/src \
		-w /src \
		docker.io/texlive/texlive:latest-full \
		bash -c 'set -e; \
			apt-get update && apt-get install -y curl lilypond make zip python3 python3-pip python3-venv; \
			curl -LsSf https://astral.sh/uv/install.sh | sh; \
			export PATH="$$HOME/.local/bin:$$PATH"; \
			rm -rf .venv; \
			uv venv; \
			. .venv/bin/activate; \
			uv pip install -e .; \
			make -C rill segments; \
			make -C rill/builds/letter-portrait music.pdf; \
			make -C rill/builds/letter-portrait'
