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
chords = abjad.OrderedDict([
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

def make_key_function_list(chord_dict):
    """
    Takes an ordered dictionary of abjad.Chords 
    returns a list of the dictionary's keys
    """
    key_functions = []
    keys = chord_dict.keys()
    for key in keys:
        key_functions.append(key)
    return key_functions

#def make_new_dict(keylist, items):
#    new_dict = OrderedDict()
#    for key in keylist:

def make_iib_chord_dict(chord_dict, inv=2): 
    func_list = make_key_function_list(chord_dict) # make list of keys
    list_ii = func_list[::3] # stride over list to get keys of type ii 
    iib_chords = []
    for key in list_ii:
        chord = chord_dict.get(key)
        inversion = mccartney.invertChord
        iib_chord = inversion(chord, inv) 
        iib_chords.append(iib_chord)
    #print(iib_chords)
    keys = list_ii[:]
    iib_keys = []
    for name in keys:
        name+='b'
        iib_keys.append(name)
    #print(iib_keys)
    # make dict{'key': 'chord'} for each key,chord in zip(iib_keys,iib_chords)
    iib_dict = {}
    for key, chord in zip(iib_keys, iib_chords):
        iib_dict[key] = chord
    return iib_dict

def make_ia_chord_dict(chord_dict, inv=1):
    func_list = make_key_function_list(chord_dict) # make list of keys
    list_i = func_list[2::3] # stride over list to get keys of type ii 
    #print(list_i)
    ia_chords = []
    for key in list_i:
        chord = chord_dict.get(key)
        inversion = mccartney.invertChord
        ia_chord = inversion(chord, inv) 
        ia_chords.append(ia_chord)
    #print(iib_chords)
    keys = list_i[:]
    ia_keys = []
    for name in keys:
        name+='a'
        ia_keys.append(name)
    #print(iib_keys)
    # make dict{'key': 'chord'} for each key,chord in zip(iib_keys,iib_chords)
    ia_dict = {}
    for key, chord in zip(ia_keys, ia_chords):
        ia_dict[key] = chord
    #print(ia_dict)
    return ia_dict



if __name__ == '__main__':
    # testing chord inversion function 
    aChord = root_guitar_chords.get('bf_ii')
    inversion = mccartney.invertChord
    aChordInv = inversion(aChord, 2)
    make_iib_chord_dict(root_guitar_chords)
