import sys

var = sys.argv[1]
seg_name = f"segment_{var}"  # used to recall music data from db


pitch_data_key = f"{seg_name}_pitch_data"
talea_data_key = f"{seg_name}_talea_data"
instr_pdref_key = f"{seg_name}_instrument_pitch_data_ref"

music_data = f"""
import shelve
import abjad

from pathlib import Path

from rill.materials.music_init_data.definition import InstrumentMusicData
from rill.materials.music_init_data.definition import SegmentMusicData


up_two_dirs = Path.cwd().parents[1] # ../rill/
db_path = up_two_dirs / 'materials' / 'music_data' / 'music_data_shelve'

db = shelve.open(str(db_path))

{seg_name}_pitch_data = db['{pitch_data_key}']
{seg_name}_talea_data = db['{talea_data_key}']
{seg_name}_instr_pdref = db['{instr_pdref_key}']


{seg_name}_Flute1_dref = {seg_name}_instr_pdref.Flute1
{seg_name}_Flute1_pd = getattr({seg_name}_pitch_data,
                                   segment_A_Flute1_instr_pdref)
{seg_name}_Flute1_pitch_segment = abjad.PitchSegment({seg_name}_Flute1_pd)
Flute1_music_data = InstrumentMusicData()
Flute1_music_data.pitches = {seg_name}_Flute1_pitch_segment

Flute2_music_data = InstrumentMusicData()
Flute3_music_data = InstrumentMusicData()
Flute4_music_data = InstrumentMusicData()

Bbclarinet1_music_data = InstrumentMusicData()

Vibraphone_music_data = InstrumentMusicData()

Violin1_music_data = InstrumentMusicData()
Violin2_music_data = InstrumentMusicData()
Violin3_music_data = InstrumentMusicData()
Violin4_music_data = InstrumentMusicData()
Violin5_music_data = InstrumentMusicData()
Violin6_music_data = InstrumentMusicData()
Violin7_music_data = InstrumentMusicData()
Viola_music_data = InstrumentMusicData()

segment_music_data = SegmentMusicData()

db.close()
"""

output_file = open('music_data.py', 'w')
output_file.write(music_data)
output_file.close()
