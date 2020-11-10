import shelve
import copy

from rill.materials.music_init_data.definition import (
    SegmentPitchData,
    SegmentTaleaData,
)

from rill.materials.pitch.definition import (
    chord_voice,
    melody_voice,
    tremolo_voice,
    )

from rill.tools.SequenceGenerator import SequenceGenerator as seq

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

# A

segment_A_cv1_pitch_materials = chord_voice["blue"][6][0:3]
segment_A_cv1_pitches = str(segment_A_cv1_pitch_materials)

segment_A_cv2_pitch_materials = chord_voice["green"][6][0:3]
segment_A_cv2_pitches = str(segment_A_cv2_pitch_materials)

segment_A_cv3_pitch_materials = chord_voice["black"][5][0:3]
segment_A_cv3_pitch_materials += chord_voice["red"][5][0:3]
segment_A_cv3_pitches = str(segment_A_cv3_pitch_materials)

segment_A_cv4_pitch_materials = chord_voice["black"][4][0:3]
segment_A_cv4_pitches = str(segment_A_cv4_pitch_materials)

segment_A_mv_materials = melody_voice["blue"]["p1"][4][:]
segment_A_mv_pitches = str(segment_A_mv_materials)

segment_A_tv1_materials = tremolo_voice["green"][6]["v1"][:]
segment_A_tv1_pitches = str(segment_A_tv1_materials)

segment_A_tv2_materials = tremolo_voice["black"][5]["v1"][:]
segment_A_tv2_pitches = str(segment_A_tv2_materials)

# B

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

segment_B_mv_materials = melody_voice["blue"]["p1"][6][:]
segment_B_mv_pitches = str(segment_B_mv_materials)

segment_B_tv1_materials = tremolo_voice["green"][5]["v1"][:]
segment_B_tv1_pitches = str(segment_B_tv1_materials)

segment_B_tv2_materials = tremolo_voice["black"][4]["v1"][:]
segment_B_tv2_pitches = str(segment_B_tv2_materials)


# C

segment_C_cv1_pitch_materials = chord_voice["blue"][6][3:5]
segment_C_cv1_pitches = str(segment_C_cv1_pitch_materials)

segment_C_cv2_pitch_materials = chord_voice["green"][6][3:5]
segment_C_cv2_pitches = str(segment_C_cv2_pitch_materials)

segment_C_cv3_pitch_materials = chord_voice["black"][5][3:5]
segment_C_cv3_pitch_materials += chord_voice["red"][5][3:5]
segment_C_cv3_pitches = str(segment_C_cv3_pitch_materials)

segment_C_cv4_pitch_materials = chord_voice["black"][4][3:5]
segment_C_cv4_pitches = str(segment_C_cv4_pitch_materials)

segment_C_mv_materials = melody_voice["blue"]["p2"][5][:]
segment_C_mv_pitches = str(segment_C_mv_materials)

segment_C_tv1_materials = tremolo_voice["green"][6]["v2"][:]
segment_C_tv1_pitches = str(segment_C_tv1_materials)

segment_C_tv2_materials = tremolo_voice["black"][5]["v2"][:]
segment_C_tv2_pitches = str(segment_C_tv2_materials)

# D

segment_D_cv1_pitch_materials = chord_voice["blue"][6][6:8]
segment_D_cv1_pitches = str(segment_D_cv1_pitch_materials)

segment_D_cv2_pitch_materials = chord_voice["green"][6][6:8]
segment_D_cv2_pitches = str(segment_D_cv2_pitch_materials)

segment_D_cv3_pitch_materials = chord_voice["black"][5][6:8]
segment_D_cv3_pitch_materials += chord_voice["red"][5][6:8]
segment_D_cv3_pitches = str(segment_D_cv3_pitch_materials)

segment_D_cv4_pitch_materials = chord_voice["black"][4][6:8]
segment_D_cv4_pitches = str(segment_D_cv4_pitch_materials)

segment_D_mv_materials = melody_voice["blue"]["p3"][6][:]
segment_D_mv_pitches = str(segment_D_mv_materials)

segment_D_tv3_materials = tremolo_voice["green"][6]["v3"][:]
segment_D_tv3_pitches = str(segment_D_tv3_materials)

segment_D_tv2_materials = tremolo_voice["black"][5]["v3"][:]
segment_D_tv2_pitches = str(segment_D_tv2_materials)

# E

segment_E_cv1_pitch_material = copy.deepcopy(segment_D_cv1_pitch_materials)
segment_E_cv1_transposed = segment_E_cv1_pitch_material.transpose(-12)
segment_E_cv1_pitches = str(segment_E_cv1_transposed)

segment_E_cv2_pitch_material = copy.deepcopy(segment_D_cv2_pitch_materials)
segment_E_cv2_transposed = segment_E_cv2_pitch_material.transpose(-12)
segment_E_cv2_pitches = str(segment_E_cv2_transposed)

