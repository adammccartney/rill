import sys

import abjad
import rill

segment_name = sys.argv[1]
rehearsal_mark = sys.argv[2]


# Switch over segment_name to make assignments

# Test variables

def make_music_code_block(instrument_name):
    music_block = f"""{instrument_name}_rhythm_definition = segment_maker.define_rhythm()
{instrument_name}_music_maker = MusicMaker(
    counts=test_counts,
    denominator=test_denominator,
    pitches=test_pitches,
    attachment_makers=[
                    tenuto_attachment_maker,
                    staccato_attachment_maker
                    ],
    )
{instrument_name}_music = {instrument_name}_music_maker(time_signature_pairs=test_ts_pairs),
{instrument_name}_rhythm_definition.notes = {instrument_name}_music
{instrument_name}_rhythm_definition.instrument_name = \"{instrument_name}\"
"""
    return music_block


Flute1_music_code_block = make_music_code_block(instrument_name="Flute1")
Flute2_music_code_block = make_music_code_block(instrument_name="Flute2")
Flute3_music_code_block = make_music_code_block(instrument_name="Flute3")
Bbclarinet1_music_code_block = make_music_code_block(
    instrument_name="Bbclarinet1")


Vibraphone_music_code_block = make_music_code_block(
    instrument_name="Vibraphone")

Violin1_music_code_block = make_music_code_block(instrument_name="Violin1")
Violin2_music_code_block = make_music_code_block(instrument_name="Violin2")
Violin3_music_code_block = make_music_code_block(instrument_name="Violin3")
Violin4_music_code_block = make_music_code_block(instrument_name="Violin4")
Violin5_music_code_block = make_music_code_block(instrument_name="Violin5")
Violin6_music_code_block = make_music_code_block(instrument_name="Violin6")
Violin7_music_code_block = make_music_code_block(instrument_name="Violin7")
Viola_music_code_block = make_music_code_block(instrument_name="Viola")


segment_definition = f"""
import copy
import pathlib

import abjad
import rill


from rill.tools.MusicMaker import MusicMaker as MusicMaker
from rill.tools.AttachmentMaker import (
                                        AccentAttachmentMaker
                                        as AccentAttachmentMaker
                                       )

from rill.materials.music_init_data.definition import InstrumentMusicData


this_current_directory =  pathlib.Path.cwd().parent
score =rill.ScoreTemplate()
score_template = score()

segment_maker = rill.SegmentMaker(
                                _lilypond_file=None,
                                _score=score_template,
                                current_directory=this_current_directory,
                                build_path=rill.build_path,
                                markup_leaves=False,
                                segment_name='segment_{segment_name}',
                                rehearsal_mark={rehearsal_mark},
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


{Flute1_music_code_block}

{Flute2_music_code_block}

{Flute3_music_code_block}

{Bbclarinet1_music_code_block}



{Vibraphone_music_code_block}



{Violin1_music_code_block}

{Violin2_music_code_block}

{Violin3_music_code_block}

{Violin4_music_code_block}

{Violin5_music_code_block}

{Violin6_music_code_block}

{Violin7_music_code_block}

{Viola_music_code_block}


lilypond_file = segment_maker.run()
"""

output_file = open('definition.py', 'w')
output_file.write(segment_definition)
output_file.close()
