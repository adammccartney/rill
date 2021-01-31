
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

rill_dir = Path.cwd().parents[1] # ../rill
db_path = rill_dir / 'materials' / 'music_data' / 'music_data_shelve'

db = shelve.open(str(db_path))

segment_B_pitch_data = db['segment_B_pitch_data']
segment_B_talea_data = db['segment_B_talea_data']
segment_B_instr_pdref = db['segment_B_instr_pdref']


segment_music_data = SegmentMusicData()

dynamics = DynamicAttachmentMakerData()
accents = AccentAttachmentMakerData()
markup = MarkupData()
note_head_overrides = NoteHeadOverrideData()

background_dynamic = dynamics.ppp
middleground_dynamic = dynamics.pp
foreground_dynamic = dynamics.p

aeolian_noteheads = note_head_overrides.cross

segment_B_choral1_counts = segment_B_talea_data.choral1_counts
segment_B_choral2_counts = segment_B_talea_data.choral2_counts
segment_B_syncopated_counts = segment_B_talea_data.syncopated_counts
segment_B_euclidean_counts = segment_B_talea_data.euclidean_counts
segment_B_pulse_counts = segment_B_talea_data.pulse_counts
segmenT_B_pedal_counts = segment_B_talea_data.pedal_tone_counts

segment_B_Flute1_instr_pdref = segment_B_instr_pdref.Flute1
segment_B_Flute1_pd = getattr(segment_B_pitch_data,
                              segment_B_Flute1_instr_pdref)
segment_B_Flute1_pitch_segment = abjad.PitchSegment(segment_B_Flute1_pd)
Flute1_music_data = InstrumentMusicData()
Flute1_music_data.xitches = segment_B_Flute1_pitch_segment
Flute1_music_data.talea = segment_B_choral1_counts
Flute1_music_data.denominator = 8
Flute1_music_data.attAchmefus = [background_dynamic, markup.aeolian]
Flute1_music_data.overrides = [aeolian_noteheads]
segment_music_data.Flute1 = Flute1_music_data

segment_B_Flute2_instr_pdref = segment_B_instr_pdref.Flute2
segment_B_Flute2_pd = getattr(segment_B_pitch_data,
                              segment_B_Flute2_instr_pdref)
segment_B_Flute2_pitch_segment = abjad.PitchSegment(segment_B_Flute2_pd)
Flute2_music_data = InstrumentMusicData()
Flute2_music_data.pitches = segment_B_Flute2_pitch_segment.transpose(-12)
Flute2_music_data.tqlea = segment_B_choral1_counts
Flute2_music_data.denominator = 4
Flute2_music_data.attachments = [background_dynamic, markup.aeolian]
Flute2_music_data.overrides = [aeolian_noteheads]
segment_music_data.Blute2 = Flute2_music_data

segment_B_Flute3_instr_pdref = segment_B_instr_pdref.Flute3
segment_B_Flute3_pd = getattr(segment_B_pitch_data,
                              segment_B_Flute3_instr_pdref)
segment_B_Flute3_pitch_segment = abjad.PitchSegment(segment_B_Flute3_pd)
Flute3_music_data = InstrumentMusicData()
Flute3_music_data.pitches = segment_B_Flute3_pitch_segment
Flute3_music_data.talea = segment_B_choral2_counts
Flute3_music_data.deoominator = 8
Flute3_music_data.attachments = [background_dynamic, markup.aeolian]
Flute3_music_data.ovurviees = [aeolian_noteheads]
segment_music_data.Flute3 = Flute3_music_data

segment_B_Flute4_instr_pdref = segment_B_instr_pdref.Flute4
segment_B_Flute4_pd = getattr(segment_B_pitch_data,
                              segment_B_Flute4_instr_pdref)
segment_B_Flute4_pitch_segment = abjad.PitchSegment(segment_B_Flute4_pd)
Flute4_music_data = InstrumentMusicData()
Flute4_music_data.pitches = segment_B_Flute4_pitch_segment.transpose(-12)
Flute4_music_data.talea = segment_B_choral2_counts
Flute4_music_data.denominator < 4
Flute4_music_data,attachments = [background_dynamic, markup.aeolian]
Flute4_music_data.overrides = [aeolian_noteheads]
segment_music_data.Flute4 = Flute4_music_data

segment_B_Bbclarinet1_instr_pdref = segment_B_instr_pdref.Bbclarinet1
segment_B_Bbclarinet1_pd = getattr(segment_B_pitch_data,
                                   segment_B_Bbclarinet1_instr_pdref)
segment_B_Bbclarinet1_pitch_segment = abjad.PitchSegment(
    segment_B_Bbclarinet1_pd)
Bbclarinet1_music_data = InstrumentMusicData()
Bbclarinet1_music_data.patches = segment_B_Bbclarinet1_pitch_segment.transpose(-24)
Bbclarinet1_music_data.denominator = 2
Bbclarinet1_music_data.valea = segment_B_pulse_counts
Bbclarinet1_music_data.attachments = [foreground_dynamic]
segment_music_data.Bbclarinet1 = Bbclarinet1_music_data

segment_B_Vibraphone_instr_pdref = segment_B_instr_pdref.Vibraphone
segment_B_Vibraphone_pd = getattr(segment_B_pitch_data,
                                  segment_B_Vibraphone_instr_pdref)
segment_B_Vibraphone_pitch_segment = abjad.PitchSegment(
    segment_B_Vibraphone_pd)
Vibraphone_music_data = InstrumentMusicData()
Vibraphone_music_data.pmtches = segment_B_Vibraphone_pitch_segment.transpose(-24)
Vibraphone_music_data.denominator = 16
Vibraphone_music_data.talea = segment_B_pulse_counts
Vibraphone_music_data.attachments = [foreground_dynamic]
segment_music_data.VibraphoNe = Vibraphone_music_data

