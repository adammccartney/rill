import abjad
import baca
import ins_wasser


###############################################################################
##################################### [G] #####################################
###############################################################################

maker = ins_wasser.SegmentMaker(
    markup_leaves=False,
    name='G',
    )

maker.metronome_marks = [
    (0, [ins_wasser.metronome_marks['108'], baca.Ritardando()], 6),
    (4, ins_wasser.metronome_marks['54']),
    (5, baca.Accelerando(), 4),
    (9, ins_wasser.metronome_marks['108']),
    (10, baca.Ritardando()),
    (14, ins_wasser.metronome_marks['54']),
    (15, baca.Accelerando()),
    (19, ins_wasser.metronome_marks['108']),
    (20, baca.Ritardando()),
    (24, ins_wasser.metronome_marks['54']),
    (25, baca.Accelerando()),
    (29, ins_wasser.metronome_marks['108']),
    (30, baca.Ritardando()),
    (34, ins_wasser.metronome_marks['54']),
    (35, baca.Accelerando()),
    (39, ins_wasser.metronome_marks['108']),
    (40, baca.Ritardando()),
    (46, ins_wasser.metronome_marks['54']),
    (49, baca.Ritardando(), 6),
    (55, ins_wasser.metronome_marks['27']),
    (-1, abjad.Fermata(), 2),
    ]

time_signatures = 64 * [(4, 4)] + [(1, 4)]
maker.time_signatures = time_signatures

###############################################################################
################################### VIOLA I ###################################
###############################################################################

music_maker = maker.define_rhythm()
music_maker.instrument_name = 'Viola_I'

pedal_chord = abjad.Chord([2, 6], abjad.Duration(4), multiplier=(46, 4))
music_maker.notes = [
    pedal_chord,
    ('D4 G#4', abjad.Duration(3)),
    ('D4 G#4', abjad.Duration(3)),
    ('D4 G#4', abjad.Duration(3)),
    ('D4', abjad.Duration(3, 2)),
    ('D4', abjad.Duration(3, 2)),
    ('D4', abjad.Duration(3, 2)),
    ('D4', abjad.Duration(3, 2)),
    ('D4', abjad.Duration(3, 2)),
    ('D4', abjad.Duration(3, 2)),
    'r4',
    ]

music_maker.dynamics = [
    (1, abjad.Dynamic('ppppp')),
    (1, '<'),
    (3, abjad.Dynamic('mf')),
    ]

music_maker.markup = [
    (0, ins_wasser.markup.sustain_until_m_250(), 2),
    (2, [ins_wasser.markup.trans()]),
    (4, ins_wasser.markup.tasto_scratch()),
    (5, [ins_wasser.markup.trans()]),
    (6, ins_wasser.markup.clicks_2_3_per_second()),
    (7, [ins_wasser.markup.trans()]),
    (8, ins_wasser.markup.clicks_1_2_per_second()),
    (9, [ins_wasser.markup.trans()]),
    ]

###############################################################################
################################### VIOLA II ##################################
###############################################################################

music_maker = maker.define_rhythm()
music_maker.instrument_name = 'Viola_II'

music_maker.notes = [
    ('B3', abjad.Duration(4), ins_wasser.hide_bar_lines()),
    ('B3', abjad.Duration(1)),
    ('B3', abjad.Duration(4)),
    ('B3', abjad.Duration(1)),
    ('B3', abjad.Duration(4)),
    ('B3', abjad.Duration(1)),
    ('B3', abjad.Duration(4)),
    ('B3', abjad.Duration(1)),

    ('B3', abjad.Duration(3, 2)),
    ('B3', abjad.Duration(2, 2)),
    ('B3', abjad.Duration(3, 2)),
    ('B3', abjad.Duration(2, 2)),
    ('B3', abjad.Duration(3, 2)),
    ('B3', abjad.Duration(2, 2)),
    ('B3', abjad.Duration(3, 2)),
    ('B3', abjad.Duration(2, 2)),
    ('B3', abjad.Duration(3, 2)),
    ('B3', abjad.Duration(2, 2)),
    ('B3', abjad.Duration(3, 2)),
    ('B3', abjad.Duration(2, 2)),
    ('B3', abjad.Duration(3, 2)),
    ('B3', abjad.Duration(2, 2)),
    ('B3', abjad.Duration(3, 2)),
    ('B3', abjad.Duration(2, 2)),

    ('B3', abjad.Duration(3)),
    ('B3', abjad.Duration(3)),
    ('B3', abjad.Duration(3)),
    ('B3', abjad.Duration(6)),

    ('B3', abjad.Duration(6)),

    abjad.Rest(abjad.Duration(3)),
    (
        abjad.Rest(abjad.Duration(1, 4)),
        None,
        ins_wasser.show_bar_lines(),
        abjad.LilyPondLiteral(r'\bar "|."', 'after'),
        ),
    ]

music_maker.dynamics = [
    (8, abjad.Dynamic('ppppp')),
    (8, '<'),

    (9, abjad.Dynamic('pppp')),
    (10, abjad.Dynamic('pppp')),
    (10, '<'),
    (11, abjad.Dynamic('ppp')),
    (12, abjad.Dynamic('ppp')),
    (12, '<'),

    (13, abjad.Dynamic('pp')),
    (14, abjad.Dynamic('pp')),
    (14, '<'),
    (15, abjad.Dynamic('p')),
    (16, abjad.Dynamic('p')),
    (16, '<'),
    (17, abjad.Dynamic('mp')),
    (18, abjad.Dynamic('mp')),
    (18, '<'),
    (19, abjad.Dynamic('mf')),
    (20, abjad.Dynamic('mf')),
    (20, '<'),
    (21, abjad.Dynamic('f')),
    (22, abjad.Dynamic('f')),
    (22, '<'),
    (23, abjad.Dynamic('ff')),
    (24, abjad.Dynamic('ff')),
    (24, '<'),
    (25, abjad.Dynamic('fff')),
    ]

music_maker.markup = [
    (2, [ins_wasser.markup.trans()], 2),
    (3, ins_wasser.markup.PO_FB_flaut()),
    (4, [ins_wasser.markup.trans()]),
    (5, ins_wasser.markup.PO_NBS()),
    (25, [ins_wasser.markup.trans()]),
    (26, [ins_wasser.markup.PO_slow_bow()]),
    (27, ins_wasser.markup.PO_scratch()),
    ]
