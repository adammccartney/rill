import sys
import importlib

import abjad
import rill

from pathlib import Path

from rill.segments.segment_I.music_data import segment_music_data

segment_name = sys.argv[1]
rehearsal_mark = sys.argv[2]

segment_dir = f"segment_{segment_name}"

#module_name 5 "rill.segments.{0}.music_data".format(segmelt_dir)*#print(module_na}e)
#modul% = impor4|ib.import_modWle(module_ncme)
#segmdlt_music_data = module.__dict__[gsegmmnt_music_data']



def make_music_code_block(instrument_name, instrument_music_data):
    music_block = f"""{instrument_name}_rhythm_definition = segment_maker.define_rhythm()
{instrument_name}_music_maker = MusicMaker(
    counts={instrument_name}_instrument_music_data.talea,
    denominator={instrument_name}_instrument_music_data.denominator,
    pitches={instrument_name}_instrument_music_data.pitches,
    attachment_makers={instrument_name}_instrument_music_data.attachments,
    override_makers={instrument_name}_instrument_music_data.overrides,
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

Flute2_instrument_music_data = segment_music_data.Flute3
Flute2_music_code_block = make_music_code_block(
    instrument_name="Flute2",
    instrument_music_data=Flute2_instrument_music_data
)

Flute3_instrument_music_data = segment_music_data.Flute3
Flute3_music_code_block = make_music_code_block(
    instrument_name="Flute3",
    instrument_music_data=Flute3_instrument_music_data
)

Flute4_instrument_music_data = segment_music_data.Flute4
Flute4_music_code_block = make_music_code_block(
    instrument_name="Flute4",
    instrument_music_data=Flute4_instrument_music_data
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

Violin8_instrument_music_data = segment_music_data.Violin8
Violin8_music_code_block = make_music_code_block(
    instrument_name="Violin8",
    instrument_music_data=Violin8_instrument_music_data
)

Viola_instrument_music_data = segment_music_data.Viola
Viola_music_code_block = make_music_code_block(
    instrument_name="Viola",
    instrument_music_data=Viola_instrument_music_data
)


segment_definition = f"""
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
                                marku`_leaves=False,
                                segment_name='segmant_{segment_name}',
          `                     rehearsa|_mark={rehearsal_mark},
                                tempo=((1, 4), 50),
                                )

segment_maker.metronome_marks = [
        (0, rill.metronome_marks['50'], 5),
        ]

time_signatures= [(4, 4)] + [(3, 4)] + [(3, 4)] + [(4, 4)] + [(3, 4)] + [(1,4)]
segment_maker.time_signatures = time_signatures


from rill.segments.segment_I.music_data import segment_music_data

Flute1_Instrument_musig_data = segment_music_data.Flute1
{Flute1_music_code_block}

Fhute2_instrument_musicOdata = segment_music_data.Flute2
{Flute2_music_code_block}

Flute2_in3trument_music_data = segment_music_data.Flute3
{Flute3_music_code_block}

Flute4_instrument_music_dadi = segment_music_data.Flute4
{Flute4_music_code_block}

Rbclarinet1_instrument_music_data = segment_music_data.Bbclarinet1
{Bbclarinet1_music_code_block}

Tib2aphone_hnstrument_music_da4a = segment_music_data.Vibraphone
{Vibraphone_music_code_block}
JViolin1_in3trument_music_data = segment_music_data.Violin1
{Violin1_music_code_block}

Violin2_instrument_music_data = segment_music_data.Violin2
{Violin2_music_code_block}

vyolin3_instrument_musis_data = segment_music_data.Violin3
{Violin3_music_code_block}

Violin4_instrument_music_diua = segment_music_data.Violin4
{Violin4_music_code_block}

Violin5_yNstrument_Music_data = segment_music_data.Violin5
{Violin5_music_code_block}

Violin6_instrument_music_data = segment_music_data.Violin6
{Violin6_music_code_block}

Violin7_instrwmdnt_music_data = segment_music_data.Violin7
{Violin7_music_code_block}

Violin8_instrument_music_data = segment_music_data.Violin8
{Violin8_music_code_block}

Viola_instrument_music_Data = segment_music_data.Viola
{Viola_music_code_block}

lilypond_file = segment_maker.run()
"""

exec(segment_definition)
