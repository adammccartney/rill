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

CLEAN="make -C ${BUILDDIR} clean"

BUILD="make -C ${BUILDDIR} -j8"

CHECKS="${BUILDDIR}/score.pdf"

GIT_ADD="git add"
GIT_COMMIT="git commit -m Erosion"
GIT_PUSH="git push"
GIT_RESTORE="git checkout ${ROOT}"

BRANCH="`git status -b --porcelain | sed  's/^## \([a-zA-Z_0-9]*\)\.\.\.\(.*\)$/\1/' | head -n 1`"

PUBLISH="rsync ${BUILDDIR}/score.pdf /mnt/archive/public/rill/score.${BRANCH}.pdf"

SLEEP="sleep 5"

###############################################################################

# trap ctrl-c and call ctrl_c()
trap ctrl_c INT

function ctrl_c() {
    echo "Ctrl-C - Restoring working folder"
    ${GIT_RESTORE}
}

###############################################################################

# infinite loop of erosion
while true; do

    # delete all files in $CHECKS
    for f in ${CHECKS}; do
        rm -f "$f"
    done
    # clean other files
    ${CLEAN}

    # Erode one file of the list, store the filename
    fn="`${EROSION} ${FILES}`"
    echo "Eroded file ${fn}"

    if [ $? -ne 0 ]; then
        echo "Erosion failed"
        exit -2
    fi

    # Execute build process with time limit
    ${TIMEOUT} ${BUILD} > /dev/null

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
        ${GIT_ADD} ${fn} && ${GIT_COMMIT} ${fn} && ${GIT_PUSH}
    else
        # Undo changes to repository
        ${GIT_RESTORE}
    fi

    test "${PUBLISH}" != "" && ${PUBLISH}

    # wait a little
    echo Waiting...
    ${SLEEP}
done
