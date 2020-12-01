#!/bin/bash

# tag_script.sh
# Simple shell script to generate a version tag for the score front page

touch ./tag_script_output.tex
branch=$(git branch --show-current)
SHA=$(git rev-parse --short HEAD)
echo $branch $SHA > ./tag_script_output.tex

exit 0
