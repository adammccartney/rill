import abjad 
import mccartney 

from abjadext import rmakers 



# Music Maker 
class MusicMaker(object):
    """
    Populates a staff one measure at a time
    """

    def __init__(self, staff):
        self.staff = staff

    def make_music(self, durations, denominator, divisions, pitches):
        # make rhythm with one tuplet per division
        stack = rmakers.stack(
            rmakers.talea(
                durations,
                denominator, 
                extra_counts=(0),
            ),
        )
        selection = stack(divisions)

        # apply chords 
        iterator = abjad.iterate(selection).logical_ties(pitched=True) # make iterator out of selection using logical ties as virtual measures
        iterator = enumerate(iterator) # makes enum out of iterator  
        # iterate through chord dictionaries 
        # Possible harmonic progrssions are: 
        # ii - v - i 
        # iib - v - i
        # iib - v - ia
        # ii - v - ia
