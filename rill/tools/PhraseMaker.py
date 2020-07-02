import abjad 

class PhraseMaker(object):
    """
    Makes a musical phrase by combining
    pitches from a harmony and durations

    Single slot is a container

    This class is purely for modifying the container
    i.e. populating it with music
    """

    ### INITIALIZER ###

    def __init__(self, container=None):
        self._container = container

    def __format__(self, format_specification="") -> str:
        """
        Formats phrase.
        """
        return abjad.StorageFormatManager(self).get_storage_format()
    
    def _extend_container(self, selection):
        self._container.extend(selection)
    
    ### PUBLIC METHODS ###

    def make_notes(self, pitches, durations):
        """Returns a container with leaves"""
        maker = abjad.LeafMaker()
        leaves = maker(pitches, durations)
        self._extend_container(leaves)
        
    @property
    def container(self):
        """Gets container"""
        return self._container

class PhraseStream(object):
    """Interface to aggregate a list of phrases
    Phrases are stored as containers
    Basically a list object with an added make and store functionality
    """
    def __init__(self, phrases=[]):
        self._phrases = phrases
    
    def make_extension(self, pitches, durations):
        """Collects a number of phrase containers into a list"""
        container = abjad.Container()
        phrase_maker = PhraseMaker(container)
        phrase_maker.make_notes(pitches, durations)
        made_phrase = phrase_maker.container
        self._add_to_list(made_phrase)

    def _add_to_list(self, phrase):
        self._phrases.append(phrase)

    @property
    def phrases(self):
        """Gets phrases as list"""
        return self._phrases

    @property
    def components(self) -> abjad.Component:
        """
        Gets stream as abjad components
        """
        self._components = []
        for phrase in self._phrases:
            self._components.append(phrase)
        return self._components 

class PhraseOutflow(object):
    """Has an outlet to connect a phrase stream to a score
    Routes phrases to voice by instrument name
    Can be called from a segment maker during the
    make process. 
    """

    def __init__(self):
        self._instrument_name = None
        self._phrases = []

    def __call__(self, score):
        """Calls phrase outflow
        routes phrases by instrument name (voice) in score
        returns none
        """
        self._score = score
        self._route_phrases()

    def __format__(self, format_specification="") -> str:
        return abjad.StorageFormatManager(self).get_storage_format()

    def _route_phrases(self):
        voice = self._score[f"{self.instrument_name}_Music_Voice"]
        for phrase in self._phrases:
            print("appending phrase :", phrase)
            voice.append(phrase)
    
    @property 
    def components(self):
        """Gets stream components"""
        self._components = []
        for phrase in self._phrases:
            self._components.append(phrase.components)

    @property 
    def instrument_name(self) -> str:
        """
        Gets instrument name
        """
        return self._instrument_name

    @instrument_name.setter
    def instrument_name(self, name):
        """
        Sets instrument name
        """
        self._instrument_name = name


    @property
    def phrases(self) -> list:
        """
        Gets list of phrases
        """
        return self._phrases

    @phrases.setter
    def phrases(self, phrase_list):    
        """
        Sets list of phrases
        """
        self._phrases = phrase_list


    if __name__ == '__main__':
    import rill.tools.FuzzyHarmony as FuzzyHarmony
    import rill.tools.PhraseMaker as PhraseMaker

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
    components = phrase_stream.components
    print("phrase stream components :", components)

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
        Makes a test ly file
        """
        score_template = TestScoreTemplate()
        score = score_template()
        phrase_outflow = PhraseOutflow(instrument_name="Violin", phrases=list_phrases)
        phrase_outflow(score)
        lilypond_file = abjad.LilyPondFile.new(score)
        return lilypond_file

    ly_file = make_test_lilypond_file()
    abjad.f(ly_file)
