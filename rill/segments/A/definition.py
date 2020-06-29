import os
import pathlib
import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony
from rill.tools.FuzzyHarmony import invert_up as invert_up
import rill.tools.PhraseMaker as PhraseMaker
from rill.tools.SegmentMaker import PhraseCatcher


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

test_current_directory = pathlib.Path(__file__).parent
test_build_path = (pathlib.Path(__file__).parent/".."/"build").resolve()
score = rill.ScoreTemplate()
segment_maker = rill.SegmentMaker()
segment_maker.set_current_directory(test_current_directory)
segment_maker.set_build_path(test_build_path)
segment_maker.set_score_template(score)
segment_maker.set_name('A')
segment_maker.set_time_signatures([(4, 4)] * 20)
print(segment_maker.score)

###########################
# CONSTANTS for SEGMENT A #
###########################

#--------------/
#   Violin    /
#____________/


# Make material


## Attach to score

#rhythm_definition = segment_maker.define_rhythm()
#rhythm_definition.instrument_name = 'Violin'



#-----------------/
#   MonoSynth    /
#_______________/

#rhythm_definition = segment_maker.define_rhythm()
#rhythm_definition.instrument_name = 'MonoSynth'




#-------------------PolySynth----------------#

#--------------/
# RH_I  /
#____________/

#rhythm_definition = segment_maker.define_rhythm()
#rhythm_definition.instrument_name = 'RH_I'

#rhythm_definition.notes = [phrase_one]


#--------------/
# LH_I  /
#____________/

caught_phrases = []
harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1) # cmin7/e
container = abjad.Container()
durations = [2, 3, 3, 6, 2]
denominator = 4
divisions = [(4, 4)] * 5
pitches = harmony.pitch_list
phrase_one = PhraseMaker(container)
phrase_one.make_phrase(durations, denominator, divisions, pitches)

# make phrase two
harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("g' bf' c'' ef''"), 2) 
container = abjad.Container()
pitches = harmony.pitch_list
phrase_two = PhraseMaker(container)
phrase_two.make_phrase(durations, denominator, divisions, pitches)
caught_phrases.append(container)

# make phrase three
harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("bf' c'' ef'' g''"), 3)   
container = abjad.Container()
pitches = harmony.pitch_list
phrase_three = PhraseMaker(container)
phrase_three.make_phrase(durations, denominator, divisions, pitches)
caught_phrases.append(container)

 # make phrase four
harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("c'' ef'' g'' bf''"), 0)
container = abjad.Container()
pitches = harmony.pitch_list
phrase_four = PhraseMaker(container)
phrase_four.make_phrase(durations, denominator, divisions, pitches)
caught_phrases.append(container)

phrases = PhraseCatcher(
                        instrument_name = 'LH_I',
                        phrases = caught_phrases
                        )    

#segment_maker.route_phrases(phrases)
#lilypond_file = segment_maker.run() 
