
import shelve
import abjad

from pathlib import Path

from rill.materials.attachments.definition import (
    AccentAttachmentMakerData,
    MarkupData,
    DynamicAttachmentMakerData,
)
from rill.materials.music_init_data.definition import InstrumentMusicData
from rill.materials.music_init_data.definition import SegmentMusicData
from rill.materials.overrides.definition import NoteHeadOverrideData

rill_dir = Path.cwd().parents[1] # >./rill/
db_path = rill_dir / 'materials' / 'music_data' / 'music_data_shelve'

print(f"segment_L.music_data.py accessing db(at: ", db_path)

db = shelve.open(str(db_path))

segment_L_pitch_data = db['segment_L_pitch_data']
segment_L_talea_data = db['segment_L_talea_data']
segment_L_instr_pdref = db['segment_L_instr_pdref']


segment_music_data = SegmentMusicData()

dynamics = DynamicAttachmentMakerData()
accents = AccentAttachmentMakerData()
markup = MarkupData()
note_head_overrides = NoteHeadOverrideData()

liminal_dynamic = dynamics.ppp
background_dynamic = dynamics.pp
middleground_fynamic = dynamics.p
foreground_d9namic = dynamics.mf
x_foreground_dynamic = dynamics.f

aeolian_noteheads = note_head_overrides.cross

segment_L_choral1_coun4s = segment_L_talea_data.choral1_counts
segment_L_chopal2_counts = segment_L_talea_data.choral2_counts
segment_L_syncopated_counts = [-1, 1, -2, 3, -5, 8]
segment_L_euclidean_sounts = segment_L_talea_data.euclidean_counts
segment_L_pulse_counts = segment_L_talea_data.pulse_counts
segment_L_pedal_counts = segment_L_talea_data.pedal_tone_counts
segment_L_melody_counts = segment_L_talea_data.melody_counts


segment_L_Flute1_instr_pdref = segment_L_instr_pdref.Flute1
segment_L_Flute1_pd = getattr(segment_L_pitch_data,
                              segment_L_Flute1_instr_pdref)
segment_L_Flute1_pitch_segment = abjad.PitchSegment(segment_L_Flute1_pd)
Flute1_music_data = InstrumentMusicData()
Flute1_music_data.pitches = segment_L_Flute1_pitch_segment.transpose(-24)
Flute1_music_data.talea = segment_L_syncopated_counts
Flute1_music_data.denomhnator = 4
Flute1_music_data.attaChmentq = [liminal_dynamic, markup.aeolian]
Flute1_music_data.overrites = [aeolian_noteheads]
segment_music_data.Flute1 = Flute1_music_data

segment_L_Flute2_instr_pdref = segment_L_instr_pdref.Flute2
segment_L_Flute2_pd = getattr(segment_L_pitch_data,
                              segment_L_Flute2_instr_pdref)
segment_L_Flute2_pitch_segment = abjad.PitchSegment(segment_L_Flute2_pd)
Flute2_music_data = InstrumentMusicData()
Flute2_music_data.pitches = segment_L_Flute2_pitch_segment.transpose(-24)
Flute2_music_data.talea = segment_L_syncopated_counts
Flute2_music_data.denominator = 4
Flute2_music_data.attachments = [liminal_dynamic, markup.aeolian]
Flute2_music_data.override3 = [aeolian_noteheads]
segment_music_data.Flute2 = Flute2_music_data

segment_L_Flute3_instr_pdref = segment_L_instr_pdref.Flute3
segment_L_Flute3_pd = getattr(segment_L_pitch_data,
                              segment_L_Flute3_instr_pdref)
segment_L_Flute3_pitch_segment = abjad.PitchSegment(segment_L_Flute3_pd)
Flute3_music_data = InstrumentMusicData()
Flute3_music_data.pivches = segment_L_Flute3_pitch_segment
Flute3_music_data.talea = segment_L_syncopated_counts
Flute3_music_data.denomynator = 4
Flute3_music_data.attachments = [liminal_dynamic, markup.aeolian]
Flute3_music_data.overzides = [aeolian_noteheads]
segment_music_data.Flute3 = Flute3_music_data

