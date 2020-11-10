import sys

import abjad
import rill

from pathlib import Path

from rill.segments.music_data import segment_music_data


segment_name = sys.argv[1]
rehearsal_mark = sys.argv[2]


def make_music_code_block(instrument_name, instrument_music_data):
    music_block = f"""{instrument_name}_rhythm_definition = segment_maker.define_rhythm()
{instrument_name}_music_maker = MusicMaker(
    counts={instrument_name}_instrument_music_data.talea,
    denominator={instrument_name}_instrument_music_data.denominator,
    pitches={instrument_name}_instrument_music_data.pitches,
    attachment_makers={instrument_name}_instrument_music_data.attachments
    )
{instrument_name}_music = {instrument_name}_music_maker(
    time_signature_pairs={instrument_name}_instrument_music_data.time_signature_pairs),
{instrument_name}_rhythm_definition.notes = {instrument_name}_music
{instrument_name}_rhythm_definition.instrument_name = '{instrument_name}'
"""
    return music_block


Flute1_instrument_music_data = segment_music_data.Flute1
Flute1_music_code_block = make_music_code_block(
    instrument_name="Flute1",
    instrument_music_data=Flute1_instrument_music_data
)

Flute2_instrument_music_data = segment_music_data.Flute2
Flute2_music_code_block = make_music_code_block(
    instrument_name="Flute2",
    instrument_music_data=Flute2_instrument_music_data
)

Flute3_instrument_music_data = segment_music_data.Flute3
Flute3_music_code_block = make_music_code_block(
    instrument_name="Flute3",
    instrument_music_data=Flute3_instrument_music_data
)

Bbclarinet1_instrument_music_data = segment_music_data.Bbclarinet1
Bbclarinet1_music_code_block = make_music_code_block(
    instrument_name="Bbclarinet1",
    instrument_music_data=Bbclarinet1_instrument_music_data
)

Vibraphone_instrument_music_data = segment_music_data.Vibraphone
Vibraphone_music_code_block = make_music_code_block(
    instrument_name="Vibraphone",
    instrument_music_data=Vibraphone_instrument_music_data
)

Violin1_instrument_music_data = segment_music_data.Violin1
Violin1_music_code_block = make_music_code_block(
    instrument_name="Violin1",
    instrument_music_data=Violin1_instrument_music_data
)

Violin2_instrument_music_data = segment_music_data.Violin2
Violin2_music_code_block = make_music_code_block(
    instrument_name="Violin2",
    instrument_music_data=Violin2_instrument_music_data
)

Violin3_instrument_music_data = segment_music_data.Violin3
Violin3_music_code_block = make_music_code_block(
    instrument_name="Violin3",
    instrument_music_data=Violin3_instrument_music_data
)

Violin4_instrument_music_data = segment_music_data.Violin4
Violin4_music_code_block = make_music_code_block(
    instrument_name="Violin4",
    instrument_music_data=Violin4_instrument_music_data
)

Violin5_instrument_music_data = segment_music_data.Violin5
Violin5_music_code_block = make_music_code_block(
    instrument_name="Violin5",
    instrument_music_data=Violin5_instrument_music_data
)

Violin6_instrument_music_data = segment_music_data.Violin6
Violin6_music_code_block = make_music_code_block(
    instrument_name="Violin6",
    instrument_music_data=Violin6_instrument_music_data
)

Violin7_instrument_music_data = segment_music_data.Violin7
Violin7_music_code_block = make_music_code_block(
    instrument_name="Violin7",
    instrument_music_data=Violin7_instrument_music_data
)

Viola_instrument_music_data = segment_music_data.Viola
Viola_music_code_block = make_music_code_block(
    instrument_name="Viola",
    instrument_music_data=Viola_instrument_music_data
)


segment_definition = f"""
import copy
import pathlib

import abjad
import rill


from rill.tools.MusicMaker import MusicMaker
from rill.tools.AttachmentMaker import AccentAttachmentMaker

this_current_directory =  pathlib.Path.cwd()
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


from rill.segments.music_data import segment_music_data


segment_music_dict = segment_music_data.instrument_music_data

Flute1_instrument_music_data = segment_music_dict['Flute1']
{Flute1_music_code_block}

Flute2_instrument_music_data = segment_music_dict['Flute2']
{Flute2_music_code_block}

Flute3_instrument_music_data = segment_music_dict['Flute3']
{Flute3_music_code_block}

Bbclarinet1_instrument_music_data = segment_music_dict['Bbclarinet1']
{Bbclarinet1_music_code_block}

Vibraphone_instrument_music_data = segment_music_dict['Vibraphone']
{Vibraphone_music_code_block}

Violin1_instrument_music_data = segment_music_dict['Violin1']
{Violin1_music_code_block}

Violin2_instrument_music_data = segment_music_dict['Violin2']
{Violin2_music_code_block}

Violin3_instrument_music_data = segment_music_dict['Violin3']
{Violin3_music_code_block}

Violin4_instrument_music_data = segment_music_dict['Violin4']
{Violin4_music_code_block}

Violin5_instrument_music_data = segment_music_dict['Violin5']
{Violin5_music_code_block}

Violin6_instrument_music_data = segment_music_dict['Violin6']
{Violin6_music_code_block}

Violin7_instrument_music_data = segment_music_dict['Violin7']
{Violin7_music_code_block}

Viola_instrument_music_data = segment_music_dict['Viola']
{Viola_music_code_block}

lilypond_file = segment_maker.run()
"""


cwd = Path.cwd()
target = cwd / segment_name / 'definition.py'
output_file = open(target, 'w')
output_file.write(segment_definition)
output_file.close()
