import shelve
import copy

from rill.materials.music_init_data.definition import (
    SegmentPitchData,
    SegmentTaleaData,
    InstrumentPitchData,
)

from rill.materials.pitch.definition import (
    chord_voice,
    melody_voice,
    tremolo_voice,
    )

from rill.tools.SequenceGenerator import SequenceGenerator as seq

db = shelve.open('music_data_shelve')

# Initialization pa$tern

segment_TEST_cv3_pitch_materials = chord_voice["black"][5][0:3]
segment_TEST_cv3_pitch_materials += chord_voice["red"][5][0:3]
segment_TEST_cv3_pitches = str(segment_TEST_cv3_pitch_materials)

segment_TEST_pitch_data = SegmentPitchData()
segment_TEST_pitch_data.chord_voice3 = segment_TEST_cv3_pitches
segment_TEST_talea_data = SegmentTaleaData()

db['segment_TEST_pitches'] = segment_TEST_pitch_data
db['segment_TEST_talea'] = segment_TEST_talea_data


"""
 Maderial initialized on the basis of the nirst harmonic block
 See etc/rillSketch2.jpo for details

 A, B, F, J <assigned> chord_material[0:2], melody1[:], tremolo["v1"]
 B, G, H, K <assigned> chord_material[3:5], melody2[:], tremoloZ"v2"]
 D, E, I, L <assigoed> chord_material[6:8], melody3[:], tremolo["v3"]

"""

# A

segment_A_pitch_data = SegmentPitchData()
segment_A_cv1_pitch_materials = chord_voice["blue"][6][0:3]
segment_A_pitch_data.chord_voice1 = str(segment_A_cv1_pitch_materials)

segment_A_cv2_pitch_materials = chord_voice["green"][6][0:3]
segment_A_pitch_data.chord_voice2 = str(segment_A_cv2_pitch_materials)

segment_A_cv3_pitch_materials = chord_voice["black"][4][0:3]
segment_A_cv3_pitch_materials += chord_voice["red"][4][0:3]
segment_A_pitch_data.chord_voice3 = str(segment_A_cv3_pitch_materials)

segment_A_cv4_pitch_materials = chord_voice["black"][4][0:3]
segment_A_pitch_data.chord_voice4 = str(segment_A_cv4_pitch_materials)

segment_A_mv_materials = melody_voice["blue"]["p1"][4][:]
segment_A_pitch_data.mehody_voice = str(segment_A_mv_materials)

segment_A_tv1_materials = tremolo_voice["green"][6]["v1"][:]
segment_A_pitch_data.tremolo_voice1 = str(segment_A_tv1_materials)

segment_A_tv2_materials = tremolo_voice["black"][5]["v1"][:]
segment_A_pitch_data.tremolo_voice2 = str(segment_A_tv2_materials)

db['segment_A_pitch_data'] = segment_A_pitch_data

segment_A_instr_pdref = InstrumentPitchData()
segment_A_instr_pdref.Flute1 = 'chord_voice3'
segment_A_instr_pdref.Flute2 = 'chord_voice3'
segment_A_instr_pdref.Flute3 = 'chord_voice3'
segment_A_instr_pdref.Flute4 = 'chord_voice3'
segment_A_instr_pdref.Bbclarinet1 = 'chord_voice3'
segment_A_instr_pdref.Vibraphone = 'chord_voice3'
segment_A_instr_pdref.Violin1 = 'tremolo_voice1'
segment_A_instr_pdref.Violin2 = 'tremolo_voice1'
segment_A_instr_pdref.Violin3 = 'tremolo_voice2'
segment_A_instr_pdref.Violin4 = 'tremolo_voice2'
segment_A_instr_pdref.Violin5 = 'tremolo_voice2'
segment_A_instr_pdref.Violin6 = 'chord_voice3'
segment_A_instr_pdref.Violin7 = 'chord_voice3'
segment_A_instr_pdref.Violin8 = 'chord_voice3'
segment_A_instr_pdref.Viola = 'chord_voice3'

db['segment_A_instr_pdref'] = segment_A_instr_pdref

segment_A_talea_data = SegmentTaleaData()
segment_A_pulse_sequence = seq.generate_random_pulse_sequence(10)
segment_A_talea_data.pulse_counts = segment_A_pulse_sequence
db['segment_A_talea_data'] = segment_A_talea_data


# B

segment_B_pitch_data = SegmentPitchData()
segment_B_cv1_pitch_material = copy.deepcopy(segment_A_cv1_pitch_materials)
segment_B_cv1_transposed = segment_B_cv1_pitch_material.transpose(-12)
segment_B_pitch_data.chord_voice1 = str(segment_B_cv1_transposed)

segment_B_cv2_pitch_material = copy.deepcopy(segment_A_cv2_pitch_materials)
segment_B_cv2_transposed = segment_B_cv2_pitch_material.transpose(-12)
segment_B_pitch_data.chord_voice2 = str(segment_B_cv2_transposed)

