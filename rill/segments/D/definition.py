import abjad
import rill


###########
### [D] ###
###########

segment_maker = rill.SegmentMaker(
        name='D'
        )

time_signatures = [(4, 4) * 12]
segment_maker.time_signatures = time_signatures


#--------------/
#   Violin    /
#____________/

rhythm_definition = segment_maker.define_rhythm()
rhythm_definition.instrument_name = 'Violin'

rhythm_definition.notes = [
        ("C4", abjad.Duration(1)),
        ('E4', abjad.Duration(1)),
        ]

#-----------------/
#   MonoSynth    /
#_______________/


#-------------------PolySynth----------------#

#--------------/
# RH_Voice_I  /
#____________/

#---------------/
# RH_Voice_II  /
#_____________/

#--------------/
# LH_Voice_I  /
#____________/

#---------------/
# LH_Voice_II  /
#_____________/

#--------------------------------------------#
