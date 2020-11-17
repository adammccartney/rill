
import copy

import abjad
import rill

from pathlib import Path

from rill.tools.MusicMaker import MusicMaker

this_current_directory =  Path.cwd()
score = rill.ScoreTemplate()
score_template = score()

segment_maker = rill.SegmentMaker(
                                _lilypond_file=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=rill.build_path,
                                markup_leaves=False,
                                segment_name='segment_H',
                                rehearsal_mark=8,
                                tempo=((1, 4), 50),
                                )

segment_maker.metronome_marks = [
        (0, rill.metronome_marks['50'], 5),
        ]

time_signatures= [(4, 4)] + [(3, 4)] + [(3, 4)] + [(4, 4)] + [(3, 4)] + [(3,4)]
segment_maker.time_signatures = time_signatures


from rill.segments.segment_H.music_data import segment_music_data

Flute1_instrument_music_data = segment_music_data.Flute1
Flute1_rhythm_definition = segment_maker.define_rhythm()
Flute1_music_maker = MusicMaker(
    counts=Flute1_instrument_music_data.talea,
    denominator=Flute1_instrument_music_data.denominator,
    pitches=Flute1_instrument_music_data.pitches,
    attachment_makers=Flute1_instrument_music_data.attachments,
    override_makers=Flute1_instrument_music_data.overrides,
    )
Flute1_music = Flute1_music_maker(
    time_signature_pairs=Flute1_instrument_music_data.time_signature_pairs),
Flute1_rhythm_definition.notes = Flute1_music
Flute1_rhythm_definition.instrument_name = 'Flute1'


Flute2_instrument_music_data = segment_music_data.Flute2
Flute2_rhythm_definition = segment_maker.define_rhythm()
Flute2_music_maker = MusicMaker(
    counts=Flute2_instrument_music_data.talea,
    denominator=Flute2_instrument_music_data.denominator,
    pitches=Flute2_instrument_music_data.pitches,
    attachment_makers=Flute2_instrument_music_data.attachments,
    override_makers=Flute2_instrument_music_data.overrides,
    )
Flute2_music = Flute2_music_maker(
    time_signature_pairs=Flute2_instrument_music_data.time_signature_pairs),
Flute2_rhythm_definition.notes = Flute2_music
Flute2_rhythm_definition.instrument_name = 'Flute2'


Flute3_instrument_music_data = segment_music_data.Flute3
Flute3_rhythm_definition = segment_maker.define_rhythm()
Flute3_music_maker = MusicMaker(
    counts=Flute3_instrument_music_data.talea,
    denominator=Flute3_instrument_music_data.denominator,
    pitches=Flute3_instrument_music_data.pitches,
    attachment_makers=Flute3_instrument_music_data.attachments,
    override_makers=Flute3_instrument_music_data.overrides,
    )
Flute3_music = Flute3_music_maker(
    time_signature_pairs=Flute3_instrument_music_data.time_signature_pairs),
Flute3_rhythm_definition.notes = Flute3_music
Flute3_rhythm_definition.instrument_name = 'Flute3'


Flute4_instrument_music_data = segment_music_data.Flute4
Flute4_rhythm_definition = segment_maker.define_rhythm()
Flute4_music_maker = MusicMaker(
    counts=Flute4_instrument_music_data.talea,
    denominator=Flute4_instrument_music_data.denominator,
    pitches=Flute4_instrument_music_data.pitches,
    attachment_makers=Flute4_instrument_music_data.attachments,
    override_makers=Flute4_instrument_music_data.overrides,
    )
Flute4_music = Flute4_music_maker(
    time_signature_pairs=Flute4_instrument_music_data.time_signature_pairs),
Flute4_rhythm_definition.notes = Flute4_music
Flute4_rhythm_definition.instrument_name = 'Flute4'


