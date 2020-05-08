import abjad
import baca
import ins_wasser


###############################################################################
##################################### [F] #####################################
###############################################################################

maker = ins_wasser.SegmentMaker(
    markup_leaves=False,
    name='F',
    )

maker.metronome_marks = [
    (0, ins_wasser.metronome_marks['108'], 6),
    (3, abjad.Fermata(), 2),
    (9, baca.Ritardando(), 6),
    (11, [ins_wasser.metronome_marks['54'], baca.Accelerando()]),
    (13, ins_wasser.metronome_marks['108']),
    (18, abjad.Fermata(), 2),
    ]

time_signatures = 28 * [(4, 4)]
maker.time_signatures = time_signatures

###############################################################################
################################### VIOLA I ###################################
###############################################################################

music_maker = maker.define_rhythm()
music_maker.instrument_name = 'Viola_I'

music_maker.notes = [
    ('F#4 A4', abjad.Duration(1), ins_wasser.hide_bar_lines()),
    ('E4 G4', abjad.Duration(1)),
    ('D4 F#4', abjad.Duration(1)),
    ('D4 F#4', abjad.Duration(2)),
    ('F#4 A4', abjad.Duration(2)),
    ('E4 G4', abjad.Duration(2)),
    ('D4 F#4', abjad.Duration(2)),
    ('D4 F#4', abjad.Duration(2)),

    ('F#4 A4', abjad.Duration(1)),
    ('F#4 A4', abjad.Duration(1)),
    ('F#4 A4', abjad.Duration(1)),
    ('F#4 A4', abjad.Duration(1)),
    ('E4 G4', abjad.Duration(1)),
    ('D4 F#4', abjad.Duration(2)),

    ('D4 F#4', abjad.Duration(2)),
    ('E4 G4', abjad.Duration(2)),
    ('D4 F#4', abjad.Duration(4)),
    ]

music_maker.dynamics = [
    (0, abjad.Dynamic('mp'), 2),
    (4, abjad.Dynamic('p')),
    (4, '>'),
    (6, abjad.Dynamic('ppp')),
    (6, '<'),
    (7, abjad.Dynamic('f')),
    (7, '>'),
    (8, abjad.Dynamic('ppp')),
    (14, abjad.Dynamic('ppppp')),
    ]

music_maker.markup = [
    (0, ins_wasser.markup.tasto_FB_flaut(), 2),
    (6, [ins_wasser.markup.trans()]),
    (7, [ins_wasser.markup.tasto_slow_bow()]),
    (8, ins_wasser.markup.tasto_XFB_flaut()),
    ]

###############################################################################
################################### VIOLA II ##################################
###############################################################################

music_maker = maker.define_rhythm()
music_maker.instrument_name = 'Viola_II'

music_maker.notes = [
    ('D4', abjad.Duration(1)),
    ('F#4', abjad.Duration(1)),
    ('A3', abjad.Duration(1)),
    ('D4', abjad.Duration(2)),
    ('D4', abjad.Duration(2)),
    ('A3', abjad.Duration(2)),
    ('B3', abjad.Duration(2)),
    ('B3', abjad.Duration(2)),

    ('D4', abjad.Duration(1)),
    ('F#4', abjad.Duration(1)),
    ('B#3 F#4', abjad.Duration(1)),
    ('F#4', abjad.Duration(1)),
    ('A3 F#4', abjad.Duration(1)),
    ('D4', abjad.Duration(2)),

    ('D4', abjad.Duration(2)),
    ('A3', abjad.Duration(2)),
    ('B3', abjad.Duration(4)),
    ]

music_maker.dynamics = [
    (0, abjad.Dynamic('mp'), 2),
    (4, abjad.Dynamic('p')),
    (4, '>'),
    (6, abjad.Dynamic('ppp')),
    (6, '<'),
    (7, abjad.Dynamic('f')),
    (7, '>'),
    (8, abjad.Dynamic('ppp')),
    (14, abjad.Dynamic('ppppp')),
    ]

music_maker.markup = [
    (0, ins_wasser.markup.tasto_FB_flaut(), 1.5),
    (6, [ins_wasser.markup.trans()]),
    (7, [ins_wasser.markup.tasto_slow_bow()]),
    (8, ins_wasser.markup.tasto_XFB_flaut()),
    ]
