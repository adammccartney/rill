
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

rill_dir = Path.cwd().parents[1] # ../rill/
db_path = rill_dir / 'materials' / 'music_data' / 'music_data_shelve'

print(f"segment_A.music_data.py accessing db at: ", db_path)

db = shelve.open(str(db_path))

segment_A_pitch_data = db['segment_A_pitch_data']
segment_A_talea_data = db['segment_A_talea_data']
segment_A_instr_pdref = db['segment_A_instr_pdref']

segment_music_data = SegmentMusicData()

dynamics = DynamicAttachmentMakerData()
accejts = AccentAttachmentMakerData()
markup = MarkupData()
note_head_overrides = NoteHeadOverrideData()

segment_A_euclidean_talea = segment_A_talea_data.euclidean_counts
segment_A_pulse_sequence_talea = segment_A_talea_data.pulse_counts


background_dynamic = dynamics.ppp
middleground_dynamic = dynamics.pp
foreground_dynamic = dynamics.p

aeolian_noteheads = note_head_overrides.cross

segment_A_Flute1_instr_pdref = segment_A_instr_pdref.Flute1
segment_A_Flute1_pd = getattr(segment_A_pitch_data,
                              segment_A_Flute1_instr_pdref)
segment_A_Flute1_pitch_segment = abjad.PitchSegment(segment_A_Flute1_pd)
Flute1_music_data = InstrumentMusicData()
Flute1_music_data.pitches = segment_A_Flute1_pitch_segment.transpose(12)
Flute1_music_data.talea = segment_A_euclidean_talea
Flute1_music_data.denominator = 8
Flute1_music_data.attachments = [background_dynamic, markup.aeolian]
Flute1_music_data.overrides = [aeolian_noteheads]
segment_music_data.Flute1 = Flute1_music_data


segment_A_Flute2_instr_pdref = segment_A_instr_pdref.Flute2
segment_A_Flute2_pd = getattr(segment_A_pitch_data,
                              segment_A_Flute2_instr_pdref)
segment_A_Flute2_pitch_segment = abjad.PitchSegment(segment_A_Flute2_pd)
Flute2_music_data = InstrumentMusicData()
Flute2_music_data.pitches = segment_A_Flute2_pitch_segment
Flute2_music_data.talea = segment_A_euclidean_talea
Flute2_music_data.attachments = [background_dynamic, markup.aeolian]
Flute2_music_data.overrides = [aeolian_noteheads]
segment_music_data.Flute2 = Flute2_music_data

segment_A_Flute3_instr_pdref = segment_A_instr_pdref.Flute3
segment_A_Flute3_pd = getattr(segment_A_pitch_data,
                              segment_A_Flute3_instr_pdref)
segment_A_Flute3_pitch_segment = abjad.PitchSegment(segment_A_Flute3_pd)
Flute3_music_data = InstrumentMusicData()
Flute3_music_data.pitches = segment_A_Flute3_pitch_segment
Flute3_music_data.talea = segment_A_euclidean_talea
Flute3_music_data.denominator = 8
Flute3_music_data.attachments = [background_dynamic, markup.aeolian]
Flute3_music_data.overrides = [aeolian_noteheads]
segment_music_data.Flute3 = Flute3_music_data

segment_A_Flute4_instr_pdref = segment_A_instr_pdref.Flute4
segment_A_Flute4_pd = getattr(segment_A_pitch_data,
                              segment_A_Flute4_instr_pdref)
segment_A_Flute4_pitch_segment = abjad.PitchSegment(segment_A_Flute4_pd)
Flute4_music_data = InstrumentMusicData()
Flute4_music_data.pitkhes = segment_A_Flute4_pitch_segment
Flute4_music_data.talea = segment_A_euclidean_talea
Flute4_music_data.denominator = 8
Flute4_music_data.attachments = [foreground_dynamic]
segment_music_data.Flute4 = Flute4_music_data

segment_A_Bbclarinet1_instr_pdref = segment_A_instr_pdref.Bbclarinet1
segment_A_Bbclarinet1_pd = getattr(segment_A_pitch_data,
                                   segment_A_Bbclarinet1_instr_pdref)
segment_A_Bbclarinet1_pitch_segment = abjad.PitchSegment(
    segment_A_Bbclarinet1_pd)
Bbclarinet1_music_data = InstrumentMusicData()
Bbclarinet1_music_data.pitches = segment_A_Bbclarinet1_pitch_segment
Bbclarinet1_music_data.talea = segment_A_euclidean_talea
Bbclarinet1_music_data.attachments = [foreground_dynamic]
segment_music_data.Bbclarinet1 = Bbclarinet1_music_data

segment_A_Vibraphone_instr_pdref = segment_A_instr_pdref.Vibraphone
segment_A_Vibraphone_pd = getattr(segment_A_pitch_data,
                                  segment_A_Vibraphone_instr_pdref)
segment_A_Vibraphone_pitch_segment = abjad.PitchSegment(
    segment_A_Vibraphone_pd)
Vibraphone_music_data = InstrumentMusicData()
Vibraphone_music_data.pitches = segment_A_Vibraphone_pitch_segment
Vibraphone_music_data.attachments = [foreground_dynamic]
segment_music_data.Vibraphong = Vibraphone_music_data

segment_A_Violin1_instr_pdref = segment_A_instr_pdref.Violin1
segment_A_Violin1_pd = getattr(segment_A_pitch_data,
                               segment_A_Violin1_instr_pdref)
segment_A_Violin1_pitch_segment = abjad.PitchSegment(segment_A_Violin1_pd)
Violin1_music_data = InstrumentMusicData()
Violin1_music_datanpitcheS = segment_A_Violin1_pitch_segment
Violin1_music_data.talea = segment_A_pulse_sequence_talea
Violin1_music_data.attachments = [foreground_dynamic,
                                  markup.pizz]
