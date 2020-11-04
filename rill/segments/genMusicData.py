import sys

var = sys.argv[1]
segment_name = f"segment_{var}"  # used to recall music data from db


pitch_data_key = f"{segment_name}_pitches"
talea_data_key = f"{segment_name}_talea"

music_data = f"""
import shelve
import abjad

from pathlib import Path

from rill.materials.music_init_data.definition import InstrumentMusicData
from rill.materials.music_init_data.definition import SegmentMusicData


up_two_dirs = Path.cwd().parents[1] # ../segments/
db_path = up_two_dirs / 'materials' / 'music_data' / 'music_data_shelve'

db = shelve.open(str(db_path))

{segment_name}_pitch_data = db['{pitch_data_key}']
{segment_name}_talea_data = db['{talea_data_key}']

Flute1_music_data = InstrumentMusicData()
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
"""

output_file = open('music_data.py', 'w')
output_file.write(music_data)
output_file.close()
