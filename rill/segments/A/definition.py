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


test_current_directory = rill.current_directory
test_build_path = rill.build_path 
score = rill.ScoreTemplate()
score_template = score()

segment_maker = rill.SegmentMaker(
                                _lilypond_file=None,
                                _phrase_outflows=None,
                                _score=score_template,
                                current_directory=test_current_directory,
                                build_path=test_build_path,
                                segment_name='A',
                                tempo=((1, 4), 50),
                                time_signatures=([(4, 4)] * 20),
                                )


#--------------/
#   Violin    /
#____________/


phrase_outflow = segment_maker.stream_phrases(
                                        instrument_name = "Violin",
                                        phrases = ["s1"],
                                       )

#-----------------/
#   MonoSynth    /
#_______________/

phrase_outflow = segment_maker.stream_phrases(
                                        instrument_name = "Monosynth",
                                        phrases = ["s1"],
                                       )

#-------------------PolySynth----------------#

###########################
# CONSTANTS for SEGMENT A #
###########################

## Set up material for segment 

durations = [
        abjad.Duration(1, 2), 
        abjad.Duration(3, 4), 
        abjad.Duration(3, 4), 
        abjad.Duration(3, 2),
        abjad.Duration(1, 2),
        ]

harmony_one = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1) # cmin7/e
harmony_two = FuzzyHarmony('bf_ii', abjad.PitchSegment("g' bf' c'' ef''"), 2) 
harmony_three = FuzzyHarmony('bf_ii', abjad.PitchSegment("bf' c'' ef'' g''"), 3)   
harmony_four = FuzzyHarmony('bf_ii', abjad.PitchSegment("c'' ef'' g'' bf''"), 0)

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

authentic = rill.make_diads(progression)
print("authentic: ", authentic)
plagal = rill.make_diads(progression_fifth)
print("plagal: ", plagal)


# Stream material into containers


#--------------/
# RH_I  /
#____________/

dry_phrase_stream = PhraseStream()
wet_phrase_stream = rill.order_material(
                                  authentic,
                                  durations,
                                  dry_phrase_stream,
                                  )
plagal_containers = wet_phrase_stream.containers
#print("plagal_containers: ", plagal_containers)
#
## Rests for beggining and end of segment
#first_container = abjad.Container("r1 r2")
#last_container = abjad.Container("r2 r1 r1")
#updated_containers = []
#updated_containers.append(first_container)
#for container in plagal_containers[:-1]:
#    updated_containers.append(container)
#updated_containers.append(last_container)
#
#wet_phrase_stream.containers = updated_containers
#phrase_outflow = segment_maker.stream_phrases(
#                                        instrument_name = "RH_I",
#                                        phrases = [wet_phrase_stream],
#                                       )
#
#--------------/
# LH_I  /
#____________/


#phrase_outflow = segment_maker.stream_phrases(
#                                        instrument_name = "LH_I", 
#                                        phrases = list_phrases,
#                                    ) 

#lilypond_file = segment_maker.run()
