import abjad
import baca
import ins_wasser
import os
from abjadext import rmakers


###############################################################################
##################################### [B] #####################################
###############################################################################

maker = baca.SegmentMaker(
    activate=[
        abjad.tags.LOCAL_MEASURE_NUMBER,
        ],
    segment_directory=abjad.Path(os.path.realpath(__file__)).parent,
    time_signatures=32 * [(4, 4)],
    validate_measure_count=32,
)

maker(
    "Global_Skips",
    baca.metronome_mark(
        "72",
        selector=baca.leaf(1 - 1),
    ),
    baca.metronome_mark(
        "72",
        selector=baca.leaf(9 - 1),
    ),
    baca.metronome_mark(
        baca.Ritardando(),
        selector=baca.leaf(9 - 1),
    ),
    baca.metronome_mark(
        "36",
        selector=baca.leaf(12 - 1),
    ),
    baca.metronome_mark(
        "36",
        selector=baca.leaf(14 - 1),
    ),
    baca.metronome_mark(
        baca.Ritardando(),
        selector=baca.leaf(14 - 1),
    ),
    baca.metronome_mark(
        "18",
        selector=baca.leaf(17 - 1),
    ),
    baca.metronome_mark(
        "18",
        selector=baca.leaf(18 - 1),
    ),
    baca.metronome_mark(
        baca.Accelerando(),
        selector=baca.leaf(18 - 1),
    ),
    baca.metronome_mark(
        "36",
        selector=baca.leaf(21 - 1),
    ),
    baca.metronome_mark(
        "36",
        selector=baca.leaf(23 - 1),
    ),
    baca.metronome_mark(
        baca.Accelerando(),
        selector=baca.leaf(23 - 1),
    ),
    baca.metronome_mark(
        "72",
        selector=baca.leaf(26 - 1),
    ),
)

# va1

maker(
    "va1",
    baca.dls_staff_padding(4),
    baca.dynamic("mp"),
    baca.text_spanner_staff_padding(3.5),
)

maker(
    ("va1", (1, 6)),
    baca.music(r"<fs' a'>\breve <e' g'>1 <d' fs'>1 <fs' a'>\breve")
)

maker(
    ("va1", (5, 29)),
    baca.repeat_tie(baca.pleaves()),
)

maker(
    ("va1", (7, 12)),
    baca.music(
        r"<fs' a'>\breve <fs' a'>1 <fs' a'>1. <fs' a'>1."
)
)

maker(
    ("va1", (10, 11)),
    baca.chunk(
        baca.hairpin("p < mp"),
        baca.text_spanner(
            r"trans. => \ins-wasser-po-fb-flaut"
        ),
    ),
)

maker(
    ("va1", (13, 14)),
    baca.chunk(
        baca.hairpin("mp < mf"),
        baca.text_spanner(
            r"trans. => \ins-wasser-po-nbs"
        ),
    ),
)

maker(
    ("va1", (13, 17)),
    baca.music(r"<fs' a'>1. <fs' a'>2 <fs' a'>1. a'1.")
)

maker(
    ("va1", (15, 16)),
    baca.chunk(
        baca.hairpin("mf < f"),
        baca.text_spanner(
            r"trans. => \ins-wasser-po-scratch"
        ),
    ),
)

maker(
    ("va1", (18, 26)),
    baca.dynamic("ff", selector=baca.pleaf(0)),
    baca.music(r"a'1 a'1. a'1. a'2 a'1. a'1. a'1.")
)

maker(
    ("va1", (20, 22)),
    baca.chunk(
        baca.hairpin("f > mf"),
        baca.text_spanner(
            r"trans. => \ins-wasser-po-nbs",
        ),
        selector=baca.pleaves()[:-1],
    ),
)

maker(
    ("va1", (22, 24)),
    baca.chunk(
        baca.hairpin("mf > mp"),
        baca.text_spanner(
            r"trans. => \ins-wasser-po-fb-flaut",
        ),
        selector=baca.pleaves()[1:],
    ),
)

maker(
    ("va1", (25, 27)),
    baca.chunk(
        baca.hairpin("mp > p"),
        baca.text_spanner(
            r"trans. => \ins-wasser-tasto-fb-flaut",
        ),
    ),
)

maker(
    ("va1", (27, 32)),
    baca.music(r"<fs' a'>\breve <fs' a'>1 <e' g'>1 <d' fs'>\breve"),
)

# va2

maker(
    "va2",
    baca.dls_staff_padding(4),
    baca.dynamic("mp"),
    baca.text_spanner_staff_padding(3.5),
)

maker(
    "va2",
    baca.music(
        r"""
        d'1 cs'1 a1 d'1 d'1 cs'1 
        <b ds'>\breve 
        <b ds'>1. <b ds'>1. 
        <b ds'>1. <b ds'>2 
        <b ds'>1. b1. 
        b1 b1. b1. 
        b2 b1. b1. b1. b1 
        <b ds'>\breve cs'1 <a cs'>1
        d'\breve 
        """,
    ),
)

maker(
    ("va2", 5),
    baca.repeat_tie(baca.pleaf(0)),
)

maker(
    ("va2", (9, 27)),
    baca.repeat_tie(baca.pleaves()),
)

maker(
    ("va2", 30),
    baca.repeat_tie(baca.pleaf(0)),
)
