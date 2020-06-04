import abjad
import rill

## method for inverting chords
#def invertChord(chord, inv):
#    if 0 > inv > 4:
#        print("can't invert beyond tetrads")
#    invertedChord = abjad.Chord()
#    _chord = chord.__copy__()
#    if isinstance(chord, abjad.Chord):
#        for i in range(inv):
#            noteList = _chord.note_heads               # copy noteheads to new list 
#            lowestNoteHead = noteList.pop(0)          # get lowest note_head
#            lowestPitch = lowestNoteHead.named_pitch  # note_head to pitch
#            highestPitch = lowestPitch.transpose(12)  # transpose up an octave
#            highestNoteHead = abjad.NoteHead(highestPitch.name) # Pitch to NoteHead
#            newNoteList = noteList[0::]               # make new list of upper tones
#            newNoteList.append(highestNoteHead)       # append notehead to list
#            _chord.note_heads = newNoteList           # reset _chord with permuted list
#            # print(_chord)
#        return _chord                                 # return target inversion
#


#def invert(old_segment, shift): # arguments = PitchSegment, rotation
#    """invert PitchSegments as if they were chords"""
#    print(old_segment.to_pitches())
#    if shift > len(old_segment): # check rotation !> PitchSegment length
#        message = "Rotation argument too large: retry with transposed segment"
#        raise ValueError(message)
#    new_segment = old_segment.rotate(n=shift)    # rotate to desired position
#    print(new_segment.to_pitches())
#    pitches = new_segment.to_pitches()
#    print("new_segment as pitches :", pitches)
#    plist = []
#    for pitch in pitches:
#        plist.append(pitch)
#    print(plist)
#    pitch_set = abjad.PitchSet(
#            plist,
#            item_class=abjad.NamedPitch,
#            ) # make PitchSet for easy rotation + transposition
#    print(pitch_set)
#   # if 0 < rotation: # bottom_to_top
#        ## transpose rotated pitches 8ve
#
### modify copied pitch segment
## if rotation == top_to_bottom
### transpose rotated pitches 8vb
### modify copied pitch segment
## return modfieif copied pitch segment

def make_iterable_pitch_set(segment):
    """returns list of pitches"""
    set_ = abjad.PitchSet(
        segment,
        item_class=abjad.NamedPitch,
        )
    iterator = abjad.iterate(set_).pitches()
    set_full = []
    for i in iterator:
        set_full.append(i)
    return set_full
    
def trim_pitch(iterable_pitch_set, last=True):
    """trims item from list""" 
    set_trim = []
    pitch_set = iterable_pitch_set
    if last:      # if last is true, trim last element
        for item in pitch_set[:-1]:
            set_trim.append(item) 
    if not last:  # if not, trim first
        for item in pitch_set[1:]:
            set_trim.append(item)
    return set_trim

def global_maxima(pitch_segment):
    result = []
    maxima = pitch_segment[0]
    if 3 <= len(pitch_segment):
        for i in range(len(pitch_segment)):
            new_max = pitch_segment[i]
            if maxima < new_max:
                maxima = new_max
        result.append(maxima)
        return result

def global_minima(pitch_segment):
    result = []
    minima = pitch_segment[0]
    if 3 <= len(pitch_segment):
        for i in range(len(pitch_segment)):
            new_min = pitch_segment[i]
            if minima > new_min:
                minima = new_min
        result.append(minima)
        return result  
 

def invert(segment, shift):
    """
    inverts PitchSegments as if they were chords
    
    returns new pitch segment
    """

    # check that we can get local max & min
    print(segment)
    print(segment.local_maxima)


def invert(segment, shift):
    """
    invert PitchSegments as if they were chords
    
    returns a new segment
    """
    new_segment = segment
    for i in range(shift):
        if 0 > shift:          # if shift is negative, transpose top to bottom
            # run this loop shift times
            segment = new_segment
            top_list = global_maxima(segment)
            for top_pitch in top_list:
                new_bottom = top_pitch
                transposed = abjad.NamedInterval("-P8").transpose(top_pitch)
            print("transposed: ", transposed)
            set_full = make_iterable_pitch_set(segment) # convert to iterable
            print("full set: ", set_full)
            set_trim = trim_pitch(set_full, True) # trim top pitch 
            set_trim.insert(0, new_bottom)    
            new_set = set_trim
            print("after transpose", new_set)
            new_segment = abjad.PitchSegment(new_set)
            print("before looping :", new_segment)

        if 0 < shift:
            # run this loop shift times
            bottom_list = global_minima(segment)
            segment = new_segment
            new_top = abjad.NamedPitch()
            for bottom_pitch in bottom_list:
                new_top = abjad.NamedInterval("+P8").transpose(bottom_pitch)
            print(new_top)
            set_full = make_iterable_pitch_set(segment)
            print("full set: ", set_full)
            set_trim = trim_pitch(set_full, False) # trim bottom pitch
            set_trim.append(new_top)
            new_set = set_trim
            print("after transpose", new_set)
            new_segment = abjad.PitchSegment(new_set)
            print("before looping :", new_segment)
    return new_segment # returns the inverted segment

# convert segment to pitch set
# check shift to see direction of transposition
# if positive modify local minima up
# if negative modify local maxima down


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
            print("appending :", chord)
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



   
if __name__ == '__main__':

    a = abjad.PitchSegment("c' d' e' f' g'")
    b = abjad.PitchSegment("f c' c'' e' g'")
    print("a min: ",global_minima(a))
    print("a max: ", global_maxima(a))
    print("b min: ",global_minima(b))
    print("b max: ", global_maxima(b))
    
    
    
    
    
    
    
    
    #    pitch_segments = rill.pitch_segments
    #    seg_bf_ii = pitch_segments['bf_ii']
    #    print(seg_bf_ii)
    #    segment = seg_bf_ii.rotate(n=2)
    #    print(segment)
    #    # a_set = invert(seg_bf_ii, 2)
    #    #print(a_set)
    #    inversionTB = invert(segment, -2)
    #    print("segment =",segment)
    #    print("inversionTB : ",inversionTB)
    #    inversionBT = invert(segment, 2)
    #    print("inversionBT : ", inversionBT)
    #    
    #    it_pitch_set = make_iterable_pitch_set(seg_bf_ii)
    #    print(it_pitch_set)
    #    top_trim = trim_pitch(it_pitch_set, True)
    #    bottom_trim = trim_pitch(it_pitch_set, False)
    #    print("top_trim: ",top_trim)
    #    print("bottom_trim", bottom_trim)
    #
    segment = abjad.PitchSegment("c' e' g' bf'")
    segment = abjad.PitchSegment([1, 3, 5, 7, -9])
    top_list = segment.local_maxima
    print("top_list: ", top_list)
    first_inv = invert(segment, 1)
    second_inv = invert(segment, 2)
    third_inv = invert(segment, 3)
    fourth_inv = invert(segment, 4)
    nfirst_inv = invert(segment, -1)
    nsecond_inv = invert(segment, -2)
    nthird_inv = invert(segment, -3)
    nfourth_inv = invert(segment, -4) 
    print(
            "first_inv: ", first_inv,
            "second_inv: ", second_inv,
            "third_inv: ", third_inv,
            "fourth_inv: ", fourth_inv,
            "n-first_inv: ", nfirst_inv,
            "n-second_inv: ", nsecond_inv,
            "n-third_inv: ", nthird_inv,
            "n-fourth_inv: ", nfourth_inv,
           )

#     a = abjad.NamedPitch("a'")
#     a_t = abjad.NamedInterval("+P8").transpose(a)
#     print(a_t)

#
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
