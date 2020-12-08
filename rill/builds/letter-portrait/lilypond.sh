#!/bin/bash

trap 'rm -f "$TMPFILE"' EXIT

TMPFILE=$(mktemp) || exit 1
echo $TMPFILE

LANG=C lilypond $1 >/dev/null 2>$TMPFILE

res=`grep -E "warning: (barcheck failed|strange time signature found)" $TMPFILE`

# test for detected error
test "$res" == ""
