
import shelve
import abjad

from pathlib import Path

from rill.materials.music_init_data.definition import InstrumentMusicData
from rill.materials.music_init_data.definition import SegmentMusicData


rill_dir = Path.cwd().parents[1] # ../rill/
db_path = rill_dir / 'materials' / 'music_data' / 'music_data_shelve'

print(f"segment_G.music_data.py accessing db at: ", db_path)

db = shelve.open(str(db_path))

segment_G_pitch_data = db['segment_G_pitch_data']
segment_G_talea_data = db['segment_G_talea_data']
segment_G_instr_pdref = db['segment_G_instr_pdref']


segment_music_data = SegmentMusicData()

segment_G_Flute1_instr_pdref = segment_G_instr_pdref.Flute1
segment_G_Flute1_pd = getattr(segment_G_pitch_data, segment_G_Flute1_instr_pdref)
segment_G_Flute1_pitch_segment = abjad.PitchSegment(segment_G_Flute1_pd)
Flute1_music_data = InstrumentMusicData()
Flute1_music_data.pitches = segment_G_Flute1_pitch_segment
segment_music_data.Flute1 = Flute1_music_data

segment_G_Flute2_instr_pdref = segment_G_instr_pdref.Flute2
segment_G_Flute2_pd = getattr(segment_G_pitch_data, segment_G_Flute2_instr_pdref)
segment_G_Flute2_pitch_segment = abjad.PitchSegment(segment_G_Flute2_pd)
Flute2_music_data = InstrumentMusicData()
Flute2_music_data.pitches = segment_G_Flute2_pitch_segment
segment_music_data.Flute2 = Flute2_music_data

segment_G_Flute3_instr_pdref = segment_G_instr_pdref.Flute3
segment_G_Flute3_pd = getattr(segment_G_pitch_data, segment_G_Flute3_instr_pdref)
segment_G_Flute3_pitch_segment = abjad.PitchSegment(segment_G_Flute3_pd)
Flute3_music_data = InstrumentMusicData()
Flute3_music_data.pitches = segment_G_Flute3_pitch_segment
segment_music_data.Flute3 = Flute3_music_data

segment_G_Flute4_instr_pdref = segment_G_instr_pdref.Flute4
segment_G_Flute4_pd = getattr(segment_G_pitch_data, segment_G_Flute4_instr_pdref)
segment_G_Flute4_pitch_segment = abjad.PitchSegment(segment_G_Flute4_pd)
Flute4_music_data = InstrumentMusicData()
Flute4_music_data.pitches = segment_G_Flute4_pitch_segment
segment_music_data.Flute4 = Flute4_music_data

segment_G_Bbclarinet1_instr_pdref = segment_G_instr_pdref.Bbclarinet1
segment_G_Bbclarinet1_pd = getattr(segment_G_pitch_data, segment_G_Bbclarinet1_instr_pdref)
segment_G_Bbclarinet1_pitch_segment = abjad.PitchSegment(
segment_G_Bbclarinet1_pd)
Bbclarinet1_music_data = InstrumentMusicData()
Bbclarinet1_music_data.pitches = segment_G_Bbclarinet1_pitch_segment
segment_music_data.Bbclarinet1 = Bbclarinet1_music_data

segment_G_Vibraphone_instr_pdref = segment_G_instr_pdref.Vibraphone
segment_G_Vibraphone_pd = getattr(segment_G_pitch_data, segment_G_Vibraphone_instr_pdref)
segment_G_Vibraphone_pitch_segment = abjad.PitchSegment(
segment_G_Vibraphone_pd)
Vibraphone_music_data = InstrumentMusicData()
Vibraphone_music_data.pitches = segment_G_Vibraphone_pitch_segment
segment_music_data.Vibraphone = Vibraphone_music_data

segment_G_Violin1_instr_pdref = segment_G_instr_pdref.Violin1
segment_G_Violin1_pd = getattr(segment_G_pitch_data, segment_G_Violin1_instr_pdref)
segment_G_Violin1_pitch_segment = abjad.PitchSegment(segment_G_Violin1_pd)
Violin1_music_data = InstrumentMusicData()
Violin1_music_data.pitches = segment_G_Violin1_pitch_segment
segment_music_data.Violin1 = Violin1_music_data

