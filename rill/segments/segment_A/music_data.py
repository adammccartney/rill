
import shelve
import abjad

from pathlib import Path

from rill.materials.music_init_data.definition import InstrumentMusicData
from rill.materials.music_init_data.definition import SegmentMusicData


up_two_dirs = Path.cwd().parents[1] # ../rill/
db_path = up_two_dirs / 'materials' / 'music_data' / 'music_data_shelve'

db = shelve.open(str(db_path))

segment_A_pitch_data = db['segment_A_pitch_data']
segment_A_talea_data = db['segment_A_talea_data']

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

db.close()
