#!/bin/bash

if [ "`which timeout`" != "" ]; then
	TIMEOUT="timeout 1m"
else
	TIMEOUT=
fi

LANG=C $TIMEOUT xelatex $1
