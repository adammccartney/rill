import abjad
import rill

# Test Segment for making sketch of guitar chords


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

# set chord dictionary
guitar_chord_dict = rill.root_guitar_chords

# make phrase selection
import itertools
chords = dict(itertools.islice(guitar_chord_dict.items(), 3)) # make slice

# make music 
score = make_empty_score()
staff = score[0]

maker = rill.MusicMaker(staff)

print(chords)
phrase = rill.Progression(chords)
print(phrase.get_names())
print(phrase.get_chords())

names = phrase.get_names()
for name in names:
    print("searching", name)
    print("found: ", phrase.get_chord(name))

invertChord = rill.invertChord
var_phrase = phrase
target_degree = 'bf_ii'
chord = var_phrase.get_chord(target_degree)
print(var_phrase.get_chords())
inverted_chord = invertChord(chord, 1)
var_phrase.set_chord(target_degree, inverted_chord)
print(var_phrase.get_chords())

#pitches = phrase.chords                      # return chords as list

#maker.make_music(
#        [3, 3, 2], # durations
#        4,         # denominator
#        [(3, 4), (3, 4), (2, 4)], # divisions
#        pitches,                  # pitches
#        )
#

#name = "progress_bf-e_iib"
#degree = 'ii'
#phrase = rill.Variation(chords, name, degree, 1) # make progression
##pitches = phrase.chords # return chords in phrase as list
#
#maker.make_music(
#        [3, 3, 2], # durations
#        4,         # denominator
#        [(3, 4), (3, 4), (2, 4)], # divisions
#        pitches,                  # pitches
#        )
#
## make phrase selection
#chords = dict(itertools.islice(guitar_chord_dict.items(), 3, 6)) # make slice
#
#
#name = "progress_cs-g"
#phrase = ProgressionDefinition(chords, name) # make root progression
#pitches = phrase.chords                      # return chords as list
#
#maker.make_music(
#        [3, 3, 2], # durations
#        4,         # denominator
#        [(3, 4), (3, 4), (2, 4)], # divisions
#        pitches,                  # pitches
#        )
#
#
#name = "progress_cs-g_iib"
#degree = 'ii'
#phrase = Variation(chords, name, degree, 1) # make progression
#pitches = phrase.chords # return chords in phrase as list
#
#maker.make_music(
#        [3, 3, 2], # durations
#        4,         # denominator
#        [(3, 4), (3, 4), (2, 4)], # divisions
#        pitches,                  # pitches
#        )
#
#
#score.add_final_bar_line()
#lilypond_file = make_lilypond_file(score)
#abjad.show(lilypond_file)
#
