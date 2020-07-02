import os
import pathlib
import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony
from rill.tools.FuzzyHarmony import invert_up as invert_up
import rill.tools.PhraseMaker as PhraseMaker
from rill.tools.PhraseMaker import PhraseStream as PhraseStream
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
test_build_path = (pathlib.Path(__file__).parent/".."/".."/"build").resolve()
score = rill.ScoreTemplate()
score_template = score()

segment_maker = rill.SegmentMaker(
                                  score=score_template,
                                  lilypond_file=None,
                                  phrase_catcher=None,
                                  current_directory=test_current_directory,
                                  build_path=test_build_path,
                                  segment_name='A',
                                  tempo=((1, 4), 50),
                                  time_signatures=([(4, 4)] * 20),
                                 )


###########################
# CONSTANTS for SEGMENT A #
###########################

durations = [
            abjad.Duration(1, 2), 
            abjad.Duration(3, 4), 
            abjad.Duration(3, 4), 
            abjad.Duration(3, 2),
            abjad.Duration(1, 2),
            ]

#--------------/
#   Violin    /
#____________/

#-----------------/
#   MonoSynth    /
#_______________/


#-------------------PolySynth----------------#

#--------------/
# RH_I  /
#____________/


#--------------/
# LH_I  /
#____________/

harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1) # cmin7/e
pitches = harmony.numbered_pitch_list
pitches.append(None)
phrases = []
phrase_stream = PhraseStream(phrases)
phrase_stream.make_extension(pitches, durations)

# make phrase two
harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("g' bf' c'' ef''"), 2) 
pitches = harmony.numbered_pitch_list
pitches.append(None)
phrase_stream.make_extension(pitches, durations)

# make phrase three
harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("bf' c'' ef'' g''"), 3)   
phrase_stream.make_extension(pitches, durations)

# make phrase four
harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("c'' ef'' g'' bf''"), 0)
phrase_stream.make_extension(pitches, durations)

list_phrases = phrase_stream.phrases
print(list_phrases)

#phrases = PhraseCatcher(
#                        instrument_name = 'LH_I',
#                        phrases = caught_phrases,
#                        )    
#
#routed_score = phrases(segment_maker.score)
#liypond_file = segment_maker.run()
#
