#!/bin/bash
#
# Script to run all defintition.py scripts in every subtree of the segments dir
#

for SEGMENT_NAME in A B C D E F G H I J K L

do
    echo "building $SEGMENT_NAME"
    cd "segment_$SEGMENT_NAME"
    echo $(pwd)
    echo $(python ./definition.py &)
    cd ..
done

exit 0
