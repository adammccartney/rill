import pathlib

import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony
from rill.tools.PhraseMaker import PhraseOutflow as PhraseOutflow
from rill.tools.PhraseMaker import PhraseStream as PhraseStream

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


rests = [None] * 10
breve = abjad.Duration(2, 1)

violin_rest_stream = PhraseStream(rests)
violin_rest_stream.durate_stream(breve)

phrase_outflow = segment_maker.stream_phrases(
                                        instrument_name = "Violin",
                                        streams = [violin_rest_stream],
                                       )

#-----------------/
#   MonoSynth    /
#_______________/

monosynth_rest_stream = PhraseStream(rests)
monosynth_rest_stream.durate_stream(breve)
phrase_outflow = segment_maker.stream_phrases(
                                        instrument_name = "Monosynth",
                                        streams = [monosynth_rest_stream],
                                       )

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


rh_durations = [
        abjad.Duration(2, 1), 
        abjad.Duration(2, 1), 
        abjad.Duration(2, 1), 
        abjad.Duration(4, 1),
        ]

gm7_diads = rill.make_diads(gm7_fz_hrmns, interval_doubling=None)

# first_rh_stream
rh_stream = PhraseStream(gm7_diads)
rh_stream.durate_stream(rh_durations)
rh_durated_stream = rh_stream.container
print("rh stream: ", rh_stream)


# second rh_stream

phrase_outflow = segment_maker.stream_phrases(
                                        instrument_name = "RH_I",
                                        streams = [rh_stream],
                                       )

#--------------/
# LH_I  /
#____________/

lh_durations = [
        abjad.Duration(4, 1), 
        #abjad.Duration(3, 2), 
        #abjad.Duration(3, 2), 
        #abjad.Duration(3, 1),
        #abjad.Duration(1, 1),
        ]


cm7_diads = rill.make_diads(cm7_fz_hrmns, interval_doubling='d5')

lh_stream = PhraseStream(cm7_diads)
print("lh_stream: " , lh_stream.phrases)
lh_stream.durate_stream(lh_durations)

lh_durated_stream = lh_stream.container
print("durated lh_stream: ", lh_stream.container)

phrase_outflow = segment_maker.stream_phrases(
                                        instrument_name = "LH_I", 
                                        streams = [lh_stream],
                                    ) 
#
lilypond_file = segment_maker.run()