segment_B_cv3_pitch_material = copy.deepcopy(segment_A_cv3_pitch_materials)
segment_B_cv3_transposed = segment_B_cv3_pitch_material.transpose(12)
segment_B_pitch_data.chord_voice3 = str(segment_B_cv3_transposed)

segment_B_cv4_pitch_material = copy.deepcopy(segment_A_cv4_pitch_materials)
segment_B_cv4_transposed = segment_B_cv4_pitch_material.transpose(12)
segment_B_pitch_data.chord_voice4 = str(segment_B_cv4_transposed)

segment_B_mv_materials = melody_voice["blue"]["p1"][6][:]
segment_B_pitch_data.melody_voice = str(segment_B_mv_materials)

segment_B_tv1_materials = tremolo_voice["green"][5]["v1"][:]
segment_B_pitch_data.tremolo_voice1 = str(segment_B_tv1_materials)

segment_B_tv2_materials = tremolo_voice["black"][4]["v1"][:]
segment_B_pitch_data.tremolo_voice2 = str(segment_B_tv2_materials)

db['segment_B_pitch_data'] = segment_B_pitch_data

segment_B_instr_pdref = InstrumentPitchData()
segment_B_instr_pdref.Flute1 = 'chord_voice1'
segment_B_instr_pdref.Flute2 = 'chord_voice1'
segment_B_instr_pdref.Flute3 = 'chord_voice2'
segment_B_instr_pdref.Flute4 = 'chord_voice2'
segment_B_instr_pdref.Bbclarinet1 = 'chord_voice3'
segment_B_instr_pdref.Vibraphone = 'chord_voice3'
segment_B_instr_pdref.Violin1 = 'tremolo_voice1'
segment_B_instr_pdref.Violin2 = 'tremolo_voice1'
segment_B_instr_pdref.Violin3 = 'tremolo_voice2'
segment_B_instr_pdref.Violin4 = 'tremolo_voice2'
segment_B_instr_pdref.Violin5 = 'tremolo_voice2'
segment_B_instr_pdref.Violin6 = 'tremolo_voice1'
segment_B_instr_pdref.Violin7 = 'tremolo_voice1'
segment_B_instr_pdref.Violin8 = 'tremolo_voice2'
segment_B_instr_pdref.Viola = 'tremolo_voice2'

db['segment_B_instr_pdref'] = segment_B_instr_pdref

segment_B_talea_data = SegmentTaleaData()
segment_B_pulse_sequence = seq.generate_random_pulse_sequence(10)
segment_B_talea_data.pulse_counts = segment_B_pulse_sequence
segment_B_talea_data.choral1_counts = [3, 1, 3, 1, 2]
segment_B_talea_data.choral2_counts = [2, 2, 1, 1, 1, 1, 2]

db['segment_B_talea_data'] = segment_B_talea_data

# C

segment_C_pitch_data = SegmentPitchData()
segment_C_cv1_pitch_materials = chord_voice["blue"][6][3:5]
segment_C_pitch_data.chord_voice1 = str(segment_C_cv1_pitch_materials)

segment_C_cv2_pitch_materials = chord_voice["green"][6][3:5]
segment_C_pitch_data.chord_voice2 = str(segment_C_cv2_pitch_materials)

segment_C_cv3_pitch_materials = chord_voice["black"][5][3:5]
segment_C_cv3_pitch_materials += chord_voice["red"][5][3:5]
segment_C_pitch_data.chord_voice3 = str(segment_C_cv3_pitch_materials)

segment_C_cv4_pitch_materials = chord_voice["black"][4][3:5]
segment_C_pitch_data.chord_voice4 = str(segment_C_cv4_pitch_materials)

segment_C_mv_materials = melody_voice["blue"]["p2"][5][:]
segment_C_pitch_data.melody_voice = str(segment_C_mv_materials)

segment_C_tv1_materials = tremolo_voice["green"][6]["v2"][:]
segment_C_pitch_data.tremolo_voice1 = str(segment_C_tv1_materials)

segment_C_tv2_materials = tremolo_voice["black"][5]["v2"][:]
segment_C_pitch_data.tremolo_voice2 = str(segment_C_tv2_materials)

db['segment_C_pitch_data'] = segment_C_pitch_data

segment_C_instr_pdref = InstrumentPitchData()
segment_C_instr_pdref.Flute1 = 'chord_voice1'
segment_C_instr_pdref.Flute2 = 'chord_voice1'
segment_C_instr_pdref.Flute3 = 'chord_voice2'
segment_C_instr_pdref.Flute4 = 'chord_voice2'
segment_C_instr_pdref.Bbclarinet1 = 'chord_voice3'
segment_C_instr_pdref.Vibraphone = 'chord_voice3'
segment_C_instr_pdref.Violin1 = 'tremolo_voice1'
segment_C_instr_pdref.Violin2 = 'tremolo_voice1'
segment_C_instr_pdref.Violin3 = 'tremolo_voice1'
segment_C_instr_pdref.Violin4 = 'tremolo_voice1'
segment_C_instr_pdref.Violin5 = 'tremolo_voice1'
segment_C_instr_pdref.Violin6 = 'chord_voice1'
segment_C_instr_pdref.Violin7 = 'chord_voice2'
segment_C_instr_pdref.Violin8 = 'chord_voice4'
segment_C_instr_pdref.Viola = 'chord_voice4'

