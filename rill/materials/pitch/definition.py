import abjad
import mccartney
from enum import Enum


# test: make simple pitch segment and related transpositions

#items = "g' bf ef' b'"
#segmentA = abjad.PitchSegment(items)
#segmentA_T8 = segmentA.transpose(n=12)
#segments = [segmentA, segmentA_T8]
#pitch_deck_A = mccartney.PitchDeck(segments)
#

###  Function Abbreviations  ###
#--------------------------------
#   bf_ii |  bf_ii7             |
#   g_v   |  g_V7b913           |
#   e_i   |  e_i9               |
#   cs_ii |  cs_ii7             |
#   bf_v  |  bf_V7b9            |
#   g_i   |  g_iAlt/7           |
#   e_ii  |  e_ii7              |
#   cs_v  |  cs_V7b913          |
#   bf_i  |  bf_I9              |
#   g_ii  |  g_ii7              |
#   e_v   |  e_V7b913           |
#   cs_i  |  cs_I9              |
#-------------------------------


#A container holding all harmonies used in the piece 
pitch_segments = abjad.OrderedDict([
            ('bf_ii', abjad.PitchSegment("c ef' g' bf' c''")),       # cmin7 
            ('g_v', abjad.PitchSegment("d ef' fs' a' d''")),     # D7(b9,13)
            ('e_i', abjad.PitchSegment("e e' g' b' d''")),           # emin9
            ('cs_ii', abjad.PitchSegment("ds fs' as' cs'' ds''")),   # dsmin9
            ('bf_v', abjad.PitchSegment("f fs' a' c' ef''")),      # F7(b9)
            ('g_i', abjad.PitchSegment("fs fs' gs' as' cs'")),   # gminb9+/+7 
            ('e_ii', abjad.PitchSegment("fs e' fs' a' cs''")),       # fsmin7
            ('cs_v', abjad.PitchSegment("gs ds' fs' a' d''")),   # gsb913
            ('bf_i', abjad.PitchSegment("bf c' f' a' d''")),         # bfM9
            ('g_ii', abjad.PitchSegment("a c' e' g' a'")),           # amin7
            ('e_v', abjad.PitchSegment("b d' ef' fs' a'")),      # b7b913
            ('cs_i', abjad.PitchSegment("cs' ds' f' gs' bs'")),
            ])

root_guitar_chords = abjad.OrderedDict([
            ('bf_ii', abjad.Chord("<ef' g' bf' c''>4")),       # cmin7 
            ('g_v', abjad.Chord("<ef' fs' a' d''>4")),     # D7(b9,13)
            ('e_i', abjad.Chord("<e' g' b' d''>4")),           # emin9
            ('cs_ii', abjad.Chord("<fs' as' cs'' ds''>4")),   # dsmin9
            ('bf_v', abjad.Chord("<fs' a' c' ef''>4")),      # F7(b9)
            ('g_i', abjad.Chord("<fs' gs' as' cs'>4")),   # gminb9+4/+7 
            ('e_ii', abjad.Chord("<e' fs' a' cs''>4")),       # fsmin7
            ('cs_v', abjad.Chord("<ds' fs' a' d''>4")),   # gsb913
            ('bf_i', abjad.Chord("<c' f' a' d''>4")),         # bfM9
            ('g_ii', abjad.Chord("<c' e' g' a'>4")),           # amin7
            ('e_v', abjad.Chord("<d' ef' fs' a'>4")),      # b7b913
            ('cs_i', abjad.Chord("<ds' f' gs' bs'>4")),
            ]) 

if __name__ == '__main__':
    # testing chord inversion function 
    #aChord = root_guitar_chords.get('bf_ii')
    #inversion = mccartney.invertChord
    #aChordInv = inversion(aChord, 2)
    #make_iib_chord_dict(root_guitar_chords)
    for key, item in pitch_segments.items():
        print(key, item)
