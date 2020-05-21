import abjad
import rill


###########
### [A] ###
###########

maker = rill.SegmentMaker(
        name = 'A',
        )

time_signatures = 9 * [(3, 4)]
maker.time_signatures = time_signatures


#############
### Flute ###
#############


