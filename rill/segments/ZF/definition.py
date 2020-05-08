import abjad
import baca
import ins_wasser
import os
from abjadext import rmakers


###############################################################################
##################################### [F] #####################################
###############################################################################

maker = baca.SegmentMaker(
    activate=[
        abjad.tags.LOCAL_MEASURE_NUMBER,
        ],
    segment_directory=abjad.Path(os.path.realpath(__file__)).parent,
    time_signatures=28 * [(4, 4)],
    validate_measure_count=28,
)

maker(
    "Global_Skips",
    baca.metronome_mark(
        "108",
        selector=baca.leaf(1 - 1),
    ),
    baca.metronome_mark(
        "108",
        selector=baca.leaf(10 - 1),
    ),
    baca.metronome_mark(
        baca.Ritardando(),
        selector=baca.leaf(10 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(12 - 1),
    ),
    baca.metronome_mark(
        baca.Accelerando(),
        selector=baca.leaf(12 - 1),
    ),
    baca.metronome_mark(
        "108",
        selector=baca.leaf(14 - 1),
    ),
)
