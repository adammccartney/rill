#!/usr/bin/env python3
#
# (One) bit-flip erosion on given filenames
#
# (c)2020 grrrr.org
# for Rotting sounds (FWF AR445-G24)

from glob import glob
import os
import sys
from collections import OrderedDict
import time
import random

def getfilenames(filenames, verbosity=0):
    "Retrieve file names"
    return sum(map(glob, filenames), [])


def selectbit(filenames, verbosity=0):
    "Get bit lengths"
    files = OrderedDict((fn, os.path.getsize(fn)*8) for fn in filenames)
    totalbits = sum(files.values())

    if verbosity:
        print(f"Files: {len(files)}, total bits: {totalbits}", file=sys.stderr)

    bitix = random.randint(0, totalbits-1)

    for fn,s in files.items():
        if bitix < s:
            return fn, bitix
        bitix -= s
        
    raise RuntimeError("Can not happen")


def bitflip(fn, bitix, verbosity=0):
    "Flip bit in file {fn} at position {bitix}"
    with open(fn, 'br+') as f:
        f.seek(bitix//8)
        fb = f.read(1)
        b = fb[0]
        b ^= 1<<(bitix%8)
        fb = bytes((b,))
        assert len(fb) == 1
        f.seek(bitix//8)
        f.write(fb)


def erode(filenames, verbosity=0):
    "Erode one bit within the totality of filenames given"
    
    # retrieve filenames from list (with wildcards)
    fns = getfilenames(filenames, verbosity=verbosity)
    if verbosity >= 2:
          print(f"Files to erode: {fns}", file=sys.stderr)
    
    # select one bit: filename and index
    fn, bitix = selectbit(fns, verbosity=verbosity)
    if verbosity:
          print(f"Flipping {fn}, bit {bitix}", file=sys.stderr)
          
    # flip that bit
    bitflip(fn, bitix, verbosity=verbosity)
    # return changed file    
    return fn


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("files", type=str, nargs='+', help="Files to consider for erosion, with wildcards")
    parser.add_argument("-v", "--verbosity", action="count", help="Increase verbosity (default=%(default)d)", default=0)
    args = parser.parse_args()
    # erode files
    fn = erode(args.files, verbosity=args.verbosity)
    # print out eroded file
    print(fn)
