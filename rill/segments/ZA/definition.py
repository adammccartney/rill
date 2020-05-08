import abjad
import baca
import ins_wasser
import os
from abjadext import rmakers


###############################################################################
##################################### [A] #####################################
###############################################################################

maker = baca.SegmentMaker(
    activate=[
        abjad.tags.LOCAL_MEASURE_NUMBER,
        ],
    first_segment=True,
    segment_directory=abjad.Path(os.path.realpath(__file__)).parent,
    time_signatures=54 * [(4, 4)] + [(1, 4)],
    validate_measure_count=55,
)

maker(
    "Global_Skips",
    baca.metronome_mark(
        "108",
        selector=baca.leaf(1 - 1),
    ),
    baca.metronome_mark(
        "108",
        selector=baca.leaf(45 - 1),
    ),
    baca.metronome_mark(
        baca.Ritardando(),
        selector=baca.leaf(45 - 1),
    ),
    baca.metronome_mark(
        "54",
        selector=baca.leaf(49 - 1),
    ),
    baca.metronome_mark(
        baca.Ritardando(),
        selector=baca.leaf(49 - 1),
    ),
    baca.metronome_mark(
        "27",
        selector=baca.leaf(52 - 1),
    ),
)

# va1

maker(
    "va1",
    baca.dls_staff_padding(4),
    baca.markup(
        r"\ins-wasser-tasto-xfb-flaut",
        literal=True,
    ),
    baca.suite(
        ins_wasser.margin_markup("Va. I"),
        baca.start_markup(
            r"\ins-wasser-viola-i-markup",
            literal=True,
        ),
    ),
)

maker(
    ("va1", (1, 16)),
    baca.dynamic("p"),
    baca.music(r"fs\longa g\longa \glissando a\longa fs\longa \fermata"),
)

maker(
    ("va1", (17, 32)),
    baca.dynamic("ppp"),
    baca.repeat_tie(baca.pleaf(0)),
    baca.music(r"fs\longa \glissando g\longa a\longa fs\longa \fermata"),
)

maker(
    ("va1", (33, 44)),
    baca.repeat_tie(baca.pheads()),
    baca.music(r"fs\breve. fs1. fs1. fs1. fs1. fs1. fs1."),
)

maker(
    ("va1", (35, 45)),
    baca.text_spanner(
        "trans. =>"
        r" \ins-wasser-pt-xfb-flaut =>"
        r" \ins-wasser-po-xfb-flaut =>"
        r" \ins-wasser-pp-xfb-flaut =>"
        r" \ins-wasser-p-xfb-flaut =>"
        r" \ins-wasser-mp-xfb-flaut =>"
        r" \ins-wasser-xp-xfb-flaut",
        pieces=baca.leaves().partition_by_counts([1], cyclic=True),
    ),
    baca.text_spanner_staff_padding(2.5),
)

maker(
    ("va1", (45, 50)),
    baca.repeat_tie(baca.pheads()),
    baca.music(r"fs\breve fs\longa"),
)

maker(
    ("va1", (47, 54)),
    baca.text_spanner(
        "trans. =>"
        r" \ins-wasser-xp-full-bow-strokes =>"
        r" \ins-wasser-half-ob =>"
        r" \ins-wasser-ob-no-pitch",
        bookend=False,
        pieces=baca.leaves().partition_by_counts([1, 6, 6, 4]),
    ),
    baca.text_spanner_staff_padding(4.5),
)

maker(
    ("va1", (51, 54)),
    baca.alternate_bow_strokes(),
    baca.make_repeated_duration_notes([(1, 4)]),
    baca.pitch("F#3"),
)

maker(
    ("va1", 55),
    baca.music(r"r4 \fermata"),
)

# va2

maker(
    "va2",
    baca.dls_staff_padding(4),
    baca.markup(
        r"\ins-wasser-tasto-xfb-flaut",
        literal=True,
    ),
    baca.suite(
        ins_wasser.margin_markup("Va. II"),
        baca.start_markup(
            r"\ins-wasser-viola-ii-markup",
            literal=True,
        ),
    ),
)

maker(
    ("va2", (1, 16)),
    baca.dynamic("p"),
    baca.repeat_tie(baca.pleaf(2)),
    baca.music(r"d\longa \glissando cs\longa cs\longa d\longa \fermata"),
)

maker(
    ("va2", (17, 32)),
    baca.dynamic("ppp"),
    baca.repeat_tie(baca.pleaf(0)),
    baca.repeat_tie(baca.pleaf(2)),
    baca.music(r"d\longa cs\longa cs\longa \glissando d\longa \fermata"),
)

maker(
    ("va2", (33, 44)),
    baca.repeat_tie(baca.pheads()),
    baca.music(r"d1. d1. d1. d1. d1. d1. d\breve."),
)

maker(
    ("va2", (33, 42)),
    baca.text_spanner(
        "trans. =>"
        r" \ins-wasser-pt-xfb-flaut =>"
        r" \ins-wasser-po-xfb-flaut =>"
        r" \ins-wasser-pp-xfb-flaut =>"
        r" \ins-wasser-p-xfb-flaut =>"
        r" \ins-wasser-mp-xfb-flaut =>"
        r" \ins-wasser-xp-xfb-flaut",
        pieces=baca.leaves().partition_by_counts([1], cyclic=True),
    ),
    baca.text_spanner_staff_padding(2.5),
)

maker(
    ("va2", (45, 48)),
    baca.repeat_tie(baca.pleaf(0)),
    baca.music(r"d\longa"),
)

maker(
    ("va2", (45, 52)),
    baca.text_spanner(
        "trans. =>"
        r" \ins-wasser-xp-full-bow-strokes =>"
        r" \ins-wasser-half-ob =>"
        r" \ins-wasser-ob-no-pitch",
        bookend=False,
        pieces=baca.leaves().partition_by_counts([1, 6, 6, 4]),
    ),
    baca.text_spanner_staff_padding(4.5),
)

maker(
    ("va2", (49, 54)),
    baca.alternate_bow_strokes(),
    baca.make_repeated_duration_notes([(1, 4)]),
    baca.pitch("D3"),
)

maker(
    ("va2", 55),
    baca.music(r"r4 \fermata"),
)