segment_E_cv3_pitch_material = copy.deepcopy(segment_D_cv3_pitch_materials)
segment_E_cv3_transposed = segment_E_cv3_pitch_material.transpose(12)
segment_E_cv3_pitches = str(segment_E_cv3_transposed)

segment_E_cv4_pitch_material = copy.deepcopy(segment_D_cv4_pitch_materials)
segment_E_cv4_transposed = segment_E_cv4_pitch_material.transpose(12)
segment_E_cv4_pitches = str(segment_E_cv4_transposed)

segment_E_mv_materials = melody_voice["blue"]["p3"][8][:]
segment_E_mv_pitches = str(segment_E_mv_materials)

segment_E_tv1_materials = tremolo_voice["green"][5]["v3"][:]
segment_E_tv1_pitches = str(segment_E_tv1_materials)

segment_E_tv2_materials = tremolo_voice["black"][4]["v3"][:]
segment_E_tv2_pitches = str(segment_E_tv2_materials)

# F

segment_F_cv1_pitch_materials = chord_voice["blue"][5][0:3]
segment_F_cv1_pitches = str(segment_F_cv1_pitch_materials)

segment_F_cv2_pitch_materials = chord_voice["green"][5][0:3]
segment_F_cv2_pitches = str(segment_F_cv2_pitch_materials)

segment_F_cv3_pitch_materials = chord_voice["red"][5][0:3].retrograde()
segment_F_cv3_pitch_materials += chord_voice["black"][5][0:3].retrograde()
segment_F_cv3_pitches = str(segment_F_cv3_pitch_materials)

segment_F_cv4_pitch_materials = chord_voice["black"][5][0:3]
segment_F_cv4_pitches = str(segment_F_cv4_pitch_materials)

segment_F_mv_materials = melody_voice["blue"]["p1"][3][:]
segment_F_mv_pitches = str(segment_F_mv_materials)

segment_F_tv1_materials = tremolo_voice["green"][5]["v1"][:]
segment_F_tv1_pitches = str(segment_F_tv1_materials)

segment_F_tv2_materials = tremolo_voice["black"][5]["v1"][:]
segment_F_tv2_pitches = str(segment_F_tv2_materials)

# G

segment_G_cv1_pitch_material = copy.deepcopy(segment_C_cv1_pitch_materials)
segment_G_cv1_transposed = segment_G_cv1_pitch_material.transpose(-12)
segment_G_cv1_pitches = str(segment_G_cv1_transposed)

segment_G_cv2_pitch_material = copy.deepcopy(segment_C_cv2_pitch_materials)
segment_G_cv2_transposed = segment_G_cv2_pitch_material.transpose(-12)
segment_G_cv2_pitches = str(segment_G_cv2_transposed)

segment_G_cv3_pitch_material = copy.deepcopy(segment_C_cv3_pitch_materials)
segment_G_cv3_transposed = segment_G_cv3_pitch_material.transpose(12).retrograde()
segment_G_cv3_pitches = str(segment_G_cv3_transposed)

segment_G_cv4_pitch_material = copy.deepcopy(segment_C_cv4_pitch_materials)
segment_G_cv4_transposed = segment_G_cv4_pitch_material.transpose(12)
segment_G_cv4_pitches = str(segment_G_cv4_transposed)

segment_G_mv_materials = melody_voice["blue"]["p2"][4][:]
segment_G_mv_pitches = str(segment_G_mv_materials)

segment_G_tv1_materials = tremolo_voice["green"][5]["v2"][:]
segment_G_tv1_pitches = str(segment_G_tv1_materials)

segment_G_tv2_materials = tremolo_voice["black"][4]["v2"][:]
segment_G_tv2_pitches = str(segment_G_tv2_materials)

# H

segment_H_cv1_pitch_materials = chord_voice["blue"][5][3:5]
segment_H_cv1_pitches = str(segment_H_cv1_pitch_materials)

segment_H_cv2_pitch_materials = chord_voice["green"][5][3:5]
segment_H_cv2_pitches = str(segment_H_cv2_pitch_materials)

segment_H_cv3_pitch_materials = chord_voice["black"][5][3:5].retrograde()
segment_H_cv3_pitch_materials += chord_voice["red"][5][3:5].retrograde()
segment_H_cv3_pitches = str(segment_H_cv3_pitch_materials)

segment_H_cv4_pitch_materials = chord_voice["black"][5][3:5]
segment_H_cv4_pitches = str(segment_H_cv4_pitch_materials)

segment_H_mv_materials = melody_voice["blue"]["p2"][3][:]
segment_H_mv_pitches = str(segment_H_mv_materials)

segment_H_tv1_materials = tremolo_voice["green"][5]["v2"][:]
segment_H_tv1_pitches = str(segment_H_tv1_materials)

segment_H_tv2_materials = tremolo_voice["black"][5]["v2"][:]
segment_H_tv2_pitches = str(segment_H_tv2_materials)

