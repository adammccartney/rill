import abjad
import baca
import ins_wasser


###############################################################################
##################################### [A] #####################################
###############################################################################

maker = ins_wasser.SegmentMaker(
    markup_leaves=False,
    name='A',
    )

maker.metronome_marks = [
    (0, ins_wasser.metronome_marks['108'], 6),
    (12, abjad.Fermata(), 2),
    (28, abjad.Fermata()),
    (44, baca.Ritardando(), 8),
    (48, [ins_wasser.metronome_marks['54'], baca.Ritardando()]),
    (51, ins_wasser.metronome_marks['27']),
    (-1, abjad.Fermata(), 2),
    ]

time_signatures = 54 * [(4, 4)] + [(1, 4)]
maker.time_signatures = time_signatures

###############################################################################
################################### VIOLA I ###################################
###############################################################################

rhythm_definition = maker.define_rhythm()
rhythm_definition.instrument_name = 'Viola_I'

rhythm_definition.notes = [
    ('F#3', abjad.Duration(4), ins_wasser.hide_bar_lines()),
    ('G3', abjad.Duration(4), ins_wasser.glissando()),
    ('A3', abjad.Duration(4)),
    ('F#3', abjad.Duration(4)),
    ('F#3', abjad.Duration(4), ins_wasser.glissando()),
    ('G3', abjad.Duration(4)),
    ('A3', abjad.Duration(4)),
    ('F#3', abjad.Duration(4)),

    ('F#3', abjad.Duration(3)),
    ('F#3', abjad.Duration(3, 2)),
    ('F#3', abjad.Duration(3, 2)),
    ('F#3', abjad.Duration(3, 2)),
    ('F#3', abjad.Duration(3, 2)),
    ('F#3', abjad.Duration(3, 2)),
    ('F#3', abjad.Duration(3, 2)),
    ('F#3', abjad.Duration(2)),

    ('F#3', abjad.Duration(4)),

    ('F#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('F#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('F#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('F#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('F#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('F#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('F#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('F#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('F#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('F#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('F#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('F#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('F#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('F#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('F#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('F#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    'r4',

    ]

rhythm_definition.dynamics = [
    (0, abjad.Dynamic('p'), 2.5),
    (4, abjad.Dynamic('ppp')),
    ]

rhythm_definition.markup = [
    (0, ins_wasser.markup.tasto_XFB_flaut(), 1.5),
    (2, ins_wasser.composer_markup(), (44.5, 2)),
    (9, [ins_wasser.markup.trans()]),
    (10, [ins_wasser.markup.pT_XFB_flaut()]),
    (11, [ins_wasser.markup.PO_XFB_flaut()]),
    (12, [ins_wasser.markup.pP_XFB_flaut()]),
    (13, [ins_wasser.markup.P_XFB_flaut()]),
    (14, [ins_wasser.markup.MP_XFB_flaut()]),
    (15, ins_wasser.markup.XP_XFB_flaut()),
    (16, [ins_wasser.markup.trans()], 3.5),
    (17, [ins_wasser.markup.XP_full_bow_strokes()]),
    (23, [ins_wasser.markup.one_half_OB()]),
    (29, ins_wasser.markup.OB_no_pitch()),
    ]

###############################################################################
################################### VIOLA II ##################################
###############################################################################

rhythm_definition = maker.define_rhythm()
rhythm_definition.instrument_name = 'Viola_II'

rhythm_definition.notes = [
    ('D3', abjad.Duration(4), ins_wasser.glissando()),
    ('C#3', abjad.Duration(4)),
    ('C#3', abjad.Duration(4)),
    ('D3', abjad.Duration(4)),
    ('D3', abjad.Duration(4)),
    ('C#3', abjad.Duration(4)),
    ('C#3', abjad.Duration(4), ins_wasser.glissando()),
    ('D3', abjad.Duration(4)),

    ('D3', abjad.Duration(3, 2)),
    ('D3', abjad.Duration(3, 2)),
    ('D3', abjad.Duration(3, 2)),
    ('D3', abjad.Duration(3, 2)),
    ('D3', abjad.Duration(3, 2)),
    ('D3', abjad.Duration(3, 2)),
    ('D3', abjad.Duration(3)),

    ('D3', abjad.Duration(4)),

    ('D3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    'r4',

    ]

rhythm_definition.dynamics = [
    (0, abjad.Dynamic('p'), 3.5),
    (4, abjad.Dynamic('ppp')),
    ]

rhythm_definition.markup = [
    (0, ins_wasser.markup.tasto_XFB_flaut(), 1.5),
    (8, [ins_wasser.markup.trans()]),
    (9, [ins_wasser.markup.pT_XFB_flaut()]),
    (10, [ins_wasser.markup.PO_XFB_flaut()]),
    (11, [ins_wasser.markup.pP_XFB_flaut()]),
    (12, [ins_wasser.markup.P_XFB_flaut()]),
    (13, [ins_wasser.markup.MP_XFB_flaut()]),
    (14, ins_wasser.markup.XP_XFB_flaut()),
    (15, [ins_wasser.markup.trans()], 3.5),
    (16, [ins_wasser.markup.XP_full_bow_strokes()]),
    (22, [ins_wasser.markup.one_half_OB()]),
    (28, ins_wasser.markup.OB_no_pitch()),
    ]
