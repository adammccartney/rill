import abjad
import rill

import rill.tools.FuzzyHarmony as FuzzyHarmony
import rill.tools.PhraseMaker as PhraseMaker

from rill.tools.PhraseMaker import PhraseStream as PhraseStream
from rill.tools.PhraseMaker import PhraseOutflow as PhraseOutflow

durations = [
abjad.Duration(1, 2), 
abjad.Duration(3, 4), 
abjad.Duration(3, 4), 
abjad.Duration(3, 2),
abjad.Duration(1, 2),
]

harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1) # cmin7/e
pitches = harmony.numbered_pitch_list
pitches.append(None)
phrases = []
phrase_stream = PhraseStream(phrases)
phrase_stream.make_extension(pitches, durations)

# make phrase two
harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("g' bf' c'' ef''"), 2) 
pitches = harmony.numbered_pitch_list
pitches.append(None)
phrase_stream.make_extension(pitches, durations)

# make phrase three
harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("bf' c'' ef'' g''"), 3)   
pitches = harmony.numbered_pitch_list
pitches.append(None)
phrase_stream.make_extension(pitches, durations)

# make phrase four
harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("c'' ef'' g'' bf''"), 0)
pitches = harmony.numbered_pitch_list
pitches.append(None) 
phrase_stream.make_extension(pitches, durations)

list_phrases = phrase_stream.phrases
print("list phrase :", list_phrases)
containers = phrase_stream.containers
print("phrase stream components :", containers)

class TestScoreTemplate:

    def __call__(self):
        # make first violin voice and staff
        first_violin_voice = abjad.Voice(name="Violin_Music_Voice")
        first_violin_staff = abjad.Staff(
        [first_violin_voice], name="First Violin Staff"
        )
        score = abjad.Score([first_violin_staff], name ="Test Score")
        return score

def make_test_lilypond_file():
    """
    makes a test ly file
    """
    score_template = TestScoreTemplate()
    score = score_template()
    phrase_outflow = PhraseOutflow()
    phrase_outflow.instrument_name = "Violin"
    phrase_outflow.phrases = list_phrases 
    phrase_outflow(score)
    lilypond_file = abjad.LilyPondFile.new(score)
    return lilypond_file

ly_file = make_test_lilypond_file()
abjad.f(ly_file)
