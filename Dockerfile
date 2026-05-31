# Dockerfile for rill erosion runtime environment
# Based on TeX Live full installation with additional dependencies for erosion

FROM docker.io/texlive/texlive@sha256:91f9d3b4bf623022432c4838940e94bf2923e6f655575c412cd3c2df1a543777

# Install required dependencies: LilyPond, Python/uv, git, make, and other tools
RUN apt-get update && apt-get install -y \
    curl \
    lilypond \
    make \
    zip \
    python3 \
    python3-pip \
    python3-venv \
    git \
    rsync \
    && rm -rf /var/lib/apt/lists/*

# Install uv (Python package manager)
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

# Set up working directory
WORKDIR /src

# Copy project files
COPY . /src/

# Default command - will be overridden by docker-compose
# User creation and venv setup happens at runtime to match host UID/GID
CMD ["bash"]
