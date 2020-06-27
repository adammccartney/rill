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

    def make_phrase(self, durations, denominator, divisions, pitches):
        # make rhythm with one tuplet per division
        stack = rmakers.stack(
            rmakers.talea(
                durations,
                denominator, 
                extra_counts=(0, 0, 0),
            ),
            rmakers.beam()
        )
        selection = stack(divisions)

        # attach time signature to first leaf in each tuplet
        assert len(divisions) == len(selection)
        previous_time_signature = None
        for division, tuplet in zip(divisions, selection):
            time_signature = abjad.TimeSignature(division)
            leaf = abjad.select(tuplet).leaf(0)
            if time_signature != previous_time_signature:
                abjad.attach(time_signature, leaf)
                previous_time_signature = time_signature

        # apply pitch material
        cyclic_tuple = abjad.CyclicTuple(pitches) 
        iterator = abjad.iterate(selection).logical_ties(pitched=True) # make iterator out of selection using logical ties as virtual measures
        iterator = enumerate(iterator) # makes enum out of iterator  
        for index, logical_tie in iterator:
            pitch = cyclic_tuple[index]
            for old_leaf in logical_tie:
                if isinstance(pitch, int):
                    old_leaf.written_pitch = pitch
                elif isinstance(pitch, str):
                    # warning: was formerly checking for list
                    new_leaf = abjad.Chord(pitch, old_leaf.written_duration)
                    indicators = abjad.inspect(old_leaf).indicators()
                    if indicators != None:
                        for indicator in indicators:
                            abjad.attach(indicator, new_leaf)
                    abjad.mutate(old_leaf).replace(new_leaf)
                elif isinstance(pitch, abjad.Chord):
                    new_leaf = abjad.Chord(pitch, old_leaf.written_duration)
                    indicators = abjad.inspect(old_leaf).indicators()
                    if indicators != None:
                        for indicator in indicators:
                            abjad.attach(indicator, new_leaf)
                    abjad.mutate(old_leaf).replace(new_leaf)

        # remove trivial 1:1 tuplets
        self._extend_container(selection)
        command = rmakers.extract_trivial()
        command(selection)


     #   def get_container(self):
      #      """Returns phrase as abjad.Container"""


if __name__ == '__main__':
    import rill.tools.FuzzyHarmony as FuzzyHarmony

    harmony_third = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1) # cmin7/e
    durations = [2, 3, 3, 6, 2]
    denominator = 4
    divisions = [(4, 4)] * 5
    pitches = harmony_third.pitch_list
    print(pitches)
    phrase_one = abjad.Container()
    music_one = PhraseMaker(phrase_one)
    music_one.make_phrase(durations, denominator, divisions, pitches)
    
    components = phrase_one.components 
    for component in components:
        abjad.f(component)

    note = phrase_one[0]
    abjad.f(note)
