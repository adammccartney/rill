import distutils.version
import platform

if not (
    distutils.version.LooseVersion("3.7")
    < distutils.version.LooseVersion(platform.python_version())
):
    raise ImportError("Requires Python 3.7.")
del distutils
del platform

from rill.tools import *
from rill.tools import MarkupLibrary as markup
from rill.materials.instruments.definition import instruments
from rill.materials.pitch.definition import (
                                    bass_pitches, 
                                    tetrads,
                                    pentads,
                                    transposition_lookup,
                                    scale_lookup,
                                    melody_lookup,
                                    vln_str_diads,
                                    pure_maj_third_diads,
                                   )
from rill.materials.metronome_marks.definition import  metronome_marks
from rill import segments