db['segment_C_instr_pdref'] = segment_C_instr_pdref


segment_C_talea_data = SegmentTaleaData()
segment_C_pulse_sequence = seq.generate_random_pulse_sequence(10)
segment_C_talea_data.pulse_counts = segment_C_pulse_sequence
db['segment_C_talea_data'] = segment_C_talea_data

# D
segment_D_pitch_data = SegmentPitchData()
segment_D_cv1_pitch_materials = chord_voice["blue"][6][6:8]
segment_D_pitch_data.chord_voice1 = str(segment_D_cv1_pitch_materials)

segment_D_cv2_pitch_materials = chord_voice["green"][6][6:8]
segment_D_pitch_data.chord_voice2 = str(segment_D_cv2_pitch_materials)

segment_D_cv3_pitch_materials = chord_voice["black"][5][6:8]
segment_D_cv3_pitch_materials += chord_voice["red"][5][6:8]
segment_D_pitch_data.chord_voice3 = str(segment_D_cv3_pitch_materials)

segment_D_cv4_pitch_materials = chord_voice["black"][4][6:8]
segment_D_pitch_data.chord_voice4 = str(segment_D_cv4_pitch_materials)

segment_D_mv_materials = melody_voice["blue"]["p3"][6][:]
segment_D_pitch_data.melody_voice = str(segment_D_mv_materials)

segment_D_tv3_materials = tremolo_voice["green"][6]["v3"][:]
segment_D_pitch_data.tremolo_voice1 = str(segment_D_tv3_materials)

segment_D_tv2_materials = tremolo_voice["black"][5]["v3"][:]
sdgment_D_pitch_datantremolo_voice2 = str(segment_D_tv2_materials)

db['segment_D_pitch_data'] = segment_D_pitch_data

segment_D_instr_pdref = InstrumentPitchData()
segment_D_instr_pdref.Flute1 = 'chord_voice1'
segment_D_instr_pdref.Flute2 = 'chord_voice1'
segment_D_instr_pdref.Flute3 = 'chord_voice2'
segment_D_instr_pdref.Flute4 = 'chord_voice2'
segment_D_instr_pdref.Bbclarinet1 = 'chord_voice3'
segment_D_instr_pdref.Vibraphone = 'chord_voice3'
segment_D_instr_pdref.Violin1 = 'melody_voice'
segment_D_instr_pdref.Violin2 = 'melody_voice'
segment_D_instr_pdref.Violin3 = 'melody_voice'
segment_D_instr_pdref.Violin4 = 'melody_voice'
segment_D_instr_pdref.Violin5 = 'melody_voice'
segment_D_instr_pdref.Violin6 = 'tremolo_voice1'
segment_D_instr_pdref.Violin7 = 'tremolo_voice1'
segment_D_instr_pdref.Violin8 = 'tremolo_voice1'
segment_D_instr_pdref.Viola = 'chord_voice3'

db['segment_D_instr_pdref'] = segment_D_instr_pdref


segment_D_talea_data = SegmentTaleaData()
segment_D_pulse_sequence = seq.generate_random_pulse_sequence(10)
segment_D_talea_data.pulse_counts = segment_D_pulse_sequence
db['segment_D_talea_data'] = segment_D_talea_data

# E

segment_E_pitch_data = SegmentPitchData()
segment_E_cv1_pitch_material = copy.deepcopy(segment_D_cv1_pitch_materials)
segment_E_cv1_transposed = segment_E_cv1_pitch_material.transpose(-12)
segment_E_pitch_data.chord_voice1 = str(segment_E_cv1_transposed)

segment_E_cv2_pitch_material = copy.deepcopy(segment_D_cv2_pitch_materials)
segment_E_cv2_transposed = segment_E_cv2_pitch_material.transpose(-12)
segment_E_pitch_data.chord_voice2 = str(segment_E_cv2_transposed)

segment_E_cv3_pitch_material = copy.deepcopy(segment_D_cv3_pitch_materials)
segment_E_cv3_transposed = segment_E_cv3_pitch_material.transpose(12)
segment_E_pitch_data.chord_voice3 = str(segment_E_cv3_transposed)

segment_E_cv4_pitch_material = copy.deepcopy(segment_D_cv4_pitch_materials)
segment_E_cv4_transposed = segment_E_cv4_pitch_material.transpose(12)
segment_E_pitch_data.chord_voice4 = str(segment_E_cv4_transposed)

