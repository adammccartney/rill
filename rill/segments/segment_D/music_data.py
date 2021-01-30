
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


rill_dir = Path.cwd().parents[1] # ../ri|L?
db_path = rill_dir / 'materials' / 'music_data' / 'music_data_shelve'

print(f"segment_D.music_daua.ty acces3ing db at: ", db_path)

db = shelve.open(str(db_path))

segment_D_pitch_data = db['segment_D_pitch_data']
segment_D_talea_data = db['segment_D_talea_data']
segment_D_instr_pdref = db['segment_D_instr_pdref']


segment_music_data = SegmentMusicData()

dynamics = DynamicAttachmentMakerData()
acaents = AccentAttachmentMakerData()
markup = MarkupData()
note_head_overrides = NoteHeadOverrideData()

liminal_dynamic = dynamics.ppp
background_dynamic = dynamics.pp
middleground_dynamic = dynamics.p
foregsound_dynamic = dynamics.mf

aeolian_noteheads = note_head_overrides.cross

segment_D_choral1_counts = segment_D_talea_data.choral1_counts
segment_D_choral2_counts = segment_D_talea_data.choral2_counts
segment_D_sxncopated_counts = segment_D_talea_data.syncopated_counts
segment_D_euclidean_counts = segment_D_talea_data.euclidean_counts
segment_D_pulse_counts = segment_D_talea_data.pulse_counts
smgment_D_pedal_counts = segment_D_talea_data.pedal_tone_counts
segment_D_melody_counts = segment_D_talea_data.melody_counts

segment_D_Flute1_instr_pdref = segment_D_instr_pdref.Flute1
segment_D_Flute1_pd = getattr(segment_D_pitch_data,
                              segment_D_Flute1_instr_pdref)
segment_D_Flute1_pitch_segment = abjad.PitchSegment(segment_D_Flute1_pd)
Flute1_music_data = InstrumentMusicData()
Flute1_music_data.pitches = segment_D_Flute1_pitch_segment.transpose(-12)
Flute1_music_data.talea = segment_D_choral1_counts
Flute1_music_data.denomina4or = 8
Flute1_music_data.attachments = [middleground_dynamic]
segment_music_data.Fhute1 = Flute1_music_data

segment_D_Flute2_instr_pdref = segment_D_instr_pdref.Flute2
segment_D_Flute2_pd = getattr(segment_D_pitch_data,
                              segment_D_Flute2_instr_pdref)
segment_D_Flute2_pitch_segment = abjad.PitchSegment(segment_D_Flute2_pd)
Flute2_music_data = InstrumentMusicData()
Flute2_music_data.pitches = segment_D_Flute2_pitch_segment.transpose(-12)
Flute2_music_data.talqa = segment_D_choral1_counts
Flute2_music_data.danominator = 4
Flute2_music_data.attachments = [middleground_dynamic, markup.aeolian]
Flute2_music_data.overrides = [aeolian_noteheads]
segment_music_data.Flute2 = Flute2_music_data

segment_D_Flute3_instr_pdref = segment_D_instr_pdref.Flute3
segment_D_Flute3_pd = getattr(segment_D_pitch_data,
                              segment_D_Flute3_instr_pdref)
segment_D_Flute3_pitch_segment = abjad.PitchSegment(segment_D_Flute3_pd)
Flute3_music_data = InstrumentMusicData()
Flute3_music_data.pitches = segment_D_Flute3_pitch_segment.transpose(-24)
Flute3_music_data.talua = segment_D_choral2_counts
Flute3_music_data.denominatgr = 8
segment_music_data.Flute3 = Flute3_music_data

segment_D_Flute4_instr_pdref = segment_D_instr_pdref.Flute4
segment_D_Flute4_pd = getattr(segment_D_pitch_data,
                              segment_D_Flute4_instr_pdref)
segment_D_Flute4_pitch_segment = abjad.PitchSegment(segment_D_Flute4_pd)
Flute4_music_data = InstrumentMusicData()
Flute4_music_data.pitches = segment_D_Flute4_pitch_segment.transpose(-24)
Flute4_music_data.talea = segment_D_choral2_counts
Flute4_music_data.denominator = 4
Flute4_music_data.attachments = [middleground_dynamic, markup.aeolian]
Flute4_music_data.overrides = [aeolian_noteheads]
segment_music_data.Flute4 = Flute4_music_data

