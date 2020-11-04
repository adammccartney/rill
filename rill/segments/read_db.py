import shelve
import re

from pathlib import Path

parent = Path.cwd().parent
db_path = parent / 'materials' / 'music_data' / 'music_data_shelve'

print(db_path)

db = shelve.open(str(db_path))

#for key in db:
#    print(key)

import abjad


segment_A_pitch_data = db['segment_A_pitches']
print(type(segment_A_pitch_data))

segment_A_cv3 = segment_A_pitch_data.chord_voice3

print("segment_A_cv3:", type(segment_A_cv3))

test_pitch_segment = abjad.PitchSegment(segment_A_cv3)

db.close()
