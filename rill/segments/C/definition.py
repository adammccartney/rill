import abjad
import baca
import ins_wasser


###############################################################################
##################################### [C] ####################################
###############################################################################

maker = ins_wasser.SegmentMaker(
    markup_leaves=False,
    name='C',
    )

maker.metronome_marks = [
    (0, baca.Accelerando(), 4),
    (6, ins_wasser.metronome_marks['108']),
    (26, baca.Ritardando()),
    (30, ins_wasser.metronome_marks['54']),
    (36, baca.Ritardando()),
    (39, ins_wasser.metronome_marks['27']),
    ]

time_signatures = 42 * [(4, 4)]
maker.time_signatures = time_signatures

###############################################################################
################################### VIOLA I ###################################
###############################################################################

music_maker = maker.define_rhythm()
music_maker.instrument_name = 'Viola_I'

note = abjad.Note(2, abjad.Duration(4), multiplier=(21, 2))
music_maker.notes = [
    note,
    ]

music_maker.markup = [
    (0, ins_wasser.markup.sustain_until_m_130(), 1.5),
    ]

music_maker.dynamics = [
    ]

###############################################################################
################################### VIOLA II ##################################
###############################################################################

music_maker = maker.define_rhythm()
music_maker.instrument_name = 'Viola_II'

music_maker.notes = [
    ('D4', abjad.Duration(2), ins_wasser.hide_bar_lines()),
    ('D4', abjad.Duration(4)),
    ('D4', abjad.Duration(4)),

    ('D4', abjad.Duration(3, 2)),
    ('D4', abjad.Duration(1)),
    ('D4', abjad.Duration(3, 2)),
    ('D4', abjad.Duration(1)),
    ('D4', abjad.Duration(3, 2)),
    ('D4', abjad.Duration(1)),
    ('D4', abjad.Duration(3, 2)),
    ('D4', abjad.Duration(1)),
    ('D4', abjad.Duration(3, 2)),
    ('D4', abjad.Duration(1)),
    ('D4', abjad.Duration(3, 2)),
    ('D4', abjad.Duration(2)),

    ('D4', abjad.Duration(4)),

    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('D4', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ]

music_maker.markup = [
    (1, [ins_wasser.markup.trans()], 2),
    (2, ins_wasser.markup.tasto_XFB_flaut()),
    (3, [ins_wasser.markup.trans()]),
    (4, ins_wasser.markup.pT_XFB_flaut()),
    (5, [ins_wasser.markup.trans()]),
    (6, ins_wasser.markup.PO_XFB_flaut()),
    (7, [ins_wasser.markup.trans()]),
    (8, ins_wasser.markup.pP_XFB_flaut()),
    (9, [ins_wasser.markup.trans()]),
    (10, ins_wasser.markup.P_XFB_flaut()),
    (11, [ins_wasser.markup.trans()]),
    (12, ins_wasser.markup.MP_XFB_flaut()),
    (13, [ins_wasser.markup.trans()]),
    (14, ins_wasser.markup.XP_XFB_flaut()),
    (15, [ins_wasser.markup.trans()], 3),
    (16, ins_wasser.markup.XP_full_bow_strokes()),
    (22, [ins_wasser.markup.XP()]),
    (28, ins_wasser.markup.one_third_OB()),
    (34, [ins_wasser.markup.trans()]),
    (40, ins_wasser.markup.two_thirds_OB()),
    (46, [ins_wasser.markup.trans()]),
    (52, ins_wasser.markup.OB_no_pitch()),
    ]

music_maker.dynamics = [
    ]
