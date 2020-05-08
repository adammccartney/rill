import abjad
import baca
import ins_wasser
import os
from abjadext import rmakers


###############################################################################
##################################### [G] #####################################
###############################################################################

maker = baca.SegmentMaker(
    activate=[
        abjad.tags.LOCAL_MEASURE_NUMBER,
        ],
    final_segment=True,
    segment_directory=abjad.Path(os.path.realpath(__file__)).parent,
    time_signatures=64 * [(4, 4)] + [(1, 4)],
    validate_measure_count=65,
)

maker(
    "Global_Skips",
    baca.metronome_mark(
        "108",
        selector=baca.leaf(1 - 1),
    ),
    baca.metronome_mark(
        baca.Ritardando(),
        selector=baca.leaf(1 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(5 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(6 - 1),
    ),
    baca.metronome_mark(
        baca.Accelerando(),
        selector=baca.leaf(6 - 1),
    ),
    baca.metronome_mark(
        "108",
        selector=baca.leaf(10 - 1),
    ),

    baca.metronome_mark(
        "108",
        selector=baca.leaf(11 - 1),
    ),
    baca.metronome_mark(
        baca.Ritardando(),
        selector=baca.leaf(11 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(15 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(16 - 1),
    ),
    baca.metronome_mark(
        baca.Accelerando(),
        selector=baca.leaf(16 - 1),
    ),
    baca.metronome_mark(
        "108",
        selector=baca.leaf(20 - 1),
    ),

    baca.metronome_mark(
        "108",
        selector=baca.leaf(21 - 1),
    ),
    baca.metronome_mark(
        baca.Ritardando(),
        selector=baca.leaf(21 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(25 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(26 - 1),
    ),
    baca.metronome_mark(
        baca.Accelerando(),
        selector=baca.leaf(26 - 1),
    ),
    baca.metronome_mark(
        "108",
        selector=baca.leaf(30 - 1),
    ),

    baca.metronome_mark(
        "108",
        selector=baca.leaf(31 - 1),
    ),
    baca.metronome_mark(
        baca.Ritardando(),
        selector=baca.leaf(31 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(35 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(36 - 1),
    ),
    baca.metronome_mark(
        baca.Accelerando(),
        selector=baca.leaf(36 - 1),
    ),
    baca.metronome_mark(
        "108",
        selector=baca.leaf(40 - 1),
    ),

    baca.metronome_mark(
        "108",
        selector=baca.leaf(41 - 1),
    ),
    baca.metronome_mark(
        baca.Ritardando(),
        selector=baca.leaf(41 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(47 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(50 - 1),
    ),
    baca.metronome_mark(
        baca.Ritardando(),
        selector=baca.leaf(50 - 1),
    ),
    baca.metronome_mark(
        "27",
        selector=baca.leaf(56 - 1),
    ),
    baca.bar_line("|.", baca.skip(-1)),
)

maker(
    ("va2", -1),
    baca.chunk(
        baca.mark(r"\ins-wasser-colophon-markup"),
        baca.rehearsal_mark_down(),
        baca.rehearsal_mark_padding(6),
        baca.rehearsal_mark_self_alignment_x(abjad.Right),
        selector=baca.leaves().rleak()[-1],
    ),
)