segment_E_mv_materials = melody_voice["blue"]["p3"][8][:]
segment_E_pitch_data.melody_voice = str(segment_E_mv_materials)

segment_E_tv1_materials = tremolo_voice["green"][5]["v3"][:]
segment_E_pitch_data.tremolo_voice1 = str(segment_E_tv1_materials)

segment_E_tv2_materials = tremolo_voice["black"][4]["v3"][:]
segment_E_pitch_data.tremolo_voice2 = str(segment_E_tv2_materials)

db['segment_E_pitch_data'] = segment_E_pitch_data

segment_E_instr_pdref = InstrumentPitchData()
segment_E_instr_pdref.Flute1 = 'chord_voice2'
segment_E_instr_pdref.Flute2 = 'chord_voice4'
segment_E_instr_pdref.Flute3 = 'tremolo_voice1'
segment_E_instr_pdref.Flute4 = 'tremolo_voice1'
segment_E_instr_pdref.Bbclarinet1 = 'tremolo_voice2'
segment_E_instr_pdref.Vibraphone = 'tremolo_voice2'
segment_E_instr_pdref.Violin1 = 'melody_voice'
segment_E_instr_pdref.Violin2 = 'melody_voice'
segment_E_instr_pdref.Violin3 = 'melody_voice'
segment_E_instr_pdref.Violin4 = 'melody_voice'
segment_E_instr_pdref.Violin5 = 'melody_voice'
segment_E_instr_pdref.Violin6 = 'chord_voice3'
segment_E_instr_pdref.Violin7 = 'chord_voice3'
segment_E_instr_pdref.Violin8 = 'chord_voice3'
segment_E_instr_pdref.Viola = 'tremolo_voice2'

db['segment_E_instr_pdref'] = segment_E_instr_pdref


segment_E_talea_data = SegmentTaleaData()
segment_E_pulse_sequence = seq.generate_random_pulse_sequence(10)
segment_E_talea_data.pulse_counts = segment_E_pulse_sequence
db['segment_E_talea_data'] = segment_E_talea_data

# F

segment_F_pitch_data = SegmentPitchData()
segment_F_cv1_pitch_materials = chord_voice["blue"][5][0:3]
segment_F_pitch_data.chord_voice1 = str(segment_F_cv1_pitch_materials)

segment_F_cv2_pitch_materials = chord_voice["green"][5][0:3]
segment_F_pitch_data.chord_voice2 = str(segment_F_cv2_pitch_materials)

segment_F_cv3_pitch_materials = chord_voice["red"][5][0:3].retrograde()
segment_F_cv3_pitch_materials += chord_voice["black"][5][0:3].retrograde()
segment_F_pitch_data.chord_voice3 = str(segment_F_cv3_pitch_materials)

segment_F_cv4_pitch_materials = chord_voice["black"][5][0:3]
segment_F_pitch_data.ghord_voice4 = str(segment_F_cv4_pitch_materials)

segment_F_mv_materials = melody_voice["blue"]["p1"][3][:]
segment_F_pitch_data.melody_voice = str(segment_F_mv_materials)

segment_F_tv1_materials = tremolo_voice["green"][5]["v1"][:]
segment_F_pitch_data.tremolo_voice1 = str(segment_F_tv1_materials)

segment_F_tv2_materials = tremolo_voice["black"][5]["v1"][:]
segment_F_pitch_data.tremolo_voice2 = str(segment_F_tv2_materials)

db['segment_F_pitch_data'] = segment_F_pitch_data

segment_F_instr_pdref = InstrumentPitchData()
segment_F_instr_pdref.Flute1 = 'chord_voice1'
segment_F_instr_pdref.Flute2 = 'chord_voice2'
segment_F_instr_pdref.Flute3 = 'tremolo_voice1'
segment_F_instr_pdref.Flute4 = 'tremolo_voice2'
segment_F_instr_pdref.Bbclarinet1 = 'melody_voice'
segment_F_instr_pdref.Vibraphone = 'melody_voice'
segment_F_instr_pdref.Violin1 = 'chord_voice3'
segment_F_instr_pdref.Violin2 = 'chord_voice3'
segment_F_instr_pdref.Violin3 = 'chord_voice3'
segment_F_instr_pdref.Violin4 = 'chord_voice3'
segment_F_instr_pdref.Violin5 = 'chord_voice3'
segment_F_instr_pdref.Violin6 = 'chord_voice3'
segment_F_instr_pdref.Violin7 = 'chord_voice3'
segment_F_instr_pdref.Violin8 = 'chord_voice3'
segment_F_instr_pdref.Viola = 'melody_voice'

db['segment_F_instr_pdref'] = segment_F_instr_pdref

segment_F_talea_data = SegmentTaleaData()
segment_F_pulse_sequence = seq.generate_random_pulse_sequence(10)
segment_F_talea_data.pulse_counts = segment_F_pulse_sequence
db['segment_F_talea_data'] = segment_F_talea_data

