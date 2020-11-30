#!/bin/bash

###############################################################################

EROSION=${1:-./erosion/erosion.py}

if [ ! -f "${EROSION}" ]; then
    echo "Erosion script must be given as first argument."
    exit -1
fi

ROOT=${2:-.}

if [ "${ROOT}" == ""  -o ! -d "${ROOT}" ]; then
    echo ".git project root folder must be given as second argument."
    exit -1
fi

RILL="$ROOT/rill"

FILES="${RILL}/materials/*.py ${RILL}/materials/*/*.py ${RILL}/segments/*.py ${RILL}/segments/*/*.py"

BUILDDIR="${RILL}/builds/letter-portrait/"

if [ `uname` == Linux ]; then
    TIMEOUT="timeout 3m"
else
    # no timeout on MacOS
    TIMEOUT=""
fi
    
BUILD="make -C ${BUILDDIR} make -l 4"

CHECKS="${BUILDDIR}/score.pdf"

COMMIT="git commit -m 'Automatic erosion'"
PUSH="git push"
RESTORE="git restore ${ROOT}"

SLEEP="sleep 5"

###############################################################################

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function ctrl_c() {
    echo "Ctrl-C - Restoring working folder"
    ${RESTORE}
}

###############################################################################

# infinite loop of erosion
while true; do
    
    # Erode one file of the list, store the filename
    fn="`${EROSION} ${FILES}`"
    echo "Eroded file ${fn}"

    if [ $? -ne 0 ]; then
        echo "Erosion failed"
        exit -2
    fi

    # Execute build process with time limit
    ${TIMEOUT} ${BUILD}
    
    if [ $? -eq 0 ]; then
        echo "Build successful"
        ok=1
        
        # check for all files in $CHECKS
        for f in ${CHECKS}; do
            if [ ! -f "$f" ]; then
                ok=0
                break;
            fi
        done
    else
        ok=0
    fi
    
    # if build is ok, commit change to git
    if [ ${ok} -eq 1 ]; then
        echo "Erosion successful: $fn"
        # Commit changes by erosion to repository
        ${COMMIT} ${fn} && ${PUSH}        
    else
        # Undo changes to repository
        ${RESTORE}
    fi
    
    # wait a little
    ${SLEEP}
done
