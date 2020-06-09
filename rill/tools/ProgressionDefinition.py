import abjad
import rill

from collections import deque 

class FuzzyHarmony(object):
    """
    Stores a collection of notes in a PitchSegment
    Fuzzy because the names are used to roughly track
    the position in a given harmonic sequence and not
    to store precise information on the harmony.
    e.g.:
    bf_ii = key of bfat, minor harmony on ii degree 

    """
    def __init__(self, shortname, segment, inversion):
        self.shortname = shortname
        self.segment = abjad.PitchSegment(segment)
        self.inversion = inversion

class PitchDeque(object):
    """
    Initialised with a pitch set
    made to contain some easy ways
    to append to front or back
    """

    def __init__(self, iterable_pitch_set):
        self.pitch_deque = deque(iterable_pitch_set)
        self.modified = deque()

    def get_pitch_deque(self):
        return deque(self.pitch_deque)

    def set_modified(self, last=True):
        """
        trims item from list
        will trim last item if last is true 
        returns modified pitch deque
        """ 
        trimmed_pitch_deque = self.pitch_deque
        if last:      # if last is true, trim last element
            trimmed_pitch_deque.pop()
        if not last:  # if not, trim first
            trimmed_pitch_deque.popleft()
        self.modified = trimmed_pitch_deque

    def get_modified(self):
        return self.modified 


def extend_deque(pitch_deque, pitch, beginning=True):
    """adds a pitch at beggining or end based on check"""
    new_deque = deque(pitch_deque)
    if beginning:
        new_deque.appendleft(pitch)
    if not beginning:
        new_deque.append(pitch)
    return new_deque

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
    invert PitchSegments in the style of chord inversions
    
    returns a new segment
    """
#    new_segment = segment
#    transposed = abjad.NamedPitch()
#    print("got this far")
#    print("shift:",shift)
#    for i in range(abs(shift)):
#        print("i = ", i)
#        print("in for loop")
#        segment = new_segment
#        print("segment:", segment)
#        t_interval = "+P8" # set to transpose up octave
#        trim_last = False  # trim the first item from pitch set 
#        select_outer = global_maxima  # function to select top pitch
#        position = True               # will append to beginning
#        if 0 > shift:          # if shift is negative, transpose top to bottom
#            # run this loop shift times
#            t_interval = "-P8"
#            trim_last = True
#            select_outer = global_minima
#            position = False
#        print("got this far")
#        outer_pitch_list = select_outer(segment)
#        print("top list:", top_list)
#        for pitch in outer_pitch_list:
#            transposed = abjad.NamedInterval(t_interval).transpose(pitch)
#        print("transposed: ", transposed)
#        set_full = make_iterable_pitch_set(segment) # convert to iterable
#        print("full set: ", set_full)
#        pitch_deque = PitchDeque(set_full)
#        pitch_deque.set_modified(trim_last) # trim outer
#        pitch_deque.extend_modified(position,transposed)    
#        new_set = pitch_deque.get_modified()
#        new_segment = abjad.PitchSegment(new_set)
#        print("before looping :", new_segment)
#
#    return new_segment
#
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
    iterable_set = make_iterable_pitch_set(a)
    d = PitchDeque(iterable_set)
    print("d.pitch_deque: ", d.pitch_deque)
    d.set_modified(last=True)
    d_ = d.get_modified()
    print("d_: ", d_)
    c = extend_deque(d_, abjad.NamedPitch("a'''"), beginning=True)
    print("c: ", c)
    d = extend_deque(d_, abjad.NamedPitch("b,"), beginning=False)
    print("d: ", d)
    
    #a = abjad.PitchSegment("c' d' e' f' g'")
    #b = abjad.PitchSegment("f c' c'' e' g'")
    #print("a min: ",global_minima(a))
    #print("a max: ", global_maxima(a))
    #print("b min: ",global_minima(b))
    #print("b max: ", global_maxima(b))
    # 
    
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
    #top_list = global_maxima(segment)
    #print("top_list: ", top_list)
    ##first_inv = invert(segment, 1)
    ##second_inv = invert(segment, 2)
    ##third_inv = invert(segment, 3)
    ##fourth_inv = invert(segment, 4)
    #nfirst_inv = invert(segment, -1)
    #nsecond_inv = invert(segment, -2)
    #print(
    #        #       "first_inv: ", first_inv,
    #        #"second_inv: ", second_inv,
    #        #"third_inv: ", third_inv,
    #        #"fourth_inv: ", fourth_inv,
    #        "n-first_inv: ", nfirst_inv,
    #        "n-second_inv: ", nsecond_inv,
    #        )

#   #  a = abjad.NamedPitch("a'")
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