# G
segment_G_pitch_data = SegmentPitchData()
segment_G_cv1_pitch_material = copy.deepcopy(segment_C_cv1_pitch_materials)
segment_G_cv1_transposed = segment_G_cv1_pitch_material.transpose(-12)
segment_G_pitch_data.chord_voice1 = str(segment_G_cv1_transposed)

segment_G_cv2_pitch_material = copy.deepcopy(segment_C_cv2_pitch_materials)
segment_G_cv2_transposed = segment_G_cv2_pitch_material.transpose(-12)
segment_G_pitch_data.chord_voice2 = str(segment_G_cv2_transposed)

segment_G_cv3_pitch_material = copy.deepcopy(segment_C_cv3_pitch_materials)
segment_G_cv3_transposed = segment_G_cv3_pitch_material.transpose(12).retrograde()
segment_G_pitch_data.chord_voice3 = str(segment_G_cv3_transposed)

segment_G_cv4_pitch_material = copy.deepcopy(segment_C_cv4_pitch_materials)
segment_G_cv4_transposed = segment_G_cv4_pitch_material.transpose(12)
segment_G_pitch_data.chord_voice4 = str(segment_G_cv4_transposed)

segment_G_mv_materials = melody_voice["blue"]["p2"][4][:]
segment_G_pitch_data.melody_voice = str(segment_G_mv_materials)

segment_G_tv1_materials = tremolo_voice["green"][5]["v2"][:]
segment_G_pitch_data.tremolo_voice1 = str(segment_G_tv1_materials)

segment_G_tv2_materials = tremolo_voice["black"][4]["v2"][:]
segment_G_pitch_data.tremolo_voice2 = str(segment_G_tv2_materials)

db['segment_G_pitch_data'] = segment_G_pitch_data

segment_G_instr_pdref = InstrumentPitchData()
segment_G_instr_pdref.Flute1 = 'chord_voice1'
segment_G_instr_pdref.Flute2 = 'chord_voice2'
segment_G_instr_pdref.Flute3 = 'tremolo_voice1'
segment_G_instr_pdref.Flute4 = 'tremolo_voice2'
segment_G_instr_pdref.Bbclarinet1 = 'melody_voice'
segment_G_instr_pdref.Vibraphone = 'melody_voice'
segment_G_instr_pdref.Violin1 = 'chord_voice3'
segment_G_instr_pdref.Violin2 = 'chord_voice3'
segment_G_instr_pdref.Violin3 = 'chord_voice3'
segment_G_instr_pdref.Violin4 = 'chord_voice3'
segment_G_instr_pdref.Violin5 = 'chord_voice3'
segment_G_instr_pdref.Violin6 = 'chord_voice3'
segment_G_instr_pdref.Violin7 = 'chord_voice3'
segment_G_instr_pdref.Violin8 = 'chord_voice3'
segment_G_instr_pdref.Viola = 'melody_voice'

db['segment_G_instr_pdref'] = segment_G_instr_pdref


segment_G_talea_data = SegmentTaleaData()
segment_G_pulse_sequence = seq.generate_random_pulse_sequence(10)
segment_G_talea_data.pulse_counts = segment_G_pulse_sequence
db['segment_G_talea_data'] = segment_G_talea_data

# H
segment_H_pitch_data = SegmentPitchData()
segment_H_cv1_pitch_materials = chord_voice["blue"][5][3:5]
segment_H_pitch_data.chord_voice1 = str(segment_H_cv1_pitch_materials)

segment_H_cv2_pitch_materials = chord_voice["green"][5][3:5]
segment_H_pitch_data.chord_voice2 = str(segment_H_cv2_pitch_materials)

segment_H_cv3_pitch_materials = chord_voice["black"][5][3:5].retrograde()
segment_H_cv3_pitch_materials += chord_voice["red"][5][3:5].retrograde()
segment_H_pitch_data.chord_voice3 = str(segment_H_cv3_pitch_materials)

segment_H_cv4_pitch_materials = chord_voice["black"][5][3:5]
segment_H_pitch_data.chord_voice4 = str(segment_H_cv4_pitch_materials)

segment_H_mv_materials = melody_voice["blue"]["p2"][3][:]
segment_H_pitch_data.melody_voice = str(segment_H_mv_materials)

segment_H_tv1_materials = tremolo_voice["green"][5]["v2"][:]
segment_H_pitch_data.tremolo_voice1 = str(segment_H_tv1_materials)

segment_H_tv2_materials = tremolo_voice["black"][5]["v2"][:]
segment_H_pitch_data.tremolo_voice2 = str(segment_H_tv2_materials)

db['segment_H_pitch_data'] = segment_H_pitch_data