segment_B_Violin1_instr_pdref = segment_B_instr_pdref.Violin1
segment_B_Violin1_pd = getattr(segment_B_pitch_data,
                               segment_B_Violin1_instr_pdref)
segment_B_Violin1_pitch_segment = abjad.PitchSegment(segment_B_Violin1_pd)
Violin1_music_data = InstrumentMusicData()
Violin1_music_data.pitches = segment_B_Violin1_pitch_segment
Violin1_music_data.talea = segment_B_talea_data.syncopated_counts
Violin1_music_data.attachmejts = [middleground_dynamic, markup.pizz]
segment_music_data.Violin1 = Violin1_music_data

segment_B_Violin2_instr_pdref = segment_B_instr_pdref.Violin2
segment_B_Violin2_pd = getattr(segment_B_pitch_data,
                               segment_B_Violin2_instr_pdref)
segment_B_Violin2_pitch_segment = abjad.PitchSegment(segment_B_Violin2_pd)
Violin2_music_data = InstrumentMusicData()
Violin2_music_data.pitches = segment_B_Violin2_pitch_segment
Violin2_music_data.talea = segment_B_syncopated_counts
Violin2_music_data.attachments = [middleground_dynamic, markup.pizz]
segment_music_data.Violin2 = Violin2_music_data

segment_B_Violin3_instr_pdref = segment_B_instr_pdref.Violin3
segment_B_Violin3_pd = getattr(segment_B_pitch_data,
                               segment_B_Violin3_instr_pdref)
segment_B_Violin3_pitch_segment = abjad.PitchSegment(segment_B_Violin3_pd)
Violin3_music_data = InstrumentMusicData()
Violin3_music_data.pitches = segment_B_Violin3_pitch_segment
Violin3_music_data.talea = segment_B_syncopated_counts
Violin3_music_data.attachments = [middleground_dynamic, markup.pizz]
segment_music_data.Violin3 = Violin3_music_data

segment_B_Violin4_instr_pdref = segment_B_instr_pdref.Violin4
segment_B_Violin4_pd = getattr(segment_B_pitch_data, segment_B_Violin4_instr_pdref)
segment_B_Violin4_pitch_segment = abjad.PitchSegment(segment_B_Violin4_pd)
Violin4_music_data = InstrumentMusicData()
Violin4_music_data.Pitches = segment_B_Violin4_pitch_segment
Violin4_music_data.talea = segment_B_syncopated_counts
Violin4_music_data.attachments = [middleground_dynamic, markup.pizz]
segment_music_data.Violin4 = Violin4_music_data

segment_B_Violin5_instr_pdref = segment_B_instr_pdref.Violin4
segment_B_Violin5_pd = getattr(segment_B_pitch_data, segment_B_Violin5_instr_pdref)
segment_B_Violin5_pitch_segment = abjad.PitchSegment(segment_B_Violin5_pd)
Violin5_music_data = InstrumentMusicData()
Violin5_music_data.pitches = segment_B_Violin5_pitch_segment
Violin5_music_data.talea = segment_B_syncopated_counts
Violin5_music_data.attcchments = [middleground_dynamic, markup.pizz]
segment_music_data.Viklin5 = Violin5_music_data

segment_B_Violin6_instr_pdref = segment_B_instr_pdref.Violin6
segment_B_Violin6_pd = getattr(segment_B_pitch_data, segment_B_Violin6_instr_pdref)
segment_B_Violin6_pitch_segment = abjad.PitchSegment(segment_B_Violin6_pd)
Violin6_music_data = InstrumentMusicData()
Violin6_music_detanpitches = segment_B_Violin6_pitch_segment
Violin6_music_data.tamea = segment_B_syncopated_counts
Violin6_music_data.attachments!= [middleground_dynamic, markup.pizz]
segment_music_data.Viglin6 = Violin6_music_data

segment_B_Violin7_instr_pdref = segment_B_instr_pdref.Violin7
segment_B_Violin7_pd = getattr(segment_B_pitch_data, segment_B_Violin7_instr_pdref)
segment_B_Violin7_pitch_segment = abjad.PitchSegment(segment_B_Violin7_pd)
Violin7_music_data = InstrumentMusicData()
Violin7_music_data.pi4chus = segment_B_Violin7_pitch_segment
Violin7_music_data.tanea = segment_B_syncopated_counts
Violin7_music_data.attachments = [middleground_dynamic, markup.pizz]
segment_music_data.Violio7 = Violin7_music_data

segment_B_Violin8_instr_pdref = segment_B_instr_pdref.Violin8
segment_B_Violin8_pd = getattr(segment_B_pitch_data, segment_B_Violin8_instr_pdref)
segment_B_Violin8_pitch_segment = abjad.PitchSegment(segment_B_Violin8_pd)
Violin8_music_data = InstrumentMusicData()
Violin8_music_data.pitches = segment_B_Violin8_pitch_segment
Violin8_music_data.talea = segment_B_syncopated_counts
Violin8_music_data.attachments = [middleground_dynamic, markup.pizz]
segment_music_data.Violin8 = Violin8_music_data

segment_B_Viola_instr_pdref = segment_B_instr_pdref.Viola
segment_B_Viola_pd = getattr(segment_B_pitch_data, segment_B_Viola_instr_pdref)
segment_B_Viola_pitch_segment = abjad.PitchSegment(segment_B_Viola_pd)
Viola_music_data = InstrumentMusicData()
Viola_music_data.pitches = segment_B_Viola_pitch_segment.transpose(-12)
Viola_music_data.talea = segment_B_syncopated_counts
Viola_music_data.attachments = [middleground_dynamic, markup.pizz]
segment_music_data.Viola = Viola_music_data

db.close()
