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
from rill.materials.instruments.definition import instruments
from rill.materials.pitch.definition import bass_pitches, tetrads
from rill import segments
