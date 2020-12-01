#!/bin/bash

# tag_script.sh
# Simple shell script to generate a version tag for the score front page

branch=$(git status -b --porcelain | sed  's/^## \([a-zA-Z_0-9]*\)\.\.\.\(.*\)$/\1/' | head -n 1)
SHA=$(git rev-parse --short HEAD)
# replace _ by \_
echo ${branch}~${SHA} | sed -r 's/_/\\_/g'
