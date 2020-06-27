import abjad
import copy
import rill
import mccartney 

from abjadext import rmakers 

class PhraseCatcher(abjad.Component):
    """
    Aggregates PhraseMaker objects
    Allocates one voice per PhraseMaker
    
    Voices organized by instrument name (rh / lh for piano)
    
    e.g.: "{}_.Music_Voice".format(instrument_name)
    can be: Violin_Music_Voice
    
    check via ScoreTemplate getter: .voice_abbreviations
    Returns an ordered dictionary

    Called from SegmentMaker and helps to produce lilypond file
    """

    def __init__(self, instrument_name=None, phrases=None):
        self.instrument_name = instrument_name
        self.phrases = phrases

    def __call__(self, score):
        """
        Routes phrase to voice in score
        Returns none
        """
        self._score = score
        self._route_phrases()

    def __format__(self, format_specification="") -> str:
        return abjad.StorageFormatManager(self).get_storage_format()

    def _get_music_voices(self):
        return(
                self._score["Violin_Music_Voice"],
                self._score["Monosynth_Music_Voice"],
                self._score["RH_I_Music_Voice"],
                self._score["LH_I_Muisc_Voice"],
            )

    def _route_phrases(self):
        voice = self._score[f"{self.instrument_name}_Music_Voice"]
        for argument in self.phrases:
            if isinstance(argument, abjad.Component):
                print("I can see your phrases")
                copied_expr = copy.deepcopy(argument)
                voice.append(copied_expr)
            else:
                raise ValueError(f"what is {argument!r}?")

class SegmentMaker(abjad.SegmentMaker):
    
    def __init__(
            self, name=None, time_signatures=None,
        ):
            super(SegmentMaker, self).__init__()
            self._lilypond_file = None
            self._phrases = []
            self.name= name
            self.tempo = ((1, 4), 60)
            self.time_signatures = time_signatures or []

    @property 
    def _music_voices(self):
        return(
                self._score["Violin_Music_Voice"],
                self._score["Monosynth_Music_Voice"],
                self._score["RH_I_Music_Voice"],
                self._score["LH_I_Music_Voie"],
            )

    def _call_phrases(self):
        for phrase in self._phrases:
            phrase(self._score)

    def _make_lilypond_file(self, midi=False):
        path = abjad.Path('rill', 'stylesheets', 'contexts.ily')
        lilypond_file = abjad.LilyPondFile.new(
                music=self._score, includes=[path], use_relative_includes=True
                )
        delattr(lilypond_file.header_block, "tagline")
        for item in lilypond_file.items[:]:
            if getattr(item, "name", None) in ("layout", "paper"):
                lilypond_file.items.remove(item)
        self._lilypond_file = lilypond_file

    def _make_score(self):
        template = rill.ScoreTemplate()
        score = template()
        self._score = score
    
    @property
    def metadata(self):
        """
        Gets metadata after run
        """
        return self._metadata

    def route_phrases(self, phrase_catcher):
        """
        Makes voices from phrases
        """
        self._phrases.append(phrase_catcher)

    def run(
            self,
            metadata=None,
            persist=None,
            previous_metadata=None,
            previous_persist=None,
            segment_directory=None,
    ):
        """
        Runs segment maker
        
        Returns Lilypond file
        """
        self._metadata = abjad.OrderedDict(metadata)
        self._persist = abjad.OrderedDict(persist)
        self._previous_metadata = abjad.OrderedDict(previous_metadata)
        self._previous_persist = abjad.OrderedDict(previous_persist)
        self._segment_directory = segment_directory
        self._make_score()
        self._make_lilypond_file()
        self._call_phrases()
        return self._lilypond_file

if __name__ == '__main__':
    import rill.tools.FuzzyHarmony as FuzzyHarmony
    import rill.tools.PhraseMaker as PhraseMaker
    
    caught_phrases = []
    # make phrase one 
    harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("ef' g' bf' c''"), 1) # cmin7/e
    container = abjad.Container()
    durations = [2, 3, 3, 6, 2]
    denominator = 4
    divisions = [(4, 4)] * 5
    pitches = harmony.pitch_list
    phrase_one = PhraseMaker(container)
    phrase_one.make_phrase(durations, denominator, divisions, pitches)
    caught_phrases.append(phrase_one)

    # make phrase two
    harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("g' bf' c'' ef''"), 2) 
    container = abjad.Container()
    pitches = harmony.pitch_list
    phrase_two = PhraseMaker(container)
    phrase_two.make_phrase(durations, denominator, divisions, pitches)
    caught_phrases.append(phrase_two)

    # make phrase three
    harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("bf' c'' ef'' g''"), 3)   
    container = abjad.Container()
    pitches = harmony.pitch_list
    phrase_three = PhraseMaker(container)
    phrase_three.make_phrase(durations, denominator, divisions, pitches)
    caught_phrases.append(phrase_three)

     # make phrase four
    harmony = FuzzyHarmony('bf_ii', abjad.PitchSegment("c'' ef'' g'' bf''"), 0)
    container = abjad.Container()
    pitches = harmony.pitch_list
    phrase_four = PhraseMaker(container)
    phrase_four.make_phrase(durations, denominator, divisions, pitches)
    caught_phrases.append(phrase_four)
    
    #abjad.f(phrase_catcher)

    score = rill.ScoreTemplate()
    segment_maker = SegmentMaker(
            name='Test',
            time_signatures = 20 * [(4, 4)]
            )

    phrase_catcher = PhraseCatcher()
    phrase_catcher.instrument_name = 'Violin'
    phrase_catcher.phrases = caught_phrases
    segment_maker.route_phrases(phrase_catcher)
   
    lilypond_file = segment_maker.run()
    abjad.f(lilypond_file)



