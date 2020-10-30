import sys

import abjad
import rill

from rill.tools.MusicMaker import MusicMaker as MusicMaker
from rill.tools.MusicMaker import *

segment_name = sys.argv[1]
rehearsal_mark = sys.argv[2]


# Switch over segment_name to make assignments

# Test variables

test_pitches = rill.chord_voice["blue"][5][1:3]

test_ts_pairs = [(4, 4), (3, 4), (3, 4), (4, 4), (3, 4), (3, 4)]
test_counts = [1, 2, -3, 4]
test_denominator = 8
test_pitches = abjad.CyclicTuple(test_pitches)

tenuto_attachment_maker = rill.AccentAttachmentMaker(
    selector=abjad.select().logical_ties(),
    attachment=abjad.Articulation("tenuto")
)

staccato_attachment_maker = rill.AccentAttachmentMaker(
    selector=abjad.select().logical_ties(),
    attachment=abjad.Staccato()
)


# Need to assign variables for mMakerDataManager

class mMakerDataManager(object):
    """container class for music maker data"""

    def __init__(
            self,
            counts,
            denominator,
            pitches,
            attachment_makers
    ):
        self.counts = counts
        self.denominator = denominator
        self.pitches = pitches
        self.attachment_makers = attachment_makers


def factory(aClass, *pargs, **kargs):
    return aClass(*pargs, **kargs)


class mMakerGenerator(object):
    """Generates the code block for a MusicGenerator"""

    def __init__(
            self,
            counts,
            denominator,
            pitches,
            attachment_makers,
            time_signature_pairs,
    ):
        self.counts = counts
        self.denominator = denominator
        self.pitches = pitches
        self.attachment_makers = attachment_makers
        self.time_signature_pairs = time_signature_pairs

    def __call__(self, instrument_name):
        music_maker_obj = self._make_music_maker_object()
        music = music_maker_obj(self.time_signature_pairs)
        return music

    def _make_music_maker_object(self):
        music_maker_obj = factory(
            MusicMaker,
            self.counts,
            self.denominator,
            self.pitches,
            self.attachment_makers,
        )
        return music_maker_obj


def make_music_code_block(instrument_name):
    music_block = f"""
       {instrument_name}_rhythm_definition = segment_maker.define_rhythm()
       music = generator({instrument_name})
       {instrument_name}_rhythm_definition.notes = [music]
       {instrument_name}_rhythm_definition.instrument_name = \"{instrument_name}\"
       """
    return music_block


generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[tenuto_attachment_maker, staccato_attachment_maker],
    time_signature_pairs=test_ts_pairs,
)

music_code_block = make_music_code_block(instrument_name="Flute1")


segment_definition = f"""
import copy
import pathlib

import abjad
import rill

#####################
# Setting up segment ### [{segment_name}] ###
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
                                segment_name='segment_{segment_name}',
                                rehearsal_mark={rehearsal_mark},
                                tempo=((1, 4), 50),
                                )

segment_maker.metronome_marks = [
        (0, rill.metronome_marks['50'], 5),
        ]

time_signatures= [(4, 4)] + [(3, 4)] + [(3, 4)] + [(4, 4)] + [(3, 4)] + [(3,4)]
segment_maker.time_signatures = time_signatures



# -----------------/________________________
# Pitch Material /  Constants for section /
# _______________/------------------------/


# ----- Diads
# -- sequences of notes for arpeggios


# -------------- Woodwinds ----------------------/
# -----------------------------------------------/

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

# ----------------Strings -------------------------/
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
"""

output_file = open('definition.py', 'w')
output_file.write(segment_definition)
output_file.close()
