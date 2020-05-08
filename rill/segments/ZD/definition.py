import abjad
import baca
import ins_wasser
import os
from abjadext import rmakers


###############################################################################
##################################### [D] #####################################
###############################################################################

maker = baca.SegmentMaker(
    activate=[
        abjad.tags.LOCAL_MEASURE_NUMBER,
        ],
    segment_directory=abjad.Path(os.path.realpath(__file__)).parent,
    time_signatures=30 * [(4, 4)] + [(1, 4)],
    validate_measure_count=31,
)

maker(
    "Global_Skips",
    baca.metronome_mark(
        "27",
        selector=baca.leaf(1 - 1),
    ),
    baca.metronome_mark(
        baca.Accelerando(),
        selector=baca.leaf(1 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(5 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(11 - 1),
    ),
    baca.metronome_mark(
        baca.Accelerando(),
        selector=baca.leaf(11 - 1),
    ),
    baca.metronome_mark(
        "108",
        selector=baca.leaf(15 - 1),
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
        "27",
        selector=baca.leaf(25 - 1),
    ),
)

maker(
    ("Global_Rests", -1),
    baca.global_fermata("fermata"),
)

# va1

maker(
    "va1",
    baca.dls_staff_padding(3),
    baca.parenthesize(
        selector=baca.leaves().get([2, 6, 10, 12, 14]),
    ),
    baca.music(
        r"""
        d'1. cqs'1 dtqf'1. c'1 c'1. bqs1 cqf'1. b1
        b1. bqf1 atqs1. as1 bf1. aqs1 btqf1. a1
        a\longa a\longa.
        r4
        """
    ),
    baca.text_spanner(
        r"\ins-wasser-trans => \ins-wasser-po-fb-flaut ||"
        r" \ins-wasser-trans => \ins-wasser-po-nbs ||"
        r" \ins-wasser-trans => \ins-wasser-po-slow-bow ||"
        r" \ins-wasser-trans => \ins-wasser-po-scratch",
        pieces=baca.lparts([3, 1, 3, 1, 3, 1, 3 + 1]),
        selector=baca.leaves()[:-3],
    ),
    baca.text_spanner_staff_padding(2.5),
)

maker(
    ("va1", [(1, 2), (3, 5), (6, 7), (8, 10), (11, 12), (13, 15),
        (16, 17), (18, 20)]),
    baca.glissando(),
)

maker(
    ("va1", (1, 10)),
    baca.hairpin(
        "pp < p  p < mp  mp < mf  mf < f",
        pieces=baca.clparts([1]),
    ),
)

maker(
    ("va1", (5, 6)),
    baca.repeat_tie(baca.pleaves()[1:]),
)

maker(
    ("va1", (10, 11)),
    baca.repeat_tie(baca.pleaves()[1:]),
)

maker(
    ("va1", (11, 20)),
    baca.hairpin(
        "f < ff  ff < fff",
        pieces=baca.lparts([3, 1, 4]),
    ),
)

maker(
    ("va1", (20, 25)),
    baca.repeat_tie(baca.pleaves()[1:]),
)

# va2

maker(
    "va2",
    baca.dls_staff_padding(4),
)

maker(
    ("va2", (1, 4)),
    baca.pitch("D4"),
)

maker(
    ("va2", (1, 19)),
    baca.alternate_bow_strokes(full=True),
    baca.make_repeated_duration_notes([(1, 4)]),
    baca.script_staff_padding(1),
)

maker(
    ("va2", (5, 30)),
    baca.pitch("A#3"),
)

maker(
    ("va2", (20, 31)),
    baca.music(
        r"""
        as1 as\longa as1. as1. as1. as1. r4
        """
    ),
    baca.text_spanner(
        r"\ins-wasser-xp-xfb-flaut ||"
        r" \ins-wasser-trans => \ins-wasser-xp-xfb-flaut =>"
        r" \ins-wasser-tasto-slow-bow => \ins-wasser-tasto-scratch =>"
        r" \ins-wasser-clicks-one-two-sec",
        pieces=baca.lparts([1, 1, 1, 1, 1 + 1]),
        selector=baca.leaves()[:-1],
    ),
    baca.text_spanner_staff_padding(2.5),
)

maker(
    ("va2", (20, 28)),
    baca.hairpin(
        "mf > p < mf",
        pieces=baca.lparts([2, 3]),
    ),
)
