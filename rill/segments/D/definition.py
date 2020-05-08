import abjad
import baca
import ins_wasser


###############################################################################
##################################### [D] ####################################
###############################################################################

maker = ins_wasser.SegmentMaker(
    markup_leaves=False,
    name='D',
    )

maker.metronome_marks = [
    (0, baca.Accelerando(), 6),
    (4, ins_wasser.metronome_marks['54']),
    (10, baca.Accelerando()),
    (14, ins_wasser.metronome_marks['108']),
    (20, baca.Ritardando(), 4),
    (24, ins_wasser.metronome_marks['27']),
    (-1, abjad.Fermata(), 2),
    ]

time_signatures = 30 * [(4, 4)] + [(1, 4)]
maker.time_signatures = time_signatures

###############################################################################
################################### VIOLA I ###################################
###############################################################################

music_maker = maker.define_rhythm()
music_maker.instrument_name = 'Viola_I'

music_maker.notes = [
    ('D4', abjad.Duration(3, 2), ins_wasser.glissando()),
    ('Cqs4', abjad.Duration(2, 2)),
    ('Dtqf4', abjad.Duration(3, 2), 'parenthesize', ins_wasser.glissando()), 
    ('C4', abjad.Duration(2, 2)),
    ('C4', abjad.Duration(3, 2), 'parenthesize', ins_wasser.glissando()),
    ('Bqs3', abjad.Duration(2, 2)),
    ('Cqf4', abjad.Duration(3, 2), 'parenthesize', ins_wasser.glissando()),
    ('B3', abjad.Duration(2, 2)),
    ('B3', abjad.Duration(3, 2), 'parenthesize', ins_wasser.glissando()),
    ('Bqf3', abjad.Duration(2, 2)),
    ('Atqs3', abjad.Duration(3, 2), 'parenthesize', ins_wasser.glissando()),
    ('A#3', abjad.Duration(2, 2)),
    ('Bb3', abjad.Duration(3, 2), 'parenthesize', ins_wasser.glissando()),
    ('A+3', abjad.Duration(2, 2)),
    ('Btqf3', abjad.Duration(3, 2), 'parenthesize', ins_wasser.glissando()),
    ('A3', abjad.Duration(2, 2)),

    ('A3', abjad.Duration(4)),
    ('A3', abjad.Duration(6)),
    abjad.Rest('r4'),
    ]

music_maker.markup = [
    (0, [ins_wasser.markup.trans()], 2),
    (3, ins_wasser.markup.PO_FB_flaut()),
    (4, [ins_wasser.markup.trans()]),
    (7, ins_wasser.markup.PO_NBS()),
    (8, [ins_wasser.markup.trans()]),
    (11, ins_wasser.markup.PO_slow_bow()),
    (12, [ins_wasser.markup.trans()]),
    (15, ins_wasser.markup.PO_scratch()),
    ]

music_maker.dynamics = [
    (0, abjad.Dynamic('pp'), 2),
    (0, '<'),
    (1, abjad.Dynamic('p')),
    (2, abjad.Dynamic('p')),
    (2, '<'),
    (3, abjad.Dynamic('mp')),
    (4, abjad.Dynamic('mp')),
    (4, '<'),
    (5, abjad.Dynamic('mf')),
    (6, abjad.Dynamic('mf'), 2.5),
    (6, '<'),
    (7, abjad.Dynamic('f')),
    (8, abjad.Dynamic('f')),
    (8, '<'),
    (11, abjad.Dynamic('ff')),
    (12, abjad.Dynamic('ff')),
    (12, '<'),
    (15, abjad.Dynamic('fff')),
    ]

###############################################################################
################################### VIOLA II ##################################
###############################################################################

music_maker = maker.define_rhythm()
music_maker.instrument_name = 'Viola_II'

music_maker.notes = [
    ('D4', abjad.Duration(1, 4), ins_wasser.hide_bar_lines(), ins_wasser.down_bow()),
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

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.down_bow()),
    ('A#3', abjad.Duration(1, 4), ins_wasser.up_bow()),

    ('A#3', abjad.Duration(1)),

    ('A#3', abjad.Duration(4)),

    ('A#3', abjad.Duration(3, 2)),
    ('A#3', abjad.Duration(3, 2)),
    ('A#3', abjad.Duration(3, 2)),
    ('A#3', abjad.Duration(3, 2)),
    (abjad.Rest('r4'), None, ins_wasser.show_bar_lines()),
    ]

music_maker.markup = [
    (76, ins_wasser.markup.XP_XFB_flaut(), 1.5),
    (77, [ins_wasser.markup.trans()]),
    (78, [ins_wasser.markup.tasto_XFB_flaut()]),
    (79, [ins_wasser.markup.tasto_slow_bow()]),
    (80, [ins_wasser.markup.tasto_scratch()]),
    (81, ins_wasser.markup.clicks_1_2_per_second()),
    ]

music_maker.dynamics = [
    (76, abjad.Dynamic('mf'), 2.5),
    (76, '>'),
    (78, abjad.Dynamic('p')),
    (78, '<'),
    (80, abjad.Dynamic('mf')),
    ]
