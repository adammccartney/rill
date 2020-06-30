import abjad 

from abjadext import rmakers

class PhraseMaker(object):
    """
    Makes a musical phrase by combining
    pitches from a harmony and durations

    Single slot is a container

    This class is purely for modifying the container
    i.e. populating it with music
    """

    ### INITIALIZER ###

    def __init__(self, container=None):
        self._container = container

    def __format__(self, format_specification="") -> str:
        """
        Formats phrase.
        """
        return abjad.StorageFormatManager(self).get_storage_format()
    
    def _extend_container(self, selection):
        self._container.extend(selection)
    
    ### PUBLIC METHODS ###

    def make_notes(self, pitches, durations):
        """Returns a container with leaves"""
        maker = abjad.LeafMaker()
        leaves = maker(pitches, durations)
        self._extend_container(leaves)
        
    @property
    def container(self):
        """Gets container"""
        return self._container

if __name__ == '__main__':
    import rill.tools.FuzzyHarmony as FuzzyHarmony
    import rill.tools.PhraseMaker as PhraseMaker

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
    phrase_maker = PhraseMaker(container)
    phrase_maker.make_notes(pitches, durations)
    made = phrase_maker.container
    abjad.f(made)

