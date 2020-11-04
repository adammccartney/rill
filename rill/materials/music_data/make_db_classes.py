import shelve

from rill.materials.music_init_data.definition import (
    SegmentPitchData,
    SegmentTaleaData,
)

from rill.materials.pitch.definition import chord_voice

db = shelve.open('music_data_shelve')

segment_TEST_cv3_pitch_materials = chord_voice["black"][5][0:3]
segment_TEST_cv3_pitch_materials += chord_voice["red"][5][0:3]
segment_TEST_cv3_pitches = str(segment_TEST_cv3_pitch_materials)

segment_TEST_pitch_data = SegmentPitchData(_chord_voice3=segment_TEST_cv3_pitches)
segment_TEST_talea_data = SegmentTaleaData()

db['segment_TEST_pitches'] = segment_TEST_pitch_data
db['segment_TEST_talea'] = segment_TEST_talea_data

db.close()

if __name__ == '__main__':
    db = shelve.open('music_data_shelve')
    for key in db:
        print(key)
    segment_TEST_pitch_data = db['segment_TEST_pitches']
    segment_TEST_talea_data = db['segment_TEST_talea']
    print(segment_TEST_pitch_data.chord_voice3)
    print(segment_TEST_talea_data)
    db.close()
