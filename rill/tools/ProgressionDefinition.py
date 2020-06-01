import abjad
import rill



guitar_chord_dict = rill.root_guitar_chords

for key in guitar_chord_dict:
    print(guitar_chord_dict[key])


class ProgressionMaker(object):
    """
    Progression maker

    makes a harmonic progression
    """

    def __init__(self, name=None, harmonies=[]):
        self.name = name
        self.harmonies = harmonies


