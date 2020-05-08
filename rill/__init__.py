import distutils.version
import platform

if not (
    distutils.version.LooseVersion("3.7")
    < distutils.version.LooseVersion(platform.python_version())
):
    raise ImportError("Requires Python 3.7.")
del distutils
del platform
from ins_wasser.tools import *
from ins_wasser.tools import MarkupLibrary as markup
from ins_wasser.materials.instruments.definition import instruments
from ins_wasser.materials.margin_markups.definition import margin_markups
from ins_wasser.materials.metronome_marks.definition import metronome_marks
from ins_wasser import segments
