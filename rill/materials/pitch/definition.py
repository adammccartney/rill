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
rill_chords = abjad.OrderedDict([
            ('bf_ii', abjad.Chord("<c ef' g' bf' c''>4")),       # cmin7 
            ('g_v', abjad.Chord("<d ef' fs' a' d''>4")),     # D7(b9,13)
            ('e_i', abjad.Chord("<e e' g' b' d''>4")),           # emin9
            ('cs_ii', abjad.Chord("<ds fs' as' cs'' ds''>4")),   # dsmin9
            ('bf_v', abjad.Chord("<f fs' a' c' ef''>4")),      # F7(b9)
            ('g_i', abjad.Chord("<fs fs' gs' as' cs'>4")),   # gminb9+4/+7 
            ('e_ii', abjad.Chord("<fs e' fs' a' cs''>4")),       # fsmin7
            ('cs_v', abjad.Chord("<gs ds' fs' a' d''>4")),   # gsb913
            ('bf_i', abjad.Chord("<bf c' f' a' d''>4")),         # bfM9
            ('g_ii', abjad.Chord("<a c' e' g' a'>4")),           # amin7
            ('e_v', abjad.Chord("<b d' ef' fs' a'>4")),      # b7b913
            ('cs_i', abjad.Chord("<cs' ds' f' gs' bs'>4")),
            ])


def make_key_function_list(chord_dict):
    """
    Takes an ordered dictionary of abjad.Chords 
    returns a list of the dictionaries keys
    """
    key_functions = []
    keys = rill_chords.keys()
    for key in keys:
        key_functions.append(key)
    return key_functions