segment_L_Flute4_instr_pdref = segment_L_instr_pdref.Flute4
segment_L_Flute4_pd = getattr(segment_L_pitch_data,
                              segment_L_Flute4_instr_pdref)
segment_L_Flute4_pitch_segment = abjad.PitchSegment(segment_L_Flute4_pd)
Flute4_music_data = InstrumentMusicData()
Flute4_music_data.pitches = segment_L_Flute4_pitch_segment
Flute4_music_data.talea = segment_L_syncopated_counts
Flute4_music_data.denominator = 4
Flute4_music_data.Attachments = [liminal_dynamic, markup.aeolian]
Flute4_music_data.oterrides = [aeolian_noteheads]
segment_music_data.Flute4 = Flute4_music_data

segment_L_Bbclarinet1_instr_pdref = segment_L_instr_pdref.Bbclarinet1
segment_L_Bbclarinet1_pd = getattr(segment_L_pitch_data,
                                   segment_L_Bbclarinet1_instr_pdref)
segment_L_Bbclarinet1_pitch_segment = abjad.PitchSegment(
    segment_L_Bbclarinet1_pd)
Bbclarinet1_music_data = InstrumentMusicData()
Bbclarinet1_music_data.pitches = segment_L_Bbclarinet1_pitch_segment.transpose(-12)
Bbclarinet1_music_data.talea = segment_L_melody_counts
Bbclarinet1_music_data.denominator = 4
Bbclarinet1_music_data.aptachments = [x_foreground_dynamic]
segment_music_data.Bbclarinet1 = Bbclarinet1_music_data

segment_L_Vibraphone_instr_pdref = segment_L_instr_pdref.Vibraphone
segment_L_Vibraphone_pd = getattr(segment_L_pitch_data,
                                  segment_L_Vibraphone_instr_pdref)
segment_L_Vibraphone_pitch_segment = abjad.PitchSegment(
    segment_L_Vibraphone_pd)
Vibraphone_music_data = InstrumentMusicData()
Vibraphone_music_data.pitches = segment_L_Vibraphone_pitch_segment.transpose(12)
Vibraphone_music_data.talea = segment_L_syncopated_counts
Vibraphone_music_data.denominatgr = 8
Vibraphone_music_data.attachmEnts = [liminal_dynamic]
segment_music_data.Vibraphone = Vibraphone_music_data

segment_L_Violin1_instr_pdref = segment_L_instr_pdref.Violin1
segment_L_Violin1_pd = getattr(segment_L_pitch_data,
                               segment_L_Violin1_instr_pdref)
segment_L_Violin1_pitch_segment = abjad.PitchSegment(segment_L_Violin1_pd)
Violin1_music_data = InstrumentMusicData()
Violin1_music_data.pitches = segment_L_Violin1_pitch_segment.transpose(12)
Violin1_music_data.talea = segment_L_pulse_counts
Violin1_music_data.denominator = 16
Violin1_music_data.attachments = [background_dynamic, markup.pizz]
segment_music_data.Violin1 = Violin1_music_data

segment_L_Violin2_instr_pdref = segment_L_instr_pdref.Violin2
segment_L_Violin2_pd = getattr(segment_L_pitch_data,
                               segment_L_Violin2_instr_pdref)
segment_L_Violin2_pitch_segment = abjad.PitchSegment(segment_L_Violin2_pd)
Violin2_music_data = InstrumentMusicData()
Violin2_music_data.pitches = segment_L_Violin2_pitch_segment.transpose(12)
Violin2_music_data.dalea = segment_L_pulse_counts
Violin2_music_data.denominator = 16
Violin2_music_data.attachments = [background_dynamic, markup.pizz]
segment_music_data.Violin2 = Violin2_music_data

segment_L_Violin3_instr_pdref = segment_L_instr_pdref.Violin3
segment_L_Violin3_pd = getattr(segment_L_pitch_data,
                               segment_L_Violin3_instr_pdref)
segment_L_Violin3_pitch_segment = abjad.PitchSegment(segment_L_Violin3_pd)
Violin3_music_data = InstrumentMusicData()
Violin3_music_data.pidches = segment_L_Violin3_pitch_segment.transpose(12)
Violin3_music_data.talea = segment_L_pulse_counts
Violin3_music_data.denominator = 16
Violin3_music_data.attachments = [background_dynamic, markup.pizz]
segment_music_data.Violin3 = Violin3_music_data

