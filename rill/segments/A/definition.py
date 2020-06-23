import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony
from rill.tools.FuzzyHarmony import invert_up as invert_up

from rill.tools.PhraseMaker import make_four_bar_phrase as make_four_bar_phrase

###########
### [A] ###
###########

segment_maker = rill.SegmentMaker(
        name='A'
        )

time_signatures = 20 * [(4, 4)]
segment_maker.time_signatures = time_signatures

###########################
# CONSTANTS for SEGMENT A #
###########################

durations = [
        abjad.Duration(2, 4),
        abjad.Duration(3, 4),
        abjad.Duration(3, 4),
        abjad.Duration(6, 4),
        abjad.Duration(2, 4),
        ]

harmony_third = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1) # cmin7/e
harmony_fifth = FuzzyHarmony('bf_ii', abjad.PitchSegment("g' bf' c'' ef''"), 2) 
harmony_seventh = FuzzyHarmony('bf_ii', abjad.PitchSegment("bf' c'' ef'' g''"), 3)
harmony_root = FuzzyHarmony('bf_ii', abjad.PitchSegment("c'' ef'' g'' bf''"), 0)

#--------------/
#   Violin    /
#____________/


# Make material

phrase_one = make_four_bar_phrase(harmony_third, durations)
phrase_two= make_four_bar_phrase(harmony_fifth, durations)
phrase_three = make_four_bar_phrase(harmony_seventh, durations)
phrase_four = make_four_bar_phrase(harmony_root, durations)

## Attach to score

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Violin'

rhythm_definition.notes = [
                          phrase_one, 
                          phrase_two, 
                          phrase_three,
                          phrase_four,
                          ]


#-----------------/
#   MonoSynth    /
#_______________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'MonoSynth'

rhythm_definition.notes = [phrase_one]



#-------------------PolySynth----------------#

#--------------/
# RH_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'RH_I'

rhythm_definition.notes = [phrase_one]


#---------------/
# RH_II  /
#_____________/
#
#rhythm_definition = segment_maker.define_rhythm()
#rhythm_definition.instrument_name = 'RH_II'
#
#rhythm_definition.notes = [
#        'r1',
#        'r1',
#        'r1',
#        'r1',
#        'r1',
#        ]
#
#--------------/
# LH_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'LH_I'

rhythm_definition.notes = [
                          phrase_one, 
                          phrase_two, 
                          phrase_three,
                          phrase_four,
                          ]

rhythm_definition_dynamics = [
        (0, abjad.Dynamic('pp')),
        ]

#---------------/
# LH_II  /
#_____________/

#rhythm_definition = segment_maker.define_rhythm()
#rhythm_definition.instrument_name = 'LH_II'
#
#rhythm_definition.notes = [
#        (pitch_list[0], abjad.Duration(1)),
#        (pitch_list[0], abjad.Duration(1)),
#        (pitch_list[1], abjad.Duration(1)),
#        (pitch_list[3], abjad.Duration(1)),
#        (pitch_list[2], abjad.Duration(1)),
#        ]
#
#--------------------------------------------#
