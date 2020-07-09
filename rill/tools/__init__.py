from .FuzzyHarmony import (
        FuzzyHarmony,
        Progression,
        replace_and_make_new_progression,
        get_global_minima,
        invert_up,
        get_global_maxima,
        invert_down,
        )

from .material_methods import (
        get_pitch_classes,
        make_diads, 
        make_stream,
        transpose,
        )
from .PhraseMaker import (
        PhraseMaker,
        PhraseStream,
        PhraseOutflow,
        )
from .ScoreTemplate import ScoreTemplate
from .SegmentMaker import SegmentMaker
from .set_build_path import build_path

