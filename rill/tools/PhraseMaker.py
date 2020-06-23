import abjad 


def make_four_bar_phrase(harmony=None, durations=None):
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


