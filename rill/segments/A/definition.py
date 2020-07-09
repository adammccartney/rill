import pathlib

import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony
from rill.tools.PhraseMaker import PhraseOutflow as PhraseOutflow
from rill.tools.PhraseMaker import PhraseStream as PhraseStream

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

score_template = rill.ScoreTemplate()
score = score_template()
#abjad.f(score)


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

###########################
# CONSTANTS for SEGMENT A #
###########################

## Set up material for segment 

durations = [
        abjad.Duration(1, 1), 
        abjad.Duration(3, 2), 
        abjad.Duration(3, 2), 
        abjad.Duration(3, 1),
        abjad.Duration(1, 1),
        ]

harmony_one = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef g bf c'"), 1) # cmin7/e
harmony_two = FuzzyHarmony('bf_ii', abjad.PitchSegment("g bf c' ef'"), 2) 
harmony_three = FuzzyHarmony('bf_ii', abjad.PitchSegment("bf c' ef' g'"), 3)   
harmony_four = FuzzyHarmony('bf_ii', abjad.PitchSegment("c' ef' g' bf'"), 0)

fuzzy_harmonies = [harmony_one, harmony_two, harmony_three, harmony_four]
empty_list = []
transposed_harmonies = rill.transpose_up_fifth(fuzzy_harmonies, empty_list)

print("transposed harmonies: ", transposed_harmonies)

progression = [
          harmony_one,
          harmony_two,
          harmony_three,
          harmony_four,
          ]

progression_fifth = transposed_harmonies


# Stream material into containers


#--------------/
# RH_I  /
#____________/


plagal = rill.make_diads(progression_fifth)

rh_stream = rill.make_stream(plagal)
rh_stream.durate_stream(durations)
rh_durated_stream = rh_stream.container


#Rests for beggining and end of segment
first_voice = abjad.Voice("r1 r2", name='z')
last_voice = abjad.Voice("r2 r1 r1", name='y')
updated_container = []
updated_container.append(first_voice)
for voice in rh_durated_stream[:-1]:
    updated_container.append(voice)
updated_container.append(last_voice)

print(updated_container)
rh_stream.container = updated_container

phrase_outflow = segment_maker.stream_phrases(
                                        instrument_name = "RH_I",
                                        streams = [rh_stream],
                                       )

#--------------/
# LH_I  /
#____________/


authentic = rill.make_diads(progression)

lh_stream = rill.make_stream(authentic)
lh_stream.durate_stream(durations)
lh_durated_stream = lh_stream.container

phrase_outflow = segment_maker.stream_phrases(
                                        instrument_name = "LH_I", 
                                        streams = [lh_stream],
                                    ) 
#
lilypond_file = segment_maker.run()
