import abjad
import copy
import rill
import mccartney 

from abjadext import rmakers 

class PhraseCatcher(abjad.Container):
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

    def route_phrase(self):
        """
        Makes voices from phrases
        """
        phrase_definition = PhraseCatcher()
        self._phrases.append(phrase_definition)

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
    score_template = rill.ScoreTemplate()
    segment_maker = SegmentMaker()
    abjad.f(segment_maker)
