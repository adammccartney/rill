import abjad
import baca
import ins_wasser
import os
from abjadext import rmakers


###############################################################################
##################################### [E] #####################################
###############################################################################

maker = baca.SegmentMaker(
    activate=[
        abjad.tags.LOCAL_MEASURE_NUMBER,
        ],
    segment_directory=abjad.Path(os.path.realpath(__file__)).parent,
    time_signatures=14 * [(4, 4)] + [(1, 4)],
    validate_measure_count=15,
)

maker(
    "Global_Skips",
    baca.metronome_mark(
        "36",
        selector=baca.leaf(1 - 1),
    ),
)

maker(
    "Global_Skips",
    baca.markup(
        r"\ins-wasser-repeat-eight",
        abjad.tweak((0, 6)).extra_offset,
        literal=True,
        selector=baca.skip(0),
    ),
    baca.open_volta(baca.skip(1 - 1)),
    baca.close_volta(baca.skip(2 - 1)),
)

# va1

maker(
    "va1",
    baca.dls_staff_padding(4),
    baca.markup(
        r"\ins-wasser-tasto-nbs",
        literal=True,
    ),
)

maker(
    ("va1", 1),
    baca.dynamic("mf"),
    baca.music(
        abjad.select([
            abjad.TremoloContainer(4, "cs'32 e'32"),
            abjad.TremoloContainer(4, "cs'32 e'32"),
            abjad.Rest("r2"),
        ]),
    ),
)

maker(
    ("va1", (1, 7)),
    baca.slur(map=baca.pleaves(exclude=abjad.const.HIDDEN).clparts([2])),
)

maker(
    ("va1", 2),
    baca.dynamic("mp"),
    baca.music(
        abjad.select([
            abjad.TremoloContainer(4, "as32 d'32"),
            abjad.TremoloContainer(4, "as32 d'32"),
            abjad.Rest("r2"),
        ]),
    ),
)

maker(
    ("va1", 4),
    baca.dynamic("mf"),
    baca.music(
        abjad.select([
            abjad.TremoloContainer(4, "cs'32 e'32"),
            abjad.TremoloContainer(4, "cs'32 e'32"),
            abjad.Rest("r2"),
        ]),
    ),
)

# TODO: allow ("va1", [5, 7]) with hand-built rhythms
maker(
    ("va1", 5),
    baca.dynamic("mp"),
    baca.music(
        abjad.select([
            abjad.TremoloContainer(4, "b32 d'32"),
            abjad.TremoloContainer(4, "b32 d'32"),
            abjad.Rest("r2"),
        ]),
    ),
)

maker(
    ("va1", 7),
    baca.music(
        abjad.select([
            abjad.TremoloContainer(4, "b32 d'32"),
            abjad.TremoloContainer(4, "b32 d'32"),
            abjad.Rest("r2"),
        ]),
    ),
)

maker(
    ("va1", (9, 15)),
    baca.dynamic_text_self_alignment_x(
        -1,
        selector=baca.leaf(2),
    ),
    baca.hairpin(
        "p < mf -- ! >o niente",
        pieces=baca.lparts([1, 1, 1 + 1]),
    ),
    baca.pitches(
        "<G3 C#4>",
        allow_repeats=True,
        selector=baca.pleaf(1),
    ),
    baca.music(
        r"<a cs'>\breve <g cs'>\breve <fs d'>\breve r4",
    ),
)
