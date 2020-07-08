import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony
from rill.tools.PhraseMaker import PhraseStream as PhraseStream

def get_pitch_classes(pitch_segment):
    if isinstance(pitch_segment, abjad.PitchSegment):
        pitch_classes = pitch_segment.to_pitch_classes()
        return pitch_classes

def make_diads(fuzzy_harmonies):
    """
    Harmonizes with lookup table 
    Returns a list of tuples
    """
    harmonized_pitch_lookup = {
            abjad.NamedPitchClass("c"): -5,  # add a P4 below
            abjad.NamedPitchClass("b"): -15,  # add a m10 below
            abjad.NamedPitchClass("bf"): -3, # add a m3 below
            abjad.NamedPitchClass("a"): -3,  # add a m3 below
            abjad.NamedPitchClass("af"): -12, # add an 8vb
            abjad.NamedPitchClass("g"): -11,  # add M7 below
            abjad.NamedPitchClass("fs"): -10, # add m7 below
            abjad.NamedPitchClass("f"): 1,    # add m2 above
            abjad.NamedPitchClass("e"): 2,    # add M2 above
            abjad.NamedPitchClass("ef"): -7,  # add P5 below
            abjad.NamedPitchClass("d"): -8,   # add m6 below
            abjad.NamedPitchClass("cs"): -6,  # add tritone below
            }
    harmonized_melodies = []
    for harmony in fuzzy_harmonies:
        melody = harmony.pitches
        harmonized_melody = []
        for pitch in melody:
            pitch_class = pitch.pitch_class
            harmonized_pitch = pitch + harmonized_pitch_lookup[pitch_class] 
            diad = (harmonized_pitch, pitch)
            harmonized_melody.append(diad)
        harmonized_melodies.append(tuple(harmonized_melody))
    return harmonized_melodies


def make_stream(progression):
    """Makes phrases and adds them to stream
    returns an instance of PhraseStream
    """
    augment_with_rest = None
    augmented_progression = []
    for harmony in progression: 
        augment_with_rest = harmony + (None,)
        augmented_progression.append(augment_with_rest)
    phrase_stream = PhraseStream(augmented_progression)
    return phrase_stream

def transpose_up_fifth(fuzzy_harmonies, transposed_harmonies):
    """Takes a lits of fuzzy harmony objects
    returns a new list of related objects"""

    harmony_shortname_lookup = {
            str("bf_ii"): "f_ii",
            str("g_v"): "d_v",
            str("e_i"): "b_i",
            str("cs_ii"): "gs_ii",
            str("bf_v"): "f_v",
            str("g_i"): "d_i",
            str("e_ii"): "b_ii",
            str("cs_v"): "gs_v",
            str("bf_i"): "f_i",
            str("g_ii"): "d_ii",
            str("e_v"): "b_v",
            str("cs_i"): "gs_i",
            }

    for harmony in fuzzy_harmonies:
        transposed_name = harmony_shortname_lookup[harmony.shortname]
        transposed_segment = harmony.segment.transpose(n=7)
        inversion_num = harmony.inversion
        transposed_harmony = FuzzyHarmony(
                                 transposed_name, 
                                 transposed_segment, 
                                 inversion_num
                                 )
        transposed_harmonies.append(transposed_harmony)
    return transposed_harmonies


