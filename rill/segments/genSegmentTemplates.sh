#!/bin/bash
#
# Script to generate all the empty segments for the score
#

declare -i REHEARSAL_MARK=1
for SEGMENT_NAME in A B C D E F G H I K L

do
    echo $(python ./genMusicData.py "$SEGMENT_NAME" &)
    cd "segment_$SEGMENT_NAME"
    echo $(python ./genDef_v1.py "$SEGMENT_NAME" "$REHEARSAL_MARK" &)
    cd ..
    REHEARSAL_MARK=$((REHEARSAL_MARK + 1))
done

exit 0