segment_G_Violin2_instr_pdref = segment_G_instr_pdref.Violin2
segment_G_Violin2_pd = getattr(segment_G_pitch_data, segment_G_Violin2_instr_pdref)
segment_G_Violin2_pitch_segment = abjad.PitchSegment(segment_G_Violin2_pd)
Violin2_music_data = InstrumentMusicData()
Violin2_music_data.pitches = segment_G_Violin2_pitch_segment
segment_music_data.Violin2 = Violin2_music_data

segment_G_Violin3_instr_pdref = segment_G_instr_pdref.Violin3
segment_G_Violin3_pd = getattr(segment_G_pitch_data, segment_G_Violin3_instr_pdref)
segment_G_Violin3_pitch_segment = abjad.PitchSegment(segment_G_Violin3_pd)
Violin3_music_data = InstrumentMusicData()
Violin3_music_data.pitches = segment_G_Violin3_pitch_segment
segment_music_data.Violin3 = Violin3_music_data

segment_G_Violin4_instr_pdref = segment_G_instr_pdref.Violin4
segment_G_Violin4_pd = getattr(segment_G_pitch_data, segment_G_Violin4_instr_pdref)
segment_G_Violin4_pitch_segment = abjad.PitchSegment(segment_G_Violin4_pd)
Violin4_music_data = InstrumentMusicData()
Violin4_music_data.pitches = segment_G_Violin4_pitch_segment
segment_music_data.Violin4 = Violin4_music_data

segment_G_Violin5_instr_pdref = segment_G_instr_pdref.Violin5
segment_G_Violin5_pd = getattr(segment_G_pitch_data, segment_G_Violin5_instr_pdref)
segment_G_Violin5_pitch_segment = abjad.PitchSegment(segment_G_Violin5_pd)
Violin5_music_data = InstrumentMusicData()
Violin5_music_data.pitches = segment_G_Violin5_pitch_segment
segment_music_data.Violin5 = Violin5_music_data

segment_G_Violin6_instr_pdref = segment_G_instr_pdref.Violin6
segment_G_Violin6_pd = getattr(segment_G_pitch_data, segment_G_Violin6_instr_pdref)
segment_G_Violin6_pitch_segment = abjad.PitchSegment(segment_G_Violin6_pd)
Violin6_music_data = InstrumentMusicData()
Violin6_music_data.pitches = segment_G_Violin6_pitch_segment
segment_music_data.Violin6 = Violin6_music_data

segment_G_Violin7_instr_pdref = segment_G_instr_pdref.Violin7
segment_G_Violin7_pd = getattr(segment_G_pitch_data, segment_G_Violin7_instr_pdref)
segment_G_Violin7_pitch_segment = abjad.PitchSegment(segment_G_Violin7_pd)
Violin7_music_data = InstrumentMusicData()
Violin7_music_data.pitches = segment_G_Violin7_pitch_segment
segment_music_data.Violin7 = Violin7_music_data

segment_G_Violin8_instr_pdref = segment_G_instr_pdref.Violin8
segment_G_Violin8_pd = getattr(segment_G_pitch_data, segment_G_Violin8_instr_pdref)
segment_G_Violin8_pitch_segment = abjad.PitchSegment(segment_G_Violin8_pd)
Violin8_music_data = InstrumentMusicData()
Violin8_music_data.pitches = segment_G_Violin8_pitch_segment
segment_music_data.Violin8 = Violin8_music_data

segment_G_Viola_instr_pdref = segment_G_instr_pdref.Viola
segment_G_Viola_pd = getattr(segment_G_pitch_data, segment_G_Viola_instr_pdref)
segment_G_Viola_pitch_segment = abjad.PitchSegment(segment_G_Viola_pd)
Viola_music_data = InstrumentMusicData()
Viola_music_data.pitches = segment_G_Viola_pitch_segment
segment_music_data.Viola = Viola_music_data

db.close()