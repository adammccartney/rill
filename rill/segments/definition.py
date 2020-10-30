
import copy
import pathlib

import abjad
import rill


from rill.tools.MusicMaker import MusicMaker as MusicMaker
from rill.tools.MusicMaker import mMakerGenerator as mMakerGenerator
from rill.tools.MusicMaker import AccentAttachmentMaker as AccentAttachmentMaker

this_current_directory =  pathlib.Path(__file__).parent 
score =rill.ScoreTemplate()
score_template = score()

segment_maker = rill.SegmentMaker(
                                _lilypond_file=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=rill.build_path,
                                markup_leaves=False,
                                segment_name='segment_A',
                                rehearsal_mark=1,
                                tempo=((1, 4), 50),
                                )

segment_maker.metronome_marks = [
        (0, rill.metronome_marks['50'], 5),
        ]

time_signatures= [(4, 4)] + [(3, 4)] + [(3, 4)] + [(4, 4)] + [(3, 4)] + [(3,4)]
segment_maker.time_signatures = time_signatures

# Test variables

test_pitches = rill.chord_voice["blue"][5][1:3]

test_ts_pairs = [(4, 4), (3, 4), (3, 4), (4, 4), (3, 4), (3, 4)]
test_counts = [1, 2, -3, 4]
test_denominator = 8
test_pitches = abjad.CyclicTuple(test_pitches)

tenuto_attachment_maker = AccentAttachmentMaker(
    selector=abjad.select().logical_ties(),
    attachment=abjad.Articulation("tenuto")
)

staccato_attachment_maker = AccentAttachmentMaker(
    selector=abjad.select().logical_ties(),
    attachment=abjad.Staccato()
)


Flute1_rhythm_definition = segment_maker.define_rhythm()
Flute1_music_generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    time_signature_pairs=test_ts_pairs,
    )
Flute1_music = Flute1_music_generator()
Flute1_rhythm_definition.notes = [Flute1_music]
Flute1_rhythm_definition.instrument_name = "Flute1"


Flute2_rhythm_definition = segment_maker.define_rhythm()
Flute2_music_generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    time_signature_pairs=test_ts_pairs,
    )
Flute2_music = Flute2_music_generator()
Flute2_rhythm_definition.notes = [Flute2_music]
Flute2_rhythm_definition.instrument_name = "Flute2"


Flute3_rhythm_definition = segment_maker.define_rhythm()
Flute3_music_generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    time_signature_pairs=test_ts_pairs,
    )
Flute3_music = Flute3_music_generator()
Flute3_rhythm_definition.notes = [Flute3_music]
Flute3_rhythm_definition.instrument_name = "Flute3"


Bbclarinet1_rhythm_definition = segment_maker.define_rhythm()
Bbclarinet1_music_generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    time_signature_pairs=test_ts_pairs,
    )
Bbclarinet1_music = Bbclarinet1_music_generator()
Bbclarinet1_rhythm_definition.notes = [Bbclarinet1_music]
Bbclarinet1_rhythm_definition.instrument_name = "Bbclarinet1"




Vibraphone_rhythm_definition = segment_maker.define_rhythm()
Vibraphone_music_generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    time_signature_pairs=test_ts_pairs,
    )
Vibraphone_music = Vibraphone_music_generator()
Vibraphone_rhythm_definition.notes = [Vibraphone_music]
Vibraphone_rhythm_definition.instrument_name = "Vibraphone"




Violin1_rhythm_definition = segment_maker.define_rhythm()
Violin1_music_generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    time_signature_pairs=test_ts_pairs,
    )
Violin1_music = Violin1_music_generator()
Violin1_rhythm_definition.notes = [Violin1_music]
Violin1_rhythm_definition.instrument_name = "Violin1"


Violin2_rhythm_definition = segment_maker.define_rhythm()
Violin2_music_generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    time_signature_pairs=test_ts_pairs,
    )
Violin2_music = Violin2_music_generator()
Violin2_rhythm_definition.notes = [Violin2_music]
Violin2_rhythm_definition.instrument_name = "Violin2"


Violin3_rhythm_definition = segment_maker.define_rhythm()
Violin3_music_generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    time_signature_pairs=test_ts_pairs,
    )
Violin3_music = Violin3_music_generator()
Violin3_rhythm_definition.notes = [Violin3_music]
Violin3_rhythm_definition.instrument_name = "Violin3"


Violin4_rhythm_definition = segment_maker.define_rhythm()
Violin4_music_generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    time_signature_pairs=test_ts_pairs,
    )
Violin4_music = Violin4_music_generator()
Violin4_rhythm_definition.notes = [Violin4_music]
Violin4_rhythm_definition.instrument_name = "Violin4"


Violin5_rhythm_definition = segment_maker.define_rhythm()
Violin5_music_generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    time_signature_pairs=test_ts_pairs,
    )
Violin5_music = Violin5_music_generator()
Violin5_rhythm_definition.notes = [Violin5_music]
Violin5_rhythm_definition.instrument_name = "Violin5"


Violin6_rhythm_definition = segment_maker.define_rhythm()
Violin6_music_generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    time_signature_pairs=test_ts_pairs,
    )
Violin6_music = Violin6_music_generator()
Violin6_rhythm_definition.notes = [Violin6_music]
Violin6_rhythm_definition.instrument_name = "Violin6"


Violin7_rhythm_definition = segment_maker.define_rhythm()
Violin7_music_generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    time_signature_pairs=test_ts_pairs,
    )
Violin7_music = Violin7_music_generator()
Violin7_rhythm_definition.notes = [Violin7_music]
Violin7_rhythm_definition.instrument_name = "Violin7"


Viola_rhythm_definition = segment_maker.define_rhythm()
Viola_music_generator = mMakerGenerator(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    time_signature_pairs=test_ts_pairs,
    )
Viola_music = Viola_music_generator()
Viola_rhythm_definition.notes = [Viola_music]
Viola_rhythm_definition.instrument_name = "Viola"



lilypond_file = segment_maker.run()