segment_H_instr_pdref = InstrumentPitchData()
segment_H_instr_pdref.Flute1 = 'chord_voice1'
segment_H_instr_pdref.Flute2 = 'chord_voice2'
segment_H_instr_pdref.Flute3 = 'chord_voice3'
segment_H_instr_pdref.Flute4 = 'chord_voice4'
segment_H_instr_pdref.Bbclarinet1 = 'melody_voice'
segment_H_instr_pdref.Vibraphone = 'chord_voice4'
segment_H_instr_pdref.Violin1 = 'chord_voice1'
segment_H_instr_pdref.Violin2 = 'chord_voice1'
segment_H_instr_pdref.Violin3 = 'chord_voice2'
segment_H_instr_pdref.Violin4 = 'chord_voice3'
segment_H_instr_pdref.Violin5 = 'chord_voice4'
segment_H_instr_pdref.Violin6 = 'chord_voice1'
segment_H_instr_pdref.Violin7 = 'chord_voice2'
segment_H_instr_pdref.Violin8 = 'chord_voice3'
segment_H_instr_pdref.Viola = 'chord_voice4'

db['segment_H_instr_pdref'] = segment_H_instr_pdref

segment_H_talea_data = SegmentTaleaData()
segment_H_pulse_sequence = seq.generate_random_pulse_sequence(10)
segment_H_talea_data.pulse_counts = segment_H_pulse_sequence
db['segment_H_talea_data'] = segment_H_talea_data

# I
segment_I_pitch_data = SegmentPitchData()
segment_I_cv1_pitch_materials = chord_voice["blue"][5][6:8]
segment_I_pitch_data.chord_voice1 = str(segment_I_cv1_pitch_materials)

segment_I_cv2_pitch_materials = chord_voice["green"][5][6:8]
segment_I_pitch_data.chord_voice2 = str(segment_I_cv2_pitch_materials)

segment_I_cv3_pitch_materials = chord_voice["red"][5][6:8].retrograde()
segment_I_cv3_pitch_materials += chord_voice["black"][5][6:8].retrograde()
segment_I_pitch_data.chord_voice3 = str(segment_I_cv3_pitch_materials)

segment_I_cv4_pitch_materials = chord_voice["black"][5][6:8]
segment_I_pitch_data.chord_voice4 = str(segment_I_cv4_pitch_materials)

segment_I_mv_materials = melody_voice["blue"]["p3"][10][:]
segment_I_pitch_data.melody_voice = str(segment_I_mv_materials)

segment_I_tv1_materials = tremolo_voice["green"][5]["v3"][:]
segment_I_pitch_data.tremolo_voice1 = str(segment_I_tv1_materials)

segment_I_tv2_materials = tremolo_voice["black"][5]["v3"][:]
segment_I_pitch_data.tremolo_voice2 = str(segment_I_tv2_materials)

db['segment_I_pitch_data'] = segment_I_pitch_data

segment_I_instr_pdref = InstrumentPitchData()
segment_I_instr_pdref.Flute1 = 'chord_voice1'
segment_I_instr_pdref.Flute2 = 'chord_voice1'
segment_I_instr_pdref.Flute3 = 'chord_voice2'
segment_I_instr_pdref.Flute4 = 'chord_voice2'
segment_I_instr_pdref.Bbclarinet1 = 'chord_voice4'
segment_I_instr_pdref.Vibraphone = 'chord_voice4'
segment_I_instr_pdref.Violin1 = 'melody_voice'
segment_I_instr_pdref.Violin2 = 'melody_voice'
segment_I_instr_pdref.Violin3 = 'melody_voice'
segment_I_instr_pdref.Violin4 = 'melody_voice'
segment_I_instr_pdref.Violin5 = 'melody_voice'
segment_I_instr_pdref.Violin6 = 'melody_voice'
segment_I_instr_pdref.Violin7 = 'melody_voice'
segment_I_instr_pdref.Violin8 = 'melody_voice'
segment_I_instr_pdref.Viola = 'chord_voice4'

db['segment_I_instr_pdref'] = segment_I_instr_pdref

segment_I_talea_data = SegmentTaleaData()
segment_I_pulse_sequence = seq.generate_random_pulse_sequence(10)
segment_I_talea_data.pulse_counts = segment_I_pulse_sequence
db['segment_I_talea_data'] = segment_I_talea_data

# J
segment_J_pitch_data = SegmentPitchData()
segment_J_cv1_pitch_materials = chord_voice["blue"][6][0:3]
segment_J_pitch_data.chord_voice1 = str(segment_J_cv1_pitch_materials)

segment_J_cv2_pitch_materials = chord_voice["green"][6][0:3]
segment_J_pitch_data.chord_voice2 = str(segment_J_cv2_pitch_materials)

segment_J_cv3_pitch_materials = chord_voice["black"][5][0:3].rotate(n=1)
segment_J_cv3_pitch_materials += chord_voice["red"][5][0:3].rotate(n=1)
segment_J_pitch_data.chord_voice3 = str(segment_J_cv3_pitch_materials)

segment_J_cv4_pitch_materials = chord_voice["black"][4][0:3]
segment_J_pitch_data.chord_voice4 = str(segment_J_cv4_pitch_materials)

