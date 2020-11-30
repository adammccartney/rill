#!/bin/bash

EROSION=${$1:-./erosion.py}

if [ ! -f "${EROSION}" ]; then
    echo "Erosion script must be given as first argument."
    exit -1
fi

ROOT=${$2:-.}

if [ "${ROOT}" == ""  -o ! -d "${ROOT}" ]; then
    echo ".git project root folder must be given as second argument."
    exit -1
fi

RILL="$ROOT/rill"

FILES="${RILL}/materials/*.py ${RILL}/materials/*/*.py ${RILL}/materials/*/*.ly ${RILL}/segments/*.py ${RILL}/segments/*/*.py"

BUILDDIR="${RILL}/builds/letter-portrait/"

BUILD="timeout 3m make -j8"
BUILD="make -C ${BUILDDIR} -j8"

CHECKS="${BUILDDIR}/score.pdf"

COMMIT="git commit -am 'Automatic erosion'"
RESTORE="git restore ${ROOT}"

SLEEP="sleep 5"


# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function ctrl_c() {
    echo "Ctrl-C - Restoring working folder"
    ${RESTORE}
}

while true; do
    ok=0
    
    fn="`${EROSION} -v ${FILES}`"
    echo $fn
    exit -1

    if [ $? -ne 0 ]; then
        echo "Erosion failed"
        exit -2
    fi

    ${BUILD}
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
    fi
    
    if [ ${ok} -eq 1 ]; then
        echo "Erosion successful: $txt"
        ${COMMIT}
        
        ${SLEEP}
    else
        ${RESTORE}
    fi
done
