import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony
from rill.tools.PhraseMaker import PhraseStream as PhraseStream

from rill.materials.pitch.definition import transposition_lookup

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

def mod_twelve(semitones):
    """makes a positive or negative wrap value for semitone arg"""
    if semitones in range(-176, 0):
        neg_wrap_tval = (semitones % 12) * -1 # make negative
        return neg_wrap_tval
    elif semitones in range(0, 176):
        wrap_tval = semitones % 12
        return wrap_tval
    else: 
        raise ValueError('outside transposible range')

def wrap_transposition(val):
    """
    Currently designed to return an int
    can be adapted to also return mircrotones
    returns a wrapped value
    """
    if val <= 0 or val >= 12:
        print("inside if of wrap_tran...")
        wrapval = mod_twelve(val)
        return wrapval 
    else:
        return val

def transpose(fuzzy_harmonies, transposed_harmonies, t_interval=0):
    """Takes a lits of fuzzy harmony objects
    returns a new list of related objects
    based on an interval argument
    """
    wrapped_t_interval = wrap_transposition(t_interval)
    harmony_shortname_lookup = transposition_lookup[wrapped_t_interval]

    for harmony in fuzzy_harmonies:
        transposed_name = harmony_shortname_lookup[harmony.shortname]
        transposed_segment = harmony.segment.transpose(n=t_interval)
        transposed_harmony = FuzzyHarmony(
                                 transposed_name, 
                                 transposed_segment, 
                                 )
        transposed_harmonies.append(transposed_harmony)
    return transposed_harmonies

