
import copy
import pathlib

import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony

from rill.tools.accents import tenuto as tenuto
from rill.tools.barlines import barline as barline
from rill.tools.clef import clef as clef
from rill.tools.FuzzyHarmony import Diad as Diad
from rill.tools.FuzzyHarmony import LegatoArpeggio as LegatoArpeggio
from rill.tools.material_methods import transpose_segment as transpose_segment
from rill.tools.tremolo import tremolo as tremolo

from abjad import NamedPitch as NamedPitch
from typing import List

#####################
# Setting up segment ### [B] ###
#####################

this_current_directory =  pathlib.Path(__file__).parent 
score =rill.ScoreTemplate()
score_template = score()

segment_maker = rill.SegmentMaker(
                                _lilypond_file=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=rill.build_path,
                                markup_leaves=False,
                                segment_name='segment_B',
                                rehearsal_mark=2,
                                tempo=((1, 4), 50),
                                )

segment_maker.metronome_marks = [
        (0, rill.metronome_marks['50'], 5),
        ]

time_signatures= [(4, 4)] + [(3, 4)] + [(3, 4)] + [(4, 4)] + [(3, 4)] + [(3,4)]
segment_maker.time_signatures = time_signatures

#-----------------/________________________
# Pitch Material /  Constants for section /
#_______________/------------------------/


# ----- Diads
# -- sequences of notes for arpeggios


# -------------- Woodwinds ----------------------/
#-----------------------------------------------/

# Flute1
#-----------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Flute1"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = []


# Flute2
#-----------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Flute2"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = []


# Flute3
#-----------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Flute3"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = []



# Bbclarinet
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Bbclarinet1"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = []

# Vibraphone 
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Vibraphone"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = []

#----------------Strings -------------------------/
# Violin1
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Violin1"


rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = []

# Violin2
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Violin2"


rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = []

# Violin3
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Violin3"


rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = []


# Violin4
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Violin4"


rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = []


# Violin5
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Violin5"


rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = []


# Violin6
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Violin6"


rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = []


# Violin7
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Violin7"


rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = []



# Viola
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Viola"

rhythm_definition.notes = [
        ("r1"),
        ("r2."),
        ("r2."),
        ("r1"),
        ("r2."),
        ("r2."),
]

rhythm_definition.dynamics = []

rhythm_definition.markup = []

# ---------------------------------------RUN SEGMENT

lilypond_file = segment_maker.run()
