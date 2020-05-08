import abjad
import baca
import ins_wasser
import os
from abjadext import rmakers


###############################################################################
##################################### [C] #####################################
###############################################################################

maker = baca.SegmentMaker(
    activate=[
        abjad.tags.LOCAL_MEASURE_NUMBER,
        ],
    segment_directory=abjad.Path(os.path.realpath(__file__)).parent,
    time_signatures=42 * [(4, 4)],
    validate_measure_count=42,
)

maker(
    "Global_Skips",
    baca.metronome_mark(
        "72",
        selector=baca.leaf(1 - 1),
    ),
    baca.metronome_mark(
        baca.Accelerando(),
        selector=baca.leaf(1 - 1),
    ),
    baca.metronome_mark(
        "108",
        selector=baca.leaf(7 - 1),
    ),
    baca.metronome_mark(
        "108",
        selector=baca.leaf(27 - 1),
    ),
    baca.metronome_mark(
        baca.Ritardando(),
        selector=baca.leaf(27 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(31 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(37 - 1),
    ),
    baca.metronome_mark(
        baca.Ritardando(),
        selector=baca.leaf(37 - 1),
    ),
    baca.metronome_mark(
        "27",
        selector=baca.leaf(40 - 1),
    ),
)

# va1

maker(
    "va1",
    baca.flat_glissando("D4"),
    baca.make_repeated_duration_notes([(1, 1)]),
)

# va2

maker(
    ("va2", (1, 26)),
    baca.text_spanner_staff_padding(2.5),
)

maker(
    ("va2", (1, 30)),
    baca.repeat_tie_extra_offset(
        (-1.5, 0),
        selector=baca.leaves(),
    ),
    baca.repeat_tie(baca.pleaves()[1:]),
    baca.music(
        r"""
        d'\breve d'\longa d'\longa
        d'1. d'1 d'1. d'1 d'1. d'1 d'1. d'1
        d'1. d'1 d'1. d'\breve d'\longa
        """
    ),
)

maker(
    ("va2", (3, 7)),
    baca.text_spanner(
        r"\ins-wasser-trans => \ins-wasser-tasto-xfb-flaut",
    ),
)

maker(
    ("va2", (11, 12)),
    baca.text_spanner(
        r"\ins-wasser-trans => \ins-wasser-pt-xfb-flaut",
    ),
)

maker(
    ("va2", (13, 15)),
    baca.text_spanner(
        r"\ins-wasser-trans => \ins-wasser-po-xfb-flaut",
    ),
)

maker(
    ("va2", (16, 17)),
    baca.text_spanner(
        r"\ins-wasser-trans => \ins-wasser-pp-xfb-flaut",
    ),
)

maker(
    ("va2", (18, 20)),
    baca.text_spanner(
        r"\ins-wasser-trans => \ins-wasser-p-xfb-flaut",
    ),
)

maker(
    ("va2", (21, 22)),
    baca.text_spanner(
        r"\ins-wasser-trans => \ins-wasser-mp-xfb-flaut",
    ),
)

maker(
    ("va2", (23, 25)),
    baca.text_spanner(
        r"\ins-wasser-trans => \ins-wasser-xp-xfb-flaut",
    ),
)

maker(
    ("va2", (27, 30)),
    baca.text_spanner(
        r"\ins-wasser-trans => \ins-wasser-xp",
        selector=baca.leaves().rleak(),
    ),
)

maker(
    ("va2", (27, -1)),
    baca.text_spanner_staff_padding(4.5),
)

maker(
    ("va2", (31, 42)),
    baca.alternate_bow_strokes(full=True),
    baca.make_repeated_duration_notes([(1, 4)]),
    baca.pitch("D4"),
)

maker(
    ("va2", (32, 33)),
    baca.text_spanner(
        r"\ins-wasser-xp => \ins-wasser-one-third-ob",
        selector=baca.leaves()[2:].rleak(),
    ),
)

maker(
    ("va2", (34, 35)),
    baca.text_spanner(
        r"\ins-wasser-trans => \ins-wasser-two-thirds-ob",
        selector=baca.leaves()[2:].rleak(),
    ),
)

maker(
    ("va2", (37, 38)),
    baca.text_spanner(
        r"\ins-wasser-trans => \ins-wasser-ob-no-pitch",
        selector=baca.leaves()[2:].rleak(),
    ),
)
