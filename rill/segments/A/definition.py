import pathlib

import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony
from rill.tools.PhraseMaker import PhraseOutflow as PhraseOutflow
from rill.tools.PhraseMaker import PhraseStream as PhraseStream

from abjad import NamedPitch as NamedPitch
from typing import List
# call to segment maker contains:
    # Set instruments
    # Set voice names
    # set score_template
    # set time signatures
    # Set path for output
    # set tempo
    # set midi
    # 

#####################
# Setting up segment ### [A] ###
#####################

this_current_directory =  pathlib.Path(__file__).parent 
test_build_path = rill.build_path 
score = rill.ScoreTemplate()
score_template = score()

segment_maker = rill.SegmentMaker(
                                _lilypond_file=None,
                                _phrase_outflows=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=test_build_path,
                                segment_name='A',
                                tempo=((1, 4), 50),
                                time_signatures=([(4, 4)] * 20),
                                )


#--------------/
#   Violin    /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Violin'

rhythm_definition.notes = [
        ("c'", abjad.Duration(1, 1), rill.tremolo(32)),
        ("d'", abjad.Duration(2, 1)),
        ("e'", abjad.Duration(1, 4)),
        ("f'", abjad.Duration(3, 4)),
        ]

rhythm_definition.dynamics = [
        (0, abjad.Dynamic('ppp'), 2.5),
        (1, abjad.Dynamic('f')),
        (3, abjad.Dynamic('mf')),
       ]

rhythm_definition.markup = [
        (0, rill.markup.tasto(), 1.5),
        (1, rill.markup.pont()),
        (2, rill.markup.flaut_pont()),
        ]


#-----------------/
#   MonoSynth    /
#_______________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Monosynth'


#-------------------PolySynth----------------#


## Set up material for segment 

cmin7_6 = rill.FuzzyHarmony('bf_ii', abjad.PitchSegment("ef g c' bf")) # cmin7/e
cmin7_64 = rill.FuzzyHarmony('bf_ii', abjad.PitchSegment("g bf ef' c'")) 
cmin7_42 = rill.FuzzyHarmony('bf_ii', abjad.PitchSegment("bf c' g ef"))   
cmin7 = rill.FuzzyHarmony('bf_ii', abjad.PitchSegment("c' bf ef g"))

cm7_fz_hrmns = [cmin7_6, cmin7_64, cmin7_42, cmin7]
empty_list: List[any] = []
gm7_fz_hrmns = rill.transpose(cm7_fz_hrmns, empty_list, 19)


# Stream material into containers
#--------------/
# RH_I  /
#____________/



rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'LH_I'

gm7_diads = rill.make_diads(gm7_fz_hrmns, interval_doubling='d3')

#--------------/
# LH_I  /
#____________/
rhythm_definition.notes = [
        ("ef", abjad.Duration(1, 2), rill.tremolo(32), rill.tie()),
        ("ef g", abjad.Duration(1, 2), rill.tie()),
        ("ef g", abjad.Duration(1, 4), rill.tie()),
        ("ef g c'", abjad.Duration(3, 4), rill.tie()),
        ("ef g c' bf", abjad.Duration(1), rill.tie()),
        ("ef g c' bf", abjad.Duration(1, 2)), 
        ("r2"),
        ]

cm7_diads = rill.make_diads(cm7_fz_hrmns, interval_doubling='d5')

lilypond_file = segment_maker.run()
