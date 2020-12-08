#!/bin/bash

trap 'rm -f "$TMPFILE"' EXIT

TMPFILE=$(mktemp) || exit 1

LANG=C timeout 1m lilypond $1 2>$TMPFILE

res=`grep -E "warning: (barcheck failed|strange time signature found)" $TMPFILE`

# test for detected error
test "$res" == ""