# I

segment_I_cv1_pitch_materials = chord_voice["blue"][5][6:8]
segment_I_cv1_pitches = str(segment_I_cv1_pitch_materials)

segment_I_cv2_pitch_materials = chord_voice["green"][5][6:8]
segment_I_cv2_pitches = str(segment_I_cv2_pitch_materials)

segment_I_cv3_pitch_materials = chord_voice["red"][5][6:8].retrograde()
segment_I_cv3_pitch_materials += chord_voice["black"][5][6:8].retrograde()
segment_I_cv3_pitches = str(segment_I_cv3_pitch_materials)

segment_I_cv4_pitch_materials = chord_voice["black"][5][6:8]
segment_I_cv4_pitches = str(segment_I_cv4_pitch_materials)

segment_I_mv_materials = melody_voice["blue"]["p3"][10][:]
segment_I_mv_pitches = str(segment_I_mv_materials)

segment_I_tv1_materials = tremolo_voice["green"][5]["v3"][:]
segment_I_tv1_pitches = str(segment_I_tv1_materials)

segment_I_tv2_materials = tremolo_voice["black"][5]["v3"][:]
segment_I_tv2_pitches = str(segment_I_tv2_materials)


# J

segment_J_cv1_pitch_materials = chord_voice["blue"][6][0:3]
segment_J_cv1_pitches = str(segment_J_cv1_pitch_materials)

segment_J_cv2_pitch_materials = chord_voice["green"][6][0:3]
segment_J_cv2_pitches = str(segment_J_cv2_pitch_materials)

segment_J_cv3_pitch_materials = chord_voice["black"][5][0:3].rotate(n=1)
segment_J_cv3_pitch_materials += chord_voice["red"][5][0:3].rotate(n=1)
segment_J_cv3_pitches = str(segment_J_cv3_pitch_materials)

segment_J_cv4_pitch_materials = chord_voice["black"][4][0:3]
segment_J_cv4_pitches = str(segment_J_cv4_pitch_materials)

segment_J_mv_materials = melody_voice["blue"]["p1"][5][:]
segment_J_mv_pitches = str(segment_J_mv_materials)

segment_J_tv1_materials = tremolo_voice["green"][6]["v1"][:]
segment_J_tv1_pitches = str(segment_J_tv1_materials)

segment_J_tv2_materials = tremolo_voice["black"][4]["v1"][:]
segment_J_tv2_pitches = str(segment_J_tv2_materials)


# K

segment_K_cv1_pitch_materials = chord_voice["blue"][6][3:5]
segment_K_cv1_pitches = str(segment_K_cv1_pitch_materials)

segment_K_cv2_pitch_materials = chord_voice["green"][6][3:5]
segment_K_cv2_pitches = str(segment_K_cv2_pitch_materials)

segment_K_cv3_pitch_materials = chord_voice["black"][5][3:5].rotate(n=1)
segment_K_cv3_pitch_materials += chord_voice["red"][5][3:5].rotate(n=1)
segment_K_cv3_pitches = str(segment_K_cv3_pitch_materials)

segment_K_cv4_pitch_materials = chord_voice["black"][4][3:5]
segment_K_cv4_pitches = str(segment_K_cv4_pitch_materials)

segment_K_mv_materials = melody_voice["blue"]["p2"][2][:]
segment_K_mv_pitches = str(segment_G_mv_materials)

segment_K_tv1_materials = tremolo_voice["green"][6]["v2"][:]
segment_K_tv1_pitches = str(segment_K_tv1_materials)

segment_K_tv2_materials = tremolo_voice["black"][4]["v2"][:]
segment_K_tv2_pitches = str(segment_K_tv2_materials)


# L


segment_L_cv1_pitch_materials = chord_voice["blue"][6][6:8]
segment_L_cv1_pitches = str(segment_L_cv1_pitch_materials)

segment_L_cv2_pitch_materials = chord_voice["green"][6][6:8]
segment_L_cv2_pitches = str(segment_L_cv2_pitch_materials)

segment_L_cv3_pitch_materials = chord_voice["black"][5][6:8].rotate(n=1)
segment_L_cv3_pitch_materials += chord_voice["red"][5][6:8].rotate(n=1)
segment_L_cv3_pitches = str(segment_L_cv3_pitch_materials)

segment_L_cv4_pitch_materials = chord_voice["black"][4][6:8]
segment_L_cv4_pitches = str(segment_L_cv4_pitch_materials)

segment_L_mv_materials = melody_voice["blue"]["p3"][1][:]
segment_L_mv_pitches = str(segment_G_mv_materials)

segment_L_tv1_materials = tremolo_voice["green"][6]["v3"][:]
segment_L_tv1_pitches = str(segment_L_tv1_materials)

segment_L_tv2_materials = tremolo_voice["black"][4]["v3"][:]
segment_L_tv2_pitches = str(segment_L_tv2_materials)










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
