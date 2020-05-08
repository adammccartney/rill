import abjad
import baca
import ins_wasser


###############################################################################
##################################### [E] #####################################
###############################################################################

maker = ins_wasser.SegmentMaker(
    markup_leaves=False,
    name='E',
    )

maker.metronome_marks = [
    (0, ins_wasser.metronome_marks['36'], 11),
    (-1, abjad.Fermata(), 2),
    ]

time_signatures = 14 * [(4, 4)] + [(1, 4)]
maker.time_signatures = time_signatures

###############################################################################
################################### VIOLA I ###################################
###############################################################################

music_maker = maker.define_rhythm()
music_maker.instrument_name = 'Viola_I'

container = ins_wasser.repeated_figure("cs' e'")
music_maker.notes = [
    container,
    ('A#3 D4', abjad.Duration(1, 4)),
    ('A#3 D4', abjad.Duration(1, 4)),
    'r2',
    'r1',
    ('C#4 E4', abjad.Duration(1, 4)),
    ('C#4 E4', abjad.Duration(1, 4)),
    'r2',
    ('B3 D4', abjad.Duration(1, 4)),
    ('B3 D4', abjad.Duration(1, 4)),
    'r2',
    'r1',
    ('B3 D4', abjad.Duration(1, 4)),
    ('B3 D4', abjad.Duration(1, 4)),
    'r2',
    'r1',
    ('A3 E#4', abjad.Duration(2)),
    ('G3 E#4', abjad.Duration(2)),
    ('F#3 D4', abjad.Duration(2)),
    'r4',
    ]

music_maker.markup = [
    (0, ins_wasser.markup.tasto_NBS(), 2.5),
    (18, ins_wasser.markup.tasto_FB_flaut(), 1.5),
    ]

music_maker.dynamics = [
    (0, abjad.Dynamic('mf'), 4),
    (3, abjad.Dynamic('mp'), 2),
    (7, abjad.Dynamic('mf')),
    (10, abjad.Dynamic('mp')),
    (14, abjad.Dynamic('mp')),
    (18, abjad.Dynamic('p'), 2),
    (18, '<'),
    (19, abjad.Dynamic('mf')),
    (20, abjad.Dynamic('mf')),
    (20, '>'),
    (21, abjad.Dynamic('mp')),
    ]

###############################################################################
################################### VIOLA II ##################################
###############################################################################

music_maker = maker.define_rhythm()
music_maker.instrument_name = 'Viola_II'

container = ins_wasser.repeated_figure('e a')
music_maker.notes = [
    container,
    ('E3 G3', abjad.Duration(1, 4)),
    ('E3 G3', abjad.Duration(1, 4)),
    'r2',
    'r1',
    ('E3 A3', abjad.Duration(1, 4)),
    ('E3 A3', abjad.Duration(1, 4)),
    'r2',
    ('E3 G#3', abjad.Duration(1, 4)),
    ('E3 G#3', abjad.Duration(1, 4)),
    'r2',
    'r1',
    ('G#3 A3', abjad.Duration(1, 4)),
    ('G#3 A3', abjad.Duration(1, 4)),
    'r2',
    'r1',
    ('A3', abjad.Duration(3)),
    ('A3', abjad.Duration(3)),
    'r4',
    ]

music_maker.dynamics = [
    (0, abjad.Dynamic('mf'), 3.5),
    (3, abjad.Dynamic('mp')),
    (7, abjad.Dynamic('mf')),
    (10, abjad.Dynamic('mp')),
    (14, abjad.Dynamic('mp'), 2.5),
    (18, abjad.Dynamic('pp'), 2),
    (18, '<'),
    (19, abjad.Dynamic('mf')),
    (19, '>'),
    (20, abjad.Dynamic('ppp')),
    ]

music_maker.markup = [
    (0, ins_wasser.markup.tasto_NBS(), 2.5),
    (18, [ins_wasser.markup.tasto_XFB_flaut()], 1.5),
    (19, ins_wasser.markup.XP_XFB_flaut()),
    ]
