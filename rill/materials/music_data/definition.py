import shelve
import copy

from rill.materials.music_init_data.definition import (
    SegmentPitchData,
    SegmentTaleaData,
)

from rill.materials.pitch.definition import chord_voice

db = shelve.open('music_data_shelve')

# Initialization pattern

segment_TEST_cv3_pitch_materials = chord_voice["black"][5][0:3]
segment_TEST_cv3_pitch_materials += chord_voice["red"][5][0:3]
segment_TEST_cv3_pitches = str(segment_TEST_cv3_pitch_materials)

segment_TEST_pitch_data = SegmentPitchData()
segment_TEST_pitch_data.chord_voice3 = segment_TEST_cv3_pitches
segment_TEST_talea_data = SegmentTaleaData()

db['segment_TEST_pitches'] = segment_TEST_pitch_data
db['segment_TEST_talea'] = segment_TEST_talea_data


"""
 Material initialized on the basis of the first harmonic block
 See etc/rillSketch2.jpg for details

 A, B, F, J <assigned> chord_material[0:2], melody1[:], tremolo["v1"]
 C, G, H, K <assigned> chord_material[3:5], melody2[:], tremolo["v2"]
 D, E, I, L <assigned> chord_material[6:8], melody3[:], tremolo["v3"]

"""

segment_A_cv1_pitch_materials = chord_voice["blue"][6][0:3]
segment_A_cv1_pitches = str(segment_A_cv1_pitch_materials)

segment_A_cv2_pitch_materials = chord_voice["green"][6][0:3]
segment_A_cv2_pitches = str(segment_A_cv2_pitch_materials)

segment_A_cv3_pitch_materials = chord_voice["black"][5][0:3]
segment_A_cv3_pitch_materials += chord_voice["red"][5][0:3]
segment_A_cv3_pitches = str(segment_A_cv3_pitch_materials)

segment_A_cv4_pitch_materials = chord_voice["black"][4][0:3]
segment_A_cv4_pitches = str(segment_A_cv4_pitch_materials)


segment_B_cv1_pitch_material = copy.deepcopy(segment_A_cv1_pitch_materials)
segment_B_cv1_transposed = segment_B_cv1_pitch_material.transpose(-12)
segment_B_cv1_pitches = str(segment_B_cv1_transposed)

segment_B_cv2_pitch_material = copy.deepcopy(segment_A_cv2_pitch_materials)
segment_B_cv2_transposed = segment_B_cv2_pitch_material.transpose(-12)
segment_B_cv2_pitches = str(segment_B_cv2_transposed)

segment_B_cv3_pitch_material = copy.deepcopy(segment_A_cv3_pitch_materials)
segment_B_cv3_transposed = segment_B_cv3_pitch_material.transpose(12)
segment_B_cv3_pitches = str(segment_B_cv3_transposed)

segment_B_cv4_pitch_material = copy.deepcopy(segment_A_cv4_pitch_materials)
segment_B_cv4_transposed = segment_B_cv4_pitch_material.transpose(12)
segment_B_cv4_pitches = str(segment_B_cv4_transposed)

segment_F_cv1_pitch_materials = chord_voice["blue"][6][0:3]
segment_F_cv1_pitches = str(segment_F_cv1_pitch_materials)

segment_F_cv2_pitch_materials = chord_voice["green"][6][0:3]
segment_F_cv2_pitches = str(segment_F_cv2_pitch_materials)

segment_F_cv3_pitch_materials = chord_voice["black"][5][0:3]
segment_F_cv3_pitch_materials += chord_voice["red"][5][0:3]
segment_F_cv3_pitches = str(segment_F_cv3_pitch_materials)

segment_F_cv4_pitch_materials = chord_voice["black"][4][0:3]
segment_F_cv4_pitches = str(segment_F_cv4_pitch_materials)

segment_J_cv1_pitch_materials = chord_voice["blue"][6][0:3]
segment_J_cv1_pitches = str(segment_J_cv1_pitch_materials)

segment_J_cv2_pitch_materials = chord_voice["green"][6][0:3]
segment_J_cv2_pitches = str(segment_J_cv2_pitch_materials)

segment_J_cv3_pitch_materials = chord_voice["black"][5][0:3]
segment_J_cv3_pitch_materials += chord_voice["red"][5][0:3]
segment_J_cv3_pitches = str(segment_J_cv3_pitch_materials)

segment_J_cv4_pitch_materials = chord_voice["black"][4][0:3]
segment_J_cv4_pitches = str(segment_J_cv4_pitch_materials)


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
