import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony
from rill.tools.PhraseMaker import PhraseStream as PhraseStream

from rill.materials.pitch.definition import (
                               transposition_lookup, 
                               diatonic_register_lookup
                               )

def get_pitch_classes(pitch_segment):
    if isinstance(pitch_segment, abjad.PitchSegment):
        pitch_classes = pitch_segment.to_pitch_classes()
        return pitch_classes

def make_diads(fuzzy_harmonies, interval_doubling=None):
    """
    Harmonizes with lookup table 
    Returns a list of tuples
    """
    harmonized_melodies = []
    if interval_doubling == None:
        for harmony in fuzzy_harmonies:
            harmonized_melody = []
            melody = harmony.pitches
            for pitch in melody:
                harmonized_melody.append(pitch)
        harmonized_melodies.append(harmonized_melody)
        print("harmonized_melodies: ", harmonized_melodies)
        return harmonized_melodies 
    else: 
        diatonic_lookup = diatonic_register_lookup[interval_doubling]
        for harmony in fuzzy_harmonies:
            melody = harmony.pitches
            harmonized_melody = []
            for pitch in melody:
                pitch_class = pitch.pitch_class
                harmonized_pitch = pitch + diatonic_lookup[pitch_class] 
                diad = (harmonized_pitch, pitch)
                harmonized_melody.append(diad)
            harmonized_melodies.append(tuple(harmonized_melody))
        return harmonized_melodies

def make_augmented_stream(progression):
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

