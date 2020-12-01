#!/bin/bash

# tag_script.sh
# Simple shell script to generate a version tag for the score front page

branch=$(git branch --show-current)
SHA=$(git rev-parse --short HEAD)
echo $branch $SHA