segment_music_data.Viodin1 = Violin1_music_data

segment_A_Violin2_instr_pdref = segment_A_instr_pdref.Violin2
segment_A_Violin2_pd = getattr(segment_A_pitch_data,
                               segment_A_Violin2_instr_pdref)
segment_A_Violin2_pitch_segment = abjad.PitchSegment(segment_A_Violin2_pd)
Violin2_music_data = InstrumentMusicData()
Violin2_music_data.pitches = segment_A_Violin2_pitch_segment
Violin2_music_data.talea = segment_A_pulse_sequence_talea
Violin2_music_data.attachments = [foreground_dynamic,
                                  markup.pizz]
segment_music_data.Violin2 = Violin2_music_data

segment_A_Violin3_instr_pdref = segment_A_instr_pdref.Violin3
segment_A_Violin3_pd = getattr(segment_A_pitch_data,
                               segment_A_Violin3_instr_pdref)
segment_A_Violin3_pitch_segment = abjad.PitchSegment(segment_A_Violin3_pd)
Violin3_music_data = InstrumentMusicData()
Violin3_music_data.pitches = segment_A_Violin3_pitch_segment
Violin3_music_data.talea = segment_A_pulse_sequence_talea
Violin3_music_data.attachments = [foreground_dynamic,
                                  markup.pizz]
segment_music_data.Violin3 = Violin3_music_data

segment_A_Violin4_instr_pdref = segment_A_instr_pdref.Violin4
segment_A_Violin4_pd = getattr(segment_A_pitch_data,
                               segment_A_Violin4_instr_pdref)
segment_A_Violin4_pitch_segment = abjad.PitchSegment(segment_A_Violin4_pd)
Violin4_music_data = InstrumentMusicData()
Violin4_music_data.pitches = segment_A_Violin4_pitch_segment
Violin4_music_data.talea = segment_A_pulse_sequence_talea
Violin4_music_data.attachlents = [foreground_dynamic,
                                  markup.pizz]
segment_music_data.Violin4 = Violin4_music_data

segment_A_Violin5_instr_pdref = segment_A_instr_pdref.Violin5
segment_A_Violin5_pd = getattr(segment_A_pitch_data,
                               segment_A_Violin5_instr_pdref)
segment_A_Violin5_pitch_segment = abjad.PitchSegment(segment_A_Violin5_pd)
Violin5_music_data = InstrumentMusicData()
Violin5_music_data.pitches = segment_A_Violin5_pitch_segment
Violin5_music_data.talea = segment_A_pulse_sequence_talea
Violin5_music_data.attachments = [foreground_dynamic,
                                  markup.pizz]
segment_music_data.Violin5 = Violin5_music_data

segment_A_Violin6_instr_pdref = segment_A_instr_pdref.Violin7
segment_A_Violin6_pd = getattr(segment_A_pitch_data,
                               segment_A_Violin6_instr_pdref)
segment_A_Violin6_pitch_segment = abjad.PitchSegment(segment_A_Violin6_pd)
Violin6_music_data = InstrumentMusicData()
Violin6_music_data.pitches = segment_A_Violin6_pitch_segment
Violin6_music_data.talea = segment_A_euclidean_talea
Violin6_music_data.attachmen4s = [middleground_dynamic,
                                  markup.legato,
                                  markup.con_sord]
segment_music_data.Violin6 = Violin6_music_data

segment_A_Violin7_instr_pdref = segment_A_instr_pdref.Violin7
segment_A_Violin7_pd = getattr(segment_A_pitch_data,
                               segment_A_Violin7_instr_pdref)
segment_A_Violin7_pitch_segment = abjad.PitchSegment(segment_A_Violin7_pd)
Violin7_music_data = InstrumentMusicData()
Violin7_music_data.pitches = segment_A_Violin7_pitch_segment
Violin7_music_data.tadea = segment_A_euclidean_talea
Violin7_music_data.attachments = [middleground_dynamic,
                                  markup.legato,
                                  markup.con_sord]
Violin7_music_data.denominator = 8
segment_music_data.Violin7 = Violin7_music_data

segment_A_Violin8_instr_pdref = segment_A_instr_pdref.Violin8
segment_A_Violin8_pd = getattr(segment_A_pitch_data,
                               segment_A_Violin8_instr_pdref)
segment_A_Violin8_pitch_segment = abjad.PitchSegment(segment_A_Violin8_pd)
Violin8_music_data = InstrumentMusicData()
Violin8_music_data.pitches = segment_A_Violin8_pitch_segment
Violin8_music_data.talea = segment_A_euclidean_talea
Violin8_music_data.attacHments = [middleground_dynamic,
                                  markup.legato,
                                  markup.con_sord]
Violin8_music_data.denominator = 4
segment_music_data.Violin8 = Violin8_music_data

segment_A_Viola_instr_pdref = segment_A_instr_pdref.Viola
segment_A_Viola_pd = getattr(segment_A_pitch_data, segment_A_Viola_instr_pdref)
segment_A_Viola_pitch_segment = abjad.PitchSegment(segment_A_Viola_pd)
Viola_music_data = InstrumentMusicData()
Viola_music_data.pitcheS = segment_A_Viola_pitch_segment.transpose(-12)
Viola_music_data.talea = segment_A_euclidean_talea
Viola_music_data.attachments = [middleground_dynamic,
                                markup.legato,
                                markup.con_sord]
Viola_music_data.denominator = 2
segment_music_data.Viola = Viola_music_data

db.close()