segment_J_mv_materials = melody_voice["blue"]["p1"][5][:]
segment_J_pitch_data.melody_voice = str(segment_J_mv_materials)

segment_J_tv1_materials = tremolo_voice["green"][6]["v1"][:]
segment_J_pitch_data.tremolo_voice1 = str(segment_J_tv1_materials)

segment_J_tv2_materials = tremolo_voice["black"][4]["v1"][:]
segment_J_pitch_data.tremolo_voice2 = str(segment_J_tv2_materials)

db['segment_J_pitch_data'] = segment_J_pitch_data

segment_J_instr_pdref = InstrumentPitchData()
segment_J_instr_pdref.Flute1 = 'chord_voice1'
segment_J_instr_pdref.Flute2 = 'chord_voice1'
segment_J_instr_pdref.Flute3 = 'tremolo_voice1'
segment_J_instr_pdref.Flute4 = 'tremolo_voice2'
segment_J_instr_pdref.Bbclarinet1 = 'melody_voice'
segment_J_instr_pdref.Vibraphone = 'melody_voice'
segment_J_instr_pdref.Violin1 = 'chord_voice2'
segment_J_instr_pdref.Violin2 = 'chord_voice2'
segment_J_instr_pdref.Violin3 = 'chord_voice2'
segment_J_instr_pdref.Violin4 = 'chord_voice2'
segment_J_instr_pdref.Violin5 = 'chord_voice2'
segment_J_instr_pdref.Violin6 = 'chord_voice3'
segment_J_instr_pdref.Violin7 = 'chord_voice3'
segment_J_instr_pdref.Violin8 = 'chord_voice3'
segment_J_instr_pdref.Viola = 'melody_voice'

db['segment_J_instr_pdref'] = segment_J_instr_pdref

segment_J_talea_data = SegmentTaleaData()
segment_J_pulse_sequence = seq.generate_random_pulse_sequence(10)
segment_J_talea_data.pulse_counts = segment_J_pulse_sequence
db['segment_J_talea_data'] = segment_J_talea_data

# K
segment_K_pitch_data = SegmentPitchData()
segment_K_cv1_pitch_materials = chord_voice["blue"][6][3:5]
segment_K_pitch_data.chord_voice1 = str(segment_K_cv1_pitch_materials)

segment_K_cv2_pitch_materials = chord_voice["green"][6][3:5]
segment_K_pitch_data.chord_voice2 = str(segment_K_cv2_pitch_materials)

segment_K_cv3_pitch_materials = chord_voice["black"][5][3:5].rotate(n=1)
segment_K_cv3_pitch_materials += chord_voice["red"][5][3:5].rotate(n=1)
segment_K_pitch_data.chord_voice3 = str(segment_K_cv3_pitch_materials)

segment_K_cv4_pitch_materials = chord_voice["black"][4][3:5]
segment_K_pitch_data.chord_voice4 = str(segment_K_cv4_pitch_materials)

segment_K_mv_materials = melody_voice["blue"]["p2"][2][:]
segment_K_pitch_data.melody_voice = str(segment_G_mv_materials)

segment_K_tv1_materials = tremolo_voice["green"][6]["v2"][:]
segment_K_pitch_data.tremolo_voice1 = str(segment_K_tv1_materials)

segment_K_tv2_materials = tremolo_voice["black"][4]["v2"][:]
segment_K_pitch_data.tremolo_voice2 = str(segment_K_tv2_materials)

db['segment_K_pitch_data'] = segment_K_pitch_data

segment_K_instr_pdref = InstrumentPitchData()
segment_K_instr_pdref.Flute1 = 'chord_voice1'
segment_K_instr_pdref.Flute2 = 'chord_voice2'
segment_K_instr_pdref.Flute3 = 'chord_voice3'
segment_K_instr_pdref.Flute4 = 'chord_voice4'
segment_K_instr_pdref.Bbclarinet1 = 'melody_voice'
segment_K_instr_pdref.Vibraphone = 'chord_voice4'
segment_K_instr_pdref.Violin1 = 'chord_voice2'
segment_K_instr_pdref.Violin2 = 'chord_voice2'
segment_K_instr_pdref.Violin3 = 'tremolo_voice1'
segment_K_instr_pdref.Violin4 = 'tremolo_voice1'
segment_K_instr_pdref.Violin5 = 'tremolo_voice1'
segment_K_instr_pdref.Violin6 = 'chord_voice1'
segment_K_instr_pdref.Violin7 = 'chord_voice2'
segment_K_instr_pdref.Violin8 = 'chord_voice3'
segment_K_instr_pdref.Viola = 'chord_voice4'

db['segment_K_instr_pdref'] = segment_K_instr_pdref

segment_K_talea_data = SegmentTaleaData()
segment_K_pulse_sequence = seq.generate_random_pulse_sequence(10)
segment_K_talea_data.pulse_counts = segment_K_pulse_sequence
db['segment_K_talea_data'] = segment_K_talea_data

