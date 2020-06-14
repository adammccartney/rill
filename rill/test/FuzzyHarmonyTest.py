import abjad

# Testing Fuzzy Harmony and related routines
# also testing Progression class

class FuzzyHarmony(object):
    """
    Stores a collection of notes in a PitchSegment
    Fuzzy because the names are used to roughly track
    the position in a given harmonic sequence and not
    to store precise information on the harmony.
    e.g.:
    bf_ii = key of bflat, minor harmony on ii degree 

    """
    def __init__(self, shortname, segment, inversion):
        self.shortname = shortname
        self.segment = abjad.PitchSegment(segment)
        self.inversion = inversion

    def __repr__(self):
        """
        Simple string represenation of harmony
        Similiar layout to a dict
        """
        segment_str = str(self.segment)
        shortname_str = str(self.shortname)
        return '{}: {}'.format(shortname_str, segment_str)

class Progression(object):
    """
    Harmonic Progression
    Contains a number of FuzzyHarmonies in a tuple 
    """

    def __init__(self, harmonies=()):
        self._harmonies = harmonies

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
        print(new_progression[i])
        progression_list.append(new_progression[i])
    print(progression_list)
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
        print("nwseg at top: ", new_segment)
        segment = new_segment
        lowest_note = get_global_minima(segment) #call global_minima to find lowest note
        set_ = abjad.PitchSet(
                items=[lowest_note.name],
                item_class=abjad.NamedPitch,
                )
        transposed_set = set_.transpose(interval)  #transposed note is lowest note.tranpose("+P8")
        print("transposed set:", transposed_set)
        transposed_pitch = None
        for i in transposed_set:
            transposed_pitch = abjad.NamedPitch(i)
            print("items: ", i)
        print("transposed_pitch: ", transposed_pitch)
        new_pitches = []
        segment_len = len(segment)
        section = range(1, segment_len)    # trim lowest note
        for i in section:                 
            new_pitches.append(segment[i])
            print(new_pitches)
        new_pitches.append(transposed_pitch) # append transposed 
        print("list of new pitches: ", new_pitches)
        new_segment = abjad.PitchSegment(new_pitches) # make new segment
        print("nwseg: ", new_segment)
    return new_segment

def get_global_maxima(pitch_segment):
    """
    returns the highest
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
    print("Initial segment: ", new_segment)
    for i in range(abs(inversion)):
        print("nwseg at top: ", new_segment)
        segment = new_segment
        highest_note = get_global_maxima(segment) #call global_minima to find lowest note
        print("top note: ", highest_note)
        set_ = abjad.PitchSet(
                items=[highest_note.name],
                item_class=abjad.NamedPitch,
                )
        transposed_set = set_.transpose(interval)  #transposed note is lowest note.tranpose("+P8")
        print("transposed note: ", transposed_set)
        transposed_pitch = None
        for i in transposed_set:
            transposed_pitch = abjad.NamedPitch(i)   # initialize as named pitch
            print("items: ", i)
        print("transposed_pitch: ", transposed_pitch)
        new_pitches = []
        segment_len = len(segment)
        section = range(0, segment_len - 1)    # trim lowest note
        new_pitches.append(transposed_pitch) # append transposed 
        for i in section:                 
            new_pitches.append(segment[i])
            print(new_pitches)
        print("list of new pitches: ", new_pitches)
        new_segment = abjad.PitchSegment(new_pitches) # make new segment
        print("nwseg: ", new_segment)
    return new_segment




if __name__ == '__main__':
    segment = abjad.PitchSegment("ef' g' bf' c''")       # cmin7 
    name = 'bf_ii'
    inversion = 1
    bf_ii = FuzzyHarmony(name, segment, inversion)
    #    #print(bf_ii.shortname, bf_ii.segment, bf_ii.inversion)
    #    g_v = FuzzyHarmony('g_v', abjad.PitchSegment("d ef' fs' a' d''"), 2)     # D7(b9,13)
    #    e_i = FuzzyHarmony('e_i', abjad.PitchSegment("e e' g' b' d''"), 0)          # emin9
    #    print(g_v)
    #    harmonies = (bf_ii, g_v, e_i)
    #    progression_ = Progression(harmonies)
    #    print(progression_.get_progression())
    #    print(progression_.get_harmony(2))
    #    harmony = progression_.get_harmony(2)
    #    print(harmony.__dict__)
    #    new_fuzzy = FuzzyHarmony('cs_ii', abjad.PitchSegment("ds fs' as' cs'' ds''"), 3)
    #    #progression_.set_harmony(new_fuzzy, 2) # trying to write a modifying 
    #    #print(progression_.get_progression())  # operation for what is a tuple 
    #    prog_a = replace_and_make_new_progression(progression_, 0, new_fuzzy)
    #    print(prog_a)
    #    new_note = invert_up(segment, 3)
    #    print("new note: ", new_note)
    #    #new_pitch = get_global_minima(segment)
    #    #print(new_pitch)
    #    #new_note = invert_up(segment, 333)
    #    #print("new note: ", new_note)
    #    new_note = invert_up(segment, -433)
    #    print("new note: ", new_note)
    #    new_note = invert_down(segment, -4)
    #    print("new note: ", new_note)
    #
    set_ = abjad.PitchSet(["bf'"])
    transposed = set_.transpose(12)
    print(transposed)
    transposed = invert_up(bf_ii.segment, 1)
    print("transposed up 1: ", transposed)
    transposed = invert_up(bf_ii.segment, 2)
    print("transposed up 2: ", transposed)
    transposed = invert_up(bf_ii.segment, 3)
    print("transposed up 3: ", transposed)
    transposed = invert_down(bf_ii.segment, -1)
    print("transposed down 1: ", transposed)

    transposed = invert_down(bf_ii.segment, -2)
    print("transposed down 2: ", transposed)

    transposed = invert_down(bf_ii.segment, -3)
    print("transposed down 3: ", transposed)

    transposed = invert_down(bf_ii.segment, -4)
    print("transposed down 4: ", transposed)


    transposed = invert_down(bf_ii.segment, 2) 
    print("transposed down: ", transposed)

    transposed = invert_down(bf_ii.segment, -202) 
    print("transposed down: ", transposed)
