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
print(segment_A_pitch_data)

segment_A_cv3 = segment_A_pitch_data.chord_voice3

def replace_brackets(pitch_segment_as_string):
    pitch_segment = re.sub(r'<|>', r'"', pitch_segment_as_string)
    return pitch_segment

segment_A_cv3_string = replace_brackets(segment_A_cv3)

print(segment_A_cv3_string)

#cv3_pitch_segment = abjad.PitchSegment(segment_A_cv3)

#test_pitch_segment = abjad.PitchSegment("<c' d' e'>")

db.close()

if __name__ == '__main__':
    print(segment_A_cv3)
    print(segment_A_cv3_string)