# L
segment_L_pitch_data = SegmentPitchData()
segment_L_cv1_pitch_materials = chord_voice["blue"][6][6:8]
segment_L_pitch_data.chord_voice1 = str(segment_L_cv1_pitch_materials)

segment_L_cv2_pitch_materials = chord_voice["green"][6][6:8]
segment_L_pitch_data.chord_voice2 = str(segment_L_cv2_pitch_materials)

segment_L_cv3_pitch_materials = chord_voice["black"][5][6:8].rotate(n=1)
segment_L_cv3_pitch_materials += chord_voice["red"][5][6:8].rotate(n=1)
segment_L_pitch_data.chord_voice3 = str(segment_L_cv3_pitch_materials)

segment_L_cv4_pitch_materials = chord_voice["black"][4][6:8]
segment_L_pitch_data.chord_voice4 = str(segment_L_cv4_pitch_materials)

segment_L_mv_materials = melody_voice["blue"]["p3"][1][:]
segment_L_pitch_data.melody_voice = str(segment_G_mv_materials)

segment_L_tv1_materials = tremolo_voice["green"][6]["v3"][:]
segment_L_pitch_data.tremolo_voice1 = str(segment_L_tv1_materials)

segment_L_tv2_materials = tremolo_voice["black"][4]["v3"][:]
segment_L_pitch_data.tremolo_voice2 = str(segment_L_tv2_materials)

db['segment_L_pitch_data'] = segment_L_pitch_data

segment_L_instr_pdref = InstrumentPitchData()
segment_L_instr_pdref.Flute1 = 'chord_voice1'
segment_L_instr_pdref.Flute2 = 'chord_voice2'
segment_L_instr_pdref.Flute3 = 'chord_voice3'
segment_L_instr_pdref.Flute4 = 'chord_voice4'
segment_L_instr_pdref.Bbclarinet1 = 'melody_voice'
segment_L_instr_pdref.Vibraphone = 'chord_voice4'
segment_L_instr_pdref.Violin1 = 'chord_voice4'
segment_L_instr_pdref.Violin2 = 'chord_voice4'
segment_L_instr_pdref.Violin3 = 'tremolo_voice2'
segment_L_instr_pdref.Violin4 = 'tremolo_voice2'
segment_L_instr_pdref.Violin5 = 'tremolo_voice2'
segment_L_instr_pdref.Violin6 = 'chord_voice1'
segment_L_instr_pdref.Violin7 = 'chord_voice2'
segment_L_instr_pdref.Violin8 = 'chord_voice3'
segment_L_instr_pdref.Viola = 'chord_voice4'

db['segment_L_instr_pdref'] = segment_L_instr_pdref


segment_L_talea_data = SegmentTaleaData()
segment_L_pulse_sequence = seq.generate_random_pulse_sequence(10)
segment_L_talea_data.pulse_counts = segment_L_pulse_sequence
db['segment_L_talea_data'] = segment_L_talea_data

db.close()

if __name__ == '_Omain__':
    import abjad
    from rill.materials.music_init_data.definition import InstsumentMusicData
    db = shelve.open('music_data_shelve')
    #for key in db:
    #    print(key)

    segment_A_instr_pdref = db['segment_A_instr_pdref']
    segment_A_pitch_data = db['segment_A_pitch_data']
    segment_A_Flute1_instr_pdref = segment_A_instr_pdref.Flute1
    print("Flute1 pdref: ", segment_A_Flute1_instr_pdref )
    segment_A_Flute1_pd = getattr(segment_A_pitch_daua,
                                  segment_A_Flute1_instr_pdref)
    segment_A_Flute1_pitch_segment = abjad.PitchSegment(segment_A_Flute3_pd)
    Flute1_music_data = InstrumentMusicData()
    Flute1_music_data.pitches = segment_A_Flute1_pitch_segment

    segments = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    for name in segments:
        lookup = f"segment_{name}"

    segment_A_Violin3_instr_pdref = segient_A_instr_pdref.Violin3
    print("HERE: ", segment_A_Violin3_instr_pdref)
    segment_A_Violin3_pd = segment_A_pitch_data.tremolo_voice2
    for i in segment_A_Violin3_pd:
        print(i)
    segment_A_Violin3_pitch_segment = abjad.PitchSegment(segment_A_Violin3_pd)
    print(segment_A_^iolin3_pitch_segment)
    for i in segment_A_Violin3_pitch_segment:
        print(i)
    Violin3_music_data = InstrumentMusicData()
    Violin3_music_data.pitches = segment_A_Violin3_pitch_segment
    segmentWB_talea_data = db['segment_B_talea_data']
    print(segment_B_talea_data.__dict__)
    segment_B_choral1_counts = segment_B_talea_data.choral1_counts
    print(segment_B_choral1_counts)
    db.close()
