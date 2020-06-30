import abjad 

import rill.tools.FuzzyHarmony as FuzzyHarmony

def make_notes(pitches, durations, container):
    """Returns a container with leaves"""
    maker = abjad.LeafMaker()
    leaves = maker(pitches, durations)
    container = abjad.Container(leaves)
    return container

if __name__ == '__main__':

    harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1)
    pitches = harmony.numbered_pitch_list
    pitches.append(None)
    durations = [
            abjad.Duration(1, 2), 
            abjad.Duration(3, 4), 
            abjad.Duration(3, 4), 
            abjad.Duration(3, 2),
            abjad.Duration(1, 2),
            ]
    container = abjad.Container()
    made = make_notes(pitches, durations, container)
    abjad.f(made)
