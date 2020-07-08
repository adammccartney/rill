import abjad

from FuzzyHarmony import FuzzyHarmony

# Testing Fuzzy Harmony and related routines
# also testing Progression class



Segment = abjad.PitchSegment("ef' g' bf' c''")       # cmin7 
Name = 'bf_ii'
Inversion = 1
Bf_ii = FuzzyHarmony(name, segment, inversion)
#print(bf_ii.shortname, bf_ii.segment, bf_ii.inversion)
g_v = FuzzyHarmony('g_v', abjad.PitchSegment("d ef' fs' a' d''"), 2)     # D7(b9,13)
e_i = FuzzyHarmony('e_i', abjad.PitchSegment("e e' g' b' d''"), 0)          # emin9
print(g_v)
harmonies = (bf_ii, g_v, e_i)
progression_ = Progression(harmonies)
print(progression_.get_progression())
print(progression_.get_harmony(2))
harmony = progression_.get_harmony(2)
print(harmony.__dict__)
new_fuzzy = FuzzyHarmony('cs_ii', abjad.PitchSegment("ds fs' as' cs'' ds''"), 3)
#progression_.set_harmony(new_fuzzy, 2) # trying to write a modifying 
#print(progression_.get_progression())  # operation for what is a tuple 
prog_a = replace_and_make_new_progression(progression_, 0, new_fuzzy)
print(prog_a)
new_note = invert_up(segment, 3)
print("new note: ", new_note)
#new_pitch = get_global_minima(segment)
#print(new_pitch)
#new_note = invert_up(segment, 333)
#print("new note: ", new_note)
new_note = invert_up(segment, -433)
print("new note: ", new_note)
new_note = invert_down(segment, -4)
print("new note: ", new_note)

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


# testing new fuzzy harmony @property 
# Create Pitch Material
bf_ii = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1) # cmin7
g_v = FuzzyHarmony('g_v', abjad.PitchSegment("ef' fs' a' d''"), 2)     # D7(b9,13)
e_i = FuzzyHarmony('e_i', abjad.PitchSegment("e' g' b' d''"), 0)          # emin9

# make progression 
harmonies = (bf_ii, g_v, e_i)
progression = Progression(harmonies)

    

