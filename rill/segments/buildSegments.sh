#!/bin/bash
#
# Script to run all defintition.py scripts in every subtree of the segments dir
#

declare -i REHEARSAL_MARK=1
for SEGMENT_NAME in A B C D E F G H I J K L

do  echo "building $SEGMENT_NAME"
    cd "segment_$SEGMENT_NAME"
    echo $(pwd)
    echo $(render_illustration "$SEGMENT_NAME" "$REHEARSAL_MARK" &)
    cd ..
    REHEARSAL_MARK=$((REHEARSAL_MARK + 1))
done

exit 0
