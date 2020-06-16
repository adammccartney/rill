import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony


###########
### [A] ###
###########

segment_maker = rill.SegmentMaker(
        name='A'
        )

time_signatures = 20 * [(4, 4)]
segment_maker.time_signatures = time_signatures


# Create Pitch Material
harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1) # cmin7/e
pitches = harmony.pitches
pitch_list = []
for pitch in pitches:
    pitch_list.append(pitch.name)

#--------------/
#   Violin    /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Violin'

rhythm_definition.notes = [
        (pitch_list[0], abjad.Duration(1)),
        (pitch_list[0], abjad.Duration(1)),
        (pitch_list[1], abjad.Duration(1)),
        (pitch_list[3], abjad.Duration(1)),
        (pitch_list[2], abjad.Duration(1)),
        ]

#-----------------/
#   MonoSynth    /
#_______________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'MonoSynth'

rhythm_definition.notes = [
        (pitch_list[0], abjad.Duration(1)),
        (pitch_list[0], abjad.Duration(1)),
        (pitch_list[1], abjad.Duration(1)),
        (pitch_list[3], abjad.Duration(1)),
        (pitch_list[2], abjad.Duration(1)),
        ]



#-------------------PolySynth----------------#

#--------------/
# RH_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'RH_I'

rhythm_definition.notes = [
        (pitch_list[0], abjad.Duration(1)),
        (pitch_list[0], abjad.Duration(1)),
        (pitch_list[1], abjad.Duration(1)),
        (pitch_list[3], abjad.Duration(1)),
        (pitch_list[2], abjad.Duration(1)),
        ]


#---------------/
# RH_II  /
#_____________/
#
#rhythm_definition = segment_maker.define_rhythm()
#rhythm_definition.instrument_name = 'RH_II'
#
#rhythm_definition.notes = [
#        (pitch_list[0], abjad.Duration(1)),
#        (pitch_list[0], abjad.Duration(1)),
#        (pitch_list[1], abjad.Duration(1)),
#        (pitch_list[3], abjad.Duration(1)),
#        (pitch_list[2], abjad.Duration(1)),
#        ]
#
#--------------/
# LH_I  /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'LH_I'

rhythm_definition.notes = [
        (pitch_list[0], abjad.Duration(1)),
        (pitch_list[0], abjad.Duration(1)),
        (pitch_list[1], abjad.Duration(1)),
        (pitch_list[3], abjad.Duration(1)),
        (pitch_list[2], abjad.Duration(1)),
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
