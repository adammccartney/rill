import sys
from pathlib import Path

var = sys.argv[1]
seg_name = f"segment_{var}"  # used to recall music data from db


pitch_data_key = f"{seg_name}_pitch_data"
talea_data_key = f"{seg_name}_talea_data"
instr_pdref_key = f"{seg_name}_instr_pdref"

music_data = f"""
import shelve
import abjad

from pathlib import Path

from rill.materials.music_init_data.definition import InstrumentMusicData
from rill.materials.music_init_data.definition import SegmentMusicData


rill_dir = Path.cwd().parents[1] # ../rill/
db_path = rill_dir / 'materials' / 'music_data' / 'music_data_shelve'

db = shelve.open(str(db_path))

{seg_name}_pitch_data = db['{pitch_data_key}']
{seg_name}_talea_data = db['{talea_data_key}']
{seg_name}_instr_pdref = db['{instr_pdref_key}']


segment_music_data = SegmentMusicData()

{seg_name}_Flute1_instr_pdref = {seg_name}_instr_pdref.Flute1
{seg_name}_Flute1_pd = getattr({seg_name}_pitch_data, segment_A_Flute1_instr_pdref)
{seg_name}_Flute1_pitch_segment = abjad.PitchSegment({seg_name}_Flute1_pd)
Flute1_music_data = InstrumentMusicData()
Flute1_music_data.pitches = {seg_name}_Flute1_pitch_segment
segment_music_data.Flute1 = Flute1_music_data

{seg_name}_Flute2_instr_pdref = {seg_name}_instr_pdref.Flute2
{seg_name}_Flute2_pd = getattr({seg_name}_pitch_data, segment_A_Flute2_instr_pdref)
{seg_name}_Flute2_pitch_segment = abjad.PitchSegment({seg_name}_Flute2_pd)
Flute2_music_data = InstrumentMusicData()
Flute2_music_data.pitches = {seg_name}_Flute2_pitch_segment
segment_music_data.Flute2 = Flute2_music_data

{seg_name}_Flute3_instr_pdref = {seg_name}_instr_pdref.Flute3
{seg_name}_Flute3_pd = getattr({seg_name}_pitch_data, segment_A_Flute3_instr_pdref)
{seg_name}_Flute3_pitch_segment = abjad.PitchSegment({seg_name}_Flute3_pd)
Flute3_music_data = InstrumentMusicData()
Flute3_music_data.pitches = {seg_name}_Flute3_pitch_segment
segment_music_data.Flute3 = Flute3_music_data

{seg_name}_Flute4_instr_pdref = {seg_name}_instr_pdref.Flute4
{seg_name}_Flute4_pd = getattr({seg_name}_pitch_data, segment_A_Flute4_instr_pdref)
{seg_name}_Flute4_pitch_segment = abjad.PitchSegment({seg_name}_Flute4_pd)
Flute4_music_data = InstrumentMusicData()
Flute4_music_data.pitches = {seg_name}_Flute4_pitch_segment
segment_music_data.Flute4 = Flute4_music_data

{seg_name}_Bbclarinet1_instr_pdref = {seg_name}_instr_pdref.Bbclarinet1
{seg_name}_Bbclarinet1_pd = getattr({seg_name}_pitch_data, segment_A_Bbclarinet1_instr_pdref)
{seg_name}_Bbclarinet1_pitch_segment = abjad.PitchSegment(
{seg_name}_Bbclarinet1_pd)
Bbclarinet1_music_data = InstrumentMusicData()
Bbclarinet1_music_data.pitches = {seg_name}_Bbclarinet1_pitch_segment
segment_music_data.Bbclarinet1 = Bbclarinet1_music_data

{seg_name}_Vibraphone_instr_pdref = {seg_name}_instr_pdref.Vibraphone
{seg_name}_Vibraphone_pd = getattr({seg_name}_pitch_data, segment_A_Vibraphone_instr_pdref)
{seg_name}_Vibraphone_pitch_segment = abjad.PitchSegment(
{seg_name}_Vibraphone_pd)
Vibraphone_music_data = InstrumentMusicData()
Vibraphone_music_data.pitches = {seg_name}_Vibraphone_pitch_segment
segment_music_data.Vibraphone = Vibraphone_music_data

{seg_name}_Violin1_instr_pdref = {seg_name}_instr_pdref.Violin1
{seg_name}_Violin1_pd = getattr({seg_name}_pitch_data, segment_A_Violin1_instr_pdref)
{seg_name}_Violin1_pitch_segment = abjad.PitchSegment({seg_name}_Violin1_pd)
Violin1_music_data = InstrumentMusicData()
Violin1_music_data.pitches = {seg_name}_Violin1_pitch_segment
segment_music_data.Violin1 = Violin1_music_data

{seg_name}_Violin2_instr_pdref = {seg_name}_instr_pdref.Violin2
{seg_name}_Violin2_pd = getattr({seg_name}_pitch_data, segment_A_Violin2_instr_pdref)
{seg_name}_Violin2_pitch_segment = abjad.PitchSegment({seg_name}_Violin2_pd)
Violin2_music_data = InstrumentMusicData()
Violin2_music_data.pitches = {seg_name}_Violin2_pitch_segment
segment_music_data.Violin2 = Violin2_music_data

{seg_name}_Violin3_instr_pdref = {seg_name}_instr_pdref.Violin3
{seg_name}_Violin3_pd = getattr({seg_name}_pitch_data, segment_A_Violin3_instr_pdref)
{seg_name}_Violin3_pitch_segment = abjad.PitchSegment({seg_name}_Violin3_pd)
Violin3_music_data = InstrumentMusicData()
Violin3_music_data.pitches = {seg_name}_Violin3_pitch_segment
segment_music_data.Violin3 = Violin3_music_data

{seg_name}_Violin4_instr_pdref = {seg_name}_instr_pdref.Violin4
{seg_name}_Violin4_pd = getattr({seg_name}_pitch_data, segment_A_Violin4_instr_pdref)
{seg_name}_Violin4_pitch_segment = abjad.PitchSegment({seg_name}_Violin4_pd)
Violin4_music_data = InstrumentMusicData()
Violin4_music_data.pitches = {seg_name}_Violin4_pitch_segment
segment_music_data.Violin4 = Violin4_music_data

{seg_name}_Violin5_instr_pdref = {seg_name}_instr_pdref.Violin5
{seg_name}_Violin5_pd = getattr({seg_name}_pitch_data, segment_A_Violin5_instr_pdref)
{seg_name}_Violin5_pitch_segment = abjad.PitchSegment({seg_name}_Violin5_pd)
Violin5_music_data = InstrumentMusicData()
Violin5_music_data.pitches = {seg_name}_Violin5_pitch_segment
segment_music_data.Violin5 = Violin5_music_data

{seg_name}_Violin6_instr_pdref = {seg_name}_instr_pdref.Violin6
{seg_name}_Violin6_pd = getattr({seg_name}_pitch_data, segment_A_Violin6_instr_pdref)
{seg_name}_Violin6_pitch_segment = abjad.PitchSegment({seg_name}_Violin6_pd)
Violin6_music_data = InstrumentMusicData()
Violin6_music_data.pitches = {seg_name}_Violin6_pitch_segment
segment_music_data.Violin6 = Violin6_music_data

{seg_name}_Violin7_instr_pdref = {seg_name}_instr_pdref.Violin7
{seg_name}_Violin7_pd = getattr({seg_name}_pitch_data, segment_A_Violin7_instr_pdref)
{seg_name}_Violin7_pitch_segment = abjad.PitchSegment({seg_name}_Violin7_pd)
Violin7_music_data = InstrumentMusicData()
Violin7_music_data.pitches = {seg_name}_Violin7_pitch_segment
segment_music_data.Violin7 = Violin7_music_data

{seg_name}_Violin8_instr_pdref = {seg_name}_instr_pdref.Violin8
{seg_name}_Violin8_pd = getattr({seg_name}_pitch_data, segment_A_Violin8_instr_pdref)
{seg_name}_Violin8_pitch_segment = abjad.PitchSegment({seg_name}_Violin8_pd)
Violin8_music_data = InstrumentMusicData()
Violin8_music_data.pitches = {seg_name}_Violin8_pitch_segment
segment_music_data.Violin8 = Violin8_music_data

{seg_name}_Viola_instr_pdref = {seg_name}_instr_pdref.Viola
{seg_name}_Viola_pd = getattr({seg_name}_pitch_data, segment_A_Viola_instr_pdref)
{seg_name}_Viola_pitch_segment = abjad.PitchSegment({seg_name}_Viola_pd)
Viola_music_data = InstrumentMusicData()
Viola_music_data.pitches = {seg_name}_Viola_pitch_segment
segment_music_data.Viola = Viola_music_data

db.close()
"""

cwd = Path.cwd()  # ../rill/segments/
output_file_path = cwd / seg_name / 'music_data.py'

output_file = open(output_file_path, 'w')
output_file.write(music_data)
output_file.close()
