import sys

segment_name=sys.argv[1]
rehearsal_mark=sys.argv[2]


segment_definition=f"""
import copy
from pathlib import Path

import abjad
import rill

from rill.tools.ScoreTemplate import ScoreTemplate

from typing import List

#####################
# Setting up segment ### [{segment_name}] ###
#####################

this_current_directory =  Path.cwd()
score = ScoreTemplate()
score_template = score()

segment_maker = rill.SegmentMaker(
                                _lilypond_file=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=rill.build_path,
                                markup_leaves=False,
                                segment_name='segment_{segment_name}',
                                rehearsal_mark={rehearsal_mark},
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


# Flute4
#-----------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Flute4"

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

# Violin8
#------------------------------------------------#
rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = "Violin8"


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
"""

output_file = open('definition.py', 'w')
output_file.write(segment_definition)
output_file.close()
