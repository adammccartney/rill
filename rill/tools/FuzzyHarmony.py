import abjad

class FuzzyHarmony(object):
    """
    Stores a collection of notes in a PitchSegment
    Fuzzy because the names are used to roughly track
    the position in a given harmonic sequence and not
    to store precise information on the harmony.
    e.g.:
    bf_ii = key of bflat, minor harmony on ii degree 

    """

    ### CLASS ATTRIBUTES ###

    __slots__ = (
        "_pitches",
        "inversion",
        "segment",
        "shortname",
    )

    def __init__(self, shortname=str(), segment=None, inversion=0):
        self.shortname = shortname
        self.segment = abjad.PitchSegment(segment)
        self.inversion = inversion
        self._set_pitches()

    def __repr__(self):
        """
        Simple string represenation of harmony
        Similiar layout to a dict
        """
        segment_str = str(self.segment)
        shortname_str = str(self.shortname)
        return '{}: {}'.format(shortname_str, segment_str)

    ### PRIVATE METHODS ###

    def _set_pitches(self):
        pitches = self.segment.to_pitches()
        self._pitches = tuple(pitches)

    ### PUBLIC PROPERTIES ###

    @property
    def pitches(self):
        """
        Gets pitches
        """
        return self._pitches


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
        for harmony in progression:
            return progression[index]

def replace_and_make_new_progression(progression, index, fuzzy_harmony):
    """
    Takes three arguments
    progression to copy
    index to change
    fuzzy_harmony to insert
    
    makes new progression, similar to the old 
    but containing fuzzy_harmony inserted at index
    """
    new_progression = progression.get_progression()
    progression_list = []
    for i in range(len(new_progression)):
        progression_list.append(new_progression[i])
    progression_list[index] = fuzzy_harmony
    new_progression = tuple(progression_list)
    return new_progression

def get_global_minima(pitch_segment):
    """
    returns global minima of a pitch segment
    as a single member list containing an abjad.Pitch()
    """
    result = []
    bottom_index = 0
    minima = pitch_segment[bottom_index]
    if 3 <= len(pitch_segment):        # works for triads and above
        for i in range(len(pitch_segment)):
            new_min = pitch_segment[i]
            if minima > new_min:
                minima = new_min
        result.append(minima)
        global_minima = abjad.NamedPitch(result[bottom_index]) # could build check
        return global_minima   

def invert_up(segment, inversion):
    """
    inverts a chord upwards
    assumes segment is within octave range
    returns new pitch segment

    Warning: no sanity check on transposition at the moment
    i.e. you can invert 433 times and still generate strings
    that represent pitches
    """
    interval = 12
    new_segment = segment
    
    if inversion < 0:
        print("Inversion needs to be a positive int")
    for i in range(inversion):
        segment = new_segment
        lowest_note = get_global_minima(segment) #call global_minima to find lowest note
        set_ = abjad.PitchSet(
                items=[lowest_note.name],
                item_class=abjad.NamedPitch,
                )
        transposed_set = set_.transpose(interval)  #transposed note is lowest note.tranpose("+P8")
        transposed_pitch = None
        for i in transposed_set:
            transposed_pitch = abjad.NamedPitch(i)
        new_pitches = []
        segment_len = len(segment)
        section = range(1, segment_len)    # trim lowest note
        for i in section:                 
            new_pitches.append(segment[i])
        new_pitches.append(transposed_pitch) # append transposed 
        new_segment = abjad.PitchSegment(new_pitches) # make new segment
    return new_segment

def get_global_maxima(pitch_segment):
    """
    returns the highest abjad.NamedPitch in a PitchSegment
    """
    result = []
    top_index = -1
    maxima = pitch_segment[top_index]         # last item in list is top of segment
    if 3 <= len(pitch_segment):        # works for triads and above
        for i in range(len(pitch_segment)):
            new_max = pitch_segment[i]
            if maxima < new_max:
                maxima = new_max
        result.append(maxima)
        global_maxima = abjad.NamedPitch(result[top_index]) # could build check
        return global_maxima  

def invert_down(segment, inversion):
    """
    inverts a chord downwards
    assumes segment is within octave range
    returns new pitch segment

    Warning: no sanity check on transposition at the moment
    i.e. you can invert -433 times and still generate strings
    that represent pitches
    """

    if inversion > 0:
        print("Inversion needs to be a negative int")
    interval = -12
    new_segment = segment
    for i in range(abs(inversion)):
        segment = new_segment
        highest_note = get_global_maxima(segment) #call global_minima to find lowest note
        set_ = abjad.PitchSet(
                items=[highest_note.name],
                item_class=abjad.NamedPitch,
                )
        transposed_set = set_.transpose(interval)  #transposed note is lowest note.tranpose("+P8")
        transposed_pitch = None
        for i in transposed_set:
            transposed_pitch = abjad.NamedPitch(i)   # initialize as named pitch
        new_pitches = []
        segment_len = len(segment)
        section = range(0, segment_len - 1)    # trim lowest note
        new_pitches.append(transposed_pitch) # append transposed 
        for i in section:                 
            new_pitches.append(segment[i])
        new_segment = abjad.PitchSegment(new_pitches) # make new segment
    return new_segment


