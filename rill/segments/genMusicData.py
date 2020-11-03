music_data = f"""
from rill.materials.music_init_data.definition import InstrumentMusicData
from rill.materials.music_init_data.definition import SegmentMusicData


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
