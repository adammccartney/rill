import abjad

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

class Progression(object):
    """
    Progression

    Makes a harmonic progression
    """
    
    ### INITIALIZER ###

    def __init__(self, chord_dict):
        self._chord_dict = chord_dict.copy()
        self._names = []
        self._chords = []
        self._make_progression()

    def get_chord_dict(self):
        """Returns chords in self._chord_dict as list""" 
        return self._chord_dict

    ### PRIVATE METHODS ###

    def _make_progression(self):
        """Makes list of abjad.Chords"""
        names = []
        chords = []
        for name, chord in self._chord_dict.items(): # for chord in chord_dict
            print("appending :", name)
            names.append(name)
            print("appen?!?jedi=1, ding :", chord)?!? (*_*object: _T*_*) ?!?jedi?!?"
            chords.append(chord)       # append to chords
        self._names = names
        self._chords = chords 

    ### PUBLIC METHODS ###

    def get_names(self):
        return self._names
    
    def get_chords(self):
        return self._chords

    def get_chord(self, key):
        """Returns chord based on key"""
        return self._chord_dict.__getitem__(key)

    def set_chord(self, key, chord):
        """
        Alters a chord on one of the steps
        Ideally replacing with a simple inversion
        """
        self._chord_dict.__setitem__(key, chord)
        self._make_progression()

#class Progression(object):
#    """
#    Progression definition
#
#    makes harmonic progression
#
#    """
#
#    ### CLASS ATTRIBUTES ###
#
#    __slots__ = ("_chord_names", "_chords", "_progression", "materials", "name")
#
#    ### INITIALIZER ###
#
#    def __init__(self, materials={}, name=None):
#        self.materials = materials
#        self.name = name
#        print("set name =", self.name)
#        self._progression = self.materials.items()
#        print("set progression =", self._progression)
#        self._handle_chord_names()
#        #self._make_progression()
#
#    ### PRIVATE METHODS ###
#
#    def _handle_chord_names(self):
#        """extract harmonic functions from dictionary"""
#        chord_names = []
#        for item in self.materials:
#            chord_names.append(item)
#        self._chord_names = chord_names
#
#    def _make_progression(self):
#        """ Makes cyclic tuple of abjad.Chords"""
#        chords = []
#        for chord_name in self._chord_names:
#            chords.append(self.materials.get(chord_name))
#        self._chords = chords
#        cyclic_tuple = abjad.CyclicTuple(self._chords) # make pitch material
#        self._progression = cyclic_tuple                # generate chord progression
#
#    ### PROPERTIES ###
#
#    @property 
#    def chord_names(self):
#        """Returns list of chord names"""
#        return self._chord_names
#    
#    @property
#    def chords(self):
#        """Returns list of abjad.Chord(abjad.Leaf) objects"""
#        return self._chords
#
#    @property
#    def chord_cycle(self):
#        """Returns progression as cyclic tuple (of chords/pitches)"""
#        return self._progression
#    
#    ### PUBLIC METHODS ###
#
#    def get_chord(self, key):
#        """Returns chord based on key"""
#        return self.materials.__getitem__(key)
#
#    def set_chord(self, key, chord):
#        """Sets chord based on key"""
#        self.dictionary.__setitem__(key, chord)
#        self._make_progression()
#
#class Variation(Progression):
#    """
#    Creates a variation by accepting two further arguments for 
#    scale degree and inversion
#    """
#
#    ### CLASS ATTRIBUTES ###
#
#    __slots__ = ("degree", "inversion")
#
#    ### INITIALIZER ###
#
#    def __init__(self, materials={}, name=None, degree=None, inversion=0):
#        super().__init__(materials, name)
#        self.degree = degree
#        self.inversion = inversion
#        self._make_variation()
#    
#    def _make_variation(self):
#        """
#        Makes a simple variation of progression by inverting certain chords
#
#        Not really tracking precise chord/function names in terms of keys
#        Letting python's namespace rules handle this automatically 
#        
#        Purpose of this class is to create flexible harmonic variation
#        """
#        if isinstance(self.degree, str):
#            if self.degree == 'ii' or 'i':
#                search_key = self.degree                       # set to search dictionary
#                res = {}
#                print(self.materials.items())
##                res.update(filter(lambda item: search_key in item[0], self.dictionary.items()))
##                for key in res.keys():
##                    chord_name = key
##                chord = self.get_chord(chord_name)               # get chord of res
##                inverted_chord = invertChord(chord, self.inversion)  # create inversion
##                self.set_chord(chord_name, inverted_chord)       # set inverted chord to progression
##
#
