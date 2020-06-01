import abjad 
import mccartney 
import rill 

from abjadext import rmakers 


class ProgressionDefinition(object):
    """
    Progression definition

    makes harmonic progression

    """

    ### CLASS ATTRIBUTES ###

    __slots__ = ("_chord_names", "_chords", "_progression", "dictionary", "name")

    ### INITIALIZER ###

    def __init__(self, dictionary=None, name=None):
        self.dictionary = dictionary or {}
        self.name = name
        self._progression = self.dictionary.items()
        self._handle_chord_names()
        self._make_progression()

    ### PRIVATE METHODS ###

    def _handle_chord_names(self):
        """extract harmonic functions from dictionary"""
        chord_names = []
        for item in self.dictionary:
            chord_names.append(item)
        self._chord_names = chord_names

    def _make_progression(self):
        """ Makes cyclic tuple of abjad.Chords"""
        chords = []
        for chord_name in self._chord_names:
            chords.append(self.dictionary.get(chord_name))
        self._chords = chords
        cyclic_tuple = abjad.CyclicTuple(self._chords) # make pitch material
        self._progression = cyclic_tuple                # generate chord progression

    ### PROPERTIES ###

    @property 
    def chord_names(self):
        """Returns list of chord names"""
        return self._chord_names
    
    @property
    def chords(self):
        """Returns list of abjad.Chord objects"""
        return self._chords

    @property
    def progression(self):
        """Returns progression as cyclic tuple (of chords/pitches)"""
        return self._progression


import itertools 

guitar_chord_dict = rill.root_guitar_chords
chords = dict(itertools.islice(guitar_chord_dict.items(), 3))
print(chords)
progression_A = ProgressionDefinition(chords)
print(progression_A.chord_names)
print(progression_A.chords)
print(progression_A.progression)

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
 
        # apply pitch material
        cyclic_tuple = abjad.CyclicTuple(pitches) 
        iterator = abjad.iterate(selection).logical_ties(pitched=True) # make iterator out of selection using logical ties as virtual measures
        iterator = enumerate(iterator) # makes enum out of iterator  
        for index, logical_tie in iterator:
            pitch = cyclic_tuple[index]
            for old_leaf in logical_tie:
                if isinstance(pitch, int):
                    old_leaf.written_pitch = pitch
                elif isinstance(pitch, list):
                    new_leaf = abjad.Chord(pitch, old_leaf.written_duration)
                    indicators = abjad.inspect(old_leaf).indicators()
                    if indicators != None:
                        for indicator in indicators:
                            abjad.attach(indicator, new_leaf)
                    abjad.mutate(old_leaf).replace(new_leaf)



        # iterate through the chord dictionary
        # yield chord progression as pitch material
        
