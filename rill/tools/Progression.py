import abjad

class Progression(object):
    """
    Harmonic Progression
    Contains a number of FuzzyHarmonies in a tuple 
    """

    def __init__(self, harmonies):
        self._harmonies = tuple(harmonies)

    ### NON-MODIFYING MEMBER FUNCTIONS ###
    def get_progression(self):
        """returns a tuple of harmonies"""
        return self._harmonies

    def get_harmony(self, index):
        """returns a specific harmony"""
        progression = self.get_progression()
        for chord in progression:
            return progression[index]
