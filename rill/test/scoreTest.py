import abjad 
import mccartney 
import rill 

from abjadext import rmakers 

### Score
def make_empty_score():
    staff = abjad.Staff()
    score = abjad.Score()
    score.append(staff)
    abjad.setting(staff).instrument_name = abjad.Markup('Staff')
    return score

### LILYPOND FILE
def make_lilypond_file(score):
    lilypond_file = abjad.LilyPondFile.new([score])
    return lilypond_file

# method for inverting chords
def invertChord(chord, inv):
    if 0 > inv > 4:
        print("can't invert beyond tetrads")
    invertedChord = abjad.Chord()
    _chord = chord.__copy__()
    if isinstance(chord, abjad.Chord):
        for i in range(inv):
            noteList = _chord.note_heads               # copy noteheads to new list 
            lowestNoteHead = noteList.pop(0)          # get lowest note_head
            lowestPitch = lowestNoteHead.named_pitch  # note_head to pitch
            highestPitch = lowestPitch.transpose(12)  # transpose up an octave
            highestNoteHead = abjad.NoteHead(highestPitch.name) # Pitch to NoteHead
            newNoteList = noteList[0::]               # make new list of upper tones
            newNoteList.append(highestNoteHead)       # append notehead to list
            _chord.note_heads = newNoteList           # reset _chord with permuted list
            # print(_chord)
        return _chord                                 # return target inversion
 
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
        """Returns list of abjad.Chord(abjad.Leaf) objects"""
        return self._chords

    @property
    def progression(self):
        """Returns progression as cyclic tuple (of chords/pitches)"""
        return self._progression
    
    ### PUBLIC METHODS ###

    def get_chord(self, key):
        """Returns chord based on key"""
        return self.dictionary.__getitem__(key)

    def set_chord(self, key, chord):
        """Sets chord based on key"""
        self.dictionary.__setitem__(key, chord)
        self._make_progression()

class Variation(ProgressionDefinition):
    """
    Creates a variation by accepting two further arguments for 
    scale degree and inversion
    """

    def __init__(self, dictionary=None, name=None, degree=None, inversion=0):
        super().__init__(dictionary, name)
        self.degree = degree
        print(self.degree)
        self.inversion = inversion
        self._make_variation()

    def _make_variation(self):
        """
        Makes a simple variation of progression by inverting certain chords

        Not really tracking precise chord/function names in terms of keys
        Letting python's namespace rules handle this automatically 
        
        Purpose of this class is to create flexible harmonic variation
        """
        print('calling _make_variation')
        if isinstance(self.degree, str):
            if degree == 'ii' or 'i':
                search_key = degree                       # set to search dictionary
                res = dict(filter(lambda item: search_key in item[0], self.dictionary.items()))
                for key in res.keys():
                    chord_name = key
                chord = self.get_chord(chord_name)               # get chord of res
                inverted_chord = invertChord(chord, self.inversion)  # create inversion
                self.set_chord(chord_name, inverted_chord)       # set inverted chord to progression

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
                extra_counts=(0, 0, 0),
            ),
            rmakers.beam()
        )
        selection = stack(divisions)

        # attach time signature to first leaf in each tuplet
        assert len(divisions) == len(selection)
        for division, tuplet in zip(divisions, selection):
            time_signature = abjad.TimeSignature(division)
            leaf = abjad.select(tuplet).leaf(0)
            abjad.attach(time_signature, leaf)
 
        # apply pitch material
        cyclic_tuple = abjad.CyclicTuple(pitches) 
        iterator = abjad.iterate(selection).logical_ties(pitched=True) # make iterator out of selection using logical ties as virtual measures
        iterator = enumerate(iterator) # makes enum out of iterator  
        for index, logical_tie in iterator:
            print("entered the loop make_music")
            pitch = cyclic_tuple[index]
            print(pitch)
            for old_leaf in logical_tie:
                print("here is the old leaf: ", old_leaf)
                if isinstance(pitch, int):
                    print("in if pitch is still", pitch)
                    old_leaf.written_pitch = pitch
                    print(old_leaf)
                elif isinstance(pitch, list):
                    print("entered elif")
                    print("pitch is still", pitch)
                    new_leaf = abjad.Chord(pitch, old_leaf.written_duration)
                    print("this is the new leaf: ", new_leaf)
                    indicators = abjad.inspect(old_leaf).indicators()
                    if indicators != None:
                        for indicator in indicators:
                            abjad.attach(indicator, new_leaf)
                    abjad.mutate(old_leaf).replace(new_leaf)
                elif isinstance(pitch, abjad.Chord):
                    print("entered elif")
                    print("pitch is still", pitch)
                    new_leaf = abjad.Chord(pitch, old_leaf.written_duration)
                    print("this is the new leaf: ", new_leaf)
                    indicators = abjad.inspect(old_leaf).indicators()
                    if indicators != None:
                        for indicator in indicators:
                            abjad.attach(indicator, new_leaf)
                    abjad.mutate(old_leaf).replace(new_leaf)

        # remove trivial 1:1 tuplets
        self.staff.extend(selection)
        command = rmakers.extract_trivial()
        command(selection)

## Define a chord dictionary
root_guitar_chords = abjad.OrderedDict([
            ('bf_ii', abjad.Chord("<ef' g' bf' c''>4")),       # cmin7 
            ('g_v', abjad.Chord("<ef' fs' a' d''>4")),     # D7(b9,13)
            ('e_i', abjad.Chord("<e' g' b' d''>4")),           # emin9
            ('cs_ii', abjad.Chord("<fs' as' cs'' ds''>4")),   # dsmin9
            ('bf_v', abjad.Chord("<fs' a' c' ef''>4")),      # F7(b9)
            ('g_i', abjad.Chord("<fs' gs' as' cs'>4")),   # gminb9+4/+7 
            ('e_ii', abjad.Chord("<e' fs' a' cs''>4")),       # fsmin7
            ('cs_v', abjad.Chord("<ds' fs' a' d''>4")),   # gsb913
            ('bf_i', abjad.Chord("<c' f' a' d''>4")),         # bfM9
            ('g_ii', abjad.Chord("<c' e' g' a'>4")),           # amin7
            ('e_v', abjad.Chord("<d' ef' fs' a'>4")),      # b7b913
            ('cs_i', abjad.Chord("<ds' f' gs' bs'>4")),
            ]) 


# yield chord progression as pitch material
import itertools 

guitar_chord_dict = root_guitar_chords
chords = dict(itertools.islice(guitar_chord_dict.items(), 3)) # make slice
name = "progress_bf-e_iib"
degree = 'ii'
phrase = Variation(chords, name, degree, 1) # make progression
pitches = phrase.chords # return chords in phrase as list

# make music 
score = make_empty_score()
staff = score[0]

maker = MusicMaker(staff)
maker.make_music(
        [3, 3, 3], # durations
        4,         # denominator
        [(3, 4), (3, 4), (3, 4)], # divisions
        pitches,                  # pitches
        )

#maker.make_music(
#        [3, 2, 1],
#        16,
#        [(3, 16), (1, 4), (5, 16), (3, 8)],
#        [7, 5, 4, 2],
#        )
#
score.add_final_bar_line()
lilypond_file = make_lilypond_file(score)
abjad.show(lilypond_file)
