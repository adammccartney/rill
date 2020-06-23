import abjad 

import rill.tools.FuzzyHarmony as FuzzyHarmony

harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1) # cmin7/e
durations = [
        abjad.Duration(2, 4),
        abjad.Duration(3, 4),
        abjad.Duration(3, 4),
        abjad.Duration(6, 4),
        abjad.Duration(2, 4),
        ]

def make_four_bar_phrase(harmony):
    """
    Takes a harmony and makes a four bar phrase
    Phrase is partially hard coded to be useful 
    for the segments of the score rill
    """

    pitches = harmony.pitches
    pitch_list = []
    for pitch in pitches:
        pitch_list.append(pitch.name)
    pitch_list.append(None) # append none prep rest
    maker = abjad.LeafMaker()
    pitches = pitch_list
    leaves = maker(pitches, durations)
    container = abjad.Container(leaves)
    meter = abjad.Meter(4,4)
    abjad.mutate(container).rewrite_meter(meter)
    return container


phrase = make_four_bar_phrase(harmony)
abjad.f(phrase)

harmony_two = FuzzyHarmony()
