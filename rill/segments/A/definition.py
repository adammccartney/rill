import abjad
import rill


###########
### [A] ###
###########

maker = rill.SegmentMaker(
        name='A'
        )

time_signatures = 12 * [(4, 4)]
maker.time_signatures = time_signatures


#--------------/
#   Violin    /
#____________/

rhythm_definition = maker.define_rhythm()
rhythm_definition.instrument_name = 'Violin'

rhythm_definition.notes = [
        ("c' d'", abjad.Duration(3, 2)),
        ('F4 E4', abjad.Duration(1)),
        ]

lilypond_file = maker.run()

#-----------------/
#   MonoSynth    /
#_______________/


#-------------------PolySynth----------------#

#--------------/
# RH_Voice_I  /
#____________/

#--------------/
# RH_Voice_II  /
#____________/

#--------------/
# LH_Voice_I  /
#____________/

#--------------/
# LH_Voice_II  /
#____________/

#--------------------------------------------#