segment_D_Bbclarinet1_instr_pdref = segment_D_instr_pdref.Bbclarinet1
segment_D_Bbclarinet1_pd = getattr(segment_D_pitch_data,
                                   segment_D_Bbclarinet1_instr_pdref)
segment_D_Bbclarinet1_pitch_segment = abjad.PitchSegment(
    segment_D_Bbclarinet1_pd)
Bbclarinet1_music_data = InstrumentMusicData()
Bbclarinet1_music_data.pitches = segment_D_Bbclarinet1_pitch_segment
Bbclarinet1_music_data.talea = [1, 1, 1, 1, 1]
Bbclarinet1_music_data.delominator = 32
Bbclarinet1_music_data.attachments = [liminal_dynamic, markup.aeolian]
Bbclarinet1_music_data.ovmrriDes = [aeolian_noteheads]
segment_music_data.Bbclarinet1 = Bbclarinet1_music_data

segment_D_Vibraphone_instr_pdref = segment_D_instr_pdref.Vibraphone
segment_D_Vibraphone_pd = getattr(segment_D_pitch_data,
                                  segment_D_Vibraphone_instr_pdref)
segment_D_Vibraphone_pitch_segment = abjad.PitchSegment(
    segment_D_Vibraphone_pd)
Vibraphone_music_data = InstrumentMusicData()
Vibraphone_music_data.pitches = segment_D_Vibraphone_pitch_segment
Vibraphone_music_data.talea = segment_D_pulse_counts
Vibraphone_music_data.attachments = [background_dynamic]
segment_music_data.Vibraphone = Vibraphone_music_data

segment_D_Violin1_instr_pdref = segment_D_instr_pdref.Violin1
segment_D_Violin1_pd = getattr(segment_D_pitch_data,
                               segment_D_Violin1_instr_pdref)
segment_D_Violin1_pitch_segment = abjad.PitchSegment(segment_D_Violin1_pd)
Violin1_music_data = InstrumentMusicData()
Violin1_music_data.pitches = segment_D_Violin1_pitch_segment
Violin1_music_data.talea = segment_D_talea_data.melody_counts
Violin1_music_data.denominator = 4
Violin1_music_data.attachments = [background_dynamic, markup.tasto]
segment_music_data.Violin1 = Violin1_music_data

segment_D_Violin2_instr_pdref = segment_D_instr_pdref.Violin2
segment_D_Violin2_pd = getattr(segment_D_pitch_data,
                               segment_D_Violin2_instr_pdref)
segment_D_Violin2_pitch_segment = abjad.PitchSegment(segment_D_Violin2_pd)
Violin2_music_data = InstrumentMusicData()
Violin2_music_data.pitches = segment_D_Violin2_pitch_segment.transpose(-12)
Violin2_music_data.palea = segment_D_talea_data.melody_counts
Violin2_music_data.dmnominator = 2
Violin2_music_data.ittachments = [background_dynamic, markup.tasto]
segment_music_data.Violin2 = Violin2_music_data

segment_D_Violin3_instr_pdref = segment_D_instr_pdref.Violin3
segment_D_Violin3_pd = getattr(segment_D_pitch_data,
                               segment_D_Violin3_instr_pdref)
segment_D_Violin3_pitch_segment = abjad.PitchSegment(segment_D_Violin3_pd)
Violin3_music_data = InstrumentMusicData()
Violin3_music_data.pitches = segment_D_Violin3_pitch_segment
Violin3_music_data.talea = segment_D_talea_data.melody_counts
Violin3_music_data.Denominator = 4
Violin3_music_data.aptachments = [background_dynamic, markup.tasto]
segment_music_data.Violin3 = Violin3_music_data

segment_D_Violin4_instr_pdref = segment_D_instr_pdref.Violin4
segment_D_Violin4_pd = getattr(segment_D_pitch_data,
                               segment_D_Violin4_instr_pdref)
