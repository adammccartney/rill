import abjad
import baca
import ins_wasser


###############################################################################
##################################### [B] #####################################
###############################################################################

maker = ins_wasser.SegmentMaker(
    markup_leaves=False,
    name='B',
    )

maker.metronome_marks = [
    (0, ins_wasser.metronome_marks['72'], 8),
    (8, baca.Ritardando()),
    (11, ins_wasser.metronome_marks['36']),
    (13, baca.Ritardando()),
    (16, ins_wasser.metronome_marks['18']),
    (17, baca.Accelerando()),
    (20, ins_wasser.metronome_marks['36']),
    (22, baca.Accelerando()),
    (25, ins_wasser.metronome_marks['72']),
    ]

time_signatures = 32 * [(4, 4)]
maker.time_signatures = time_signatures

###############################################################################
################################### VIOLA I ###################################
###############################################################################

music_maker = maker.define_rhythm()
music_maker.instrument_name = 'Viola_I'

music_maker.notes = [
    ('F#4 A4', abjad.Duration(2)),
    ('E4 G4', abjad.Duration(1)),
    ('D4 F#4', abjad.Duration(1)),

    ('F#4 A4', abjad.Duration(2)),
    ('F#4 A4', abjad.Duration(2)),

    ('F#4 A4', abjad.Duration(1)),
    ('F#4 A4', abjad.Duration(3, 2)),
    ('F#4 A4', abjad.Duration(3, 2)),
    ('F#4 A4', abjad.Duration(3, 2)),
    ('F#4 A4', abjad.Duration(1, 2)),

    ('F#4 A4', abjad.Duration(3, 2)),
    ('A4', abjad.Duration(3, 2)),

    ('A4', abjad.Duration(1)),

    ('A4', abjad.Duration(3, 2)),
    ('A4', abjad.Duration(3, 2)),
    ('A4', abjad.Duration(1, 2)),

    ('A4', abjad.Duration(3, 2)),
    ('A4', abjad.Duration(3, 2)),
    ('A4', abjad.Duration(3, 2)),

    ('F#4 A4', abjad.Duration(2)),
    ('F#4 A4', abjad.Duration(1)),
    ('E4 G4', abjad.Duration(1)),
    ('D4 F#4', abjad.Duration(2)),
    ]

music_maker.markup = [
    (0, ins_wasser.markup.tasto_FB_flaut(), 2.5),
    (6, [ins_wasser.markup.trans()]),
    (7, ins_wasser.markup.PO_FB_flaut()),
    (8, [ins_wasser.markup.trans()]),
    (9, ins_wasser.markup.PO_NBS()),
    (10, [ins_wasser.markup.trans()]),
    (11, ins_wasser.markup.PO_scratch()),
    (14, [ins_wasser.markup.trans()]),
    (15, ins_wasser.markup.PO_NBS()),
    (16, [ins_wasser.markup.trans()]),
    (17, ins_wasser.markup.PO_FB_flaut()),
    (18, [ins_wasser.markup.trans()]),
    (19, ins_wasser.markup.tasto_FB_flaut()),
    ]

music_maker.dynamics = [
    (0, abjad.Dynamic('mp'), 2),
    (3, abjad.Dynamic('p')),
    (6, abjad.Dynamic('p')),
    (6, '<'),
    (7, abjad.Dynamic('mp')),
    (8, abjad.Dynamic('mp')),
    (8, '<'),
    (9, abjad.Dynamic('mf')),
    (10, abjad.Dynamic('mf')),
    (10, '<'),
    (11, abjad.Dynamic('f')),
    (12, abjad.Dynamic('ff')),
    (14, abjad.Dynamic('f')),
    (14, '>'),
    (15, abjad.Dynamic('mf')),
    (16, abjad.Dynamic('mf')),
    (16, '>'),
    (17, abjad.Dynamic('mp')),
    (18, abjad.Dynamic('mp')),
    (18, '>'),
    (19, abjad.Dynamic('p')),
    ]

###############################################################################
################################### VIOLA II ##################################
###############################################################################

music_maker = maker.define_rhythm()
music_maker.instrument_name = 'Viola_II'

music_maker.notes = [
    ('D4', abjad.Duration(1), ins_wasser.hide_bar_lines()),
    ('C#4', abjad.Duration(1)),
    ('A3', abjad.Duration(1)),
    ('D4', abjad.Duration(1)),

    ('D4', abjad.Duration(1)),
    ('C#4', abjad.Duration(1)),
    ('B3 D#4', abjad.Duration(2)),

    ('B3 D#4', abjad.Duration(3, 2)),
    ('B3 D#4', abjad.Duration(3, 2)),
    ('B3 D#4', abjad.Duration(3, 2)),
    ('B3 D#4', abjad.Duration(1, 2)),

    ('B3 D#4', abjad.Duration(3, 2)),
    ('B3', abjad.Duration(3, 2)),

    ('B3', abjad.Duration(1)),

    ('B3', abjad.Duration(3, 2)),
    ('B3', abjad.Duration(3, 2)),
    ('B3', abjad.Duration(1, 2)),
    ('B3', abjad.Duration(3, 2)),
    ('B3', abjad.Duration(3, 2)),
    ('B3', abjad.Duration(3, 2)),

    ('B3', abjad.Duration(1)),

    ('B3 D#4', abjad.Duration(2)),
    ('C#4', abjad.Duration(1)),
    ('A3 C#4', abjad.Duration(1)),
    ('D4', abjad.Duration(2)),
    ]

music_maker.markup = [
    (0, ins_wasser.markup.tasto_FB_flaut(), 2),
    (7, [ins_wasser.markup.trans()]),
    (8, ins_wasser.markup.PO_FB_flaut()),
    (9, [ins_wasser.markup.trans()]),
    (10, ins_wasser.markup.PO_NBS()),
    (11, [ins_wasser.markup.trans()]),
    (12, ins_wasser.markup.PO_scratch()),
    (15, [ins_wasser.markup.trans()]),
    (16, ins_wasser.markup.PO_NBS()),
    (17, [ins_wasser.markup.trans()]),
    (18, ins_wasser.markup.PO_FB_flaut()),
    (19, [ins_wasser.markup.trans()]),
    (20, ins_wasser.markup.tasto_FB_flaut()),
    ]

music_maker.dynamics = [
    (0, abjad.Dynamic('mp'), 2),
    (4, abjad.Dynamic('p')),
    (7, abjad.Dynamic('p'), 3),
    (7, '<'),
    (8, abjad.Dynamic('mp')),
    (9, abjad.Dynamic('mp')),
    (9, '<'),
    (10, abjad.Dynamic('mf')),
    (11, abjad.Dynamic('mf')),
    (11, '<'),
    (12, abjad.Dynamic('f')),
    (13, abjad.Dynamic('ff')),
    (15, abjad.Dynamic('f')),
    (15, '>'),
    (16, abjad.Dynamic('mf')),
    (17, abjad.Dynamic('mf')),
    (17, '>'),
    (18, abjad.Dynamic('mp')),
    (19, abjad.Dynamic('mp')),
    (19, '>'),
    (20, abjad.Dynamic('p')),
    ]