Bbclarinet1_instrument_music_data = segment_music_data.Bbclarinet1
Bbclarinet1_rhythm_definition = segment_maker.define_rhythm()
Bbclarinet1_music_maker = MusicMaker(
    counts=Bbclarinet1_instrument_music_data.talea,
    denominator=Bbclarinet1_instrument_music_data.denominator,
    pitches=Bbclarinet1_instrument_music_data.pitches,
    attachment_makers=Bbclarinet1_instrument_music_data.attachments,
    override_makers=Bbclarinet1_instrument_music_data.overrides,
    )
Bbclarinet1_music = Bbclarinet1_music_maker(
    time_signature_pairs=Bbclarinet1_instrument_music_data.time_signature_pairs),
Bbclarinet1_rhythm_definition.notes = Bbclarinet1_music
Bbclarinet1_rhythm_definition.instrument_name = 'Bbclarinet1'


Vibraphone_instrument_music_data = segment_music_data.Vibraphone
Vibraphone_rhythm_definition = segment_maker.define_rhythm()
Vibraphone_music_maker = MusicMaker(
    counts=Vibraphone_instrument_music_data.talea,
    denominator=Vibraphone_instrument_music_data.denominator,
    pitches=Vibraphone_instrument_music_data.pitches,
    attachment_makers=Vibraphone_instrument_music_data.attachments,
    override_makers=Vibraphone_instrument_music_data.overrides,
    )
Vibraphone_music = Vibraphone_music_maker(
    time_signature_pairs=Vibraphone_instrument_music_data.time_signature_pairs),
Vibraphone_rhythm_definition.notes = Vibraphone_music
Vibraphone_rhythm_definition.instrument_name = 'Vibraphone'


Violin1_instrument_music_data = segment_music_data.Violin1
Violin1_rhythm_definition = segment_maker.define_rhythm()
Violin1_music_maker = MusicMaker(
    counts=Violin1_instrument_music_data.talea,
    denominator=Violin1_instrument_music_data.denominator,
    pitches=Violin1_instrument_music_data.pitches,
    attachment_makers=Violin1_instrument_music_data.attachments,
    override_makers=Violin1_instrument_music_data.overrides,
    )
Violin1_music = Violin1_music_maker(
    time_signature_pairs=Violin1_instrument_music_data.time_signature_pairs),
Violin1_rhythm_definition.notes = Violin1_music
Violin1_rhythm_definition.instrument_name = 'Violin1'


Violin2_instrument_music_data = segment_music_data.Violin2
Violin2_rhythm_definition = segment_maker.define_rhythm()
Violin2_music_maker = MusicMaker(
    counts=Violin2_instrument_music_data.talea,
    denominator=Violin2_instrument_music_data.denominator,
    pitches=Violin2_instrument_music_data.pitches,
    attachment_makers=Violin2_instrument_music_data.attachments,
    override_makers=Violin2_instrument_music_data.overrides,
    )
Violin2_music = Violin2_music_maker(
    time_signature_pairs=Violin2_instrument_music_data.time_signature_pairs),
Violin2_rhythm_definition.notes = Violin2_music
Violin2_rhythm_definition.instrument_name = 'Violin2'


Violin3_instrument_music_data = segment_music_data.Violin3
Violin3_rhythm_definition = segment_maker.define_rhythm()
Violin3_music_maker = MusicMaker(
    counts=Violin3_instrument_music_data.talea,
    denominator=Violin3_instrument_music_data.denominator,
    pitches=Violin3_instrument_music_data.pitches,
    attachment_makers=Violin3_instrument_music_data.attachments,
    override_makers=Violin3_instrument_music_data.overrides,
    )
Violin3_music = Violin3_music_maker(
    time_signature_pairs=Violin3_instrument_music_data.time_signature_pairs),
Violin3_rhythm_definition.notes = Violin3_music
Violin3_rhythm_definition.instrument_name = 'Violin3'


Violin4_instrument_music_data = segment_music_data.Violin4
Violin4_rhythm_definition = segment_maker.define_rhythm()
Violin4_music_maker = MusicMaker(
    counts=Violin4_instrument_music_data.talea,
    denominator=Violin4_instrument_music_data.denominator,
    pitches=Violin4_instrument_music_data.pitches,
    attachment_makers=Violin4_instrument_music_data.attachments,
    override_makers=Violin4_instrument_music_data.overrides,
    )