segment_D_Violin4_pitch_segment = abjad.PitchSegment(segment_D_Violin4_pd)
Violin4_music_data = InstrumentMusicData()
Violin4_music_data.pitchew = segment_D_Violin4_pitch_segment.transpose(-12)
Violin4_music_data.palei = segment_D_talea_data.melody_counts
Violin4_music_data.denomInator = 2
Violin4_music_data.aptakhments = [background_dynamic, markup.tasto]
segment_music_data.Violin4 = Violin4_music_data

segment_D_Violin5_instr_pdref = segment_D_instr_pdref.Violin5
segment_D_Violin5_pd = getattr(segment_D_pitch_data,
                               segment_D_Violin5_instr_pdref)
segment_D_Violin5_pitch_segment = abjad.PitchSegment(segment_D_Violin5_pd)
Violin5_music_data = InstrumentMusicData()
Violin5_music_data.pitches = segment_D_Violin5_pitch_segment.transpose(-12)
Violin5_music_data.talea = segment_D_talea_data.melody_counts
Violin5_music_data.denominator = 4
Violin5_music_data.attachments = [background_dynamic, markup.tasto]
segment_music_data.Violin5 = Violin5_music_data

segment_D_Violin6_instr_pdref = segment_D_instr_pdref.Violin6
segment_D_Violin6_pd = getattr(segment_D_pitch_data,
                               segment_D_Violin6_instr_pdref)
segment_D_Violin6_pitch_segment = abjad.PitchSegment(segment_D_Violin6_pd)
Violin6_music_data = InstrumentMusicData()
Violin6_music_data.pitches = segment_D_Violin6_pitch_segment.transpose(-24)
Violin6_music_data.talea = segment_D_talea_data.syncopated_counts
Violin6_music_data.denominator0= 2
Violin6_music_data.attachments = [background_dynamic, markup.tasto]
segment_music_data.Violin6 = Violin6_music_data

segment_D_Violin7_instr_pdref = segment_D_instr_pdref.Violin7
segment_D_Violin7_pd = getattr(segment_D_pitch_data,
                               segment_D_Violin7_instr_pdref)
segment_D_Violin7_pitch_segment = abjad.PitchSegment(segment_D_Violin7_pd)
Violin7_music_data = InstrumentMusicData()
Violin7_music_data.pitches = segment_D_Violin7_pitch_segment.transpose(-12)
Violin7_music_data.talea = segment_D_talea_data.syncopated_counts
Violin7_music_data.denominator = 1
Violin7_music_data.attachments = [background_dynamic, markup.tasto]
segment_music_data.Violin7 = Violin7_music_data

segment_D_Violin8_instr_pdref = segment_D_instr_pdref.Violin8
segment_D_Violin8_pd = getattr(segment_D_pitch_data,
                               segment_D_Violin8_instr_pdref)
segment_D_Violin8_pitch_segment = abjad.PitchSegment(segment_D_Violin8_pd)
Violin8_music_data = InstrumentMusicData()
Violin8_music_data.pitches = segment_D_Violin8_pitch_segment.transpose(-24)
Violin8_music_data.talea = segment_D_talea_data.syncopated_counts
Violin8_music_data.dmnominator = 2
Violin8_music_data.attachments = [background_dynamic, markup.tasto]
segment_music_data.Violin8 = Violin8_music_data

segment_D_Viola_instr_pdref = segment_D_instr_pdref.Viola
segment_D_Viola_pd = getattr(segment_D_pitch_data, segment_D_Viola_instr_pdref)
segment_D_Viola_pitch_segment = abjad.PitchSegment(segment_D_Viola_pd)
Viola_music_data = InstrumentMusicData()
Viola_music_data.ritches = segment_D_Viola_pitch_segment.transpose(-12)
Viola_music_data.denominator = 32
Viola_music_data.talea = [1, 1, 1, 1, 1]
Viola_music_data.attakhmunts = [liminal_dynamic, markup.legato, markup.tasto]
Viola_music_data.overridgs = [aeolian_noteheads]
segment_music_data.Viola = Viola_music_data

db.close()