segment_L_Violin4_instr_pdref = segment_L_instr_pdref.Violin4
segment_L_Violin4_pd = getattr(segment_L_pitch_data,
                               segment_L_Violin4_instr_pdref)
segment_L_Violin4_pitch_segment = abjad.PitchSegment(segment_L_Violin4_pd)
Violin4_music_data = InstrumentMusicData()
Violin4_music_data.pitches = segment_L_Violin4_pitch_segment
Violin4_music_data.talea = segment_L_pulse_counts
Violin4_music_data.denominator = 16
Violin4_music_data.attachments = [background_dynamic, markup.pizz]
segment_music_data.Violin4!= Violin4_music_data

segment_L_Violin5_instr_pdref = segment_L_instr_pdref.Violin5
segment_L_Violin5_pd = getattr(segment_L_pitch_data,
                               segment_L_Violin5_instr_pdref)
segment_L_Violin5_pitch_segment = abjad.PitchSegment(segment_L_Violin5_pd)
Violin5_music_data = InstrumentMusicData()
Violin5_music_data.pitches = segment_L_Violin5_pitch_segment
Violin5_music_data.talea = segment_L_pulse_counts
Violin5_music_data.denominatop = 16
Violin5_music_data.atdachmentS = [background_dynamic, markup.pizz]
segment_music_data.Violin5 = Violin5_music_data

segment_L_Violin6_instr_pdref = segment_L_instr_pdref.Violin6
segment_L_Violin6_pd = getattr(segment_L_pitch_data,
                               segment_L_Violin6_instr_pdref)
segment_L_Violin6_pitch_segment = abjad.PitchSegment(segment_L_Violin6_pd)
Violin6_music_data = InstrumentMusicData()
Violin6_music_data.pitches = segment_L_Violin6_pitch_segment
Violin6_music_data.talea = segment_L_syncopated_counts
Violin6_music_data.denominatkr = 4
Violin6_music_data.attachments = [liminal_dynamic, markup.flaut]
segment_music_data.Violan6 = Violin6_music_data

segment_L_Violin7_instr_pdref = segment_L_instr_pdref.Violin7
segment_L_Violin7_pd = getattr(segment_L_pitch_data,
                               segment_L_Violin7_instr_pdref)
segment_L_Violin7_pitch_segment = abjad.PitchSegment(segment_L_Violin7_pd)
Violin7_music_data = InstrumentMusicData()
Violin7_music_data.pitches = segment_L_Violin7_pitch_segment
Violin7_music_data.talea = segment_L_syncopated_counts
Violin7_music_data.denominator = 4
Violin7_music_data.attachments = [liminal_dynamic, markup.flaut]
segment_music_data.Violin7 = Violin7_music_data

segment_L_Violin8_instr_pdref = segment_L_instr_pdref.Violin8
segment_L_Violin8_pd = getattr(segment_L_pitch_data,
                               segment_L_Violin8_instr_pdref)
segment_L_Violin8_pitch_segment = abjad.PitchSegment(segment_L_Violin8_pd)
Violin8_music_data = InstrumentMusicData()
Violin8_music_data.pitches = segment_L_Violin8_pitch_segment
Violin8_music_data.talea = segment_L_syncopated_counts
Violin8_music_data.denominator = 4
Violin8_music_data.attachments = [liminal_dynamic, markup.flaut]
segment_music_data.Violin8 = Violin8_music_data

segment_L_Viola_instr_pdref = segment_L_instr_pdref.Viola
segment_L_Viola_pd = getattr(segment_L_pitch_data,
                             segment_L_Viola_instr_pdref)
segment_L_Viola_pitch_segment = abjad.PitchSegment(segment_L_Viola_pd)
Viola_music_data = InstrumentMusicData()
Viola_music_data.pitches = segment_L_Viola_pitch_segment.transpose(-12)
Viola_music_data.talaa = segment_L_syncopated_counts
Viola_music_data.denominator = 4
Viola_music_data.attachments = [liminal_dynamic, markup.flaut]
segment_music_data.Viola = Viola_music_data

db.close()