Violin4_music = Violin4_music_maker(
    time_signature_pairs=Violin4_instrument_music_data.time_signature_pairs),
Violin4_rhythm_definition.notes = Violin4_music
Violin4_rhythm_definition.instrument_name = 'Violin4'


Violin5_instrument_music_data = segment_music_data.Violin5
Violin5_rhythm_definition = segment_maker.define_rhythm()
Violin5_music_maker = MusicMaker(
    counts=Violin5_instrument_music_data.talea,
    denominator=Violin5_instrument_music_data.denominator,
    pitches=Violin5_instrument_music_data.pitches,
    attachment_makers=Violin5_instrument_music_data.attachments,
    override_makers=Violin5_instrument_music_data.overrides,
    )
Violin5_music = Violin5_music_maker(
    time_signature_pairs=Violin5_instrument_music_data.time_signature_pairs),
Violin5_rhythm_definition.notes = Violin5_music
Violin5_rhythm_definition.instrument_name = 'Violin5'


Violin6_instrument_music_data = segment_music_data.Violin6
Violin6_rhythm_definition = segment_maker.define_rhythm()
Violin6_music_maker = MusicMaker(
    counts=Violin6_instrument_music_data.talea,
    denominator=Violin6_instrument_music_data.denominator,
    pitches=Violin6_instrument_music_data.pitches,
    attachment_makers=Violin6_instrument_music_data.attachments,
    override_makers=Violin6_instrument_music_data.overrides,
    )
Violin6_music = Violin6_music_maker(
    time_signature_pairs=Violin6_instrument_music_data.time_signature_pairs),
Violin6_rhythm_definition.notes = Violin6_music
Violin6_rhythm_definition.instrument_name = 'Violin6'


Violin7_instrument_music_data = segment_music_data.Violin7
Violin7_rhythm_definition = segment_maker.define_rhythm()
Violin7_music_maker = MusicMaker(
    counts=Violin7_instrument_music_data.talea,
    denominator=Violin7_instrument_music_data.denominator,
    pitches=Violin7_instrument_music_data.pitches,
    attachment_makers=Violin7_instrument_music_data.attachments,
    override_makers=Violin7_instrument_music_data.overrides,
    )
Violin7_music = Violin7_music_maker(
    time_signature_pairs=Violin7_instrument_music_data.time_signature_pairs),
Violin7_rhythm_definition.notes = Violin7_music
Violin7_rhythm_definition.instrument_name = 'Violin7'


Violin8_instrument_music_data = segment_music_data.Violin8
Violin8_rhythm_definition = segment_maker.define_rhythm()
Violin8_music_maker = MusicMaker(
    counts=Violin8_instrument_music_data.talea,
    denominator=Violin8_instrument_music_data.denominator,
    pitches=Violin8_instrument_music_data.pitches,
    attachment_makers=Violin8_instrument_music_data.attachments,
    override_makers=Violin8_instrument_music_data.overrides,
    )
Violin8_music = Violin8_music_maker(
    time_signature_pairs=Violin8_instrument_music_data.time_signature_pairs),
Violin8_rhythm_definition.notes = Violin8_music
Violin8_rhythm_definition.instrument_name = 'Violin8'


Viola_instrument_music_data = segment_music_data.Viola
Viola_rhythm_definition = segment_maker.define_rhythm()
Viola_music_maker = MusicMaker(
    counts=Viola_instrument_music_data.talea,
    denominator=Viola_instrument_music_data.denominator,
    pitches=Viola_instrument_music_data.pitches,
    attachment_makers=Viola_instrument_music_data.attachments,
    override_makers=Viola_instrument_music_data.overrides,
    )
Viola_music = Viola_music_maker(
    time_signature_pairs=Viola_instrument_music_data.time_signature_pairs),
Viola_rhythm_definition.notes = Viola_music
Viola_rhythm_definition.instrument_name = 'Viola'


lilypond_file = segment_maker.run()
