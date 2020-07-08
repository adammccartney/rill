import abjad
import rill


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


def order_material(progression, durations, phrase_stream):
    """Makes phrases and adds them to stream
    returns an instance of PhraseStream
    """
    augment_with_rest = None
    augmented_fragments = []
    for harmony in progression: 
        augment_with_rest = harmony + (None,)
        augmented_fragments.append(augment_with_rest)
    for item in augmented_fragments:
        phrase_stream.make_extension(item, durations)
    return phrase_stream

   
