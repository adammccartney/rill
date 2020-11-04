import shelve

from rill.materials.music_init_data.definition import (
    SegmentPitchData,
)

from rill.materials.pitch.definition import chord_voice

db = shelve.open('music_data_shelve')

segmentA_cv3_pitch_materials = chord_voice["black"][5][0:3]
segmentA_cv3_pitch_materials += chord_voice["red"][5][0:3]
segmentA_cv3_pitches = str(segmentA_cv3_pitch_materials)

segmentA_pitch_data = SegmentPitchData(_chord_voice3=segmentA_cv3_pitches)


db['segment_A_pitches'] = segmentA_pitch_data

db.close()

if __name__ == '__main__':
    db = shelve.open('music_data_shelve')
    for key in db:
        print(key)
    segment_A_pitch_data = db['segment_A_pitches']
    print(segment_A_pitch_data.chord_voice3)
    db.close()
